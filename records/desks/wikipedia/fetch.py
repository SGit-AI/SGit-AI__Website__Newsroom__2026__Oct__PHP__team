"""Fetch a Wikipedia article's every revision, its Wikidata item and the articles that link to it, into data/wikipedia/.

Kept by the ontologist (ontologist@php.newsroom). Brief: admin/content/briefs/2026-10-25__brief__wikipedia-as-an-anchor.md.
Standard library only. The build never fetches: it reads what this tool wrote, so the site stays deterministic and the
fetch is the one step that touches the open web. Everything fetched is material: the wikitext, the edit summaries and
the editors' names are stored as text and reach a page only through the build's escaping.

    python3 admin/wikipedia/fetch.py PHP2Shell            # new revisions since the last run, the item, the backlinks
    python3 admin/wikipedia/fetch.py PHP2Shell --all      # every revision again (after a change to what is stored)
    python3 admin/wikipedia/fetch.py Talk:PHP2Shell       # the talk page, the same way (kind 'talk', of the article)

What it writes, under data/wikipedia/<slug>/:
    article.json              the page, its Wikidata item, the latest revision seen, every fetch (time, bytes, sha256)
    revisions/<revid>.json    one file per revision: ids, time, editor, size, Wikipedia's sha1, the wikitext and its sha256
    wikidata.json             the item's claims with their property labels, as fetched
    wikidata-history.json     every revision of the item: when, who, which property the summary names
    links-in.json             the articles that link to this one
and data/wikipedia/index.json, the list of articles watched.

The text is Wikipedia's, CC BY-SA 4.0, by its contributors; the revision ids are the attribution. Anonymous editors
are recorded as anonymous: an IP address is never written (admin/security/REQUIREMENTS.md). Bidi and zero-width
characters are removed from the wikitext and counted in the revision's record, because the gate refuses them.
"""
import datetime, hashlib, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'data', 'wikipedia')
API = 'https://en.wikipedia.org/w/api.php'
WIKIDATA = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'
WD_API = 'https://www.wikidata.org/w/api.php'
UA = 'php-newsroom-ontologist/1.0 (https://php.oct.2026.newsroom.sgit.ai/wikipedia/; read-only; one request every two seconds)'
# the ranges are built from code points so that no such character sits in this file (the gate refuses them)
HIDDEN = re.compile('[%s]' % ''.join(f'{chr(a)}-{chr(b)}' for a, b in ((0xE0000, 0xE007F), (0x202A, 0x202E), (0x2066, 0x2069), (0x200B, 0x200D), (0x2060, 0x2064), (0xFEFF, 0xFEFF))))
IP = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$|^[0-9a-f:]{3,}$', re.I)
LOG = []


