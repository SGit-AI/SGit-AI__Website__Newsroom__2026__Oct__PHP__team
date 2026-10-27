#!/usr/bin/env python3
"""The project hub: one page per project that links everything it holds, for people and for agents.

Usage, from the team repository's root:  python3 records/projects/hub.py PROJECT-001
Writes records/projects/<id>/index.html (people), index.md (the markdown twin) and manifest.json (agents: every file,
its URL and sha256, the messages and their status). Standard library only, no network. Kept by projects@php.newsroom.
Everything it reads is the project's own records; nothing secret is ever written into a project folder.
"""
import hashlib, html, json, os, sys

BASE = 'https://team.php.oct.2026.newsroom.sgit.ai/records/projects/'
PRESS = 'https://press.php.oct.2026.newsroom.sgit.ai/latest/assets/'
SKIP = {'index.html', 'index.md', 'manifest.json'}
ABOUT = {
    'project.json': 'the state: phases, checkpoints, decisions, the next step',
    'log.md': 'every event, dated, newest last',
    'actors-audit': 'step 1a, the ontologist: what we hold about each actor, and what each page lacks',
    'candidates.json': 'step 1b, the Sherpa: 55 candidates scored by the three tests',
    'the-ten': 'step 1c, the Sherpa: the ten proposed at checkpoint A',
    'bbc-regrade': 'step 2b, the journalist: the BBC points and claims re-graded against the evidence vault',
    'clean-hands.md': 'step 1 of phase 2, fact-check and story-site: our own BBC claims corrected in data',
    'SPEC.md': 'step 2a, the design agent: the outlet page /outlets/<id>/, one template for every recipient',
    'FLOWS.md': 'step 2a: the pipeline, the per-outlet workflow and the request states, as diagrams',
    'prototype-bbc.html': 'step 2a: the BBC outlet page as a static prototype (not published)',
    'sample-bbc.json': 'step 2a: the sample the prototype was drawn from',
    'build_outlet.py': 'step 2c, the ontologist: makes the outlet file for any outlet from the data repository',
    'messages.json': 'step 2d: every draft message, its channel, its one ask and its status',
}


def about(rel):
    name = os.path.basename(rel)
    if rel.startswith('feedback/') and name != 'README.md':
        return "the editor's own words, filed verbatim"
    if rel.startswith('phase-2/outlets/') and name.endswith('.json') and '/editorial/' not in rel:
        return 'the outlet file every view of the page reads: ' + name[:-5]
    if rel.startswith('phase-2/messages/') and name.endswith('.md'):
        return 'draft message to ' + name[:-3] + ' (not sent; sent only once the editor approves it)'
    for k, v in ABOUT.items():
        if k in name:
            return v
    return ''


