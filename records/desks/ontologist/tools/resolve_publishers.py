# Turns the pass's unresolved publishers into entities in the data repository's files/entities.json (27 October 2026, the ontologist's session).
# Usage: python3 resolve_publishers.py <tsv of 'publisher<TAB>https://host'> after the pass lists them. The O table holds the overrides for names the pass
# has met (kind, country, hosts, notes where a name misleads, merges into existing parties); add rows for new names, read each page first.
# DATA below is the data clone's path; edit it if the clone is elsewhere.
import json,re,collections,sys
DATA='/home/user/sgit-ai__website__newsroom__2026__oct__php__data/files/entities.json'
D=json.load(open(DATA,encoding='utf-8'),object_pairs_hook=collections.OrderedDict); E=D['entities']; by={e['id']:e for e in E}
rows=[l.rstrip('\n').split('\t') for l in open(sys.argv[1],encoding='utf-8')]
CC={'it':'IT','tr':'TR','de':'DE','fr':'FR','es':'ES','pl':'PL','id':'ID','vn':'VN','br':'BR','pt':'PT','jp':'JP','kr':'KR','cn':'CN','tw':'TW','hk':'HK','th':'TH','gr':'GR','hu':'HU','ro':'RO','cz':'CZ','lv':'LV','at':'AT','ch':'CH','uk':'UK','my':'MY','re':'FR','in':'IN','ph':'PH','co':'CO','cl':'CL','sa':'SA','kw':'KW','qa':'QA','bh':'BH','tv':'','ai':'','io':'','com':'','org':'','net':'','info':'','jp':'JP'}
SECOND={'co','com','ne','or','ac','org','gov','net','go'}
def reg(h):
    h=re.sub(r'^(www\d?|m)\.','',h); p=h.split('.')
    if len(p)>=3 and p[-2] in SECOND and len(p[-1])==2: return '.'.join(p[-3:])
    return '.'.join(p[-2:])
