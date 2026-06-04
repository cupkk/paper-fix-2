# 实验进展日志 20260603

## 总体研究进展

### 项目目标
本项目目标是将当前 FRAA 论文精修为可投稿 PRICAI 2026 的 CCF-C 会议论文版本。用户明确说明实验结果已经完成且真实可用，代码和结果已跑通，后续重点不是改实验数值，而是按会议风格完成论文精修、逻辑与实验一致性检查、公式/引用/图表检查、LaTeX 排版编译，并输出可投稿版本。

### 当前研究方向
论文提出 FRAA，即面向实时金融风险评估的风险感知检索增强智能体框架。核心设计包括时间感知多源序列融合、金融知识库检索增强推理、风险评分与解释生成双头。实验围绕主风险评分、场景迁移、业务影响、特征重要性、上下文窗口、检索深度、训练动态、解释质量和推理延迟展开。

### 已完成工作
- 初步梳理仓库结构：根目录包含 `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/`、`官方latex模板/` 和 `参考范文.pdf`。
- 确认论文主文件为 `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/original_tex.tex`，参考文献文件为同目录下 `references.bib`。
- 确认官方模板目录包含 Springer LNCS/LNAI 模板文件：`llncs.cls`、`samplepaper.tex`、`splncs04.bst`、`llncsdoc.pdf`。
- 查询 PRICAI 2026 官方页面，确认投稿使用 Springer LNAI/LNCS 模板，双盲审稿，PDF 通过 EasyChair 提交；长文 12-16 页、短文 6-11 页，页数含参考文献。
- 加载本地 `figures-for-papers` 技能说明，后续如需修改数据图，应优先参考本地 figures4papers 案例，导出高 DPI PNG 和 PDF/SVG，并检查输出文件。
- 阅读现有 `figure_check_report.md`，确认 13 个脚本生成图已修复输出路径和边界裁切问题；2 个机制/动机图为 AI 生成图，仅有 prompt，后续用户计划用 PPT 手动完善。

### 关键发现
- 当前 LaTeX 主文件使用 `\documentclass[10pt,twocolumn]{article}`，但 PRICAI 2026 要求 Springer LNAI/LNCS 样式，应迁移到 `\documentclass[runningheads]{llncs}` 并使用 `splncs04.bst`。
- 当前参考文献样式为 `IEEEtran`，与 LNCS 模板不一致，应改为 `splncs04`。
- 当前正文和脚注多处写有 `simulated/pilot estimates`、`will be updated`、`pending production A/B` 等表述；这与用户明确说明的“结果已经完成且真实”冲突，会削弱投稿可信度，后续应统一改成真实内部实验/离线回放/专家评估等准确表述，且不能改变数值。
- 当前论文图表很多且存在重复：主结果、消融、检索深度等内容在 Experiments/Ablation/Evaluation 中重复出现。按 LNCS 16 页上限，后续需要压缩重复图表和叙述，优先保留最关键、最能支撑贡献的结果。
- 当前参考文献大量使用 `arxiv-25xx` 条目，且部分题名与金融风险、RAG、可解释推荐的相关性较弱。后续应进行引用相关性和可信度审查，替换或删除不支撑论点的引用。
- 当前机制图和动机图为 PNG，后续可保留占位，但投稿前应由用户用 PPT 完善并导出更适合 LNCS 的清晰图像或矢量图。

### 当前阻塞/风险
- 需要将 article 双栏稿迁移为 LNCS 单栏稿，迁移后页数、浮动体位置和宏包兼容性需要重新编译验证。
- 需要谨慎处理“pilot/simulated”措辞：不能改实验数值，但必须和用户声明的真实结果保持一致。
- 需要检查本地 LaTeX 工具链是否可用；若不可用，需要记录无法本地编译的原因，并给出 Overleaf/LNCS 编译路径。

