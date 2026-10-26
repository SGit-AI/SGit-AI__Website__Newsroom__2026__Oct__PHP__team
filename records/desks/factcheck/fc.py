#!/usr/bin/env python3
"""The fact-check desk's tool. Standard library plus the issues-fs CLI (pip install issues-fs-cli).

  fc.py check [--vault DIR]      scripted checks over data/ and the desk's files; with a vault clone, verify every cited capture's text by sha256
  fc.py changed                  claims whose text, sources or status changed since their assessment
  fc.py drift --vault DIR        excerpts a grade rests on that are no longer in the newest capture of their source
  fc.py extract CLAIM --vault DIR  print the captured text of every source a claim cites, with paths and hashes (for mode 1)
  fc.py ticket create TYPE TITLE [--claims a,b] [--sources s] [--pages p] [--run Run-N] [--desc TEXT] [--severity S] [--prop k=v ...]
  fc.py ticket set LABEL [--status S] [--comment TEXT] [--prop k=v ...]
  fc.py ticket link LABEL VERB LABEL
  fc.py export                   write data/factcheck.json for the build (deterministic: no clock)
"""
import hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
ISSUES = os.path.join(HERE, '.issues')

LEVELS = [
    ('A0', 'Unsupported', 'No capture carries it, or the cited capture does not say it'),
    ('A1', 'Weak signal', 'Second hand, unnamed, blocked, or only partly carried by its capture'),
    ('A2', 'Reported', 'One named party says it, in a capture this desk checked'),
    ('A3', 'Echoed', 'Several outlets say it, tracing to one origin'),
    ('A4', 'Corroborated', 'Two or more independent parties say it, at least one checked in a capture'),
    ('A5', 'Confirmed', 'Two or more independent primary sources say it, each checked in a capture'),
    ('A6', 'Established', 'The authoritative primary record carries it, or this site counted it from a captured file'),
]
KINDS = ['record', 'event', 'state', 'count', 'quote', 'attribution', 'reading', 'advice']
VERDICTS = ['holds', 'holds-in-part', 'not-shown', 'refuted']
TENSIONS = ['none', 'measures-differently', 'disputed', 'contradicted', 'superseded']
TENSION_CAP = {'contradicted': 1, 'disputed': 2}
RESULTS = ['carries', 'partial', 'absent', 'blocked', 'not-captured']
FITS = ['ok', 'overstated', 'understated']
STATUS_RANK = {'contradicted': 0, 'unverified': 1, 'disputed': 2, 'reported': 2, 'confirmed': 5}


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def data(name):
    return load(os.path.join(ROOT, 'data', name + '.json'))


def desk(name, default):
    p = os.path.join(HERE, name)
    return load(p) if os.path.exists(p) else default


def claim_hash(c):
    s = json.dumps({k: c.get(k) for k in ('claim', 'by', 'sources', 'status', 'note')}, sort_keys=True)
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def display_level(a, contradictions):
    lv = a['level']
    if a.get('kind') == 'reading':
        lv = min(lv, 3)
    t = a.get('tension', 'none')
    open_c = [c for c in a.get('contradictions', []) if contradictions.get(c, {}).get('status') == 'open']
    if t in TENSION_CAP and (open_c or not a.get('contradictions')):
        lv = min(lv, TENSION_CAP[t])
    return lv


# ----------------------------------------------------------------------------- tickets (Issues-FS)

def ifs(*args):
    r = subprocess.run(['issues-fs', *args, '--for-agent'], cwd=HERE, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f'issues-fs {" ".join(args)}: {r.stderr or r.stdout}')
    return json.loads(r.stdout) if r.stdout.strip().startswith(('{', '[')) else r.stdout


def node_path(label):
    t, _ = label.rsplit('-', 1)
    for d in os.listdir(os.path.join(ISSUES, 'data')):
        p = os.path.join(ISSUES, 'data', d, label, 'issue.json')
        if os.path.exists(p):
            return p
    sys.exit(f'no ticket {label}')


