# Group B Supplement Candidates — Ch14 & Ch16

---

## [B-01] Opening Range Projection Formula (CPE Deviation)
- type: calculation
- source: PDF p.282–283
- mechanism: Opening Range Projection = Open + HOD（当日最高价）；Opening Range = Opening Range Projection − Opening Price。该区间定义了开盘价下方允许的价格偏离幅度，用于高概率做空场景中的"Close Proximity Entries"（CPE）。原文："We want to see 1:1 deviation below." 即在CPE区域内，预期价格向下偏离与向上偏离呈1:1对称。所有日线范围内的潜在空头（FVG、Imbalance、Raid）均在此区域形成。【需看图 PDF p.283】
- chart_dependency: 高【需看图 PDF p.283，展示Open+HOD投影与1:1偏离示意】
- counterexamples: 原文未给出明确失效条件；但暗示若开盘区间两侧均未被take，则不构成dealing range，CPE逻辑不适用。
- mapping: 建议新增能力「opening-range-cpe-projection」+ 理由：cap-13 po3-amd-state-machine 覆盖PO3三阶段但未包含Opening Range的具体计算公式与1:1偏离量化规则；cap-02 daily-static-anchors 涉及锚点但不含此投影公式。此为独立可计算的入场过滤工具。

---

## [B-02] Close Proximity Entries (CPE) Definition & Usage
- type: procedure
- source: PDF p.279–282
- mechanism: CPE定义为开盘价上方或接近开盘价的区域，Smart Money在此寻找做空（看跌日）或做多（看涨日）机会。适用场景：(1) 错过了开盘价上方的初始入场；(2) 需要对已有持仓进行金字塔加仓。CPE区域内聚集了FVG、Imbalance、Raid等入场信号。原文："Above the Opening Price or at 'Close Proximity Entries' is where Smart Money is looking to go short."【需看图 PDF p.280-281】
- chart_dependency: 中【需看图 PDF p.280-281，展示CPE区域与PO3各阶段关系】
- counterexamples: 无明示反例。
- mapping: 建议并入 cap-13 po3-amd-state-machine + 理由：CPE是PO3 Accumulation阶段的同义操作区域，补充了具体名称与使用场景（错过入场/金字塔加仓），属于cap-13的操作细化增量。

---

## [B-03] Pyramid Position Sizing Rule
- type: procedure
- source: PDF p.282
- mechanism: 金字塔加仓规则：首先建立最大仓位，随后每次加仓递减规模。原文："Start by putting your biggest position on first. Then, reduce the size of your next entry and continue to reduce the size for each subsequent entry." 目的：在市场反向运动时最小化复合损失风险。
- chart_dependency: 低
- counterexamples: 无明示反例；但隐含前提为已有bias确认且方向正确，否则递减加仓仍会累积亏损。
- mapping: 建议并入 cap-08 high-probability-entry-risk + 理由：cap-08覆盖止损止盈与Ch32清单，但未包含金字塔加仓的具体仓位递减规则。此为风险管理增量。

---

## [B-04] Bias Determination Three Questions (Framework)
- type: framework
- source: PDF p.273–276
- mechanism: 确定Bias的三问框架：(1) Did the Market take out any Significant Liquidity Pools? (2) Did the Market hit a Significant FVG? (3) Did the Market create a Market Structure Break with Displacement? 基于当前Framework判断下一步Draw on Liquidity：是否有clean highs/lows？是否有需要rebalance的FVG？然后判断Dealing Range内的Premium/Discount位置。原文强调避免抄底摸顶诱惑。
- chart_dependency: 中【需看图 PDF p.274-276，展示三问对应的图表标注】
- counterexamples: 原文明示警告："Avoid the temptation of picking bottoms and tops. It's a situation that will cause more losses than necessary." "Retail methods and teachings will give you false confidence."
- mapping: 建议并入 cap-04 daily-bias-checklist + 理由：cap-04已有bias判定清单，但此三问框架提供了更结构化的决策树（流动性池→FVG→MSS+Displacement的顺序检查），属于cap-04的流程增量。注意与cap-15 top-down-workflow区分：此处聚焦单日bias判定，非多时间框架分析。

