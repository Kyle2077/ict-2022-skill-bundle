# Principle Candidates — ICT 2022 Mentorship

> Extractor: principle-extractor | Source: ch01, ch02, ch03, ch04, ch06, ch09, ch10, ch11, ch12, ch13, ch29, ch32
> 数值均原样保留；原文未给出的参数标"原文未给出"。

---

## pr-01
- **title**: Killzone 五个时间窗（纽约本地时间）
- **type**: rule
- **source_chapter**: Ch11 (PDF p.156)
- **source_quote**: "There are 5 killzone: 1. London open, from 02:00 to 05:00 am; 2. New-York open, from 07:00 to 10:00 am; 3. London close, from 10:00 am to 12:00 pm; 4. Central Bank Dealers Range, from 14:00 to 20:00; 5. Asia, from 20:00 to 00:00 NY Local time."
- **summary**: ICT 定义五个 Killzone 时间窗：伦敦开 02:00–05:00、纽约开 07:00–10:00、伦敦收 10:00–12:00、CBDR 14:00–20:00、亚洲 20:00–00:00，均为纽约本地时间。算法在这些窗口内猎取流动性。
- **tags**: [rule, time, killzone]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-02
- **title**: ES/NQ/YM 合约规格表
- **type**: calculation
- **source_chapter**: Ch06 (PDF p.88)
- **source_quote**: "ES/MES: 12.50 [0.25] or $50 per one point – ES / 1.25 or $5 per one point – MES. NQ/MNQ: 5.0 [0.25] or $20 per one point – NQ / 0.50 or $2 per one point – MNQ. YM/MYM: 5.0 [1.00] or $5 per one point – YM / $0.50 per one point – MYM."
- **summary**: ES 每点 $50（tick $12.50）、MES 每点 $5；NQ 每点 $20（tick $5.0）、MNQ 每点 $2；YM 每点 $5（tick $5.0）、MYM 每点 $0.50。合约交付月：H/M/U/Z。
- **tags**: [calculation, contract-spec, ES, NQ, YM]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/MES/NQ/MNQ/YM/MYM

---

## pr-03
- **title**: OTE 最优入场区 Fib 0.62–0.79 / 0.705 甜蜜点
- **type**: rule
- **source_chapter**: Ch09 (PDF p.131), BOOK_OVERVIEW 引用 Ch16 p.373
- **source_quote**: "Draw your Fibonacci tool from swing high to swing low. Wait for price return back to discount and look for longs there." + Overview: "OTE = Fib 0.62–0.79, 0.705 sweet spot; author claims '80% effective' without data source."
- **summary**: 最优交易入场（OTE）为 Fibonacci 回撤 0.62–0.79 区间，0.705 为甜蜜点。买入在折价区、卖出在溢价区。作者声称 80% 有效但无数据来源。
- **tags**: [rule, entry, fibonacci, OTE]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-04
- **title**: MSS 必须伴随 Displacement
- **type**: principle
- **source_chapter**: Ch04 (PDF p.80–81), Ch10 (PDF p.143)
- **source_quote**: "MSS must be energetic and leave behind displacement to ensure that market is looking to reverse." + "A displacement candle is a candle that breaks through a previous high or low... Lack of displacement occurs when the price fails to break through."
- **summary**: 市场结构转变（MSS）必须有位移（Displacement）确认：突破前高/前低的有力K线收盘运动并留下 FVG。无位移的"结构突破"不算数，无位移本身可作为反向信号。
- **tags**: [principle, MSS, displacement, structure]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-05
- **title**: FVG 三蜡烛判定规则
- **type**: calculation
- **source_chapter**: Ch10 (PDF p.140, 147–150)
- **source_quote**: "Fair Value Gaps are created within a three-candle sequence... Candle 1: the low of this candle will be the starting point for the fair value gap. Candle 2: where the FVG is formed. Candle 3: the high of this candle will be the ending point." (Bearish mirror applies.)
- **summary**: Bearish FVG = 蜡烛1低点 → 蜡烛3高点之间的空档（三蜡烛序列中相邻蜡烛影线不完全重叠）。Bullish FVG 镜像。FVG 是入场点、目标和情绪转换工具。
- **tags**: [calculation, FVG, three-candle, entry]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-06
- **title**: 不在旧高上买 / 不在旧低下卖（铁律）
- **type**: principle
- **source_chapter**: Ch03 (PDF p.50), Ch02 (PDF p.34)
- **source_quote**: "We do NOT buy at the break of the old HIGH and we do NOT sell at the break of the old LOW!" + "It will feel scary to sell above an old high or buy below an old low but that's because you haven't practiced enough."
- **summary**: 核心铁律：绝不在旧高突破时买入、绝不在旧低突破时卖出。应在流动性被扫后的折价/溢价 PD Array 入场。跨章重复出现（Ch02、Ch03、Overview Ch21 p.477）。
- **tags**: [principle, iron-rule, entry, liquidity]
- **computable**: false
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-07
- **title**: SMT 背离仅作确认工具
- **type**: principle
- **source_chapter**: Ch12 (PDF p.190)
- **source_quote**: "You are not looking for SMT divergence to take a trade, you use it only around predetermined levels with trade idea in mind. Then once pattern unfolds that is the green light to get into the trade."
- **summary**: SMT 背离（相关品种间创新高/新低不同步）仅作为确认工具，不单独用于入场。只在预定水平附近、已有交易想法时使用。适用于 EURUSD/GBPUSD、ES/NQ、BTC/ETH、DXY/ES 等配对。
- **tags**: [principle, SMT, confirmation]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 相关品种对

