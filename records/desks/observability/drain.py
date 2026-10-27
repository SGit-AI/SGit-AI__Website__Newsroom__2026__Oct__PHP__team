#!/usr/bin/env python3
"""Drain the telemetry lane into a clone of the telemetry vault (84wr8mib), the way the telemetry application drains it.

Kept by observability@php.newsroom. The same order as the application's Queue & drain (5wnsr5h8, app/modules/drain.js):
list, fetch, open each event with the drain key kept in the vault (identity/private/drain-key.pkcs8.json), append the
rows to drain/<date>.jsonl byte for byte as the application writes them, recompute reports/, commit and push the vault,
and only then mark the events processed in the lane: a failed push leaves every event waiting.

The vault key is the whole boundary (CLAUDE.md): the lane's enum key is derived from it, the drain key is inside the
vault. Nothing secret is printed. Run it with a Python that has sgit-ai (and so `cryptography`), outside the repository:

    SG_SEND_TOKEN=<access token> python -I drain.py --vault <clone> --key-file <file holding the vault key> [--dry-run]

--dry-run fetches and opens the events and prints what came in, and writes, commits, pushes and marks nothing.
Batches are fetched, opened and marked processed PARALLEL at a time (since 27 October); the rows go into the drain file
in the lane's order, whatever order the batches finish in.
"""
import argparse, base64, collections, datetime, hashlib, json, os, subprocess, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = 'https://dev.send.sgraph.ai/api/vault/append/'
BATCH = 100                                              # the server's limit on ids per fetch and per mark-processed
PARALLEL = 4                                             # batches in flight at once, as the application does
NOTE = ('Counts over events received in the lane. Every event is an untrusted claim: the token and the public key are '
        'published, so rows can be forged or flooded. Visitors with blockers do not appear. No row leaves the vault.')


def enum_key(key_file):
    """The lane's enum key: SHA-256 of "sg-inbox-enum:" and the vault's read key (SG/Send's sg-append.js, locked there)."""
    from sgit_ai.crypto.Vault__Crypto import Vault__Crypto
    keys = Vault__Crypto().derive_keys_from_vault_key(open(key_file).read().strip())
    rk = keys['read_key_bytes'] if 'read_key_bytes' in keys else bytes.fromhex(keys['read_key'])
    return hashlib.sha256(b'sg-inbox-enum:' + rk).hexdigest()


def post(op, vault_id, body, enum):
    req = urllib.request.Request(API + op + '/' + vault_id, data=json.dumps(body).encode(), method='POST',
                                 headers={'Content-Type': 'application/json', 'x-sgraph-vault-enum-key': enum})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def drain_key(vault):
    from cryptography.hazmat.primitives.serialization import load_der_private_key
    doc = json.load(open(os.path.join(vault, 'identity', 'private', 'drain-key.pkcs8.json')))
    return load_der_private_key(base64.b64decode(doc['pkcs8']), password=None), doc['fingerprint']


