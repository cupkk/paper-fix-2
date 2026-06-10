from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "figures" / "summary"

BLUE = "#4C78A8"
BLUE_DARK = "#0F4D92"
GREEN = "#59A14F"
GREEN_LIGHT = "#8BCF8B"
ORANGE = "#F28E2B"
RED = "#E15759"
GRAY = "#BAB0AC"
GRAY_DARK = "#4D4D4D"
TEAL = "#76B7B2"


def apply_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": 9.5,
            "axes.labelsize": 10.0,
            "xtick.labelsize": 9.0,
            "ytick.labelsize": 9.0,
            "legend.fontsize": 8.6,
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "legend.frameon": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.16,
        1.11,
        label,
        transform=ax.transAxes,
        fontsize=12.0,
        fontweight="bold",
        va="top",
        ha="left",
    )


def clean_axes(ax: plt.Axes, grid: bool = True) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(width=0.8, length=3)
    if grid:
        ax.grid(axis="y", color="#E6E6E6", linestyle="--", linewidth=0.5, alpha=0.75)
        ax.set_axisbelow(True)


def save_all(fig: plt.Figure, basename: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for suffix in ("png", "pdf", "svg"):
        path = OUT_DIR / f"{basename}.{suffix}"
        fig.savefig(path, dpi=600 if suffix == "png" else None, bbox_inches="tight", pad_inches=0.05)


def ablation_sensitivity_summary() -> None:
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(7.1, 2.35), constrained_layout=True)

    # Panel a: component ablation, using values from Tables 1 and 3.
    variants = ["Trans.", "-Dyn", "-TE", "-KB", "Full"]
    log_loss = np.array([0.5698, 0.5642, 0.5510, 0.5385, 0.5163])
    recall5 = np.array([0.3846, 0.3891, 0.3957, 0.4023, 0.4185])
    x = np.arange(len(variants))
    ax = axes[0]
    ax.plot(x, log_loss, marker="o", color=BLUE_DARK, linewidth=1.2, markersize=3.2, label="Log Loss")
    ax.set_ylabel("Log Loss", color=BLUE_DARK)
    ax.tick_params(axis="y", colors=BLUE_DARK)
    ax.set_xticks(x)
    ax.set_xticklabels(variants, rotation=35, ha="right")
    ax.set_ylim(0.505, 0.58)
    ax2 = ax.twinx()
    ax2.plot(x, recall5, marker="s", color=ORANGE, linewidth=1.2, markersize=3.0, label="Recall@5")
    ax2.set_ylabel("Recall@5", color=ORANGE)
    ax2.tick_params(axis="y", colors=ORANGE)
    ax2.set_ylim(0.375, 0.425)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(ORANGE)
    clean_axes(ax)
    panel_label(ax, "a")
    lines = ax.get_lines() + ax2.get_lines()
    ax.legend(lines, [line.get_label() for line in lines], loc="lower left", handlelength=1.6)

    # Panel b: feature-family occlusion, using Table 4.
    ax = axes[1]
    groups = [
        "Knowledge-\nretrieved",
        "Transaction\n dynamics",
        "Macro\n indicators",
        "Quasi-static\n profile",
    ]
    drops = np.array([3.92, 2.87, 1.55, 0.93])
    colors = [BLUE_DARK, BLUE, TEAL, GRAY]
    ypos = np.arange(len(groups))
    ax.barh(ypos, drops, color=colors, edgecolor="white", linewidth=0.5)
    ax.set_yticks(ypos)
    ax.set_yticklabels(groups)
    ax.invert_yaxis()
    ax.set_xlabel("AUC drop (%)")
    ax.set_xlim(0, 4.4)
    for y, value in zip(ypos, drops):
        ax.text(value + 0.08, y, f"{value:.2f}", va="center", fontsize=8.0)
    clean_axes(ax, grid=False)
    ax.grid(axis="x", color="#E6E6E6", linestyle="--", linewidth=0.5, alpha=0.75)
    panel_label(ax, "b")

    # Panel c: retrieval-depth sensitivity, using Table 5.
    ax = axes[2]
    k = np.array([1, 3, 5, 7, 10])
    depth_loss = np.array([0.5287, 0.5214, 0.5163, 0.5175, 0.5189])
    depth_rec = np.array([0.4068, 0.4117, 0.4185, 0.4173, 0.4160])
    ax.plot(k, depth_loss, marker="o", color=BLUE_DARK, linewidth=1.2, markersize=3.2, label="Log Loss")
    ax.set_xlabel("Retrieved documents K")
    ax.set_ylabel("Log Loss", color=BLUE_DARK)
    ax.tick_params(axis="y", colors=BLUE_DARK)
    ax.set_xticks(k)
    ax.set_ylim(0.514, 0.531)
    ax2 = ax.twinx()
    ax2.plot(k, depth_rec, marker="s", color=ORANGE, linewidth=1.2, markersize=3.0, label="Recall@5")
    ax2.set_ylabel("Recall@5", color=ORANGE)
    ax2.tick_params(axis="y", colors=ORANGE)
    ax2.set_ylim(0.404, 0.421)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(ORANGE)
    ax.axvline(5, color=GREEN, linestyle="--", linewidth=0.9)
    ax.text(5.15, 0.530, "selected", color=GREEN, fontsize=8.0, va="top")
    clean_axes(ax)
    panel_label(ax, "c")

    save_all(fig, "ablation_sensitivity_summary")
    plt.close(fig)


