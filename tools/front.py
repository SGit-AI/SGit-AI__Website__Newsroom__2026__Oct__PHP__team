#!/usr/bin/env python3
"""index.html: the team site's front page, built from this repository alone (no clock, no network).

    python3 tools/front.py           write index.html
    python3 tools/front.py --check   exit 1 if index.html is not what this would write

A plain page until the press's layout is published: who is on the team, what runs on a schedule and when, what is on
the board and whose it is. The full team pages (the control room, each member's page, the runs) move here with the
press's v1.0.0.
"""
import html, json, os, sys
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
E = lambda s: html.escape(str(s if s is not None else ''), quote=True)
GH = 'https://github.com/SGit-AI/sgit-ai__website__newsroom__2026__oct__php__team'


def load(p):
    return json.load(open(os.path.join(ROOT, p), encoding='utf-8'))


def page():
    imp = load('tools/imported.json')
    board = [load(f'board/{f}') for f in sorted(os.listdir(os.path.join(ROOT, 'board')))]
    board.sort(key=lambda r: r.get('order', 0))
    by = defaultdict(Counter)
    for r in board:
        by[r['owner']][r['status']] += 1
    owners = sorted(by, key=lambda o: (-sum(by[o][s] for s in ('open', 'waiting')), o))
    brow = ''.join(f'<tr><td>{E(o)}</td><td>{by[o]["open"]}</td><td>{by[o]["waiting"]}</td><td>{by[o]["done"]}</td></tr>' for o in owners)
    cards = []
    for f in sorted(os.listdir(os.path.join(ROOT, 'schedule'))):
        if f.endswith('.json'):
            c = load(f'schedule/{f}')
            cards.append(f'<tr><td><a href="{GH}/blob/dev/schedule/{E(f)}">{E(c.get("member") or f[:-5])}</a></td><td>{E(c.get("status"))}</td><td>{E(", ".join(c.get("times") or []))}</td><td>{E((c.get("objective") or "")[:140])}</td></tr>')
    members = sorted(d for d in os.listdir(os.path.join(ROOT, 'agents')) if os.path.isdir(os.path.join(ROOT, 'agents', d)))
    mlist = ' &middot; '.join(f'<a href="{GH}/tree/dev/agents/{E(m)}">{E(m)}</a>' for m in members)
    waiting = ''.join(f'<li><b>{E(r["id"])}</b> ({E(r["owner"])}): {E(r["title"][:160])}</li>' for r in board if r['status'] == 'waiting')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PHP October 2026: the team</title>
<style>:root{{color-scheme:light dark}}body{{font:15px/1.5 system-ui,sans-serif;max-width:980px;margin:0 auto;padding:16px}}table{{border-collapse:collapse;width:100%;font-size:14px}}
td,th{{text-align:left;padding:.3rem .5rem;border-bottom:1px solid #8884;vertical-align:top}}.tw{{overflow-x:auto}}</style></head>
<body>
<h1>PHP October 2026: the team</h1>
<p>The newsroom's own operations for <a href="https://php.oct.2026.newsroom.sgit.ai/">php.oct.2026.newsroom.sgit.ai</a>: the board, the schedule, the run records, the messages, every member's role, policy, status and debriefs, the vault registers and the briefs. Imported from the site's repository at <code>{E(imp["from"]["commit"][:12])}</code> (site v{E(imp["from"]["site_version"])}) until the cutover; then written here. Source: <a href="{GH}">{E(GH.rsplit("/", 1)[1])}</a>.</p>
<h2>Waiting on someone</h2>
<ul>{waiting or "<li>Nothing.</li>"}</ul>
<h2>The board, by owner</h2>
<p>{len(board)} rows, one file each in <a href="{GH}/tree/dev/board">board/</a>.</p>
<div class="tw"><table><thead><tr><th>Owner</th><th>Open</th><th>Waiting</th><th>Done</th></tr></thead><tbody>{brow}</tbody></table></div>
<h2>On a schedule</h2>
<div class="tw"><table><thead><tr><th>Member</th><th>Status</th><th>Wakes (London)</th><th>Objective</th></tr></thead><tbody>{"".join(cards)}</tbody></table></div>
<h2>Members</h2>
<p>{mlist}</p>
</body></html>
'''


if __name__ == '__main__':
    out = page()
    p = os.path.join(ROOT, 'index.html')
    if '--check' in sys.argv[1:]:
        if not os.path.exists(p) or open(p, encoding='utf-8').read() != out:
            sys.exit('not what tools/front.py writes; run python3 tools/front.py')
    else:
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(out)
        print('wrote index.html')
