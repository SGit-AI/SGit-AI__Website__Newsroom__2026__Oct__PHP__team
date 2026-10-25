#!/usr/bin/env python3
"""Copy the newsroom's own operations from the v1 repository into this one.

    python3 tools/import_v1.py --from ../sgit-ai__website__newsroom__2026__oct__php

Until the cutover, v1 is where the agents write: this copies it here, every file byte for byte, except the board,
which it splits into one file per row (board/<id>.json), so that two agents adding rows never touch the same file.
It records the v1 commit it read. Everything it writes is under records/; the site's pages, which the press
partitions from v1, are served at the root beside it. After the cutover the agents write here and this tool is retired.
"""
import argparse, json, os, shutil, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# v1 path -> path here; a path ending in / is a folder, copied whole
COPY = [
    ('data/schedule/', 'records/schedule/'),
    ('data/runs/', 'records/runs/'),
    ('data/messages/', 'records/messages/'),
    ('data/vault-register/', 'records/registers/'),
    ('admin/content/agents/', 'records/agents/'),
    ('admin/content/briefs/', 'records/briefs/'),
    ('admin/sherpa/', 'records/sherpa/'),
    ('data/synthetic-runs/', 'records/synthetic/runs/'),
    ('admin/schedule/WAKE.md', 'records/WAKE.md'),
    ('data/team.json', 'records/data/team.json'),
    ('data/agents-status.json', 'records/data/agents-status.json'),
    ('data/schedules.json', 'records/data/schedules.json'),
    ('data/scheduled-tasks.json', 'records/data/scheduled-tasks.json'),
    ('data/comms.json', 'records/data/comms.json'),
    ('data/contributors.json', 'records/data/contributors.json'),
    ('data/collaborators.json', 'records/data/collaborators.json'),
    ('data/control.json', 'records/data/control.json'),
    ('data/advisories.json', 'records/data/advisories.json'),
    ('data/appsec.json', 'records/data/appsec.json'),
    ('data/synthetic.json', 'records/synthetic/synthetic.json'),
    ('data/versions.json', 'records/history/v1-versions.json'),
    ('data/release-pages.json', 'records/history/v1-release-pages.json'),
]


def git(v1, *a):
    return subprocess.run(['git', '-C', v1, *a], capture_output=True, text=True, check=True).stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from', dest='v1', required=True)
    v1 = os.path.abspath(ap.parse_args().v1)
    if git(v1, 'status', '--porcelain', '--', 'data', 'admin/content', 'admin/sherpa', 'admin/schedule'):
        sys.exit('import: the v1 clone has uncommitted changes; import from a released commit')
    for src, dst in COPY:
        s, d = os.path.join(v1, src.rstrip('/')), os.path.join(ROOT, dst.rstrip('/'))
        if not os.path.exists(s):
            sys.exit(f'import: {src} is not in v1')
        if src.endswith('/'):
            shutil.rmtree(d, ignore_errors=True)
            shutil.copytree(s, d)
        else:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copyfile(s, d)
    # the board: one file per row, in the order v1 lists them; a repeated id (two rows took the same number) is kept,
    # filed as <id>__2.json, and named by the gate until someone renumbers one of them
    admin = json.load(open(os.path.join(v1, 'data', 'admin.json'), encoding='utf-8'))
    bdir = os.path.join(ROOT, 'records', 'board')
    shutil.rmtree(bdir, ignore_errors=True); os.makedirs(bdir)
    seen = {}
    for order, row in enumerate(admin['board']):
        n = seen.get(row['id'], 0) + 1; seen[row['id']] = n
        name = row['id'] if n == 1 else f'{row["id"]}__{n}'
        with open(os.path.join(bdir, f'{name}.json'), 'w', encoding='utf-8', newline='\n') as f:
            json.dump({**row, 'order': order}, f, ensure_ascii=False, indent=1); f.write('\n')
    with open(os.path.join(ROOT, 'records', 'data', 'roles.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'about': 'The roles of the newsroom, as v1 data/admin.json kept them.', 'roles': admin['roles']}, f, ensure_ascii=False, indent=1); f.write('\n')
    commit = git(v1, 'rev-parse', 'HEAD')
    version = open(os.path.join(v1, 'VERSION'), encoding='utf-8').read().strip()
    with open(os.path.join(ROOT, 'records', 'imported.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'from': {'repository': 'SGit-AI/sgit-ai__website__newsroom__2026__oct__php', 'commit': commit, 'site_version': version},
                   'board_rows': len(admin['board'])}, f, indent=1); f.write('\n')
    print(f'imported from v1 at {commit[:12]} (site v{version}): {len(admin["board"])} board rows, {len(COPY)} paths')


if __name__ == '__main__':
    main()
