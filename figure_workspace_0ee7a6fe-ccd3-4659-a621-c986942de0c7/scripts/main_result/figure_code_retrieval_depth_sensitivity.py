import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ========== 顶级期刊绘图风格 (Nature/Science) ==========
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,               # 禁用图表标题（由 LaTeX caption 提供）
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
    'lines.linewidth': 2.2,
    'lines.markersize': 7,
    'grid.alpha': 0.5,
    'grid.linestyle': '--',
    'grid.color': '#E0E0E0',
    'grid.linewidth': 0.8,
})

# ========== 数据准备（模拟消融研究结果） ==========
K = [1, 3, 5, 7, 9]

# Log Loss: 在 K=5 时最低，两端升高
log_loss = np.array([0.45, 0.38, 0.35, 0.37, 0.40])
log_loss_std = np.array([0.03, 0.02, 0.015, 0.02, 0.025])

# Recall@5: 在 K=5 时最高，两端降低
recall5 = np.array([0.62, 0.72, 0.78, 0.75, 0.71])
recall5_std = np.array([0.03, 0.025, 0.02, 0.025, 0.03])

# ========== 创建画布与轴 ==========
fig, ax1 = plt.subplots(figsize=(6.8, 4.4), constrained_layout=True)

# 左侧 y 轴：Log Loss
ax1.set_xlabel('Number of Retrieved Documents (K)', labelpad=8)
ax1.set_ylabel('Log Loss', color='#2E86AB', labelpad=8)
ax1.tick_params(axis='y', labelcolor='#2E86AB')
ax1.set_ylim(0.30, 0.52)               # 留出右上方图例空间

# 右侧 y 轴：Recall@5
ax2 = ax1.twinx()
ax2.set_ylabel('Recall@5', color='#F6AE2D', labelpad=8)
ax2.tick_params(axis='y', labelcolor='#F6AE2D')
ax2.set_ylim(0.55, 0.90)               # 留出右上方图例空间

# ========== 绘制折线 + 误差棒 ==========
line1 = ax1.errorbar(
    K, log_loss, yerr=log_loss_std,
    fmt='o-', color='#2E86AB', linewidth=2.2, markersize=7,
    capsize=3, elinewidth=1.2, markeredgecolor='#2E86AB', markerfacecolor='white',
    label='Log Loss'
)

line2 = ax2.errorbar(
    K, recall5, yerr=recall5_std,
    fmt='s--', color='#F6AE2D', linewidth=2.2, markersize=7,
    capsize=3, elinewidth=1.2, markeredgecolor='#F6AE2D', markerfacecolor='white',
    label='Recall@5'
)

# ========== 坐标轴风格化 ==========
ax1.set_xticks(K)
ax1.set_xlim(0.5, 9.5)

# 去除左侧轴的顶部和右侧脊柱（右侧轴的脊柱保留作为第二个纵轴）
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)    # twinx 顶部脊柱隐藏

# 网格（仅作用于左轴，避免双轴网格重叠）
ax1.grid(True, alpha=0.5, linestyle='--', color='#E0E0E0', linewidth=0.8)

# ========== 图例：放在右上方内部，避免遮挡 ==========
# 合并两个轴的图例句柄，放置在 ax1 内部右上角，并微调位置
lines = [line1, line2]
labels = ['Log Loss', 'Recall@5']

ax1.legend(
    lines, labels,
    loc='upper right',
    bbox_to_anchor=(0.98, 0.98),       # 置于右上角轻微内缩
    ncol=1,
    frameon=True,
    framealpha=0.95,
    edgecolor='#CCCCCC',
)

# ========== 保存图片（严格遵循路径与参数要求） ==========
output_path = Path(r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/workspace/figures/main_result/retrieval_depth_sensitivity.png')
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output_path,
    dpi=300,
    facecolor='white',
    pad_inches=0.2,                    # 保留边距，不使用 bbox_inches='tight'
)
plt.close()