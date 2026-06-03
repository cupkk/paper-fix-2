import matplotlib.pyplot as plt
from pathlib import Path

# ---------- 全局样式 ----------
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,               # 禁止标题（LaTeX 统一管理）
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# ---------- 数据 ----------
groups = [
    'Knowledge-retrieved context',
    'Transaction dynamics',
    'Macroeconomic indicators',
    'Quasi-static profile'
]
drops = [-3.92, -2.87, -1.55, -0.93]   # AUC 下降百分比
# 从深到浅的颜色，突出重要性顺序
colors = ['#1B4F72', '#2E86AB', '#6BB3D9', '#AED8E6']

# ---------- 画图 ----------
fig, ax = plt.subplots(figsize=(7.0, 4.0), constrained_layout=True)
fig.patch.set_facecolor('white')

y_pos = range(len(groups))
bars = ax.barh(y_pos, drops, height=0.65, color=colors,
               edgecolor='white', linewidth=0.8)

# 最重要的特征放在最上面
ax.invert_yaxis()
ax.set_yticks(y_pos)
ax.set_yticklabels(groups, fontsize=11)

# 基准线
ax.axvline(x=0, color='black', linewidth=0.8, linestyle='-')

# 坐标轴范围（留出左侧数值标签空间）
ax.set_xlabel('AUC Drop (%)', labelpad=8)
ax.set_xlim(-5.2, 0.3)

# 条形两端不紧贴边框
ax.set_ylim(-0.6, 3.6)

# 去除多余的边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 浅灰色纵向网格
ax.grid(axis='x', linestyle='--', color='#E0E0E0', alpha=0.5, linewidth=0.8)

# 在条形末端添加数值标签（向左偏移，字体不小于8pt，不加粗）
for i, val in enumerate(drops):
    ax.text(val - 0.15, i, f'{val:.2f}%',
            va='center', ha='right', fontsize=9)

# ---------- 保存 ----------
output_png = (r'/app/output/figure_generation/'
              r'5c9d5ad4-f623-451b-82ec-01683b1c4254/'
              r'workspace/figures/main_result/feature_importance_occlusion.png')
Path(output_png).parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_png, dpi=300, facecolor='white', bbox_inches='tight')
plt.close()