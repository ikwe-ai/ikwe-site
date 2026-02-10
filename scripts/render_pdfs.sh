#!/usr/bin/env bash
set -euo pipefail

CHROME_BIN=${CHROME_BIN:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}

"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_public_preview.pdf" "file://$(pwd)/print/public-preview-print.html"
"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_board_brief.pdf" "file://$(pwd)/print/board-brief-print.html"
"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_audit_report.pdf" "file://$(pwd)/print/audit-report-print.html"

echo "PDFs regenerated in downloads/."
