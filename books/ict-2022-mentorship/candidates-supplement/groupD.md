# Group D 补充提取 — Ch17 / Ch22 / Ch23 / Ch24 / Ch25 / Ch26

> 提取纪律：只录原文有的；缺参数标"原文未给出"；与已有能力重复标"已覆盖于 cap-XX"仅提增量。

---

## [GD-01] DXY-指数三场景模型
- type: framework
- source: PDF p.386–387
- mechanism: DXY 与 ES/NQ/YM 三种联动场景：① DXY 下跌 → ES/NQ/YM 上涨（risk-on）；② DXY 上涨 → ES/NQ/YM 下跌（risk-off）；③ DXY 盘整 → ES/NQ/YM 上涨。Risk-off 时外币与指数期货下跌自由更大、难反弹；Risk-on 时支持指数与外币上涨。原文："The growth of the US dollar index causes a decrease in the price of assets in dollar pairs, while the drop and consolidation of the index causes assets in dollar pairs to strengthen."
- chart_dependency: 中【需看图 PDF p.387（4图展示三场景示意）】
- counterexamples: 作者指出"There are also times when the S&P 500 and the US dollar both move up together"，通常发生在经济复苏期；三场景非穷尽，存在同向运动例外。
- mapping: 建议新增能力「dxy-index-correlation」— 作为 top-down 宏观过滤层，为 cap-04 daily-bias 提供跨市场确认信号；不与现有 cap 重叠。

## [GD-02] DXY/EURUSD/GBPUSD 季节性月份规律
- type: framework
- source: PDF p.389–398
- mechanism: 完整月度规律（作者明示"not absolute""not guarantees""should not be relied upon entirely"）：
  **通用季节**：Dec–Jan 盘整/流动性低/不利交易；Feb–Apr 趋势启动/高概率模型；May–Aug "Sell in May"夏季萧条/下跌+盘整/Aug休假；Sep–Nov 市场再启动/股市倾向上涨/新循环。
  **EURUSD**：① 2月中筑底→3月中走高→回调→4月底再攀；② 6月低点→7月底/8月初攀升；③ 8月初→9月初下跌；④ 9月初至9月底利好→10月初下跌；⑤ 10月后均值背离/信号不可靠。
  **GBPUSD**：① 3月初至3月底筑底→4月底走高；② 5月初至5月中熊市；③ 5月中筑底→8月初走高；④ 8月初见顶→9月初下跌；⑤ 11月初均线重排成顶→11月中下旬下滑→此后均值再背离。
  **DXY**（5/10/15年三周期共性）：① 年初至2月中向上偏向；② 2月中见顶→3月中下跌；③ 3月后半月强劲→4月下旬抛售；④ 5月初至5月中强势→5月底短期低点；⑤ 5月底至6月中可能升值；⑥ 6月中短期高点→7月底下跌；⑦ 8月初至9月初反弹；⑧ 11月初至11月底上涨；⑨ 12月下旬熊市。
- chart_dependency: 高【需看图 PDF p.390–397（多张季节性叠加图表）】
- counterexamples: 原文明确："Seasonal tendencies are not absolute""they are not guarantees""market conditions and other factors can influence the actual outcome""This is not a panacea." 10月后EURUSD/DXY均值背离，信号不可靠。
- mapping: 落实 ref-03 → 建议升级为能力「seasonal-tendency-filter」，作为 cap-04 daily-bias 的月度上下文过滤器；理由：原文给出精确到月份的转折点结构，可用于 bias 先验加权，但必须标注"非保证"。

## [GD-03] 区间高低点四种确定方式
- type: procedure
- source: PDF p.482–483
- mechanism: 确定交易区间 High/Low 的四种方法：① 导致对面横扫的高/低点（the high that led to the sweep of the range low）— 注意不是第一个高点，而是引发扫荡的那个；② 同侧扫描前的高/低点；③ Equal Highs & Lows — 相等高低点，目标明确且多数被扫；④ Previous daily/weekly/monthly range — 缩放到目标时间框架取蜡烛高低（可含影线或仅实体，以 midrange 对齐为准）。
- chart_dependency: 中【需看图 PDF p.482–483（图示四种区间界定）】
- counterexamples: 方法①"tricky to spot"，误用第一个高点会导致 midrange 不对齐；方法④影线vs实体选择取决于 midrange 匹配效果。
- mapping: 建议并入 cap-02 daily-static-anchors — 补充区间界定的操作细则；cap-02 目前覆盖 PDH/PDL/Asian range/CBDR，但未涵盖这四种通用区间确定法。

