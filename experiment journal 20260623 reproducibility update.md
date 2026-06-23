# 研究进展日志 20260623 可复现性段落修改

## 总体研究进展

项目目标是将 FRAA 论文整理为 PRICAI 2026 / Springer LNCS 投稿版本。当前主线应聚焦于时间有效检索、时间行为建模、校准风险预测和可审计解释。投稿前的策略是保留强实验链条，删除或弱化容易引发审稿质疑的业务收益、训练动态和低边际补充表格。

## 2026-06-23 更新

### 修改原因

用户明确要求：可复现性问题不要写成“数据不可公开/数据来源”这类会放大短板的表述，而是通过补充实验协议细节来增强可信度。目标是服务中稿概率，让审稿人看到协议清晰、可审计、无测试集泄漏。

### 已完成修改

1. 重写 `Limitations and Reproducibility` 小节。
   - 删除 `raw data cannot be released publicly`、`direct reproduction`、`public benchmarks where legally possible` 等短板放大表述。
   - 改为强调协议细节：30-day prediction horizon、strict chronological split、validation-month hyperparameter selection、120-day behavioral window、timestamp-filtered retrieval、fixed retrieval depth `K=5`、calibration/ranking metrics。
   - 明确 no test-set labels are used for checkpoint selection，retrieval candidates are timestamp-filtered at scoring time。
   - 将未来工作写成 repeated temporal splits、multi-seed training runs、institution-level transfer tests，用“稳定性量化”替代“数据不可公开”。
2. 同步修改 Conclusion 中的限制句。
   - 删除 `limited to one proprietary financial environment` 和 `public benchmarks where legally possible`。
   - 改为 future work should test repeated temporal splits, multi-seed training runs, and institution-level transfer to quantify stability under distribution shift。
3. 同步文件。
   - `figure_workspace_0ee7a6fe-ccd3-4659-a621-c986942de0c7/submission_pricai2026.tex`
   - `overleaf_pricai2026_package/submission_pricai2026.tex`

### 验证结果

- 主 TeX 与 Overleaf 包 TeX 已再次验证字节一致。
- 未检出以下短板放大表述：`cannot be released`、`raw data cannot`、`public benchmarks`、`public or multi-institution`、`direct reproduction`、`legally possible`。
- RAR/revenue 风险词仍未恢复：`estimated 10.45`、`risk-adjusted revenue`、`revenue lift`。

### 下一步

在 Overleaf 重新编译，确认最终页数和浮动位置。若仍超页或接近 16 页满版，优先压缩 Scenario Adaptation 或 Conclusion，不恢复可复现性短板表述。
