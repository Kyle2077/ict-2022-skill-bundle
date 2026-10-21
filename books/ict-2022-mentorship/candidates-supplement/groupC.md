# Group C Supplement Candidates (Ch19–Ch21)

## [C-01] ICT ATM Method — Standalone Stop-Hunt Pattern
- type: framework
- source: PDF p.415–418
- mechanism: 独立价格行为模式，利用stop hunt。在60分钟图上扫描：(1) 寻找Key High/Low形成时伴随短期swing low/high被突破；(2) 理想情况下Key High前有一对swing highs被打破（持续走高结构）；(3) 等待价格回撤至Key High形成前被突破的swing low（做多）或Key Low形成前被突破的swing high（做空）；(4) 突破结构并取得2个Short-Term Lows/Highs后，等待回调至Breaker Block入场。止损：High或Breaker Block（做空）/ Low或Breaker Block（做多）。止盈：Below Second Short Term Low / Above Second Short Term High。
- chart_dependency: 高【需看图 PDF p.416–418】— Key High/Low识别、2个STL/STH的位置关系、Breaker Block精确位置均需图表确认
- counterexamples: 原文强调"this is only a setup, you have to frame context behind every setup"；可在任何时间框架找到但推荐60分钟图
- mapping: 建议新增能力「ICT ATM Method」+ 理由：与cap-10（2022 Model）和cap-12（Turtle Soup）均不同——ATM是独立的stop-hunt模式，使用Breaker Block入场而非FVG/OB，有独立的止损止盈规则，且专门针对60分钟图

## [C-02] MMXM/MMBM Complete Structure — Buy/Sell Program Cycle
- type: framework
- source: PDF p.419–467
- mechanism: 做市商卖出模型(MMXM)完整结构：前提HTF bearish。(1) Initial Consolidation = 起点，工程师SSL > BSL；(2) Buy Program = Net Long，从Initial Consolidation Low到HTF PD Array为BDR(Buyside Delivery Range)，用Fib锚定high-to-low分25%象限；(3) BDR内积累阶段：第1-2象限间第一阶段accumulation（回盘整或rebalance inefficiency/run SSL），第2-3象限间第二阶段re-accumulation；(4) 50%处出现Measuring Gap（未填充FVG，反映origin-to-terminus中点）；(5) Manipulation Swing：最后re-accumulation后的爆炸性上涨腿，欺骗买家做多，形成中期swing（左STH + 右STH）；(6) SMR(Smart Money Reversal)：Type1 = 跑过old high触及HTF level后跌破old swing low（理想型）；Type2 = 到达HTF level后形成lower high再跌破swing low；(7) MSB确认需含FVG——若FVG不存在则不视为有效break；(8) Sell Program = Net Short，SDR从SMR high到Initial Consolidation以下terminus，同样25%分级；(9) Distribution四要素：run liquidity → rebalance/run stops → mitigate in area → continue lower seek liquidity。MMBM完全镜像反转。
- chart_dependency: 极高【需看图 PDF p.420–466】— BDR/SDR 25%象限划分、Measuring Gap位置、Manipulation Swing形态、SMR Type1 vs Type2视觉区分、Distribution Block蜡烛位置均纯文字无法还原
- counterexamples: "there can be more than two stages of accumulation or distribution cycles"；SMR确认需displacement + time双重验证；仅当HTF IOF bearish时使用sell model
- mapping: 建议将ref-01升级为正式能力「MMXM/MMBM State Machine」+ 理由：原文给出了可判定的状态转换条件——(a) SMR确认 = MSS/MSB + FVG存在 + displacement；(b) Calibration数值NQ 5/10/15/20点、ES 2/5/7/10点；(c) Manipulation Swing 2-2.5 STD投影；(d) BDR/SDR 25%象限分级。这些使MMXM从概念变为可执行框架

## [C-03] MMXM Calibration Techniques — Point Range & STD Projection
- type: calculation
- source: PDF p.447–452
- mechanism: 校准terminus深度的精确方法：(1) 取Initial Consolidation range (high - low)，在consolidation下方寻找point range增量：NQ = 5/10/15/20点，ES/SP500 = 2/5/7/10点；(2) 检查HTF level是否与某point range level接近；(3) 取Manipulation Swing (last swing low before reversal → swing high)，向下投影STD：2-2.5 STD为常见目标区；1-2 STD为redistribution区域；(4) 若STD投影与point range及HTF level三重汇合 = 高概率distribution area；(5) 额外确认：取SMR后第一个swing low到short-term high的Fib，向下投影deviations，若与上述汇合则增强信心；(6) Consolidation Range Fib：取midway point，reject half STD above consolidation high，用于预测buy program高点。
- chart_dependency: 高【需看图 PDF p.447–452】— STD投影的具体锚定点、point range与HTF level的重叠关系需图表验证
- counterexamples: 原文未给出失效条件，但强调"if these deviations overlap with the grades of our buyside delivery range, this is where we are likely to see our highest probability setups"——暗示不重叠时概率降低
- mapping: 建议并入C-02（MMXM/MMBM State Machine）作为其calibration子模块；若单独成能力则命名「MMXM Calibration」

