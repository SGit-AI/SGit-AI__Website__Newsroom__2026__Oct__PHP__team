"""Slide deck for 'Someone stole the bitcoin: what it tells us about php2shell'. Self-contained HTML, 16:9, prints to PDF.
Defensive and conceptual; no exploit recipe. correspondent@php.newsroom, 26 October 2026."""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import charts2 as C2

E = html.escape
URL = 'https://php.oct.2026.newsroom.sgit.ai/articles/steal-my-bitcoin/'


def slide(inner, cls=''):
    return (f'<section class="slide {cls}">{inner}'
            f'<footer><span>php2shell, the evidence · php.oct.2026.newsroom.sgit.ai</span>'
            f'<span>As of 12:14 UTC, 26 October 2026</span></footer></section>')


def chart(n):
    return f'<div class="chart">{C2.CHARTS[n]()}</div>'


slides = [
    slide('''<p class="kicker">A reader's question, answered from the evidence</p>
<h1>Someone stole the bitcoin.<br>Was php2shell finally used for real?</h1>
<div class="answer"><div><b>A working exploit</b><span class="big green">Proven</span></div>
<div><b>A real-world victim</b><span class="big red">Still none</span></div></div>
<p class="sub">A researcher won a public "steal my bitcoin" bounty by breaking into a <b>deliberately vulnerable</b> server with php2shell, and published how. Here is what that does, and does not, mean.</p>''', 'title'),
    slide('''<h2>One minute</h2>
<ul class="points">
<li>Someone built a server <b>on purpose</b> to be vulnerable to php2shell, put ~$2,000 of bitcoin on it, and invited the internet to steal it.</li>
<li>On 25 October a skilled researcher did, in ~19 hours, and wrote it up.</li>
<li>That is <b>real proof the flaw gives full control of a machine</b> — the strongest public demonstration so far.</li>
<li>But it is <b>a game with a consenting target, not a victim.</b> Nobody was harmed.</li>
<li>So it does <b>not</b> change the standing answer: <b>no named organisation breached</b> through php2shell in the real world.</li>
</ul>'''),
    slide(chart('three-things'), 'full'),
    slide('''<h2>Was it the same bug?</h2>
<ul class="points">
<li><b>Yes.</b> It targeted <b>PHP 8.4.26</b> — one version below the 8.4.27 that carries the fix.</li>
<li>It abused the same mechanism the PHP advisory names: the <b>session upload-progress</b> feature, the memory disclosure, and the memory-corruption flaws behind CVE-2026-109618 and CVE-2026-109619.</li>
<li><b>Not a new vulnerability.</b> It is the known php2shell family, demonstrated end to end on an unpatched build.</li>
</ul>'''),
    slide(chart('chain'), 'full'),
    slide('''<h2>A new attack vector? One wrinkle worth noting</h2>
<ul class="points">
<li>Not a new vulnerability — but a new <b>data point</b>.</li>
<li>The usual advisories studied Apache <b>mod_php</b> and <b>PHP-FPM</b>. This challenge ran neither.</li>
<li>It ran PHP's <b>built-in web server</b> (<code>php -S</code>) with worker processes — a mode the project says is <b>not for production</b>.</li>
<li>The win shows that this built-in server, too, can be driven to full code execution. We have flagged it to add to the affected-systems table.</li>
</ul>'''),
    slide(chart('replicable'), 'full'),
    slide(chart('funnel'), 'full'),
    slide(f'''<h2>What a defender should take from it</h2>
<ol class="points">
<li><b>Patch</b> to 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35, or your distribution's backport. 8.4.26 is vulnerable.</li>
<li>As a stopgap, <b>turn off upload-progress</b> (<code>session.upload_progress.enabled=0</code>) — not a substitute for the update.</li>
<li><b>Never run the built-in <code>php -S</code> server in production.</b></li>
<li><b>Assume memory disclosure beats ASLR</b>: a randomised layout is not a backstop here.</li>
<li><b>Keep the proportion.</b> One consenting honeypot fell to a specialist in 19 hours. Real-world named victims: still zero.</li>
</ol>
<p class="cta">The full analysis, every claim sourced and fingerprinted:<br><b>{E(URL)}</b></p>''', ),
]

CSS = '''
@page { size: 1280px 720px; margin: 0 }
* { box-sizing: border-box }
html, body { margin: 0; background: #e9ecef; font-family: 'Inter','Helvetica Neue',Arial,sans-serif; color: #1d2733 }
.slide { width: 1280px; height: 720px; margin: 24px auto; background: #fff; position: relative; padding: 54px 72px 70px; overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,.12); page-break-after: always; break-after: page }
@media print { html, body { background: #fff } .slide { margin: 0; box-shadow: none } }
footer { position: absolute; left: 72px; right: 72px; bottom: 22px; display: flex; justify-content: space-between; font-size: 13px; color: #5f6b78;
  border-top: 1px solid #d9dee4; padding-top: 10px }
h1 { font-size: 48px; line-height: 1.1; margin: 10px 0 26px; letter-spacing: -0.5px }
h2 { font-size: 36px; margin: 0 0 24px }
.kicker { text-transform: uppercase; letter-spacing: 2px; font-size: 15px; color: #6a4bb0; font-weight: 700; margin: 0 }
.title { background: linear-gradient(180deg,#f7f5fd 0,#fff 60%) }
.answer { display: flex; gap: 28px; margin: 6px 0 24px }
.answer div { flex: 1; border: 1px solid #d9dee4; border-radius: 16px; padding: 18px 26px }
.answer b { display: block; font-size: 18px; color: #5f6b78; font-weight: 600 }
.big { display: block; font-size: 60px; font-weight: 800; line-height: 1.1 }
.green { color: #2f7d6b } .red { color: #c2410c }
.sub { font-size: 20px; color: #5f6b78; max-width: 1060px; line-height: 1.5 }
.points { font-size: 24px; line-height: 1.5; padding-left: 28px; margin: 0 }
.points li { margin: 0 0 15px }
code { background: #f1ede8; padding: 1px 7px; border-radius: 5px; font-size: 0.9em }
.cta { margin-top: 26px; font-size: 20px; line-height: 1.5; background: #f6f7f9; border-left: 6px solid #6a4bb0; padding: 14px 20px; border-radius: 6px }
.full { padding: 32px 44px 60px; display: flex; align-items: center; justify-content: center }
.chart { width: 100% } .chart svg { width: 100%; height: auto; max-height: 600px; display: block; margin: 0 auto }
'''

doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
       f'<title>Steal My Bitcoin and php2shell: the evidence, 26 October 2026</title><style>{CSS}</style></head>'
       f'<body>{"".join(slides)}</body></html>')
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deck2.html')
open(out, 'w', encoding='utf-8').write(doc)
print(out, len(slides), 'slides')
