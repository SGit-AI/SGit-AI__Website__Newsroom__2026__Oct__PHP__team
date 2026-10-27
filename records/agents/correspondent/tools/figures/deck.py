"""The slide deck for 'Has anyone actually been hacked through php2shell?': one self-contained HTML file, 16:9, one slide a
page when printed (Save as PDF). Charts are the article's, inline. Written by correspondent@php.newsroom, 26 October 2026."""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import charts as C

E = html.escape
URL = 'https://php.oct.2026.newsroom.sgit.ai/articles/has-anyone-been-hacked/'
F = C.FACTS


def slide(inner, cls=''):
    return f'<section class="slide {cls}">{inner}<footer><span>php2shell, the evidence · php.oct.2026.newsroom.sgit.ai</span><span>As of 12:14 UTC, 26 October 2026 · evidence vault {E(F["HEAD"])}</span></footer></section>'


def chart(name):
    return f'<div class="chart">{C.CHARTS[name]()}</div>'


slides = [
    slide(f'''<p class="kicker">A reader's question, answered from the evidence</p>
<h1>Has anyone actually been hacked through php2shell?</h1>
<div class="answer"><div><b>Attack attempts</b><span class="big green">Millions</span></div><div><b>Confirmed, named victims</b><span class="big red">Not yet</span></div></div>
<p class="sub">CVE-2026-109618 and CVE-2026-109619, the two critical PHP flaws fixed on 21 October 2026. What {F["N_SOURCES"]} captured sources in at least {F["langs"]} languages say, five days on.</p>
<p class="cta">The full analysis, every source linked and fingerprinted:<br><b>{E(URL)}</b></p>''', 'title'),
    slide('''<h2>The short answer</h2>
<ul class="points">
<li><b>No organisation has said it was breached through php2shell</b>, in its own words or a regulator's, as of 12:14 UTC on 26 October.</li>
<li><b>Attempts are certain and massive:</b> millions at Cloudflare; Amazon's decoy server hit on 17 October, four days before the fix.</li>
<li><b>Vendors say "exploited in the wild", but name no victim:</b> Hadrian, Patchstack, Amazon (against its own sensors), NCSC New Zealand.</li>
<li><b>Not on CISA's Known Exploited list</b> at the last check (24 October); CISA's own CVE record says "Exploitation: none".</li>
<li><b>Hundreds of sites went offline as a precaution.</b> Offline is a decision, not a breach.</li>
</ul>'''),
    slide(chart('ladder'), 'full'),
    slide('''<h2>The named cases, tested against their own words</h2>
<table><thead><tr><th>Organisation</th><th>What it said</th><th>What that proves</th></tr></thead><tbody>
<tr><td>GMO Internet Group (Japan)</td><td>Malicious programs on its FX VPS servers on 20 October; logins may have been taken</td><td>A real break-in; <b>cause not stated</b></td></tr>
<tr><td>Czech Technical University</td><td>An attack "part of worldwide attempts to hit PHP sites"; "the active attack was stopped"</td><td>An attack; <b>success not stated</b></td></tr>
<tr><td>DMM (Japan)</td><td>Services halted over "a vulnerability in external software"; no data leaked</td><td>A precaution; <b>PHP not confirmed</b></td></tr>
<tr><td>Valtec (Japan)</td><td>Blamed the PHP flaw, then corrected the same day: its own service's flaw</td><td><b>Withdrawn</b></td></tr>
</tbody></table>
<p class="note">One blog says "Palo Alto Networks and Trail of Bits later reported confirmed compromises". It names no victim; Palo Alto's own advisory says it is "not aware of any malicious exploitation". Held back.</p>'''),
    slide(chart('statements'), 'full'),
    slide(chart('offline-vs-breached'), 'full'),
    slide('''<h2>And the bitcoin site?</h2>
<ul class="points">
<li>The site named in the question <b>does not appear in any of the 525 captured sources</b>, and no page ties a cryptocurrency platform's loss to these flaws.</li>
<li>What the record holds points the other way: <b>Coinbase, BitGo, Bitget Wallet and PancakeSwap</b> said they were not affected; Binance took precautions.</li>
<li>BTC-ECHO found <b>no evidence of compromise</b> at the large exchanges and payment providers.</li>
<li>"Not in the evidence" is not "did not happen": <b>send the link</b>, and it is captured, read and checked like everything else.</li>
</ul>'''),
    slide(chart('timeline'), 'full'),
    slide(chart('pipeline') + chart('evidence').replace('<div class="chart">', '<div class="chart half">'), 'full stack'),
    slide(chart('weight'), 'full'),
    slide(f'''<h2>What would change the answer</h2>
<ol class="points">
<li>A named organisation saying it was compromised through php2shell, in its own notice, filing or statement.</li>
<li>GMO, Czech Technical University or DMM stating that php2shell was the cause.</li>
<li>A CISA KEV listing for either CVE, with CISA's evidence.</li>
<li>A regulator's breach notice naming the flaw.</li>
<li>A security vendor naming a victim, with the victim's consent.</li>
</ol>
<p class="cta">The full analysis, every source linked and fingerprinted:<br><b>{E(URL)}</b></p>'''),
]