## [C-04] Smart Money Reversal (SMR) Confirmation Protocol
- type: procedure
- source: PDF p.437–445
- mechanism: SMR确认的精确步骤：(1) Type1（理想型）：价格跑过old high → 触及HTF level → 跌破old swing low形成MSB；(2) Type2：到达HTF level → 形成lower high（未能超前高）→ 跌破swing low；(3) MSB有效性判定：扩张腿内必须存在FVG，若无FVG则不视为有效break；(4) 不需要收盘低于swing low即可确认有效break（只要有FVG）；(5) 更高概率：当价格穿过最后一根up-close candle（运行BSL的那根）的开盘价并收盘低于swing low时；(6) 该up-close candle成为bearish order block，其open被违反 = change in state of delivery确认；(7) SMT divergence额外确认：相关资产显示背离（如ES做HH而NQ做LH）。
- chart_dependency: 高【需看图 PDF p.439–445】— Type1 vs Type2的视觉区分、FVG在扩张腿内的位置、order block开盘价的精确标注均需图表
- counterexamples: "If this FVG is not present, we don't class this as a valid break in market structure"；SMT divergence仅在correlated asset posting higher high时才参考Type2
- mapping: 部分已覆盖于cap-05（MSS Displacement Gate）和cap-14（SMT Divergence Confirm），但SMR的Type1/Type2分类、order block open violation确认、以及"不需要close below swing low"的规则是增量内容，建议并入C-02或增强cap-05

## [C-05] MMXM Entry Models — Three Post-SMR Entry Options
- type: procedure
- source: PDF p.454–462, 467
- mechanism: SMR确认后三种入场模型：(1) 2022 Model（即cap-10六步流程）；(2) OFED（Order Flow Entry after Displacement）；(3) Breaker + Fair Value Gap。低风险卖出(Low Risk Sell)：在change in state of delivery确认后，回撤至bearish order block入场；LTF卖方项目继续时order block内会出现FVG，该FVG为高概率——不需要回来rebalance，可从low到open price直接下行；可进入order block更高但不要看到mean threshold被收盘突破。Distribution cycle第一阶段：回到打破结构的腿内FVG，在breaker（最后阶段accumulation内的down-close candles）处mitigate。
- chart_dependency: 高【需看图 PDF p.454–462】— Low Risk Sell的order block位置、breaker蜡烛识别、distribution block内down-close candles均需图表
- counterexamples: "we do not want to see the mean threshold of the order block breached on a closing basis"；distribution block定义为accumulation阶段内的down-close candles，非任意bearish candle
- mapping: 2022 Model已覆盖于cap-10；Breaker+FVG部分覆盖于cap-07；但三者在MMXM上下文中的选择逻辑和Low Risk Sell的具体规则是增量，建议并入C-02

## [C-06] BDR/SDR 25% Quadrant Grading System
- type: framework
- source: PDF p.426–432, 446–453
- mechanism: 买方交割范围(BDR)分级：(1) 锚定Fib从BDR high到low（即initial consolidation low → HTF level）；(2) 分为4个25%象限；(3) Initial consolidation一般在lower quadrant形成；(4) 第1-2象限间 = 第一阶段accumulation或return to consolidation；(5) 50% = Measuring Gap（未填充FVG，中点反射）；(6) 第2-3象限间 = 第二阶段re-accumulation（rebalance BISI或seek SSL）；(7) 从final accumulation到Terminus = 爆炸性上涨。SDR同理镜像：从SMR high到calibrated terminus，25%增量分级；第一阶段distribution在第1象限，第二阶段(Silver Bullet)在第3象限。
- chart_dependency: 极高【需看图 PDF p.427–432, 446–453】— 25%象限的视觉划分、各阶段accumulation/distribution在象限中的位置、Measuring Gap与50%线的对齐均需图表
- counterexamples: Measuring Gap "will not be fully filled"；"there can be more than two stages of accumulation or distribution cycles"
- mapping: 建议并入C-02（MMXM/MMBM State Machine）作为其grading子系统

