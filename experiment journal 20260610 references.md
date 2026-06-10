# experiment journal 20260610 references

## 参考文献检索与可用性核验

### 本次触发

用户询问 `original_tex.tex` / `references.bib` 中的 arXiv 参考文献是否都不能使用，并指出 arXiv 文献本身也可以引用，要求检索核验。

### 检索对象

- 文件：
  - `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/original_tex.tex`
  - `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/references.bib`
  - `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/submission_pricai2026.bib`
- 从 `original_tex.tex` 抽取到 72 个 `arxiv-xxxx.xxxxx` 引用键，另有 `johnson2019billion`。

### 核验方法

- 使用 arXiv 官方 API 批量查询：
  - `https://export.arxiv.org/api/query?id_list=...&start=0&max_results=25`
- 第一次查询未加 `max_results`，因默认分页只返回部分结果，出现误判缺失。
- 第二次加 `max_results=25` 分批查询后，72 个 arXiv ID 全部可查。

### 核验结果

- `references.bib` 中 72 个 arXiv ID 均真实存在。
- 其中 70 条题名与 arXiv 当前题名一致。
- 2 条题名不一致，需要修正或重新核对：
  - `2511.11132`
    - `.bib` 题名：`Hindsight Distillation Reasoning with Knowledge Encouragement Preference for Knowledge-based Visual Question Answering`
    - arXiv 当前题名：`From Hindsight to Foresight: Self-Encouraged Hindsight Distillation for Knowledge-based Visual Question Answering`
  - `2511.17655`
    - `.bib` 题名：`Explainable Deep Learning for Brain Tumor Classification: Comprehensive Benchmarking with Dual Interpretability and Lightweight Deployment`
    - arXiv 当前题名：`Intelligent Systems in Neuroimaging: Pioneering AI Techniques for Brain Tumor Detection`

### 判断

- 不能说原始 arXiv 参考文献“都不能用”。它们多数真实存在，arXiv 预印本在计算机科学论文中可以被引用。
- 但当前 `references.bib` 的核心问题不是“查不到”，而是“主题相关性弱、放置位置不匹配、像自动堆砌引用”。
- 大量条目来自医学影像、脑科学、机器人、材料、网络安全、智能合约、通用 agent 安全等方向，不能支撑金融风险评估、信用风险、金融推荐、RAG 金融知识检索等具体论断。
- 可保留的方向应优先包括：
  - 金融服务推荐/个性化：如 `arxiv-2511.14865` FinTRec。
  - RAG / KG-RAG / 检索增强推理：如 `arxiv-2510.15552`、`arxiv-2511.01059`、`arxiv-2511.04700` 等。
  - 时间序列/长程依赖：如 `arxiv-2512.05442`、`arxiv-2510.25800`、`arxiv-2511.23260` 等，需要谨慎放在合适段落。
  - Agentic AI 背景：只可作为一般背景，不应替代金融风险或金融推荐实证文献。
- 更稳妥的稿件应以 `submission_pricai2026.bib` 中的经典正式出版文献和 DOI 文献为主，再补少量高度相关的 arXiv 预印本。

### 后续建议

- 不应整批删除所有 arXiv 条目。
- 应建立一个引用筛选表：保留、替换、删除、需修正题名。
- 对正文中的每一处 `\cite{...}` 检查其支撑的具体句子，删除主题错配的引用。
- 对保留的 arXiv 条目补全 `eprint`、`archivePrefix`、`primaryClass`、`url`，并优先查找是否已有正式会议/期刊版本。
