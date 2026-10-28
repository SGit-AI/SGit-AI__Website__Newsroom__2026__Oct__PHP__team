"""Screenshot a page as a reader sees it (scripts run, data filled live): python3 shot.py URL OUT.png [CSS selector to scroll to]
Needs playwright and a Chromium (the sessions have one under /opt/pw-browsers). Written by desk@php.newsroom."""
import glob, sys
from playwright.sync_api import sync_playwright
url, out = sys.argv[1], sys.argv[2]; sel = sys.argv[3] if len(sys.argv) > 3 else ''
exe = (glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome') or [None])[0]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
    pg = b.new_page(viewport={'width': 1200, 'height': 900}); pg.goto(url, wait_until='networkidle'); pg.wait_for_timeout(3000)
    if sel: pg.evaluate("s => document.querySelector(s) && document.querySelector(s).scrollIntoView()", sel)
    pg.screenshot(path=out); b.close()
