# needs-review.md — 来源/条件/测试缺口（不编译为 active 能力依据）

| nr_id | 缺口 | 影响能力 | 处理 |
|---|---|---|---|
| nr-01 | 全书时段标 EST/纽约时间，未说明夏令时(EDT)处理与 UTC 换算 | cap-01, cap-13, cap-09 | 能力统一按"纽约本地时间（America/New_York）"解释并在 B 显式声明；原书口径缺口如实标注 |
| nr-02 | LRLR/HRLR 无量化度量 | cap-03 | 只做定性标注，不做评分；不凭文字补阈值 |
| nr-03 | Displacement/"energetic"/"强脉冲"无量化阈值 | cap-05, cap-07 | 采用可计算代理（收盘越位+留下 FVG）；阶段 4 实测代理边界 |
| nr-04 | FVG 最小宽度未定义 | cap-06 | 输出原始区间不过滤 |
| nr-05 | 全部点数参数仅 ES/SP500 标定，跨品种无换算 | cap-08, cap-09, cap-10 | B 声明品种限定；非 ES 输入时能力降级为"仅结构判定" |
| nr-06 | NY Scalp Fib 目标 1&2 数值原文未给 | cap-09 | 目标语义="重测日高/前日高"，不编数值 |
| nr-07 | Ch32 清单条件是 AND 还是加权组合原文未明 | cap-08 | 按"硬门+计数增信"实现并在 B 说明 |
| nr-08 | SMT 比对时间框架未规定 | cap-14 | 要求调用方指定 TF 并记录 |
| nr-09 | ~~Ch18 禁忌日细则仅摘要级~~ | cap-01 | ✅ 已解决（2026-10-21）：Ch18 p.399-405 逐页细读，完整清单并入 cap-01 补章节 |
| nr-10 | ~~结构层级在试点外 Ch15~~ | cap-05 | ✅ 已解决（2026-10-21）：Ch15 p.301-331 逐页细读，新增 cap.ict2022.market-structure-hierarchy（图 p.319 reviewed），cap-05 补章节联读 |
| nr-11 | 图表证据：45 页已渲染、8 页 reviewed（新增 nwog-p0494/structure-p0319/mmxm-p0427/mmxm-p0441），其余 prepared-unreviewed | 各图文依赖能力 | 新卡按依赖逐张核查后再标 reviewed；未核图不进入 visual_evidence |

## 补章新增缺口（2026-10-21）

| nr_id | 缺口 | 影响能力 | 处理 |
|---|---|---|---|
| nr-12 | 交易者类型→TF 组合表仅在图中（Ch15 p.315-316 未核） | top-down-workflow | 标缺口不编；如需则渲染核图后补 |
| nr-13 | Reversal 模板 4-5am/7-8am 未标时区（推测 EST） | daily-templates-playbook | 卡内已标注推测与缺口 |
| nr-14 | NDOG 5PM/6PM 时区原文未标（图 p.494 给出周五 17:00/周日 18:00 NY 为 NWOG 口径） | nwog-ndog-anchors | 输出按纽约口径并声明来源页；经纪商差异未覆盖 |
| nr-15 | 假期周的 Monday Range 处理原文未给 | monday-range-procedure | 卡内标缺口 |
| nr-16 | Ch14 p.282 Opening Range 公式字面 "Projection=Open+HOD" 量纲不通（疑排版/翻译失真） | opening-range-cpe | 按 "1:1 deviation below" 对称语义实现（Range=HOD−Open，下方目标=Open−Range），卡内标注实现约定；不改原书表述 |