---

## [B-05] PO3 Distribution Timing Window (15:30–15:45 NY)
- type: principle
- source: PDF p.280
- mechanism: Distribution周期预期发生在纽约时间下午3:30–3:45。原文："We can expect the Distribution Cycle to take place around 3:30-3:45 PM NY Time." 这是PO3第三阶段的时间窗口，Smart Money在此分配其积累的仓位，蜡烛线的反向扩张在此完成。
- chart_dependency: 低
- counterexamples: 无明示反例；但用词为"can expect"而非绝对，暗示非每日必然发生。
- mapping: 建议并入 cap-13 po3-amd-state-machine + 理由：cap-13覆盖PO3状态机但未指定Distribution的具体纽约时间窗口。此为时间参数增量。

---

## [B-06] Top Down Analysis Six-Step (4H→1M) — Incremental Detail
- type: procedure
- source: PDF p.284–292
- mechanism: 六步自顶向下分析：Step 1: 4H图识别主要趋势；Step 2: 4H图定位SSL/BSL水平；Step 3: 1H图观察Order Flow上下文中的整合区、buy stops/sell stops；Step 4: 15M图寻找SSL/BSL、SMT Divergence、FVG汇合；Step 5: 5M图确认入场时机；Step 6: 1M图微调入场并设置止损止盈。执行子规则：(1) 在Displacement内开始TDA；(2) 按5→4→3→2→1分钟图顺序；(3) 5分钟找到FVG即停止下降；(4) 2分钟找到FVG即停止；(5) 一旦找到FVG不再降低时间框架；(6) 1分钟找不到FVG则无交易。【需看图 PDF p.287-292】
- chart_dependency: 高【需看图 PDF p.287-292，每步均有对应图表示例】
- counterexamples: 原文明确："If you can't find a FVG on the 1 Minute, there is no trade." 即1M无FVG则放弃交易。
- mapping: 已覆盖于 cap-15 top-down-workflow，但有以下增量需并入：(1) 明确的六步编号流程（cap-15提及Ch6的15m→5m与Ch2/9/32框架，但Ch14给出了最完整的4H→1H→15M→5M→1M六步序列）；(2) FVG逐级下降的终止规则（5M有FVG即停、2M有FVG即停、1M无FVG则无交易）；(3) 每步的具体示例（NQ SSL 15,000 / ES BSL 4,400等）。建议将这些增量补入cap-15。

---

## [B-07] Bearish/Bullish Daily Chart Mindset Rules
- type: principle
- source: PDF p.278–279
- mechanism: 看跌日思维：每根上涨蜡烛视为卖出机会，等待价格到达关键POI或开盘价上方或在LTF上take BSL，目标为日线旧低点或前日低点。看涨日思维：每根下跌蜡烛视为买入机会，等待价格到达关键POI或开盘价下方或在LTF上take SSL，目标为日线旧高点或前日高点。
- chart_dependency: 中【需看图 PDF p.278-279，展示看跌/看涨日的蜡烛标注】
- counterexamples: 无明示反例。
- mapping: 建议并入 cap-04 daily-bias-checklist + 理由：cap-04覆盖bias判定，但未包含bias确认后的日内操作心态规则（每根反向蜡烛=机会、目标锚定旧高低点）。此为bias执行层增量。

---

## [B-08] Dealing Range Formation Definition
- type: glossary
- source: PDF p.276–277
- mechanism: Dealing Range定义：当开盘区间（Opening Range）两侧均被take后，该运行即构成Dealing Range。更广义地，任何在前一区间两端吸收流动性的价格波动形成新交易区间。PD Array是该区间内Premium与Discount的区分数组。原文："When both sides of an opening range have been taken, that run is considered a dealing range."
- chart_dependency: 中【需看图 PDF p.276-277，展示Opening Range→Dealing Range转化】
- counterexamples: 无。
- mapping: 建议并入 cap-07 pd-array-block-dictionary + 理由：cap-07覆盖PD Array矩阵但未明确Dealing Range的形成条件（opening range双侧被take）。此为cap-07的定义增量。

