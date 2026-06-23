# 研究进展日志 20260611 最终同步与核验

## 一、总体进展

本轮是在用户确认 Overleaf 网页端已经可以登录后，继续完成精修稿的最终网页端同步、编译、PDF 下载和排版核验。当前论文仍按此前确定的保守策略处理：不补回旧稿中带有 synthetic、pilot、estimated 标记的商业收益、产品迁移或训练曲线内容；只保留有来源支撑、能增强审稿可读性的实验配置表和正文精修。

当前稿件核心状态：

- Overleaf 项目：`https://www.overleaf.com/project/6a204ea1614e48bb59209a8b`
- 主 TeX：`D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- Overleaf 包 TeX：`D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`
- 最新 Overleaf 下载 PDF：`D:\github\paper-fix-2\overleaf_after_final_sync_output_full.pdf`

## 二、本轮操作

### 2026-06-11 14:56:31 +08:00

重新打开 Overleaf 项目后，页面已进入编辑器，当前活动文件为 `submission_pricai2026.tex`。通过 CodeMirror 6 编辑器内部文档读取确认网页端源码状态：

- 网页端源码长度约 31.4K 字符，与本地最终版一致，只存在结尾换行级别差异。
- 网页端源码包含 `tab:experimental_config`。
- 网页端源码不包含 `Limitations and Reproducibility`。
- 网页端源码不包含 `fig:latency`。
- 网页端 Efficiency Analysis 保留 15.7 ms/query、4,070 queries/s、retrieval cost about 4.2 ms 的文字结果。

因此本轮没有再次粘贴替换全文，避免重复粘贴或可视区域粘贴错误。

## 三、Overleaf 编译与下载结果

在 Overleaf 网页端点击 `Recompile` 后，编译完成：

- Errors: 0
- Warnings: 2
- All logs: 3

新下载 PDF：

- 路径：`D:\github\paper-fix-2\overleaf_after_final_sync_output_full.pdf`
- 文件大小：2,112,074 bytes
- SHA256：`AA1A9EDF3B4D1DD1D23BEA364A2E52F554627BCB67B3AC87C1A2FCEA6E63C079`

说明：PowerShell 直接下载 Overleaf PDF 会因缺少浏览器登录 cookie 被拒绝。本轮临时使用已登录 Playwright 浏览器上下文获取 PDF，并通过本地一次性 HTTP 接收脚本保存文件。该脚本只用于本轮下载验证，不属于论文资产，已安排删除。

## 四、PDF 页数与版面核验

使用 PyMuPDF 解析并渲染 `overleaf_after_final_sync_output_full.pdf`：

- PDF 总页数：15 页，仍低于 16 页限制。
- 新增实验配置表出现在第 8 页。
- `Feature Groups and Retrieval Depth` 与 `Explanation Quality` 正文在第 10 页。
- Fig. 3、Fig. 4、Efficiency Analysis 正文和 Conclusion 起始在第 11 页。
- Conclusion 后半部分与 References 起始在第 12 页。

渲染检查文件：

- `D:\github\paper-fix-2\tmp\pdfs\overleaf_after_final_sync\page_10.png`
- `D:\github\paper-fix-2\tmp\pdfs\overleaf_after_final_sync\page_11.png`
- `D:\github\paper-fix-2\tmp\pdfs\overleaf_after_final_sync\page_12.png`

视觉检查结论：

- 第 11 页不再是两张图孤立占整页。
- Fig. 3 和 Fig. 4 与 Explanation Quality、Efficiency Analysis、Conclusion 的衔接可以接受。
- 第 12 页顺接 Conclusion 与 References，没有明显断裂。

## 五、静态一致性检查

对 `overleaf_pricai2026_package\submission_pricai2026.tex` 和对应 BibTeX 进行静态检查：

- `tex_bytes = 31402`
- `cite_commands = 42`
- `unique_cited = 40`
- `bib_entries = 40`
- `max_keys_per_cite = 2`
- `cmd_violations = []`
- `sentence_citation_violations = []`
- `missing_bib_entries = []`
- `unused_bib_entries = []`
- `figures = 4`
- `tables = 3`
- `label_ref_missing = []`
- `has_experimental_config = True`
- `has_limitations_section = False`
- `has_latency_figure_ref = False`
- `has_latency_pdf_include = False`

本地工作区源文件与 Overleaf 包源文件 SHA256 一致：

- `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- `overleaf_pricai2026_package\submission_pricai2026.tex`
- SHA256：`CD91F2B5E048C647E9504D7D7CCD766AE19E4409817EBFE173FA1329ADE3BBBB`

## 六、保留与未改动事项

- 未新增真实实验数值。
- 未改动 BibTeX 条目数量。
- 未修改官方 LNCS 模板文件、全局行距、字体或标题间距。
- 未恢复旧稿中带有 synthetic、pilot、estimated 标记的商业收益、产品迁移或训练曲线内容。
- `overleaf_pricai2026_package` 中仍保留未被正文引用的 `inference_latency_throughput.pdf` 文件；当前正文不再引用该图。若后续要做最终投稿源包清理，可以单独决定是否从 Overleaf 项目和本地 source zip 中移除该未用图文件。

## 七、下一步建议

如果继续做最终投稿前检查，建议优先处理：

1. 再做一次 DOI/URL 联网核验，生成最终 reference verification 表。
2. 检查 Overleaf 源包中未引用资产是否需要删除，特别是 `inference_latency_throughput.pdf`。
3. 最终提交前重新下载 Overleaf source zip 和 PDF，确认 PDF 页数、正文源码 SHA256、BibTeX 一致性和图表渲染结果均与本日志记录一致。