CSS = '''
@page { size: 1280px 720px; margin: 0 }
* { box-sizing: border-box }
html, body { margin: 0; background: #e9ecef; font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif; color: #1d2733 }
.slide { width: 1280px; height: 720px; margin: 24px auto; background: #fff; position: relative; padding: 56px 72px 70px; overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,.12); page-break-after: always; break-after: page }
@media print { html, body { background: #fff } .slide { margin: 0; box-shadow: none } }
footer { position: absolute; left: 72px; right: 72px; bottom: 22px; display: flex; justify-content: space-between; font-size: 13px; color: #5f6b78;
  border-top: 1px solid #d9dee4; padding-top: 10px }
h1 { font-size: 54px; line-height: 1.08; margin: 10px 0 30px; letter-spacing: -0.5px }
h2 { font-size: 36px; margin: 0 0 26px }
.kicker { text-transform: uppercase; letter-spacing: 2px; font-size: 15px; color: #6a4bb0; font-weight: 700; margin: 0 }
.title { background: linear-gradient(180deg, #f7f5fd 0, #fff 60%) }
.answer { display: flex; gap: 28px; margin: 6px 0 26px }
.answer div { flex: 1; border: 1px solid #d9dee4; border-radius: 16px; padding: 20px 26px; background: #fff }
.answer b { display: block; font-size: 18px; color: #5f6b78; font-weight: 600 }
.big { display: block; font-size: 64px; font-weight: 800; line-height: 1.1 }
.green { color: #2f7d6b } .red { color: #c2410c }
.sub { font-size: 19px; color: #5f6b78; max-width: 1050px; line-height: 1.45 }
.points { font-size: 24px; line-height: 1.45; padding-left: 28px; margin: 0 }
.points li { margin: 0 0 14px }
table { width: 100%; border-collapse: collapse; font-size: 19px }
th { text-align: left; color: #5f6b78; font-size: 15px; text-transform: uppercase; letter-spacing: 1px; border-bottom: 2px solid #d9dee4; padding: 8px 10px }
td { padding: 12px 10px; border-bottom: 1px solid #e6e9ed; vertical-align: top }
td:first-child { font-weight: 700; width: 24% }
.note { font-size: 16px; color: #5f6b78; margin-top: 20px; line-height: 1.4 }
.cta { margin-top: 28px; font-size: 20px; line-height: 1.5; background: #f6f7f9; border-left: 6px solid #6a4bb0; padding: 14px 20px; border-radius: 6px }
.full { padding: 30px 40px 60px; display: flex; align-items: center; justify-content: center }
.chart { width: 100% } .chart svg { width: 100%; height: auto; max-height: 610px; display: block; margin: 0 auto }
.stack { flex-direction: column; gap: 4px } .stack .chart svg { max-height: 300px } .half svg { max-height: 330px }
'''

doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Has anyone been hacked through php2shell? The evidence, 26 October 2026</title><style>{CSS}</style></head>
<body>{"".join(slides)}</body></html>'''

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deck.html')
open(out, 'w', encoding='utf-8').write(doc)
print(out, len(slides), 'slides')