## [GD-04] Monday Range 完整操作流程
- type: procedure
- source: PDF p.485–487
- mechanism: 完整步骤：① 周一仅观察，等待 Monday Range（周一最高价至最低价）形成；② 周一收盘后标记 High/Low，不交易；③ 等待一侧 buy stops/sell stops 被扫 AND 价格回到区间内（"price moving too far away and not breaking back inside makes it more difficult"）；④ 扫止损+回区间后，寻找 MSS（Market Structure Shift）入场；⑤ 目标为区间对面；⑥ 若 HTF 订单流方向不明，在 midrange（50%）止盈使交易无风险。放弃条件：仅一侧被扫后变成支撑/阻力、或价格远离区间不太可能回来、或回区间后距离太远无法设合理失效点 → 放弃或换品种。
- chart_dependency: 高【需看图 PDF p.487（Monday Range 实例：低被扫→equal lows→MSS→反弹至高）】
- counterexamples: "Some weeks only one side gets taken out and turns into support/resistance"；价格远离区间时 setup 失效；HTF bearish 时可能是 bearish continuation range，不确定则 50% TP。
- mapping: 建议新增能力「monday-range-procedure」— 独立于 cap-02（锚标记）和 cap-10（ICT 2022 model），因其有独特的时间依赖流程（周一观察→周二起执行）和专属放弃条件。

## [GD-05] Daily Range 双叙事（亚洲盘整 vs 亚洲趋势）
- type: framework
- source: PDF p.488–491
- mechanism: 两套剧本基于亚洲时段幅度阈值（ES/SP500）：
  **叙事1：亚洲盘整 ≤10–15pt** → ① Asia ranging/consolidation；② London 扫 Asia BSL/SSL（Judas Swing）→ expansion  targeting opposite side；③ 价格在 LOKZ 内形成 low/high 并反转（London Swing）；④ NY session 为某种 retracement。
  **叙事2：亚洲趋势 >15pt** → LOKZ 入场较难/不够清晰；通常避免交易 LOKZ，等待 NYKZ；NYKZ 出现前趋势明显突破时入场，目标反转/回撤至 London BSL/SSL。具体：Asia trending bearish → LOKZ 在 Asia Premium 内开盘并跟随亚洲方向 → NYKZ 反转并扫 LOKZ + Asia Range 的 BSL。
  Session 链式 bias：Asia Session → creates bias for → London Session → creates bias for → New York Session。
- chart_dependency: 中【需看图 PDF p.488–491（LOKZ/NYKZ 特征对比表+双叙事示意）】
- counterexamples: 亚洲趋势>15pt 时 LOKZ 反转概率降低，不应强行套用叙事1；"some kind of Retracement" 表述模糊，NY 行为非确定。
- mapping: 建议并入 cap-01 session-taboo-filter（增量：亚洲幅度阈值 10-15pt 分流逻辑 + session 链式 bias 传导）+ cap-13 po3-amd-state-machine（增量：Judas Swing 在两种叙事中的不同位置）。已覆盖于 cap-01 的五 Killzone 窗口定义，此处仅提取幅度阈值分流与链式 bias 增量。

## [GD-06] LOKZ / NYKZ 特征对照
- type: glossary
- source: PDF p.490
- mechanism: LOKZ 特征：通常给出最清晰+最大摆动（London Swing）；最可能反转或回撤 LOKZ；最高概率形成当天 low/high。NYKZ 特征：高波动性和高成交量；经常被经济新闻操纵或影响；NYKZ 经常扫 LOKZ 的 BSL/SSL。
- chart_dependency: 低
- counterexamples: 原文未给出失效条件，但 NYKZ "often manipulated or influenced by economic news" 暗示新闻期间信号可靠性下降。
- mapping: 已覆盖于 cap-01 session-taboo-filter 的时间窗定义；此处增量为 LOKZ/NYKZ 的功能性特征描述（London Swing 概念、NYKZ 扫 LOKZ 流动性模式），建议并入 cap-01 注释或 cap-13 PO3 状态机。

