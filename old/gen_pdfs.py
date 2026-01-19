from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

styles = getSampleStyleSheet()

TRAJECTORY_CAPTION = (
    "Trajectory-aware safety evaluates patterns across time, not individual responses in isolation. "
    "This is why local evaluation (per-response) misses cumulative risk."
)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(doc.leftMargin, 0.5 * inch, "© 2026 Visible Healing Inc. | https://ikwe.ai")
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()

# Need inch from reportlab
from reportlab.lib.units import inch


def build_research_summary(path):
    doc = SimpleDocTemplate(path, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    story = []

    story.append(Paragraph("Ikwe.ai — EQ Safety Benchmark", styles['Heading2']))
    story.append(Paragraph("Research Summary", styles['Heading1']))
    story.append(Spacer(1, 8))

    story.append(Paragraph("The Emotional Safety Gap", styles['Heading2']))
    story.append(Paragraph("Behavioral Emotional Safety in Conversational AI — Research Summary", styles['Normal']))
    story.append(Spacer(1, 12))

    stats = Table([
        ["Passed Safety Gate", "Introduced Risk", "No Correction"],
        ["54.7%", "45.3%", "43%"],
    ], colWidths=[(doc.width)/3]*3)
    stats.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 10),
        ('FONTSIZE', (0,1), (-1,1), 18),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('TOPPADDING', (0,1), (-1,1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ]))
    story.append(stats)
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        "<b>Recognition ≠ Safety.</b> AI systems can accurately identify emotions while still responding in ways that increase distress. "
        "This research measures what happens when humans trust AI systems — especially under emotional load.",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph("The Two-Stage Framework", styles['Heading2']))
    story.append(Paragraph(
        "<b>Stage 1 — Safety Gate (Pass/Fail):</b> Binary detection of behaviors that introduce emotional risk at first contact. "
        "45.3% of baseline AI responses failed this gate.",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Stage 2 — Behavioral Quality (Conditional):</b> Weighted scoring across regulation, acknowledgment, and trajectory dimensions. "
        "Only responses passing Stage 1 are scored.",
        styles['Normal']
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"<i>{TRAJECTORY_CAPTION}</i>", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Model Performance (Stage 2 Conditional Scores)", styles['Heading2']))
    story.append(Paragraph(
        "<b>Regulation Score (0–5):</b> Measures how effectively responses help stabilize emotional state. "
        "Weighted across: emotional regulation (35%), acknowledgment quality (25%), response trajectory (20%), "
        "safety awareness (15%), and contextual fit (5%).",
        styles['Normal']
    ))
    story.append(Spacer(1, 10))

    table = Table([
        ["Model", "Stage 2 Score", "Regulation"],
        ["Ikwe EI Prototype", "84.6%", "4.05/5"],
        ["GPT-4o", "59.0%", "2.95/5"],
        ["Claude 3.5 Sonnet", "56.4%", "2.82/5"],
        ["Grok", "20.5%", "1.02/5"],
    ], colWidths=[doc.width*0.5, doc.width*0.25, doc.width*0.25])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (1,1), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
    ]))
    story.append(table)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<i>Note: Stage 2 scores are conditional — they measure regulation quality only among responses that passed the Stage 1 Safety Gate.</i>",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Common Safety Gate Failures", styles['Heading2']))
    bullets = [
        "Premature problem-solving before emotional validation",
        "Toxic positivity that dismisses expressed distress",
        "Abandonment via referral without presence",
        "Distress amplification through mirroring",
        "Minimization of user experience",
    ]
    story.append(ListFlowable([ListItem(Paragraph(b, styles['Normal'])) for b in bullets], bulletType='bullet'))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Why This Matters", styles['Heading2']))
    story.append(Paragraph(
        "As AI systems enter mental health, wellness, caregiving, and education contexts, the gap between sounding supportive and being safe becomes critical. "
        "A response can be accurate, policy-compliant, and well-articulated — and still increase harm. Current safety frameworks don't measure this.",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Methodology", styles['Heading2']))
    story.append(Paragraph(
        "948 responses evaluated across 79 scenarios from 8 public datasets, spanning 12 vulnerability categories. "
        "Four frontier AI systems tested under identical conditions. Full methodology and scoring rubrics available upon request.",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))

    info = Table([
        ["Full Report", "Partnership", "Contact"],
        ["ikwe.ai/full-report", "ikwe.ai/partner", "research@ikwe.ai"],
    ], colWidths=[doc.width/3]*3)
    info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ]))
    story.append(info)
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "<b>Citation:</b> Ikwe.ai. (2026). <i>The Emotional Safety Gap: Behavioral Emotional Safety in Conversational AI.</i> Visible Healing Inc. https://ikwe.ai/research",
        styles['Normal']
    ))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def build_full_report(path):
    doc = SimpleDocTemplate(path, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    story = []

    story.append(Paragraph("Ikwe.ai — Behavioral Emotional Safety in Conversational AI", styles['Heading2']))
    story.append(Paragraph("Full Research Report", styles['Heading1']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Behavioral Emotional Safety in Conversational AI", styles['Heading2']))
    story.append(Paragraph("A Scenario-Based Evaluation of Frontier AI Systems", styles['Normal']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("EQ Safety Benchmark v1 — January 2026", styles['Normal']))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Ikwe.ai | Visible Healing Inc.", styles['Normal']))
    story.append(Paragraph("research@ikwe.ai | https://ikwe.ai", styles['Normal']))
    story.append(PageBreak())

    story.append(Paragraph("Executive Summary", styles['Heading2']))
    story.append(Paragraph(
        "This report presents findings from the EQ Safety Benchmark, a two-stage evaluation framework designed to measure behavioral emotional safety in conversational AI systems. "
        "We evaluated 948 AI responses across 79 emotionally vulnerable scenarios, testing four frontier AI systems.",
        styles['Normal']
    ))
    story.append(Spacer(1, 12))

    key = Table([
        ["Passed Safety Gate", "Introduced Risk", "No Correction", "Avg. Regulation"],
        ["54.7%", "45.3%", "43%", "1.7/5"],
    ], colWidths=[doc.width/4]*4)
    key.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,1), (-1,1), 14),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ]))
    story.append(key)
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        "<b>Core Finding:</b> AI systems can accurately recognize emotions while still responding in ways that increase distress. "
        "<b>Recognition ≠ Safety.</b> High emotional articulation often correlates with worse behavioral safety scores.",
        styles['Normal']
    ))
    story.append(PageBreak())

    story.append(Paragraph("Methodology", styles['Heading2']))
    story.append(Paragraph("Two-Stage Evaluation Framework", styles['Heading3']))
    story.append(Paragraph(
        "The EQ Safety Benchmark uses a two-stage approach to separate harm detection from quality measurement:",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Stage 1 — Safety Gate (Pass/Fail):</b> Binary detection of behaviors that introduce emotional risk at first contact.",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>Stage 2 — Behavioral Quality (Conditional):</b> Only responses that pass Stage 1 proceed to Stage 2 scoring. Quality is measured across weighted dimensions: emotional regulation (35%), acknowledgment quality (25%), response trajectory (20%), safety awareness (15%), and contextual appropriateness (5%).",
        styles['Normal']
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"<i>{TRAJECTORY_CAPTION}</i>", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Data Sources", styles['Heading3']))
    story.append(Paragraph(
        "Scenarios were derived from 8 public datasets, covering 12 vulnerability categories: grief/loss, trauma/abuse, loneliness, crisis situations, relationship distress, work stress, health anxiety, financial stress, identity/self-worth, family conflict, social rejection, and life transitions.",
        styles['Normal']
    ))
    story.append(PageBreak())

    story.append(Paragraph("Results", styles['Heading2']))
    story.append(Paragraph("Model Performance Comparison", styles['Heading3']))
    story.append(Paragraph(
        "Stage 2 scores reflect performance only among responses that passed the Stage 1 Safety Gate. These are conditional scores measuring regulation quality after avoiding initial harm.",
        styles['Normal']
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Understanding the Regulation Score", styles['Heading3']))
    story.append(Paragraph(
        "The Regulation Score (0–5 scale) measures how effectively a response helps stabilize the user's emotional state. "
        "Higher scores indicate better emotional co-regulation — the response helps the user move toward stability rather than amplifying distress or dismissing it.",
        styles['Normal']
    ))
    story.append(Spacer(1, 10))

    perf = Table([
        ["Model", "Safety Gate", "Stage 2 Score", "Regulation"],
        ["Ikwe EI Prototype", "Pass", "84.6%", "4.05/5"],
        ["GPT-4o", "Pass", "59.0%", "2.95/5"],
        ["Claude 3.5 Sonnet", "Pass", "56.4%", "2.82/5"],
        ["Grok", "Pass", "20.5%", "1.02/5"],
    ], colWidths=[doc.width*0.4, doc.width*0.2, doc.width*0.2, doc.width*0.2])
    perf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (1,1), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ]))
    story.append(perf)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Common Safety Gate Failures", styles['Heading2']))
    bullets = [
        "Premature Problem-Solving: Offering solutions before acknowledging emotional reality",
        "Toxic Positivity: Reassurance that dismisses or minimizes expressed distress",
        "Abandonment via Referral: Redirecting to professional help without providing presence first",
        "Distress Amplification: Mirroring or escalating the user's emotional state",
        "Minimization: Downplaying the significance of the user's experience",
    ]
    story.append(ListFlowable([ListItem(Paragraph(b, styles['Normal'])) for b in bullets], bulletType='bullet'))
    story.append(PageBreak())

    story.append(Paragraph("Implications", styles['Heading2']))
    story.append(Paragraph("<b>For AI Developers:</b> Standard safety evaluations focus on content policy compliance and factual accuracy. These findings suggest that behavioral safety — how responses land on users emotionally — requires dedicated evaluation infrastructure.", styles['Normal']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>For Organizations Deploying AI:</b> Organizations using conversational AI in sensitive contexts should implement behavioral safety evaluation before deployment. The gap between expected and actual emotional safety is significant and measurable.", styles['Normal']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>For Policymakers:</b> Emotional safety — the behavioral impact of AI interactions on vulnerable users — is not yet addressed in major regulatory frameworks. These findings suggest it should be.", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Limitations", styles['Heading2']))
    limitations = [
        "Test conditions: Results reflect controlled scenarios, not naturalistic conversation",
        "Sample size: 79 scenarios across 4 systems; broader coverage needed for generalization",
        "Static evaluation: Models are updated frequently; results may not reflect current versions",
        "Cultural context: Scenarios primarily reflect Western emotional frameworks",
        "No longitudinal data: We measure single interactions, not long-term effects",
    ]
    story.append(ListFlowable([ListItem(Paragraph(b, styles['Normal'])) for b in limitations], bulletType='bullet'))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Citation", styles['Heading2']))
    story.append(Paragraph(
        "Ikwe.ai. (2026). <i>The Emotional Safety Gap: Behavioral Emotional Safety in Conversational AI.</i> Visible Healing Inc. https://ikwe.ai/full-report",
        styles['Normal']
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Contact", styles['Heading2']))
    story.append(Paragraph("Research Inquiries: research@ikwe.ai", styles['Normal']))
    story.append(Paragraph("Partnership: https://ikwe.ai/partner", styles['Normal']))
    story.append(Paragraph("Full Methodology Access: https://ikwe.ai/inquiry", styles['Normal']))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == '__main__':
    build_research_summary('Ikwe_Research_Summary.pdf')
    build_full_report('Ikwe_Full_Report.pdf')
