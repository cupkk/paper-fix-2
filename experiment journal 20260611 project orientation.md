# 研究进展日志 20260611：项目接手摸底

## 一、总体研究进展

本项目是 FRAA 金融风险评估论文的 PRICAI 2026 / Springer LNCS 投稿修订工作区，核心目标是把现有论文整理为可投稿版本。当前主线不是重新跑实验或修改实验数值，而是在保留真实数据、参考文献和官方 LNCS 模板的前提下，完成论文结构、语言、图表一致性、引用分布、Overleaf 同步和最终 PDF 排版核验。

当前主稿为：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`

当前 BibTeX 为：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.bib`
- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.bib`

当前 Overleaf 项目地址记录为：

- `https://www.overleaf.com/project/6a204ea1614e48bb59209a8b`

当前最新有效 PDF 记录为：

- `D:\github\paper-fix-2\overleaf_after_layout_fix_output_full.pdf`

最近一次有效 Overleaf 编译结果来自 2026-06-11 排版紧凑化后版本：14 页，0 errors；日志中记录仍有非致命 `amsmath` 警告和 `Underfull \vbox` 信息。按已核对的 PRICAI 2026 要求，Springer LNAI/LNCS 模板下 long paper 为 12--16 页且包含参考文献，因此当前 14 页属于 regular/long paper 页数范围。

## 二、2026-06-11 项目接手摸底

### 本次操作

本轮目标是详细了解项目现状，供后续继续论文修订、投稿前审计或 Overleaf 同步使用。已完成以下阅读和核验：

- 查看根目录文件结构、Git 状态、日志文件列表和 Overleaf/PDF 产物。
- 读取最新日志 `experiment journal 20260611 natural polish.md`。
- 读取图表一致性、参考文献核验、引用分散优化等关键日志：
  - `experiment journal 20260610 figure_table_consistency.md`
  - `experiment journal 20260610 references.md`
  - `experiment journal 20260610 citation spread.md`
- 读取当前主稿 `submission_pricai2026.tex`。
- 读取当前 40 条参考文献 `submission_pricai2026.bib`。
- 读取最终绘图脚本 `scripts/final_figures/figure_code_pricai_final_figures.py`。
- 抽查历史绘图脚本、图表检查报告、官方 LNCS 模板 `samplepaper.tex` 和 `readme.txt`。
- 静态核验主稿、引用、图像路径和 Overleaf 打包内容。

### 当前仓库状态

Git 当前分支为 `main`，并显示存在未提交改动和若干未跟踪的 Playwright/PDF 临时产物。重要的已修改或新增状态包括：

- `experiment journal 20260611 natural polish.md`
- `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/submission_pricai2026.tex`
- `overleaf_pricai2026_package/submission_pricai2026.tex`
- `overleaf_pricai2026_package.zip`
- 多个 `.playwright-mcp` 日志和 `tmp/pdfs/...` 渲染页图
- 最新 PDF：
  - `overleaf_after_config_table_output_full.pdf`
  - `overleaf_after_final_sync_output_full.pdf`
  - `overleaf_after_layout_fix_output_full.pdf`

这些改动均应视为用户/前序 agent 的工作成果，后续不要用 `git reset`、checkout 或清理命令直接覆盖。

### 当前论文结构

主稿当前采用：

- `\documentclass[runningheads]{llncs}`
- `llncs.cls`
- `splncs04.bst`
- `\bibliographystyle{splncs04}`
- `\bibliography{submission_pricai2026}`

当前正文一级章节为：

1. `Introduction`
2. `Related Work`
3. `Methodology`
4. `Experiments`
5. `Conclusion`

当前已删除独立 `Limitations and Reproducibility` 小节，必要边界说明被压缩进 `Conclusion`。当前也已删除正文中的 Fig. 5 浮动图，不再引用 `fig:latency` 或 `inference_latency_throughput.pdf`；效率指标只保留在 `Efficiency Analysis` 正文中。

### 当前主稿静态核验结果

本轮重新核验结果：

- 工作区主稿 SHA256：
  - `CD91F2B5E048C647E9504D7D7CCD766AE19E4409817EBFE173FA1329ADE3BBBB`
- Overleaf 包内主稿 SHA256：
  - `CD91F2B5E048C647E9504D7D7CCD766AE19E4409817EBFE173FA1329ADE3BBBB`
- 两份 TeX 字节完全一致。
- `bib_entries = 40`
- `unique_cited = 40`
- `cite_commands = 42`
- `missing_cites = []`
- `unused_bib = []`
- 当前 `\includegraphics` 共 4 处：
  - `figures/algorithm/algorithm_1_0ebe5141.png`
  - `main_results_comparison.pdf`
  - `retrieval_depth_sensitivity.pdf`
  - `explanation_quality_evaluation.pdf`