### 下一步建议
1. 建立投稿工作副本，例如 `submission_pricai2026.tex`，保留 `original_tex.tex` 作为来源稿。
2. 按 LNCS 模板迁移导言区、标题、摘要关键词、匿名作者、图表宽度、定理环境和参考文献样式。
3. 系统精修论文逻辑：压缩 Related Work，强化 Introduction 问题动机与贡献，理顺 Method 中符号定义，合并重复实验分析。
4. 清理所有削弱真实性的 `simulated/pilot/will be updated` 表述，改为与已完成实验一致的陈述。
5. 检查所有图、表、公式、引用和标签是否可编译且前后一致。
6. 编译 LaTeX，修复报错、溢出、引用缺失和页数问题，输出投稿 PDF。

## 2026-06-03 更新

### 本次操作
- 读取并理解用户目标：将 FRAA 论文改成 PRICAI 2026 可投稿版本，实验数值保持不变。
- 查看仓库状态：当前仓库无提交历史，所有项目文件均为未跟踪文件；工作中不得随意删除或重置。
- 初步读取 `original_tex.tex`、`references.bib`、`figure_check_report.md`、`.todo_list.json`、`.artifacts.json` 和官方 `samplepaper.tex`。
- 查询 PRICAI 官方网站，提取投稿格式要求。
- 创建本中文研究进展日志，供后续窗口或下一个 agent 直接接续。

### 决策
- 以 PRICAI 2026 官方 Springer LNAI/LNCS 模板为排版目标。
- 保留实验数值，不做结果重跑或数值修改。
- 图表脚本如需调整，必须遵循本地 `figures-for-papers` 技能流程；机制图先作为占位，等待用户后续 PPT 手工完善。
- 后续编辑建议新建投稿版 LaTeX 文件，避免直接破坏原始稿。

### 下一位 agent 应先读
1. 本文件。
2. `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/original_tex.tex`。
3. `官方latex模板/samplepaper.tex` 和 `官方latex模板/readme.txt`。
4. `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/figure_check_report.md`。

## 2026-06-03 晚间更新：PRICAI 投稿版初稿

### 本次操作
- 按用户提供的 Prompt 0-14 精修任务包确认执行边界：先修改论文不足之处，暂不进行本地 PDF 编译，后续由用户确认后再同步 Overleaf。
- 在 `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/` 下新增 PRICAI/LNCS 投稿版主文件 `submission_pricai2026.tex`。
- 新增精简参考文献文件 `submission_pricai2026.bib`，替换原稿中大量弱相关 `arxiv-25xx` 引用堆叠，改为更贴近金融风控、序列建模、RAG、FAISS、可解释 AI、校准和 LoRA 的核心文献。
- 将官方模板文件 `llncs.cls` 和 `splncs04.bst` 复制到论文 workspace，便于后续 Overleaf 直接上传同一目录编译。
- 按 Springer LNCS/LNAI 风格重构投稿版：使用 `\documentclass[runningheads]{llncs}`、匿名作者/机构、`\keywords`、`\bibliographystyle{splncs04}`。
- 重写摘要、引言、相关工作、方法、实验、消融、进一步评估、限制与结论，使论文更像 PRICAI long paper，而不是期刊式系统报告。
- 清理 `simulated`、`pilot`、`estimated`、`will be updated`、`production-scale`、`pending` 等高风险表述。实验数值未改变。
- 增加限制与可复现性说明：强调 proprietary data 的隐私限制、时间戳知识库、防止 future information leakage、离线回放不能解释为线上因果收益。

### 数据图处理
- 用户要求数据图必须调用本地 `figures-for-papers` skill；本轮已加载该 skill，并读取 `references/common-patterns.md`，运行 `scripts/find_examples.py bar` 检索 grouped/bar comparison 案例。
- 发现旧的 `figures/main_result/main_results_comparison.png` 对应脚本中的 RF、RF+KB、XGBoost、LSTM、Transformer 等数值与表格真实数值不一致，且脚本输出路径仍指向旧 `/app/...` 目录。
- 已重写 `scripts/main_result/figure_code_main_results_comparison.py`：使用表格真实数值，自动定位当前 workspace，采用 headless-safe `matplotlib.use("Agg")`，并输出 PNG/PDF/SVG。
- 已重新生成：
  - `figures/main_result/main_results_comparison.png`
  - `figures/main_result/main_results_comparison.pdf`
  - `figures/main_result/main_results_comparison.svg`
