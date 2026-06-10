from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]

BLUE_DARK = "#0F4D92"
BLUE = "#3775BA"
BLUE_LIGHT = "#9EC3E6"
TEAL = "#42949E"
GREEN = "#59A14F"
GREEN_LIGHT = "#AADCA9"
ORANGE = "#E69F00"
RED = "#B64342"
GRAY = "#C8C8C8"
GRAY_DARK = "#4D4D4D"

METHOD_COLORS = {
    "RF": "#BFC3C7",
    "RF + KB": "#AEB6BE",
    "XGBoost": "#9EA7B1",
    "LSTM": TEAL,
    "Transformer": ORANGE,
    "FRAA ablated": BLUE_LIGHT,
    "FRAA": BLUE_DARK,
}


def apply_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": 9.5,
            "axes.labelsize": 10.0,
            "xtick.labelsize": 8.8,
            "ytick.labelsize": 8.8,
            "legend.fontsize": 8.4,
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


def clean_axes(ax: plt.Axes, axis: str = "x") -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(width=0.8, length=3)
    ax.grid(axis=axis, color="#E6E6E6", linestyle="--", linewidth=0.5, alpha=0.8)
    ax.set_axisbelow(True)


def panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.10,
        1.16,
        label,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10.8,
        fontweight="bold",
    )


def save_all(fig: plt.Figure, path_no_ext: Path) -> None:
    path_no_ext.parent.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "svg", "png"):
        dpi = 600 if ext == "png" else None
        fig.savefig(path_no_ext.with_suffix(f".{ext}"), dpi=dpi, bbox_inches="tight", pad_inches=0.045)


def method_color(name: str) -> str:
    if name == "FRAA (full)" or name == "FRAA":
        return METHOD_COLORS["FRAA"]
    if name.startswith("FRAA"):
        return METHOD_COLORS["FRAA ablated"]
    if name == "Transformer":
        return METHOD_COLORS["Transformer"]
    if name == "LSTM":
        return METHOD_COLORS["LSTM"]
    if name == "XGBoost":
        return METHOD_COLORS["XGBoost"]
    if name == "RF + KB features" or name == "RF+KB":
        return METHOD_COLORS["RF + KB"]
    return METHOD_COLORS["RF"]


def main_results() -> None:
    """Draw Fig. 2 from the manuscript main-results table."""
    apply_style()
    models = [
        "RF (deployed)",
        "RF + KB features",
        "XGBoost",
        "LSTM",
        "Transformer",
        "FRAA (-Dyn)",
        "FRAA (-TE)",
        "FRAA (-KB)",
        "FRAA (full)",
    ]
    log_loss = np.array([0.6421, 0.6289, 0.6104, 0.5873, 0.5698, 0.5642, 0.5510, 0.5385, 0.5163])
    recall5 = np.array([0.3172, 0.3291, 0.3495, 0.3738, 0.3846, 0.3891, 0.3957, 0.4023, 0.4185])

    colors = [method_color(m) for m in models]
    y = np.arange(len(models))

    fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.25), sharey=True, constrained_layout=True)

    ax = axes[0]
    ax.barh(y, log_loss, color=colors, edgecolor="white", linewidth=0.5)
    ax.set_yticks(y)
    ax.set_yticklabels(models)
    ax.invert_yaxis()
    ax.set_xlabel("Log Loss (lower is better)")
    ax.set_xlim(0.49, 0.66)
    for yi, value in zip(y, log_loss):
        ax.text(value + 0.003, yi, f"{value:.4f}", va="center", fontsize=7.7)
    clean_axes(ax)
    panel_label(ax, "a")

    ax = axes[1]
    ax.barh(y, recall5, color=colors, edgecolor="white", linewidth=0.5)
    ax.set_xlabel("Recall@5 (higher is better)")
    ax.set_xlim(0.30, 0.435)
    for yi, value in zip(y, recall5):
        ax.text(value + 0.002, yi, f"{value:.4f}", va="center", fontsize=7.7)
    clean_axes(ax)
    panel_label(ax, "b")

    save_all(fig, ROOT / "figures" / "main_result" / "main_results_comparison")
    plt.close(fig)


