import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, '..');

const chromeBin = process.env.CHROME_BIN || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const port = process.env.SAMPLES_RENDER_PORT || '8080';
const base = `http://127.0.0.1:${port}`;

const targets = [
  { url: '/samples/public-preview.html', out: 'downloads/images/ikwe_public_preview.png' },
  { url: '/samples/board-brief.html', out: 'downloads/images/ikwe_board_brief.png' },
  { url: '/samples/audit-report.html', out: 'downloads/images/ikwe_audit_report.png' }
];

function run(cmd, args, opts = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(cmd, args, { stdio: 'inherit', ...opts });
    child.on('error', reject);
    child.on('exit', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`${cmd} exited with code ${code}`));
      }
    });
  });
}

const server = spawn('python3', ['-m', 'http.server', String(port)], {
  cwd: root,
  stdio: 'ignore'
});

const cleanup = () => {
  if (!server.killed) {
    server.kill('SIGTERM');
  }
};

process.on('exit', cleanup);
process.on('SIGINT', () => {
  cleanup();
  process.exit(1);
});
process.on('SIGTERM', () => {
  cleanup();
  process.exit(1);
});

// Give server time to start.
await new Promise((resolve) => setTimeout(resolve, 1000));

try {
  for (const target of targets) {
    const out = path.join(root, target.out);
    const src = `${base}${target.url}`;

    await run(chromeBin, [
      '--headless=new',
      '--disable-gpu',
      '--hide-scrollbars',
      '--window-size=1440,3200',
      `--screenshot=${out}`,
      src
    ]);

    console.log(`Rendered ${target.out} from ${src}`);
  }
} finally {
  cleanup();
}