- 所有图像路径均存在。
- 未发现以下高风险残留：
  - `Limitations and Reproducibility`
  - `Fig. 5`
  - `fig:latency`
  - `will be updated`
  - `simulated`
  - `pilot`
  - `estimated`
  - `pending`
  - `production-scale`

### Overleaf 包内容

当前 `overleaf_pricai2026_package.zip` 含 9 个文件：

- `submission_pricai2026.tex`
- `submission_pricai2026.bib`
- `llncs.cls`
- `splncs04.bst`
- `figures/algorithm/algorithm_1_0ebe5141.png`
- `main_results_comparison.pdf`
- `retrieval_depth_sensitivity.pdf`
- `explanation_quality_evaluation.pdf`
- `inference_latency_throughput.pdf`

注意：`inference_latency_throughput.pdf` 当前已不被主稿引用。它保留在包内不会影响编译，但如果用户要求最终投稿包极简清理，建议删除该未引用文件后重新打包，并重新同步/编译确认。

### 图表与数据状态

历史日志显示，2026-06-10 已确认早期图表脚本与 LaTeX 表格存在多处不一致。后续已经改为“以 LaTeX 表格中的数值为主数据源”，并用最终脚本重新生成投稿用图。当前主稿只保留：

- Fig. 1：流程/机制图，来自用户后续替换的 `流程图.png`，复制为 `figures/algorithm/algorithm_1_0ebe5141.png`。
- Fig. 2：主结果图 `main_results_comparison.pdf`。
- Fig. 3：特征组遮蔽与检索深度图 `retrieval_depth_sensitivity.pdf`。
- Fig. 4：解释质量图 `explanation_quality_evaluation.pdf`。

最终绘图脚本为：

- `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\scripts\final_figures\figure_code_pricai_final_figures.py`

历史脚本目录中仍有很多旧图脚本和旧数值，它们不应被直接当作当前投稿图的数据来源。若后续需要重画图，应优先使用 `scripts/final_figures/figure_code_pricai_final_figures.py`。

### 参考文献状态

当前投稿稿使用 40 条参考文献，全部在正文中被引用。历史日志记录：

- 原始 `references.bib` 中大量 arXiv 条目并非“查不到”，但主题相关性弱、放置位置不匹配。
- 当前投稿版 `submission_pricai2026.bib` 已切换到更稳妥的经典正式出版文献和 DOI 文献。
- 2026-06-10 已完成引用分散优化：单个 `\cite{}` 最多 2 篇，同一句累计引用不超过 2 篇。

后续若做最终投稿前学术诚信审计，建议联网重新逐条核验 DOI/URL，并形成最终 reference verification 表。

### 当前风险与注意事项

- 当前项目不是传统软件项目，而是论文修订、图表一致性、Overleaf 同步和投稿包管理工作区。
- 根目录和 `tmp/` 下有大量历史 PDF、页面渲染图、网络日志、Playwright 会话文件，不应未经用户确认批量删除。
- 当前 `overleaf_pricai2026_package` 内有未引用效率图 PDF；最终投稿包可以清理，但清理后必须重新打包和编译。
- 当前主稿作者、单位、运行头均为空，符合匿名投稿阶段；后续不要擅自添加作者信息。
- 不要修改官方 `llncs.cls`、`splncs04.bst` 或加入全局负间距、全局压缩行距等模板 hack。
- 若继续排版优化，应优先做局部图尺寸、图位置或正文压缩，不要破坏 LNCS 模板。
- 若继续文字精修，应避免改动真实实验数值、BibTeX 条目和已经核验的引用分布。

### 下一位 agent 应优先读取

1. 本日志。
2. `experiment journal 20260611 natural polish.md`
3. `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
4. `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.bib`
5. `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\scripts\final_figures\figure_code_pricai_final_figures.py`
6. 最新 PDF：
   - `D:\github\paper-fix-2\overleaf_after_layout_fix_output_full.pdf`

### 下一步建议

- 如果用户要求继续压缩或最终投稿包清理：删除包内未引用的 `inference_latency_throughput.pdf`，重新生成 `overleaf_pricai2026_package.zip`，同步 Overleaf 后重新编译。
- 如果用户要求投稿前审计：进行 DOI/URL 联网核验、PDF 页数与模板核验、匿名性检查、图表路径和引用跳转检查。
- 如果用户要求语言继续精修：只在主稿和 Overleaf 包 TeX 中同步修改，修改后重新检查 SHA256、引用覆盖和 PDF 编译。
- 如果用户要求重画图：只使用最终脚本和主稿表格数值，不要回退到旧 `scripts/main_result` 或 `scripts/ablation` 中的历史合成数据脚本。
