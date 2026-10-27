const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1 });
  await p.goto('file://' + process.argv[2] + '/figures2.html');
  for (const id of ['three-things','chain','replicable','funnel']) {
    await p.locator('#' + id + ' svg').screenshot({ path: `${process.argv[2]}/png2/${id}.png` });
  }
  await b.close();
})();
