# The nightly pass's scan, kept by security@php.newsroom: secret shapes (the press's build/security_check.py SECRET_KINDS, named, never printed), hidden characters and text addressed to a model, over every folder given.
# Usage: python3 -I scan.py <press clone>/build/security_check.py is read from /home/user/ro/press; pass the folders to scan. Prints the kind and the files, never a match.
import sys, os, re, importlib.util
spec=importlib.util.spec_from_file_location('sc','/home/user/ro/press/build/security_check.py'); sc=importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
pats=[(n,re.compile(p)) for n,p in sc.SECRET_KINDS] if isinstance(sc.SECRET_KINDS[0],tuple) else None
ZW=re.compile('[​-‏⁠﻿‪-‮]')
AI=re.compile(r'(ignore (all )?(previous|prior|above) instructions|you are an? (ai|assistant|language model)|as an ai|system prompt|(dear|attention|note to) (ai|claude|llm|agent)s?\b)',re.I)
for root in sys.argv[1:]:
    hits={}
    for dp,dn,fn in os.walk(root):
        dn[:]=[d for d in dn if d not in ('.git','.sg_vault')]
        for f in fn:
            p=os.path.join(dp,f)
            if os.path.getsize(p)>3_000_000: continue
            try: t=open(p,encoding='utf-8').read()
            except Exception: continue
            for n,r in pats:
                for m in r.finditer(t): hits.setdefault(('secret',n),[]).append(os.path.relpath(p,root))
            if ZW.search(t) and not p.endswith(('.js','.css')): hits.setdefault(('hidden-char',''),[]).append(os.path.relpath(p,root))
            for m in AI.finditer(t): hits.setdefault(('addresses-ai',m.group(0).lower()[:40]),[]).append(os.path.relpath(p,root))
    print('==',root)
    for k,v in sorted(hits.items()): print(' ',k,len(v),sorted(set(v))[:6])
