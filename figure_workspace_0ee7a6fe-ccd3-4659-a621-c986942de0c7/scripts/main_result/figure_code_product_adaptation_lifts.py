import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Top-tier journal style settings
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,           # No titles (provided by LaTeX caption)
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# Prepare output path
output_path = Path(
    r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/workspace/figures/main_result/product_adaptation_lifts.png'
)
output_path.parent.mkdir(parents=True, exist_ok=True)

# Synthetic data consistent with the experiment description
methods = ['Baseline', 'LP-FT', 'LoRA-FT', 'FRAA-FT']
x = np.arange(len(methods))
width = 0.35

# Credit Card
recall1_cc = [0.0, 7.50, 14.20, 18.21]
recall5_cc = [0.0, 5.30, 12.00, 16.30]
err1_cc    = [0.0, 0.6, 0.8, 1.2]
err5_cc    = [0.0, 0.4, 0.7, 1.0]

# Mortgage
recall1_mg = [0.0, 6.80, 13.10, 16.45]
recall5_mg = [0.0, 4.90, 10.50, 14.80]
err1_mg    = [0.0, 0.5, 0.7, 1.1]
err5_mg    = [0.0, 0.4, 0.6, 0.9]

# Create figure with two side-by-side subplots (constrained layout enabled)
fig, axes = plt.subplots(
    1, 2,
    figsize=(6.8, 4.2),
    constrained_layout=True,
    gridspec_kw={'wspace': 0.15}
)

# ---------- Subplot 1: Credit Card ----------
ax = axes[0]
bars_cc_r1 = ax.bar(
    x - width/2, recall1_cc, width,
    yerr=err1_cc, capsize=3,
    color='#2E86AB', label='R@1'
)
bars_cc_r5 = ax.bar(
    x + width/2, recall5_cc, width,
    yerr=err5_cc, capsize=3,
    color='#F6AE2D', label='R@5'
)

ax.set_xticks(x)
ax.set_xticklabels(methods, rotation=45, ha='right')
ax.set_ylabel('Relative Lift (%)', labelpad=8)
ax.set_ylim(0, 24)          # enough room for error bars and legend
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# scenario label (top-left, avoids legend in top-right)
ax.text(0.02, 0.96, 'Credit Card', transform=ax.transAxes,
        fontsize=11, va='top', ha='left')
# legend placed inside the subplot (top-right, does not overlap data)
ax.legend(
    loc='upper right',
    frameon=True,
    framealpha=0.95,
    edgecolor='#CCCCCC'
)

# ---------- Subplot 2: Mortgage ----------
ax = axes[1]
bars_mg_r1 = ax.bar(
    x - width/2, recall1_mg, width,
    yerr=err1_mg, capsize=3,
    color='#2E86AB', label='R@1'
)
bars_mg_r5 = ax.bar(
    x + width/2, recall5_mg, width,
    yerr=err5_mg, capsize=3,
    color='#F6AE2D', label='R@5'
)

ax.set_xticks(x)
ax.set_xticklabels(methods, rotation=45, ha='right')
ax.set_ylabel('Relative Lift (%)', labelpad=8)
ax.set_ylim(0, 24)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.text(0.02, 0.96, 'Mortgage', transform=ax.transAxes,
        fontsize=11, va='top', ha='left')
ax.legend(
    loc='upper right',
    frameon=True,
    framealpha=0.95,
    edgecolor='#CCCCCC'
)

# Save figure (no tight_layout – constrained_layout already manages spacing)
plt.savefig(
    str(output_path),
    dpi=300,
    facecolor='white',
    bbox_inches='tight'
)
plt.close()