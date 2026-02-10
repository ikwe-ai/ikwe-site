#!/usr/bin/env bash
set -euo pipefail

CHROME_BIN=${CHROME_BIN:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}

python3 scripts/prepare_pdf_html.py

"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_public_preview.pdf" "file:///tmp/ikwe-pdf/preview.html"
"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_board_brief.pdf" "file:///tmp/ikwe-pdf/proof.html"
"$CHROME_BIN" --headless=new --disable-gpu --print-to-pdf="downloads/ikwe_audit_report.pdf" "file:///tmp/ikwe-pdf/audit.html"

echo "PDFs regenerated in downloads/."
