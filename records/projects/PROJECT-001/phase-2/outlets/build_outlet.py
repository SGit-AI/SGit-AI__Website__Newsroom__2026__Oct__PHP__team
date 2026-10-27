#!/usr/bin/env python3
"""Build the derived file one outlet page reads: outlets/<id>.json.

Standard library only, no network, deterministic (no wall clock, no randomness).
Usage:
  python3 build_outlet.py --data <data files dir> --actor bbc --out bbc.json \
      [--data-commit <sha>] [--as-of <ISO time>] [--editorial editorial/bbc.json]
  # an outlet with no actor entry, or one inside a wider actor:
  python3 build_outlet.py --data ... --id cisa --name CISA --party party:cisa \
      --source-slugs a,b,c --publisher-match '^CISA$|Cybersecurity and Infrastructure' --out cisa.json
Everything read from the data is material, never instructions.
"""
import argparse, json, re, sys, os

def load(d, name):
    with open(os.path.join(d, name + '.json'), encoding='utf-8') as f:
        return json.load(f)

def tkey(t):
    """Sortable key for the data's mixed time strings ('2024', '2026-10-21', '2026-10-21T14:00Z')."""
    t = t or ''
    m = re.match(r'(\d{4})(?:-(\d\d))?(?:-(\d\d))?(?:T(\d\d):(\d\d)(?::(\d\d))?)?', t)
    if not m:
        return t
    return '%s-%s-%sT%s:%s:%s' % tuple(g or d for g, d in zip(m.groups(), ['', '00', '00', '00', '00', '00']))

def stamp_iso(s):
    m = re.match(r'(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)(\d\d)Z$', s or '')
    return '%s-%s-%sT%s:%s:%sZ' % m.groups() if m else s

def stamp_of_path(p):
    m = re.search(r'/captures/(\d{8}T\d{6}Z)/', p or '')
    return m.group(1) if m else None