def patch_props(label, props):
    p = node_path(label)
    n = load(p)
    n.setdefault('properties', {}).update({k: v for k, v in props.items() if v not in (None, '')})
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(n, f, indent=2, ensure_ascii=False)
        f.write('\n')


def opts(argv):
    o, rest, i = {'prop': []}, [], 0
    while i < len(argv):
        a = argv[i]
        if a.startswith('--'):
            k = a[2:]
            if k == 'prop':
                o['prop'].append(argv[i + 1])
            else:
                o[k] = argv[i + 1]
            i += 2
        else:
            rest.append(a); i += 1
    return o, rest


def cmd_ticket(argv):
    sub, argv = argv[0], argv[1:]
    o, rest = opts(argv)
    props = dict(p.split('=', 1) for p in o['prop'])
    for k in ('claims', 'sources', 'pages'):
        if k in o:
            props[k] = [x for x in o[k].split(',') if x]
    if 'severity' in o:
        props['severity'] = o['severity']
    if sub == 'create':
        typ, title = rest
        args = ['create', typ, title]
        if o.get('desc'):
            args += ['--description', o['desc']]
        if o.get('tags'):
            args += ['--tags', o['tags']]
        n = ifs(*args)['node']
        patch_props(n['label'], props)
        if o.get('run'):
            ifs('link', n['label'], 'opened-by', o['run'])
        print(n['label'])
    elif sub == 'set':
        label = rest[0]
        if o.get('status'):
            ifs('update', label, '--status', o['status'])
        if o.get('comment'):
            ifs('comment', label, o['comment'])
        if props:
            patch_props(label, props)
        print(label)
    elif sub == 'link':
        ifs('link', *rest)
        print(' '.join(rest))
    else:
        sys.exit(f'unknown ticket command {sub}')


def tickets():
    out = []
    base = os.path.join(ISSUES, 'data')
    if not os.path.isdir(base):
        return out
    for d in sorted(os.listdir(base)):
        dd = os.path.join(base, d)
        if not os.path.isdir(dd):
            continue
        for lab in sorted(os.listdir(dd)):
            p = os.path.join(dd, lab, 'issue.json')
            if os.path.exists(p):
                out.append(load(p))
    return out


# ----------------------------------------------------------------------------- checks

def manifest():
    return {s['slug']: s for s in data('sources')}


def capture_text(vault, slug, src):
    """The newest capture's text file in a vault clone, with the manifest's sha256 for it."""
    caps = sorted(src.get('captures', []), key=lambda c: c.get('stamp') or '')
    for cap in reversed(caps):
        for fn in ('text.txt', 'text.md', 'content.txt'):
            if fn in cap.get('files', {}):
                for cand in (os.path.join(vault, 'sources', slug, 'captures', cap['stamp'], fn), os.path.join(vault, 'sources', slug, cap['stamp'], fn)):
                    if os.path.exists(cand):
                        return cand, cap['files'][fn]['sha256'], cap['stamp']
                return None, cap['files'][fn]['sha256'], cap['stamp']
    return None, None, None


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace(' ', ' ')
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return re.sub(r' ([,.;:!?)])', r'\1', s)  # a tag stripped before punctuation leaves a space the page never had


def capture_any(path):
    """A capture file's text; HTML and JSON are reduced to their words so an excerpt read from them still matches."""
    t = open(path, encoding='utf-8', errors='replace').read()
    if path.endswith(('.html', '.htm')):
        import html as H
        t = H.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style).*?</\1>', ' ', t, flags=re.S)))
    return t


