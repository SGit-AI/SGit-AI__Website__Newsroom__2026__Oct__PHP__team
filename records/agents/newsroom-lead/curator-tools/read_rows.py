import json,re,sys,os,gzip
W='clones/watch-pack'; E='clones/evidence-pack'
q=json.load(open(W+'/index/promote.json'))
idx=json.load(open(E+'/sources/index.json')); rows=idx if isinstance(idx,list) else idx.get('sources',idx)
have={r['url'].rstrip('/') for r in rows}
done={r['slug'] for r in json.load(open(E+'/notes/promotions__curator.json'))['rows']}
pend=[r for r in q['rows'] if r['slug'] not in done and r['url'].rstrip('/') not in have]
pend.sort(key=lambda r:(r['priority'],r['slug']))
a,b=int(sys.argv[1]),int(sys.argv[2])
hit=re.compile(r'php2shell|CVE-2026-10961[89]',re.I)
ai=re.compile(r'\b(ignore (all|previous|prior)|as an? (ai|language model)|you are an? (ai|assistant)|system prompt|disregard (the|all|any))',re.I)
for r in pend[a:b]:
    d=W+'/'+r['snapshot_path']; t=open(d+'/text.txt',errors='replace').read(); t=re.sub(r'[ \t]+',' ',re.sub(r'\s*\n\s*','\n',t))
    m=json.load(open(d+'/meta.json'))
    lines=[l for l in t.split('\n') if hit.search(l)]
    print('=====',r['slug'],'|',r['lang'],'|',r['publisher'],'|',len(t),'chars | files',sorted(os.listdir(d)))
    print('WHY:',r['why'][:330],'| SUPPORTS:',r.get('supports'))
    print('TITLE:',(m.get('title') or '')[:150],'| published:',m.get('published'))
    for l in lines[:3]: print('  >',l[:330])
    print('  AI-hits:',[x.group(0) for x in ai.finditer(t)][:3])
