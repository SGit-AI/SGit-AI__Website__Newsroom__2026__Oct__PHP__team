"""The ontologist's pass: what in data/ the ontology does not yet resolve, and where the graphs do not join.

Read only: it writes nothing and prints a report; the build (admin/build/build.py) is what refuses to build when the
graph would break its grammar. Run it first on every pass (after admin/wikipedia/fetch.py), fix what it lists in
data/entities.json, data/attribution.json and data/crosswalk.json, then build. Standard library only.
Runbook: admin/ontologist/README.md. Brief: admin/content/briefs/2026-10-24__brief__the-ontologist.md.

    python3 admin/ontologist/pass.py            # the report
    python3 admin/ontologist/pass.py --strict   # exit 1 if anything would stop the build
"""
import collections, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def load(name):
    with open(os.path.join(ROOT, 'data', name + '.json'), encoding='utf-8') as f:
        return json.load(f)


def main():
    ent = load('entities')['entities']
    ids = {e['id'] for e in ent}
    alias = {a: e['id'] for e in ent for a in e.get('aliases', [])}
    att, ont, xw = load('attribution'), load('ontology'), load('crosswalk')
    src, claims, nums, expl, ags = load('sources'), load('claims'), load('numbers'), load('exploitation'), load('agencies')
    blocking, notes = [], []

    pubs = collections.Counter(s['publisher'] for s in src)
    for p in sorted(p for p in pubs if p not in alias):
        s = next(s for s in src if s['publisher'] == p)
        blocking.append(f'publisher with no entity: {p!r} ({pubs[p]} sources, e.g. {s["slug"]}, {s["url"]})')
    for c in claims:
        if c['id'] not in att['claims']:
            blocking.append(f'claim with no attribution: {c["id"]} (by: {c["by"]!r})')
    for n in nums:
        if n['id'] not in att['numbers']:
            blocking.append(f'number with no attribution: {n["id"]} (who: {n["who"]!r})')
    if len(expl) != len(att['exploitation']):
        blocking.append(f'exploitation rows: {len(expl)} in data, {len(att["exploitation"])} attributed')
    for i, (x, a) in enumerate(zip(expl, att['exploitation'])):
        if x['who'] != a['who']:
            blocking.append(f'exploitation row {i} moved: now {x["who"]!r}, attributed as {a["who"]!r}')
    for g in ags:
        if g['agency'] + '|' + g['country'] not in att['agencies']:
            blocking.append(f'agency not mapped: {g["agency"]}|{g["country"]}')
    classes = next(t for t in ont['taxonomy'] if t['id'] == 'signal-class')['maps']
    for k in sorted({x['kind'] for x in expl} - set(classes)):
        blocking.append(f'exploitation kind not in the signal-class map: {k!r}')
    refs = [x for part in ('claims', 'numbers') for r in att[part].values() for x in r['states'] + r.get('relays', [])]
    refs += [x for r in att['exploitation'] for x in r['states'] + r.get('relays', [])] + list(att['agencies'].values())
    refs += [r['syndicates'] for r in att.get('sources', {}).values()] + list(xw['parties'])
    for e in ent:
        refs += [e[k] for k in ('part_of', 'member_of', 'works_for') if e.get(k)] + e.get('by', []) + e.get('has_members', [])
    for r in sorted(set(refs) - ids):
        blocking.append(f'reference to an unknown entity: {r!r}')

    # not blocking: the long tail to look at by hand
    by_url = collections.defaultdict(list)
    for s in src:
        by_url[s['url'].rstrip('/')].append(s['slug'])
    for url, slugs in sorted(by_url.items()):
        if len(slugs) > 1:
            notes.append(f'one page, {len(slugs)} source rows: {", ".join(slugs)} ({url})')
    for e in ent:
        for s in src:
            if alias.get(s['publisher']) == e['id'] and e['kind'] == 'organisation' and s.get('kind') == 'government' and 'university' in (e.get('note', '') + e['name']).lower():
                notes.append(f'source {s["slug"]} is classed government; its publisher is {e["name"]}')
    cited = {s for c in claims + nums + expl for s in c['sources']} | {s for t in load('timeline') for s in t['sources']}
    uncited = [s['slug'] for s in src if s['slug'] not in cited]
    notes.append(f'{len(uncited)} of {len(src)} sources are cited by no claim, number, signal or event (captured, not yet traced)')
    vc = {s for c in load('vault-claims') for s in c.get('sources', [])}
    gap = sorted(vc - cited)
    if gap:
        notes.append(f'{len(gap)} sources the vault\'s own claims cite that no site row cites: ' + ', '.join(gap[:12]) + (' …' if len(gap) > 12 else ''))
    # Wikipedia: references no capture holds and publishers no entity claims (admin/build/wikitext.py reads the latest revision)
    wdir = os.path.join(ROOT, 'data', 'wikipedia')
    if os.path.isdir(wdir):
        sys.path.insert(0, os.path.join(ROOT, 'admin', 'build'))
        import wikitext
        from urllib.parse import urlsplit, unquote
        def nurl(u):
            u = unquote(u.strip()); x = urlsplit(u if '://' in u else 'https://' + u)
            h = x.netloc.lower()
            for p in ('www.', 'm.', 'edition.', 'amp.'):
                h = h[len(p):] if h.startswith(p) else h
            return (h + x.path.rstrip('/')).lower()
        srcs = {nurl(s['url']) for s in src}
        hosts = {a.lower() for e in ent for a in e.get('aliases', []) if '.' in a and ' ' not in a}
        for a in json.load(open(os.path.join(wdir, 'index.json'), encoding='utf-8'))['articles']:
            d = os.path.join(wdir, a['slug'])
            art = json.load(open(os.path.join(d, 'article.json'), encoding='utf-8'))
            rev = json.load(open(os.path.join(d, 'revisions', f'{art["latest_revid"]}.json'), encoding='utf-8'))
            X = wikitext.statements(rev['wikitext'])
            miss = [r for r in X['references'] if r.get('url') and nurl(r['url']) not in srcs]
            nopub = sorted({(r.get('publisher') or urlsplit(r['url']).netloc) for r in X['references'] if r.get('url') and not any(urlsplit(r['url']).netloc.lower().removeprefix('www.').endswith(h) for h in hosts)})
            notes.append(f'Wikipedia {a["title"]} (revision {art["latest_revid"]}): {len(miss)} of {sum(1 for r in X["references"] if r.get("url"))} references not captured in the vault: ' + ', '.join(r['url'][:60] for r in miss[:8]) + (' …' if len(miss) > 8 else ''))
            if nopub:
                blocking.append(f'Wikipedia {a["title"]}: references whose publisher no entity claims (add an alias or an entity): ' + ', '.join(nopub[:12]) + (' …' if len(nopub) > 12 else ''))
            un = [s for s in X['statements'] if not s['cited']]
            notes.append(f'Wikipedia {a["title"]}: {len(un)} of {len(X["statements"])} statements carry no reference; {art["revisions"]} revisions, latest {art["latest_revision"]}')
    unused = sorted(ids - set(alias.values()) - set(refs))
    notes.append(f'{len(ent)} entities; {len(unused)} named only by their own row (no source, no attribution, no link): ' + ', '.join(unused[:15]) + (' …' if len(unused) > 15 else ''))

    print(f'ontologist pass: {len(src)} sources, {len(pubs)} publisher spellings, {len(ent)} entities, '
          f'{len(claims)} claims, {len(nums)} numbers, {len(expl)} signals')
    print(f'\nWould stop the build ({len(blocking)}):')
    for b in blocking or ['nothing']:
        print('  -', b)
    print(f'\nTo look at ({len(notes)}):')
    for n in notes:
        print('  -', n)
    if '--strict' in sys.argv and blocking:
        sys.exit(1)


if __name__ == '__main__':
    main()
