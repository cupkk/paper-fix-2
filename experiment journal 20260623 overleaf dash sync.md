# 研究进展日志 20260623 Overleaf 同步与贡献点格式

## 总体研究进展

FRAA 论文当前处于 PRICAI 2026 投稿前最终同步阶段。主稿和 Overleaf 包需要保持一致，网页端 Overleaf 需要同步最新 TeX，并确认最终 PDF 页数、编译状态和关键格式。

## 2026-06-23 更新

### 本次修改

1. 修改 Introduction 中 `The main contributions are:` 后的三条贡献点。
   - 原写法使用 TeX 源码中的 `--`。
   - 新写法改为显式 `\textemdash{}`，确保 PDF 中显示为长破折号 `—`。
2. 贡献点排序保持为：
   - 方法贡献：将金融风险评分建模为 time-constrained retrieval problem，并实例化为 FRAA。
   - 实验评估贡献：在大规模多源专有数据集上采用严格时间切分，并与 tree-based baselines 和 neural sequence models 比较。
   - 分析验证贡献：通过 ablation、retrieval-depth、explanation-quality 和 latency studies 分析 retrieval、temporal 和 explanation components。
3. 同步修改文件：
   - `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/submission_pricai2026.tex`
   - `overleaf_pricai2026_package/submission_pricai2026.tex`

### 网页端同步

已打开 Overleaf 项目 `6a204ea1614e48bb59209a8b`，将最新 TeX 全文替换到网页端 `submission_pricai2026.tex`。通过 CodeMirror 内部状态验证：

- 网页端源码包含 `\textemdash{} We formulate`。
- 网页端源码包含最新可复现性段落 `The main reproducibility risk is external validation under distribution shift`。
- 网页端源码不再包含旧写法 `hangafter=1 -- We formulate`。
- 网页端源码不再包含旧短板表述 `raw data cannot be released`。

### 编译验证

Overleaf 已重新编译：

- Errors: 0
- Warnings: 2
- 下载 PDF：`overleaf_after_contribution_dash_sync_output_full.pdf`
- 本地解析页数：15 页
- PDF 文本抽取确认三条贡献点均显示为 `—` 开头。

### 下一步

投稿前可继续检查最终 PDF 的第一页贡献点排版和算法图，但本轮贡献点格式、排序和 Overleaf 同步已经完成。
