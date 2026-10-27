import json,re,sys
W='clones/watch-pack'; E='clones/evidence-pack'
q=json.load(open(W+'/index/promote.json'))
idx=json.load(open(E+'/sources/index.json')); rows=idx if isinstance(idx,list) else idx.get('sources',idx)
have={r['url'].rstrip('/') for r in rows}
done={r['slug'] for r in json.load(open(E+'/notes/promotions__curator.json'))['rows']}
pend=[r for r in q['rows'] if r['slug'] not in done and r['url'].rstrip('/') not in have]
pend.sort(key=lambda r:(r['priority'],r['slug']))
a,b,lim=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
for r in pend[a:b]:
    t=open(W+'/'+r['snapshot_path']+'/text.txt',errors='replace').read(); t=re.sub(r'[ \t]+',' ',re.sub(r'\s*\n\s*','\n',t))
    print('=====',r['slug'],len(t)); print(t[:lim])
