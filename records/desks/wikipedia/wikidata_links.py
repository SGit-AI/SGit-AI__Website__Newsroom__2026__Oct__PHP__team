"""Look every party of data/entities.json up on Wikidata and keep the candidates, so a party can carry its Wikidata item.

Kept by the ontologist. Standard library only; read-only against Wikidata, one request every two seconds. Writes
data/wikidata-links.json: for each party, the search's top candidates (id, label, description) and, where exactly
one candidate's description fits the party's kind by a plain word test, a proposed item. A proposal is not a link:
the ontologist confirms each one by hand (confirmed: true) in the same file, and the build reads only confirmed
links. The editor's direction (25 October 2026): use the data Wikidata already has, especially for the parties that
are already there, and watch it change.

    python3 records/desks/wikipedia/wikidata_links.py            # parties not searched yet (Wikidata rate-limits: about 20 s a party)
    python3 records/desks/wikipedia/wikidata_links.py --all      # every party again (confirmations are kept)
"""
import json, os, re, sys, time, urllib.parse, urllib.request

# The six repositories (26 October 2026): this script lives in team; the data it reads and writes is in the data
# repository (files/), and the parser is the press's (build/wikitext.py). Both are found beside this clone, or at
# NEWSROOM_DATA and NEWSROOM_PRESS.
TEAM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
_SIB = os.path.dirname(TEAM)
DATA = os.environ.get('NEWSROOM_DATA') or os.path.join(_SIB, 'sgit-ai__website__newsroom__2026__oct__php__data')
PRESS = os.environ.get('NEWSROOM_PRESS') or os.path.join(_SIB, 'sgit-ai__website__newsroom__2026__oct__php__press')
FILES = os.path.join(DATA, 'files')
if not os.path.isdir(FILES):
    sys.exit(f'the data repository is not at {DATA} (clone SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__data beside team, or set NEWSROOM_DATA)')
OUT = os.path.join(FILES, 'wikidata-links.json')
WD_API = 'https://www.wikidata.org/w/api.php'
UA = 'php-newsroom-ontologist/1.0 (https://php.oct.2026.newsroom.sgit.ai/wikipedia/; read-only; one request every two seconds)'
# words a candidate's description should carry for a party of this kind; a miss leaves the candidate unproposed
FIT = {'outlet': ('newspaper', 'news', 'magazine', 'website', 'broadcaster', 'media', 'publication', 'television', 'radio', 'journal', 'daily', 'press'),
       'agency': ('agency', 'government', 'authority', 'office', 'centre', 'center', 'team', 'cert', 'ministry', 'department', 'organization', 'organisation'),
       'organisation': ('company', 'organization', 'organisation', 'firm', 'foundation', 'corporation', 'university', 'council', 'business', 'provider', 'vendor', 'group', 'project', 'nonprofit', 'non-profit', 'institute'),
       'person': ('researcher', 'journalist', 'engineer', 'scientist', 'developer', 'executive', 'founder', 'professor', 'writer', 'hacker', 'programmer', 'author', 'person'),
       'platform': ('platform', 'website', 'service', 'social', 'forum', 'software'), 'project': ('software', 'project', 'language', 'website', 'library'),
       'registry': ('database', 'program', 'registry', 'catalog', 'list'), 'group': ()}


def get(params):
    url = WD_API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code not in (429, 503) or attempt == 5:
                raise
            time.sleep(int(e.headers.get('Retry-After') or 0) or 5 * 2 ** attempt)
    time.sleep(2.0)
    return json.loads(raw.decode('utf-8'))


def query_name(e):
    """The name to search: the entity's name without its parenthetical and role suffixes."""
    n = re.sub(r'\s*\(.*?\)\s*', ' ', e['name'])
    n = re.split(r',| / | and the | on X', n)[0]
    return n.strip()


def main():
    ent = json.load(open(os.path.join(FILES, 'entities.json'), encoding='utf-8'))['entities']
    links = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {'about': __doc__.strip().split('\n')[0], 'kept_by': 'ontologist', 'parties': {}}
    P = links['parties']
    for e in ent:
        if e['kind'] in ('unnamed', 'this-site'):
            continue
        cur = P.get(e['id'])
        if cur and cur.get('searched') and '--all' not in sys.argv:
            continue  # searched already; a proposal waits for the ontologist's hand, not another search
        q = query_name(e)
        res = get(dict(action='wbsearchentities', search=q, language='en', limit=5, format='json')).get('search', [])
        cands = [{'id': r['id'], 'label': r.get('label'), 'description': r.get('description')} for r in res]
        fit = [c for c in cands if c.get('description') and any(w in c['description'].lower() for w in FIT.get(e['kind'], ()))]
        exact = [c for c in fit if (c.get('label') or '').lower() == q.lower()]
        proposed = exact[0]['id'] if len(exact) == 1 else (fit[0]['id'] if len(fit) == 1 else None)
        rec = {'query': q, 'kind': e['kind'], 'candidates': cands, 'proposed': proposed, 'searched': time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())}
        if cur and cur.get('confirmed') is not None:
            rec['confirmed'] = cur['confirmed']; rec['item'] = cur.get('item')
        else:
            rec['confirmed'] = None; rec['item'] = None
        P[e['id']] = rec
        json.dump(links, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        print(f'{e["id"]:28} {q[:30]:30} -> {proposed or "-":12} {len(cands)} candidates')
    n = sum(1 for p in P.values() if p.get('proposed')); c = sum(1 for p in P.values() if p.get('confirmed'))
    print(f'{len(P)} parties searched; {n} proposals; {c} confirmed')


if __name__ == '__main__':
    main()
