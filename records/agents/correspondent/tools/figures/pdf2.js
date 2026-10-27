const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2];
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('file://' + d + '/deck2.html', { waitUntil: 'networkidle' });
  await p.pdf({ path: d + '/deck2.pdf', width: '1280px', height: '720px', printBackground: true, preferCSSPageSize: true });
  await p.emulateMedia({ media: 'print' });
  const n = await p.locator('section.slide').count();
  for (let i=0;i<n;i++) await p.locator('section.slide').nth(i).screenshot({ path: `${d}/s2-${i+1}.png` });
  console.log('slides', n); await b.close();
})();
