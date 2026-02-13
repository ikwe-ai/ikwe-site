#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "== Study II release gate =="
echo

echo "1) Recompute headline metrics"
python3 research/analysis/reproduce_headline_metrics.py
echo

echo "2) Consistency check"
python3 research/analysis/consistency_check.py
echo

echo "3) Claims integrity check"
bash scripts/study_ii_claims_check.sh
echo

echo "4) Live QA scan"
bash scripts/live_qa_scan.sh
echo

echo "5) Site consistency check"
./check-consistency.sh
echo

echo "PASS: release gate checks complete"
