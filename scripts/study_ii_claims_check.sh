#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

ERRORS=0

if command -v rg >/dev/null 2>&1; then
  SEARCH_TOOL="rg"
else
  SEARCH_TOOL="grep"
  echo "WARN: rg not found; falling back to grep -E"
fi

search_n() {
  local pattern="$1"
  shift
  if [[ "$SEARCH_TOOL" == "rg" ]]; then
    rg -n -- "$pattern" "$@"
  else
    grep -En -- "$pattern" "$@"
  fi
}

search_q() {
  local pattern="$1"
  shift
  if [[ "$SEARCH_TOOL" == "rg" ]]; then
    rg -q -- "$pattern" "$@"
  else
    grep -Eq -- "$pattern" "$@"
  fi
}

CLAIM_FILES=(
  "assets/ikwe-scorecard-visual.svg"
  "samples/public-preview.html"
  "samples/board-brief.html"
  "samples/audit-report.html"
  "print/public-preview-print.html"
  "print/board-brief-print.html"
  "print/audit-report-print.html"
  "proof.html"
  "audit.html"
  "research.html"
  "downloads.html"
  "downloads/index.html"
)

echo "== Study II claims integrity check =="
echo

echo "1) File presence"
echo "----------------"
for file in "${CLAIM_FILES[@]}"; do
  if [[ -f "$file" ]]; then
    echo "  OK  $file"
  else
    echo "  ERR missing file: $file"
    ERRORS=$((ERRORS + 1))
  fi
done
echo

echo "2) Deprecated wording blocklist"
echo "-------------------------------"
DEPRECATED_PATTERNS=(
  "projected reduction after controls"
  "Risk scores dropped 42[–-]67% after applying Ikwe"
  "benchmarked against frontier models"
)
for pattern in "${DEPRECATED_PATTERNS[@]}"; do
  if search_n "$pattern" "${CLAIM_FILES[@]}"; then
    echo "  ERR deprecated phrase found: $pattern"
    ERRORS=$((ERRORS + 1))
  else
    echo "  OK  not found: $pattern"
  fi
done
echo

echo "3) Canonical claim presence"
echo "---------------------------"
REQUIRED_PATTERNS=(
  "54\.7%"
  "43%"
  "42[–-]67%"
  "n=948 responses across 79 scenarios|948 responses, 79 scenarios"
)
for pattern in "${REQUIRED_PATTERNS[@]}"; do
  if search_q "$pattern" "${CLAIM_FILES[@]}"; then
    echo "  OK  present: $pattern"
  else
    echo "  ERR missing canonical pattern: $pattern"
    ERRORS=$((ERRORS + 1))
  fi
done
echo

echo "4) Method and citation anchors"
echo "------------------------------"
ANCHOR_FILES=(
  "samples/public-preview.html"
  "samples/board-brief.html"
  "samples/audit-report.html"
  "downloads.html"
  "downloads/index.html"
  "proof.html"
  "research.html"
)
for file in "${ANCHOR_FILES[@]}"; do
  if ! search_q "/research|Methodology" "$file"; then
    echo "  ERR $file missing methodology reference"
    ERRORS=$((ERRORS + 1))
  fi
  if ! search_q "Citation Guide|04_Ikwe_Citation_Guide\.pdf" "$file"; then
    echo "  ERR $file missing citation reference"
    ERRORS=$((ERRORS + 1))
  fi
  if search_q "/research|Methodology" "$file" && search_q "Citation Guide|04_Ikwe_Citation_Guide\.pdf" "$file"; then
    echo "  OK  $file"
  fi
done
echo

echo "5) PDF alias byte-identity"
echo "--------------------------"
ALIAS_PAIRS=(
  "downloads/ikwe_public_preview.pdf|downloads/ikwe_scorecard_sample.pdf"
  "downloads/ikwe_board_brief.pdf|downloads/ikwe_action_plan_sample.pdf"
  "downloads/ikwe_audit_report.pdf|downloads/ikwe_report_sample.pdf"
)
for pair in "${ALIAS_PAIRS[@]}"; do
  left="${pair%%|*}"
  right="${pair##*|}"

  if [[ ! -f "$left" || ! -f "$right" ]]; then
    echo "  ERR missing alias file(s): $left $right"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  left_sum="$(shasum -a 256 "$left" | awk '{print $1}')"
  right_sum="$(shasum -a 256 "$right" | awk '{print $1}')"

  if [[ "$left_sum" == "$right_sum" ]]; then
    echo "  OK  $left == $right"
  else
    echo "  ERR mismatch: $left != $right"
    ERRORS=$((ERRORS + 1))
  fi
done
echo

echo "== Summary =="
if [[ "$ERRORS" -eq 0 ]]; then
  echo "PASS: Study II claims integrity checks passed"
else
  echo "FAIL: $ERRORS issue(s)"
fi

exit "$ERRORS"
