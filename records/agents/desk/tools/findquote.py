"""Find a phrase in a source's captures (text.txt), print the surrounding words, file and sha256. Read-only."""
import sys, os, hashlib, glob, re
V, slug, phrase = sys.argv[1], sys.argv[2], sys.argv[3]
files = sorted(glob.glob(os.path.join(V, 'sources', slug, 'captures', '*', 'text.txt')))
if not files: print('NO CAPTURE TEXT', slug); sys.exit()
for f in files:
    b = open(f, 'rb').read(); t = b.decode('utf-8', 'replace')
    i = t.lower().find(phrase.lower())
    if i < 0: print('  absent', os.path.relpath(f, V)); continue
    a = max(0, i - 160); z = min(len(t), i + len(phrase) + 200)
    print('FOUND', os.path.relpath(f, V), hashlib.sha256(b).hexdigest())
    print('   ', re.sub(r'\s+', ' ', t[a:z]))