## [C-07] Distribution Cycle Four Elements
- type: principle
- source: PDF p.462–464
- mechanism: 分配周期四要素（Sell Program内重复循环）：(1) Run liquidity（运行流动性）；(2) Rebalance or run stops（再平衡或运行止损）；(3) Mitigate within an area on the left side of the curve（在曲线左侧区域内mitigate）；(4) Continue lower to seek liquidity（继续走低寻求流动性）。Distribution Block定义：accumulation阶段内的down-close candles。Breakaway Gap(BG)：未填充FVG，出现在distribution第一阶段附近。Silver Bullet(SB)：出现在graded range第三象限的第二阶段distribution。
- chart_dependency: 中【需看图 PDF p.462–464】— Distribution Block蜡烛位置和BG/SB的标注需图表辅助，但四要素本身为文字可传达的原则
- counterexamples: 原文未给出失效条件
- mapping: 建议并入C-02；四要素可作为MMXM sell program的状态机循环规则

## [C-08] ICT 2022 Model — 50% Fib Two Anchor Options (Incremental Detail)
- type: procedure
- source: PDF p.409–411
- mechanism: cap-10六步中Step 4的精确补充：50% Fibonacci线有两种锚定方式：(a) 从take liquidity的swing到FVG另一侧的swing；(b) 从liquidity taken swing之后的prominent swing到FVG另一侧的swing。Step 5补充：FVG缺口必须在Equilibrium线(50%)上或在流动性一侧（即better side）。Displacement Range定义：displacement low（被打破的短期低点）到displacement high（旧高点）之间的范围。
- chart_dependency: 中【需看图 PDF p.410–411】— 两种锚定方式的视觉对比、FVG与Equilibrium的位置关系需图表确认
- counterexamples: 原文未给出两种方式的优先级或选择条件
- mapping: 已覆盖于cap-10，但两种Fib锚定方式和"FVG must be on Equilibrium or better side"的精确表述是增量细节，建议补入cap-10文档

## [C-09] Daily Rebalance Algorithm Timeline
- type: principle
- source: PDF p.468–472
- mechanism: 算法时间线（纽约时间）：(1) 00:00 Midnight = 算法启动日；(2) 08:30 = 算法开始寻找流动性；(3) 08:30–09:30 = 1小时窗口，bearish sentiment预期价格上涨寻找short setups；(4) 09:30 = 股市开盘，manipulation时段，创造看似突破的机会但实际相反。Bearish场景下价格运行至Premium区的两个原因：① 取old high/highs以获取BSL，让smart money在其空头头寸上与散户竞争；② 在这些buy stops上卖出，以便之后以更便宜的SSL买入作为offset/allocate short positions的流动性池。
- chart_dependency: 低 — 时间线和两原因为纯文字原则，不依赖特定图表
- counterexamples: "Don't predict low or high, you will only lose money!"
- mapping: 部分已覆盖于cap-13（PO3 AMD State Machine）的时间框架部分，但08:30–09:30窗口的具体功能和bearish premium运行的两原因是增量，建议补入cap-13或新增「Daily Rebalance Timeline」

## [C-10] Immediate Rebalance — Rocket Fuel Effect
- type: principle
- source: PDF p.474–476
- mechanism: Immediate Rebalance定义：市场快速调整到新价格水平，通常在价格失衡或低效之后，发生在短时间框架内（几根蜡烛），导致快速价格运动。具体表现：市场重新定价到特定水平（如weekly gap low）后迅速无法继续沿该方向运行——向上通过某水平→向下通过→再次测试但立即失败。例如：一根蜡烛的高点之后立即交易回到该蜡烛高点 = immediate rebalance。效应："like rocket fuel, causing the price to take off rapidly"。
- chart_dependency: 中【需看图 PDF p.474–476】— Immediate Rebalance的蜡烛形态和"rocket fuel"效应的视觉示例需图表确认
- counterexamples: 原文未给出失效条件
- mapping: 建议新增能力「Immediate Rebalance」+ 理由：这是一个独立的价格行为现象，与cap-06(FVG)和cap-13(PO3)相关但不相同——它描述的是价格对特定水平的即时拒绝和反向加速，可作为入场时机确认信号

## [C-11] Institutional Perception Iron Rule & Three-Step Model
- type: framework
- source: PDF p.477–481
- mechanism: 铁律："Never buy above old highs, never sell below old lows." 三步模型：Step 1 = Identify market profile（盘整vs趋势，此模型在range-bound市场极有效）；Step 2 = Run on BSL followed by breaker（BSL/EQH被取→价格下跌→最后一根down-close candle = bearish breaker起点→价格突破该candle后等待回访卖出；一旦低于SSL即出场；止损above breaker block或bearish OB just above breaker）；Step 3 = SMT divergence confluence for SMR（在EQH上方寻找SMT预判转折点：如ES做HH而NQ做LH = fake-out/turtle soup信号，预示反转）。SMT分析工具：ES、NQ、YM、DXY。
- chart_dependency: 高【需看图 PDF p.477–481】— Breaker candle识别、SMT divergence的ES/NQ对比、range-bound市场的profile判断均需图表
- counterexamples: "only the divergence doesn't necessarily mean there's a trade. Narrative is a key."；breaker本身即为完整交易模型，SMT仅为confluence
- mapping: Step 2的breaker入场部分覆盖于cap-07和cap-12；SMT部分覆盖于cap-14；但"Iron Rule"作为顶层原则、三步模型的完整序列、以及breaker作为standalone model的定位是增量，建议新增能力「Institutional Perception Model」

