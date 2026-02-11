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