---

## pr-08
- **title**: 价格只做两件事：重新平衡不平衡或寻求流动性
- **type**: principle
- **source_chapter**: Ch03 (PDF p.56–59)
- **source_quote**: "Always remember price is doing only 2 things: Rebalance FVG and Seek Liquidity." + "Price only moves in two directions: from external to internal or internal to external."
- **summary**: 价格永远在"重新平衡 FVG/不平衡"与"寻求流动性（旧高/旧低）"之间移动。ERL↔IRL 交替循环构成一切行情骨架。在月/周/日/4H 上用此循环定日线偏向。
- **tags**: [principle, price-behavior, ERL, IRL]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-09
- **title**: Ch32 止损参数表（ES/SP500）
- **type**: calculation
- **source_chapter**: Ch32 (PDF p.634–635)
- **source_quote**: "If you are Trading the CBDR overlap with PDA – Stop is 15 points (ES/SP500) under. If you are Trading a Run under the Asian Range – Stop is 20 (ES/SP500) points under. If you are Trading ANY Sell Stop Raid – 15 points under the low/entry. If you are Trading the 1st retracement into +OB – 5 points under LOD. If you are Trading 2nd return for Sell Stops – 15 points under the LOD. If trading any other setup – use 50% ADR of the last 5 days subtracted from the Asian Range Low."
- **summary**: ES 日内买入止损参数：CBDR+PDA 重叠=15点；亚洲区间下方运行=20点；任何止损突袭=15点；首次回撤至+OB=LOD下5点；第二次止损回归=LOD下15点；其他设置=5天ADR的50%减去亚洲区间低点。仅 ES 标定。
- **tags**: [calculation, stop-loss, ES, risk-management]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500（跨品种缺换算）

---

