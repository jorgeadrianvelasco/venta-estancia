// Renderiza lamina-1..N.html (los que existan) a PNG 1080x1350 con Chromium.
// Uso: NODE_PATH=$(npm root -g) node render_lotes.js <dir_html> <dir_png>
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const [dirHtml, dirPng] = process.argv.slice(2);
  fs.mkdirSync(dirPng, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let n = 1; n <= 20; n++) {
    const file = path.resolve(dirHtml, `lamina-${n}.html`);
    if (!fs.existsSync(file)) break;
    await page.goto('file://' + file, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(dirPng, `lamina-${n}.png`) });
    console.log('ok', n);
  }
  await browser.close();
})();
