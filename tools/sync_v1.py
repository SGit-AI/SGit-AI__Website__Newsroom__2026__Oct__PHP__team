#!/usr/bin/env python3
"""The records, both ways between this repository and v1, while v1 still builds the pages (step A of the split).

    python3 tools/sync_v1.py import --from ../sgit-ai__website__newsroom__2026__oct__php   # v1 -> records/, never over a change made here
    python3 tools/sync_v1.py export --into ../sgit-ai__website__newsroom__2026__oct__php   # records/ -> v1, what changed here since the last import

The rule: **what is written here wins.** records/imported.json keeps the sha256 of every file the last import wrote.
A file whose sha256 differs from that record was written here since; the import leaves it alone and says so, and the
export carries it into v1 (its path, or its row in data/admin.json's board), where v1's gate and release take it to the
pages. A file not in the record is new here (a board row `dev-0001.json`, a run record): kept, exported. After v1
releases, the next import finds the same bytes and records them, and the two agree again.

The board: one file per row here, `records/board/<id>.json`, with an `order` field (v1's position; a new row here has
none and goes to the end). A row written here replaces v1's row with the same id, or is appended. Rows v1 renumbered or
removed are not followed once the file here has been written since.
"""
import argparse, hashlib, json, os, shutil, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RECORD = os.path.join(ROOT, 'records', 'imported.json')

# v1 path -> path here; a path ending in / is a folder
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
    ('REALITY.md', 'records/REALITY.md'),                          # every member's own section
    ('BRIEF-CORRECTIONS.md', 'records/BRIEF-CORRECTIONS.md'),
    ('admin/factcheck/', 'records/desks/factcheck/'),               # the desks' working files, each its own
    ('admin/liaison/', 'records/desks/liaison/'),
    ('admin/observability/', 'records/desks/observability/'),
    ('admin/ontologist/', 'records/desks/ontologist/'),
    ('admin/wikipedia/', 'records/desks/wikipedia/'),
    ('admin/synthetic/', 'records/desks/synthetic/'),
    ('review/', 'records/desks/review/'),
]
BOARD = 'records/board/'
NEVER_EXPORT = ('records/history/', 'records/data/control.json', 'records/data/roles.json', 'records/imported.json')   # v1's build writes these


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def git(v1, *a):
    return subprocess.run(['git', '-C', v1, *a], capture_output=True, text=True, check=True).stdout.strip()


def files_under(top):
    out = []
    for d, dirs, fs in os.walk(top):
        dirs.sort()
        for f in sorted(fs):
            out.append(os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, '/'))
    return out


def here_path(v1_rel):
    for src, dst in COPY:
        if src.endswith('/') and v1_rel.startswith(src):
            return dst + v1_rel[len(src):]
        if v1_rel == src:
            return dst
    return None


def v1_path(here_rel):
    for src, dst in COPY:
        if dst.endswith('/') and here_rel.startswith(dst):
            return src + here_rel[len(dst):]
        if here_rel == dst:
            return src
    return None


def load_record():
    return json.load(open(RECORD, encoding='utf-8')) if os.path.exists(RECORD) else {}


def changed_here(record):
    """Files under records/ written here since the last import: changed against the record, or not in it. With no record
    yet (the first import), nothing counts as written here."""
    known = record.get('files', {})
    if not known:
        return []
    out = []
    for p in files_under(os.path.join(ROOT, 'records')):
        if p.startswith(NEVER_EXPORT) or p == 'records/imported.json':
            continue
        if known.get(p) != sha(os.path.join(ROOT, p)):
            out.append(p)
    return out


def row_name(row, seen):
    n = seen.get(row['id'], 0) + 1; seen[row['id']] = n
    return row['id'] if n == 1 else f'{row["id"]}__{n}'