---

## [B-09] Daily Bias Seven-Step Systematic Approach
- type: procedure
- source: PDF p.332–354
- mechanism: 确定Daily Bias的系统七步：(1) Analyze External Markets：分析相关外部市场的Premium/Discount水平；(2) Identify Impulse Structure：识别强趋势移动、价格拒绝或突破；(3) Map Structure：绘制支撑阻力、swing highs/lows、整合区；(4) Look for Liquidity：关注流动性集中的结构区域；(5) Evaluate Premium/Discount Levels：评估外部市场P/D对本市场的影响；(6) Trade with the Flow：顺主流方向在有利的流动性区域入场；(7) If no displacement through structure, expect reversal：无位移穿越结构则预期反转。另附Bias三问（p.349）：What was taken? Where can this lead? What hasn't been taken yet?【需看图 PDF p.334-354】
- chart_dependency: 高【需看图 PDF p.334-354，多页图表展示七步应用】
- counterexamples: 原文明示："It is crucial to accurately define the Daily BIAS through proper backtesting, as inexperienced traders may make mistakes in determining it." 另："Just having a DAILY INDECISIVE CANDLESTICK doesn't mean anything." 单独依赖犹豫蜡烛无效。
- mapping: 建议并入 cap-04 daily-bias-checklist + 理由：cap-04已有bias清单，但Ch16的七步法提供了更完整的系统化流程（含外部市场分析、Impulse结构识别、流动性定位、P/D评估），以及独立的Bias三问。与B-04的三问框架互补：B-04侧重HTF框架判定，B-09侧重日内bias的系统化推导。两者均为cap-04增量。

---

## [B-10] Order Flow Formation Three Conditions (Bearish/Bullish)
- type: framework
- source: PDF p.338–343
- mechanism: 看跌Order Flow形成三条件：(1) 上升结构被打破或沿趋势出现流动性攫取；(2) 抓取买方流动性（buy stops）；(3) 形成新的更低低点和更低高点。确认：价格开始突破内部买方流动性并触及看跌POI区域。看涨Order Flow形成三条件（镜像）：(1) 下降结构被打破或沿趋势攫取流动性；(2) 抓取卖方流动性（sell stops）；(3) 形成新的更高高点和更高低点。确认：价格突破内部卖方流动性并触及看涨POI区域或take外部流动性。OF激活条件：价格离开OF区域后回调退出该区域即激活。【需看图 PDF p.339-343】
- chart_dependency: 高【需看图 PDF p.339-343，展示看跌/看涨OF形成的完整图表标注】
- counterexamples: 原文指出OF本身不是入场点："It is unprofitable to enter from the Order Flow zone itself, the stop loss is already too big." 应从OF内的Order Blocks寻找入场。
- mapping: 建议新增能力「order-flow-formation-gate」+ 理由：现有cap-05 mss-displacement-gate覆盖MSS+Displacement判定，但Order Flow形成是一个独立概念（含操纵仓位+主力仓位的双仓位逻辑、OF激活条件、OF≠入场点的规则），与MSS不完全等价。建议作为cap-05的前置过滤器或独立能力。

---

## [B-11] POI Types Complete List & Selection Rules
- type: framework
- source: PDF p.359–363
- mechanism: POI类型完整清单：(1) EQL/EQH（等低/等高）；(2) Liquidity Levels；(3) FVG；(4) Order Blocks；(5) Breaker Blocks；(6) Mitigation Block；(7) Rejection Blocks。选择规则：无强弱之分，每个级别本身都强。多POI重叠时按R/R选择最优者。必须等待LTF确认。时间框架配对：15m-5m / 1h-15m / 4h-1h / 1D-4h。激进者可从POI直接入场（小止损），但推荐LTF确认。【需看图 PDF p.361-363】
- chart_dependency: 高【需看图 PDF p.361-363，展示多POI重叠与LTF确认示例】
- counterexamples: 无明示反例；但强调"There is no concept of which of the POI levels are stronger and which are weaker"，反驳了常见的POI强弱排序误区。
- mapping: 建议并入 cap-07 pd-array-block-dictionary + 理由：cap-07覆盖PD Array内的块类型字典，但Ch16给出了完整的7类POI清单及选择规则（R/R优先、LTF确认、时间框架配对），属于cap-07的分类增量。EQL/EQH和Rejection Blocks可能未在cap-07中列出。