def cmd_check(argv):
    o, _ = opts(argv)
    fails, notes = [], []
    claims = {c['id']: c for c in data('claims')}
    src = manifest()
    A = desk('assessments.json', {'assessments': []})['assessments']
    K = {c['id']: c for c in desk('contradictions.json', {'contradictions': []})['contradictions']}
    seen = set()
    for a in A:
        cid = a['id']
        if cid in seen:
            fails.append(f'{cid}: assessed twice')
        seen.add(cid)
        c = claims.get(cid)
        if not c:
            fails.append(f'{cid}: assessed but not in data/claims.json (removed or renamed?)'); continue
        if a.get('kind') not in KINDS: fails.append(f'{cid}: kind {a.get("kind")!r}')
        if a.get('verdict') not in VERDICTS: fails.append(f'{cid}: verdict {a.get("verdict")!r}')
        if a.get('tension', 'none') not in TENSIONS: fails.append(f'{cid}: tension {a.get("tension")!r}')
        if a.get('status_fit') not in FITS: fails.append(f'{cid}: status_fit {a.get("status_fit")!r}')
        if not isinstance(a.get('level'), int) or not 0 <= a['level'] <= 6: fails.append(f'{cid}: level {a.get("level")!r}')
        for k in a.get('contradictions', []):
            if k not in K: fails.append(f'{cid}: names unknown contradiction {k}')
        for ch in a.get('checked', []):
            if ch['source'] not in src and not ch.get('outside_citation'): fails.append(f'{cid}: checked unknown source {ch["source"]}')
            elif ch['source'] not in src and o.get('vault') and not os.path.isdir(os.path.join(o['vault'], 'sources', ch['source'])): fails.append(f'{cid}: {ch["source"]} is in neither the manifest nor the vault')
            elif ch['source'] not in src: notes.append(f'{cid}: rests partly on {ch["source"]}, in the vault but not exported to this site')
            elif ch['source'] not in c['sources'] and not ch.get('outside_citation'):
                notes.append(f'{cid}: checked {ch["source"]}, which the claim does not cite')
            if ch.get('result') not in RESULTS: fails.append(f'{cid}: result {ch.get("result")!r} for {ch["source"]}')
        if a.get('claim_hash') != claim_hash(c):
            notes.append(f'{cid}: claim changed since it was assessed (run {a.get("run")}); re-check')
    for cid in claims:
        if cid not in seen:
            notes.append(f'{cid}: not assessed yet')
    for k in K.values():
        for s in sum([st.get('sources', []) for st in k.get('statements', [])], []):
            if s not in src: notes.append(f'contradiction {k["id"]}: cites {s}, not in the manifest (outside source, not citable until captured)')
        for cid in k.get('claims', []):
            if cid not in claims: fails.append(f'contradiction {k["id"]}: unknown claim {cid}')
    # quotes in claims and notes: list them so mode 1 checks each one
    for c in claims.values():
        for q in re.findall(r"(?:^|[\s(])'([^']{12,}?)'(?=[\s.,;:)]|$)|“([^”]{12,})”|\"([^\"]{12,})\"", (c.get('note') or '') + ' ' + c['claim']):
            q = next(x for x in q if x)
            a = next((x for x in A if x['id'] == c['id']), None)
            if not a or any(norm(q)[:40] in norm(ch.get('excerpt') or '') for ch in a.get('checked', [])):
                continue
            rec = next((x for x in a.get('quotes_checked', []) if norm(q)[:30] in norm(x.get('quote', '')) or norm(x.get('quote', ''))[:30] in norm(q)), None)
            if rec and rec.get('found') is False:
                notes.append(f'{c["id"]}: quote checked and NOT in the capture it is attributed to: "{q[:70]}"')
            elif not rec:
                notes.append(f'{c["id"]}: quote not yet checked: "{q[:70]}"')
    # with a vault: every cited text capture exists and matches the manifest hash
    if o.get('vault'):
        bad = 0
        for c in claims.values():
            for s in c['sources']:
                if s not in src: continue
                p, sha, _ = capture_text(o['vault'], s, src[s])
                if sha and p and hashlib.sha256(open(p, 'rb').read()).hexdigest() != sha:
                    fails.append(f'{s}: text capture does not match the manifest sha256'); bad += 1
        notes.append(f'vault: cited text captures checked against the manifest, {bad} mismatches')
        # every excerpt the desk recorded must be in the file it names, verbatim up to whitespace and quote style
        miss = 0
        for a in A:
            for ch in a.get('checked', []):
                ex = ch.get('excerpt')
                if not ex or not ch.get('file'):
                    continue
                p = os.path.join(o['vault'], ch['file'])
                if not os.path.exists(p):
                    fails.append(f'{a["id"]}: names {ch["file"]}, not in the vault clone'); miss += 1; continue
                if norm(ex) not in norm(capture_any(p)) and norm(ex) not in norm(open(p, encoding='utf-8', errors='replace').read()):
                    fails.append(f'{a["id"]}: excerpt not found in {ch["file"]}: "{ex[:60]}"'); miss += 1
        notes.append(f'vault: every recorded excerpt checked against its file, {miss} not found')
    for n in notes: print('note:', n)
    for f in fails: print('FAIL:', f)
    print(f'{len(A)} assessments, {len(K)} contradictions, {len(tickets())} tickets; {len(fails)} failures, {len(notes)} notes')
    sys.exit(1 if fails else 0)


