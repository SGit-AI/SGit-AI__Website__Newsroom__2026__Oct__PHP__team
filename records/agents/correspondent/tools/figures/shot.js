const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1 });
  await p.goto('file://' + process.argv[2] + '/figures.html');
  for (const id of ['ladder','statements','offline-vs-breached','evidence','pipeline','timeline','weight']) {
    await p.locator('#' + id + ' svg').screenshot({ path: `${process.argv[2]}/png/${id}.png` });
  }
  await b.close();
})();
