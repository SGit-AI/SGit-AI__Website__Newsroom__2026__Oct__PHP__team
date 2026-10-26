#!/usr/bin/env python3
"""The indexes the team's pages read when they load, written into the served tree at deploy (never committed).

    python3 tools/index.py --into _site [--commit <sha>]

A static host cannot list a folder, and a page should not make 349 requests for 349 board rows, so the deploy writes one
file per collection beside the records it is made of: records/index/board.json is every records/board/<id>.json, in
board order (a row's order field, then the rows written since the split, by file name). The records stay the source: an
agent writes its row and releases team, and the page shows it at the next deploy, a minute or two later, with no build
anywhere else. Nothing is copied from another repository. No clock: the same records give the same bytes.
"""
import argparse, glob, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def board():
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'records', 'board', '*.json'))):
        r = json.load(open(p, encoding='utf-8'))
        row = {k: r[k] for k in ('id', 'title', 'status', 'owner', 'note', 'version') if k in r}
        rows.append(((0, r['order'], '') if isinstance(r.get('order'), int) else (1, 0, os.path.basename(p)), row))
    return [row for _, row in sorted(rows, key=lambda x: x[0])]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--into', required=True); ap.add_argument('--commit', default='')
    a = ap.parse_args()
    out = os.path.join(os.path.abspath(a.into), 'records', 'index')
    os.makedirs(out, exist_ok=True)
    rows = board()
    with open(os.path.join(out, 'board.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'about': 'Every board row, from records/board/ in SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team, written at deploy.',
                   'commit': a.commit, 'rows': rows}, f, ensure_ascii=False, indent=1); f.write('\n')
    print(f'index: board {len(rows)} rows')


if __name__ == '__main__':
    sys.exit(main())
