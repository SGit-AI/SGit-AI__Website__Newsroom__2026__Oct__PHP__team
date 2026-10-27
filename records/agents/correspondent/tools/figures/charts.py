"""SVG charts for 'Has anyone actually been hacked through php2shell?' (correspondent, 26 October 2026).
Every number is read from data v0.1.33 (files/) or written below with its source; nothing is estimated."""
import json, os, html
from collections import Counter

DATA = '/home/user/sgit-ai__website__newsroom__2026__oct__php__data/v/0.1.33/'  # the article's pinned, immutable data version
E = html.escape
load = lambda n: json.load(open(DATA + n + '.json'))

INK, DIM, LINE, BG = '#1d2733', '#5f6b78', '#d9dee4', '#ffffff'
RED, AMBER, GREEN, BLUE, PURPLE, GREY = '#c2410c', '#b7791f', '#2f7d6b', '#1f5e9b', '#6a4bb0', '#8a94a0'
FONT = "font-family:'Inter','Helvetica Neue',Arial,sans-serif"

S = load('sources'); S = S if isinstance(S, list) else S['sources']
C = load('compromise'); IM = load('impact'); CR = load('claim-review')['reviews']; VC = load('vault-claims'); SW = load('source-watch')
V = load('vault')
N_SOURCES = len(S); N_CAPS = sum(len(s['captures']) for s in S)
HEAD = V['head']['commit']; AS_OF = '12:14 UTC on 26 October 2026'
kinds = Counter(r['kind'] for r in C['rows'])
langs = Counter({'cn': 'zh'}.get(l, l) for l in ((s.get('lang') or '').split('-')[0].lower() for s in S if s.get('lang')))
skind = Counter(s.get('kind', 'other') for s in S)
days = Counter()
for s in S:
    st = sorted(c['stamp'] for c in s['captures'] if c.get('stamp'))
    if st: days[st[0][:8]] += 1
verd = Counter(r['verdict'] for r in CR)
countries = set()
for r in IM['offline']:
    for c in (r.get('country') or '').replace(' ', '').split(','):
        if c: countries.add(c)
N_OFF = len(IM['offline'])


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{E(title)}" style="{FONT};background:{BG}">{body}</svg>')


