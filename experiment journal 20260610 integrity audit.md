# experiment journal 20260610 integrity audit

## 研究进展总览
- 目标：检查当前 `submission_pricai2026.tex` 是否存在学术不端、证据不足、图表与正文不一致、引用不稳、或容易被审稿人拒稿的问题。
- 当前结论：当前提交稿比 `original_tex.tex` 收敛很多，已去掉旧稿中明确的 `simulated/pilot` 表述；但若没有真实内部实验记录、专家评分记录和离线回放依据，文中若直接按“实证结果”提交，仍有明显学术诚信风险。
- 已确认：当前提交稿与打包稿的 `submission_pricai2026.tex`、`submission_pricai2026.bib` 哈希一致；当前 `submission_pricai2026.bib` 共 40 条且未发现 `arXiv/eprint` 字段。
- 已确认：当前版本主表和主图、消融图、运营评估图的数据脚本一致，图表本身已经比旧稿稳定很多。
- 主要风险：原始数据、划分清单、训练日志、专家评分原表、离线 replay 细节、模型 checkpoint 都未在当前工作区看到，导致“论文里写的结果到底是不是可审计真实结果”仍然无法闭环。

## 2026-06-10 审计记录
### 已核查内容
- `submission_pricai2026.tex` 第 4 章和后续分析章节的主张、数值、限制说明。
- `scripts/main_result/*.py`、`scripts/ablation/*.py` 与正文表格/图表的数据一致性。
- `original_tex.tex` 中是否仍保留明确的 simulated / pilot / placeholder 语句。
- `submission_pricai2026.bib` 是否仍有 arXiv / eprint 类型引用。
- PRICAI 官方投稿要求中页面与双匿名约束。

### 关键发现
- 旧稿 `original_tex.tex` 明确写过 simulated/pilot 说明；当前提交稿已删除这类显式措辞，方向是对的。
- 当前提交稿的表格数值和绘图脚本一致，没有发现“图和表对不上”的硬冲突。
- 图 1 `figures/algorithm/algorithm_1_0ebe5141.png` 是 AI/提示生成式架构图，视觉上存在两个问题：标题区域出现重复编号 `3 3`；流程上把 `Knowledge-Retrieved Context` 画成早期输入，并画出 `Generative Retrieval-Augmented Reasoning` 到融合投影模块的反馈，而正文方法描述是先编码用户状态，再查询 timestamp-valid 文档并通过 cross-attention 融合。该图需要按正文流程重画或至少修正。
- 当前版本仍然把以下内容当作正式实验结果来写：24 个月专有数据集、2000 万+ 用户、12 亿交互、5 位领域专家评分、离线业务收益、低延迟推理。
- 这些内容本身不一定是假的，但当前工作区没有看到可独立审计的原始证据链，所以不能直接判断为“已被证明真实”。
- `submission_pricai2026.bib` 已不再是原始旧稿那种高比例 arXiv 堆砌；但引用是否足以支撑每一条结论，仍需逐段复核。

### 当前判断
- 不能给出“保证不会被拒稿”或“保证没有学术不端”的结论。
- 若用户能提供内部实验日志、评分原表、数据字典、划分清单、replay 公式和生成脚本，则当前稿件有机会被整理到可投稿状态。
- 若这些结果其实是合成、占位或 pilot 数字，而正文没有明确标注，就属于高风险甚至不可投稿状态。

### 下一步建议
- 补一份数据可用性 / 代码可用性说明，明确哪些能公开，哪些受限。
- 为每个核心表图补 source-data 记录或内部审计说明。
- 补专家评分协议、评分对象范围、匿名化处理和伦理说明。
- 对业务收益表补离线 replay 公式、预算约束和限制条件。
- 若没有多次独立运行结果，继续保留“单一固定 split”的限制，但把核心结论措辞再收紧一点。
