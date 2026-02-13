#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

OUT_FILE="research/study-ii/ARTIFACT_MANIFEST.sha256"

FILES=(
  "assets/ikwe-scorecard-visual.svg"
  "samples/public-preview.html"
  "samples/board-brief.html"
  "samples/audit-report.html"
  "print/public-preview-print.html"
  "print/board-brief-print.html"
  "print/audit-report-print.html"
  "downloads/ikwe_public_preview.pdf"
  "downloads/ikwe_board_brief.pdf"
  "downloads/ikwe_audit_report.pdf"
  "downloads/ikwe_scorecard_sample.pdf"
  "downloads/ikwe_report_sample.pdf"
  "downloads/ikwe_action_plan_sample.pdf"
  "downloads/images/ikwe_public_preview.png"
  "downloads/images/ikwe_board_brief.png"
  "downloads/images/ikwe_audit_report.png"
)

for file in "${FILES[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required artifact: $file" >&2
    exit 1
  fi
done

{
  echo "# Study II artifact manifest"
  echo "# Generated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "# Format: sha256  path"
  echo
  for file in "${FILES[@]}"; do
    shasum -a 256 "$file"
  done
} > "$OUT_FILE"

echo "Wrote $OUT_FILE"
