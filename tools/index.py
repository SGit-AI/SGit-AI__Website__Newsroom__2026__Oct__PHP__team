#!/usr/bin/env python3
"""The indexes the team's pages read when they load, written into the served tree at deploy (never committed).

    python3 tools/index.py --into _site [--commit <sha>]

A static host cannot list a folder, and a page should not make 349 requests for 349 board rows, so the deploy writes one
file per collection beside the records it is made of, under records/index/:

  board.json      every records/board/<id>.json, in board order (a row's order field, then newer rows by file name)
  schedule.json   every card (records/schedule/<agent>.json), by agent
  runs.json       every run record (records/runs/<agent>/<run>.json), newest first
  messages.json   every message (records/messages/<to>/<id>.md: front matter and body), newest first, each with the run
                  that first read it
  registers.json  every register (records/registers/<agent>.json): vault IDs and kinds of key, never a key
  agents.json     every member folder (records/agents/<id>/): its status.json and its debriefs (front matter and text),
                  newest first

A record that cannot be read is left out and named in that file's "skipped" (the gate refuses it at push time; a deploy
never fails on one). The records stay the source: an
agent writes its row and releases team, and the page shows it at the next deploy, a minute or two later, with no build
anywhere else. Nothing is copied from another repository. No clock: the same records give the same bytes.
"""
import argparse, glob, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def board():
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'records', 'board', '*.json'))):
        r = json.load(open(p, encoding='utf-8'))
        row = {k: r[k] for k in ('id', 'title', 'status', 'owner', 'note', 'version') if k in r}
        rows.append(((0, r['order'], '') if isinstance(r.get('order'), int) else (1, 0, os.path.basename(p)), row))
    return [row for _, row in sorted(rows, key=lambda x: x[0])]


def load(pattern):
    out, skipped = [], []
    for p in sorted(glob.glob(os.path.join(ROOT, pattern))):
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        try:
            d = json.load(open(p, encoding='utf-8'))
            if not isinstance(d, dict): raise ValueError('not an object')
            out.append(d)
        except ValueError as e:
            skipped.append(f'{rel}: {str(e)[:80]}')
    return out, skipped


def message(p):
    """The build's sched_message: front matter (from, to, sent, subject, re) and the body; box is the folder it is in."""
    m = re.match(r'---\n(.*?)\n---\n(.*)', open(p, encoding='utf-8').read(), re.S)
    if not m: raise ValueError('no front matter')
    head = {k.strip(): v.strip() for k, v in (l.split(':', 1) for l in m.group(1).splitlines() if ':' in l)}
    miss = [k for k in ('from', 'to', 'sent', 'subject') if not head.get(k)]
    if miss: raise ValueError('missing ' + ', '.join(miss))
    return {k: head[k] for k in ('from', 'to', 'sent', 'subject', 're') if head.get(k)} | {
        'id': os.path.basename(p)[:-3], 'box': os.path.basename(os.path.dirname(p)), 'body': m.group(2).strip()}


def collections():
    cards, cskip = load('records/schedule/*.json')
    runs, rskip = load('records/runs/*/*.json')
    runs = [r for r in runs if isinstance(r.get('started'), str) and isinstance(r.get('run'), str)]
    runs.sort(key=lambda r: (r['started'], r['run']), reverse=True)
    first = {}
    for r in reversed(runs):
        for i in r.get('read') or []:
            first.setdefault(i, r['run'])
    msgs, mskip = [], []
    for p in sorted(glob.glob(os.path.join(ROOT, 'records', 'messages', '*', '*.md'))):
        try:
            m = message(p); m['read_in'] = first.get(m['id']); msgs.append(m)
        except (ValueError, UnicodeDecodeError) as e:
            mskip.append(f'{os.path.relpath(p, ROOT)}: {str(e)[:80]}')
    msgs.sort(key=lambda m: m['id'], reverse=True)
    regs, gskip = load('records/registers/*.json')
    members, askip = agents()
    return {'agents': ('agents', members, askip), 'schedule': ('cards', sorted(cards, key=lambda c: str(c.get('agent'))), cskip), 'runs': ('runs', runs, rskip),
            'messages': ('messages', msgs, mskip), 'registers': ('registers', regs, gskip)}


def debrief(p):
    """The build's load_debriefs: front matter (key: value lines) and the markdown text."""
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', open(p, encoding='utf-8').read(), re.S)
    if not m: raise ValueError('no front matter')
    meta = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^(\w+):\s*(.*)$', line)
        if kv: meta[kv.group(1)] = kv.group(2)
    return meta | {'file': os.path.basename(p), 'text': m.group(2)}


def agents():
    out, skipped = [], []
    top = os.path.join(ROOT, 'records', 'agents')
    for a in sorted(d for d in os.listdir(top) if os.path.isdir(os.path.join(top, d))):
        sp, status = os.path.join(top, a, 'status.json'), None
        if os.path.exists(sp):
            try: status = json.load(open(sp, encoding='utf-8'))
            except ValueError as e: skipped.append(f'records/agents/{a}/status.json: {str(e)[:80]}')
        dbs = []
        for p in sorted(glob.glob(os.path.join(top, a, 'debriefs', '*.md'))):
            try: dbs.append(debrief(p))
            except (ValueError, UnicodeDecodeError) as e: skipped.append(f'{os.path.relpath(p, ROOT)}: {str(e)[:80]}')
        dbs.sort(key=lambda x: (x.get('date', ''), x['file']), reverse=True)
        out.append({'agent': a, 'status': status, 'debriefs': dbs})
    return out, skipped


def write(out, name, data):
    with open(os.path.join(out, name + '.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=1); f.write('\n')   # each record's keys in its own order, as the build reads them


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--into', required=True); ap.add_argument('--commit', default='')
    a = ap.parse_args()
    out = os.path.join(os.path.abspath(a.into), 'records', 'index')
    os.makedirs(out, exist_ok=True)
    rows = board()
    with open(os.path.join(out, 'board.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'about': 'Every board row, from records/board/ in SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team, written at deploy.',
                   'commit': a.commit, 'rows': rows}, f, ensure_ascii=False, indent=1); f.write('\n')
    said = [f'board {len(rows)} rows']
    for name, (key, items, skipped) in collections().items():
        write(out, name, {'about': f'Every {name} record, from records/ in SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team, written at deploy.',
                          'commit': a.commit, key: items, 'skipped': skipped})
        said.append(f'{name} {len(items)}' + (f' ({len(skipped)} skipped)' if skipped else ''))
    print('index: ' + ', '.join(said))


if __name__ == '__main__':
    sys.exit(main())
