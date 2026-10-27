"""Figures for 'Steal My Bitcoin: what a won bounty does and does not tell us about php2shell'.
Defensive, conceptual: no offsets, no payload, no recipe. Correspondent@php.newsroom, 26 October 2026."""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from charts import svg, t, INK, DIM, LINE, BG, RED, AMBER, GREEN, BLUE, PURPLE, GREY, E


def tl_wrap(x, y, s, size, fill, width=34, lh=19, weight=400):
    words, line, out, yy = s.split(), '', [], y
    for w in words:
        if len(line) + len(w) + 1 > width:
            out.append(t(x, yy, line, size, fill, weight)); line = w; yy += lh
        else:
            line = (line + ' ' + w).strip()
    out.append(t(x, yy, line, size, fill, weight))
    return ''.join(out), yy


def three_things():
    """Separate what people conflate: the bug class, a consenting honeypot, a real victim."""
    W, H = 1200, 470
    cols = [
        ('The flaw itself', 'REAL AND CONFIRMED', GREEN,
         ['php2shell (CVE-2026-109618 / -109619) is a genuine, critical remote-code-execution flaw in PHP, fixed on 21 October.',
          'Given an unpatched server, it can hand an attacker full control. That has never been in doubt.']),
        ('The "Steal My Bitcoin" challenge', 'A GAME, WON', AMBER,
         ['A server its owner built to be hacked, with bitcoin as bait and a public invitation to try.',
          'A researcher won the ~$2,000 bounty on 25 October after ~19 hours. Consenting target, no victim.']),
        ('A real-world breach', 'STILL NONE NAMED', RED,
         ['No organisation has said it was broken into through php2shell, in its own words or a regulator’s.',
          'As of 12:14 UTC on 26 October, across 525 captured sources. This challenge does not change that.']),
    ]
    g = [t(60, 44, 'Three different things people are mixing up', 27, INK, 800),
         t(60, 74, 'A won bounty is proof the bug works — not proof a real organisation was a victim.', 17, DIM)]
    cw = 360
    for i, (title, tag, col, lines) in enumerate(cols):
        x = 60 + i * (cw + 20)
        g.append(f'<rect x="{x}" y="100" width="{cw}" height="330" rx="16" fill="#f6f7f9" stroke="{LINE}"/>')
        g.append(f'<rect x="{x}" y="100" width="{cw}" height="10" rx="5" fill="{col}"/>')
        g.append(t(x + 24, 148, title, 20, INK, 800))
        g.append(f'<rect x="{x + 24}" y="162" width="{min(len(tag)*10.5+24, cw-48):.0f}" height="30" rx="15" fill="{col}" opacity="0.16"/>')
        g.append(t(x + 36, 183, tag, 14, col, 800))
        yy = 226
        for ln in lines:
            body, yy = tl_wrap(x + 24, yy, ln, 15, INK if col != RED else INK, 36, 21)
            g.append(body); yy += 28
    return svg(W, H, ''.join(g), 'Three different things')


def chain():
    """The exploitation chain at the level our own advisory already describes. No offsets, no payload."""
    W, H = 1200, 430
    stages = [
        ('1', 'A crafted upload', 'A specially shaped file upload makes PHP’s upload-progress feature keep tracking data it should have let go.', BLUE),
        ('2', 'Memory is leaked', 'The flaw hands back scraps of the server’s own memory (Heartbleed-style), revealing where things sit — defeating the usual randomised-layout defence.', PURPLE),
        ('3', 'Memory is corrupted', 'A use-after-free and a type confusion let the attacker overwrite the right bytes, turning the leak into control of the program.', AMBER),
        ('4', 'A command runs', 'Control of execution becomes a shell command, running as the web server — before any of the site’s own code is reached.', RED),
    ]
    g = [t(60, 44, 'How the php2shell chain works, in four moves', 27, INK, 800),
         t(60, 74, 'The same mechanism the PHP advisory describes. Shown to explain, not to reproduce: no addresses, no payload.', 16, DIM)]
    bw, bh, gap = 265, 230, 18
    for i, (n, title, body, col) in enumerate(stages):
        x = 60 + i * (bw + gap)
        g.append(f'<rect x="{x}" y="110" width="{bw}" height="{bh}" rx="14" fill="#fff" stroke="{col}" stroke-width="2"/>')
        g.append(f'<circle cx="{x+34}" cy="148" r="20" fill="{col}"/>')
        g.append(t(x + 34, 155, n, 22, '#fff', 800, 'middle'))
        g.append(t(x + 66, 155, title, 18, INK, 800))
        wr, _ = tl_wrap(x + 22, 198, body, 14.5, DIM, 30, 21)
        g.append(wr)
        if i < 3:
            g.append(f'<path d="M{x+bw+2},225 l14,0 m-7,-7 l7,7 l-7,7" stroke="{DIM}" stroke-width="2.5" fill="none"/>')
    g.append(t(60, 408, 'Stopgap: turning the upload-progress feature off (session.upload_progress.enabled=0) blocks this path. Only updating to PHP 8.4.27 / 8.3.36 / 8.2.35 / 8.5.12 fixes the flaw.', 14, INK, 600))
    return svg(W, H, ''.join(g), 'The chain in four moves')