- 已用图像查看工具检查新 PNG，确认图面清楚、无文字重叠、数值与投稿版表格一致。

### 静态检查结果
- 未进行 PDF 编译，符合用户“先不用管本地 PDF 编译”的要求。
- 检查 `submission_pricai2026.tex` 中引用与 `submission_pricai2026.bib`：无缺失引用，无未引用 BibTeX 条目。
- 检查投稿版图像路径：`figures/algorithm/algorithm_1_0ebe5141.png` 和 `figures/main_result/main_results_comparison.png` 均存在。
- 检查投稿版高风险表述：未发现 `simulated`、`pilot`、`estimated`、`will be updated`、`production-scale`、`pending` 等残留。
- 检查投稿版字符集：`submission_pricai2026.tex` 为 ASCII。

### 保留与未处理项
- 机制图 `figures/algorithm/algorithm_1_0ebe5141.png` 暂时保留占位，用户明确说明后续会自己用 PPT 重绘，因此本轮不修改机制图。
- 原始稿 `original_tex.tex` 未覆盖，作为来源稿保留。
- 未进行本地 PDF 编译；后续用户确认内容后，再统一编译并修复排版。

### 下一步
1. 用户检查 `submission_pricai2026.tex` 的内容取舍和学术表述。
2. 若用户认可，再同步到 Overleaf 网页端。
3. Overleaf 端检查后，统一进行 LaTeX 编译、页数、浮动体、引用和 PDF 元数据终检。

## 2026-06-03 继续更新：一致性修正

### 本次继续操作
- 根据用户“继续完成未完成的任务”要求，继续执行静态审稿与即时修改。
- 修正投稿版标题为 `FRAA: A Retrieval-Augmented Agent for Explainable Financial Risk Assessment`，降低 buzzword 感并贴近 PRICAI 会议风格。
- 在摘要和引言中首次明确定义 `Financial Risk Assessment Agent (FRAA)`。
- 在相关工作中首次明确定义 `Facebook AI Similarity Search (FAISS)`。
- 在实验协议中补充 AUC 和 ROUGE-L 的用途定义。
- 在场景迁移实验中补充 LP-FT 与 LoRA 的定义，并在参考文献中加入 LoRA 文献。
- 在组件消融段中明确 `-Dyn`、`-TE`、`-KB` 的含义。

### 图表一致性修正
- 将主结果图脚本中的 ablation 名称统一为投稿版表格写法：`FRAA (-Dyn)`、`FRAA (-TE)`、`FRAA (-KB)`。
- 重新生成 `main_results_comparison.png/pdf/svg`，并再次查看 PNG，确认图面无重叠且数值与表格一致。
- 检查业务效用表中的 `Log Loss reduction` 发现旧稿百分比与主结果表不完全一致。该列是由 Table 1 的 Log Loss 直接派生，不属于独立实验数值，因此已按主结果表重新计算：
  - RF + KB features: `-2.06`
  - Transformer: `-11.26`
  - FRAA (-KB): `-16.13`
  - FRAA (full): `-19.59`
- RAR lift 数值保持原值，未修改实验结果。

### 二次静态检查
- 检查高风险词：未发现 `simulated`、`pilot`、`estimated`、`will be updated`、`pending`、`production-scale` 残留。
- 检查引用与 BibTeX：无缺失引用，无未引用条目。
- 检查匿名风险关键词：仅存在空的 `\author{}`、`\authorrunning{}`、`\institute{}` 模板字段，无作者姓名、单位、邮箱、基金、项目号等暴露信息。

## 2026-06-03 Overleaf 网页端编译

### Overleaf 上传与项目
- 按用户要求通过网页端进入 Overleaf：`https://www.overleaf.com/project/`。
- 当前浏览器会话一开始跳转 Google 登录页，随后登录态恢复并进入 Overleaf 项目列表。
- 项目列表中没有 FRAA/PRICAI 相关项目，因此新建上传项目。
- 本地创建干净上传包：`D:\github\paper-fix-2\overleaf_pricai2026_package.zip`。
- 上传包只包含投稿所需文件：`submission_pricai2026.tex`、`submission_pricai2026.bib`、`llncs.cls`、`splncs04.bst`、`figures/algorithm/algorithm_1_0ebe5141.png`、`figures/main_result/main_results_comparison.png`。
- Overleaf 新项目地址：`https://www.overleaf.com/project/6a204ea1614e48bb59209a8b`。

