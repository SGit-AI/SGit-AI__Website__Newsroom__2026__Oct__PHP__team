"""Add queue rows whose URL the evidence vault already holds as NEW CAPTURES of that source (captures are additive).
Does not touch source.json or notes.md of the existing source. Scans each snapshot's text for text aimed at an AI and
for invisible-character runs; a flagged snapshot is skipped and reported, not copied. Hash-checks every file.
Usage: add_captures.py [--dry]"""
import datetime, gzip, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import promote_files as pf
W='clones/watch-pack'; E='clones/evidence-pack'; VAULT='7r83qic5'; DRY='--dry' in sys.argv
q=json.load(open(W+'/index/promote.json'))
idx=json.load(open(E+'/sources/index.json')); rows=idx if isinstance(idx,list) else idx.get('sources',idx)
byurl={r['url'].rstrip('/'):r for r in rows}
prog=json.load(open(E+'/notes/promotions__curator.json')); done={r['slug'] for r in prog['rows']}
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
strong=re.compile(r"(ignore (all |any )?(previous|prior|the above)|disregard (the |all |any )?(previous|above|instructions)|system prompt|you are (now )?an? (ai|assistant|language model)|as an ai|new instructions|ignorez (les|toutes)|ignoriere (alle|die)|tu es un assistant)",re.I)
inv=re.compile('[​-‏⁠-⁤﻿\U000e0000-\U000e007f]')
added=[]; flagged=[]; skipped_same=0
for r in q['rows']:
    if r['slug'] in done or r['url'].rstrip('/') not in byurl or not isinstance(r['snapshot'],str): continue
    s=byurl[r['url'].rstrip('/')]; capdir=f"{E}/sources/{s['slug']}/captures"
    if os.path.isdir(f"{capdir}/{r['snapshot']}"): skipped_same+=1; prog['rows'].append({'slug':r['slug'],'snapshot':r['snapshot'],'watch_snapshot_path':r['snapshot_path'],'priority':r['priority'],'status':'promoted: capture already in '+s['slug'],'evidence_slug':s['slug'],'at':now}); continue
    d=W+'/'+r['snapshot_path']; t=open(d+'/text.txt',errors='replace').read()
    bad=[m.group(0) for m in strong.finditer(t)][:2]; n_inv=len(inv.findall(t))
    if bad or n_inv>8: flagged.append((r['slug'],bad,n_inv)); continue
    if DRY: added.append((r['slug'],s['slug'],r['snapshot'])); continue
    row=dict(r,_vault=VAULT)
    prov,meta,dst,files=pf.promote(W,E,row,r['snapshot'],s['slug'],now)
    pf.write_prov(row,prov,meta,dst,files,s['slug'],r['snapshot'],now)
    p=json.load(open(dst+'/provenance.json')); p['queue_slug']=r['slug']; p['added_as']='a new capture of an existing source (one folder per URL)'
    json.dump(p,open(dst+'/provenance.json','w'),indent=1,ensure_ascii=False); open(dst+'/provenance.json','a').write('\n')
    prog['rows'].append({'slug':r['slug'],'snapshot':r['snapshot'],'watch_snapshot_path':r['snapshot_path'],'priority':r['priority'],'status':'promoted: new capture of '+s['slug'],'evidence_slug':s['slug'],'at':now,'queue':'pack vault '+VAULT+' (written '+q['written']+')'})
    added.append((r['slug'],s['slug'],r['snapshot']))
if not DRY: json.dump(prog,open(E+'/notes/promotions__curator.json','w'),indent=1,ensure_ascii=False)
print('dry' if DRY else 'written','| new captures',len(added),'| already captured',skipped_same,'| flagged and skipped',len(flagged))
for f in flagged: print('  FLAGGED',f)
json.dump(added,open('added_captures.json','w'))
