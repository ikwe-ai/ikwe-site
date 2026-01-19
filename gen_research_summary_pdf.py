from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


W, H = letter

def wrap_lines(c, text, font, size, max_width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        test = (line + " " + word).strip()
        if c.stringWidth(test, font, size) <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

def draw_paragraph(c, text, x, y, max_width, font="Helvetica", size=10, leading=12):
    c.setFont(font, size)
    for ln in wrap_lines(c, text, font, size, max_width):
        c.drawString(x, y, ln)
        y -= leading
    return y

def generate(path):
    c = canvas.Canvas(path, pagesize=letter)

    margin = 54
    x = margin
    y = H - margin
    max_w = W - 2*margin

    # Page 1
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "Ikwe.ai — EQ Safety Benchmark")
    y -= 20
    c.setFont("Helvetica-Bold", 18)
    c.drawString(x, y, "Research Summary")
    y -= 26

    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y, "The Emotional Safety Gap")
    y -= 18
    c.setFont("Helvetica", 11)
    c.drawString(x, y, "Behavioral Emotional Safety in Conversational AI — Research Summary")
    y -= 22

    c.setFont("Helvetica-Bold", 11)
    c.drawString(x, y, "Passed Safety Gate")
    c.drawString(x + 170, y, "Introduced Risk")
    c.drawString(x + 320, y, "No Correction")
    y -= 16
    c.setFont("Helvetica-Bold", 18)
    c.drawString(x, y, "54.7%")
    c.drawString(x + 180, y, "45.3%")
    c.drawString(x + 330, y, "43%")
    y -= 24

    y = draw_paragraph(
        c,
        "Recognition ≠ Safety. AI systems can accurately identify emotions while still responding in ways that increase distress.",
        x, y, max_w, font="Helvetica", size=10, leading=12
    )
    y -= 4
    y = draw_paragraph(
        c,
        "This research measures what happens when humans trust AI systems — especially under emotional load.",
        x, y, max_w, font="Helvetica", size=10, leading=12
    )
    y -= 14

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, "The Two-Stage Framework")
    y -= 16

    y = draw_paragraph(
        c,
        "Stage 1 — Safety Gate (Pass/Fail): Binary detection of behaviors that introduce emotional risk at first contact. 45.3% of baseline AI responses failed this gate.",
        x, y, max_w, font="Helvetica", size=10, leading=12
    )
    y -= 4
    y = draw_paragraph(
        c,
        "Stage 2 — Behavioral Quality (Conditional): Weighted scoring across regulation, acknowledgment, and trajectory dimensions. Only responses passing Stage 1 are scored.",
        x, y, max_w, font="Helvetica", size=10, leading=12
    )
    y -= 8

    # Trajectory caption (new)
    c.setFont("Helvetica-Oblique", 9)
    y = draw_paragraph(
        c,
        "Trajectory-aware safety evaluates patterns across time, not individual responses in isolation. This is why local evaluation (per-response) misses cumulative risk.",
        x, y, max_w, font="Helvetica-Oblique", size=9, leading=11
    )
    y -= 14

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, "Model Performance (Stage 2 Conditional Scores)")
    y -= 16

    y = draw_paragraph(
        c,
        "Regulation Score (0–5): Measures how effectively responses stabilize emotional state. Weighted across: emotional regulation (35%), acknowledgment quality (25%), response trajectory (20%), safety awareness (15%), and contextual fit (5%).",
        x, y, max_w, font="Helvetica", size=10, leading=12
    )
    y -= 10

    # Table
    table_data = [
        ["Model", "Stage 2 Score", "Regulation"],
        ["Ikwe EI Prototype", "84.6%", "4.05/5"],
        ["GPT-4o", "59.0%", "2.95/5"],
        ["Claude 3.5 Sonnet", "56.4%", "2.82/5"],
        ["Grok", "20.5%", "1.02/5"],
    ]

    col_widths = [max_w*0.45, max_w*0.275, max_w*0.275]
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), (0.1,0.1,0.1)),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.whitesmoke, colors.lightgrey]),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    w, h = t.wrapOn(c, max_w, y)
    t.drawOn(c, x, y - h)
    y -= (h + 12)

    c.setFont("Helvetica-Oblique", 9)
    y = draw_paragraph(
        c,
        "Note: Stage 2 scores are conditional — they measure regulation quality only among responses that passed the Stage 1 Safety Gate.",
        x, y, max_w, font="Helvetica-Oblique", size=9, leading=11
    )
    y -= 8

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, "Common Safety Gate Failures")
    y -= 14

    bullets = [
        "Premature problem-solving before emotional validation",
        "Toxic positivity that dismisses expressed distress",
        "Abandonment via referral without presence",
        "Distress amplification through mirroring",
        "Minimization of user experience",
    ]
    c.setFont("Helvetica", 10)
    for b in bullets:
        c.drawString(x + 10, y, "• " + b)
        y -= 12

    # Footer
    c.setFont("Helvetica", 9)
    c.drawString(x, 36, "© 2026 Visible Healing Inc. | https://ikwe.ai")
    c.showPage()

    # Page 2
    x = margin
    y = H - margin
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "Ikwe.ai — EQ Safety Benchmark")
    y -= 20
    c.setFont("Helvetica-Bold", 18)
    c.drawString(x, y, "Research Summary")
    y -= 26

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, "Why This Matters")
    y -= 16
    y = draw_paragraph(
        c,
        "As AI systems enter mental health, wellness, caregiving, and education contexts, the gap between sounding supportive and being safe becomes critical. A response can be accurate, policy-compliant, and well-articulated — and still increase harm. Current safety frameworks don't measure this.",
        x, y, max_w, font="Helvetica", size=10, leading=12
    )
    y -= 14

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, "Methodology")
    y -= 16
    y = draw_paragraph(
        c,
        "948 responses evaluated across 79 scenarios from 8 public datasets, spanning 12 vulnerability categories. Four frontier AI systems tested under identical conditions. Full methodology and scoring rubrics available upon request.",
        x, y, max_w, font="Helvetica", size=10, leading=12
    )
    y -= 20

    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, "Full Report")
    c.drawString(x + 170, y, "Partnership")
    c.drawString(x + 320, y, "Contact")
    y -= 14
    c.setFont("Helvetica", 10)
    c.drawString(x, y, "ikwe.ai/full-report")
    c.drawString(x + 170, y, "ikwe.ai/partner")
    c.drawString(x + 320, y, "research@ikwe.ai")
    y -= 20

    c.setFont("Helvetica", 9)
    y = draw_paragraph(
        c,
        "Citation: Ikwe.ai. (2026). The Emotional Safety Gap: Behavioral Emotional Safety in Conversational AI. Visible Healing Inc. https://ikwe.ai/research",
        x, y, max_w, font="Helvetica", size=9, leading=11
    )

    c.setFont("Helvetica", 9)
    c.drawString(x, 36, "© 2026 Visible Healing Inc. | https://ikwe.ai")
    c.save()

if __name__ == "__main__":
    generate("Ikwe_Research_Summary.pdf")