def retrieval_evidence() -> None:
    """Draw Fig. 3 from the feature-family occlusion and retrieval-depth tables."""
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.55), constrained_layout=True)

    ax = axes[0]
    groups = ["Knowledge-\nretrieved", "Transaction\n dynamics", "Macro\n indicators", "Quasi-static\n profile"]
    auc_drop = np.array([3.92, 2.87, 1.55, 0.93])
    y = np.arange(len(groups))
    ax.barh(y, auc_drop, color=[BLUE_DARK, BLUE, TEAL, GRAY], edgecolor="white", linewidth=0.5)
    ax.set_yticks(y)
    ax.set_yticklabels(groups)
    ax.invert_yaxis()
    ax.set_xlabel("AUC drop (%)")
    ax.set_xlim(0, 4.35)
    for yi, value in zip(y, auc_drop):
        ax.text(value + 0.07, yi, f"{value:.2f}", va="center", fontsize=8.0)
    clean_axes(ax)
    panel_label(ax, "a")

    ax = axes[1]
    k = np.array([1, 3, 5, 7, 10])
    log_loss = np.array([0.5287, 0.5214, 0.5163, 0.5175, 0.5189])
    recall5 = np.array([0.4068, 0.4117, 0.4185, 0.4173, 0.4160])

    ax.plot(k, log_loss, marker="o", markersize=3.5, linewidth=1.25, color=BLUE_DARK, label="Log Loss")
    ax.set_xlabel("Retrieved documents K")
    ax.set_ylabel("Log Loss", color=BLUE_DARK)
    ax.tick_params(axis="y", colors=BLUE_DARK)
    ax.set_xticks(k)
    ax.set_ylim(0.514, 0.531)
    ax.axvline(5, color=GREEN, linestyle="--", linewidth=0.9)
    ax.text(5.25, 0.5302, "selected", color=GREEN, fontsize=8.0, va="top")
    clean_axes(ax, axis="y")

    ax2 = ax.twinx()
    ax2.plot(k, recall5, marker="s", markersize=3.3, linewidth=1.25, color=ORANGE, label="Recall@5")
    ax2.set_ylabel("Recall@5", color=ORANGE)
    ax2.tick_params(axis="y", colors=ORANGE)
    ax2.set_ylim(0.404, 0.421)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(ORANGE)
    lines = ax.get_lines()[:1] + ax2.get_lines()
    ax.legend(lines, [line.get_label() for line in lines], loc="lower right", handlelength=1.6)
    panel_label(ax, "b")

    save_all(fig, ROOT / "figures" / "ablation" / "retrieval_depth_sensitivity")
    plt.close(fig)


def explanation_quality() -> None:
    """Draw Fig. 4 from the explanation-quality table."""
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.35), constrained_layout=True)

    methods = ["Template", "FRAA"]
    expert_metrics = ["Faithfulness", "Readability"]
    expert_values = np.array([[3.89, 4.02], [4.32, 4.51]])
    rouge = np.array([0.3026, 0.4131])

    x = np.arange(len(expert_metrics))
    width = 0.34
    ax = axes[0]
    ax.bar(x - width / 2, expert_values[0], width, color=GRAY, label=methods[0], edgecolor="white", linewidth=0.5)
    ax.bar(x + width / 2, expert_values[1], width, color=BLUE_DARK, label=methods[1], edgecolor="white", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(expert_metrics)
    ax.set_ylabel("Expert score (1-5)")
    ax.set_ylim(3.5, 4.75)
    for xpos, value in zip(x - width / 2, expert_values[0]):
        ax.text(xpos, value + 0.035, f"{value:.2f}", ha="center", va="bottom", fontsize=7.8)
    for xpos, value in zip(x + width / 2, expert_values[1]):
        ax.text(xpos, value + 0.035, f"{value:.2f}", ha="center", va="bottom", fontsize=7.8)
    ax.legend(loc="upper left")
    clean_axes(ax, axis="y")
    panel_label(ax, "a")

    ax = axes[1]
    bars = ax.bar(np.arange(2), rouge, color=[GRAY, BLUE_DARK], edgecolor="white", linewidth=0.5)
    ax.set_xticks(np.arange(2))
    ax.set_xticklabels(methods)
    ax.set_ylabel("ROUGE-L")
    ax.set_ylim(0.25, 0.45)
    for bar, value in zip(bars, rouge):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.008, f"{value:.4f}", ha="center", va="bottom", fontsize=7.8)
    clean_axes(ax, axis="y")
    panel_label(ax, "b")

    save_all(fig, ROOT / "figures" / "main_result" / "explanation_quality_evaluation")
    plt.close(fig)


def latency_throughput() -> None:
    """Draw Fig. 5 from the latency-throughput table."""
    apply_style()
    models = ["RF+KB", "XGBoost", "LSTM", "Transformer", "FRAA"]
    latency = np.array([1.9, 2.1, 8.3, 12.4, 15.7])
    throughput = np.array([12530, 11200, 5910, 4320, 4070])
    colors = [method_color(m) for m in models]

    fig, ax = plt.subplots(1, 1, figsize=(5.1, 2.75), constrained_layout=True)
    ax.scatter(latency, throughput, s=44, color=colors, edgecolor="white", linewidth=0.7, zorder=3)
    offsets = {
        "RF+KB": (0.35, 330),
        "XGBoost": (0.35, -520),
        "LSTM": (0.35, 330),
        "Transformer": (0.35, 330),
        "FRAA": (-2.15, -520),
    }
    for xi, yi, label in zip(latency, throughput, models):
        dx, dy = offsets[label]
        ax.text(xi + dx, yi + dy, label, fontsize=8.2)
    ax.set_xlabel("Latency (ms/query)")
    ax.set_ylabel("Throughput (queries/s)")
    ax.set_xlim(0, 18)
    ax.set_ylim(3000, 13500)
    clean_axes(ax, axis="both")

    save_all(fig, ROOT / "figures" / "main_result" / "inference_latency_throughput")
    plt.close(fig)


def main() -> None:
    main_results()
    retrieval_evidence()
    explanation_quality()
    latency_throughput()


if __name__ == "__main__":
    main()
