# 研究进展日志 20260611 恢复辅助实验分析

## 一、总体进展

用户指出精修后的论文相对最初稿缺少若干辅助实验与业务分析，包括场景适应、离线业务影响模拟、上下文窗口敏感性、增量特征组添加、延迟与离线业务效用等内容，并要求以表格数据为准，必要时才绘图。同时要求删除当前的 `Experimental configuration used for all reported test-set results` 表。

本轮已按用户要求恢复这些分析，但采用紧凑表格方式控制篇幅，避免恢复过多旧图。新增内容仍保留审稿边界：RAR 与业务收益相关数值写为 offline replay estimates，而不是线上 A/B 结果。

## 二、修改文件

本轮修改并同步了以下文件：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package.zip`

最新 Overleaf 编译 PDF：

- `D:\github\paper-fix-2\overleaf_after_restore_auxiliary_output_full.pdf`

## 三、具体内容改动

1. 删除了原新增的实验配置表：
   - `tab:experimental_config`
   - caption: `Experimental configuration used for all reported test-set results.`

2. 新增 `Transfer, Context, and Offline Utility` 小节，用于承接主结果之后的辅助分析。

3. 新增 Table 2 `Scenario adaptation and offline replay utility`，恢复两组旧稿数据：
   - Product-scenario adaptation:
     - Scenario-specific baseline: 0.00 / 0.00
     - LP-FT: Credit card +3.14 / +2.97, Mortgage +2.88 / +2.45
     - LoRA-FT: Credit card +13.49 / +12.63, Mortgage +11.72 / +10.88
     - FRAA full-FT: Credit card +18.21 / +17.10, Mortgage +16.45 / +15.33
   - Offline replay business impact:
     - RF + KB features: Log Loss delta -2.13%, estimated RAR lift +1.89%
     - Transformer: -11.02%, +5.34%
     - FRAA (-KB): -15.18%, +7.80%
     - FRAA (full): -19.57%, +10.45%

4. 新增 Table 3 `Context-window sensitivity, incremental feature addition, and serving efficiency`，恢复三组旧稿数据：
   - Context window:
     - 30 days: 0.5413 / 0.3942
     - 60 days: 0.5291 / 0.4045
     - 90 days: 0.5210 / 0.4123
     - 120 days: 0.5163 / 0.4185
     - 180 days: 0.5172 / 0.4171
   - Incremental feature-group addition:
     - Knowledge-retrieved only: 0.5412 / 0.3971
     - + Transaction dynamics: 0.5275 / 0.4083
     - + Macroeconomic indicators: 0.5198 / 0.4146
     - + Quasi-static profile: 0.5163 / 0.4185
   - Serving efficiency:
     - RF + KB features: 1.9 ms/query, 12,530 queries/s
     - XGBoost: 2.1 ms/query, 11,200 queries/s
     - LSTM: 8.3 ms/query, 5,910 queries/s
     - Transformer: 12.4 ms/query, 4,320 queries/s
     - FRAA (full): 15.7 ms/query, 4,070 queries/s

5. 调整了 Abstract、贡献列表、Evaluation Questions、Ablation and Analysis、Efficiency Analysis 和 Conclusion，使新增表格与整体逻辑自然衔接。

6. 未恢复旧稿中的 product adaptation 图、business scatter 图、context-window 图、incremental feature 图和 latency 图。原因是用户倾向“大部分加表即可”，而当前两张紧凑表已覆盖所有指定数值，且有利于控制 16 页上限。

## 四、同步与编译结果

本地工作区 TeX 与 Overleaf 包 TeX 已同步：

- SHA256：`5DA7EB87BC2F2D2B98FC9D7B236867FB93ADCFA97E13E7E8FB7F34078FD6E3FD`

重新生成的本地 Overleaf zip：

- `D:\github\paper-fix-2\overleaf_pricai2026_package.zip`
- SHA256：`129D3BC319E69E609D70ADABAB04D932623A2B35F888D2CB3BABA202F901EEBF`

Overleaf 网页端已使用 CodeMirror 6 文档 API 全文替换为本地最终 TeX，并确认：

- `tab:experimental_config` 不存在。
- `tab:transfer_utility` 存在。
- `tab:sensitivity_efficiency` 存在。
- `10.45` 存在。
- `Product-scenario adaptation` 存在。
- `Incremental feature-group addition` 存在。

Overleaf 编译状态：

- Errors: 0
- Warnings: 2
- All logs: 3

最新下载 PDF：

- `D:\github\paper-fix-2\overleaf_after_restore_auxiliary_output_full.pdf`
- SHA256：`2C4403A9D09B8017FCB8A87981EA9E3207C30FD8AC0D9A1443B3FA16371A3DF4`
- 文件大小：2,146,206 bytes
- 页数：16 页

## 五、静态检查结果

对 Overleaf 包中的 TeX 与 BibTeX 检查结果：

- `tex_bytes = 35173`
- `cite_commands = 42`
- `unique_cited = 40`
- `bib_entries = 40`
- `max_keys_per_cite = 2`
- `cmd_violations = []`
- `sentence_citation_violations = []`
- `missing_bib_entries = []`
- `unused_bib_entries = []`
- `figures = 4`
- `tables = 4`
- `label_ref_missing = []`
- `has_experimental_config = False`
- `has_transfer_utility = True`
- `has_sensitivity_efficiency = True`
- `has_scenario_adaptation = True`
- `has_rar_1045 = True`
- `has_window_120 = True`
- `has_incremental_feature = True`
- `has_latency_table = True`

## 六、PDF 版面核验

使用 PyMuPDF 渲染并检查了新增内容附近页面：

- 第 9 页：Fig. 2 后接 `Transfer, Context, and Offline Utility` 小节与 Table 2。Table 2 未超宽。
- 第 10 页：Table 3 完整显示，随后进入 `Ablation and Analysis`。Table 3 未超宽。
- 第 11 页：Table 4 与 `Feature Groups and Retrieval Depth`、`Further Evaluation` 正文衔接正常。
- 第 12 页：Fig. 3、Fig. 4、Efficiency Analysis 和 Conclusion 起始同页，仍保持图文衔接。
- 第 13 页：Conclusion 后半与 References 起始，未出现明显断裂。

渲染检查目录：

- `D:\github\paper-fix-2\tmp\pdfs\overleaf_after_restore_auxiliary\`

## 七、保留与风险说明

- 本轮没有新增 BibTeX 条目，也没有修改真实实验主结果数值。
- 本轮没有恢复旧稿中的额外图，只用表格恢复用户指定的数值分析。
- 当前全文正好 16 页，已到 PRICAI/LNCS 长文页数上限。后续若再新增图或长段落，必须先压缩正文或参考文献前空间。
- RAR、业务影响、场景适应相关表述已写成 offline replay / adaptation estimates，避免被审稿人理解为已经完成线上 A/B 或生产收益验证。

## 八、下一步建议

如果继续精修，建议优先：

1. 检查 Table 2 和 Table 3 的 caption 是否还需要更明确地标注 offline / adaptation estimate。
2. 若用户希望进一步增强视觉呈现，只建议最多新增 1 张由表格数据重绘的 summary 图，否则页数会很紧。
3. 最终投稿前重新下载 Overleaf source zip 和 PDF，确认 16 页、0 errors、表格不超宽、所有引用一致。
