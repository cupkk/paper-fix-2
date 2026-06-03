import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Nature/Science 风格的全局绘图参数
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,          # 禁止使用标题
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# 双栏图宽度，适当增加高度以避免图例被裁切
fig, ax = plt.subplots(figsize=(6.8, 4.5), constrained_layout=True)

# 指标数据
metrics = ['Faithfulness', 'Readability', 'ROUGE-L F1']
template_scores = [3.89, 4.02, 0.3026]
fraa_scores     = [4.32, 4.51, 0.4131]

# 颜色定义
color_template = '#2E86AB'   # 深海蓝
color_fraa     = '#F6AE2D'   # 琥珀黄

# 分组柱状图位置
x = np.arange(len(metrics))
bar_width = 0.35
offset = bar_width / 2

# 创建右侧 y 轴（仅用于 ROUGE-L）
ax2 = ax.twinx()

# ---------- 在左轴绘制前两个指标 (1-5 量表) ----------
for i in range(2):
    ax.bar(x[i] - offset, template_scores[i], bar_width,
           color=color_template, edgecolor='white', linewidth=0.5)
    ax.bar(x[i] + offset, fraa_scores[i], bar_width,
           color=color_fraa, edgecolor='white', linewidth=0.5)

# ---------- 在右轴绘制 ROUGE-L ----------
ax2.bar(x[2] - offset, template_scores[2], bar_width,
        color=color_template, edgecolor='white', linewidth=0.5)
ax2.bar(x[2] + offset, fraa_scores[2], bar_width,
        color=color_fraa, edgecolor='white', linewidth=0.5)

# ---------- 左轴设置 ----------
ax.set_ylim(0, 5.5)
ax.set_ylabel('Score (1-5)', labelpad=8)
ax.set_yticks(np.arange(0, 6, 1))

# ---------- 右轴设置 ----------
ax2.set_ylim(0, 0.6)
ax2.set_ylabel('ROUGE-L F1 Score', labelpad=8)
ax2.set_yticks(np.arange(0, 0.65, 0.1))

# 保留右侧脊柱以显示第二套刻度
ax2.spines['right'].set_visible(True)
ax2.spines['top'].set_visible(False)

# ---------- X 轴 ----------
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=11)
ax.set_xlabel('')

# 水平网格线（仅左轴，辅助读数）
ax.grid(axis='y', alpha=0.5, linestyle='--', color='#E0E0E0', linewidth=0.8)

# ---------- 数值标签（小号、非加粗） ----------
# 左轴标签偏移
left_offset = 0.15
# 右轴标签偏移（量纲不同，用绝对值偏移）
right_offset = 0.02

for i in range(2):
    ax.text(x[i] - offset, template_scores[i] + left_offset,
            f'{template_scores[i]:.2f}', ha='center', va='bottom', fontsize=9)
    ax.text(x[i] + offset, fraa_scores[i] + left_offset,
            f'{fraa_scores[i]:.2f}', ha='center', va='bottom', fontsize=9)

ax2.text(x[2] - offset, template_scores[2] + right_offset,
         f'{template_scores[2]:.4f}', ha='center', va='bottom', fontsize=9)
ax2.text(x[2] + offset, fraa_scores[2] + right_offset,
         f'{fraa_scores[2]:.4f}', ha='center', va='bottom', fontsize=9)

# ---------- 图例（放置在主绘图区域上方，且确保不超界） ----------
legend_handles = [
    mpatches.Patch(color=color_template, label='Template'),
    mpatches.Patch(color=color_fraa, label='FRAA')
]
# bbox_to_anchor=(0.5, 1.09) 使图例位于坐标轴上方但仍在 constrained_layout 自动推算的边距内
ax.legend(handles=legend_handles,
          loc='upper center',
          bbox_to_anchor=(0.5, 1.09),
          ncol=2,
          frameon=False)

# ---------- 保存图像（纯白背景，高分辨率） ----------
output_path = Path(r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/workspace/figures/main_result/explanation_quality_evaluation.png')
output_path.parent.mkdir(parents=True, exist_ok=True)

# 仅使用 constrained_layout，不再调用 tight_layout 以避免冲突
plt.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
plt.close()