import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ── 论文风格全局参数 ────────────────────────────────────
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

# ── 数据 ────────────────────────────────────────────────
groups = [
    'Knowledge‑retrieved\ncontext',
    'Transaction\ndynamics',
    'Macroeconomic\nindicators',
    'Quasi‑static\nprofile',
]
auc_drops = [3.92, 2.87, 1.55, 0.93]
colors = ['#2E86AB', '#6BB5C5', '#A8D8EA', '#CEE7F0']  # 递减饱和度突出重要性

# ── 创建画布 ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(3.4, 2.8), constrained_layout=True)

# 水平条形图
y_pos = range(len(groups))
bars = ax.barh(y_pos, auc_drops, height=0.55, color=colors, edgecolor='white', linewidth=0.8)

# ── 数值标注 ─────────────────────────────────────────────
for i, (val, bar) in enumerate(zip(auc_drops, bars)):
    ax.text(
        val + 0.12, bar.get_y() + bar.get_height() / 2,
        f'{val:.2f}%',
        va='center', ha='left',
        fontsize=10, color='#333333'
    )

# ── 坐标轴设置 ─────────────────────────────────────────
ax.set_yticks(y_pos)
ax.set_yticklabels(groups)
ax.invert_yaxis()                     # 最重要的在顶部
ax.set_xlabel('AUC drop (%)', labelpad=8)

# 去除顶部和右侧边框（已在 rcParams 中设置）
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# x 轴范围留出标签空间
ax.set_xlim(0, max(auc_drops) * 1.25)

# 浅色横向参考线（垂直网格）
ax.xaxis.grid(True, alpha=0.4, linestyle='--', color='#D0D0D0', linewidth=0.6)
ax.set_axisbelow(True)

# ── 保存 ───────────────────────────────────────────────
output_path = Path(
    '/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/workspace/figures/ablation/feature_group_importance.png'
)
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
plt.close()