## [C-12] Bearish Breaker Precise Definition
- type: glossary
- source: PDF p.477–478
- mechanism: Bearish Breaker精确定义：在BSL(EQH)被取后价格下跌时，"that last down close candle is the start of the run on the buyside liquidity is the bearish breaker"。即：运行买方流动性的最后一根down-close candle。入场：价格突破该down-close candle后等待回访卖出。止损：above breaker block或bearish OB just above breaker。出场：once you go below SSL, you're out (partials or full close)。
- chart_dependency: 中【需看图 PDF p.478–479】— Breaker candle的精确识别和止损位置标注需图表
- counterexamples: 原文未给出失效条件
- mapping: 部分覆盖于cap-07（PD Array Block Dictionary），但cap-07侧重block分类，此处给出了breaker作为独立入场模型的完整规则（含止损止盈），建议补入cap-07或作为C-11的子规则

---

## glossary-supplement

| Term | Definition (from text) | Source |
|------|----------------------|--------|
| **ATM** | Independent price action pattern that capitalizes on stop hunt; used on 60-minute charts; similar to 2022 mentorship model but standalone | PDF p.415 |
| **MMXM (Market Maker Sell Model)** | Complete cycle: Buy Program (accumulation/re-accumulation) → SMR → Sell Program (distribution/re-distribution); used when HTF is bearish; delivers price efficiently to HTF draw while generating liquidity pools below marketplace | PDF p.419–467 |
| **MMBM (Market Maker Buy Model)** | Mirror reverse of MMXM; used when HTF is bullish | PDF p.454 |
| **SMR (Smart Money Reversal)** | Change in state of delivery; algorithm goes from buy program to sell program or vice versa; confirmed with displacement and time; Type1 = higher high then break below old swing low; Type2 = lower high then break below swing low | PDF p.437–440 |
| **BDR (Buyside Delivery Range)** | From initial consolidation low to HTF level where price is expected to reach; graded in 25% quadrants using Fib anchored high-to-low | PDF p.426–428 |
| **SDR (Sellside Delivery Range)** | From point of origin (MMXM high) to initial terminus below initial consolidation; graded in 25% increments | PDF p.445–446 |
| **BTR (Buyside Terminus Range)** | Projected by taking Fib from point of origin to measuring gap and projecting one deviation higher; if overlaps with HTF level and/or BSL, confirms measuring gap | PDF p.430 |
| **OFED** | Order Flow Entry after Displacement; one of three post-SMR entry models alongside 2022 Model and Breaker+FVG | PDF p.467 |
| **Measuring Gap** | Unfilled FVG at the 50% midpoint of BDR/SDR; reflects halfway point between origin and terminus; will not be fully filled; gives extra confirmation that calibrated terminus is correct | PDF p.429–430, 453 |
| **Distribution Block** | Down-close candles inside of the stage of accumulation; used for mitigation during distribution cycle | PDF p.462 |
| **Immediate Rebalance** | Market quickly adjusts to new price level after imbalance/inefficiency; happens within few candles; e.g., candle's high immediately followed by trade down to that high; acts as "rocket fuel" causing rapid price movement | PDF p.474–476 |
| **Event Horizon** | 原文未在ch19-21中出现此术语定义 | N/A |
| **Calibration** | Technique to assess how far price can go below initial consolidation using point ranges (NQ: 5/10/15/20 pts; ES: 2/5/7/10 pts) and manipulation swing STD projections (2-2.5 STD common) | PDF p.447–452 |
| **Manipulation Swing** | Last swing low before reversal to swing high that ran BSL above old high into HTF level; occurs after final re-accumulation stage; tricks buyers into longs; forms intermediate term swing with STH left and STH right; 2-2.5 STD projection = common target | PDF p.449–451 |
| **Breakaway Gap (BG)** | Unfilled FVG appearing around first stage of distribution | PDF p.453 |
| **Silver Bullet (SB)** | Second stage of distribution occurring around 3rd quadrant of graded range | PDF p.453 |
| **Iron Rule** | "Never buy above old highs, never sell below old lows" | PDF p.477 |
| **Bearish Breaker** | The last down-close candle that starts the run on buyside liquidity after BSL/EQH is taken | PDF p.477 |