---

## [B-12] OTE Detailed Parameters & Context
- type: calculation
- source: PDF p.364–377
- mechanism: OTE（Optimal Trade Entry）详细参数：回撤至Fibonacci 0.62–0.79区间，0.705为核心sweet spot。限价单放置在0.62–0.79之间。0.705–0.79在上升趋势中为Discount区，下降趋势中为Premium区。通常回调发生在0.62–0.705之间。声明"This works 80% of the time"，但必须配合风险管理。最低R/R要求3:1。Fibonacci水平本身不作为支撑阻力，而是用于搜索"Liquidity Blocks"（FVG、OB等）。原因：经典TA交易者在0.62和0.79后方放置止损，形成流动性聚集。【需看图 PDF p.365-377】
- chart_dependency: 高【需看图 PDF p.365-377，多页展示OTE在不同时间框架的应用】
- counterexamples: 原文明确："These Fibonacci levels don't magically work everywhere. Like every other concept, you must combine this with other concepts to work." 另："The Fibonacci levels themselves do not act as support or resistance, and the price does not bounce off the levels themselves."
- mapping: 已覆盖于 cap-11 ote-entry-zone，但有以下增量需并入：(1) "80%有效"声明及其上下文（必须配合风险管理）；(2) 最低R/R 3:1要求；(3) Fib水平≠支撑阻力的明确声明；(4) 流动性聚集原因解释（经典TA交易者止损位置）；(5) 0.705–0.79的P/D双重属性说明。建议将这些增量补入cap-11。

---

## [B-13] Premium/Discount Four Subdivisions
- type: framework
- source: PDF p.381
- mechanism: Premium/Discount四细分：(1) Premium within Premium Market：溢价市场的顶部，代表溢价范围内的更高值；(2) Discount within Premium Market：溢价市场的底部，代表溢价范围内的较低值；(3) Premium within Discount Market：折价市场的顶部，代表折价范围内的较高值；(4) Discount within Discount Market：折价市场的底部，代表折价范围内的更低值。算法偏好：折价市场买入、溢价市场卖出。均衡区（Equilibrium）= 0.5水平，代表买卖双方平衡的公允价值。
- chart_dependency: 中【需看图 PDF p.382，展示四细分区域的图表标注】
- counterexamples: 无明示反例。
- mapping: 建议并入 cap-07 pd-array-block-dictionary + 理由：cap-07覆盖PD Array但未细分到四层嵌套结构。此为Premium/Discount概念的精细化增量，有助于精确描述价格在P/D区域内的子位置。

---

## [B-14] Dealing Range High/Low Selection Four Steps
- type: procedure
- source: PDF p.378–379
- mechanism: 选择Dealing Range高低点四步：(1) 从交易范围内最高点到最低点运行Fibonacci回撤工具；(2) 关注算法整合区域（consolidation areas），这些区域指示公允价值；(3) 当50% Fibonacci水平与普通整合区对齐时，考虑最近的高点作为Dealing Range高点；(4) 选择回调（pullback）作为Dealing Range低点，确保范围涵盖相关价格行为并与算法活跃区一致。
- chart_dependency: 中【需看图 PDF p.378-379，展示四步操作的图表标注】
- counterexamples: 无明示反例。
- mapping: 建议并入 cap-07 pd-array-block-dictionary + 理由：Dealing Range的高低点选择是PD Array应用的前提，cap-07未覆盖此操作步骤。

---