## [GD-07] NWOG 画法与使用规则
- type: procedure
- source: PDF p.492–493
- mechanism: NWOG（New Week Opening Gap）= 周五收盘价与周日开盘价之间的价格区间。画法：使用低时间框架（如 5min 图），不用 1D 图；仅在 Regular Trading Hours（RTH）可见，Electronic trading hours 不可见。CE（Consequent Encroachment）= Fibonacci 从周五收盘锚定到周日开盘的 50% 中点。使用规则：① 像 FVG 一样对待 NWOG；② 价格可能回访并对 NWOG 做出反应；③ 价格尊重 NWOG 的 CE；④ 至少记录最近 5 个 NWOG；⑤ 多个 NWOG 聚集 → 市场进入区间震荡阶段。Up-gap = 支撑区；Down-gap = 阻力区。ICT 引述："Having the prior 4 weeks NWOG on your chart gives you an X-ray view of how the algorithm will refer back to old areas of real FAIR VALUE."
- chart_dependency: 中【需看图 PDF p.493–496（NWOG 标注示例+CE 示意）】
- counterexamples: "Price doesn't have to trade back to the Liquidity Void immediately"；多个 NWOG 聚集时市场区间震荡，单向交易概率降低。
- mapping: 落实 ref-05 子项 → 建议并入 cap-02 daily-static-anchors（增量：NWOG/NDOG 作为动态公允价值锚点，含 RTH-only 限制、5min 图要求、CE 中点计算、5个记录规则、聚集=震荡判据）。

## [GD-08] NDOG 定义与用法
- type: glossary
- source: PDF p.493
- mechanism: NDOG（New Day Opening Gap）= 5PM 收盘价与 6PM 开盘价之间的差额（原文未注明时区，按 ICT 惯例应为 EST/EDT纽约时间）。与 NWOG 同理视为真实流动性空洞和公允价值水平。
- chart_dependency: 低
- counterexamples: 原文未给出 NDOG 特有的失效条件；与 NWOG 共享"不立即回填"特性。
- mapping: 并入 cap-02 daily-static-anchors（增量：NDOG 作为日内级动态锚点，与 NWOG 互补）。

## [GD-09] Event Horizon PD Array
- type: calculation
- source: PDF p.495–496
- mechanism: Event Horizon = 两个相邻 NWOG 的中点之间的中间位置（"Halfway between a NWOG and the closest NWOG"）。功能：不允许价格逃脱对 NWOG 的吸引；当价格太"接近"某个 NWOG 但尚未到达时，Event Horizon 会创造朝向该 NWOG 的飙升。测量方法：取两个最近 NWOG 的 High-Low 范围，计算其中间点。
- chart_dependency: 高【需看图 PDF p.496（3图展示 Event Horizon 位置与价格行为）】
- counterexamples: 原文未给出失效条件；隐含前提是 NWOG 本身有效且未被完全回填。
- mapping: 落实 ref-05 子项 → 建议并入 cap-02 daily-static-anchors 或 cap-07 pd-array-block-dictionary（增量：Event Horizon 作为 PD Array 的新层级，位于 NWOG CE 之上）。