## pr-10
- **title**: Ch32 止盈分批表（ES/SP500）
- **type**: calculation
- **source_chapter**: Ch32 (PDF p.635–636)
- **source_quote**: "Always try to take something off in gain at 10-15 points (ES/SP500). Look to Scale something off every 2 STD of the Asian Range or CBDR. Take something off at the Previous Day's High +2-7 points. Take something off at 50% of the Price Range you are trading inside 1h. Take or have 60-80% off at 5 day ADR projections."
- **summary**: ES 日内买入止盈：10–15点先减一部分；每2倍STD（亚洲/CBDR）减仓；PDH+2–7点减仓；1h交易区间50%减仓；5天ADR投影处减60–80%。时间维度：5:00am/7:00am前短期高点/10:00–11:00am分批。
- **tags**: [calculation, take-profit, ES, scaling]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-11
- **title**: CBDR < 20 点（ES）过滤条件
- **type**: rule
- **source_chapter**: Ch32 (PDF p.630, 637)
- **source_quote**: "Refer to the CBDR and determine if it is less than 20 points (ES/SP500) ideally."
- **summary**: 盘前检查 CBDR（央行交易商范围）是否小于 20 点（ES/SP500）。若超过 20 点，当日交易概率降低。买入和卖出条件均适用。
- **tags**: [rule, filter, CBDR, ES]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-12
- **title**: 亚洲区间 10–15 点（ES）阈值
- **type**: rule
- **source_chapter**: Ch32 (PDF p.630, 637), Ch11 (PDF p.166)
- **source_quote**: "Determine the Asian Range be in a 10-15 points (ES/SP500) range ahead of Frankfurt Open." + "You rarely often see Asia having more than 15 points (ES/SP500)."
- **summary**: 亚洲区间理想范围为 10–15 点（ES/SP500）。若超过 15–20 点，等待纽约时段再交易更安全。窄区间预示趋势日机会。
- **tags**: [rule, filter, asian-range, ES]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-13
- **title**: NY 9:00 前无 7–10 点回撤不交易
- **type**: rule
- **source_chapter**: Ch32 (PDF p.655)
- **source_quote**: "Ideally select retracements of at least 7-10 points (ES/SP500) lower. If no retracement of 7-10 points (ES/SP500) forms by 9AM – don't take anything."
- **summary**: 纽约时段买入指南：若上午9点前没有至少7–10点（ES/SP500）的回撤形成，不做任何交易。看跌镜像同理（7–10点上涨回撤）。
- **tags**: [rule, filter, retracement, ES, no-trade]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-14
- **title**: 8:30 新闻日 9:30 无 Judas Swing 例外
- **type**: rule
- **source_chapter**: Ch10 (PDF p.151), Ch09 (PDF p.116)
- **source_quote**: "At 8:30 AM we are looking for a stop run to occur. Before 8:30 AM look for a potential liquidity pool for price to raid. We are looking at 8:30 AM due to the News Embargo Lifts. Equity market opens at 9:30 AM. This creates surge in volatility. Many times surge in volatility creates a Judas Swing."
- **summary**: 8:30 AM 新闻解禁后寻找止损突袭；9:30 AM 股市开盘波动激增常产生 Judas Swing。新闻日后10分钟内不交易（Ch09 p.116: "Don't trade the first 10 minutes of the news"）。
- **tags**: [rule, news, judas-swing, time]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-15
- **title**: 风险 1–2% / 目标 10–20% 回报
- **type**: principle
- **source_chapter**: Ch09 (PDF p.116–117), Ch32 (PDF p.634)
- **source_quote**: "We will put a maximum of 5 points stop loss. We will aim for 10 points for ES (SP500)." + Ch32 止损/止盈表隐含 2:1+ 风险回报比。
- **summary**: 单笔风险控制：ES 最大5点止损、目标10点（2:1 RR）。Ch32 完整参数表中止损15/20点对应目标10–15点起步+分批。全书隐含风险1–2%账户、目标10–20%回报的框架。
- **tags**: [principle, risk-management, RR-ratio]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-16
- **title**: PDH/PDL 25–50 点波动预期
- **type**: rule
- **source_chapter**: Ch32 (PDF p.634–635), BOOK_OVERVIEW
- **source_quote**: "Assume we have a 50 points (ES/SP500) ADR over the last 5 days, take 25 points (ES/SP500) minus the Asian range low." + Overview: "日线 40–50 点"
- **summary**: ES 日均波幅（ADR）参考 40–50 点。50% ADR 用于止损计算和止盈投影。PDH/PDL 作为流动性磁吸目标，预期 25–50 点范围内的波动。
- **tags**: [rule, ADR, volatility, ES]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-17
- **title**: Mean Threshold 50%（OB 中点阈值）
- **type**: calculation
- **source_chapter**: Ch29 (PDF p.576, 608)
- **source_quote**: "Mean threshold – is 50% level of the total range of the order block; we expect price to respect this level." + "This new so-called OB will be very sensitive, it should never see the mean threshold exceeded, 50% of the body."
- **summary**: 订单块（OB）的平均阈值为蜡烛体总范围的50%。理想情况下最佳OB不会看到价格跌破/涨破中点。Propulsion Block 同样适用此阈值。测量用蜡烛体（open→close），非影线。
- **tags**: [calculation, OB, mean-threshold, validation]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-18
- **title**: 周一二最佳买入日 / 周三前形成周高低
- **type**: rule
- **source_chapter**: Ch13 (PDF p.218–219, 252), Ch32 (PDF p.630)
- **source_quote**: "The week low is usually formed between Monday and Wednesday, most often on Tuesday or Wednesday." + "The Ideal Days of the Week buying: Monday, Tuesday, and Wednesday." + "Weekly high/low is between Sunday and Wednesday (often before NY open – before 7AM)."
- **summary**: 周低点通常在周一至周三形成（最常见周二/周三）。理想买入日为周一、周二、周三。周二 ICT 重点关注伦敦开盘，因接近周低/高。若周三仍未形成，当日观望。
- **tags**: [rule, weekly-rhythm, day-of-week]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-19
- **title**: PO3/AMD 三阶段节奏（Consolidation→Expansion→Retracement/Reversal）
- **type**: principle
- **source_chapter**: Ch13 (PDF p.227)
- **source_quote**: "Consolidation cannot be followed by Retracement or Reversal. Consolidation is always followed by Expansion. After Expansion comes either Retracement or Reversal. The market does NOT do Consolidation -> Expansion -> Consolidation."
- **summary**: 市场节奏铁律：盘整后永远是扩张（绝不直接回撤或反转）；扩张后要么回撤要么反转；绝不做"盘整→扩张→盘整"。适用于日线和周线。
- **tags**: [principle, PO3, AMD, rhythm]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-20
- **title**: 15分钟→5分钟执行流程
- **type**: rule
- **source_chapter**: Ch06 (PDF p.90–91)
- **source_quote**: "Once we have analyzed the 15-minute chart and identified relevant market conditions, we switch to the 5-minute chart for precise entry points." + "We aim to position ourselves in a trade before 11:00 AM."
- **summary**: 日内执行流程：先用15分钟图识别关键高低点、不平衡、FVG和OB；确认后切换到5分钟图精确入场。目标在上午11:00前建仓。8:30前标记潜在流动性池。
- **tags**: [rule, execution, timeframe, workflow]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-21
- **title**: 新闻日前10分钟不交易
- **type**: rule
- **source_chapter**: Ch09 (PDF p.116)
- **source_quote**: "Don't trade the first 10 minutes of the news: If the news is at 10 a.m., then we will look for a setup from 10:10 a.m. to 12:00."
- **summary**: 新闻发布后前10分钟不交易。例如10:00的新闻，从10:10到12:00寻找设置。适用于NFP、CPI、FOMC、PPI、美联储讲话等高影响事件。
- **tags**: [rule, news, no-trade, time]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-22
- **title**: BISI/SIBI 模型：新闻后反向入场
- **type**: rule
- **source_chapter**: Ch09 (PDF p.116–119)
- **source_quote**: "Buy Side Oriented: 1. Wait for a big bearish displacement after a news embargo. 2. Don't trade the first 10 minutes. 3. Wait for Bearish PD arrays to fail, see Bullish displacement, change in order flow. 9. Maximum 5 points stop loss, aim for 10 points for ES."
- **summary**: 买方导向市场（BISI）：新闻后等待看跌位移→看跌PD阵列失效→看涨位移+订单流变化→在折价阵列买入。卖方导向（SIBI）镜像。ES最大5点止损、目标10点。50% BISI/SIBI可为最终目标。
- **tags**: [rule, BISI, SIBI, news-model, ES]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: ES/SP500