# overrides: name -> dict(id, kind, country, hosts(list; default registrable), note, merge)
O={
'The Guardian':dict(merge='guardian'),'CloudLinux':dict(merge='cloudlinux'),'notebookcheck':dict(merge='notebookcheck',hosts=['notebookcheck.info']),'notebookcheck-cn':dict(merge='notebookcheck',hosts=['notebookcheck-cn.com']),
'BeInCrypto':dict(id='beincrypto',name='BeInCrypto',hosts=['beincrypto.com'],al=['BeInCrypto Polska','BeInCrypto Việt Nam'],country='US',note='A crypto-news network with national editions (nl., pl., vn.); the three publisher strings are one party.'),
'BeInCrypto Polska':dict(skip=True),'BeInCrypto Việt Nam':dict(skip=True),
'NPR':dict(country='US'),'Computing':dict(country='UK'),'CPO Magazine':dict(country='US'),'CIOL':dict(country='IN'),'Malay Mail':dict(country='MY'),'Bitcoin News':dict(hosts=['news.bitcoin.com'],country='US'),'Unite.AI':dict(country='US'),'PC Gamer':dict(country='US'),'Radio World':dict(country='US'),'TV Tech':dict(country='US'),'Startup Fortune':dict(country='US'),
'World Socialist Web Site':dict(country='US',note='The outlet of the International Committee of the Fourth International, a political party: read its framing as that.'),
'Anadolu Ajansı':dict(kind='agency',country='TR',note='Turkey\'s state news agency; a wire, so its copy is syndicated by other Turkish outlets.'),
'learn':dict(id='microsoft-learn',name='Microsoft Learn',kind='organisation',hosts=['learn.microsoft.com'],country='US',note="Microsoft's documentation site; the publisher string 'learn' is the site's own metadata, not a person or outlet."),
'トレンドマイクロ':dict(id='trend-micro',name='Trend Micro',kind='organisation',country='JP',al=['Trend Micro'],hosts=['trendmicro.com'],note='A security vendor; the Japanese-language pages are its own.'),
'PR TIMES':dict(kind='platform',country='JP',note='A press-release distribution service: the issuing company states, PR TIMES relays.'),
'アットプレス':dict(id='atpress',name='アットプレス (@Press)',kind='platform',country='JP',note='A press-release distribution service: the issuing company states, it relays.'),
'デジタルPRプラットフォーム':dict(kind='platform',country='JP',note='A press-release distribution service: the issuing company states, it relays.'),
'NEWSCAST':dict(kind='platform',country='JP',note='A press-release and event-information site: the issuing company states, it relays.'),
'PresseBox':dict(kind='platform',country='DE',note='A press-release distribution service: the issuing company states, it relays.'),
'PC Watch':dict(hosts=['pc.watch.impress.co.jp'],country='JP',note='An outlet of Impress; distinct from INTERNET Watch.'),
'ZDNET Japan':dict(hosts=['japan.zdnet.com'],country='JP',note='The Japanese edition; not the US ZDNET.'),
'Kompas Tekno':dict(hosts=['tekno.kompas.com'],country='ID'),'Bisnis Tekno':dict(hosts=['teknologi.bisnis.com'],country='ID'),
'腾讯网':dict(id='tencent-news',name='腾讯网 (Tencent News)',hosts=['news.qq.com'],country='CN'),'同花顺财经股票频道':dict(id='10jqka',hosts=['stock.10jqka.com.cn'],country='CN'),
'IT168 软件·学院':dict(hosts=['software.it168.com'],country='CN'),'周刊':dict(),
'周刊':dict(),'주간한국':dict(hosts=['weekly.hankooki.com'],country='KR'),
'stadt bremerhaven':dict(id='caschys-blog',name='Caschys Blog',al=['stadt bremerhaven'],hosts=['stadt-bremerhaven.de'],country='DE',note="The publisher string 'stadt bremerhaven' (a city's name) is the page's own metadata: the site at stadt-bremerhaven.de titles itself Caschys Blog, a German technology blog. Not the city's administration."),
'pl.martincid':dict(id='martincid-pl',name='Martin Cid Magazine PL',hosts=['pl.martincid.com'],country='PL',note='A Polish magazine (film, TV, music, technology); the publisher string is its host.'),
'wersm':dict(kind='organisation',country='US',note='A social-media agency: its post is the agency speaking.'),
'Stéphane Larue News':dict(country='FR'),'tech-noisy':dict(country='JP'),'www.tageskarte.io':dict(id='tageskarte',name='Tageskarte',hosts=['tageskarte.io'],country='DE'),
'schieb.de':dict(note="The blog of Jörg Schieb, a German technology journalist; his own site, not an outlet's."),
'Le Quotidien de la Réunion':dict(country='FR'),'Pplware':dict(country='PT'),'SempreUpdate':dict(country='BR'),'ConvergenciaDigital':dict(country='BR'),'SpaceMoney':dict(country='BR'),'UOL':dict(country='BR'),
'LAMPOST.CO':dict(country='ID'),'Notimérica':dict(country='ES'),'MONCLOA.COM':dict(country='ES'),'La Vanguardia':dict(country='ES'),'La Razón':dict(country='ES'),'MuyComputer':dict(country='ES'),'LISA News':dict(country='ES'),
'La Tercera':dict(country='CL'),'ENTER.CO':dict(country='CO'),
'Siam Blockchain':dict(country='TH'),'bangkokbiznews':dict(country='TH'),'learn':dict(id='microsoft-learn',name='Microsoft Learn',kind='organisation',hosts=['learn.microsoft.com'],country='US',note="Microsoft's documentation site; the publisher string 'learn' is the site's own metadata, not an outlet."),
'المصري لايت':dict(country='EG',hosts=['almasryalyoum.com']),'تركيا عاجل':dict(country='TR'),'جريدة البلاد':dict(country='BH'),'جريدة الجريدة الكويتية':dict(country='KW'),'جريدة الراية':dict(country='QA'),'رائج':dict(country='SA'),'عكاظ':dict(country='SA'),'وكالة خبر للأنباء':dict(country='IR'),
'Mynet':dict(country='TR'),'Takvim':dict(country='TR'),'TGRT Haber':dict(country='TR'),'mansethaber':dict(country='TR'),'turkiyedeisdunyasi':dict(country='TR'),'Technotoday':dict(country='TR'),'TeknoTalk':dict(country='TR'),'Teknoblog':dict(country='TR'),'Teknófilo':dict(country='TR'),
'Fortune Indonesia':dict(country='ID'),'Libertatea':dict(country='RO'),'Root.cz':dict(country='CZ'),'kursors':dict(country='LV'),
'Startup Fortune':dict(country='US'),'startupper':dict(country='GR'),'Οικονομικός Ταχυδρόμος':dict(country='GR'),'Világgazdaság':dict(country='HU'),'YugaTech':dict(country='PH'),
'Tia Sáng':dict(country='VN'),'Báo VietNamNet':dict(country='VN'),'VTV.vn':dict(country='VN'),'Báo Quân đội nhân dân':dict(country='VN'),
'Netzpolitik.org':dict(country='DE'),'tagesschau.de':dict(country='DE'),'WDR':dict(hosts=['wdr.de'],country='DE'),'Tages-Anzeiger':dict(country='CH'),
'ビジネス+IT':dict(country='JP'),'毎日新聞デジタル':dict(country='JP'),'搜狐':dict(country='CN'),'雷峰网':dict(country='CN'),'知新聞':dict(country='TW'),'電腦王阿達':dict(country='TW'),'香港 unwire.hk':dict(country='HK'),'新潟日報デジタルプラス':dict(country='JP'),'RBB TODAY':dict(country='JP'),
'The Guardian':dict(merge='guardian'),
}
O.update({
'AnNahar':dict(country='LB'),'EADaily':dict(country='RU',note='A Russian news site; its Russian-language pages are its own copy.'),'Evrensel':dict(country='TR'),'Kaldata.com':dict(country='BG'),
'Revista Sociedade Militar':dict(country='BR',note='A Brazilian military-affairs magazine: the page cited is about the Brazilian Army website going offline.'),
'SC Media':dict(hosts=['scworld.com'],country='US',note='SC Media, whose site is scworld.com.'),'Security NEXT':dict(country='JP'),'Sixactualités':dict(country='FR'),'Südostschweiz':dict(country='CH'),
'Telehealth.org':dict(kind='organisation',country='US',note='Read from its name and address only: the site answered with a bot challenge. A telehealth training and news publisher, not a security outlet.'),
'VOI':dict(country='ID'),"WWWhat's new":dict(id='wwwhatsnew',country='ES'),
'WeLiveSecurity':dict(kind='organisation',country='SK',note="ESET's security blog: the vendor speaking, not an independent outlet."),
'WinFuture.de':dict(country='DE'),'Xataka':dict(country='ES'),'XboxDynasty':dict(country='DE'),'ZDNET':dict(country='US',note='The US ZDNET; ZDNET Japan is a separate party.'),
'Ziua Veche':dict(country='RO'),'Zoom Tecnológico':dict(country='CL'),
'codebook.machinarecord':dict(id='machinarecord-codebook',name='Codebook (Machina Record)',hosts=['codebook.machinarecord.com'],country='JP',note='A Japanese threat-intelligence news blog; the cited page is a Silobreaker alert it relays.'),
'fr.cnet':dict(id='cnet-france',name='CNET France',hosts=['fr.cnet.com'],country='FR',note='The French edition; CNET US is a separate site.'),
'htxt.co.za':dict(id='htxt-africa',name='HTXT.africa',hosts=['htxt.co.za'],country='ZA'),
'mediamixi':dict(country='JP'),'upi':dict(id='upi',name='UPI',kind='agency',hosts=['upi.com'],country='US',note='United Press International, a wire: its copy is syndicated.'),
'xenospectrum':dict(country='JP'),'マイナビニュース':dict(hosts=['news.mynavi.jp'],country='JP',note='Mynavi News, the news site of Mynavi.'),'資安人科技網':dict(country='TW'),
})
def slug(n):
    s=re.sub(r'[^a-z0-9]+','-',n.lower().encode('ascii','ignore').decode()).strip('-'); return s
