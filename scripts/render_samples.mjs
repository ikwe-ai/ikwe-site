import { chromium } from 'playwright';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, '..');

const base = process.env.SAMPLES_BASE_URL || 'http://127.0.0.1:8080';
const targets = [
  { url: '/samples/public-preview.html', out: 'downloads/images/ikwe_public_preview.png' },
  { url: '/samples/board-brief.html', out: 'downloads/images/ikwe_board_brief.png' },
  { url: '/samples/audit-report.html', out: 'downloads/images/ikwe_audit_report.png' }
];

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 1800 }, deviceScaleFactor: 2 });

try {
  for (const target of targets) {
    const page = await context.newPage();
    const src = new URL(target.url, base).toString();
    await page.goto(src, { waitUntil: 'networkidle' });
    await page.screenshot({ path: path.join(root, target.out), fullPage: true });
    await page.close();
    console.log(`Rendered ${target.out} from ${src}`);
  }
} finally {
  await context.close();
  await browser.close();
}