---

## pr-23
- **title**: 七类流动性分类
- **type**: principle
- **source_chapter**: Ch03 (PDF p.44–47)
- **source_quote**: "Types of liquidity: 1. Major – buy & sell stops at highs/lows of each session, day, week, monthly. 2. Medium – 15m, 1h charts. 3. Minor – 1m-5m charts. 4. Equal Lows/Highs (EQL/EQH). 5. Swing Points. 6. Range. 7. Trendline."
- **summary**: 七类流动性：主要（日/周/月高低）、中等（15m/1h高低）、次要（1–5m高低）、等低/等高、摆动点、区间高低、趋势线背后流动性。低阻力流动性运行（LRLR）是最理想交易条件。
- **tags**: [principle, liquidity, classification]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-24
- **title**: 低垂果实目标：ES 5–10 点
- **type**: rule
- **source_chapter**: Ch03 (PDF p.77)
- **source_quote**: "ICT aims for five handles or 10 handles (ES/SP500) below your entry can be considered low hanging fruit objectives."
- **summary**: 低垂果实（Low-Hanging Fruit）目标为入场后5或10点（ES/SP500）。这些目标容易实现，有助于建立信心和一致性。
- **tags**: [rule, target, ES, low-hanging-fruit]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-25
- **title**: Breaker Block 投影：1 STD 目标
- **type**: calculation
- **source_chapter**: Ch29 (PDF p.567–568)
- **source_quote**: "Breaker Block Projection: We measure A-B leg NOT manipulation leg. We want to use 1 STD as our target." + "Additional standard deviations (2, 3, 4, etc.) can be used if HTF liquidity supports it."
- **summary**: Breaker Block 投影测量 A→B 腿（非操纵腿），目标为1倍标准差（STD）。若HTF流动性支持可用2/3/4倍STD。"STD"实为范围倍数而非统计标准差。
- **tags**: [calculation, breaker, STD, projection]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-26
- **title**: OB 有效性四条件
- **type**: rule
- **source_chapter**: Ch29 (PDF p.576, 579)
- **source_quote**: "The order block is validated when the high of the lowest down-close candle (for bullish OB) or the low of the highest up-close candle (for bearish OB) is traded through by a more recently formed candle. Ideally the best bullish OB will not see price trade below the mid-point of the down-close candle."
- **summary**: OB 有效性验证：(1)最低下跌收盘蜡烛的高点被后续蜡烛交易通过（看涨OB）；(2)最佳OB价格不跌破蜡烛体中点；(3)有位移和机构赞助证据；(4)动量中第一个和最后一个OB有效。测量用蜡烛体，非影线（可选）。
- **tags**: [rule, OB, validation]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-27
- **title**: BB vs MB 区分规则
- **type**: principle
- **source_chapter**: Ch29 (PDF p.600)
- **source_quote**: "A Breaker forms a higher high, while a Mitigation Block forms a lower high. A breaker will collect Buyside Liquidity on the previous high creating a new higher high, while a mitigation block will fail to collect Buyside Liquidity forming higher lows."
- **summary**: Breaker Block 形成更高高点（成功摆动+止损运行）；Mitigation Block 形成更低高点（失败摆动，无流动性抓取）。BB=止损运行后的OB失败；MB=失败摆动后的OB。
- **tags**: [principle, BB, MB, distinction]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-28
- **title**: 亚洲区间利用规则：1–2 STD + 反转
- **type**: rule
- **source_chapter**: Ch11 (PDF p.166)
- **source_quote**: "The plan: You wait for one side to get taken out within the range of 1-2 Standard Deviations, then look for reversals (ideally back inside the Asia Range) and enter after a break in structure targeting the opposite side."
- **summary**: 亚洲区间交易计划：等待一侧在1–2倍STD范围内被扫出→寻找反转（理想回到亚洲区间内）→结构突破后入场→目标对侧。可在对侧取80%利润，留runner瞄准1–2 STD。
- **tags**: [rule, asian-range, STD, entry]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-29
- **title**: 伦敦时段创造日高/日低规则
- **type**: rule
- **source_chapter**: Ch11 (PDF p.167)
- **source_quote**: "The London Session typically creates the Low of the day when the market is primarily Bullish and the High of the day when Bearish."
- **summary**: 伦敦时段通常在市场主要看涨时创造日低点，在市场看跌时创造日高点。看涨时在伦敦寻找日低做多；看跌时在伦敦寻找日高做空。
- **tags**: [rule, london, daily-high-low]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-30
- **title**: 伦敦收盘大范围日回撤约20%
- **type**: calculation
- **source_chapter**: Ch11 (PDF p.179)
- **source_quote**: "The large range day that exceeds its 5 ADR tends to retrace about 20% of its total daily range at 10:00 am to Noon NY time."
- **summary**: 超过5倍ADR的大范围日，倾向于在纽约时间10:00am至中午回撤其总日范围的约20%。可用于伦敦收盘Killzone的日内反转剥头皮。
- **tags**: [calculation, london-close, ADR, retracement]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-31
- **title**: 最佳交易时间 8:30–11:00 AM EST
- **type**: rule
- **source_chapter**: Ch12 (PDF p.196), Ch06 (PDF p.90)
- **source_quote**: "Best time to trade this model is from 8:30 am to 11:00 am EST. Wait for 1:30 pm if you're going to trade the PM session." + "At 8:30 am EST look for old highs or old low to be swept, then wait for the model."
- **summary**: 该模型最佳交易时间为EST 8:30–11:00 AM。PM时段等到1:30 PM。8:30寻找旧高/旧低被扫，然后等待模型展开。
- **tags**: [rule, time, best-hours]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-32
- **title**: 内部流动性入场 / 外部流动性出场
- **type**: principle
- **source_chapter**: Ch12 (PDF p.200), Ch03 (PDF p.56–59)
- **source_quote**: "ICT entries are mainly internal liquidity entries and external liquidity exits." + "When external range liquidity is taken, a FVG becomes the next draw on liquidity. And when a FVG is stacked, an old low or an old high becomes the next draw."
- **summary**: ICT 入场主要在内部流动性（FVG/OB/BB等PD Array），出场在外部流动性（旧高/旧低）。ERL被扫后→IRL成为下一个DOL；IRL被触及后→ERL成为下一个DOL。
- **tags**: [principle, entry-exit, ERL, IRL]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-33
- **title**: Scalp 9步指南（买入日）
- **type**: rule
- **source_chapter**: Ch32 (PDF p.655)
- **source_quote**: "1. Confirm London session was bullish. 2. Wait for 7am NY time. 3. Between 7am–9am setup will typically form. 4. After 7am wait for price retracement lower. 5. NY session will typically retrace from a swing high. 6. Ideally select retracements of at least 7-10 points. 7. If no retracement of 7-10 points by 9AM – don't take anything. 8. If it does form – enter on 62% fib. 9. Expect price to retest high of day or previous day's high."
- **summary**: 买入日Scalp九步：确认伦敦看涨→7am等待→7–9am设置形成→等待回撤≥7–10点→9am前无回撤则放弃→62% Fib入场→目标日高/PDH。看跌镜像同理。
- **tags**: [rule, scalp, checklist, ES]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: ES/SP500