ids=set(by); added=0; merged=0; skipped=[]
for name,host in rows:
    o=O.get(name,{})
    if o.get('skip'): continue
    h=host.split('//',1)[1]; hosts=o.get('hosts') or [reg(h)]
    if o.get('merge'):
        e=by[o['merge']]
        for a in [name]+hosts:
            if a not in e['aliases']: e['aliases'].append(a)
        merged+=1; continue
    eid=o.get('id') or slug(name) or slug(hosts[0].split('.')[0])
    if not eid or eid in ids: eid=slug(hosts[0].replace('.','-')); 
    assert eid not in ids,(name,eid)
    tld=reg(h).split('.')[-1]; cc=o.get('country', CC.get(tld,''))
    e=collections.OrderedDict([('id',eid),('name',o.get('name',name)),('kind',o.get('kind','outlet'))])
    if cc: e['country']=cc
    al=[name]+o.get('al',[])+hosts
    if o.get('name') and o['name']!=name and o['name'] not in al: al.insert(0,o['name'])
    e['aliases']=list(dict.fromkeys(al))
    if o.get('note'): e['note']=o['note']
    E.append(e); by[eid]=e; ids.add(eid); added+=1
json.dump(D,open(DATA,'w',encoding='utf-8'),indent=1,ensure_ascii=False); open(DATA,'a').write('\n')
print('added',added,'merged',merged,'total',len(E))