## [B-15] Risk Parameters (1-2% Risk / 10-20% Target)
- type: principle
- source: PDF p.364
- mechanism: 风险参数：每笔交易风险设定为存款的1-2%，目标利润为存款的10-20%。原文："It is most reasonable to set the risk at 1-2% of the deposit, with a target profit of 10-20% of the deposit from the trade using this concept." 配合HTF/LTF时间框架组合使用以获得更好的R/R。
- chart_dependency: 低
- counterexamples: 无明示反例；但隐含前提为使用POI+LTF确认的概念组合。
- mapping: 建议并入 cap-08 high-probability-entry-risk + 理由：cap-08覆盖Ch32止损止盈规则，但Ch16给出了具体的百分比风险参数（1-2%/10-20%），属于量化增量。

---

## [B-16] Daily Indecisive Candlestick Warning
- type: counter-example
- source: PDF p.350–351
- mechanism: 日常犹豫蜡烛（小实体+大影线）在特定上下文中可暗示潜在反转（下一根蜡烛可能与前一根相反），但不应单独依赖其确定Bias或开仓。仅在与其他因素结合时作为小提示。有效上下文示例：价格在1D POI内 + 犹豫蜡烛take Previous Week Low → 可假设反转。原文："Just having a DAILY INDECISIVE CANDLESTICK doesn't mean anything."【需看图 PDF p.351-352】
- chart_dependency: 中【需看图 PDF p.351-352，展示有效vs无效的犹豫蜡烛上下文】
- counterexamples: 这本身就是一条反例/警告：单独的犹豫蜡烛无意义，必须有POI+流动性事件等上下文支撑。
- mapping: 建议并入 cap-04 daily-bias-checklist + 理由：作为bias判定中的反面信号过滤器，防止误将犹豫蜡烛当作独立bias依据。

---

## [B-17] Two Opening Prices for PO3 Intraday (00:00 & 08:30 NY)
- type: principle
- source: PDF p.354
- mechanism: 日内PO3关注两个开盘价：纽约时间00:00 AM和08:30 AM。期望价格在开盘价上方交易作为Manipulation（Judas Swing），这与价格真正想去的方向相反。原文："We want to see the price trade above the Opening Price to act as Manipulation. This will act as a Judas Swing, and it is COUNTERING where the price will want to go."
- chart_dependency: 中【需看图 PDF p.355，展示双开盘价与Judas Swing关系】
- counterexamples: 无明示反例。
- mapping: 建议并入 cap-13 po3-amd-state-machine + 理由：cap-13覆盖PO3但未指定日内两个关键开盘价时间点及其与Judas Swing的关系。此为cap-13的时间参数增量。

---

## [B-18] Day Trading Is NOT Everyday Trading
- type: counter-example
- source: PDF p.299–300
- mechanism: 作者明示警告：日内交易不等于每天都要交易。核心陷阱：爱上胜利而非过程导向；爱上"正确"和"比别人强"。事实：不需要每天都发生高概率机会。应在不交易中找到安慰。不是每天都会给你大概率机会。原文："Find comfort in NOT taking trades." "Not every day will give you a high probability opportunity."
- chart_dependency: 低
- counterexamples: 这本身就是一条系统性反例/纪律警告：过度交易、FOMO、情绪化决策是主要失败原因。
- mapping: 建议并入 cap-08 high-probability-entry-risk + 理由：cap-08覆盖技术层面的风险管理，但此条提供心理/纪律层面的过滤规则，防止在无高概率机会时强行交易。属于cap-08的行为约束增量。

---

## [B-19] "Why Am I Considering This Trade?" Pre-Entry Filter
- type: procedure
- source: PDF p.299
- mechanism: 入场前必问："Why am I considering this trade?" 每天每次入场前都必须回答。如果有清晰自信的答案→执行交易；如果犹豫或不确定→放弃本次交易。原文声称"this works 100%"。目的是防止FOMO驱动的冲动交易。
- chart_dependency: 低
- counterexamples: 无明示反例；但"100%"声明应理解为修辞强调而非统计保证。
- mapping: 建议并入 cap-08 high-probability-entry-risk + 理由：作为入场前的心理检查清单项目，补充cap-08的技术过滤规则。