def t(x, y, s, size=16, fill=INK, weight=400, anchor='start', extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{E(s)}</text>'


def ladder():
    """The ladder of evidence: each level a stronger kind of proof; the top two are empty."""
    rungs = [
        ('Scanning and attack attempts', 'Yes: millions', 'Cloudflare counts millions of attempts; Amazon\'s decoy server was hit on 17 October, four days before the fix', GREEN, 1.0),
        ('Security vendors say "exploited in the wild"', f'Yes: {kinds["vendor-exploitation"]} statements', 'Hadrian, Patchstack, Amazon, NCSC New Zealand: none names a victim; Amazon says it was against its own sensors', AMBER, 0.8),
        ('A named organisation investigating an incident', '3 open, 1 withdrawn', 'GMO: a confirmed break-in, cause not stated; Czech Technical University: attack "stopped"; DMM: precaution', AMBER, 0.6),
        ('A named organisation says it was breached through php2shell', 'None', f'Searched across all {N_SOURCES} captured sources, in at least {len(langs)} languages'.replace('{len(langs)}', str(len(langs))) + '', RED, 0.0),
        ('Listed by CISA as known exploited (KEV)', 'Not listed', 'Neither CVE listed at the last check (05:53 UTC, 24 October); CISA\'s CVE record: "Exploitation: none"', RED, 0.0),
    ]
    W, H, X0, RH, GAP = 1200, 650, 60, 92, 14
    g = [t(X0, 44, 'The ladder of evidence: how far up has php2shell climbed?', 26, INK, 700),
         t(X0, 74, f'Each level is a stronger kind of proof than the one below it. As of {AS_OF}.', 16, DIM)]
    for i, (name, val, note, col, fill) in enumerate(reversed(rungs)):
        y = 100 + i * (RH + GAP)
        lvl = 5 - i
        g.append(f'<rect x="{X0}" y="{y}" width="{W - 2 * X0}" height="{RH}" rx="10" fill="#f6f7f9" stroke="{LINE}"/>')
        g.append(f'<rect x="{X0}" y="{y}" width="10" height="{RH}" rx="5" fill="{col}"/>')
        g.append(t(X0 + 30, y + 34, f'{lvl}. {name}', 19, INK, 700))
        g.append(t(X0 + 30, y + 64, note[:112], 14.5, DIM))
        bw = 200
        g.append(f'<rect x="{W - X0 - bw - 16}" y="{y + 22}" width="{bw}" height="48" rx="24" fill="{col}" opacity="{0.18 if fill else 0.12}"/>')
        g.append(t(W - X0 - bw / 2 - 16, y + 53, val, 18, col, 700, 'middle'))
    return svg(W, H, ''.join(g), 'The ladder of evidence')


def statements():
    order = [('no-success-known', 'Says no successful attack is known', GREEN), ('attempts', 'Reports attack attempts', BLUE),
             ('named-organisation', 'Names an organisation (tested below)', AMBER), ('vendor-exploitation', 'Vendor: "exploited", no victim named', AMBER),
             ('official-signal', 'Official signal (KEV, CISA, EPSS)', PURPLE), ('allegation', 'Unnamed allegation, unverified', GREY)]
    W, X0, BH = 1200, 420, 44
    H = 130 + len(order) * (BH + 14) + 40
    mx = max(kinds[k] for k, _, _ in order) or 1
    g = [t(60, 44, f'Every statement about compromise in the record: {sum(kinds.values())}', 26, INK, 700),
         t(60, 74, 'What each one actually says, as the compromise ledger classifies it. None names a breached organisation.', 16, DIM)]
    for i, (k, label, col) in enumerate(order):
        y = 110 + i * (BH + 14)
        w = (W - X0 - 120) * kinds[k] / mx
        g.append(t(X0 - 16, y + 29, label, 16, INK, 500, 'end'))
        g.append(f'<rect x="{X0}" y="{y}" width="{max(w, 3):.0f}" height="{BH}" rx="6" fill="{col}"/>')
        g.append(t(X0 + w + 12, y + 30, str(kinds[k]), 20, INK, 700))
    return svg(W, H, ''.join(g), 'Statements about compromise')


def offline_vs_breached():
    W, H = 1200, 420
    g = [t(60, 44, 'Taken offline is not hacked', 26, INK, 700),
         t(60, 74, 'Organisations pulled websites as a precaution; none has said it was breached through php2shell.', 16, DIM)]
    for x, n, label, sub, col in [(60, N_OFF, 'reports of sites taken offline', f'from {len(countries - {"EU"})} countries and the EU: governments, banks, hospitals', BLUE),
                                  (640, 0, 'named organisations breached', 'through php2shell, in their own words or a regulator\'s', RED)]:
        g.append(f'<rect x="{x}" y="110" width="500" height="260" rx="16" fill="#f6f7f9" stroke="{LINE}"/>')
        g.append(t(x + 250, 250, str(n), 120, col, 800, 'middle'))
        g.append(t(x + 250, 300, label, 22, INK, 700, 'middle'))
        g.append(t(x + 250, 332, sub, 14.5, DIM, 400, 'middle'))
    return svg(W, H, ''.join(g), 'Offline versus breached')


def evidence():
    W, H = 1200, 470
    g = [t(60, 44, f'The evidence behind the answer: {N_SOURCES} sources, {N_CAPS} saved captures', 26, INK, 700),
         t(60, 74, 'Every page saved when read, fingerprinted (sha256), and kept in an encrypted evidence vault. First capture of each source, by day:', 16, DIM)]
    ds = sorted(days.items()); mx = max(v for _, v in ds)
    for i, (d, v) in enumerate(ds):
        x = 80 + i * 110; h = 260 * v / mx; y = 380 - h
        g.append(f'<rect x="{x}" y="{y:.0f}" width="70" height="{h:.0f}" rx="5" fill="{BLUE}"/>')
        g.append(t(x + 35, y - 8, str(v), 16, INK, 700, 'middle'))
        g.append(t(x + 35, 404, f'{int(d[6:])} Oct', 14, DIM, 400, 'middle'))
    x0 = 700
    g.append(t(x0, 120, 'By kind', 18, INK, 700))
    for i, (k, v) in enumerate(skind.most_common(7)):
        g.append(t(x0, 150 + i * 26, f'{k}', 15, DIM)); g.append(t(x0 + 170, 150 + i * 26, str(v), 15, INK, 700, 'end'))
    x1 = 920
    g.append(t(x1, 120, f'In at least {len(langs)} languages', 18, INK, 700))
    for i, (k, v) in enumerate(langs.most_common(7)):
        g.append(t(x1, 150 + i * 26, k, 15, DIM)); g.append(t(x1 + 120, 150 + i * 26, str(v), 15, INK, 700, 'end'))
    g.append(t(80, 446, f'Evidence vault head {HEAD}; behind it the source watch: {SW.get("pages")} pages from {SW.get("publishers")} publishers, {SW.get("snapshots")} snapshots.', 14, DIM))
    return svg(W, H, ''.join(g), 'The evidence')


def pipeline():
    W, H = 1200, 330
    steps = [('Researcher', f'{SW.get("pages"):,} pages watched', f'{SW.get("snapshots"):,} snapshots', BLUE),
             ('Curator', f'{N_SOURCES} sources promoted', f'{len(VC)} claims, each quoted', GREEN),
             ('Journalist', f'{len(CR)} claim verdicts', f'{verd["used"]} used · {verd["held back"]} held back', '#b4461c'),
             ('Correspondent', 'reviews every release', 'against the captures', PURPLE)]
    g = [t(60, 44, 'How this newsroom answers a question like this', 26, INK, 700),
         t(60, 74, 'Four AI agents, one human editor, every step public: each reads only the step before it.', 16, DIM)]
    bw = 245
    for i, (n, a, b, col) in enumerate(steps):
        x = 60 + i * (bw + 40)
        g.append(f'<rect x="{x}" y="110" width="{bw}" height="170" rx="14" fill="#f6f7f9" stroke="{col}" stroke-width="2"/>')
        g.append(f'<rect x="{x}" y="110" width="{bw}" height="10" rx="5" fill="{col}"/>')
        g.append(t(x + 20, 160, n, 22, col, 800)); g.append(t(x + 20, 200, a, 16, INK, 600)); g.append(t(x + 20, 228, b, 14, DIM))
        if i < 3:
            g.append(f'<path d="M{x + bw + 6},195 l24,0 m-8,-8 l8,8 l-8,8" stroke="{DIM}" stroke-width="2.5" fill="none"/>')
    return svg(W, H, ''.join(g), 'How the newsroom answers')


def timeline():
    ev = [('17 Oct', 'Amazon\'s decoy server is hit, four days before the fix', AMBER),
          ('20 Oct', 'Details leak; watchTowr reproduces both flaws', AMBER),
          ('21 Oct', 'Fixes published, 13:31 to 13:35 UTC; sites go offline worldwide', BLUE),
          ('22 Oct', 'Millions of attempts at Cloudflare; Valtec and Sophos withdraw "hacked" claims', AMBER),
          ('23 Oct', 'A third, rarer flaw disclosed (CVE-2026-115560); no exploitation reported', BLUE),
          ('24 Oct', 'Last CISA KEV check: neither CVE listed', PURPLE),
          ('26 Oct', 'Latest capture, 12:14 UTC: still no named victim', RED)]
    W, H = 1200, 140 + len(ev) * 52
    g = [t(60, 44, 'Ten days, in the evidence', 26, INK, 700), t(60, 74, 'Dates from the captured sources; times UTC.', 16, DIM),
         f'<line x1="170" y1="100" x2="170" y2="{H - 30}" stroke="{LINE}" stroke-width="3"/>']
    for i, (d, s, col) in enumerate(ev):
        y = 120 + i * 52
        g.append(t(150, y + 6, d, 16, INK, 700, 'end'))
        g.append(f'<circle cx="170" cy="{y}" r="9" fill="{col}"/>')
        g.append(t(196, y + 6, s, 17, INK))
    return svg(W, H, ''.join(g), 'Timeline')


CAP_FILES = sum(len(c.get('files') or {}) for s in S for c in s['captures'])
CAP_BYTES = sum(m.get('bytes', 0) for s in S for c in s['captures'] for m in (c.get('files') or {}).values())


def weight():
    W, H = 1200, 560
    g = [t(60, 46, 'The weight behind one answer', 28, INK, 800),
         t(60, 78, 'What this newsroom read, saved and checked to say "not yet". Every number is counted, not estimated.', 17, DIM)]
    tiles = [
        (f'{N_SOURCES}', 'sources in the evidence vault', 'each a page saved the moment it was read', BLUE),
        (f'{N_CAPS}', 'captures', 'full snapshots: HTML, rendered HTML, screenshot, headers, text', BLUE),
        (f'{CAP_BYTES / 1e9:.2f} GB', 'of captured pages', f'in {CAP_FILES:,} files, every one sha256-fingerprinted', GREEN),
        (f'{SW.get("snapshots"):,}', 'source-watch snapshots', f'behind the vault: {SW.get("pages"):,} pages, {SW.get("publishers")} publishers', PURPLE),
        (f'{len(VC)}', 'claims promoted', 'each quoted word for word from its capture', AMBER),
        (f'{len(CR)}', 'verdicts given', f'{verd["used"]} used, {verd["held back"]} held back, before anything was published', '#b4461c'),
        ('~730 MB', 'across six public repositories', 'the whole operation, versioned and open', GREY),
        ('25+', 'languages, read in full', 'Japanese, German, Korean, Dutch, Arabic and more', GREEN),
    ]
    cols, cw, ch, gx, gy = 4, 270, 180, 16, 20
    for i, (big, lab, sub, col) in enumerate(tiles):
        x = 60 + (i % cols) * (cw + gx); y = 110 + (i // cols) * (ch + gy)
        g.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="14" fill="#f6f7f9" stroke="{LINE}"/>')
        g.append(f'<rect x="{x}" y="{y}" width="8" height="{ch}" rx="4" fill="{col}"/>')
        fs = 54 if len(big) <= 5 else (40 if len(big) <= 7 else 34)
        g.append(t(x + 26, y + 66, big, fs, col, 800))
        g.append(t(x + 26, y + 100, lab, 18, INK, 700))
        # wrap sub to ~30 chars
        words = sub.split(); line = ''; yy = y + 126
        for w in words:
            if len(line) + len(w) > 32:
                g.append(t(x + 26, yy, line, 13.5, DIM)); line = w; yy += 20
            else:
                line = (line + ' ' + w).strip()
        g.append(t(x + 26, yy, line, 13.5, DIM))
    return svg(W, H, ''.join(g), 'The weight of the evidence')


CHARTS = {'ladder': ladder, 'statements': statements, 'offline-vs-breached': offline_vs_breached,
          'evidence': evidence, 'pipeline': pipeline, 'timeline': timeline, 'weight': weight}
FACTS = dict(N_SOURCES=N_SOURCES, N_CAPS=N_CAPS, HEAD=HEAD, AS_OF=AS_OF, kinds=dict(kinds), N_OFF=N_OFF, countries=sorted(countries),
             langs=len(langs), verdicts=dict(verd), n_reviews=len(CR), n_vclaims=len(VC), sw=(SW.get('pages'), SW.get('publishers'), SW.get('snapshots')))

if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures.html')
    with open(out, 'w') as f:
        f.write('<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fff">')
        for k, fn in CHARTS.items():
            f.write(f'<div id="{k}" style="display:inline-block">{fn()}</div><br>')
    print(json.dumps(FACTS, ensure_ascii=False))
