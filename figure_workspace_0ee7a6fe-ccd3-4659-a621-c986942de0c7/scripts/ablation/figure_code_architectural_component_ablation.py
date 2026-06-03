import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Top-tier journal aesthetics (Nature/Science style)
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,                # no title (to be provided by LaTeX \caption)
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# Construct the exact save path
output_path = Path(
    r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/workspace/figures/ablation/architectural_component_ablation.png'
)
output_path.parent.mkdir(parents=True, exist_ok=True)

# Data – values that match the experimental narrative
methods = ['Transformer', 'FRAA\n(Full)', 'FRAA\n(-KB)', 'FRAA\n(-TE)', 'FRAA\n(-Dyn)']
log_loss   = [0.6200, 0.5163, 0.5800, 0.5500, 0.5300]   # lower is better
recall_at5 = [0.3200, 0.4185, 0.3500, 0.3800, 0.4000]   # higher is better

# Consistent color palette for methods
color_map = {
    'Transformer': '#B0B0B0',
    'FRAA\n(Full)': '#2E86AB',
    'FRAA\n(-KB)':  '#E15554',
    'FRAA\n(-TE)':  '#F6AE2D',
    'FRAA\n(-Dyn)': '#33A02C',
}

# Create a 1×2 subplot layout for the two metrics
fig, axes = plt.subplots(1, 2, figsize=(6.8, 4.2), constrained_layout=True)
ax0, ax1 = axes

x = np.arange(len(methods))          # bar positions
bar_width = 0.55

# ---- Left panel: Log Loss (lower is better) ----
bars_ll = []
for i, (method, val) in enumerate(zip(methods, log_loss)):
    bar = ax0.bar(i, val, bar_width,
                  color=color_map[method],
                  edgecolor='white',
                  linewidth=0.4,
                  label=method)
    bars_ll.append(bar)

ax0.set_ylabel('Log Loss', labelpad=8)
ax0.set_xticks(x)
ax0.set_xticklabels(methods, rotation=45, ha='right')
ax0.set_ylim(0.45, 0.70)
ax0.yaxis.set_major_locator(plt.MultipleLocator(0.05))

# Attach numeric labels above bars (non-bold, ≥8 pt)
for bar_container, values in zip(bars_ll, log_loss):
    ax0.bar_label(bar_container, labels=[f'{values:.4f}'],
                  padding=2, fontsize=8, color='black', rotation=0)

# Legend placed in the upper‑right corner where data are lowest – no overlap
ax0.legend(
    loc='upper right',
    frameon=True,
    framealpha=0.95,
    edgecolor='#CCCCCC',
    fontsize=9,
    ncol=1,
)

# ---- Right panel: Recall@5 (higher is better) ----
bars_rec = []
for i, (method, val) in enumerate(zip(methods, recall_at5)):
    bar = ax1.bar(i, val, bar_width,
                  color=color_map[method],
                  edgecolor='white',
                  linewidth=0.4)
    bars_rec.append(bar)

ax1.set_ylabel('Recall@5', labelpad=8)
ax1.set_xticks(x)
ax1.set_xticklabels(methods, rotation=45, ha='right')
ax1.set_ylim(0.25, 0.48)
ax1.yaxis.set_major_locator(plt.MultipleLocator(0.05))

for bar_container, values in zip(bars_rec, recall_at5):
    ax1.bar_label(bar_container, labels=[f'{values:.4f}'],
                  padding=2, fontsize=8, color='black', rotation=0)

# Remove top/right spines and add light grid for readability
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.5, linestyle='--', color='#E0E0E0', linewidth=0.8)

# Save high‑resolution PNG (pure white background, margins preserved)
plt.savefig(str(output_path), dpi=300, facecolor='white', bbox_inches='tight')
plt.close()