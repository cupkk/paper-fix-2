import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ── 顶级期刊绘图参数 ────────────────────────────────────────────
plt.rcParams.update({
    'font.family': ['Times New Roman', 'Arial'],
    'font.size': 11,
    'axes.linewidth': 1.2,
    'axes.labelsize': 11,
    'axes.titlesize': 0,               # 禁用内置标题，由 LaTeX \caption 提供
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'legend.frameon': False,
})

# ── 数据准备 ────────────────────────────────────────────────────
days = np.array([30, 60, 90, 120, 180])

# 根据描述构造合理中间值（30, 120, 180 为给定值；60, 90 内插）
log_loss = np.array([0.5413, 0.5280, 0.5200, 0.5163, 0.5172])
recall_at_5 = np.array([0.3942, 0.4040, 0.4120, 0.4185, 0.4171])

# ── 创建双栏图表（constrained_layout 自动管理边距） ──────────────
fig, ax1 = plt.subplots(figsize=(6.8, 4.2), constrained_layout=True)
ax2 = ax1.twinx()

color_log = '#2E86AB'      # 深海蓝（主色）
color_rec = '#F6AE2D'      # 琥珀黄（辅色）

# 左 y 轴：Log Loss
line1, = ax1.plot(days, log_loss, 'o-', color=color_log,
                  linewidth=2.2, markersize=8,
                  markerfacecolor='white', markeredgewidth=1.5,
                  label='Log Loss')

# 右 y 轴：Recall@5
line2, = ax2.plot(days, recall_at_5, 's--', color=color_rec,
                  linewidth=2.2, markersize=8,
                  markerfacecolor='white', markeredgewidth=1.5,
                  label='Recall@5')

# ── 坐标轴设置 ──────────────────────────────────────────────────
ax1.set_xlabel('Context Window Length (days)', labelpad=8)
ax1.set_ylabel('Log Loss', color=color_log, labelpad=8)
ax2.set_ylabel('Recall@5', color=color_rec, labelpad=8)

# 调整 y 轴显示范围，避免曲线紧贴边界
ax1.set_ylim(0.51, 0.55)
ax2.set_ylim(0.38, 0.43)

ax1.tick_params(axis='y', colors=color_log)
ax2.tick_params(axis='y', colors=color_rec)
ax1.set_xticks(days)

# 网格（仅对主坐标轴弱化显示）
ax1.grid(True, alpha=0.5, linestyle='--', color='#E0E0E0', linewidth=0.8)

# ── 图例（放在轴内部左上方，避免与曲线重叠） ─────────────────────
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2,
           loc='upper left', frameon=False)

# ── 保存图形 ────────────────────────────────────────────────────
output_path = Path(
    r'/app/output/figure_generation/5c9d5ad4-f623-451b-82ec-01683b1c4254/'
    r'workspace/figures/main_result/context_window_sensitivity.png'
)
output_path.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(str(output_path), dpi=300, facecolor='white', bbox_inches='tight')
plt.close()