def get(url, params=None):
    if params:
        url += ('&' if '?' in url else '?') + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
            break
        except urllib.error.HTTPError as e:
            # the API asks for a pause (429) or is briefly unavailable: wait as it says, or longer each time
            if e.code not in (429, 503) or attempt == 5:
                raise
            wait = int(e.headers.get('Retry-After') or 0) or 5 * 2 ** attempt
            print(f'  {e.code} from {url[:60]}: waiting {wait}s', file=sys.stderr)
            time.sleep(wait)
    LOG.append({'url': url, 'at': now(), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
    time.sleep(2.0)
    return json.loads(raw.decode('utf-8'))


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def slug_of(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')


def editor_of(rev):
    """A registered editor's public username; anything else is 'anonymous' or 'hidden', never an address."""
    if rev.get('userhidden'):
        return {'name': 'hidden', 'kind': 'hidden'}
    name = rev.get('user') or ''
    if rev.get('anon') or IP.match(name) or not rev.get('userid'):
        return {'name': 'anonymous', 'kind': 'anonymous'}
    return {'name': name, 'kind': 'registered'}


def all_revisions(title):
    revs, cont = [], {}
    while True:
        q = get(API, dict(action='query', prop='revisions', titles=title, rvlimit=500, rvdir='newer',
                          rvprop='ids|timestamp|user|userid|size|sha1|comment|parentid|tags|flags', format='json', formatversion=2, **cont))
        page = q['query']['pages'][0]
        if page.get('missing'):
            sys.exit(f'no article called {title!r}')
        revs += page.get('revisions', [])
        if 'continue' not in q:
            return page, revs
        cont = {'rvcontinue': q['continue']['rvcontinue']}


def contents(revids):
    out = {}
    for i in range(0, len(revids), 50):
        batch = revids[i:i + 50]
        q = get(API, dict(action='query', prop='revisions', revids='|'.join(map(str, batch)), rvprop='ids|content', rvslots='main', format='json', formatversion=2))
        for page in q['query']['pages']:
            for r in page.get('revisions', []):
                out[r['revid']] = r['slots']['main'].get('content', '')
    return out


def wikidata(item):
    if not item:
        return None
    ent = get(WIKIDATA.format(item))['entities'][item]
    claims = {}
    for pid, cl in sorted(ent.get('claims', {}).items()):
        vals = []
        for c in cl:
            snak = c.get('mainsnak', {})
            dv = snak.get('datavalue', {}).get('value')
            if isinstance(dv, dict):
                v = dv.get('id') or dv.get('time') or dv.get('text') or dv.get('amount') or json.dumps(dv, sort_keys=True)
            else:
                v = dv
            vals.append({'value': v, 'rank': c.get('rank'), 'type': snak.get('datatype')})
        claims[pid] = vals
    ids = sorted(set(list(claims)) | {v['value'] for vs in claims.values() for v in vs if isinstance(v['value'], str) and re.match(r'^[PQ]\d+$', v['value'])})
    labels = {}
    for i in range(0, len(ids), 50):
        q = get(WD_API, dict(action='wbgetentities', ids='|'.join(ids[i:i + 50]), props='labels', languages='en', format='json'))
        for k, e in q.get('entities', {}).items():
            labels[k] = e.get('labels', {}).get('en', {}).get('value', k)
    return {'item': item, 'label': ent.get('labels', {}).get('en', {}).get('value'), 'description': ent.get('descriptions', {}).get('en', {}).get('value'),
            'modified': ent.get('modified'), 'sitelinks': sorted(ent.get('sitelinks', {})), 'claims': claims, 'labels': labels, 'fetched_at': now()}


def item_history(item):
    """Every revision of the Wikidata item: who changed which claim, when; the summaries name the property changed."""
    if not item:
        return None
    revs, cont = [], {}
    while True:
        q = get(WD_API, dict(action='query', prop='revisions', titles=item, rvlimit=500, rvdir='newer', rvprop='ids|timestamp|user|userid|size|comment|parentid|tags|flags', format='json', formatversion=2, **cont))
        page = q['query']['pages'][0]
        revs += [{'revid': r['revid'], 'parentid': r.get('parentid'), 'timestamp': r['timestamp'], 'editor': editor_of(r), 'size': r.get('size'), 'comment': HIDDEN.sub('', r.get('comment', '')), 'tags': r.get('tags', [])} for r in page.get('revisions', [])]
        if 'continue' not in q:
            return {'item': item, 'fetched_at': now(), 'revisions': revs}
        cont = {'rvcontinue': q['continue']['rvcontinue']}


def dbpedia(title):
    """Whether DBpedia, built from periodic dumps, has a resource for the title yet: a status, never the page."""
    url = 'https://dbpedia.org/resource/' + urllib.parse.quote(title.replace(' ', '_'))
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': UA, 'Accept': 'text/html'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            status = r.status
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception as e:
        status = str(e)[:60]
    time.sleep(2.0)
    return {'url': url, 'status': status, 'checked_at': now()}


def backlinks(title):
    links, cont = [], {}
    while True:
        q = get(API, dict(action='query', list='backlinks', bltitle=title, bllimit=500, blnamespace=0, format='json', formatversion=2, **cont))
        links += [b['title'] for b in q['query']['backlinks']]
        if 'continue' not in q:
            return sorted(links)
        cont = {'blcontinue': q['continue']['blcontinue']}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(__doc__)
    title = args[0]
    everything = '--all' in sys.argv
    slug = slug_of(title)
    d = os.path.join(OUT, slug)
    os.makedirs(os.path.join(d, 'revisions'), exist_ok=True)
    art_p = os.path.join(d, 'article.json')
    art = json.load(open(art_p, encoding='utf-8')) if os.path.exists(art_p) else {'slug': slug, 'fetches': []}

    page, revs = all_revisions(title)
    have = set() if everything else {int(f[:-5]) for f in os.listdir(os.path.join(d, 'revisions')) if f.endswith('.json')}
    want = [r['revid'] for r in revs if r['revid'] not in have]
    texts = contents(want)
    stripped = 0
    for r in revs:
        if r['revid'] not in texts:
            continue
        raw = texts[r['revid']]
        text = HIDDEN.sub('', raw)
        n = len(raw) - len(text)
        stripped += n
        rec = {'revid': r['revid'], 'parentid': r.get('parentid'), 'timestamp': r['timestamp'], 'editor': editor_of(r), 'size': r.get('size'),
               'sha1': r.get('sha1'), 'minor': bool(r.get('minor')), 'tags': r.get('tags', []), 'comment': HIDDEN.sub('', r.get('comment', '')),
               'hidden_chars_removed': n, 'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'wikitext': text}
        json.dump(rec, open(os.path.join(d, 'revisions', f'{r["revid"]}.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

    kind = 'talk' if title.startswith('Talk:') else 'article'
    props = get(API, dict(action='query', prop='pageprops|info', titles=title, format='json', formatversion=2))['query']['pages'][0]
    item = props.get('pageprops', {}).get('wikibase_item') if kind == 'article' else None
    wd = wikidata(item)
    if wd:
        json.dump(wd, open(os.path.join(d, 'wikidata.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        json.dump(item_history(item), open(os.path.join(d, 'wikidata-history.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    links = backlinks(title) if kind == 'article' else []
    if kind == 'article':
        json.dump({'title': title, 'fetched_at': now(), 'articles': links}, open(os.path.join(d, 'links-in.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        art['dbpedia'] = dbpedia(title)

    art.update({'title': title, 'kind': kind, 'of': slug_of(title.split(':', 1)[1]) if kind == 'talk' else None, 'pageid': page.get('pageid'), 'url': 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(title.replace(' ', '_')),
                'wikidata_item': item, 'licence': 'CC BY-SA 4.0, by the contributors to the English Wikipedia; each revision id is the attribution',
                'latest_revid': revs[-1]['revid'], 'revisions': len(revs), 'first_revision': revs[0]['timestamp'], 'latest_revision': revs[-1]['timestamp'],
                'editors': len({json.dumps(editor_of(r), sort_keys=True) for r in revs}), 'links_in': len(links)})
    art['fetches'].append({'at': now(), 'new_revisions': len(want), 'hidden_chars_removed': stripped, 'requests': LOG})
    json.dump(art, open(art_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    idx_p = os.path.join(OUT, 'index.json')
    idx = json.load(open(idx_p, encoding='utf-8')) if os.path.exists(idx_p) else {'about': 'The Wikipedia articles this site watches, fetched by admin/wikipedia/fetch.py; the build reads them from here.', 'articles': []}
    idx['articles'] = sorted({a['slug']: a for a in idx['articles'] + [{'slug': slug, 'title': title, 'kind': kind, 'of': art['of']}]}.values(), key=lambda a: a['slug'])
    json.dump(idx, open(idx_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'{title}: {len(revs)} revisions ({len(want)} new), item {item}, {len(links)} articles link in, {len(LOG)} requests, {stripped} hidden characters removed')


if __name__ == '__main__':
    main()
