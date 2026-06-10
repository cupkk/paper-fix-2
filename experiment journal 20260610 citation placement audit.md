# 研究进展日志 20260610：引用位置复核

## 一、触发原因

用户质疑上一轮参考文献是否“随便引用”。该问题涉及学术诚信和投稿可靠性，因此本轮对正文引用位置做了逐句复核。

## 二、复核方法

- 读取当前主 TeX：
  - `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.tex`
- 读取当前 BibTeX：
  - `D:\github\paper-fix-2\figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7\submission_pricai2026.bib`
- 抽取每个含 `\cite{}` 的句子。
- 对照每个 citation key 的 BibTeX title 和 DOI 字段，检查引用主题是否支持所在句子的论点。
- 本轮没有新增任何参考文献，也没有从记忆或模型知识生成新的 BibTeX。

## 三、复核结论

当前引用不是随机插入。主要对应关系如下：

- 信用评分、消费者信贷、风险评估综述：
  - `hand1997statistical`
  - `thomas2000survey`
  - `crook2007recent`
  - `baesens2003benchmarking`
  - `abdou2011credit`
  - `louzada2016classification`
- 欺诈检测、合规监测、金融风险工作流：
  - `bolton2002statistical`
  - `ngai2011application`
  - `khandani2010consumer`
  - `bellotti2009support`
  - `brown2012experimental`
- 树模型与表格建模基线：
  - `breiman2001random`
  - `friedman2001greedy`
  - `chen2016xgboost`
  - `lessmann2015benchmarking`
  - `arik2021tabnet`
- 序列建模与 Transformer：
  - `hochreiter1997lstm`
  - `cho2014learning`
  - `vaswani2017attention`
  - `kang2018sasrec`
  - `sun2019bert4rec`
  - `jurgovsky2018sequence`
- 检索增强、RAG、向量检索：
  - `robertson2009probabilistic`
  - `karpukhin2020dpr`
  - `lewis2020rag`
  - `izacard2021leveraging`
  - `devlin2019bert`
  - `reimers2019sentence`
  - `malkov2020hnsw`
  - `johnson2019billion`
- 可解释性与校准：
  - `ribeiro2016lime`
  - `lundberg2017shap`
  - `guidotti2018survey`
  - `arrieta2020explainable`
  - `guo2017calibration`
  - `niculescu2005predicting`
  - `zadrozny2002transforming`
- 金融文本、新闻情绪、监管文本：
  - `tetlock2007giving`
  - `loughran2011liability`
- 参数高效迁移的未来工作引用：
  - `hu2022lora`

## 四、需要说明的边界

- 本轮复核确认的是“引用位置与文献主题是否匹配”，不是重新联网逐条 DOI 核验。
- 当前仓库中已有 `reference_verification_20260604.json`，说明此前做过参考文献核查记录，但该文件中部分条目的 DOI 字段为空或自动检索结果不完整。
- 因此后续若要做最终投稿前的学术诚信审计，建议再单独执行一次完整 DOI/URL 联网核验，并把核验结果固化为最终审计表。

