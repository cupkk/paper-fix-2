# Visiomaster Complexity Report: FRAA Algorithm Pipeline

## Summary
- Style profile: `paper_white`
- Page: 13.20 x 7.24 in, aspect 1.82
- Visible semantic nodes: 22
- Edges: 32
- Regions: 0
- Region-covered visible nodes: 0/22
- Cross-region edges: 0
- Region plan entries: 0
- Validation warnings: 67
- Validation errors: 0

## Source Region Plan
- Not in exact reconstruction mode.

## Recommended Build Mode
- Whole-scene authoring is acceptable, but still run module audit before final Visio render.

## Region Load
- No regions found.
- Uncovered visible nodes: `stage1_num`, `stage1_title`, `stage2_num`, `stage2_title`, `stage3_num_a`, `stage3_num_b`, `stage3_title`, `sep1`, `sep2`, `input_dynamic`, `input_profile`, `input_knowledge` ...

## Font Scale
- `ellipse_node`: 15.0-20.0 pt across 5 nodes
- `legend_block`: 14.0-14.0 pt across 1 nodes
- `process_box`: 16.0-16.0 pt across 2 nodes
- `rounded_process`: 18.0-24.0 pt across 9 nodes
- `text_block`: 15.0-20.0 pt across 4 nodes

## Text Fit Risks
- `stage1_num` 0.15x0.33 in estimated vs 0.20x0.20 in
- `stage1_title` 2.64x0.33 in estimated vs 2.32x0.17 in
- `stage2_num` 0.15x0.33 in estimated vs 0.20x0.20 in
- `stage2_title` 4.77x0.33 in estimated vs 3.25x0.17 in
- `stage3_num_a` 0.15x0.33 in estimated vs 0.20x0.20 in
- `stage3_num_b` 0.15x0.33 in estimated vs 0.20x0.20 in
- `stage3_title` 2.94x0.33 in estimated vs 2.24x0.17 in
- `fusion` 1.89x1.08 in estimated vs 1.54x2.07 in
- `knowledge_base` 2.87x0.59 in estimated vs 2.41x0.84 in
- `feedback_label` 2.10x0.49 in estimated vs 1.54x0.41 in

## Dense Region Risks
- No region exceeds the default density threshold.

## Paper Detail Grammar Risks
- No compact paper-detail primitives found; if the source has matrices, small operators, ports, or formulas, scene grammar is likely too coarse.
- Long explicit path `grid_h1` length=13.20 in; check for missing bus/junction/boundary port.
- Long explicit path `grid_h2` length=13.20 in; check for missing bus/junction/boundary port.
- Long explicit path `grid_h3` length=13.20 in; check for missing bus/junction/boundary port.
- Long explicit path `grid_h4` length=13.20 in; check for missing bus/junction/boundary port.
- Long explicit path `grid_h5` length=13.20 in; check for missing bus/junction/boundary port.
- Long explicit path `grid_h6` length=13.20 in; check for missing bus/junction/boundary port.
- Long explicit path `grid_h7` length=13.20 in; check for missing bus/junction/boundary port.
- Long explicit path `grid_h8` length=13.20 in; check for missing bus/junction/boundary port.

## Validation Snapshot
- WARN: Node `sep1` is an ultra-thin `process_box` with no text; use `bracket` or an edge/connector instead of a fake line box.
- WARN: Node `sep1` is an empty dashed `process_box`; use `dashed_region` or `group_container` for visible annotation frames.
- WARN: Node `sep2` is an ultra-thin `process_box` with no text; use `bracket` or an edge/connector instead of a fake line box.
- WARN: Node `sep2` is an empty dashed `process_box`; use `dashed_region` or `group_container` for visible annotation frames.
- WARN: Node `stage1_num` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `stage2_num` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `stage3_num_a` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `stage3_num_b` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `input_dynamic` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `input_knowledge` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `fusion` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `explain_head` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `reasoning` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `knowledge_base` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `legend` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Font sizes for `ellipse_node` vary from 15.0pt to 20.0pt (small: wave_circle; large: stage1_num, stage2_num, stage3_num_a). Large figures should keep each component family on a small role-based font scale.
- WARN: Font sizes for `rounded_process` vary from 18.0pt to 24.0pt (small: reasoning, knowledge_base; large: encoder). Large figures should keep each component family on a small role-based font scale.
- WARN: Font sizes for `text_block` vary from 15.0pt to 20.0pt (small: feedback_label; large: stage1_title, stage2_title, stage3_title). Large figures should keep each component family on a small role-based font scale.
- WARN: Text in node `stage1_num` may not fit (0.15x0.33 in estimated vs 0.20x0.20 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `stage1_title` may not fit (2.64x0.33 in estimated vs 2.32x0.17 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `stage2_num` may not fit (0.15x0.33 in estimated vs 0.20x0.20 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `stage2_title` may not fit (4.77x0.33 in estimated vs 3.25x0.17 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `stage3_num_a` may not fit (0.15x0.33 in estimated vs 0.20x0.20 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `stage3_num_b` may not fit (0.15x0.33 in estimated vs 0.20x0.20 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- Additional validation items suppressed; run `scene_validate.py` for the full list.

