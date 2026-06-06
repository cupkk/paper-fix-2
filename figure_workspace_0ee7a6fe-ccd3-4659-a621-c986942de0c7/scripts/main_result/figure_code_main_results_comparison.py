import matplotlib

matplotlib.use("Agg")

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


MODELS = [
    "RF",
    "RF+KB",
    "XGBoost",
    "LSTM",
    "Transformer",
    "FRAA (-Dyn)",
    "FRAA (-TE)",
    "FRAA (-KB)",
    "FRAA",
]

LOG_LOSS = np.array([0.6421, 0.6289, 0.6104, 0.5873, 0.5698, 0.5642, 0.5510, 0.5385, 0.5163])
RECALL_AT_5 = np.array([0.3172, 0.3291, 0.3495, 0.3738, 0.3846, 0.3891, 0.3957, 0.4023, 0.4185])


def configure_style() -> None:
    plt.rcParams.update(
        {
            "font.family": ["Times New Roman", "Arial", "DejaVu Sans"],
            "font.size": 10,
            "axes.labelsize": 10,
            "axes.titlesize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 9,
            "axes.linewidth": 1.0,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "savefig.edgecolor": "white",
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def annotate_bars(ax: plt.Axes, bars, values, fmt: str) -> None:
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            fmt.format(value),
            ha="center",
            va="bottom",
            fontsize=8,
            fontweight="normal",
            rotation=90,
            clip_on=False,
        )


def main() -> None:
    configure_style()

    x = np.arange(len(MODELS))
    colors = ["#D0D3D6"] * len(MODELS)
    colors[-1] = "#0F4D92"
    edge_color = "black"

    fig, axes = plt.subplots(1, 2, figsize=(4.95, 2.72), constrained_layout=True)

    loss_bars = axes[0].bar(x, LOG_LOSS, color=colors, edgecolor=edge_color, linewidth=0.7)
    axes[0].set_ylabel("Log Loss")
    axes[0].set_ylim(0.49, 0.665)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(MODELS, rotation=38, ha="right")
    axes[0].grid(axis="y", color="#E5E5E5", linestyle="--", linewidth=0.55)
    axes[0].set_axisbelow(True)
    annotate_bars(axes[0], loss_bars, LOG_LOSS, "{:.3f}")

    recall_bars = axes[1].bar(x, RECALL_AT_5, color=colors, edgecolor=edge_color, linewidth=0.7)
    axes[1].set_ylabel("Recall@5")
    axes[1].set_ylim(0.30, 0.435)
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(MODELS, rotation=38, ha="right")
    axes[1].grid(axis="y", color="#E5E5E5", linestyle="--", linewidth=0.55)
    axes[1].set_axisbelow(True)
    annotate_bars(axes[1], recall_bars, RECALL_AT_5, "{:.3f}")

    for ax in axes:
        ax.tick_params(axis="both", width=1.0, length=3)
        ax.spines["left"].set_color("black")
        ax.spines["bottom"].set_color("black")

    workspace = Path(__file__).resolve().parents[2]
    output_dir = workspace / "figures" / "main_result"
    output_dir.mkdir(parents=True, exist_ok=True)

    for suffix in ("png", "pdf", "svg"):
        output_path = output_dir / f"main_results_comparison.{suffix}"
        fig.savefig(output_path, dpi=600 if suffix == "png" else None, bbox_inches="tight")

    plt.close(fig)


if __name__ == "__main__":
    main()
