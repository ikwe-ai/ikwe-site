#!/usr/bin/env bash
set -euo pipefail

# IKWE.AI live site consistency check
# Focuses on production pages and avoids archive/backup noise.

cd "$(dirname "$0")"

LIVE_PAGES=(
  "index.html"
  "audit.html"
  "proof.html"
  "research.html"
  "inquiry.html"
  "about.html"
  "enterprise.html"
  "downloads.html"
  "press.html"
  "privacy.html"
  "terms.html"
  "404.html"
)

ANALYTICS_PAGES=(
  "index.html"
  "audit.html"
  "proof.html"
  "research.html"
  "inquiry.html"
  "about.html"
  "enterprise.html"
  "downloads.html"
  "press.html"
)

ERRORS=0
WARNINGS=0

echo "=========================================="
echo "  IKWE.AI Live Site Consistency Check"
echo "=========================================="
echo

echo "Pages scanned: ${#LIVE_PAGES[@]}"
echo

echo "1) Required files"
echo "-----------------"
for file in "${LIVE_PAGES[@]}"; do
  if [[ -f "$file" ]]; then
    echo "  OK  $file"
  else
    echo "  ERR missing file: $file"
    ERRORS=$((ERRORS + 1))
  fi
done
echo

echo "2) HTML closing tags"
echo "--------------------"
for file in "${LIVE_PAGES[@]}"; do
  [[ -f "$file" ]] || continue

  if ! rg -q '</html>' "$file"; then
    echo "  ERR $file missing </html>"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  if ! rg -q '</body>' "$file"; then
    echo "  ERR $file missing </body>"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  echo "  OK  $file"
done
echo

echo "3) Broken Cloudflare email-protection links"
echo "-------------------------------------------"
for file in "${LIVE_PAGES[@]}"; do
  [[ -f "$file" ]] || continue

  if rg -q '/cdn-cgi/l/email-protection|/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js' "$file"; then
    echo "  ERR $file contains Cloudflare-only email link/script"
    ERRORS=$((ERRORS + 1))
  else
    echo "  OK  $file"
  fi
done
echo

echo "4) Analytics script presence (warning-only)"
echo "-------------------------------------------"
for file in "${ANALYTICS_PAGES[@]}"; do
  [[ -f "$file" ]] || continue

  if rg -q 'plausible\.io/js/script\.js|window\.plausible' "$file"; then
    echo "  OK  $file"
  else
    echo "  WARN $file missing plausible analytics snippet"
    WARNINGS=$((WARNINGS + 1))
  fi
done
echo

echo "5) Local link and asset resolution"
echo "----------------------------------"
for file in "${LIVE_PAGES[@]}"; do
  [[ -f "$file" ]] || continue

  while IFS= read -r raw_path; do
    case "$raw_path" in
      http*|mailto:*|tel:*|\#*|javascript:*|data:* )
        continue
        ;;
    esac

    route_path="${raw_path%%\?*}"
    route_path="${route_path%%\#*}"

    [[ -z "$route_path" ]] && continue

    if [[ "$route_path" == */ ]]; then
      target=".${route_path}index.html"
      alt=".${route_path%/}.html"

      if [[ ! -e "$target" && ! -e "$alt" ]] && ! rg -q "^${route_path%/}[[:space:]]" _redirects; then
        echo "  ERR $file -> missing route $route_path"
        ERRORS=$((ERRORS + 1))
      fi
    else
      target=".${route_path}"
      alt=".${route_path}.html"

      if [[ ! -e "$target" && ! -e "$alt" ]] && ! rg -q "^${route_path}[[:space:]]" _redirects; then
        echo "  ERR $file -> missing path $route_path"
        ERRORS=$((ERRORS + 1))
      fi
    fi
  done < <(rg -o 'href="[^"]+"|src="[^"]+"' "$file" | sed -E 's/^[^"]+"([^"]+)"$/\1/' | sort -u)
done
echo

echo "=========================================="
echo "  SUMMARY"
echo "=========================================="
if [[ "$ERRORS" -eq 0 && "$WARNINGS" -eq 0 ]]; then
  echo "  PASS: no errors or warnings"
elif [[ "$ERRORS" -eq 0 ]]; then
  echo "  PASS with warnings: $WARNINGS"
else
  echo "  FAIL: $ERRORS errors, $WARNINGS warnings"
fi
echo "=========================================="

echo
exit "$ERRORS"