INJ = re.compile(r'(ignore (all |any )?(previous|prior|above)|disregard (the )?(previous|above)|you are (an? )?(ai|assistant|language model)|\bas an ai\b|(dear|hey|attention)[ ,]+(claude|ai|assistant|agent)|system prompt|instruct(ion)?s? (to|for) (the )?(ai|agent|assistant|model))', re.I)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', required=True)
    ap.add_argument('--actor')
    ap.add_argument('--id')
    ap.add_argument('--name')
    ap.add_argument('--party', help='graph node id for the ego graph (default party:<actor>)')
    ap.add_argument('--source-slugs', default='')
    ap.add_argument('--publisher-match', help='regex on sources[].publisher (case-insensitive)')
    ap.add_argument('--echo-terms', help='comma list; default derived from name, aliases, id')
    ap.add_argument('--editorial', help='JSON with proposed points / not_asked carried from the editor')
    ap.add_argument('--data-commit', default=None)
    ap.add_argument('--data-version', default=None)
    ap.add_argument('--as-of', default=None)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    actors, sources, claims = load(a.data, 'actors'), load(a.data, 'sources'), load(a.data, 'claims')
    fc, graph, outreach = load(a.data, 'factcheck'), load(a.data, 'graph'), load(a.data, 'outreach')
    timeline, entities = load(a.data, 'timeline'), load(a.data, 'entities')
    srcmap = {s['slug']: s for s in sources}
    actor = next((x for x in actors if x['id'] == a.actor), None) if a.actor else None
    if a.actor and not actor:
        sys.exit('no actor %r in actors.json' % a.actor)
    oid = a.id or a.actor
    if not oid:
        sys.exit('need --actor or --id')

    # ---- which sources are the outlet's (rules recorded in method) ----
    slugs, rules = set(), []
    if actor:
        slugs |= {s for s in actor['sources'] if s in srcmap}
        rules.append('actors.json sources of actor %r' % actor['id'])
    if a.source_slugs:
        extra = [s for s in a.source_slugs.split(',') if s]
        missing = [s for s in extra if s not in srcmap]
        slugs |= {s for s in extra if s in srcmap}
        rules.append('--source-slugs (%d given, %d not in sources.json)' % (len(extra), len(missing)))
    if a.publisher_match:
        rx = re.compile(a.publisher_match, re.I)
        hit = {s['slug'] for s in sources if rx.search(s.get('publisher') or '')}
        slugs |= hit
        rules.append('publisher field matches /%s/i (%d)' % (a.publisher_match, len(hit)))
    outlet_sources = sorted(slugs)

    ent = next((e for e in entities['entities'] if e['id'] == oid), None)
    pid = a.party or ('party:' + (a.actor or oid))
    node = {n['id']: n for n in graph['nodes']}
    pnode = node.get(pid)
    name = a.name or (ent and ent['name']) or (pnode and pnode['label']) or (actor and actor['name']) or oid
    kind = (pnode and pnode.get('class')) or (ent and ent.get('kind')) or (actor and actor.get('role')) or None

    # ---- assessments, claims ----
    assess = {x['id']: x for x in fc['assessments']}
    contra = {c['id']: c for c in fc['contradictions']}
    claim_by_id = {c['id']: c for c in claims}
    my_claims = sorted((c for c in claims if set(c['sources']) & slugs), key=lambda c: c['id'])

    def fcj(cid):
        x = assess.get(cid)
        if not x:
            return None
        return {'verdict': x['verdict'], 'level': x['level'], 'kind': x['kind'], 'tension': x['tension'],
                'status_fit': x['status_fit'], 'as_of': x['as_of'], 'volatile': x['volatile'], 'stale': x['stale'],
                'reason': x['reason'], 'contradictions': sorted(x['contradictions']), 'tickets': sorted(x['tickets']),
                'next_step': x.get('mode2') or None}

    ledger = [{'claim_id': c['id'], 'text': c['claim'], 'attributed_to': c['by'], 'status': c['status'],
               'factcheck': fcj(c['id']), 'sources': sorted(c['sources'])} for c in my_claims]
    by_verdict = {}
    for r in ledger:
        v = r['factcheck']['verdict'] if r['factcheck'] else 'unassessed'
        by_verdict[v] = by_verdict.get(v, 0) + 1

    # ---- captures ----
    captures = []
    for slug in outlet_sources:
        s = srcmap[slug]
        for c in s.get('captures') or []:
            files = {n: {'sha256': f.get('sha256'), 'bytes': f.get('bytes')} for n, f in sorted((c.get('files') or {}).items())}
            flags = []
            if any((f['bytes'] is not None and f['bytes'] < 100) for f in files.values()):
                flags.append('stub file(s) under 100 bytes: ' + ', '.join(n for n, f in files.items() if f['bytes'] is not None and f['bytes'] < 100))
            if c.get('status') not in (None, 200):
                flags.append('http %s' % c.get('status'))
            captures.append({'source': slug, 'stamp': c['stamp'], 'kind': 'vault', 'http_status': c.get('status'),
                             'started_utc': c.get('started_utc'), 'final_url': c.get('final_url'),
                             'complete': not flags, 'flags': flags, 'files': files})
        raw = s.get('raw_sha256') or {}
        if raw:
            stamps = {}
            found = {}
            for fn, h in raw.items():
                m = re.search(r'(\d{4})-(\d\d)-(\d\d)T(\d\d)(\d\d)Z', fn)
                found[fn] = '%s%s%sT%s%s00Z' % m.groups() if m else None
            known = sorted({v for v in found.values() if v})
            for fn, h in raw.items():
                st = found[fn] or (known[0] if len(known) == 1 else 'raw')
                stamps.setdefault(st, {})[fn] = {'sha256': h, 'bytes': None}
            for st, files in sorted(stamps.items()):
                captures.append({'source': slug, 'stamp': st, 'kind': 'raw', 'http_status': None, 'started_utc': None,
                                 'final_url': None, 'complete': True,
                                 'flags': ['raw curl copy held in the source folder (raw/); stamp from the file name' if st != 'raw' else 'raw files, no time in the name'],
                                 'files': dict(sorted(files.items()))})
    captures.sort(key=lambda c: (c['stamp'], c['source']))
    vault_caps = [c for c in captures if c['kind'] == 'vault']

    def latest_stamp(slug, prefer_complete=True):
        cs = [c for c in vault_caps if c['source'] == slug and (c['complete'] or not prefer_complete)]
        return cs[-1]['stamp'] if cs else None

    # ---- requests and points ----
    ed = {}
    if a.editorial:
        with open(a.editorial, encoding='utf-8') as f:
            ed = json.load(f)
    pubrx = re.compile(a.publisher_match, re.I) if a.publisher_match else None
    reqs = []
    for r in outreach['requests']:
        said_src = {s['source'] for s in r.get('said', [])}
        if (a.actor and r.get('actor') == a.actor) or (said_src & slugs) or (pubrx and pubrx.search(r.get('publisher') or '')):
            reqs.append(r)
    reqs.sort(key=lambda r: r['id'])

    terms = [t for t in (a.echo_terms.split(',') if a.echo_terms else []) if t]
    if not terms:
        terms = [name, oid] + (ent['aliases'] if ent else [])
        if pnode:
            terms.append(pnode['label'])
    terms = sorted({t.strip() for t in terms if t and t.strip()}, key=str.lower)
    termrx = re.compile(r'(?<![\w])(?:' + '|'.join(re.escape(t) for t in terms) + r')(?![\w])', re.I)

    def primary_for(cids, req=None):
        # 1. the contradiction record's first statement not made by the outlet
        if req and req.get('factcheck', {}).get('contradiction') in contra:
            for st in contra[req['factcheck']['contradiction']]['statements']:
                if termrx.search(st['who']) or not st.get('sources'):
                    continue
                src = st['sources'][0]
                cap = None
                for cid in cids:
                    for ch in (assess.get(cid) or {}).get('checked', []):
                        if ch['source'] == src and stamp_of_path(ch['file']):
                            cap = stamp_of_path(ch['file']); break
                    if cap: break
                return {'text': st['says'], 'source': src, 'capture': cap or latest_stamp(src, False)}
        # 2. a fact-check check on a source that is not the outlet's
        for prim in (True, False):
            for want in ('carries', 'partial'):
                for cid in cids:
                    for ch in (assess.get(cid) or {}).get('checked', []):
                        if (ch['source'] not in slugs and ch['result'] == want and not ch.get('outside_citation')
                                and bool((srcmap.get(ch['source']) or {}).get('primary')) == prim):
                            return {'text': ch['excerpt'], 'source': ch['source'], 'capture': stamp_of_path(ch['file'])}
        return {'text': None, 'source': None, 'capture': None}

    def their_words_for(cid):
        for want in ('carries', 'partial'):
            for ch in (assess.get(cid) or {}).get('checked', []):
                if ch['source'] in slugs and ch['result'] == want:
                    return {'text': ch['excerpt'], 'source': ch['source'], 'capture': stamp_of_path(ch['file']), 'sha256': ch['sha256']}
        return None

    points, caveats = [], {}
    rn = ed.get('request_n', {})
    for r in reqs:
        cids = r.get('factcheck', {}).get('claims', [])
        said = (r.get('said') or [{}])[0]
        first = assess.get(cids[0]) if cids else None
        n = rn.get(r['id'])
        points.append({'n': n, 'request_id': r['id'], 'status': r['status'], 'claim_ids': sorted(cids),
                       'blocked_by': sorted(r.get('blocked_by') or []),
                       'claim_text': claim_by_id[cids[0]]['claim'] if cids and cids[0] in claim_by_id else r['point'],
                       'their_words': {'text': said.get('words'), 'source': said.get('source'),
                                       'capture': stamp_of_path(said.get('file')), 'sha256': said.get('sha256')},
                       'primary': primary_for(cids, r), 'suggested': r.get('suggested'),
                       'verdict': first['verdict'] if first else None, 'held_reason': None})
    for p in ed.get('points', []):
        cid = p['claim_id']
        tw = their_words_for(cid)
        if tw is None:
            tw = {'text': None, 'source': None, 'capture': None, 'sha256': None}
            caveats[str(p['n'])] = 'no fact-check check found the outlet saying this (result absent); their_words is null'
        elif (assess.get(cid) or {}).get('checked') and not any(ch['source'] in slugs and ch['result'] in ('carries', 'partial') for ch in assess[cid]['checked']):
            pass
        x = assess.get(cid)
        # an 'absent' result on the outlet's own capture means the outlet does not state the claim as worded
        if x and any(ch['source'] in slugs and ch['result'] == 'absent' for ch in x['checked']):
            caveats.setdefault(str(p['n']), 'fact-check %s: the outlet capture does not state the claim as worded ("absent"); see ledger %s' % (x['run'], cid))
        points.append({'n': p['n'], 'request_id': None, 'status': p['status'], 'claim_ids': [cid], 'blocked_by': sorted(p.get('depends_on') or []),
                       'claim_text': claim_by_id[cid]['claim'] if cid in claim_by_id else None,
                       'their_words': tw, 'primary': primary_for([cid]), 'suggested': p.get('suggested'),
                       'verdict': x['verdict'] if x else None, 'held_reason': p.get('held_reason')})
    nxt = max([p['n'] for p in points if p['n']] + [0])
    for p in points:
        if not p['n']:
            nxt += 1; p['n'] = nxt
    points.sort(key=lambda p: p['n'])
    req_counts = {}
    for p in points:
        req_counts[p['status']] = req_counts.get(p['status'], 0) + 1

    channel = {'name': None, 'kind': None, 'url': None, 'captured': None}
    if reqs:
        ch = reqs[0].get('channel') or {}
        channel = {'name': ch.get('note') or ch.get('name'), 'kind': ch.get('kind'), 'url': ch.get('url'), 'captured': ch.get('captured')}

    # ---- timeline ----
    tl = []
    for e in timeline:
        sl = e.get('sources') or []
        lane = 'outlet' if sl and set(sl) <= slugs else 'world'
        tl.append({'t': e['at'], 'lane': lane, 'what': e['event'], 'source': sl[0] if sl else None, 'sources': sorted(sl)})
    for slug in outlet_sources:
        pub = srcmap[slug].get('published')
        if pub and re.match(r'\d{4}-\d\d-\d\dT', pub) and not any(x['lane'] == 'outlet' and x['source'] == slug and x['t'][:16] == pub[:16] for x in tl):
            tl.append({'t': pub, 'lane': 'outlet', 'what': '%s: source published (%s)' % (srcmap[slug]['publisher'], srcmap[slug]['title']), 'source': slug, 'sources': [slug]})
    tl.sort(key=lambda x: (tkey(x['t']), x['lane'], x['what']))

    # ---- graph: ego subgraph, 1 hop, plus claims' sources ----
    seeds = set(outlet_sources and ['source:' + s for s in outlet_sources])
    if pnode:
        seeds.add(pid)
    seeds &= set(node)
    N = set(seeds)
    for e in graph['edges']:
        if e['from'] in seeds: N.add(e['to'])
        if e['to'] in seeds: N.add(e['from'])
    for e in graph['edges']:
        if e['verb'] == 'cites' and e['from'] in N and e['from'].startswith('claim:'):
            N.add(e['to'])
    N &= set(node)
    gedges = sorted(({k: v for k, v in e.items() if k in ('from', 'verb', 'to', 'basis')} for e in graph['edges'] if e['from'] in N and e['to'] in N),
                    key=lambda e: (e['from'], e['verb'], e['to']))
    gnodes = []
    for nid in sorted(N):
        n = node[nid]
        o = {'id': nid, 'kind': n['kind'], 'label': n.get('label'), 'class': n.get('class'), 'href': n.get('href')}
        if nid.startswith('claim:') and nid[6:] in assess:
            o['verdict'] = assess[nid[6:]]['verdict']
            o['status'] = claim_by_id.get(nid[6:], {}).get('status')
        if nid.startswith('source:'):
            o['url'] = n.get('url'); o['published'] = n.get('published'); o['primary'] = n.get('primary')
        o['own'] = nid in seeds
        gnodes.append(o)

    # ---- echo (from notes) ----
    echo, injection = [], []
    for s in sources:
        if s['slug'] in slugs:
            continue
        txt = (s.get('notes') or '') + '\n' + (s.get('notes_md') or '')
        m = termrx.search(txt)
        if not m:
            continue
        i = max(0, m.start() - 110)
        ex = re.sub(r'\s+', ' ', txt[i:m.end() + 150]).strip()
        echo.append({'source': s['slug'], 'publisher': s.get('publisher'), 'lang': s.get('lang'), 'published': s.get('published'),
                     'claims': sorted(c['id'] for c in my_claims if s['slug'] in c['sources']),
                     'relation': 'primary-source note' if s.get('primary') else 'secondary',
                     'note_excerpt': ex})
    echo.sort(key=lambda e: e['source'])

    # injection scan over free text read
    def scan(where, txt):
        mm = INJ.search(txt or '')
        if mm:
            injection.append({'where': where, 'match': mm.group(0)})
    for slug in outlet_sources:
        scan('sources.json:%s notes' % slug, (srcmap[slug].get('notes') or '') + (srcmap[slug].get('notes_md') or ''))
    for e in echo:
        s = srcmap[e['source']]; scan('sources.json:%s notes' % e['source'], (s.get('notes') or '') + (s.get('notes_md') or ''))
    for c in my_claims:
        scan('claims.json:%s' % c['id'], c['claim'] + ' ' + (c.get('note') or ''))
    for r in reqs:
        scan('outreach.json:%s' % r['id'], json.dumps(r))

    # ---- not asked ----
    na = [{'claim_id': x['claim_id'], 'reason': x['reason']} for x in ed.get('not_asked', [])]
    for x in outreach.get('not_asked', []):
        if x['source'] in slugs or (pubrx and pubrx.search(x['publisher'])) or (a.actor and x['publisher'].lower() == name.lower()):
            na.append({'claim_id': None, 'reason': '%s (%s): "%s" - %s' % (x['publisher'], x['source'], x['words'], x['why'])})
    na.sort(key=lambda x: (x['claim_id'] or '~', x['reason']))

    # ---- changes strip ----
    ch = []
    for c in vault_caps:
        ch.append({'t': stamp_iso(c['stamp']), 'what': 'capture %s of %s recorded%s' % (c['stamp'], c['source'], ' (partial: ' + '; '.join(c['flags']) + ')' if c['flags'] else '')})
    for r in reqs:
        for l in r.get('log', []):
            ch.append({'t': l['at'], 'what': '%s: %s' % (r['id'], l['event'])})
    for r in ledger:
        if r['factcheck']:
            ch.append({'t': stamp_iso(r['factcheck']['as_of']), 'what': 'fact-check of %s: %s' % (r['claim_id'], r['factcheck']['verdict'])})
    ch.sort(key=lambda x: (tkey(x['t']), x['what']))

    # ---- as_of / version ----
    newest = max([stamp_iso(c['stamp']) for c in vault_caps] + [stamp_iso(r['factcheck']['as_of']) for r in ledger if r['factcheck']] or [''])
    ver = a.data_version
    if not ver:
        for p in (os.path.join(a.data, '..', 'VERSION'), os.path.join(a.data, 'VERSION')):
            if os.path.exists(p):
                ver = open(p).read().strip(); break
    ver = ver or graph.get('version')
    latest_cap = vault_caps[-1]['stamp'] if vault_caps else None

    out = {
     'outlet': {'id': oid, 'name': name, 'kind': kind, 'actor': a.actor, 'channel': channel},
     'as_of': a.as_of or newest, 'data_version': ver,
     'summary': {'sources': len(outlet_sources), 'captures': len(captures), 'captures_vault': len(vault_caps),
                 'latest_capture': latest_cap, 'claims': len(ledger), 'by_verdict': dict(sorted(by_verdict.items())),
                 'requests': dict(sorted(req_counts.items()))},
     'points': points, 'ledger': ledger,
     'captures': captures, 'timeline': tl,
     'graph': {'nodes': gnodes, 'edges': gedges},
     'echo': echo, 'not_asked': na, 'changes': ch,
     'method': {
        'data_commit': a.data_commit, 'data_repo': 'sgit-ai__website__newsroom__2026__oct__php__data',
        'generator': 'records/projects/PROJECT-001/phase-2/outlets/build_outlet.py',
        'source_rules': rules, 'sources': outlet_sources,
        'party_node': pid if pnode else None,
        'echo': {'from': 'notes and notes_md of sources.json, not the graph', 'terms': terms,
                 'rule': 'case-insensitive, word-boundary match; the outlet\'s own sources excluded; claims = ledger claims the echo source also cites (graph-backed), not claims named in the notes',
                 'found': len(echo)},
        'points': {'requests': 'outreach.json requests with actor == outlet actor, or whose said[].source is an outlet source, or whose publisher matches --publisher-match',
                   'proposed': 'carried by hand from the editor\'s briefing (editorial file), request_id null, not graded here; verdict is the fact-check verdict of the linked claim',
                   'their_words': 'the outlet\'s words as the fact-check desk quoted them from the capture (checked[] result carries/partial); null when the capture does not carry them',
                   'primary': 'the contradiction record\'s first statement not made by the outlet, else the first fact-check check on a non-outlet source, primary sources before secondary',
                   'caveats': caveats, 'editorial_file': a.editorial},
        'timeline': 'lane outlet = timeline.json entries all of whose sources are the outlet\'s, plus the source published time when no such entry shares its minute; lane world = every other timeline.json entry (all 69 in the data; filter by t)',
        'ledger': 'every claim in claims.json citing an outlet source, with factcheck.json assessment joined; by_verdict counts the fact-check verdict',
        'counts': {'sources': len(outlet_sources), 'captures_vault': len(vault_caps), 'captures_total': len(captures), 'claims': len(ledger),
                   'graph_nodes': len(gnodes), 'graph_edges': len(gedges), 'echo': len(echo), 'points': len(points)},
        'limits': ['echo is read from free-text notes, not from graph edges; party:%s has no incoming edge from the echo sources' % (a.actor or oid),
                   'the outlet\'s own entries (posts) are not in the data: only the source\'s published time and timeline.json entries that cite it; the raw __INITIAL_DATA__ posts are in the vault, not here',
                   'no capture is later than the newest in captures; the page cannot say what the outlet\'s page says now',
                   'capture content is never copied: stamps and file hashes only'],
        'injection_seen': injection}}
    with open(a.out, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('%s: sources %d captures %d claims %d verdicts %s points %d echo %d graph %d/%d' % (
        oid, len(outlet_sources), len(captures), len(ledger), dict(sorted(by_verdict.items())), len(points), len(echo), len(gnodes), len(gedges)))

main()
