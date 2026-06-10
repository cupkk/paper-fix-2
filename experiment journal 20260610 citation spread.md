# 研究进展日志 20260610：参考文献引用分散优化

## 一、整体研究进展概览

- 项目目标：将 FRAA 论文整理为符合 PRICAI 2026 / LNCS 投稿模板要求的可投稿版本，同时保持真实实验数据、真实参考文献和官方模板排版不被破坏。
- 当前主线：论文已完成章节结构调整、图表同步、流程图替换、Overleaf 编译验证。本轮根据用户要求，优化正文引用分布，避免单个位置堆叠过多参考文献。
- 本轮原则：不新增参考文献，不从记忆编造 BibTeX，不改动参考文献条目信息，只使用当前 `.bib` 中已有且此前已核查的 40 条文献。

## 二、2026-06-10 本轮操作记录

### 1. 用户要求

用户指出：

- 参考文献应尽量分散标注。
- 一个引用位置最多标 2 篇。
- 参考文献必须真实。

### 2. 初始问题

扫描主 TeX 后发现，Introduction 和 Related Work 中存在多个引用聚集点：

- 单个 `\cite{}` 中一次放入 4、5、6、7、9 篇文献。
- 部分句子虽然可以拆成多个 `\cite{}`，但同一句仍累计 3 篇以上引用。

这些写法容易显得像机械堆文献，不利于会议论文的自然行文。

### 3. 修改策略

本轮采取保守修改：

- 不新增任何 BibTeX 条目。
- 不删除已有参考文献。
- 将大簇引用拆散到不同句子和不同论点中。
- 每个 `\cite{}` 最多保留 2 个 key。
- 进一步检查句子级引用密度，避免同一句累计超过 2 篇。
- 将参考文献与具体论点对应，例如：
  - 信用评分与消费者信贷：`hand1997statistical`、`thomas2000survey`
  - 欺诈检测与合规工作流：`bolton2002statistical`、`ngai2011application`
  - 随机森林：`breiman2001random`
  - 梯度提升与 XGBoost：`friedman2001greedy`、`chen2016xgboost`
  - RAG 与 dense retrieval：`karpukhin2020dpr`、`lewis2020rag`
  - XAI 与 calibration：按解释方法、综述、校准方法分别分散引用

### 4. 修改文件

同步修改了：

- `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- `D:\github\paper-fix-2\overleaf_pricai2026_package\submission_pricai2026.tex`

修改后两个 TeX 文件 SHA-256 一致：

- `501DF62E7CD4451F85E23DEB069C172F793315308DA29F297D7FBF4FF25201F6`

### 5. 静态引用检查结果

脚本检查结果：

- `cite_commands = 43`
- `unique_cited = 40`
- `bib_entries = 40`
- `max_keys_per_cite = 2`
- `cite_command_violations = 0`
- `sentence_violations = 0`
- `missing = []`
- `unused = []`

结论：

- 每个引用命令最多 2 篇。
- 每个句子也没有超过 2 篇文献的累计引用。
- 40 条 BibTeX 均仍被正文引用。
- 正文没有引用不存在的 key。

### 6. Overleaf 同步与编译

- 已重新生成：
  - `D:\github\paper-fix-2\overleaf_pricai2026_package.zip`
- 已将修改后的 `submission_pricai2026.tex` 同步到 Overleaf 项目：
  - `https://www.overleaf.com/project/6a204ea1614e48bb59209a8b`
- Overleaf 编译日志：
  - Errors：0
  - Warnings：1
  - Info：1
- Warning：
  - `Package amsmath Warning: Unable to redefine math accent \vec.`
- Info：
  - `Underfull \vbox`
- 以上均为非致命提示，不影响 PDF 输出。

### 7. PDF 输出与验证

- 最新网页端 PDF：
  - `D:\github\paper-fix-2\overleaf_after_citation_spread_output_full.pdf`
- PDF 大小：
  - `2,114,271 bytes`
- PDF 页数：
  - 15 页
- 文本验证：
  - `Introduction`、`Related Work`、`Methodology`、`Experiments`、`Conclusion`、`References` 均存在。
  - PDF 首页 Introduction 中可见拆散后的引用形式，例如 `[16,38]`、`[6,31]`、`[11]`、`[7]`，说明 Overleaf 已使用新正文。

## 三、当前判断

- 本轮“参考文献分散标注、单个位置最多 2 篇”的要求已完成。
- 没有新增未核验文献。
- 参考文献仍保持 40 条，且全部被正文引用。
- Overleaf 已同步并编译成功。