def open_event(key, content):
    """sgit's hybrid envelope v2: base64 of the .enc text, which is base64 of {v, w, i, c}; RSA-OAEP-256 wraps an AES-GCM key."""
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    env = json.loads(base64.b64decode(base64.b64decode(content)))
    aes = key.decrypt(base64.b64decode(env['w']), padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return json.loads(AESGCM(aes).decrypt(base64.b64decode(env['i']), base64.b64decode(env['c']), None).decode('utf-8'))


def row_text(ev):
    """drain.js pyJSON: json.dumps(sort_keys=True, ensure_ascii=False), the bytes the command-line drainer writes too."""
    return json.dumps(ev, sort_keys=True, ensure_ascii=False)


def report(rows, drained_now, as_of):
    """drain.js report(): counts over every drained row, never a row."""
    real = [r for r in rows if r.get('v') == 1 and not r.get('test')]
    def top(k, n=25):
        return [[v, c] for v, c in collections.Counter(str(r.get(k) or '(none)') for r in real).most_common(n)]
    days = collections.Counter(str(r.get('ts') or '')[:10] for r in real)
    return {'as_of': as_of, 'drained_now': drained_now, 'events': len(real), 'test_or_undecryptable': len(rows) - len(real),
            'sessions': len({r.get('sid') for r in real}), 'by_day': sorted([d, n] for d, n in days.items()),
            'by_path': top('path', 40), 'by_country': top('country'), 'by_region': top('region'), 'by_city': top('city'),
            'by_referrer': top('ref'), 'by_screen': top('screen'), 'by_version': top('ver'), 'note': NOTE}


def sgit(vault, *args):
    exe = os.path.join(os.path.dirname(sys.executable), 'sgit')
    p = subprocess.run([exe, *args], cwd=vault, capture_output=True, text=True, timeout=600)
    return p.returncode, p.stdout + p.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', required=True); ap.add_argument('--key-file', required=True)
    ap.add_argument('--vault-id', default='84wr8mib'); ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--rows-out', help='also write the rows this run opened to this file (outside the repository), to look at them')
    a = ap.parse_args()
    V, token = os.path.abspath(a.vault), os.environ.get('SG_SEND_TOKEN', '')
    if not a.dry_run and not token: sys.exit('SG_SEND_TOKEN is not set: the push needs the SG/Send access token')
    enum = enum_key(a.key_file)
    key, fp = drain_key(V)
    print(f'drain key open: {fp}')

    pending, after = [], None
    while True:
        r = post('list', a.vault_id, {'include_content': False, 'limit': 200, **({'after_file_id': after} if after else {})}, enum)
        e = r.get('entries') or []
        pending += e
        if not r.get('truncated') or not e: break
        after = e[-1]['file_id']
    lanes = collections.defaultdict(list)
    for e in pending: lanes[e['inbox']].append(e)
    print(f'waiting: {len(pending)} in {len(lanes)} lane(s)')
    if not pending: return

    today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    path = os.path.join(V, 'drain', today + '.jsonl')
    existing = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
    seen = {json.loads(l).get('_file') for l in existing.splitlines() if l.strip()}
    jobs = [(lane, items[i:i + BATCH]) for lane, items in lanes.items() for i in range(0, len(items), BATCH)]

    def one(job):
        lane, batch = job
        t = time.time()
        got = post('fetch', a.vault_id, {'inbox': lane, 'file_ids': [x['file_id'] for x in batch]}, enum)
        files = got.get('files') or got.get('entries') or []
        evs, ids, again = [], [], 0
        for f in files:
            fid, content = f.get('file_id') or f.get('id'), f.get('content') or f.get('payload')
            if not fid or not content: continue
            ids.append(fid)
            if fid in seen: again += 1; continue
            try: ev = open_event(key, content)
            except Exception as x: ev = {'v': 0, 'undecryptable': True, 'error': str(x)[:120]}
            meta = next((x for x in batch if x['file_id'] == fid), {})
            ev['_file'] = fid
            ev['_received'] = f.get('received') or meta.get('received') or int(str(fid)[:13] or 0) or None
            evs.append(ev)
        print(f'  lane {lane[:8]}…: fetched {len(files)} of {len(batch)} and opened them in {time.time() - t:.1f} s')
        return lane, ids, evs, again, len(batch) - len(files)

    t0 = time.time()
    with ThreadPoolExecutor(PARALLEL) as ex:
        results = list(ex.map(one, jobs))                # map keeps the jobs' order: the lane's order
    print(f'fetched and opened {len(jobs)} batch(es), {PARALLEL} at a time, in {time.time() - t0:.1f} s')
    rows, done = [r for x in results for r in x[2]], collections.defaultdict(list)
    for lane, ids, *_ in results: done[lane] += ids
    dup, unserved = sum(x[3] for x in results), sum(x[4] for x in results)
    bad = sum(1 for r in rows if r.get('undecryptable'))
    print(f'opened {len(rows)}: {len(rows) - bad} readable, {bad} undecryptable, {dup} already drained, {unserved} not served')
    if a.rows_out:
        with open(a.rows_out, 'w', encoding='utf-8') as f: f.write(''.join(row_text(r) + '\n' for r in rows))
    if a.dry_run:
        print('dry run: nothing written, pushed or marked'); return

    if rows:
        with open(path, 'w', encoding='utf-8') as f: f.write(existing + ''.join(row_text(r) + '\n' for r in rows))
    allrows = []
    for fn in sorted(os.listdir(os.path.join(V, 'drain'))):
        if fn.endswith('.jsonl'):
            for l in open(os.path.join(V, 'drain', fn), encoding='utf-8'):
                try: allrows.append(json.loads(l))
                except ValueError: pass                  # a broken line is skipped, as the application does
    rep = json.dumps(report(allrows, len(rows), today), indent=1, ensure_ascii=False)
    for name in (today + '.json', 'latest.json'):
        open(os.path.join(V, 'reports', name), 'w', encoding='utf-8').write(rep)
    print(f'reports written: {json.loads(rep)["events"]} events, {json.loads(rep)["sessions"]} sessions')

    code, out = sgit(V, 'commit', '-m', f'drain {today}: {len(rows)} event(s) (observability@php.newsroom)')
    if code != 0 and 'nothing to commit' not in out.lower(): sys.exit('commit failed; nothing marked processed')
    code, out = sgit(V, 'push', '--token', token)
    code2, st = sgit(V, 'status')
    if code != 0 or 'in sync with remote' not in st: sys.exit('the push did not land; nothing marked processed')
    print('pushed; the vault is in sync with the server')

    marks = [(lane, ids[j:j + BATCH]) for lane, ids in done.items() for j in range(0, len(ids), BATCH)]
    with ThreadPoolExecutor(PARALLEL) as ex:
        marked = sum(ex.map(lambda m: (post('mark-processed', a.vault_id, {'inbox': m[0], 'file_ids': m[1]}, enum), len(m[1]))[1], marks))
    print(f'marked {marked} lane file(s) processed')


if __name__ == '__main__':
    main()