def replicable():
    """Why a working lab exploit is not a drop-in weapon against arbitrary sites."""
    W, H = 1200, 470
    rows = [
        ('Pinned to one PHP build', 'PHP 8.4.26 on Alpine, exact binary', 'Memory-corruption offsets are specific to the compiled build; the write-up says a Debian stack would not match', RED),
        ('An unusual server mode', 'PHP’s built-in dev server (php -S) with multiple workers', 'Not Apache mod_php or PHP-FPM — the modes the primary advisories studied; the built-in server is explicitly “not for production”', AMBER),
        ('A race, not a certainty', '~7 wins in 10 tries, in the author’s own lab', 'Timing-dependent; it fails much of the time even against the target it was tuned for', AMBER),
        ('Re-tuned per target', 'offsets, layout and timing redone for each build', 'Against a different production stack an attacker must redevelop the exploit, not re-run this one', PURPLE),
    ]
    g = [t(60, 44, 'Why the class travels but this exploit does not', 27, INK, 800),
         t(60, 74, 'The vulnerability is general. This particular working exploit is bespoke to the challenge server.', 17, DIM)]
    y0 = 108
    for i, (h, v, note, col) in enumerate(rows):
        y = y0 + i * 86
        g.append(f'<rect x="60" y="{y}" width="1080" height="74" rx="12" fill="#f6f7f9" stroke="{LINE}"/>')
        g.append(f'<rect x="60" y="{y}" width="8" height="74" rx="4" fill="{col}"/>')
        g.append(t(84, y + 30, h, 18, INK, 800))
        g.append(t(84, y + 56, v, 15, col, 700))
        wr, _ = tl_wrap(560, y + 30, note, 15, DIM, 60, 22)
        g.append(wr)
    return svg(W, H, ''.join(g), 'Why this exploit is bespoke')


def funnel():
    """Exposed -> reachable -> working exploit exists -> weaponised at scale -> a named victim."""
    W, H = 1200, 460
    steps = [
        ('Runs PHP', '~70% of the web (survey share)', BLUE, 1.0),
        ('Exposed and unpatched', '1.57 million hosts on release day (Censys)', BLUE, 0.78),
        ('A working exploit exists', 'Yes — demonstrated: the challenge, watchTowr, PoCs', AMBER, 0.5),
        ('Weaponised reliably at scale', 'Not shown: attempts in millions, success rare / difficult', AMBER, 0.3),
        ('A named organisation breached', 'None, as of 12:14 UTC 26 October', RED, 0.08),
    ]
    g = [t(60, 44, 'From "runs PHP" to "was hacked": where php2shell actually sits', 25, INK, 800),
         t(60, 74, 'Each step is a smaller set than the one above. The challenge proved step 3; steps 4 and 5 are still not met.', 16, DIM)]
    cx = 600; top = 110; bh = 60; gap = 12; maxw = 980
    for i, (name, note, col, frac) in enumerate(steps):
        y = top + i * (bh + gap); w = maxw * frac
        g.append(f'<rect x="{cx - w/2:.0f}" y="{y}" width="{w:.0f}" height="{bh}" rx="8" fill="{col}" opacity="{0.25 + 0.12*(1-frac):.2f}"/>')
        g.append(t(cx, y + 26, name, 18, INK, 800, 'middle'))
        g.append(t(cx, y + 48, note, 14, INK, 400, 'middle'))
        if i == 2:
            g.append(t(cx + w/2 + 16, y + 38, '← the "Steal My Bitcoin" win is here', 15, AMBER, 700))
    return svg(W, H, ''.join(g), 'The funnel')


CHARTS = {'three-things': three_things, 'chain': chain, 'replicable': replicable, 'funnel': funnel}

if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures2.html')
    with open(out, 'w') as f:
        f.write('<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fff">')
        for k, fn in CHARTS.items():
            f.write(f'<div id="{k}" style="display:inline-block">{fn()}</div><br>')
    print('ok', list(CHARTS))
