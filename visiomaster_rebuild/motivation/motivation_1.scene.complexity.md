# Visiomaster Complexity Report: FRAA Motivation Figure

## Summary
- Style profile: `clean_white`
- Page: 12.00 x 9.60 in, aspect 1.25
- Visible semantic nodes: 34
- Edges: 19
- Regions: 0
- Region-covered visible nodes: 0/34
- Cross-region edges: 0
- Region plan entries: 0
- Validation warnings: 55
- Validation errors: 0

## Source Region Plan
- Not in exact reconstruction mode.

## Recommended Build Mode
- Use `region_first` or `tiled_subscenes`: rebuild each logical module/crop, validate it, then assemble the full-page scene.
- Add invisible `audit_region` boxes for source areas that do not have visible dashed frames.
- Freeze shared style tokens before assembly: body font, small label font, operator font, frame title font, and arrow weight.

## Region Load
- No regions found.
- Uncovered visible nodes: `left_bg`, `right_bg`, `title_left`, `title_right`, `divider`, `vs_circle`, `tree_root`, `tree_a`, `tree_b`, `tree_c`, `tree_d`, `tree_e` ...

## Font Scale
- `ellipse_node`: 15.0-36.0 pt across 3 nodes
- `polygon_node`: 13.0-13.0 pt across 1 nodes
- `process_box`: 16.0-16.0 pt across 9 nodes
- `rounded_process`: 13.0-21.0 pt across 14 nodes
- `text_block`: 18.0-64.0 pt across 7 nodes

## Text Fit Risks
- `title_left` 3.17x0.46 in estimated vs 2.98x0.37 in
- `title_right` 2.54x0.46 in estimated vs 2.98x0.37 in
- `manual_features` 1.20x0.66 in estimated vs 1.18x0.46 in
- `failure_x` 0.48x1.05 in estimated vs 0.67x0.67 in
- `question_icon` 0.18x0.39 in estimated vs 0.29x0.29 in
- `knowledge_label` 1.15x0.59 in estimated vs 1.14x0.46 in
- `fusion_label` 2.90x0.36 in estimated vs 2.30x0.29 in
- `reasoning` 2.44x0.59 in estimated vs 1.57x1.71 in
- `agent` 1.50x0.69 in estimated vs 1.24x1.83 in

## Dense Region Risks
- No region exceeds the default density threshold.

## Paper Detail Grammar Risks
- No compact paper-detail primitives found; if the source has matrices, small operators, ports, or formulas, scene grammar is likely too coarse.
- Long explicit path `bus_vertical` length=3.83 in; check for missing bus/junction/boundary port.

## Validation Snapshot
- WARN: Junction point `source_bus` is larger than usual; keep merge/fan points tiny.
- WARN: Node `title_left` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `title_right` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `manual_features` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `failure_x` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `no_interp` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `question_icon` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `isolated_label` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `knowledge_label` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `fusion_label` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `reasoning` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `transformer` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Node `agent` text is likely to wrap or overflow; set `text_fit: "shrink_to_fit"` or use `math_text`/smaller role-specific font.
- WARN: Complex scene has 34 visible nodes and 19 edges; set metadata.region_strategy to `region_first`, `tiled_subscenes`, or `module_first`, then build/review the figure module-by-module before whole-page assembly.
- WARN: Complex scene has only 0 group/audit regions; add roughly 3 logical `audit_region`/`group_container` areas so large figures are reviewed as smaller subscenes instead of one global layout.
- WARN: Only 0/34 visible nodes are assigned to a region. For large diagrams, bind nodes with explicit `container_id` or add invisible `audit_region` boxes.
- WARN: Font sizes for `rounded_process` vary from 13.0pt to 21.0pt (small: src_transactions, explain_bubble; large: agent). Large figures should keep each component family on a small role-based font scale.
- WARN: Font sizes for `text_block` vary from 18.0pt to 64.0pt (small: knowledge_label; large: failure_x). Large figures should keep each component family on a small role-based font scale.
- WARN: Text in node `title_left` may not fit (3.17x0.46 in estimated vs 2.98x0.37 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `title_right` may not fit (2.54x0.46 in estimated vs 2.98x0.37 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `manual_features` may not fit (1.20x0.66 in estimated vs 1.18x0.46 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `failure_x` may not fit (0.48x1.05 in estimated vs 0.67x0.67 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `question_icon` may not fit (0.18x0.39 in estimated vs 0.29x0.29 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- WARN: Text in node `knowledge_label` may not fit (1.15x0.59 in estimated vs 1.14x0.46 in available). Wrap text, enlarge the node, or assign a smaller role font before rendering.
- Additional validation items suppressed; run `scene_validate.py` for the full list.