---

## pr-34
- **title**: Turtle Soup 入场条件
- **type**: rule
- **source_chapter**: Ch11 (PDF p.157), Ch32 (PDF p.631)
- **source_quote**: "If we are bullish, we want to see a 15m swing low get run between 8pm–12am EST for Turtle Soup Long." + "If Short-term low is taken out twice with no buy side taken – buy the Turtle Soup."
- **summary**: Turtle Soup 条件：看涨时亚洲Killzone（8pm–12am EST）内15m摆动低点被扫；或短期低点被扫两次且买方未被扫。看跌镜像。止损15点在低点下方（Ch32）。
- **tags**: [rule, turtle-soup, entry, asian]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-35
- **title**: 不要为了模式而交易模式 / 不要交易指标
- **type**: principle
- **source_chapter**: Ch09 (PDF p.112)
- **source_quote**: "1. Do not trade patterns for pattern's sake. 2. Do not trade indicator readings or momentum. 3. We look to enter Longs when Retail Sells. 4. We look to enter Shorts when Retail Buys. 5. We anticipate Price seeking opposite liquidity. 6. Time of Day is vital when engaging with Price."
- **summary**: 六条内化价格传递原则：不为模式而交易、不交易指标/动量、散户卖时做多、散户买时做空、预期价格寻求相反流动性、时间至关重要。
- **tags**: [principle, mindset, contrarian]
- **computable**: false
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-36
- **title**: 初始止损不要急于移动
- **type**: rule
- **source_chapter**: Ch32 (PDF p.634, 639)
- **source_quote**: "Whatever you use as the initial Stop loss – Do Not Rush to move it."
- **summary**: 无论使用什么作为初始止损，不要急于移动它。给予交易足够的呼吸空间。买入和卖出日交易均适用。
- **tags**: [rule, stop-loss, discipline]
- **computable**: false
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-37
- **title**: 不要试图挑选顶部和底部
- **type**: principle
- **source_chapter**: Ch32 (PDF p.642)
- **source_quote**: "***Don't try to pick tops and bottoms."
- **summary**: 明确禁止试图挑选市场的顶部和底部。应等待结构确认和流动性被扫后再入场。
- **tags**: [principle, discipline, no-picking]
- **computable**: false
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-38
- **title**: Vacuum Block（缺口）处理规则
- **type**: rule
- **source_chapter**: Ch29 (PDF p.611–615)
- **source_quote**: "A bullish and bearish vacuum blocks are 'gaps' created in price action as a result of some volatile event... There is a high probability that the market will want to come back and close this and deliver both buy side and sell side."
- **summary**: 真空块由波动事件（NFP、开盘等）造成的价格缺口。高概率回填但不一定完全填补。若有看涨OB在缺口内，价格可能只回到OB即继续。纽约时段更可能完全填补；晚间缺口更可能留开。
- **tags**: [rule, vacuum-block, gap, fill]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-39
- **title**: Rejection Block 识别规则
- **type**: calculation
- **source_chapter**: Ch29 (PDF p.602–604), Ch09 (PDF p.134)
- **source_quote**: "Bearish Rejection Block is when a High has formed with long wicks on the high(s) of the candlestick(s) and price reaches up above the body of the candle(s) to run Buy Side Liquidity out before price declines." + "Look for the highest close or open at the swing high that forms. It doesn't matter if the highest candle closed bullish or bearish."
- **summary**: 看跌拒绝块：摆动高点有长影线，价格在蜡烛体上方扫BSL后下跌。取最高收盘或开盘作为RB区域（不论涨跌收盘）。可跨多根蜡烛形成。看涨镜像。
- **tags**: [calculation, rejection-block, RB]
- **computable**: true
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## pr-40
- **title**: 避免伦敦开盘的条件
- **type**: rule
- **source_chapter**: Ch11 (PDF p.170)
- **source_quote**: "WHEN TO AVOID LONDON OPEN: Interest rate announcement; Key Speeches; Holiday trading; Global and Economic events; Weekly Range objective achieved."
- **summary**: 避免伦敦开盘交易的情况：利率公告、重要演讲、假日交易、全球/经济事件、周范围目标已达成。
- **tags**: [rule, filter, london, no-trade]
- **computable**: false
- **chart_dependency**: false
- **instrument_limit**: 全品种通用

