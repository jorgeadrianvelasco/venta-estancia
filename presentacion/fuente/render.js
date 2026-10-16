// Vista previa local: renderiza lamina-N.html a PNG 1080x1350 con Chromium.
// Uso: node render.js <dir_html> <dir_png> [alto=1350]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const [dirHtml, dirPng, alto] = process.argv.slice(2); const H = parseInt(alto || '1350', 10);
  fs.mkdirSync(dirPng, { recursive: true });
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
  const page = await browser.newPage({ viewport: { width: 1080, height: H } });
  for (let n = 1; n <= 8; n++) {
    const file = path.resolve(dirHtml, `lamina-${n}.html`);
    await page.goto('file://' + file, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(dirPng, `lamina-${n}.png`) });
    console.log('ok', n);
  }
  await browser.close();
})();
