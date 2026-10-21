# Opening Range 投影与 CPE（Opening Range & Close Proximity Entries）

## R — Reading (原文)

> Opening Range Projection = Open + HOD；Opening Range = Projection − Opening Price；该区间定义开盘价下方允许的偏离幅度，"We want to see 1:1 deviation below"（p.282–283）。
> CPE：开盘价上方或接近开盘价的区域，Smart Money 在此做空（看跌日）/做多（看涨日）；适用=错过初始入场或金字塔加仓；FVG/Imbalance/Raid 集中于 CPE 区（p.279–282）。
> Dealing Range 形成：开盘区间两侧均被 take 后，该运行即构成 dealing range（p.276–277）。
> Opening Range（另一口径，Ch28 p.538）：9:30 EST 开后 30 分钟——两口径并存，本能力同时输出并标注来源页。

出处：Ch14 PDF p.276–283；Ch28 p.538。

## I — Interpretation (自述)

开盘价的投影尺：用 Open+HOD 得到投影区间，其宽度=开盘价下方（看跌日）预期的 1:1 对称偏离幅度；CPE 则是开盘价附近的"聪明钱挂单区"，错过的入场与加仓都在这里找 FVG/Imbalance/Raid。附带一个状态判定：开盘区间两侧都被扫过=dealing range 成立（折溢价划分的前提）。能力输出三件：投影区间与 1:1 偏离带、CPE 区、dealing range 成立与否。

## A1 — Application Example

原书案例：Ch14 p.283 Open+HOD 投影与 1:1 偏离示意图（【图 prepared-unreviewed】）。原书未给偏离实现率统计。

## A2 — Future Trigger

情境：开盘后问"今天开盘区间投影多少、下方空间多大"；问"错过开盘入场在哪补"；问"dealing range 成立了吗"。
语言信号：opening range / 开盘区间 / 投影 / CPE / close proximity / 1:1 deviation / dealing range 成立。
区分：只管开盘价相关的投影与补入区；全天静态锚→ daily-static-anchors；折溢价偏向→ daily-bias-checklist。

## E — Execution

输入契约：当日 Opening Price、HOD（或截至当前的高点并标注"截至"）、开盘区间两侧是否已被 take。
1. 计算向上偏离 Range = HOD − Opening Price；开盘价下方 1:1 对称偏离带 = [Open − Range, Open]，下方 1:1 目标 = Open − Range。（原文公式字面为 "Projection = Open + HOD; Opening Range = Projection − Opening Price"，量纲不通；结合 "We want to see 1:1 deviation below" 的对称语义实现为上述口径，此为实现约定并已登记 nr-16，不改变原意方向。）
2. CPE 区=开盘价上方至 HOD 附近（看涨日镜像下方）。
3. Dealing range 判定：两侧均被 take=成立；否则标"未成立，折溢价划分不可用"。
4. 同时输出 9:30 后 30 分钟 Opening Range（Ch28 口径）作为时段参照。
5. 输出：{range_width, deviation_band, dev_target_1to1, cpe_zone, dealing_range, opening_range_30min}。
判停：HOD 未形成（开盘初期）→输出"截至当前"值并标注。

## B — Boundary

- 1:1 偏离为作者预期而非保证；两侧未 take 时 CPE 逻辑不适用。
- 两口径 Opening Range 并存，输出必须带来源页防混用。
- 点数口径随品种价格尺度变化，未给跨品种换算。
- 不用于无开盘价概念的 24/7 品种。
