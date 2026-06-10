# experiment journal 20260610 figure table consistency

## 第 4 章节及全文图表数据一致性检查

### 本次触发

用户要求检查第 4 章节图片和表格的数据是否一致，并说明绘图代码都在压缩包中；重点判断全文是否使用同一组数据，或图表是否在展示不同数据。

### 检查范围

- 主文本：
  - `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/original_tex.tex`
- 第 4 节对应绘图脚本：
  - `scripts/main_result/figure_code_main_results_comparison.py`
  - `scripts/main_result/figure_code_product_adaptation_lifts.py`
  - `scripts/main_result/figure_code_business_impact_scatter.py`
  - `scripts/main_result/figure_code_feature_importance_occlusion.py`
  - `scripts/main_result/figure_code_context_window_sensitivity.py`
  - `scripts/main_result/figure_code_retrieval_depth_sensitivity.py`
- 横向复核第 5 节同类脚本：
  - `scripts/ablation/figure_code_architectural_component_ablation.py`
  - `scripts/ablation/figure_code_feature_group_importance.py`
  - `scripts/ablation/figure_code_incremental_feature_addition.py`
  - `scripts/ablation/figure_code_retrieval_depth_sensitivity.py`

### 第 4 节结论

- `main_results_comparison`：图代码与表 1 数据一致。
- `product_adaptation_lifts`：图代码与表 2 数据不一致。除完整 FT 的 R@1 外，多数组值不同，R@5 也不同。
- `business_impact_scatter`：图代码与表 3 数据不一致。只有完整 FRAA 的 `-19.57/+10.45` 一致，其他模型为近似/合成值。
- `feature_importance_occlusion`：图代码与表 4 数据一致。
- `context_window_sensitivity`：图代码与表 5 在 30/120/180 天一致，但 60/90 天不一致；脚本注释称 60/90 为插值值，而表格给出了具体数值。
- `retrieval_depth_sensitivity`：第 4 节该图没有相邻表格，但与第 5 节检索深度表和 caption 不一致；脚本使用 `K=[1,3,5,7,9]` 和 `Log Loss=[0.45,0.38,0.35,0.37,0.40]`、`Recall=[0.62,0.72,0.78,0.75,0.71]`，而表格使用 `K=[1,3,5,7,10]` 和 `0.5287/0.5214/0.5163/0.5175/0.5189`、`0.4068/0.4117/0.4185/0.4173/0.4160`。

### 全文横向结论

- 第 5 节 `architectural_component_ablation.py` 与其表格不一致，脚本使用了明显不同的 Transformer、-KB、-TE、-Dyn 数值。
- 第 5 节 `feature_group_importance.py` 与表格一致。
- 第 5 节 `incremental_feature_addition.py` 与表格完全不一致，脚本使用 `0.450/0.320/0.302/0.285` 和 `0.550/0.720/0.755/0.780`，表格使用 `0.5412/0.5275/0.5198/0.5163` 和 `0.3971/0.4083/0.4146/0.4185`。
- 第 5 节 `retrieval_depth_sensitivity.py` 与表格不一致，虽然 K 列一致，但数值不同。

### 判断

- 当前论文不是全文统一使用同一个数据源生成图表。
- 有些图像可能原本是“趋势示意图”或“合成图”，但正文、表格和 caption 没有明确说明它们是不同数据或示意数据。
- 因为 caption 和正文直接引用具体实验数值，读者会默认图和表展示同一实验结果。因此这些不一致应视为需要修复的问题，而不是可接受的“不同数据展示”。

### 后续建议

- 以 LaTeX 表格中的数值作为主数据源，统一修改绘图脚本并重新生成图片。
- 或者反过来以脚本为主数据源，统一改表格和正文数值；但这会影响更多论文叙述，不建议。
- 对第 4 节优先修复：
  - `product_adaptation_lifts.py`
  - `business_impact_scatter.py`
  - `context_window_sensitivity.py`
  - `retrieval_depth_sensitivity.py`
- 对全文一致性再修复：
  - `architectural_component_ablation.py`
  - `incremental_feature_addition.py`
  - `ablation/retrieval_depth_sensitivity.py`
