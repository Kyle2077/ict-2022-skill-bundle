# OTE 入场区计算（OTE Entry Zone Calculator）

## R — Reading (原文)

> "How to identify discount? First, look for a bullish displacement in price. Once that occur, you want to see price forming a swing high. Now you can draw your Fibonacci tool from swing high to swing low. Wait for price return back to discount and look for longs there."（PDF p.131）
> OTE = Fib 0.62–0.79，0.705 甜蜜点；限价单置于区间内（Ch16 p.373，试点外摘要：作者称"80% 情况有效"无数据来源）。NY Scalp 用 62% 档入场（p.655）。

出处：Ch9 PDF p.131–132；Ch32 p.655。

## I — Interpretation (自述)

位移发生后的回撤入场定位器：确认位移方向→取位移腿的摆动高/低→按方向选择 Fib 锚定（看涨=高→低）→输出 0.62–0.79 回撤区与 0.705 甜蜜点作为限价挂单区。它是纯斐波那契算术，价值在于统一锚定方向（很多人画反）与把"折价/溢价"落成具体价位带；同时诚实标注：价格不总进 OTE（50% 回撤常见），进区也不保证反转。

## A1 — Application Example

原书未提供带数值的算例；明确标记的合成演练：看涨位移后 swing high=4520.0、swing low=4500.0（ES）→ Fib 高→低锚定 → OTE 区 = 4500+0.62×20=4512.4 至 4500+0.79×20=4515.8，甜蜜点 4514.1。与 p.131 规则逐字对应。

## A2 — Future Trigger

情境：位移后问"回撤到哪儿挂单"；问"0.705 是什么/甜蜜点"；为入场能力定限价档。
语言信号：OTE / optimal trade entry / 0.62 / 0.79 / 0.705 / 甜蜜点 / fib 回撤 / 挂单区 / discount premium 价位。
区分：只算区间；"这个块能不能挂"→ pd-array-block-dictionary；"做不做"→ high-probability-entry-risk。

## E — Execution

输入契约：位移方向、位移腿摆动高/低两点价位。缺锚点先询问，不得用近似高低点。
1. 校验位移存在（引用 mss-displacement-gate 口径或使用者确认）。
2. 锚定：看涨=swing high→swing low；看跌=swing low→swing high。
3. 计算 0.62/0.705/0.79 三档价位与区间。
4. 输出：{方向, 锚点, OTE 区间, 甜蜜点, 提示：价格可能仅回撤 50% 即走}。
判停：锚点不可靠（无明确摆动点）→说明并停。

## B — Boundary

- "80% 有效"无数据来源：仅作作者声明记录，不进结论。
- 不保证进区即反转；需与 PD Array 汇合使用。
- 不用于无位移的震荡区。
- 与 Dealing range 折溢价区分：OTE 是位移腿的回撤带，dealing range 是双边扫掠区间的中点划分。

## 补章并入（2026-10-21，Ch16 逐页细读）

- 增量参数（Ch16 p.364–377）：最低 R/R 要求 3:1；回调通常发生在 0.62–0.705 之间；0.705–0.79 在上升趋势=Discount、下降趋势=Premium；Fib 水平本身不作支撑阻力（价格不从线反弹），用于定位 Liquidity Blocks（FVG/OB）；经典 TA 止损聚集于 0.62/0.79 后方=流动性来源解释。
- "80% 有效"上下文（p.373）：必须配合风险管理；"These Fibonacci levels don't magically work everywhere"。
