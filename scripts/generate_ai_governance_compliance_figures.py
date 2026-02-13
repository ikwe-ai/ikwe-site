#!/usr/bin/env python3
"""Generate AI governance canon figures as SVG and PNG assets."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "research" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

BG = "#0f1117"
PANEL = "#171b24"
TEXT = "#e9eefc"
MUTED = "#aeb7ce"
LILAC = "#b794f6"
CORAL = "#f6a192"
TEAL = "#59d6c2"
AMBER = "#f6d992"
GREEN = "#89c7a2"
RED = "#f08a8a"


def base_canvas():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=220)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    return fig, ax


def save(fig, basename):
    svg_path = OUT_DIR / f"{basename}.svg"
    png_path = OUT_DIR / f"{basename}.png"
    fig.savefig(svg_path, format="svg", facecolor=BG, bbox_inches="tight", pad_inches=0.2)
    fig.savefig(png_path, format="png", facecolor=BG, bbox_inches="tight", pad_inches=0.2, dpi=240)
    plt.close(fig)


def draw_governance_window():
    fig, ax = base_canvas()
    ax.text(
        4,
        95,
        "Figure 1. The Governance Window",
        color=TEXT,
        fontsize=25,
        fontweight="bold",
        ha="left",
    )
    ax.text(
        4,
        89,
        "Risk accumulation timeline from fluent output to enforceable incident.",
        color=MUTED,
        fontsize=12,
        ha="left",
    )

    zones = [
        ("A", "Model fluency +\nconfidence cues", "#263040"),
        ("B", "Human deference\nbegins", "#2f304a"),
        ("C", "Behavioral drift\n(pattern repeats)", "#3a2f4f"),
        ("D", "Escalation\n(stakes increase)", "#4a2e46"),
        ("E", "Policy breach / harm /\ncomplaint / enforcement", "#5c2c3d"),
    ]

    x_start = 6
    width = 17.2
    gap = 1.5
    y = 34
    height = 30

    for i, (letter, label, color) in enumerate(zones):
        x = x_start + i * (width + gap)
        box = FancyBboxPatch(
            (x, y),
            width,
            height,
            boxstyle="round,pad=0.6,rounding_size=2.2",
            linewidth=1.5,
            edgecolor="#6f7384",
            facecolor=color,
        )
        ax.add_patch(box)
        ax.add_patch(Circle((x + 3.0, y + height - 4), 2.4, facecolor="#101319", edgecolor="#73778a", linewidth=1))
        ax.text(x + 3.0, y + height - 4.05, letter, color=TEXT, fontsize=10, fontweight="bold", ha="center", va="center")
        ax.text(x + width / 2, y + height / 2 - 1, label, color=TEXT, fontsize=11, ha="center", va="center")

        if i < len(zones) - 1:
            arrow = FancyArrowPatch(
                (x + width + 0.2, y + height / 2),
                (x + width + gap - 0.1, y + height / 2),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=1.2,
                color="#8a8fa3",
            )
            ax.add_patch(arrow)

    ax.add_patch(
        FancyArrowPatch(
            (x_start - 1.5, 25),
            (96, 25),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=1.6,
            color="#7f859a",
        )
    )
    ax.text(49, 20, "Interaction Timeline", color=MUTED, fontsize=11, ha="center")

    b_start = x_start + (width + gap)
    d_end = x_start + 3 * (width + gap) + width
    ax.plot([b_start, b_start, d_end, d_end], [77, 72, 72, 77], color=TEAL, linewidth=2.2)
    ax.text((b_start + d_end) / 2, 79.5, "Intervention Window", color=TEAL, fontsize=13, fontweight="bold", ha="center")

    save(fig, "ikwe-figure-1-governance-window")


def draw_trust_layer_stack():
    fig, ax = base_canvas()
    ax.text(4, 95, "Figure 2. Trust Layer Stack", color=TEXT, fontsize=25, fontweight="bold", ha="left")
    ax.text(
        4,
        89,
        "Governance maturity ladder with Ikwe behavioral instrumentation highlighted.",
        color=MUTED,
        fontsize=12,
        ha="left",
    )

    layers = [
        "1  Content Safety / Output Filtering",
        "2  Policy & Guidelines",
        "3  Monitoring & Logging",
        "4  Human Oversight (procedural)",
        "5  Behavioral Risk Instrumentation (Ikwe zone)",
        "6  Audit-Ready Governance (evidence, controls, reporting)",
    ]

    x = 15
    width = 62
    h = 10.2
    gap = 2.4
    base_y = 14

    for idx, label in enumerate(layers):
        y = base_y + idx * (h + gap)
        is_ikwe = idx == 4
        is_top = idx == 5
        face = PANEL
        edge = "#6f7386"
        text_color = TEXT
        if is_ikwe:
            face = "#332c4c"
            edge = LILAC
        if is_top:
            face = "#233742"
            edge = TEAL

        box = FancyBboxPatch(
            (x, y),
            width,
            h,
            boxstyle="round,pad=0.6,rounding_size=2",
            linewidth=2 if (is_ikwe or is_top) else 1.4,
            edgecolor=edge,
            facecolor=face,
        )
        ax.add_patch(box)
        ax.text(x + 2.4, y + h / 2, label, color=text_color, fontsize=11, fontweight="bold" if is_ikwe else "normal", va="center")

    y5 = base_y + 4 * (h + gap) + h / 2
    y6 = base_y + 5 * (h + gap) + h / 2
    x_arrow = x + width + 5
    ax.add_patch(
        FancyArrowPatch(
            (x_arrow, y5),
            (x_arrow, y6),
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=2.2,
            color=AMBER,
        )
    )
    ax.text(
        x_arrow + 2.2,
        (y5 + y6) / 2,
        "Instrumentation -> defensible\ncompliance evidence",
        color=AMBER,
        fontsize=10.8,
        va="center",
        ha="left",
    )

    tag = FancyBboxPatch(
        (x + width + 2, y5 - 3.2),
        16,
        6.4,
        boxstyle="round,pad=0.4,rounding_size=1.5",
        linewidth=1.2,
        edgecolor=LILAC,
        facecolor="#2a2340",
    )
    ax.add_patch(tag)
    ax.text(x + width + 10, y5, "Ikwe zone", color=LILAC, fontsize=10, ha="center", va="center")

    save(fig, "ikwe-figure-2-trust-layer-stack")


def draw_confidence_curve():
    fig, ax = base_canvas()
    ax.text(4, 95, "Figure 3. Confidence -> Deference Curve", color=TEXT, fontsize=25, fontweight="bold", ha="left")
    ax.text(
        4,
        89,
        "As AI confidence cues increase, human critical evaluation can degrade without controls.",
        color=MUTED,
        fontsize=12,
        ha="left",
    )

    ax.add_patch(FancyArrowPatch((12, 12), (92, 12), arrowstyle="-|>", mutation_scale=16, linewidth=2, color="#7b8196"))
    ax.add_patch(FancyArrowPatch((12, 12), (12, 88), arrowstyle="-|>", mutation_scale=16, linewidth=2, color="#7b8196"))

    ax.text(52, 4.5, "AI Confidence Signals (tone/certainty/fluency/speed)", color=MUTED, fontsize=11, ha="center")
    ax.text(
        2.5,
        51,
        "Human Critical Evaluation\n(verification/skepticism/second opinions)",
        color=MUTED,
        fontsize=10.5,
        ha="center",
        va="center",
        rotation=90,
    )

    x = np.linspace(14, 90, 240)
    t = (x - 14) / (90 - 14)
    y = 84 - 60 * (t ** 1.22)
    ax.plot(x, y, color=LILAC, linewidth=3.2)

    ax.fill_between([39, 65], [56, 56], [40, 40], color=GREEN, alpha=0.23)
    ax.text(52, 58.7, "Appropriate reliance zone", color=GREEN, fontsize=11, fontweight="bold", ha="center")

    threshold_y = 36
    ax.hlines(threshold_y, 14, 90, colors=RED, linestyles="dashed", linewidth=2)
    ax.text(89.2, threshold_y + 1.8, "Overreliance threshold", color=RED, fontsize=10.5, ha="right")

    handoff_x = 72
    handoff_y = 84 - 60 * (((handoff_x - 14) / (90 - 14)) ** 1.22)
    ax.scatter([handoff_x], [handoff_y], s=52, color=CORAL, zorder=5)
    ax.annotate(
        "Accountability\nhandoff",
        xy=(handoff_x, handoff_y),
        xytext=(79, handoff_y + 16),
        color=CORAL,
        fontsize=10.5,
        ha="center",
        arrowprops={"arrowstyle": "->", "color": CORAL, "lw": 1.7},
    )

    ax.text(86, 20, "High deference risk", color="#dcb5b5", fontsize=10, ha="right")

    save(fig, "ikwe-figure-3-confidence-deference-curve")


def main():
    draw_governance_window()
    draw_trust_layer_stack()
    draw_confidence_curve()
    print(f"Generated figures in {OUT_DIR}")


if __name__ == "__main__":
    main()
