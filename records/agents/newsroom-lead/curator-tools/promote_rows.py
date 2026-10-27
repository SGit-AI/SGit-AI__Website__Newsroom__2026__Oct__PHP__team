"""Promote queue rows from a spec file (written after reading each capture). Usage: promote_rows.py SPEC.json
Dry pass first (quote verbatim in the capture, claim ids unused, URL not already held, slug free); writes only if all pass."""
import json, os, re, subprocess, sys, datetime
W='clones/watch-pack'; E='clones/evidence-pack'; VAULT='7r83qic5'
spec=json.load(open(sys.argv[1]))
q=json.load(open(W+'/index/promote.json')); byslug={r['slug']:r for r in q['rows']}
norm=lambda s: re.sub(r"[‘’“”\"]","'",re.sub(r'\s+',' ',s))
idx=json.load(open(E+'/sources/index.json')); rows=idx if isinstance(idx,list) else idx.get('sources',idx)
have_url={r['url'].rstrip('/') for r in rows}; have_slug={r['slug'] for r in rows}
claims=json.load(open(E+'/claims/curator@php.newsroom.json')); tl=json.load(open(E+'/timeline/curator@php.newsroom.json'))
cids={c['id'] for c in claims}; prog=json.load(open(E+'/notes/promotions__curator.json'))
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def resolve(pfx):
    if pfx in byslug: return byslug[pfx]
    m=[k for k in byslug if k.startswith(pfx)]; assert len(m)==1,('slug prefix',pfx,m); return byslug[m[0]]
plan=[]; skipped=[]
for s in spec:
    r=resolve(s['slug'])
    if s.get('skip'): skipped.append((r,s['skip'])); continue
    s['slug']=r['slug']; d=W+'/'+r['snapshot_path']
    assert r['url'].rstrip('/') not in have_url and r['slug'] not in have_slug, ('already held',r['slug'])
    text=open(d+'/text.txt',errors='replace').read()
    for k in ('quote_original',):
        assert norm(s[k]) in norm(text), ('QUOTE NOT VERBATIM',r['slug'],s[k][:80])
    for c in s.get('claims',[]): assert c[0] not in cids,c[0]; cids.add(c[0])
    plan.append((s,r,d))
new_claims=[]; new_tl=[]; done=[]
for s,r,d in plan:
    slug=r['slug']; snap=r['snapshot']; row=dict(r,_vault=VAULT)
    p=subprocess.run([sys.executable,'-I','tools/promote_files.py',W,E,json.dumps(row)],capture_output=True,text=True)
    if p.returncode: sys.exit(p.stdout+p.stderr)
    meta=json.load(open(d+'/meta.json')); title=meta.get('title') or slug
    published=s.get('published') or meta.get('published') or 'not stated in the capture'
    src={'slug':slug,'url':r['url'],'publisher':r['publisher'],'kind':'news','title':title,'published':published,'captures':[snap],'status':'captured','primary':False,'added_by':'curator@php.newsroom','lang':r['lang'],
         'notes':f"Promoted from the source watch (pack copy {VAULT}), snapshot {snap}, queue priority {r['priority']} (mechanical selection by researcher@php.newsroom, read by the curator). {s['summary'][:150].rstrip()}..."}
    o=f'{E}/sources/{slug}'
    json.dump(src,open(o+'/source.json','w'),indent=1,ensure_ascii=False); open(o+'/source.json','a').write('\n')
    tr=''; tp='%s/translations/%s.json'%(W,r['watch_page'])
    if os.path.exists(tp):
        t=json.load(open(tp)); tr=f"\n_The watch reader's summary (researcher@php.newsroom, of its snapshot {t.get('snapshot')}, not necessarily this one):_ {t.get('summary_en','')}\n"
    qen=s.get('quote_en'); qb=f"> {s['quote_original']}\n"+(f"\n_Curator's translation:_ \"{qen}\"\n" if qen else '')
    open(o+'/notes.md','w').write(f"""# {title}

Promoted by curator@php.newsroom from the source watch (vault `oq9gflln`, read from its pack copy `{VAULT}`), page `{r['watch_page']}`, snapshot `{snap}`. Copied byte for byte; every file's sha256 is in `captures/{snap}/provenance.json` and was re-checked against the watch's own hashes.

## What the page says

_Curator's reading of the capture._

{s['summary']}

{qb}{tr}
## Why it is here

From the promotion queue (`index/promote.json`, priority {r['priority']}): {r['why']}

## Capture notes

Language `{r['lang']}`. {s.get('capture_note') or 'Nothing in the page addresses an AI or hides text from a reader.'}
""")
    for (cid,ct,by,st,topic,note) in s.get('claims',[]): new_claims.append({'id':cid,'claim':ct,'by':by,'sources':[slug],'status':st,'topic':topic,'note':note})
    for (at,ev,conf,ph) in s.get('timeline',[]): new_tl.append({'at':at,'event':ev,'sources':[slug],'confidence':conf,'phase':ph})
    prog['rows'].append({'slug':slug,'snapshot':snap,'watch_snapshot_path':r['snapshot_path'],'priority':r['priority'],'status':'promoted','at':now,'queue':'pack vault '+VAULT+' (written '+q['written']+')'})
    done.append(slug)
for r,why in skipped:
    prog['rows'].append({'slug':r['slug'],'snapshot':r['snapshot'],'watch_snapshot_path':r['snapshot_path'],'priority':r['priority'],'status':'skipped: '+why,'at':now,'queue':'pack vault '+VAULT+' (written '+q['written']+')'})
json.dump(claims+new_claims,open(E+'/claims/curator@php.newsroom.json','w'),indent=1,ensure_ascii=False)
json.dump(tl+new_tl,open(E+'/timeline/curator@php.newsroom.json','w'),indent=1,ensure_ascii=False)
json.dump(prog,open(E+'/notes/promotions__curator.json','w'),indent=1,ensure_ascii=False)
print(len(skipped),'skipped;',len(done),'promoted',len(new_claims),'claims',len(new_tl),'timeline rows'); open(sys.argv[1]+'.done','w').write(json.dumps(done))
