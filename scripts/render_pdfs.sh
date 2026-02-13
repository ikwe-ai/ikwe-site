#!/usr/bin/env bash
set -euo pipefail

CHROME_BIN=${CHROME_BIN:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
PORT=${PDF_RENDER_PORT:-8080}
BASE_URL="http://127.0.0.1:${PORT}"

if [[ ! -x "$CHROME_BIN" ]]; then
  echo "Chrome binary not found or not executable: $CHROME_BIN" >&2
  exit 1
fi

python3 -m http.server "$PORT" >/tmp/ikwe-pdf-http.log 2>&1 &
SERVER_PID=$!
cleanup() {
  kill "$SERVER_PID" >/dev/null 2>&1 || true
}
trap cleanup EXIT

sleep 1

"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_public_preview.pdf" "${BASE_URL}/print/public-preview-print.html"
"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_board_brief.pdf" "${BASE_URL}/print/board-brief-print.html"
"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_audit_report.pdf" "${BASE_URL}/print/audit-report-print.html"

# Keep alias sample PDFs byte-identical with their canonical sources.
cp -f downloads/ikwe_public_preview.pdf downloads/ikwe_scorecard_sample.pdf
cp -f downloads/ikwe_board_brief.pdf downloads/ikwe_action_plan_sample.pdf
cp -f downloads/ikwe_audit_report.pdf downloads/ikwe_report_sample.pdf

echo "PDFs regenerated in downloads/."