def do_import(v1):
    if git(v1, 'status', '--porcelain', '--', 'data', 'admin', 'review', 'REALITY.md', 'BRIEF-CORRECTIONS.md'):
        sys.exit('import: the v1 clone has uncommitted changes; import from a released commit')
    record = load_record()
    keep = set(changed_here(record))
    kept, wrote = [], {}
    def put(dst_rel, data):
        if dst_rel in keep:
            kept.append(dst_rel); wrote[dst_rel] = sha(os.path.join(ROOT, dst_rel)); return
        p = os.path.join(ROOT, dst_rel); os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'wb') as f:
            f.write(data)
        wrote[dst_rel] = hashlib.sha256(data).hexdigest()
    for src, dst in COPY:
        s = os.path.join(v1, src.rstrip('/'))
        if not os.path.exists(s):
            sys.exit(f'import: {src} is not in v1')
        if src.endswith('/'):
            for d, dirs, fs in os.walk(s):
                for f in fs:
                    rel = os.path.relpath(os.path.join(d, f), s).replace(os.sep, '/')
                    put(dst + rel, open(os.path.join(d, f), 'rb').read())
        else:
            put(dst, open(s, 'rb').read())
    admin = json.load(open(os.path.join(v1, 'data', 'admin.json'), encoding='utf-8'))
    seen = {}
    for order, row in enumerate(admin['board']):
        name = row_name(row, seen)
        put(f'{BOARD}{name}.json', (json.dumps({**row, 'order': order}, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    put('records/data/roles.json', (json.dumps({'about': 'The roles of the newsroom, as v1 data/admin.json kept them.', 'roles': admin['roles']}, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
    # a file the last import wrote that v1 no longer has, and nobody changed here since: gone. Only a file the import
    # itself maps (under a COPY destination, the board, roles.json): a file written here (records/tools/schedule.py) is in
    # the record as its own and is never v1's to take away (board correspondent-0003; the conductor's patch).
    gone = 0
    mapped = tuple(dst for _, dst in COPY) + (BOARD, 'records/data/roles.json')
    for p, h in record.get('files', {}).items():
        if p not in wrote and p not in keep and p.startswith(mapped) and os.path.exists(os.path.join(ROOT, p)) and sha(os.path.join(ROOT, p)) == h:
            os.remove(os.path.join(ROOT, p)); gone += 1
    # what is here and was never imported (written here, new) stays, and is in the record as its own
    for p in files_under(os.path.join(ROOT, 'records')):
        if p not in wrote and p != 'records/imported.json':
            wrote[p] = sha(os.path.join(ROOT, p))
    commit = git(v1, 'rev-parse', 'HEAD')
    version = open(os.path.join(v1, 'VERSION'), encoding='utf-8').read().strip()
    with open(RECORD, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'from': {'repository': 'SGit-AI/sgit-ai__website__newsroom__2026__oct__php', 'commit': commit, 'site_version': version},
                   'board_rows': len(admin['board']), 'kept': sorted(kept), 'files': dict(sorted(wrote.items()))}, f, indent=1, ensure_ascii=False); f.write('\n')
    print(f'imported from v1 at {commit[:12]} (site v{version}): {len(admin["board"])} board rows, {len(COPY)} paths; '
          f'{len(kept)} file(s) written here since the last import kept (export them), {gone} gone')
    for p in kept[:20]:
        print(f'  kept: {p}')


def do_export(v1):
    record = load_record()
    if not record.get('files'):
        sys.exit('export: no import record with file sums yet; import first')
    changed = changed_here(record)
    built = set(open(os.path.join(v1, 'admin', 'build', 'outputs.txt'), encoding='utf-8').read().split())   # what v1's build writes
    rows, files = [], []
    for p in changed:
        if p.startswith(BOARD):
            rows.append(p); continue
        t = v1_path(p)
        if t is None:
            print(f'  not exported (no v1 path): {p}'); continue
        if t in built:
            print(f'  not exported, v1 builds it: {p}'); continue
        dst = os.path.join(v1, t); os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, p), dst); files.append(t)
    if rows:
        ap = os.path.join(v1, 'data', 'admin.json')
        raw = open(ap, encoding='utf-8').read(); admin = json.loads(raw)
        if json.dumps(admin, indent=1, ensure_ascii=False) + '\n' != raw:
            sys.exit('export: v1 data/admin.json is not in the one format the build writes; not touching it')
        by_id = {}
        seen = {}
        for i, row in enumerate(admin['board']):
            by_id[row_name(row, seen)] = i
        for p in sorted(rows):
            row = json.load(open(os.path.join(ROOT, p), encoding='utf-8'))
            name = os.path.basename(p)[:-5]
            row = {k: v for k, v in row.items() if k != 'order'}
            for k in ('id', 'title', 'status', 'owner'):
                if k not in row:
                    sys.exit(f'export: {p} has no "{k}"')
            if name in by_id:
                admin['board'][by_id[name]] = row
            else:
                admin['board'].append(row)
        with open(ap, 'w', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(admin, indent=1, ensure_ascii=False) + '\n')
    print(f'exported to v1: {len(files)} file(s), {len(rows)} board row(s); release v1, then import again')
    for t in files[:20]:
        print(f'  {t}')
    for p in rows[:20]:
        print(f'  board: {os.path.basename(p)[:-5]}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('what', choices=['import', 'export'])
    ap.add_argument('--from', dest='src', help='import: a clone of v1')
    ap.add_argument('--into', dest='dst', help='export: a clone of v1')
    a = ap.parse_args()
    if a.what == 'import':
        if not a.src: sys.exit('import needs --from')
        do_import(os.path.abspath(a.src))
    else:
        if not a.dst: sys.exit('export needs --into')
        do_export(os.path.abspath(a.dst))


if __name__ == '__main__':
    main()
