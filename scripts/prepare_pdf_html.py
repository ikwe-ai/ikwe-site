from pathlib import Path
import datetime

pages = {
    'preview.html': 'ikwe_public_preview.pdf',
    'proof.html': 'ikwe_board_brief.pdf',
    'audit.html': 'ikwe_audit_report.pdf',
}

tmp_dir = Path('/tmp/ikwe-pdf')
tmp_dir.mkdir(exist_ok=True)

label = f"Sample — Redacted for External Distribution · {datetime.date.today().strftime('%B %d, %Y')}"

print_css = f"""
<style>
@media print {{
  nav, .nav, .footer, .nav-cta, .btn, .btn-primary, .btn-ghost, .tier-cta, .router-cta,
  .hero-actions, .cta-row, .cta, .cta-bar, .inquiry-links, .router-grid, .nav-links {{
    display: none !important;
  }}
  body {{ background: #fff !important; color: #111 !important; }}
}}
.pdf-label {{
  font-family: 'DM Sans', system-ui, sans-serif;
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #6b6b6b;
  margin: 18px 0 18px;
}}
.pdf-wrap {{ max-width: 900px; margin: 0 auto; padding: 24px 32px 16px; }}
</style>
"""

for src in pages.keys():
    html_path = Path(src)
    if not html_path.exists():
        raise SystemExit(f"Missing {src}")
    html = html_path.read_text(encoding='utf-8')
    if '</head>' in html:
        html = html.replace('</head>', print_css + '\n</head>', 1)
    body_marker = '<body>'
    if body_marker in html:
        insert = f"{body_marker}\n<div class=\"pdf-wrap\">\n  <div class=\"pdf-label\">{label}</div>\n</div>"
        html = html.replace(body_marker, insert, 1)
    tmp_path = tmp_dir / src
    tmp_path.write_text(html, encoding='utf-8')
    print(f"Prepared: {tmp_path}")
