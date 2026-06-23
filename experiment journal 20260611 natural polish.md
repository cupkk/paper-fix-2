# 研究进展日志 20260611：自然化语言精修与 Overleaf 同步核验

## 一、总体研究进展

本项目目标是将 FRAA 金融风险评估论文整理为符合 PRICAI 2026 / LNCS 投稿风格的可投稿版本。当前主线不是重新跑实验或改动真实结果，而是在保持实验数据、参考文献和官方模板不变的前提下，继续降低论文语言的模板感，强化论证逻辑，检查引用和排版一致性，并将确认后的版本同步到 Overleaf。

截至本轮，论文仍采用官方 LNCS 模板文件 `llncs.cls` 与 `splncs04.bst`。正文结构保持为 `Introduction`、`Related Work`、`Methodology`、`Experiments`、`Conclusion`、`References`。问题定义与限制说明已分别整合进 Methodology 与 Experiments/Conclusion 叙述中，避免单独扩展章节导致页数压力。当前 Overleaf 下载 PDF 为 15 页，未触及用户此前要求暂不考虑的 16 页硬限制问题。

## 二、本轮触发原因

用户指出当前稿件仍有几处明显可优化点：

- Abstract 信息过满，句式类似结果清单，AI 味偏重。
- Introduction 第一段偏百科式，需要更自然地引出金融风控中的同步更新和外部证据问题。
- Related Work 仍有文献堆叠感，需要减少“清单式”陈述，突出作者判断。
- Methodology 中 explanation head 描述不够具体，需要说明参考解释来源和时间有效性约束。
- Fig. 5 所在页面空白偏大，应压缩图尺寸但不破坏官方模板。
- Retrieval-depth、explanation、Conclusion 等段落需要更自然的因果解释，减少 checklist 句式。

本轮按用户要求调用并遵循本地 `nature-polishing` 与 `academic-research-suite` 两个 skill 的写作质量规则：先检查论证功能和段落逻辑，再做句子级自然化；不虚构数据、引用、机制或新实验。

## 三、本轮实际修改

修改的主文件：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`

同步与输出文件：

- `D:\github\paper-fix-2\overleaf_pricai2026_package.zip`
- `D:\github\paper-fix-2\overleaf_after_natural_polish_output_full.pdf`
- `D:\github\paper-fix-2\tmp\pdfs\overleaf_after_natural_polish\page_11_fig5.png`

具体修改包括：

1. 压缩 Abstract，将消融、feature occlusion、retrieval-depth 的多句清单改为一句综合判断：timestamp-valid external evidence 是主要提升来源，`K=5` 在有效上下文和检索噪声之间取得最好平衡。
2. 重写 Introduction 第一段局部表达，加入金融风控流水线中 behavioral modeling、external evidence collection、explanation generation 分离导致难以及时更新和审计的现实问题。
3. 调整贡献表述，将第一条贡献改为“financial risk scoring as a time-constrained retrieval problem”，更贴合本文方法的核心定位。
4. 压缩 Related Work 2.1 的开头，减少“某某工作表明”的文献清单感，突出传统 scorecard/tree ensemble 范式的优势和边界。
5. 在 Methodology 3.5 中将 explanation head 明确为 supervised explanation decoder，并补充 reference explanation 来自 analyst-approved risk factors 与 timestamp-valid evidence snippets。
6. 在实验设置中明确 checkpoint 由 validation Log Loss 选择，未使用 test-set 信息做模型选择。
7. 重写 retrieval-depth 分析的解释句，说明文档过少导致外部上下文不足，文档过多会引入弱相关证据并削弱融合表示。
8. 在 explanation quality 分析中补充边界：目标不是自动化最终决策，而是让模型输出更便于人工检查。
9. 将 Fig. 5 宽度由 `0.78\textwidth` 调整为 `0.55\textwidth`，减少 latency-throughput 图占用空间。
10. 压缩 Conclusion，减少对模块名的重复罗列，保留核心 takeaway：检索只有在时间有效、与行为序列融合并可审计时才最有价值。

## 四、核验结果

本地源码与 Overleaf 包源码一致：

- `figure_workspace_...\submission_pricai2026.tex`
- `overleaf_pricai2026_package\submission_pricai2026.tex`
- 两者 SHA256 相同：`60DEEC544C033C85CA6D42A52EDDF78D988EB90B3AFD51E797B392BA056185E7`

引用检查结果：

- `cite_commands = 42`
- `unique_cited = 40`
- `bib_entries = 40`
- `max_keys_per_cite = 2`
- `cmd_viol = []`
- `sent_viol = []`
- `missing = []`
- `unused = []`
- Abstract 粗略源码词数为 211，仍处于 150-250 词范围内。

PDF 检查结果：

- 最新 Overleaf 下载 PDF：`D:\github\paper-fix-2\overleaf_after_natural_polish_output_full.pdf`
- 页数：15 页
- PDF 文本中确认存在以下关键改写痕迹：
  - `supervised explanation decoder`
  - `analyst-approved risk factors`
  - `too few documents leave the model with limited external context`
  - `The main finding is that retrieval helps risk scoring most`
  - `Fig. 5.`

Overleaf 编译状态：

- 已同步到 Overleaf 项目并重新编译。
- 编译错误：0
- 编译警告：1，`Package amsmath Warning: Unable to redefine math accent \vec.`
- 编译信息：1，`Underfull \vbox (badness 10000) has occurred while \output is active []`
- 两项均为非致命信息，未阻断 PDF 生成。

## 五、保留与未改动事项

- 未修改任何真实实验数值。
- 未新增或删除参考文献。
- 未改动官方模板文件、全局行距、标题间距或字体设置。
- 未使用全局 spacing hack 调整浮动体间距。
- 未修改机制图内容。当前机制图仍按用户此前要求由用户后续自行精修或替换。
- Fig. 5 已压缩到 `0.55\textwidth`；第 11 页仍是 LNCS 浮动体自动形成的上方 Fig. 4、下方 Fig. 5 布局，但没有单独占页。

## 六、下一步建议

下一位 agent 应优先读取本日志和当前 Overleaf PDF，而不是重新从旧压缩包或旧 PDF 判断论文状态。若用户继续要求排版压缩，可以在不改官方模板的前提下，优先尝试局部调整 Fig. 4/Fig. 5 的浮动参数或将效率图改成更紧凑的小表格；不要直接修改 `llncs.cls` 或加入全局负间距。

若用户要求最终投稿前学术诚信审计，应重新进行一次 DOI/URL 联网逐条核验，并将结果固化为最终 reference verification 表。当前本轮只验证了 BibTeX 与正文引用一致性、引用分散度和 PDF 编译状态。

## 七、追加更新：20260611 排版紧凑化与旧小节删除

### 触发原因

用户指出三处问题：

- Overleaf 第 11 页仍像是两张图占据一整页。
- `Limitations and Reproducibility` 章节不需要，应删除。
- Related Work 内容偏多，贡献列表前的空白过大。

### 修改内容

本轮继续修改：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package.zip`

