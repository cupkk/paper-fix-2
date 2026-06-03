import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ---------- 全球风格：顶级期刊 ----------
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,               # 禁止标题
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# ---------- 创建画布 ----------
fig, ax1 = plt.subplots(figsize=(6.8, 4.0), constrained_layout=True)

# ---------- 数据 ----------
epochs = np.array([5, 10, 20, 30, 38, 45])
log_loss = np.array([0.5832, 0.550, 0.530, 0.519, 0.5163, 0.5170])
recall5 = np.array([0.3938, 0.405, 0.412, 0.417, 0.4185, 0.4178])

# ---------- 左轴：Validation Log Loss ----------
color_loss = '#2E86AB'
line1, = ax1.plot(
    epochs, log_loss,
    'o-',
    color=color_loss,
    linewidth=3.0,
    markersize=8,
    markerfacecolor='white',
    markeredgewidth=1.5,
    label='Validation Log Loss'
)
ax1.set_xlabel('Epoch', labelpad=8)
ax1.set_ylabel('Validation Log Loss', color=color_loss, labelpad=8)
ax1.tick_params(axis='y', labelcolor=color_loss)
ax1.spines['top'].set_visible(False)       # 左轴隐藏 top spine
# 右 spine 暂时不可见（将留给右轴管理）
ax1.set_ylim(0.505, 0.595)
ax1.set_xlim(3, 47)
ax1.set_xticks(epochs)

# 浅灰网格（仅左轴）
ax1.grid(True, alpha=0.5, linestyle='--', color='#E0E0E0', linewidth=0.8)

# ---------- 右轴：Validation Recall@5 ----------
ax2 = ax1.twinx()
color_recall = '#E15554'
line2, = ax2.plot(
    epochs, recall5,
    's--',
    color=color_recall,
    linewidth=2.5,
    markersize=8,
    markerfacecolor='white',
    markeredgewidth=1.5,
    label='Validation Recall@5'
)
ax2.set_ylabel('Validation Recall@5', color=color_recall, labelpad=8)
ax2.tick_params(axis='y', labelcolor=color_recall)
# 右轴只显示 right spine，并隐藏 top spine
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(True)
ax2.spines['right'].set_color(color_recall)
ax2.spines['right'].set_linewidth(1.5)
ax2.set_ylim(0.380, 0.430)

# ---------- 图例（置于内部空白右上角，不与任何曲线重叠）----------
# 检查数据范围：log_loss 最大值 0.5832，离上边界 0.595 有距离；
# recall@5 最大值 0.4185，在右轴上边界 0.430 附近，但图例放在左轴坐标系中，
# 左轴右上角对应的是 log_loss ≈0.585 的区域，该处有 epoch 5 的 marker (0.5832) 但位置偏左，
# 图例可安全放置在 (0.99, 0.95) 位置。
ax1.legend(
    handles=[line1, line2],
    loc='upper right',
    bbox_to_anchor=(0.99, 0.95),
    frameon=True,
    framealpha=0.95,
    edgecolor='#CCCCCC',
    fontsize=10
)

# ---------- 保存 ----------
save_path = Path(
    r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/'
    r'workspace/figures/main_result/training_dynamics.png'
)
save_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(str(save_path), dpi=300, facecolor='white', bbox_inches='tight')
plt.close()