---

## [B-20] Bias Guidelines: Single-Direction Discipline
- type: principle
- source: PDF p.299–300
- mechanism: 五条Bias纪律准则：(1) 只坚持你的Bias；(2) 只在该Bias下执行；(3) 看跌只做空；(4) 看涨只做多；(5) 不必捕捉大波动，按Bias预期操作，避免在Bias间来回翻转导致自我混淆。原文："You do not have to capture the large moves, but rather work with your biased expectation so that you do not 'flip flop' back and forth between biases and confuse yourself!"
- chart_dependency: 低
- counterexamples: 无明示反例；但隐含前提是Bias本身已通过正确流程确定。
- mapping: 建议并入 cap-04 daily-bias-checklist + 理由：cap-04覆盖bias判定，但未包含bias确认后的单向执行纪律。此为bias执行层的行为约束增量。

---

## glossary-supplement

| 缩写/术语 | 定义 | 出处 |
|-----------|------|------|
| **CPE** (Close Proximity Entries) | 开盘价上方或接近开盘价的区域，Smart Money在此积累仓位；也指错过初始入场后的二次入场/金字塔加仓区域。 | PDF p.279-282 |
| **OFED** | 原文Ch14/Ch16未出现此缩写。可能在其他章节定义。 | — |
| **Protraction** | 原文Ch14/Ch16未出现此术语。可能在其他章节定义。 | — |
| **Distribution Block** | 原文Ch14/Ch16未以该名称单独定义。Distribution阶段描述见PDF p.280："Distribution is where opposite side of the Candle forms into the closing of the Candle (where the expansion occurs)." | PDF p.280 |
| **Silver Bullet** | 原文Ch14/Ch16未出现此术语。可能在其他章节定义。 | — |
| **ATH** | 原文Ch14/Ch16未出现此缩写。可能在其他章节定义。 | — |
| **Opening Range** | 指数期货中纽约时间9:30-10:30的60分钟区间，前30分钟尤为重要；用于识别其他交易者可能不知道的支撑阻力位。 | PDF p.281 |
| **Dealing Range** | 开盘区间两侧均被take后形成的新交易区间；或任何在前一区间两端吸收流动性的价格波动所形成的范围。 | PDF p.276-277 |
| **POI** (Point of Interest) | 大玩家的兴趣点，在此积累交易并"保护"其入场区域。可在任何时间框架找到（价格分形）。类型包括EQL/EQH、Liquidity Levels、FVG、OB、Breaker Block、Mitigation Block、Rejection Block。 | PDF p.359-363 |
| **OTE** (Optimal Trade Entry) | Fibonacci 0.62-0.79回撤区间，0.705为sweet spot；限价单放置区域；因接近止损位而自动获得高R/R。 | PDF p.364-377 |
| **Order Flow (OF)** | 大资本订单流，将价格传递到大资本感兴趣的区域。本质上是图表上大资本获得头寸的"痕迹"。OF本身不是入场点（止损太大），应从OF内的Order Blocks入场。 | PDF p.336-345 |
| **Judas Swing** | 市场开盘或新闻发布前的虚假价格变动，旨在将散户引向错误一侧。属于PO3 Manipulation阶段。 | PDF p.280 |
| **Daily Indecisive Candlestick** | 小实体+大影线的日线蜡烛，在特定上下文（POI+流动性事件）中可暗示反转，但单独无意义。 | PDF p.350-351 |
| **Equilibrium** | Fibonacci 0.5水平，代表资产平均价格/买卖双方平衡的公允价值区。交易者忽略0.236和0.382，等待价格越过均衡水平后再行动。 | PDF p.375 |
| **Premium/Discount Four Subdivisions** | Premium内Premium、Premium内Discount、Discount内Premium、Discount内Discount四层嵌套结构。 | PDF p.381 |
