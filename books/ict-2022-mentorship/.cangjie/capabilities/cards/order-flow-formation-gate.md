# Order Flow 形成门（Order Flow Formation Gate）

## R — Reading (原文)

> 看跌 OF 形成三条件：①上升结构被打破或沿趋势攫取流动性；②抓取买方流动性(buy stops)；③形成新的更低低点与更低高点。确认=价格开始突破内部买方流动性并触及看跌 POI。看涨镜像（p.338–343）。
> OF 激活：价格离开 OF 区域后回调退出该区域即激活。
> 关键警告："It is unprofitable to enter from the Order Flow zone itself, the stop loss is already too big." 应从 OF 内的 Order Blocks 入场（p.343）。

出处：Ch16 PDF p.338–343。

## I — Interpretation (自述)

MSS 之后的"方向持续性"门：单次位移突破只说明结构变了，Order Flow 形成才说明机构已开始沿新方向持续交付——三条件（破结构/攫流动性、取对侧止损、创同向新极值）齐备才算 OF 成立，回调退出 OF 区即激活入场窗口。同时内建作者的反直觉警告：OF 区本身不是入场点（止损太远），入场在 OF 内的 OB。它位于 mss-displacement-gate 与入场族之间，回答"这个新方向值得跟吗、在哪跟"。

## A1 — Application Example

原书案例：Ch16 p.339–343 看跌/看涨 OF 形成标注图（【图 prepared-unreviewed】）。原书未给统计。

## A2 — Future Trigger

情境：MSS 之后问"这个新方向成立了吗"；问"order flow 形成了吗、激活了吗"；问"OF 区能直接进吗"。
语言信号：order flow / OF 形成 / 机构订单流方向 / 激活 / institutional order flow formation。
区分：管"方向持续性门"；单次突破有效性→ mss-displacement-gate；层级→ market-structure-hierarchy；挂单位→ pd-array-block-dictionary。

## E — Execution

输入契约：K线序列、MSS 结果（或现场判定）、被攫流动性对象。
1. 三条件核对（按方向镜像）：破结构或沿趋势攫流动性 / 取对侧止损 / 创同向新极值对。
2. 确认：价格突破内部对侧流动性并触及同向 POI。
3. 激活判定：价格离开 OF 区后回调退出该区→激活=入场窗口开放。
4. 入场指引：OF 区内禁止直接入场；指向 OF 内 OB（调 pd-array-block-dictionary）。
5. 输出：{of_state(forming/formed/activated/absent), 三条件[], 入场指引, 警告}。
判停：三条件缺二→absent，不输出方向结论。

## B — Boundary

- OF 是作者叙事层概念（机构双仓位逻辑未证明）。
- 图依赖未全核（nr-11）。
- 不用于无 MSS 前置的场景；不替代偏向清单。
