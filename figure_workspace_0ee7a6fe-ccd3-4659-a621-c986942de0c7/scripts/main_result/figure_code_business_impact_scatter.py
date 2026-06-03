import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ----------------------------------------------------------------------
# Top‑tier journal style – Nature / Science level
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,                # no figure title (LaTeX \caption)
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# ----------------------------------------------------------------------
# Data – numbers directly from the experiment snippet
models  = ['RF+KB\nFeatures', 'Transformer', 'FRAA\n(-KB)', 'FRAA full']
logloss = [-5.0, -10.0, -15.0, -19.57]       # % reduction (more negative = better)
rar     = [ 2.0,   5.0,   7.5,  10.45]        # estimated RAR lift (%)
cost    = [ 1.0,   1.8,   1.5,   1.6 ]        # relative computational cost

# Colours – Nature‑style palette (with a strong accent for the best method)
colors  = ['#F6AE2D', '#33A02C', '#E15554', '#2E86AB']

# ----------------------------------------------------------------------
# Figure template (double‑column width)
fig, ax = plt.subplots(figsize=(6.8, 4.0), constrained_layout=True)

# ----- Bubbles (scatter) with direct model labels ----------------
#  Each bubble's size encodes relative computational cost.
#  We use a small list of text offsets to prevent label overlap.
offsets = [(12, 10),   # RF+KB  -> right‑up
           (12,  3),   # Transf -> right
           (12, -1),   # FRAA(-KB) -> right
           (12, -5)]   # FRAA full -> right‑down (avoids collision)

for i, (x, y, s, c, (dx, dy)) in enumerate(zip(logloss, rar, cost,
                                                colors, offsets)):
    ax.scatter(x, y,
               s=s * 85,                 # bubble size
               c=c,
               edgecolors='white',
               linewidth=0.8,
               zorder=5)
    ax.annotate(models[i], (x, y),
                textcoords="offset points",
                xytext=(dx, dy),
                ha='left', va='center',
                fontsize=9, color='black')

# ----- Quadratic trend line – shows directional consistency ------
coeffs = np.polyfit(logloss, rar, 2)
poly   = np.poly1d(coeffs)
x_smooth = np.linspace(min(logloss) - 1.5, max(logloss) + 1.5, 120)
y_smooth = poly(x_smooth)
ax.plot(x_smooth, y_smooth, '--', color='#888888',
        linewidth=1.5, alpha=0.65, zorder=1)

# ----- Axes properties -------------------------------------------
ax.set_xlabel('Log Loss Reduction (%)', labelpad=8)
ax.set_ylabel('Estimated RAR Lift (%)', labelpad=8)

ax.grid(True, alpha=0.5, linestyle='--', color='#E0E0E0', linewidth=0.8)

# Axes limits with comfortable margins
x_margin = 2.2
y_margin = 2.0
ax.set_xlim(min(logloss) - x_margin, max(logloss) + x_margin)
ax.set_ylim(min(rar) - y_margin, max(rar) + y_margin)

# ----------------------------------------------------------------------
# Save – pure white background, high resolution, 15%+ margin kept
output_png = (r'/app/output/figure_generation/'
              r'5c9d5ad4-f623-451b-82ec-01683b1c4254/'
              r'workspace/figures/main_result/'
              r'business_impact_scatter.png')
Path(output_png).parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_png, dpi=300, facecolor='white', bbox_inches='tight')
plt.close()