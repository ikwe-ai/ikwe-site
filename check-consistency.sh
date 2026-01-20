#!/bin/bash
# IKWE.AI Site Consistency Check Script
# Run this before deploying to catch common issues

echo "=========================================="
echo "  IKWE.AI Site Consistency Check"
echo "=========================================="
echo ""

ERRORS=0
WARNINGS=0

# Change to site directory
cd "$(dirname "$0")" 2>/dev/null || cd /home/claude/ikwe-complete-site

echo "📁 Checking $(ls *.html 2>/dev/null | wc -l) HTML files..."
echo ""

# 1. FOOTER STRUCTURE CHECK
echo "1️⃣  FOOTER STRUCTURE"
echo "-------------------"
for file in *.html; do
  # Skip report-style pages that have different footers
  if [ "$file" = "full-report.html" ] || [ "$file" = "research-summary.html" ]; then
    echo "   ⏭️  $file (report layout - different footer)"
    continue
  fi
  
  # Count footer-col divs (should be 5 total including brand)
  cols=$(grep -c '<div class="footer-col' "$file" 2>/dev/null)
  
  # Count section headers ONLY within footer section
  footer_content=$(sed -n '/<footer/,/<\/footer>/p' "$file")
  research=$(echo "$footer_content" | grep -c '>Research<')
  company=$(echo "$footer_content" | grep -c '>Company<')
  support=$(echo "$footer_content" | grep -c '>Support<')
  connect=$(echo "$footer_content" | grep -c '>Connect<')
  
  # Should have exactly 5 footer-col divs, 1 of each header in footer
  if [ "$cols" -ne 5 ]; then
    echo "   ❌ $file: Wrong number of footer columns ($cols, expected 5)"
    ERRORS=$((ERRORS + 1))
  elif [ "$research" -ne 1 ] || [ "$company" -ne 1 ] || [ "$support" -ne 1 ] || [ "$connect" -ne 1 ]; then
    echo "   ❌ $file: Footer headers issue (R:$research C:$company S:$support Co:$connect)"
    ERRORS=$((ERRORS + 1))
  else
    echo "   ✅ $file"
  fi
done
echo ""

# 2. HTML CLOSING CHECK
echo "2️⃣  HTML STRUCTURE"
echo "-----------------"
for file in *.html; do
  if ! tail -5 "$file" | grep -q '</html>'; then
    echo "   ❌ $file: Missing </html> closing tag"
    ERRORS=$((ERRORS + 1))
  else
    echo "   ✅ $file"
  fi
done
echo ""

# 3. PLAUSIBLE ANALYTICS CHECK
echo "3️⃣  PLAUSIBLE ANALYTICS"
echo "----------------------"
for file in *.html; do
  if ! grep -q 'plausible.io' "$file"; then
    echo "   ❌ $file: Missing Plausible analytics"
    ERRORS=$((ERRORS + 1))
  else
    echo "   ✅ $file"
  fi
done
echo ""

# 4. OG IMAGE CHECK
echo "4️⃣  OG IMAGES"
echo "------------"
for file in *.html; do
  if ! grep -q 'og:image' "$file"; then
    echo "   ⚠️  $file: Missing og:image meta tag"
    WARNINGS=$((WARNINGS + 1))
  else
    og_image=$(grep -oP 'og:image" content="\K[^"]+' "$file" | head -1)
    if [ -n "$og_image" ]; then
      # Check if OG image file exists
      img_path=$(echo "$og_image" | sed 's|https://ikwe.ai/||')
      if [ -f "$img_path" ]; then
        echo "   ✅ $file → $img_path"
      else
        echo "   ⚠️  $file: OG image not found locally ($img_path)"
        WARNINGS=$((WARNINGS + 1))
      fi
    fi
  fi
done
echo ""

# 5. CANONICAL URL CHECK
echo "5️⃣  CANONICAL URLs"
echo "-----------------"
for file in *.html; do
  if ! grep -q 'rel="canonical"' "$file"; then
    echo "   ⚠️  $file: Missing canonical URL"
    WARNINGS=$((WARNINGS + 1))
  else
    echo "   ✅ $file"
  fi
done
echo ""

# 6. TWITTER CARD CHECK
echo "6️⃣  TWITTER CARDS"
echo "----------------"
for file in *.html; do
  if ! grep -q 'twitter:card' "$file"; then
    echo "   ⚠️  $file: Missing Twitter card meta"
    WARNINGS=$((WARNINGS + 1))
  else
    echo "   ✅ $file"
  fi
done
echo ""

# 7. NAV CONSISTENCY CHECK
echo "7️⃣  NAVIGATION"
echo "-------------"
nav_pattern=$(grep -o 'class="nav-links"' index.html | head -1)
for file in *.html; do
  if ! grep -q 'class="nav-links"' "$file"; then
    echo "   ⚠️  $file: Different nav structure"
    WARNINGS=$((WARNINGS + 1))
  else
    echo "   ✅ $file"
  fi
done
echo ""

# 8. ASSETS CHECK
echo "8️⃣  ASSETS"
echo "---------"
if [ -d "og" ]; then
  og_count=$(ls og/*.png 2>/dev/null | wc -l)
  echo "   ✅ OG images folder: $og_count PNG files"
else
  echo "   ❌ Missing og/ folder"
  ERRORS=$((ERRORS + 1))
fi

if [ -d "assets" ]; then
  asset_count=$(ls assets/* 2>/dev/null | wc -l)
  echo "   ✅ Assets folder: $asset_count files"
else
  echo "   ⚠️  Missing assets/ folder"
  WARNINGS=$((WARNINGS + 1))
fi

if [ -f "sitemap.xml" ]; then
  echo "   ✅ sitemap.xml exists"
else
  echo "   ❌ Missing sitemap.xml"
  ERRORS=$((ERRORS + 1))
fi

if [ -f "robots.txt" ]; then
  echo "   ✅ robots.txt exists"
else
  echo "   ❌ Missing robots.txt"
  ERRORS=$((ERRORS + 1))
fi
echo ""

# SUMMARY
echo "=========================================="
echo "  SUMMARY"
echo "=========================================="
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
  echo "  ✅ All checks passed!"
elif [ $ERRORS -eq 0 ]; then
  echo "  ⚠️  $WARNINGS warnings (no errors)"
else
  echo "  ❌ $ERRORS errors, $WARNINGS warnings"
fi
echo "=========================================="
echo ""

exit $ERRORS
