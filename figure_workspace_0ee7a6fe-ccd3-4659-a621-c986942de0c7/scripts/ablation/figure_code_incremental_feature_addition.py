import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ─── 顶级期刊绘图参数 ───
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,             # 禁用内部标题（由 LaTeX \caption 提供）
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# ─── 合成数据 ───
# 特征组逐步叠加：Knowledge only, +Transaction, +Macro, +Static profile (full)
x = np.array([0, 1, 2, 3])
group_labels = ['Knowledge\nonly', '+Transaction', '+Macro', '+Static\n(full)']
log_loss = np.array([0.450, 0.320, 0.302, 0.285])     # 单调下降
recall5  = np.array([0.550, 0.720, 0.755, 0.780])    # 单调上升

# ─── 创建画布（双栏尺寸，略加高度以容纳换行标签） ───
fig, ax1 = plt.subplots(figsize=(6.8, 4.5), constrained_layout=True)
ax2 = ax1.twinx()

# ─── 绘制 Log Loss（左轴） ───
line1 = ax1.plot(x, log_loss,
                 'o-',
                 linewidth=2.8,
                 markersize=8,
                 markerfacecolor='white',
                 markeredgewidth=1.8,
                 markeredgecolor='#2E86AB',
                 color='#2E86AB',
                 label='Log Loss')

# ─── 绘制 Recall@5（右轴） ───
line2 = ax2.plot(x, recall5,
                 's--',
                 linewidth=2.8,
                 markersize=8,
                 markerfacecolor='#F6AE2D',
                 markeredgewidth=1.5,
                 markeredgecolor='#F6AE2D',
                 color='#F6AE2D',
                 label='Recall@5')

# ─── 坐标轴设置 ───
ax1.set_xlabel('Cumulative Feature Groups', labelpad=8)
ax1.set_ylabel('Log Loss', color='#2E86AB', labelpad=8)
ax2.set_ylabel('Recall@5', color='#F6AE2D', labelpad=8)

# x 轴刻度及标签
ax1.set_xticks(x)
ax1.set_xticklabels(group_labels, rotation=45, ha='right')

# 轴刻度颜色与对应曲线一致
ax1.tick_params(axis='y', colors='#2E86AB')
ax2.tick_params(axis='y', colors='#F6AE2D')

# 留白范围：为数据点顶部和底部保留适当空间
ax1.set_ylim(0.25, 0.50)
ax2.set_ylim(0.48, 0.82)

# 轻微网格（仅左轴，避免双网格杂乱）
ax1.grid(True, alpha=0.4, linestyle='--', color='#E0E0E0', linewidth=0.6)

# ─── 图例：放置于左轴内部左下角空白区域 ───
handles = line1 + line2
labels = [h.get_label() for h in handles]
ax1.legend(handles, labels,
           loc='lower left',
           frameon=False,
           framealpha=0.95,
           edgecolor='#CCCCCC',
           fontsize=11)

# ─── 保存图片 ───
output_path = Path(
    r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/workspace/figures/ablation/incremental_feature_addition.png'
)
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(str(output_path), dpi=300, facecolor='white', pad_inches=0.2)
plt.close()