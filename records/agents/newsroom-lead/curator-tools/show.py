import json,re,sys
W='clones/watch-pack'
q=json.load(open(W+'/index/promote.json'))
for s in sys.argv[2:]:
    r=[x for x in q['rows'] if x['slug'].startswith(s)][0]
    t=open(W+'/'+r['snapshot_path']+'/text.txt',errors='replace').read()
    t=re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+','\n',t))
    n=int(sys.argv[1])
    print('=====',r['slug'],'|',r['url']);import os;o=int(os.environ.get("OFF","0"));m=re.search(r'php2shell|CVE-2026-10961',t,re.I);b=max(0,m.start()-250) if (m and o==0) else o;print(t[b:b+n]);print()