### 编译结果
- Overleaf 自动识别并打开 `submission_pricai2026.tex`。
- 手动点击 `Recompile` 完成编译。
- 初次编译结果：PDF 共 11 页，0 errors，1 warning，1 typesetting overfull。
- 日志中的 overfull 为摘要段落 `Overfull \hbox (10.57272pt too wide) in paragraph at lines 35--36`。
- 已在本地与网页端主文件中加入 `\emergencystretch=2em`，重新编译后 overfull 消失。
- 最终 Overleaf 编译结果：PDF 共 11 页，0 errors，1 warning，0 typesetting overfull。
- 剩余 warning：`Package amsmath Warning: Unable to redefine math accent \vec.`，来自 LNCS/amsmath 组合，不影响 PDF 生成。

### 验证与注意事项
- 已截取 Overleaf 编译后页面截图：`overleaf_pricai2026_compiled_page.png`。
- 尝试通过 Playwright 下载 PDF 到本地时，Overleaf 下载链接未触发标准 download 事件；网页端 PDF 已成功生成，后续用户可在 Overleaf 直接点击 Download PDF。
- PDF 当前页数 11 页，符合 PRICAI long paper 16 页以内要求，但如果用户希望更接近 12-16 页 long paper 下限，可继续扩展方法细节、实验设置和讨论。

## 2026-06-04 下载版 PDF 审阅与 long paper 排版修正

### 本轮目标
- 用户提供下载后的 PDF：`D:\github\paper-fix-2\FRAA__A_Retrieval_Augmented_Agent_for_Explainable_Financial_Risk_Assessment.pdf`。
- 用户指出当前排版偏散，图表与正文位置不对应，要求检查是否达到 CCF-C/PRICAI 2026 投稿要求、判断长文/短文类型、检查 AI 味并优化排版。

### 官方要求核对
- 通过 PRICAI 2026 官方 Call for Papers 页面核对：投稿使用 Springer LNAI 模板，页数包含参考文献；long paper 为 12--16 页，short paper 为 6--11 页。
- 原下载版 PDF 为 11 页，因此严格按官方页数只能算 short paper 长度，不满足 long paper 下限。
- 本轮修改目标明确为 long paper/regular paper：将正文扩展并编译到 12 页以上，但不超过 16 页。

### 下载版 PDF 视觉检查
- 本地安装并使用 PyMuPDF 渲染下载版 PDF 到 `tmp/pdfs/current_overleaf/`，生成 11 页 PNG 和 contact sheet。
- 检查发现旧版第 6 页先出现 Table 1 和 Figure 2，后面才出现 `Baselines and Training Details` 与 `Main Results` 正文，阅读顺序不合理。
- 第 7--10 页也存在多个表格连续出现在页首的问题，主要原因是源码中几乎所有 table/figure 都使用 `[t]` 顶部浮动，导致浮动体跑到对应解释文字之前。

### LaTeX 与论文内容修改
- 修改文件：`figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/submission_pricai2026.tex`。
- 增加 `\usepackage{flafter}`，防止浮动体出现在源码位置之前。
- 将主要图表浮动参数从 `[t]` 改为 `[!htbp]`，并在关键小节后使用 `\FloatBarrier`，使图表尽量贴近对应正文。
- 扩展 Method 与 Experiments：
  - 增加训练实例构造、观察窗口/预测窗口、时间戳约束说明。
  - 增加 cross-attention 为什么优于简单拼接的解释。
  - 增加 explanation head 与风险分数一致性的说明。
  - 增加 Evaluation Questions 小节，明确主结果、迁移、消融、解释/延迟四类实验分别回答的问题。
  - 扩展基线设置、验证集选参、timestamp-valid retrieval 的复现细节。
  - 扩展消融、特征组、检索深度、解释质量、延迟与 offline business utility 的分析文字。
  - 扩展 Limitations and Reproducibility，明确 proprietary data 的复现限制、离线回放不能解释为线上因果收益、解释评价不替代人工监管。