## [GD-10] 公允价值三要素判定
- type: procedure
- source: PDF p.497–498
- mechanism: 确定 Fair Value 的三个步骤：① 找出较大价格波动的总宏观范围（Premium or Discount）；② 确定 Equilibrium 价格点相对于最近交易区间高低点的位置；③ 找到做市商瞄准的参考点（FVGs、Liquidity Voids、Order Blocks）。Equilibrium = swing high 与 swing low 之间的 50% 线。在 Equilibrium 时价格可向任一方向运动，判断最可能方向的方法：找最近市场结构突破是 swing high 还是 swing low；同时注意价格在整体范围的下部/上部/中部位置。
- chart_dependency: 中【需看图 PDF p.498–504（Equilibrium 标注+做多案例）】
- counterexamples: "At Equilibrium (or Fair Value) price can go either direction"；"We don't know how long price will stay in a consolidation."
- mapping: 建议并入 cap-07 pd-array-block-dictionary（增量：Fair Value 三要素判定程序 + Equilibrium 作为方向歧义点的处理规则）；部分已覆盖于 cap-11 OTE（Discount/Premium 判定），此处增量为三要素结构化流程和 Equilibrium 蜡烛体信号。

## [GD-11] 蜡烛体 Equilibrium 信号
- type: principle
- source: PDF p.499
- mechanism: 当价格接近 Equilibrium 时观察蜡烛体：如果蜡烛体停留在 Equilibrium 一侧而影线穿过 Equilibrium，暗示价格可能在影线穿越后反转。原文："Does the bodies of the candles stay on one side of Equilibrium while the wicks cross it? This gives hints that price may reverse after the wicks go across the Equilibrium."
- chart_dependency: 中【需看图 PDF p.499 附近示意图】
- counterexamples: 仅为"hints"，非确定性信号；原文未给出失效率或反例。
- mapping: 建议并入 cap-10 ict-2022-model 或 cap-11 ote-entry-zone（增量：Equilibrium 处的蜡烛体确认信号，用于 OTE 入场过滤）。

## [GD-12] Liquidity Void 特征与回填行为
- type: framework
- source: PDF p.499–501
- mechanism: Liquidity Void 定义：价格在短时间内单方向大幅移动（相比近期蜡烛尺寸），留下大实体小影线蜡烛，交易活动极少。特征：长实体、小影线、有时大蜡烛间有小缺口。回填行为：价格回到 Void 时会上下插针（wick up and down），因为做市商在 Void 范围内卖出多头或回购空头。回填不必立即发生。Void 填满后，寻找更远端的 FVG 或 Order Block 作为做市商对冲位置。做市商视角：Void = 低效交易的价格范围，算法寻求再平衡。
- chart_dependency: 高【需看图 PDF p.501（4图展示 Void 回填插针行为）】
- counterexamples: "Sometimes it first goes higher, deceiving traders, and then completely fills it"——假突破欺骗；"Price doesn't have to trade back to the Liquidity Void immediately"——时间不确定。
- mapping: 建议并入 cap-06 fvg-three-candle（增量：Liquidity Void 作为 FVG 的极端形态，含回填插针行为模式和做市商对冲逻辑）；与 cap-06 的三蜡烛 FVG 互补，Void 强调单方向大幅运动的极端情况。

## [GD-13] 做市商循环：buy stops → sell stops → buy stops
- type: principle
- source: PDF p.503–507
- mechanism: 市场在做市商控制下循环运动：从 buy stops 到 sell stops，再从 sell stops 到 buy stops；从 Fair Value → Discount → Premium → Fair Value。做市商净多头时价格上涨符合其利益；散户买卖数量不影响价格设定。Fair Value in Discount = MM buy；Fair Value in Premium = MM sell。扩张前必有盘整；急剧运动后的大蜡烛是最低效交易区域。
- chart_dependency: 低
- counterexamples: 原文未给出循环失效条件；"We don't know how long price will stay in a consolidation" 为时间不确定性。
- mapping: 已覆盖于 cap-13 po3-amd-state-machine（Accumulation-Manipulation-Distribution 循环）；此处增量为明确的三断点循环表述（Fair Value/Discount/Premium）和 MM 净头寸逻辑，建议作为 cap-13 的理论注释补充。

