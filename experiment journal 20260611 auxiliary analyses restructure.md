# 研究进展日志 20260611：辅助分析拆分恢复与章节重排

## 一、总体研究进展

本项目目标是将 FRAA 论文整理成符合 PRICAI/LNCS 页数和写作要求的投稿版本，同时尽量保留精修前论文中有价值的实验分析。当前主线论文已经完成语言精修、引用分散、流程图替换、Overleaf 同步和 16 页内编译检查。上一轮为恢复用户指定的辅助分析，曾把场景适应、离线业务影响、上下文窗口、增量特征组和延迟/吞吐量压缩到两张汇总表中，但用户明确指出这种处理不符合预期。

本轮新的目标是：把每一类辅助分析放回合适章节位置，配独立表格和正文解释，不再使用混合汇总表；新文本参考精修前 `original_tex.tex` 和 `FRAA_中英对照人工精修稿_20260604.md` 的叙述逻辑，同时继续使用 `nature-polishing` 和 `academic-research-suite` 的约束进行语言与逻辑润色。

关键写作边界：

- 不新增或发明数据。
- 不改变用户认为真实的原始数值。
- RAR 和业务影响按离线回放/离线估计表述，不写成线上因果收入提升。
- 场景适应按迁移/适应结果表述，不扩大为已验证的生产 A/B 结论。
- 删除当前新增的 `Experimental configuration` 表，并避免把新内容塞进现有表格。

## 二、本轮执行计划

1. 删除当前混合小节 `Transfer, Context, and Offline Utility`。
2. 删除当前两张混合汇总表 `tab:transfer_utility` 与 `tab:sensitivity_efficiency`。
3. 在 `Main Results` 后添加独立小节 `Scenario Adaptation`，放置场景适应表和自然解释。
4. 在 `Main Results` 后添加独立小节 `Offline Replay Utility`，放置 Log Loss 降幅与估计 RAR 提升表，并明确离线回放边界。
5. 在 `Ablation and Analysis` 中添加 `Context-Window Sensitivity`，放置上下文窗口表和解释。
6. 在 `Ablation and Analysis` 中添加 `Incremental Feature-Group Addition`，放置增量特征组表和解释。
7. 在 `Further Evaluation / Efficiency Analysis` 中添加独立延迟与吞吐量表，恢复延迟/离线业务效用相关描述中可被当前数据支持的部分。
8. 同步到 Overleaf 包，运行静态检查，随后同步网页端 Overleaf、编译、下载 PDF 并检查页数和版面。

## 三、已确认数据来源

数据来自精修前 `original_tex.tex` 和人工精修参考稿 `FRAA_中英对照人工精修稿_20260604.md`。

- 场景适应：Credit Card 和 Mortgage 上的 LP-FT、LoRA-FT、FRAA full-FT 相对 Recall@1/Recall@5 提升。
- 离线业务影响：RF + KB Features、Transformer、FRAA (-KB)、FRAA (full) 的 Log Loss 降幅和估计 RAR 提升。
- 上下文窗口：30、60、90、120、180 天窗口下的 Log Loss 与 Recall@5。
- 增量特征组：从知识检索上下文开始，逐步加入交易动态、宏观指标、准静态画像后的 Log Loss 与 Recall@5。
- 延迟与吞吐量：RF + KB Features、XGBoost、LSTM、Transformer、FRAA (full) 的 ms/query 和 queries/s。

## 四、当前待完成

下一步直接修改主 TeX 文件：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`

完成后同步：

- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package.zip`

## 五、已完成的 TeX 重构

已修改主 TeX 文件：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`

具体改动：

- 删除混合小节 `Transfer, Context, and Offline Utility`。
- 删除混合表 `tab:transfer_utility` 与 `tab:sensitivity_efficiency`。
- 在 `Main Results` 后新增 `Scenario Adaptation` 小节，加入独立表 `tab:scenario_adaptation` 和正文说明。
- 在 `Main Results` 后新增 `Offline Replay Utility` 小节，加入独立表 `tab:offline_utility`，并明确 RAR 是离线回放估计。
- 在 `Ablation and Analysis` 中新增 `Context-Window Sensitivity` 小节，加入独立表 `tab:context_window` 和 120 天窗口解释。
- 在 `Ablation and Analysis` 中新增 `Incremental Feature-Group Addition` 小节，加入独立表 `tab:incremental_features` 和增量特征解释。
- 在 `Further Evaluation / Efficiency Analysis` 中新增独立表 `tab:latency`，恢复延迟与吞吐量描述。
- 更新 `Evaluation Questions`，使实验顺序与当前章节逻辑一致。

当前检查到的新旧标签状态：

- 已移除：`tab:transfer_utility`、`tab:sensitivity_efficiency`、`tab:experimental_config`。
- 已新增：`tab:scenario_adaptation`、`tab:offline_utility`、`tab:context_window`、`tab:incremental_features`、`tab:latency`。

下一步：运行静态检查，随后同步 Overleaf 包并编译检查页数和版面。

## 六、最终同步、编译与版面检查结果

已完成最终版同步和 Overleaf 编译。

最终修改文件：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package.zip`

最终输出 PDF：

- `D:\github\paper-fix-2\overleaf_after_auxiliary_restructure_output_full.pdf`
- 页数：16 页
- PDF SHA256：`02E563CEC6333AA69DB0667E90410153DA989C5DFB15B4BA95F4F0317030F493`
- TeX SHA256：`1007284664B8186BA37FCD33DC57A3F3267787FF3EE27B72BC4179D85C44D2A5`
- Overleaf zip SHA256：`E61BD52E71CEF6F7CE131A7CA4E24D40BBB34FDCB906BF5467CB642E27A2BBBF`

最终静态检查结果：

- 40 个唯一引用，对应 40 个 BibTeX 条目。
- 无缺失 BibTeX，无未使用 BibTeX。
- 单个 `\cite{}` 未超过 2 篇引用。
- 无缺失 `\ref{}` 标签。
- 图：4 张。
- 表：7 张。
- 旧混合表标签已删除：`tab:transfer_utility`、`tab:sensitivity_efficiency`、`tab:experimental_config`。
- 新增独立标签存在：`tab:scenario_adaptation`、`tab:offline_utility`、`tab:context_window`、`tab:incremental_features`、`tab:latency`。

最终排版检查：

- Fig. 2 已固定在 `Main Results` 对应位置，不再漂移到场景适应小节之后。
- Table 2 场景适应位于 `Scenario Adaptation` 小节内，表前有方法说明，表后有结果解释和离线迁移边界。
- Table 3 离线 RAR 位于 `Offline Replay Utility` 小节内，明确写为离线回放/离线决策支持证据，不是线上因果收入声明。
- Table 5 上下文窗口位于 `Context-Window Sensitivity` 小节内。
- Table 6 增量特征组位于 `Incremental Feature-Group Addition` 小节内。
- Table 7 延迟/吞吐量位于 `Efficiency Analysis` 小节内。
- 新增表格均未发现超宽，正文和图表顺序符合“先介绍、再图表、再解释”的基本逻辑。

保留与取舍：

- 保留用户要求恢复的五类数据和对应描述。
- 没有额外新增旧稿中的大图，避免超页和重复视觉负担。
- 为确保图表对应正文位置，新增表使用 `[H]` 就地放置，并加入 `float` 包；主结果 Fig. 2 也使用 `[H]` 固定到 Main Results 后。
- 为恢复 16 页上限，对新增段落做了语言压缩，但保留原意和关键边界。
