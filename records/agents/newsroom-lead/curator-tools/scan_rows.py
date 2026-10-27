import json,re,gzip,os,sys,collections
W='clones/watch-pack'
q=json.load(open(W+'/index/promote.json')); spec=json.load(open(sys.argv[1]))
inv=re.compile('[​-‏⁠-⁤﻿\U000e0000-\U000e007f]')
ai=re.compile(r"(claude|chatgpt|codex|copilot|assistant|language model|\bLLM\b|ignore (all|previous|the above)|ignorez|ignoriere|disregard|system prompt|tu es un|you are an? |act as|as an ai|new instructions|do not tell|override)",re.I)
for s in spec:
    m=[r for r in q['rows'] if r['slug']==s['slug']] or [r for r in q['rows'] if r['slug'].startswith(s['slug'])]; assert len(m)==1,s['slug']; m=m[0]; d=W+'/'+m['snapshot_path']
    t=open(d+'/text.txt',errors='replace').read()
    h=gzip.decompress(open(d+'/page.html.gz','rb').read()).decode('utf8','replace') if os.path.exists(d+'/page.html.gz') else ''
    cm=[c.strip()[:90] for c in re.findall(r'<!--(.{0,300}?)-->',h,re.S) if ai.search(c)]
    chars=collections.Counter(hex(ord(c)) for c in inv.findall(t))
    hits=[re.sub(r'\s+',' ',t[max(0,x.start()-60):x.end()+60]) for x in ai.finditer(t)][:2]
    print(m['slug'][:40].ljust(40),'inv-text',dict(chars),'| comments',cm[:1],'| hits',hits)
