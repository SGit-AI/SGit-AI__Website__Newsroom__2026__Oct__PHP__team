// Two tabs of one site in one browser must settle: no endless redraws, no page errors.
// Why: on 28 October 2026 the front page's line answered every other tab's storage write with a redraw, so two open tabs
// called document.startViewTransition about 250 times a second each (hundreds of "Transition was skipped" errors), and
// no test opened a second tab. Usage: NODE_PATH=$(npm root -g) node two-tabs.cjs [site url]   exits 1 on a failure.
// Answers every POST locally (the telemetry lane is never sent a test event); reads only.
const { chromium } = require('playwright');
const URL = process.argv[2] || 'https://php.oct.2026.newsroom.sgit.ai/';
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1400, height: 800 } });
  await ctx.addInitScript(() => {
    window.__vt = 0; window.__wr = 0; const o = Storage.prototype.setItem;
    Storage.prototype.setItem = function (k, v) { if (k === 'p2s.lens') window.__wr++; return o.call(this, k, v); };
    if (document.startViewTransition) { const s = document.startViewTransition.bind(document); document.startViewTransition = function (f) { window.__vt++; return s(f); }; }
  });
  const open = async () => { const p = await ctx.newPage(); p.errs = 0; p.on('pageerror', () => p.errs++);
    await p.route('**/*', r => r.request().method() === 'POST' ? r.fulfill({ status: 200, body: '{}' }) : r.continue());
    await p.goto(URL, { waitUntil: 'networkidle', timeout: 60000 }); return p; };
  const A = await open(); await A.waitForTimeout(1500); const B = await open(); await B.waitForTimeout(5000);
  const g = p => p.evaluate(() => [window.__vt, window.__wr]);
  const [va, wa] = await g(A), [vb, wb] = await g(B);
  console.log(URL, 'transitions A/B', va, vb, '| p2s.lens writes A/B', wa, wb, '| page errors A/B', A.errs, B.errs);
  await b.close();
  const bad = va > 20 || vb > 20 || wa > 40 || wb > 40 || A.errs || B.errs;
  console.log(bad ? 'FAIL: the tabs do not settle' : 'ok: two tabs settle'); process.exit(bad ? 1 : 0);
})();
