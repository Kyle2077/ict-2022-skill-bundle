# ICT ATM 方法（60 分钟 Stop-Hunt 模式）

## R — Reading (原文)

> ATM：独立价格行为模式，利用 stop hunt；推荐 60 分钟图。流程：①扫描 1H 图关键高点/低点形成时伴随短期 swing low/high 被突破；②理想=Key High 前有一对 swing highs 被打破（持续走高结构）；③等价格回撤至 Key High 形成前被突破的 swing low（做多镜像：Key Low 前被突破的 swing high）；④突破结构并取得 2 个 STL/STH 后，等回调至 Breaker Block 入场。止损：High 或 Breaker Block；止盈：第二个 STL 以下 / 第二个 STH 以上（p.415–418）。
> 警告："this is only a setup, you have to frame context behind every setup"；可在任何 TF 找到但推荐 60m（p.415）。

出处：Ch19 PDF p.415–418。

## I — Interpretation (自述)

一个 60 分钟图的"stop hunt 回踩"模式：关键高点的形成过程先打破了它前面的短期低点（猎杀），之后价格回踩那个被打破的短期低点区域，等结构再突破并取下两个短期低点后，在 Breaker Block 回调处入场；止损放在关键高或 Breaker，止盈看向第二个短期低点之外。与 2022 Model 的区别：不依赖 FVG 链与新闻窗口，依赖 Breaker 与双 STL 计数；与 Turtle Soup 的区别：入场在 Breaker 回踩而非扫掠影线外限价。

## A1 — Application Example

原书案例：Ch19 p.416–418 ATM 标注图（Key High、被破 swing low、2×STL、Breaker 入场带；【图 prepared-unreviewed】）。原书未给结果统计。

## A2 — Future Trigger

情境：1H 图上问"这个关键高点扫完低点后怎么接"；问"ATM 模式现在到第几步"；问"breaker 回踩入场用哪个模型"。
语言信号：ATM / atm method / 60分钟 / 1H stop hunt / key high / breaker 回踩 / 两个短期低点。
区分：管 60m 的 ATM 序列；Breaker 分类→ pd-array-block-dictionary；FVG 链→ ict-2022-model。

## E — Execution

输入契约：1H K线序列、Key High/Low 候选、被突破的短期摆动点。
1. 扫描 Key High/Low 形成时是否伴随对侧短期摆动被突破；无→停"模式未形成"。
2. 理想结构核验：Key High 前一对 swing highs 被打破（加分项，缺失标注降级）。
3. 回踩等待：价格回撤至 Key High 前被突破的 swing low。
4. 结构计数：突破后取得 2 个 STL（做空语境）→等回调至 Breaker Block 入场。
5. 风控：止损=Key High 或 Breaker；止盈=第二个 STL 之下（镜像对称）。
6. 输出：{阶段, key level, 回踩位, 入场, 止损, 止盈, 降级标注}。
判停：步骤 1/3 未满足→等待或停。

## B — Boundary

- 作者明示"只是 setup，必须配上下文"——无 HTF narrative 不执行。
- 推荐 60m；其他 TF 使用为使用者自担口径。
- 图依赖未全核（nr-11）。
- 不用于无 stop-hunt 结构的顺势行情。
