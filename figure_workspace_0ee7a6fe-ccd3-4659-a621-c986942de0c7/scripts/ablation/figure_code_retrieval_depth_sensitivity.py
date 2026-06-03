import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ========== 顶级期刊风格参数 ==========
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# ========== 创建图表 ==========
fig, ax = plt.subplots(figsize=(6.8, 4.0), constrained_layout=True)

# ========== 数据准备 ==========
K = [1, 3, 5, 7, 10]

# Log Loss（左轴）—— 先降后升，最优在 K=5
log_loss = [0.535, 0.525, 0.5163, 0.522, 0.528]

# Recall@5（右轴）—— 先升后降，最优在 K=5
recall = [0.34, 0.40, 0.4185, 0.405, 0.39]

color_loss = '#2E86AB'
color_recall = '#F6AE2D'

# ========== 左轴：Log Loss ==========
line1, = ax.plot(K, log_loss, 'o-',
                 color=color_loss,
                 linewidth=2.2,
                 markersize=7,
                 label='Log Loss')
ax.set_xlabel('Retrieval Depth K', labelpad=8)
ax.set_ylabel('Log Loss', color=color_loss, labelpad=8)
ax.tick_params(axis='y', labelcolor=color_loss)

# ========== 右轴：Recall@5 ==========
ax_twin = ax.twinx()
line2, = ax_twin.plot(K, recall, 's--',
                      color=color_recall,
                      linewidth=2.2,
                      markersize=7,
                      label='Recall@5')
ax_twin.set_ylabel('Recall@5', color=color_recall, labelpad=8)
ax_twin.tick_params(axis='y', labelcolor=color_recall)

# ========== 坐标轴美化 ==========
ax.spines['top'].set_visible(False)
ax_twin.spines['top'].set_visible(False)
ax.grid(True, axis='y', alpha=0.5, linestyle='--', color='#E0E0E0', linewidth=0.8)

# ========== 图例（放在坐标轴上方，避免与曲线重叠） ==========
ax.legend(handles=[line1, line2],
          loc='upper center',
          bbox_to_anchor=(0.5, 1.08),
          ncol=2,
          frameon=False)

# ========== 保存图片 ==========
out_path = Path(
    r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/'
    r'workspace/figures/ablation/retrieval_depth_sensitivity.png'
)
out_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(str(out_path), dpi=300, facecolor='white', bbox_inches='tight')
plt.close()