def operational_evaluation_summary() -> None:
    apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(7.1, 4.7), constrained_layout=True)
    axes = axes.ravel()

    # Panel a: scenario adaptation, R@5 relative lift from Table 2.
    ax = axes[0]
    methods = ["Baseline", "LP-FT", "LoRA-FT", "Full-FT"]
    credit_r5 = np.array([0.0, 2.97, 12.63, 17.10])
    mortgage_r5 = np.array([0.0, 2.45, 10.88, 15.33])
    x = np.arange(len(methods))
    width = 0.36
    ax.bar(x - width / 2, credit_r5, width, color=BLUE, label="Credit card", edgecolor="white", linewidth=0.5)
    ax.bar(x + width / 2, mortgage_r5, width, color=GREEN_LIGHT, label="Mortgage", edgecolor="white", linewidth=0.5)
    ax.set_ylabel("R@5 lift (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=30, ha="right")
    ax.set_ylim(0, 20)
    ax.legend(loc="upper left", ncol=1)
    clean_axes(ax)
    panel_label(ax, "a")

    # Panel b: explanation-quality gains over template baseline, using Table 6.
    ax = axes[1]
    metrics = ["Faithfulness", "Readability", "ROUGE-L"]
    template = np.array([3.89, 4.02, 0.3026])
    fraa = np.array([4.32, 4.51, 0.4131])
    gains = (fraa - template) / template * 100.0
    ax.bar(np.arange(len(metrics)), gains, color=[BLUE, BLUE, BLUE_DARK], edgecolor="white", linewidth=0.5)
    ax.set_xticks(np.arange(len(metrics)))
    ax.set_xticklabels(metrics, rotation=20, ha="right")
    ax.set_ylabel("Relative gain (%)")
    ax.set_ylim(0, 42)
    for i, value in enumerate(gains):
        ax.text(i, value + 1.0, f"{value:.1f}%", ha="center", va="bottom", fontsize=8.0)
    clean_axes(ax)
    panel_label(ax, "b")

    # Panel c: latency-throughput trade-off, using Table 7.
    ax = axes[2]
    models = ["RF+KB", "XGBoost", "LSTM", "Transformer", "FRAA"]
    latency = np.array([1.9, 2.1, 8.3, 12.4, 15.7])
    throughput = np.array([12530, 11200, 5910, 4320, 4070])
    colors = [GRAY, GRAY, TEAL, ORANGE, BLUE_DARK]
    ax.scatter(latency, throughput, s=28, color=colors, edgecolor="white", linewidth=0.6)
    label_offsets = {
        "RF+KB": (0.25, 360),
        "XGBoost": (0.25, 360),
        "LSTM": (0.25, 360),
        "Transformer": (0.25, 520),
        "FRAA": (-2.1, -420),
    }
    for xi, yi, label in zip(latency, throughput, models):
        dx, dy = label_offsets[label]
        ax.text(xi + dx, yi + dy, label, fontsize=8.0)
    ax.set_xlabel("Latency (ms/query)")
    ax.set_ylabel("Throughput (queries/s)")
    ax.set_xlim(0, 18)
    ax.set_ylim(2500, 14000)
    clean_axes(ax)
    panel_label(ax, "c")

    # Panel d: offline business utility, using Table 8.
    ax = axes[3]
    models = ["RF+KB", "Transformer", "FRAA -KB", "FRAA"]
    log_reduction = np.array([2.06, 11.26, 16.13, 19.59])
    rar_lift = np.array([1.89, 5.34, 7.80, 10.45])
    colors = [GRAY, ORANGE, TEAL, BLUE_DARK]
    ax.plot(log_reduction, rar_lift, color="#B0B0B0", linestyle="--", linewidth=0.9, zorder=1)
    ax.scatter(log_reduction, rar_lift, s=30, color=colors, edgecolor="white", linewidth=0.6, zorder=2)
    for xi, yi, label in zip(log_reduction, rar_lift, models):
        ax.text(xi + 0.25, yi + 0.25, label, fontsize=8.0)
    ax.set_xlabel("Log Loss reduction (%)")
    ax.set_ylabel("RAR lift (%)")
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 12)
    clean_axes(ax)
    panel_label(ax, "d")

    save_all(fig, "operational_evaluation_summary")
    plt.close(fig)


def main() -> None:
    ablation_sensitivity_summary()
    operational_evaluation_summary()


if __name__ == "__main__":
    main()
