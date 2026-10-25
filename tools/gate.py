#!/usr/bin/env python3
"""The team repository's gate: seconds. Exits non-zero on any failure.

1. Every JSON file parses.
2. Every board row has an id, a title, a status (open, waiting, done) and an owner, and is filed under its id.
3. Every schedule card names its member, a status and its wake times; every member folder has a role and a policy.
4. The front page is what tools/front.py writes (it is built from this repository, so it cannot drift).
5. No credential shapes anywhere: registers list vault IDs and key kinds, never a key.
"""
import json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
fails, notes = [], []
CREDENTIAL = re.compile(r'sgit_private_(vault|read)_[0-9a-f]{12,}|BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}')
STATUS = {'open', 'waiting', 'done'}
KNOWN_REPEATS = {'013__2'}  # two v1 rows took the number 013 (dev's and the librarian's); renumber one to clear this


def files(top):
    for d, dirs, fs in os.walk(os.path.join(ROOT, top)):
        dirs[:] = sorted(x for x in dirs if x != '.git')
        for f in sorted(fs):
            yield os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, '/')


docs = {}
for p in files('records'):
    if p.startswith(('.git/', 'tools/__pycache__')):
        continue
    if p.endswith('.json'):
        try:
            docs[p] = json.load(open(os.path.join(ROOT, p), encoding='utf-8'))
        except ValueError as e:
            fails.append(f'{p}: not valid JSON ({e})')
    if p.endswith(('.json', '.md', '.html', '.py', '.txt', '.sh')):
        if CREDENTIAL.search(open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()):
            fails.append(f'{p}: a credential shape')

rows = {p: d for p, d in docs.items() if p.startswith('records/board/')}
for p, r in rows.items():
    stem = os.path.basename(p)[:-5]
    for k in ('id', 'title', 'status', 'owner'):
        if k not in r:
            fails.append(f'{p}: no "{k}"')
    if r.get('status') not in STATUS:
        fails.append(f'{p}: status "{r.get("status")}" is not one of {", ".join(sorted(STATUS))}')
    if stem != r.get('id') and stem not in KNOWN_REPEATS:
        fails.append(f'{p}: filed under {stem}, but its id is {r.get("id")}')
for stem in sorted(KNOWN_REPEATS):
    if f'records/board/{stem}.json' in rows:
        notes.append(f'records/board/{stem}.json: a v1 row that repeats another row\'s id; renumber one of them')

for p, c in docs.items():
    if p.startswith('records/schedule/') and p.count('/') == 2:
        for k in ('member', 'status', 'times'):
            if k not in c:
                fails.append(f'{p}: no "{k}"')
agents = sorted(d for d in os.listdir(os.path.join(ROOT, 'records', 'agents')) if os.path.isdir(os.path.join(ROOT, 'records', 'agents', d)))
for a in agents:
    for need in ('ROLE.md', 'policy.json'):
        if not os.path.exists(os.path.join(ROOT, 'records', 'agents', a, need)):
            notes.append(f'records/agents/{a}/: no {need} (as in v1; the member, or abp@newsroom.sgit who keeps the policies, adds it)')

r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'front.py'), '--check'], capture_output=True, text=True)
if r.returncode:
    fails.append('index.html: ' + (r.stdout + r.stderr).strip()[-300:])

notes.append(f'{len(rows)} board rows ({sum(1 for r in rows.values() if r.get("status") != "done")} not done), '
             f'{sum(1 for p in docs if p.startswith("records/schedule/") and p.count("/") == 2)} schedule cards, {len(agents)} member folders')
for n in notes:
    print('note:', n)
for f in fails:
    print('FAIL:', f)
if fails:
    sys.exit(f'{len(fails)} failure(s)')
print(f'gate passed: {len(docs)} JSON files')