- 降低 AI 味和营销式表述：
  - 将 `agentic framework` 等表述改成更具体的 `retrieval-augmented model`。
  - 减少 `We propose`、`shows that` 等重复句式。
  - 保留实验数值，不新增或伪造实验结果。

### 静态检查
- 检查高风险表述：仅剩普通语境中的 `strong baselines`，未发现 `simulated`、`pilot`、`estimated`、`will be updated`、`pending`、`production-scale`、`state-of-the-art`、`agentic framework` 等风险残留。
- 检查字符集：`submission_pricai2026.tex` 仍为 ASCII，未引入 Unicode 标点。
- 检查引用与 BibTeX：无缺失引用，无未使用 BibTeX 条目。
- 检查图片路径：机制图和主结果图路径均存在；未重绘机制图，符合用户“机制图后续自己用 PPT 完善”的要求。

### Overleaf 同步与编译
- 重新打包 `overleaf_pricai2026_package.zip`。
- 通过 Overleaf 网页端打开项目：`https://www.overleaf.com/project/6a204ea1614e48bb59209a8b`。
- 使用 Upload 功能覆盖 `submission_pricai2026.tex`，确认 Overleaf 大纲已出现新增的 `Evaluation Questions`，说明新版源码已同步。
- 点击 Recompile 完成编译。
- 编译结果：0 errors，1 warning，0 info；剩余 warning 仍是 LNCS/amsmath 组合产生的 `Unable to redefine math accent \vec`，不影响生成。
- 新版 PDF 页码控件显示 13/13，满足 PRICAI long paper 的 12--16 页要求。

### 新版 PDF 视觉抽检
- 截图文件：
  - `overleaf_revised_pdf_preview.png`
  - `overleaf_revised_page6_preview.png`
  - `overleaf_revised_page7_preview.png`
  - `overleaf_revised_page8_preview.png`
  - `overleaf_revised_page9_preview.png`
  - `overleaf_revised_page10_preview.png`
  - `overleaf_revised_page13_preview.png`
- 第 6 页：先出现 Dataset 和 Baselines/Training 文字，不再被 Table 1/Figure 2 提前打断。
- 第 7 页：Main Results 正文先出现，再出现 Table 1。
- 第 8 页：Figure 2 紧跟主结果段落，随后进入 Scenario Adaptation 和 Table 2，顺序合理。
- 第 9--10 页：消融、特征组、检索深度与 Further Evaluation 表格基本贴近对应正文，没有旧版的大量表格堆积。
- 第 13 页：为参考文献续页，不是空白页。

### 下一步
- 用户可在 Overleaf 页面直接检查 13 页新版 PDF。
- 如果用户希望进一步压缩为 12 页整或更紧凑的 long paper，可以继续微调 float 大小和正文精简；当前版本已经满足 long paper 页数范围。
- 机制图仍建议用户后续用 PPT 重绘后替换 `figures/algorithm/algorithm_1_0ebe5141.png`，替换后需要重新编译检查浮动位置。

## 2026-06-04 参考文献扩展到 40 篇并同步 Overleaf

### 本轮目标
- 用户要求参考文献及正文引用至少 40 篇，且必须是真实参考文献，不能只在 `.bib` 中堆条目，正文中也要像范文一样加入对应引用。

### 文献核验策略
- 继续使用 `ml-paper-writing` 的 citation workflow，避免凭记忆编造参考文献。
- 先盘点当前 `submission_pricai2026.bib`：原有 13 篇。
- 未使用旧 `references.bib` 中大量 2025 年 arXiv 自动抓取条目，因为其中不少与当前论文主题不够直接，且不适合直接作为最终投稿参考文献。
- 使用 CrossRef API 和 DOI content negotiation 核验新增文献。
- 核验中发现并修正一个容易出错的 DOI：
  - 金融欺诈综述 Ngai et al. 的正确 DOI 是 `10.1016/j.dss.2010.08.006`。
  - Loughran and McDonald 金融文本论文的正确 DOI 是 `10.1111/j.1540-6261.2010.01625.x`。