具体操作：

1. 删除 `Limitations and Reproducibility` 小节。
2. 将该小节中必须保留的边界说明压缩进 Conclusion，避免论文显得缺少边界意识。
3. 删除 Fig. 5 的浮动图环境，不再在正文中引用 `fig:latency` 或 `inference_latency_throughput.pdf`；latency 和 throughput 数值保留在 Efficiency Analysis 正文中。
4. 压缩 Related Work 的表述，减少文献清单式句子，但保留 40 篇真实参考文献的正文引用覆盖。
5. 贡献列表不再使用 `itemize`，改为三条悬挂缩进短段落，解决 `itemize` 在 LNCS 下产生的顶部空白问题。

### Overleaf 同步与核验

同步过程中发现一次网页端粘贴只替换了可见区域，导致 TeX 内容被错误叠加到约 60K 字符。随后使用 CodeMirror API 程序化选中全文，再粘贴本地最终 TeX，确认网页端源码恢复为约 30K 字符，并且贡献部分为 `\hangindent` 悬挂缩进版本。

最终 Overleaf 编译和下载结果：

- 最终 PDF：`D:\github\paper-fix-2\overleaf_after_layout_fix_output_full.pdf`
- 页数：14 页
- 最终渲染检查图：
  - `D:\github\paper-fix-2\tmp\pdfs\overleaf_after_layout_fix_final_manual_contrib\page_2.png`
  - `D:\github\paper-fix-2\tmp\pdfs\overleaf_after_layout_fix_final_manual_contrib\page_11.png`

最终静态检查：

- `unique_cited = 40`
- `bib_entries = 40`
- `max_keys_per_cite = 2`
- `sent_viol = []`
- `missing = []`
- `unused = []`
- PDF 文本中 `Limitations and Reproducibility = False`
- PDF 文本中 `Fig. 5. = False`
- PDF 文本中 `Inference latency and throughput = False`

视觉检查结论：

- 第 2 页贡献列表已无截图中那种大块空白，三条贡献紧跟引导句。
- 第 11 页只保留 Fig. 4、效率分析正文和 Conclusion，不再出现两张图占一整页的问题。
- 未修改真实实验数值、BibTeX 条目或官方 LNCS 模板文件。