## [GD-14] Ch25 时段增量细节（cap-01 未覆盖部分）
- type: procedure
- source: PDF p.508–514
- mechanism: 与 cap-01 五 Killzone 窗口比对后的增量：
  ① **00:00–02:00 EST**：sell day 后市场在此时段上涨（原文"Market rallies up in the sell day after 12:00 am EST to 02:00 am EST"）。
  ② **02:00–05:00 EST**：形成当日 swing high/low 的理想时间窗口（for sell trade: move back to higher of day forms swing high then continue down, or SMT Divergence）。
  ③ **05:00 EST 开盘价规则**：标记 05:00 EST 开盘价，多数时候此价格设置 NY OTE，与伦敦形成的 H/L 同步；若伦敦未见 Judas Swing，预期 Judas 在 05:00 EST 形成。
  ④ **05:00–06:00 EST**：伦敦运动后的价格停顿，或在低时间框架形成市场方向分形。
  ⑤ **07:20 EST ±10pt 规则**：期货合约 07:20 EST 开始交易（纽约 Killzone 开始后 20 分钟）；买入需在 07:20 开盘价下方 10pt（ES/SP500），卖出需在上方 10pt。
  ⑥ **10:00–11:00 EST**：sell trade 的 day low 通常在此形成；buy trade 反之。若在 LOKZ 卖出，需在 10:00–11:00 EST 附近平仓。
  ⑦ **London Close KZ 10:00–12:00 EST（最晚 13:00）**：获利回吐时段（伦敦收盘+纽约午餐）；可形成 day H/L；通常有 5min OTE setup；非常短期运动。看涨日 high 通常在 10:00–noon 形成。
  ⑧ **NY Session 开盘价规则**：Buy below 05:00 and 07:00 EST open price; Sell above 05:00 and 07:00 EST open price。
  注：以上时区均为 EST，原文未说明夏令时调整规则。
- chart_dependency: 中【需看图 PDF p.508–514（多张时段标注图）】
- counterexamples: "Most of the time" 反复出现，所有时段规则均为概率性而非确定性；原文未给出夏令时处理方式。
- mapping: 增量并入 cap-01 session-taboo-filter（新增 07:20 ±10pt 入场规则、05:00/07:00 开盘价买卖规则、London Close 5min OTE、02:00–05:00 理想窗口细化）；cap-01 原有五窗口定义不变，此处补充窗口内的精确操作参数。

## [GD-15] London Swing to NY Open / London Close Reversal 模板
- type: framework
- source: PDF p.516–518
- mechanism: 反转市场概况模板。看涨版本：像 Classic Buy 一样先跌至开盘价以下形成买入入场 → 价格反弹至 HTF POI（bearish OB/FVG）→ 若发生在 NY session 则为经典反转。监控时段：伦敦最后 1h（4–5am）+ 纽约第一小时（7–8am）（原文未注明时区，按上下文推测为 EST）。看涨日流程：伦敦创建 initial low → NY 在 London Close 附近创建 high → 回落清除伦敦 initial low。优势：利用伦敦/纽约重叠动量。
- chart_dependency: 高【需看图 PDF p.516–518（模板示意图+实例）】
- counterexamples: 若市场未按预期反转则亏损；重叠期波动增加可能导致突然价格跳空/缺口，难以预测。
- mapping: 落实 ref-04 子项 → 建议新增能力「daily-template-reversal」或在 cap-10 ict-2022-model 中增加模板分支；与 GD-16 Classic Buy/Sell Day 互为补充。

## [GD-16] Classic Buy/Sell Day 模板
- type: framework
- source: PDF p.519–521
- mechanism: 最佳盈利模板，大范围趋势日。主要出现在周一、周二，最迟周三伦敦时段。日线范围持续 7–8 小时。趋势通常持续到 11:00 EST。Classic Buy Day：在关键支撑位低于开盘价时买入；若价格先高于开盘价不要追，等它回到开盘价以下。开盘价到支撑距离平均 7–12pt（ES/SP500）；若伦敦时段从开盘到支撑超过 12pt，等纽约交易。12:00 前锁定 5–7pt 小利润（ES/SP500）。纽约时段给出回撤以延续伦敦设定的趋势。
- chart_dependency: 高【需看图 PDF p.519–521（Classic Buy/Sell Day 示意图+实例）】
- counterexamples: 若开盘价到支撑超 12pt 则伦敦入场风险增大，应等纽约；"mostly on Monday, Tuesday and latest on Wednesday" 暗示周四五概率降低。
- mapping: 落实 ref-04 子项 → 建议新增能力「daily-template-classic」；包含精确数值（7-12pt 支撑距离、12pt 阈值、5-7pt 止盈、11:00 EST 趋势终点、7-8h 持续时间），可直接编码为规则。

