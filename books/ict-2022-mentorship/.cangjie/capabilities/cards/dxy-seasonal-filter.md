# DXY 联动与季节性过滤器（DXY Correlation & Seasonal Filter）

## R — Reading (原文)

> DXY-指数三场景：①DXY 跌→ES/NQ/YM 涨；②DXY 涨→ES/NQ/YM 跌；③DXY 盘整→ES/NQ/YM 涨。例外："There are also times when the S&P 500 and the US dollar both move up together"（经济复苏期）（p.386–387）。
> 季节性（作者明示 not absolute / not guarantees / not a panacea）：通用 Dec–Jan 盘整不利、Feb–Apr 高概率模型期、May–Aug 夏季萧条、Sep–Nov 再启动；EURUSD/GBPUSD/DXY 各自月度转折结构（2 月中筑底→3 月中走高→…；DXY 年初–2 月中上行→2 月中顶→3 月中跌→…→12 月下旬熊）（p.389–398）。

出处：Ch17 PDF p.383–398。

## I — Interpretation (自述)

一个"先验加权"过滤器而非信号源：用 DXY 与指数的三场景联动给当日偏向加一个跨市场确认/冲突标记，用月度季节结构给周度偏向加一个先验权重。两者都被作者自己声明为非保证，因此能力的输出永远是"确认/冲突/中性 + 原文月份结构"，绝不单独产生交易结论；冲突时明确提示例外情形（复苏期同涨）。

## A1 — Application Example

原书案例：Ch17 p.387 三场景四图与 p.390–397 季节性叠加图（【图 prepared-unreviewed】）。无统计样本量与起止年份（作者未给）。

## A2 — Future Trigger

情境：周度/月度规划问"这个季节对 ES/欧元偏多还是偏空"；问"DXY 现在盘整对指数意味什么"；为偏向清单加跨市场确认。
语言信号：DXY / 美元指数 / 季节性 / seasonal / 月份规律 / risk on off / 跨市场 / intermarket。
区分：只做先验与确认标记；当日偏向→ daily-bias-checklist；SMT 裂缝→ smt-divergence-confirm。

## E — Execution

输入契约：DXY 当前状态（涨/跌/盘整，调用方提供或说明缺）、品种、当前月份。
1. 三场景匹配→输出联动预期与例外提示（同涨可能=复苏期）。
2. 月份结构查表：输出该品种（ES 通用/EURUSD/GBPUSD/DXY）当月原文结构与转折点。
3. 与调用方既有偏向比对→确认/冲突/中性标记。
4. 输出：{联动预期, 月份结构, 确认标记, 免责声明：非保证}。
判停：DXY 状态缺→仅输出月份结构并标注缺输入。

## B — Boundary

- 作者三重免责（not absolute/guarantees/panacea）必须随输出呈现。
- 季节性数据无起止年份与更新频率（时效风险）。
- 10 月后 EURUSD/DXY 均值背离、信号不可靠（作者明示）。
- 不单独产生交易结论；不用于加密等非覆盖品种。
