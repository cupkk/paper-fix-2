# 研究进展日志 20260611：训练动态补充与标题间距排查

## 项目总体进展

当前目标是将 FRAA 的 PRICAI/LNCS 投稿稿整理到 16 页以内，同时尽量恢复精修前论文中有表格数据支撑的辅助实验。论文主线保持为：FRAA 通过时间感知行为编码、时间戳有效检索、交叉注意力融合和解释生成，提升金融风险评分的校准、排序和可审计性。当前稿件已经恢复了场景适应、离线回放效用、上下文窗口敏感性、增量特征组添加、延迟与吞吐量等结果，并删除了此前新增但用户不认可的 `Experimental configuration` 表。

## 今日更新

- 根据用户指出的缺口，核对了精修前 `original_tex.tex`、`FRAA_figure_workspace_中英对照版_20260609.md` 和人工精修参考稿。
- 确认缺失内容是“Training Dynamics and Convergence / Checkpoint Selection”部分，包含完整 FRAA 在选定 epoch 上的验证 Log Loss 与 Recall@5 表格。
- 将该内容补入当前主 TeX：`figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/submission_pricai2026.tex`。
- 新增位置放在 `Baselines and Training Details` 之后、`Evaluation Questions` 之前。原因是它解释模型选择和验证集检查点，而不是测试集主结果或后验业务分析。
- 新增表格标签为 `tab:training_dynamics`，数据保持精修前论文数值：
  - epoch 5: Log Loss 0.5832, Recall@5 0.3938
  - epoch 10: Log Loss 0.5564, Recall@5 0.4021
  - epoch 20: Log Loss 0.5271, Recall@5 0.4116
  - epoch 30: Log Loss 0.5205, Recall@5 0.4152
  - epoch 38: Log Loss 0.5163, Recall@5 0.4185
  - epoch 45: Log Loss 0.5170, Recall@5 0.4178
- 新增文字经过保守润色：说明 Log Loss 和 Recall@5 在 epoch 38 达到最佳，epoch 45 出现轻微过拟合，学习率在 25 到 30 epoch 的平台期后减半，并据此支持按验证 Log Loss 选择 epoch 38 检查点。
- 对用户截图中的标题前后大空白做了排查。当前判断是由 LNCS 页面底部对齐和强制浮动体造成的竖直间距拉伸，不是模板标题命令本身被修改。下一步需要通过 Overleaf 编译后的 PDF 再确认新增内容是否填充该页并消除异常空白。

## 本地静态检查结果

- BibTeX 条目数：40。
- 正文唯一引用键：40。
- 缺失引用：0。
- 未使用 BibTeX：0。
- 未解析 `\ref`：0。
- 重复 label：0。
- 当前图数：4。
- 当前表数：8。
- 单个 `\cite{}` 中最大引用数：2。
- 旧的错误/混合表标签 `tab:experimental_config`、`tab:transfer_utility`、`tab:sensitivity_efficiency` 均已不存在。

## 下一步

- 同步 Overleaf 包并在网页端重新编译。
- 下载新 PDF，检查页数是否仍不超过 16 页。
- 检查训练动态表是否位于对应正文附近。
- 检查 `Evaluation Questions`、`Main Results` 等标题附近是否仍有异常大空白。
- 再对照精修前论文和人工精修稿，列出剩余缺口与投稿风险。

## 排版修复补记

- PDF 目检发现主结果表和组件消融表使用普通浮动时，会被 LaTeX 移到下一页页首，导致解释句被图表打断。
- 已将 \begin{table} 调整为 \begin{table}[H]，仅针对 	ab:main_results 和 	ab:component_ablation 两张表。
- 目标是让图表靠近对应正文，避免破坏阅读逻辑；不修改 LNCS 标题样式命令。


## 标题间距修复补记

- 官方 llncs.cls 未要求重定义标题段前段后；截图中的大间距主要来自页面底部对齐造成的竖向胶水拉伸。
- 已在导言区加入 \raggedbottom，让页面自然结束，避免 LaTeX 为对齐页底拉大标题附近间距。
- 未使用 	itlesec，也未改 \subsection 或 \subsubsection 的模板样式。


## 最终验证结论

- Overleaf 已同步并重新编译最终版 PDF：overleaf_after_training_dynamics_spacing_ragged_final_output_full.pdf。
- 最终 PDF 为 16 页，满足当前 PRICAI/LNCS 长文页数上限。
- SHA256：6C9390F82D6D48D93B6415C00866D9B394908BA3B5D912EA88AB8640B9D45384。
- 新增训练动态表位于第 8 页，与 Training Dynamics and Checkpoint Selection 正文相邻。
- 用户截图中 Evaluation Questions 和 Main Results 附近的大块空白已消失；主结果表和组件消融表不再把解释句切开。
- 对照精修前稿件，已恢复核心辅助内容：场景适应、离线 RAR、上下文窗口、增量特征组、延迟/吞吐、训练动态。仍未恢复旧稿中的单独训练曲线图、业务散点图和场景适应图，原因是当前 16 页已满，并且表格足以承载对应数据；继续加图会显著增加超页和浮动风险。
- 剩余投稿风险：专有数据不可公开复现；部分离线效用/RAR 仍是离线估计，不应表述为线上因果收益；当前材料没有多随机种子/显著性检验日志。