## [GD-17] Range to NY Open / London Close Rally 模板
- type: framework
- source: PDF p.521
- mechanism: 最常出现在 NFP、FOMC、利率公告期间。市场原本盘整 → 消息前价格打破 London Lows → 消息发布后反弹。
- chart_dependency: 高【需看图 PDF p.521（2图展示消息前后价格行为）】
- counterexamples: 仅限重大新闻事件触发；非新闻日不适用。
- mapping: 落实 ref-04 子项 → 建议并入 GD-18 Consolidation Raid 或作为 cap-01 新闻日特殊模板补充。

## [GD-18] Consolidation Raid on News Release 模板
- type: procedure
- source: PDF p.522
- mechanism: 最常出现在 NFP、FOMC、利率公告。流程：① 开盘后市场在消息前盘整；② 消息发布时价格下跌诱导交易者并扫止损（不必跌破盘整太多，但必须打破盘整）；③ 清除止损+诱导后价格走向真实方向；④ 识别盘整下方的关键支撑或 order block；⑤ 5 分钟规则：看价格是否在消息发布后 5 分钟内拒绝支撑/阻力，若不拒绝则离场（分析可能错误）。
- chart_dependency: 高【需看图 PDF p.522（2图展示 Consolidation Raid 流程）】
- counterexamples: 5 分钟内无拒绝 = 分析错误，必须离场；消息诱导方向可能与预期相反。
- mapping: 落实 ref-04 子项 → 建议新增能力「news-consolidation-raid」或在 cap-01 新闻禁忌日框架中增加"消息后 5min 确认规则"作为可交易例外。

---

## glossary-supplement

| 术语 | 定义 | 来源 |
|---|---|---|
| Event Horizon | 两个相邻 NWOG 中点之间的中间位置；不允许价格逃脱对 NWOG 的吸引，当价格过于接近但未到达某 NWOG 时创造朝向该 NWOG 的飙升。 | PDF p.495–496 |
| Protraction | 原文未在 Ch17/22–26 中出现此术语定义。（注：可能在其他章节定义，Group D 范围内未找到。） | — |
| London Swing | LOKZ 内形成的最清晰+最大摆动；价格在 LOKZ 内设定 low/high 后的反转运动，通常给出当天的高点或低点。 | PDF p.490, 516 |
| Opening Range | 原文未在 Ch17/22–26 中以独立术语定义；相关概念为 Monday Range（周一最高价至最低价）和 05:00/07:00 EST 开盘价规则。 | PDF p.485 |
| Monday Range | 周一最高价与最低价之间的价格区间；用于周二起的区间交易，等待一侧被扫并回区间后以 MSS 入场，目标对面。 | PDF p.485–487 |
| Consequent Encroachment (CE) | 任何 Gap 或 Inefficiency 的中点（50%）；NWOG 的 CE 通过 Fibonacci 从周五收盘锚定到周日开盘取得。 | PDF p.493 |
| Liquidity Void | 价格在短时间内单方向大幅移动留下的低效交易区域；特征为大实体小影线蜡烛；做市商视其为公允价值，价格倾向于回填（插针方式）。 | PDF p.499–501 |
| Fair Valuation | 做市商视角的公允价格区域；由宏观范围、Equilibrium、参考点（FVG/Void/OB）三要素确定；Equilibrium 本身即 Fair Value。 | PDF p.497–498, 502 |
| Equilibrium | Swing high 与 swing low 之间的 50% 中点线；在此位置价格可向任一方向运动，需参考最近 MSS 和范围位置判断偏向。 | PDF p.498 |
| Judas Swing | 假方向摆动，用于诱导和扫止损；在亚洲盘整叙事中发生于 LOKZ（扫 Asia BSL/SSL），在亚洲趋势叙事中可能延迟至 05:00 EST。 | PDF p.489, 509 |