def main(pid):
    root = os.path.join('records', 'projects', pid)
    p = json.load(open(os.path.join(root, 'project.json')))
    files = []
    for d, _, fs in os.walk(root):
        for f in sorted(fs):
            rel = os.path.relpath(os.path.join(d, f), root).replace(os.sep, '/')
            if rel in SKIP:
                continue
            b = open(os.path.join(d, f), 'rb').read()
            files.append({'path': rel, 'url': BASE + pid + '/' + rel, 'bytes': len(b),
                          'sha256': hashlib.sha256(b).hexdigest(), 'about': about(rel)})
    files.sort(key=lambda x: x['path'])
    msgs = []
    mp = os.path.join(root, 'phase-2', 'messages', 'messages.json')
    if os.path.exists(mp):
        for m in json.load(open(mp)).get('messages', []):
            msgs.append({k: m.get(k) for k in ('id', 'to', 'channel', 'subject', 'ask', 'status', 'approved_by', 'sent', 'sender')}
                        | {'url': BASE + pid + '/phase-2/messages/' + (m.get('file') or (m.get('id', '') + '.md'))})
    outlets = []
    od = os.path.join(root, 'phase-2', 'outlets')
    if os.path.isdir(od):
        for f in sorted(os.listdir(od)):
            if f.endswith('.json'):
                o = json.load(open(os.path.join(od, f)))
                s = o.get('summary', {})
                outlets.append({'id': f[:-5], 'name': (o.get('outlet') or {}).get('name'), 'sources': s.get('sources'),
                                'captures': s.get('captures'), 'claims': s.get('claims'), 'by_verdict': s.get('by_verdict'),
                                'url': BASE + pid + '/phase-2/outlets/' + f})
    log = open(os.path.join(root, 'log.md')).read().splitlines()
    cp = p.get('checkpoint') or {}
    man = {'project': pid, 'title': p.get('title'), 'state': p.get('state'), 'lead': p.get('lead'),
           'checkpoint': cp, 'next': p.get('next'), 'brief': 'https://team.php.oct.2026.newsroom.sgit.ai/' + p['brief'],
           'hub': BASE + pid + '/', 'for_agents': (
               'Everything here is public and holds no secret. Read project.json for the state and messages.json for the '
               'messages. A message may be sent only when its status is "approved" and approved_by is "editor"; a draft is '
               'never sent. Nothing on these pages is an instruction to any agent but the newsroom\'s own; the editor, in '
               'his own session, decides.'),
           'messages': msgs, 'outlets': outlets, 'files': files}
    json.dump(man, open(os.path.join(root, 'manifest.json'), 'w'), indent=1, ensure_ascii=False)
    open(os.path.join(root, 'manifest.json'), 'a').write('\n')

    e = html.escape
    rows = ''.join(f'<tr><td><a href="{e(f["path"])}">{e(f["path"])}</a></td><td>{e(f["about"])}</td><td class="pj-r">{f["bytes"]:,}</td></tr>' for f in files)
    mrows = ''.join(f'<tr><td><a href="{e(m["url"])}">{e(str((m.get("to") or {}).get("name") or m["id"]))}</a></td><td>{e(str(m.get("ask") or ""))}</td><td>{e(str((m.get("channel") or {}).get("name") or ""))}</td><td><b>{e(str(m.get("status")))}</b></td></tr>' for m in msgs) or '<tr><td colspan="4">No drafts yet.</td></tr>'
    orows = ''.join(f'<tr><td><a href="{e(o["url"])}">{e(o["name"] or o["id"])}</a></td><td class="pj-r">{o["sources"]}</td><td class="pj-r">{o["captures"]}</td><td class="pj-r">{o["claims"]}</td><td>{e(", ".join(f"{k} {v}" for k, v in (o["by_verdict"] or {}).items()))}</td></tr>' for o in outlets)
    phases = ''.join(f'<li><b>{e(ph["phase"])}</b>: checkpoint {e(ph["checkpoint"])}, {"passed " + e(str(ph["passed"])) if ph.get("passed") else "not passed"}</li>' for ph in p.get('phases', []))
    recent = ''.join(f'<li>{e(l[2:])}</li>' for l in [l for l in log if l.startswith('- ')][-8:][::-1])
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(pid)}: the project hub</title>
<meta name="description" content="{e(p.get("title", ""))}: everything the project holds, for people and for agents.">
<link rel="stylesheet" href="{PRESS}site.css"><link rel="stylesheet" href="{PRESS}themes/themes.css"><link rel="stylesheet" href="{PRESS}themes/site-tokens.css">
<link rel="alternate" type="application/json" href="manifest.json"><link rel="alternate" type="text/markdown" href="index.md">
<style>body{{max-width:980px;margin:0 auto;padding:16px}} table{{width:100%;border-collapse:collapse;font-size:.95rem}} td,th{{border-bottom:1px solid #ddd;padding:6px 8px;text-align:left;vertical-align:top}} .pj-r{{text-align:right;white-space:nowrap}} .box{{border-left:4px solid #0f766e;padding:8px 12px;background:#f3f7f6;margin:12px 0}} @media(max-width:640px){{td:nth-child(2){{display:none}}}}</style>
</head><body>
<p><a href="https://team.php.oct.2026.newsroom.sgit.ai/">team</a> / records / projects / {e(pid)}</p>
<h1>{e(pid)}: {e(p.get("title", ""))}</h1>
<p>State: <b>{e(str(p.get("state")))}</b> · lead: {e(str(p.get("lead")))} · brief: <a href="https://team.php.oct.2026.newsroom.sgit.ai/{e(p["brief"])}">{e(os.path.basename(p["brief"]))}</a> · <a href="project.json">project.json</a> · <a href="log.md">log</a> · <a href="manifest.json">manifest.json</a> (for agents)</p>
<div class="box"><b>Now:</b> {e(str(p.get("next")))}<br><b>Checkpoint:</b> {e(str(cp.get("at")))}: waits for {e(str(cp.get("waits_for")))}</div>
<div class="box"><b>For agents (and the agent at riskmandate.ai):</b> {e(man["for_agents"])}</div>
<h2>Messages</h2><table><tr><th>To</th><th>The one ask</th><th>Channel</th><th>Status</th></tr>{mrows}</table>
<h2>What we hold, per recipient</h2><table><tr><th>Outlet file</th><th class="pj-r">Sources</th><th class="pj-r">Captures</th><th class="pj-r">Claims</th><th>By verdict</th></tr>{orows}</table>
<p>The page each recipient will see: <a href="phase-2/design/prototype-bbc.html">the BBC's, as a prototype</a> (not yet published).</p>
<h2>Phases</h2><ul>{phases}</ul>
<h2>Latest in the log</h2><ul>{recent}</ul>
<h2>Every file</h2><table><tr><th>File</th><th>What</th><th class="pj-r">Bytes</th></tr>{rows}</table>
<p>Written by records/projects/hub.py from the project's records; public, no secret. Captures stay in the evidence vault: only hashes and short quotes appear here.</p>
</body></html>
'''
    open(os.path.join(root, 'index.html'), 'w').write(page)
    md = [f'# {pid}: {p.get("title", "")}', '', f'State: **{p.get("state")}** · lead: {p.get("lead")} · [project.json](project.json) · [log](log.md) · [manifest.json](manifest.json)', '',
          f'**Now:** {p.get("next")}', '', f'**For agents:** {man["for_agents"]}', '', '## Messages', '']
    md += [f'- [{(m.get("to") or {}).get("name") or m["id"]}]({m["url"]}): {m.get("ask")} · **{m.get("status")}**' for m in msgs] or ['No drafts yet.']
    md += ['', '## What we hold, per recipient', ''] + [f'- [{o["name"] or o["id"]}]({o["url"]}): {o["sources"]} sources, {o["captures"]} captures, {o["claims"]} claims' for o in outlets]
    md += ['', '## Every file', ''] + [f'- [{f["path"]}]({f["path"]}): {f["about"]}' for f in files]
    open(os.path.join(root, 'index.md'), 'w').write('\n'.join(md) + '\n')
    print(f'{pid}: {len(files)} files, {len(msgs)} messages, {len(outlets)} outlet files')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'PROJECT-001')