def newest_capture_text(vault, slug):
    """The newest capture's text file of a source in a vault clone, whatever the manifest says."""
    d = os.path.join(vault, 'sources', slug, 'captures')
    for st in sorted(os.listdir(d), reverse=True) if os.path.isdir(d) else []:
        p = os.path.join(d, st, 'text.txt')
        if os.path.exists(p):
            return st, p
    return None, None


def cmd_drift(argv):
    """For every excerpt a grade rests on, is it still in the newest capture of its source? Words that survive a
    re-capture leave the grade standing; words that are gone mean the source changed, and the grade needs a look."""
    o, _ = opts(argv)
    A = desk('assessments.json', {'assessments': []})['assessments']
    gone = 0
    for a in A:
        for ch in a.get('checked', []):
            ex = ch.get('excerpt')
            if not ex or not ch.get('file') or not ch['file'].endswith('text.txt'):
                continue
            st, p = newest_capture_text(o['vault'], ch['source'])
            if not p or p.endswith(ch['file']):
                continue
            if norm(ex) not in norm(open(p, encoding='utf-8', errors='replace').read()):
                gone += 1
                print(f'{a["id"]}\t{ch["source"]}\t{st}\tgone: "{ex[:70]}"')
    print(f'drift: {gone} excerpt(s) no longer in the newest capture of their source')


def cmd_changed(argv):
    claims = data('claims')
    A = {a['id']: a for a in desk('assessments.json', {'assessments': []})['assessments']}
    for c in claims:
        a = A.get(c['id'])
        if not a:
            print(f'{c["id"]}\tnew')
        elif a.get('claim_hash') != claim_hash(c):
            print(f'{c["id"]}\tchanged')


def cmd_extract(argv):
    o, rest = opts(argv)
    claims = {c['id']: c for c in data('claims')}
    src = manifest()
    c = claims[rest[0]]
    print(json.dumps({k: c.get(k) for k in ('id', 'claim', 'by', 'status', 'note', 'sources')}, indent=1, ensure_ascii=False))
    for s in c['sources']:
        row = src.get(s)
        if not row:
            print(f'\n=== {s}: NOT IN MANIFEST'); continue
        p, sha, stamp = capture_text(o['vault'], s, row)
        print(f'\n=== {s} | {row.get("publisher")} | primary={row.get("primary")} | status={row.get("status")} | published={row.get("published")}')
        print(f'    url: {row.get("url")}')
        print(f'    capture: {stamp} text sha256 {sha} file {p}')
        if row.get('notes'):
            print(f'    collector notes: {row["notes"][:600]}')
        if p:
            t = open(p, encoding='utf-8', errors='replace').read()
            ok = hashlib.sha256(open(p, 'rb').read()).hexdigest() == sha
            print(f'    hash matches manifest: {ok}; {len(t)} chars')