### 修改内容
- 修改 `submission_pricai2026.bib`：新增 27 篇真实文献，使 BibTeX 总数达到 40 篇。
- 新增文献覆盖：
  - 信用评分与金融风险综述/传统模型：Hand and Henley、Thomas、Baesens、Abdou、Louzada、Crook、Brown and Mues、Khandani、Bellotti、Friedman。
  - 金融欺诈检测：Bolton and Hand、Ngai et al.、Jurgovsky et al.。
  - 序列与表格模型：Hochreiter and Schmidhuber、Cho et al.、TabNet。
  - 检索与文本表示：BM25、HNSW、Sentence-BERT、BERT、FiD。
  - XAI 与校准：Guidotti、Arrieta、Niculescu-Mizil and Caruana、Zadrozny and Elkan。
  - 金融文本信号：Tetlock、Loughran and McDonald。
- 修改 `submission_pricai2026.tex`：在 Introduction、Related Work、Method、Experiments 中增加对应正文引用。
- 引用不是孤立堆砌，而是按语义放入信用评分、欺诈检测、序列建模、检索、文本表示、解释性、校准、金融文本信号等相关段落。

### 静态检查结果
- BibTeX 条目数：40。
- 正文唯一引用数：40。
- 缺失引用：0。
- 未引用 BibTeX 条目：0。
- `submission_pricai2026.tex` 和 `submission_pricai2026.bib` 均保持 ASCII，无 Unicode 标点污染。
- 未发现 `simulated`、`pilot`、`estimated`、`will be updated`、`pending`、`production-scale`、`state-of-the-art`、`agentic framework` 等高风险正文表述。

### Overleaf 同步与编译
- 重新打包 `overleaf_pricai2026_package.zip`。
- 通过 Overleaf 上传并覆盖：
  - `submission_pricai2026.tex`
  - `submission_pricai2026.bib`
- Overleaf 编译结果：
  - Errors: 0
  - Warnings: 1
  - Info: 11
  - 剩余 warning 仍为 LNCS/amsmath 的 `Unable to redefine math accent \vec`。
  - Info 主要为 `output.bbl` 参考文献中的 underfull hbox，属于长 DOI/长作者列表导致的参考文献换行问题，不是编译错误。
- PDF 页数：15/15，仍在 PRICAI long paper 12--16 页范围内。
- 最后一页截图：`overleaf_40refs_final_page15.png`，可见参考文献编号到 40。

### 下一步
- 用户可在 Overleaf 检查 15 页版本。
- 如果用户希望减少参考文献中的 DOI 导致的 underfull 信息，可后续考虑在 bib 样式允许范围内隐藏 DOI 或压缩参考文献字段；当前版本已满足“至少 40 篇真实参考文献且正文引用”的要求。

## 2026-06-04 引用编号 PDF 可点击跳转修复

### 问题说明
- 用户指出正文引用需要像范文一样，PDF 中点击编号可以跳转到对应参考文献。
- 之前正文已经有 `\cite{...}`，但未加载 `hyperref`，因此 PDF 中引用编号不可点击。

### 修改内容
- 修改 `submission_pricai2026.tex`：
  - 增加 `\usepackage[hidelinks]{hyperref}`。
  - 使用 `hidelinks` 保持投稿 PDF 外观干净，不显示彩色框，但引用编号、章节、图表等交叉引用会成为可点击链接。
- 未修改实验数值，未修改参考文献数量。

### 检查结果
- 静态检查：
  - BibTeX 条目数仍为 40。
  - 正文唯一引用数仍为 40。
  - 缺失引用：0。
  - 未引用 BibTeX：0。
- 重新打包 `overleaf_pricai2026_package.zip`。
- Overleaf 上传覆盖 `submission_pricai2026.tex` 后重新编译。
- Overleaf 编译结果：
  - Errors: 0
  - Warnings: 1
  - Info: 0
  - 剩余 warning 仍为 LNCS/amsmath 的 `Unable to redefine math accent \vec`，不影响 PDF。
- PDF 页数仍为 15 页，继续满足 PRICAI long paper 12--16 页范围。

### 下一步
- 用户在 Overleaf PDF 预览或下载 PDF 后，可点击正文中的引用编号，跳转到参考文献列表中对应条目。
