#!/usr/bin/env bash
set -euo pipefail

echo "== Live pages old-pricing drift scan =="
rg -n "\$250|Preview Pack|Public Preview Pack|250,000" \
  index.html audit.html proof.html research.html inquiry.html about.html enterprise.html downloads.html \
  || echo "OK: no old-pricing drift in live HTML pages"

echo
echo "== Live pricing presence scan =="
rg -n "2,500|5,000|25,000|25,000\+" \
  index.html audit.html proof.html inquiry.html terms.html \
  || echo "WARN: expected canonical pricing strings not found in one or more scanned pages"

echo
echo "== Core download links scan =="
rg -n "ikwe_public_preview\.pdf|ikwe_board_brief\.pdf|ikwe_audit_report\.pdf|ikwe_research_summary\.pdf|ikwe_full_research_report\.pdf" \
  downloads.html research.html audit.html proof.html index.html \
  || echo "WARN: some canonical download links may be missing in scanned pages"

echo
echo "== Claims consistency scan =="
CLAIMS_FILES=(
  assets/ikwe-scorecard-visual.svg
  samples/public-preview.html
  samples/board-brief.html
  samples/audit-report.html
  print/public-preview-print.html
  print/board-brief-print.html
  print/audit-report-print.html
  proof.html
  audit.html
  downloads.html
)

if rg -n "projected reduction after controls|Risk scores dropped 42–67% after applying Ikwe|benchmarked against frontier models" "${CLAIMS_FILES[@]}"; then
  echo "ERR: found deprecated or non-verifiable claim phrasing"
  exit 1
else
  echo "OK: no deprecated claim phrasing found"
fi

if rg -n "n=948 responses across 79 scenarios|n=948 responses, 79 scenarios" "${CLAIMS_FILES[@]}" >/dev/null; then
  echo "OK: canonical benchmark basis present"
else
  echo "WARN: benchmark basis phrase missing from scanned claim files"
fi