# ----------------------------------------------------------------------------- export

def investigations():
    """Each investigation's case file and its data sets, from admin/factcheck/investigations/<id>/."""
    base = os.path.join(HERE, 'investigations')
    out = []
    for d in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        p = os.path.join(base, d)
        if os.path.exists(os.path.join(p, 'case.json')):
            inv = load(os.path.join(p, 'case.json'))
            for part in ('measures', 'lineage', 'live'):
                if os.path.exists(os.path.join(p, part + '.json')):
                    inv[part] = load(os.path.join(p, part + '.json'))
            out.append(inv)
    return out


def cmd_export(argv):
    claims = {c['id']: c for c in data('claims')}
    A = sorted(desk('assessments.json', {'assessments': []})['assessments'], key=lambda a: a['id'])
    K = sorted(desk('contradictions.json', {'contradictions': []})['contradictions'], key=lambda k: k['id'])
    Kd = {k['id']: k for k in K}
    T = tickets()
    runs = []
    rd = os.path.join(HERE, 'runs')
    for fn in sorted(os.listdir(rd)) if os.path.isdir(rd) else []:
        if fn.endswith('.json'):
            runs.append(load(os.path.join(rd, fn)))
    by_claim = {}
    tix = []
    for t in T:
        if t['node_type'] == 'run':
            continue
        p = t.get('properties', {})
        row = {'label': t['label'], 'type': t['node_type'], 'status': t['status'], 'title': t['title'], 'description': t.get('description', ''),
               'severity': p.get('severity', ''), 'claims': p.get('claims', []), 'sources': p.get('sources', []), 'pages': p.get('pages', []),
               'url': p.get('url', ''), 'retrieved_at': p.get('retrieved_at', ''), 'sha256': p.get('sha256', ''), 'excerpt': p.get('excerpt', ''),
               'run': next((l['target_label'] for l in t.get('links', []) if l['verb'] == 'opened-by'), ''),
               'links': sorted([{'verb': l['verb'], 'to': l['target_label']} for l in t.get('links', []) if l['verb'] not in ('opened-by',)], key=lambda x: (x['verb'], x['to']))}
        tix.append(row)
        for c in row['claims']:
            by_claim.setdefault(c, []).append(t['label'])
    rows = []
    for a in A:
        c = claims.get(a['id'])
        if not c:
            continue
        r = dict(a)
        r['display'] = display_level(a, Kd)
        r['stale'] = a.get('claim_hash') != claim_hash(c)
        r['tickets'] = sorted(set(a.get('tickets', []) + by_claim.get(a['id'], [])))
        rows.append(r)
    out = {
        'schema': 'sgit.newsroom.factcheck/1',
        'desk': 'factcheck@php.newsroom',
        'levels': [{'code': c, 'n': i, 'name': n, 'means': m} for i, (c, n, m) in enumerate(LEVELS)],
        'kinds': KINDS, 'verdicts': VERDICTS, 'tensions': TENSIONS, 'tension_cap': TENSION_CAP,
        'assessments': rows,
        'unassessed': sorted(set(claims) - {a['id'] for a in A}),
        'contradictions': K,
        'tickets': sorted(tix, key=lambda t: (t['type'], int(t['label'].rsplit('-', 1)[1]))),
        'runs': runs,
        'investigations': investigations(),
    }
    with open(os.path.join(ROOT, 'data', 'factcheck.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
        f.write('\n')
    print(f'data/factcheck.json: {len(rows)} assessments, {len(K)} contradictions, {len(tix)} tickets, {len(runs)} runs')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    {'check': cmd_check, 'drift': cmd_drift, 'changed': cmd_changed, 'extract': cmd_extract, 'ticket': cmd_ticket, 'export': cmd_export}[cmd](sys.argv[2:])
