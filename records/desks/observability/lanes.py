#!/usr/bin/env python3
"""The telemetry vault's lanes in parallel: several append tokens on one vault, so a page can move to the next lane when
one is full (the server keeps 1,000 waiting per token, then answers 507). Kept by observability@php.newsroom; the brief
is records/briefs/2026-10-24__brief__the-lane-cap-and-sharded-lanes.md (option 2 and 3), at the editor's word of
27 October 2026: "four or five append lanes that the UI can use when one fails".

Lane 1 is the token the site already publishes; lanes 2 to N are derived from the vault's write key (HMAC-SHA256 with
the label below), so whoever holds the vault key can rebuild every lane: the vault key stays the whole boundary. Append
tokens write and read nothing; they are published by design. Nothing secret is printed.

    python -I lanes.py --vault <clone> --key-file <vault key file> plan                 # the lanes, from the vault key
    SG_SEND_TOKEN=... python -I lanes.py --vault <clone> --key-file <file> configure      # set the anchors on the server
    python -I lanes.py --vault <clone> --key-file <file> test                             # one test event into every lane

`configure` replaces the server's whole anchor list, so it always sends every lane, lane 1 first. It also writes
identity/lanes.json in the clone (commit and push the vault after). A test event is {"v": 1, "test": true}: the
reports leave it out.
"""
import argparse, base64, hashlib, hmac, json, os, sys, urllib.error, urllib.request

API = 'https://dev.send.sgraph.ai/api/vault/append/'
LABEL = 'sgit.newsroom/telemetry/lane-{}/v1'


def keys(key_file):
    from sgit_ai.crypto.Vault__Crypto import Vault__Crypto
    return Vault__Crypto().derive_keys_from_vault_key(open(key_file).read().strip())


def lanes(vault, write_key, n):
    doc = json.load(open(os.path.join(vault, 'identity', 'lanes.json')))
    first = doc['lanes'][0]['append_token']             # the token the site publishes today
    out = [first] + [hmac.new(bytes.fromhex(write_key), LABEL.format(i).encode(), hashlib.sha256).hexdigest() for i in range(2, n + 1)]
    return doc, out


def call(op, vault_id, body, headers):
    req = urllib.request.Request(API + op + '/' + vault_id, data=json.dumps(body).encode(), method='POST', headers={'Content-Type': 'application/json', **headers})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read().decode()[:200]
    except urllib.error.HTTPError as e:
        return e.code, ''


def envelope(pem, text):
    """telemetry.js envelope(): sgit's hybrid envelope v2, base64 twice, RSA-OAEP-256 wrapping an AES-256-GCM key."""
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    pub = serialization.load_pem_public_key(pem.encode())
    aes, iv = AESGCM.generate_key(bit_length=256), os.urandom(12)
    c = AESGCM(aes).encrypt(iv, text.encode(), None)
    w = pub.encrypt(aes, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    b = lambda x: base64.b64encode(x).decode()
    enc = b(json.dumps({'v': 2, 'w': b(w), 'i': b(iv), 'c': b(c)}, separators=(',', ':')).encode())   # the .enc file's text
    return b(enc.encode())                              # the payload is the .enc file's bytes, in base64: encoded twice


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', required=True); ap.add_argument('--key-file', required=True); ap.add_argument('--lanes', type=int, default=5)
    ap.add_argument('cmd', choices=['plan', 'configure', 'test'])
    a = ap.parse_args()
    V, k = os.path.abspath(a.vault), keys(a.key_file)
    doc, toks = lanes(V, k['write_key'], a.lanes)
    vault_id = doc['vault_id']
    if a.cmd == 'plan':
        for i, t in enumerate(toks, 1): print(f'lane {i}: {t[:8]}… anchor {hashlib.sha256(t.encode()).hexdigest()[:12]}…')
        return
    if a.cmd == 'configure':
        token = os.environ.get('SG_SEND_TOKEN') or sys.exit('SG_SEND_TOKEN is not set: configure needs the SG/Send access token')
        anchors = [hashlib.sha256(t.encode()).hexdigest() for t in toks]
        code, body = call('configure', vault_id, {'append_anchors': anchors}, {'x-sgraph-vault-write-key': k['write_key'], 'x-sgraph-access-token': token})
        print(f'configure: HTTP {code} {body}')
        if code != 200: sys.exit('not configured; the server keeps the anchors it had')
        doc['about'] = ('The append lanes on this vault, in the order a page tries them. Each token only writes (they are published on the site); '
                        'lane 1 is the site\'s first token, lanes 2 and up are derived from this vault\'s write key (records/desks/observability/lanes.py '
                        'in the team repository). The enum key that lists and fetches every lane is derived from this vault\'s read key; it is not stored here.')
        used = doc['lanes'][0].get('used_by', '')
        doc['lanes'] = [{'name': f'site telemetry, lane {i}', 'append_token': t, 'used_by': used if i == 1 else 'assets/telemetry.js, when the lanes before it answer 507 (once the page knows this lane)'}
                        for i, t in enumerate(toks, 1)]
        open(os.path.join(V, 'identity', 'lanes.json'), 'w').write(json.dumps(doc, indent=1) + '\n')
        print(f'identity/lanes.json: {len(toks)} lanes; commit and push the vault')
        return
    pem = json.load(open(os.path.join(V, 'identity', 'public-bundle.json'))).get('encrypt') if os.path.exists(os.path.join(V, 'identity', 'public-bundle.json')) else None
    pem = pem or os.environ.get('TELEMETRY_PUBLIC_PEM_FILE') and open(os.environ['TELEMETRY_PUBLIC_PEM_FILE']).read()
    if not pem: sys.exit('no public key: identity/public-bundle.json has no "encrypt", and TELEMETRY_PUBLIC_PEM_FILE is not set')
    for i, t in enumerate(toks, 1):
        ev = {'v': 1, 'test': True, 'site': 'observability lane test', 'path': f'/lane-test/{i}/', 'sid': f'lanetest{i}', 'ts': ''}
        code, _ = call('write', vault_id, {'append_token': t, 'payload': envelope(pem, json.dumps(ev))}, {})
        print(f'lane {i} ({t[:8]}…): write HTTP {code}')


if __name__ == '__main__':
    main()