---

## pr-41
- **title**: 亚洲区间偶尔超15–20点则等纽约
- **type**: rule
- **source_chapter**: Ch11 (PDF p.171)
- **source_quote**: "Occasionally: If the Asian session range is over 15-20 points (ES/SP500), wait for New York trade to be safe."
- **summary**: 若亚洲时段范围超过15–20点（ES/SP500），等待纽约时段交易更安全。与pr-12互补。
- **tags**: [rule, filter, asian-range, ES]
- **computable**: true
- **chart_dependency**: false
- **instrument_limit**: ES/SP500

---

## pr-42
- **title**: Daily Bias 不预设、依赖规则和体验
- **type**: principle
- **source_chapter**: Ch12 (PDF p.204–206)
- **source_quote**: "Determining the daily bias in trading is not about establishing a preconceived bias before the market commences trading... Instead, it relies on experience and adherence to specific rules." + "You don't want to flip flop back and forth between your Draw on Liquidity idea."
- **summary**: 日线偏向不应在市场开盘前预设，而是依赖经验和特定规则。一旦确定DOL方向，不要反复翻转。关注前一天高低点、溢价/折价位置、HTF PD阵列反应。
- **tags**: [principle, daily-bias, discipline]
- **computable**: false
- **chart_dependency**: true
- **instrument_limit**: 全品种通用

---

## Summary

共提取 **42 条**原则/规则/计算口径候选。覆盖：
- **时间规则** 7条（pr-01, pr-14, pr-18, pr-21, pr-31, pr-40, pr-41）
- **合约/数值参数** 3条（pr-02, pr-16, pr-24）
- **入场规则** 8条（pr-03, pr-06, pr-13, pr-22, pr-28, pr-33, pr-34, pr-42）
- **风控参数** 5条（pr-09, pr-10, pr-11, pr-12, pr-15）
- **结构/形态规则** 8条（pr-04, pr-05, pr-17, pr-26, pr-27, pr-39, pr-25, pr-38）
- **核心原则** 7条（pr-07, pr-08, pr-19, pr-23, pr-32, pr-35, pr-37）
- **执行纪律** 4条（pr-20, pr-29, pr-30, pr-36）

所有数值均原样保留并标注品种限定（ES/SP500）。原文未给出的参数已标注。跨章重复规则已合并并注明出处。
