# 研究进展日志 20260623 贡献点对齐调整

## 总体研究进展

FRAA 论文处于 PRICAI 2026 投稿前最终排版同步阶段。本轮目标是根据用户提供的参考图，调整 Introduction 中贡献点的排版，使破折号位于左列，正文首行和续行按同一左边界对齐，避免首行看起来有额外缩进。

## 2026-06-23 更新

### 修改内容

1. 将 `The main contributions are:` 后三条贡献点从 hanging paragraph 写法改为无边框两列 `tabular`。
2. 左列固定宽度 `1.4em`，只放 `\textemdash{}`。
3. 右列为正文内容，宽度为 `\linewidth-1.4em`，换行后自动与正文首行左边界对齐。
4. 在 tabular 前加入 `\par\noindent`，避免表格接在上一句后面或产生段首缩进。

### 修改文件

- `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/submission_pricai2026.tex`
- `overleaf_pricai2026_package/submission_pricai2026.tex`

### 网页端同步与验证

1. 已将最新 TeX 全文同步到 Overleaf 项目 `6a204ea1614e48bb59209a8b`。
2. Overleaf CodeMirror 内部状态验证：
   - 包含 `\begin{tabular}{@{}p{1.4em}@{}p{\dimexpr\linewidth-1.4em\relax}@{}}`。
   - 不再包含旧的 `makebox[1.6em]`。
   - 不再包含旧的 `hangafter=1`。
3. 已重新编译并下载 PDF：
   - `overleaf_after_contribution_aligned_output_full.pdf`
   - 页数：15 页。
4. 已渲染第 2 页贡献点区域：
   - `overleaf_after_contribution_aligned_crop_page2_contrib.png`
   - 视觉检查确认破折号单独成左列，正文首行和续行左边界一致。

### 下一步

若用户希望破折号更接近参考图中的短横线风格，可将 `\textemdash{}` 改为 `--` 或 `\textendash{}`；当前版本保留之前用户要求的长破折号 `—`，并已解决对齐问题。
