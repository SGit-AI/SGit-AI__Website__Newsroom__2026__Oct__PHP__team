"""Set quote_checked in data/outreach.json only where the words are found verbatim in the named capture with the named sha256."""
import sys, json, hashlib, os
V, P = sys.argv[1], sys.argv[2]
o = json.load(open(P)); bad = 0
claims = {c['id'] for c in json.load(open(os.path.join(os.path.dirname(P), 'claims.json')))}
for r in o['requests']:
    for c in r.get('factcheck', {}).get('claims', []):
        if c not in claims: print('UNKNOWN CLAIM', r['id'], c); bad += 1
    for s in r['said']:
        f = os.path.join(V, s['file'])
        if not os.path.exists(f): print('MISSING', r['id'], s['file']); s['quote_checked'] = False; bad += 1; continue
        b = open(f, 'rb').read(); ok_h = hashlib.sha256(b).hexdigest() == s['sha256']; ok_w = s['words'] in b.decode('utf-8')
        s['quote_checked'] = ok_h and ok_w
        if not s['quote_checked']: bad += 1
        print(r['id'], 'hash', ok_h, 'words', ok_w, s['where'])
for x in o.get('not_asked', []):
    import glob
    hit = any(x['words'] in open(g, encoding='utf-8').read() for g in glob.glob(os.path.join(V, 'sources', x['source'], 'captures', '*', 'text.txt')))
    print('not-asked', x['publisher'], hit); bad += (not hit)
json.dump(o, open(P, 'w'), indent=1, ensure_ascii=False); open(P, 'a').write('\n')
print('problems', bad)
