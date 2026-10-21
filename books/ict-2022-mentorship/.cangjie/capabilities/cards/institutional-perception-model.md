# 机构感知区间模型（Institutional Perception / Breaker Standalone Model）

## R — Reading (原文)

> 铁律："Never buy above old highs, never sell below old lows."（p.477）
> 三步模型：①识别 market profile（盘整 vs 趋势；本模型在 range-bound 市场最有效）；②BSL 被扫后出现 breaker——"that last down close candle is the start of the run on the buyside liquidity is the bearish breaker"；价格突破该蜡烛后等回踩卖出；止损 above breaker block 或 just above 的 bearish OB；一旦低于 SSL 即出场（部分或全平）；③SMT divergence 作汇合确认（ES 创 HH 而 NQ 创 LH = fake-out/turtle soup 信号）（p.477–481）。
> 警告："only the divergence doesn't necessarily mean there's a trade. Narrative is a key."（p.481）

出处：Ch21 PDF p.477–481。

## I — Interpretation (自述)

一个可以独立运行的区间反转模型：在 range-bound 市场里，等买方流动性（EQH/旧高）被扫，把"发动这次扫掠的最后一根 down-close 蜡烛"定义为 bearish breaker，价格突破它之后回踩即卖，止损放在 breaker 或其上方 bearish OB，跌破 SSL 就走。SMT 背离只在 EQH 上方作汇合确认、不构成独立信号。整个模型的顶层约束是铁律（不追旧高买/旧低卖）。它比 2022 Model 更轻：不需要 FVG 链，靠 breaker+回踩。

## A1 — Application Example

原书案例：Ch21 p.478–481 breaker 与 SMT 对比图（【图 prepared-unreviewed】）。原书未给结果统计。

## A2 — Future Trigger

情境：区间市问"扫完前高之后在哪空"；问"breaker  standalone 怎么用"；问"EQH 被扫了能反手吗"。
语言信号：institutional perception / breaker 模型 / 区间反转 / EQH 被扫 / last down close candle / 回踩卖出。
区分：管"breaker 独立入场模型"；breaker 分类→ pd-array-block-dictionary；扫掠 V 型反手→ turtle-soup-entry；SMT→ smt-divergence-confirm。

## E — Execution

输入契约：市场 profile 判定（range-bound 必需）、BSL/EQH 水平、扫掠后K线序列、（可选）SMT 配对。
1. Profile 门：非 range-bound→输出"模型不适用（趋势市用其他流程）"。
2. Breaker 定位：扫掠 BSL 的那根最后 down-close 蜡烛=breaker；记录其高低。
3. 入场：价格突破 breaker 后回踩→卖出；止损=breaker 上方或 just above 的 bearish OB。
4. 出场：低于 SSL→部分/全平。
5. SMT 汇合（可选）：EQH 上方 ES/NQ(YM/DXY) 背离=加强；无背离不否决但标注。
6. 输出：{profile, breaker 区间, 入场, 止损, 出场规则, smt 汇合}。
判停：步骤 1 失败即停。

## B — Boundary

- 仅 range-bound 市场有效（作者明示）。
- SMT 单独不构成交易（narrative 为王）。
- 铁律为顶层约束：本模型一切入场不得违反。
- 图依赖未全核（nr-11）。
