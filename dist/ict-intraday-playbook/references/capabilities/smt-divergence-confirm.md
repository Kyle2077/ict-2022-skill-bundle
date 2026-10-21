# SMT 背离确认工具（SMT Divergence Confirm）

## R — Reading (原文)

> "You are not looking for SMT divergence to take a trade, you use it only around predetermined levels with trade idea in mind. Then once pattern unfolds that is the green light to get into the trade."（PDF p.190）
> 配对：EURUSD/GBPUSD、ES/NQ、BTC/ETH、DXY/ES（p.186–189）。溢价区某品种未能创新高=看跌背离；折价区未能创新低=看涨背离（p.188）。

出处：Ch12 PDF p.186–192。

## I — Interpretation (自述)

跨品种裂缝探测器：两个高相关品种在关键水平上"一个创新低/高、另一个不跟"，视为聪明钱在其中之一上不再推动的信号。作者给它定了严格用法边界——只在已有交易想法+预定水平附近用作绿灯/红灯确认，绝不单独成信号。能力实现为比对器：输入两个品种在同一窗口的极值行为与所在折溢价区，输出确认/不确认/无裂缝，并强制记录比对时间框架（原书未规定，nr-08）。

## A1 — Application Example

原书案例：Ch12 p.187–191 的 EURUSD/GBPUSD 与 BTC/ETH 背离示意图（【图 prepared-unreviewed】）：折价区一品种创新低而另一品种更高低=看涨裂缝。原书未给结果统计。

## A2 — Future Trigger

情境：已有多头/空头想法，问"ES 和 NQ 背离了吗/能进吗"；问"SMT 是什么/怎么用"。
语言信号：SMT / divergence / 背离 / ES NQ / EUR GBP / BTC ETH / DXY / 裂缝 / 确认信号 / green light。
区分：只作确认；"想法本身成不成立"→ daily-bias-checklist；"何时进"→ 入场族能力。

## E — Execution

输入契约：配对品种、比对时间框架（调用方指定并记录）、关键水平、两品种该窗口极值行为、折溢价区。缺任一项先询问。
1. 判定裂缝类型：溢价区未同步新高=看跌；折价区未同步新低=看涨；同步=无裂缝。
2. 用法门：调用方是否已有想法+该水平是否预定？否→输出"仅供观察，不构成确认"。
3. 输出：{裂缝类型, 确认/不确认现有想法, 比对TF, 依据极值}。
判停：无想法场景直接判停为观察模式。

## B — Boundary

- 绝不单独入场（作者明令）；背离出现≠立即反转。
- 比对 TF 原文未规定（nr-08）：不同 TF 结论可能相反，必须记录所用 TF。
- 相关性破裂期（宏观分化）裂缝失效；加密配对流动性差异大。
- 不用于非配对品种。
