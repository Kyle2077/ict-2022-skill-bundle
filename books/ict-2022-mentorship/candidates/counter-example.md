# 反例提取器产出 — ICT 2022 Mentorship

> 提取范围：ch01, ch02, ch03, ch04, ch06, ch09, ch10, ch11, ch12, ch13, ch29, ch32
> 纪律：仅收录作者**明确说过**的警告/失效条件；推断风险单独标注。

---

## cx-01 · 不在旧高之上买入 / 不在旧低之下卖出

- **失败模式名称**: 在旧高突破时追买 / 在旧低跌破时追卖
- **作者原话警告**: "We do NOT buy at the break of the old HIGH and we do NOT sell at the break of the old LOW!"（ch03）
- **触发条件**: 价格突破旧高或旧低时，散户因FOMO追入 breakout 方向，但该突破实为做市商扫止损的操纵动作。
- **对应正向规则**: 等待扫完流动性后的反转信号（Turtle Soup / Stop Run），在折价区买入、溢价区卖出。
- **原文出处**: PDF p.51（ch03 line 322）
- **可编码为检查项**: 是。布尔规则：`entry_price > previous_swing_high && direction == LONG → REJECT`；`entry_price < previous_swing_low && direction == SHORT → REJECT`。

---

## cx-02 · FOMC/NFP 等重大新闻日不交易

- **失败模式名称**: 在高影响新闻发布时段强行交易
- **作者原话警告**: "Don't trade the first 10 minutes of the news: If the news is at 10 a.m., then we will look for a setup from 10:10 a.m. to 12:00."（ch09）；"The news we are interested in are the NFP, CPI, FOMC, PPI, FED talks."（ch09）
- **触发条件**: NFP/CPI/FOMC/PPI/美联储讲话发布前后，波动率激增且方向不可预测，算法行为异常。
- **对应正向规则**: 使用经济日历标记禁忌时段；新闻后至少等10分钟再寻找setup；或整日回避。
- **原文出处**: PDF p.88–91（ch09 line 106–172）
- **可编码为检查项**: 是。维护新闻日历API，`if high_impact_news_within(±30min) → BLOCK_TRADE`。

---

## cx-03 · 亚洲区间 >15–20 点(ES) 时伦敦交易危险

- **失败模式名称**: 亚洲时段已大幅波动后仍按常规伦敦模板入场
- **作者原话警告**: "Occasionally: If the Asian session range is over 15-20 points (ES/SP500), wait for New York trade to be safe."（ch11）
- **触发条件**: 亚洲时段已经产生了超出正常范围的波动（>15–20点ES），说明算法已在亚洲完成部分分配，伦敦开盘可能无典型Judas Swing或方向混乱。
- **对应正向规则**: 亚洲区间超阈值时跳过伦敦Killzone，等待纽约时段再评估。
- **原文出处**: PDF p.170（ch11 line 269–271）
- **可编码为检查项**: 是。`asian_range_points > 20 → SKIP_LONDON_KILLZONE`。

---

## cx-04 · NY 9:00 前无 7–10 点回撤不交易

- **失败模式名称**: 纽约开盘前没有足够回撤就急于入场
- **作者原话警告**: "If no retracement of 7-10 points (ES/SP500) forms by 9AM - don't take anything."（ch32）
- **触发条件**: 看涨日中价格在7am–9am之间未从日内高点回撤至少7–10点，说明缺乏足够的折价入场机会，强行入场等于在溢价区买入。
- **对应正向规则**: 等待至少7–10点回撤后再在OTE(Fib 0.62)入场；无回撤则当日放弃。
- **原文出处**: PDF p.655（ch32 line 551–553）
- **可编码为检查项**: 是。`if bias==BULL && max_retrace_from_swing_high < 7 by 09:00 ET → NO_TRADE`。

---

## cx-05 · SMT 背离不单独入场

- **失败模式名称**: 仅凭SMT背离信号就直接开仓
- **作者原话警告**: "You are not looking for SMT divergence to take a trade, you use it only around predetermined levels with trade idea in mind. Then once pattern unfolds that is the green light to get into the trade."（ch12）
- **触发条件**: 看到EURUSD/GBPUSD或ES/NQ之间出现SMT裂缝就直接入场，而没有预先确定的PD Array水平和方向偏向。
- **对应正向规则**: SMT仅作确认工具；必须先有方向偏向+预定水平+其他结构信号，SMT才作为绿灯。
- **原文出处**: PDF p.190（ch12 line 128–132）
- **可编码为检查项**: 是。`if signal_source == SMT_ONLY && !has_predetermined_level → REJECT`。

---

## cx-06 · 无 Displacement 不算 MSS

- **失败模式名称**: 把无位移的价格穿越当作有效市场结构转变
- **作者原话警告**: "It is important to note that Market Structure Shifts should not be forced or anticipated without valid signals. Traders should wait for price action to validate their analysis before considering a Market Structure Shift."（ch04）；"If there is no displacement and the market immediately moves back into the range, it's best to wait for a clearer signal."（ch10）
- **触发条件**: 价格短暂穿越前高/前低但没有大蜡烛收盘确认（无Displacement），交易者误判为MSS并据此入场。
- **对应正向规则**: MSS必须伴随Displacement（大蜡烛收盘突破结构+留下FVG）；无位移本身是反向信号。
- **原文出处**: PDF p.82（ch04 line 66–70）；PDF p.144（ch10 line 112–116）
- **可编码为检查项**: 是。`if structure_break && !displacement_candle(body_size > threshold && close_beyond_level) → INVALID_MSS`。

---

## cx-07 · 前K线高点抵消第三K线低点则非 FVG

- **失败模式名称**: 把已平衡的三蜡烛序列误认为FVG
- **作者原话警告**: "The illustration below does not depict a Fair Value Gap, as the previous candle's high level has counterbalanced the low level of the third candle. This price action is considered to be balanced."（ch10）
- **触发条件**: 三根K线序列中，蜡烛1的高点与蜡烛3的低点重叠或交叉，中间大蜡烛的间隙已被填补，不构成真正的不平衡。
- **对应正向规则**: FVG要求蜡烛1的低点与蜡烛3的高点之间存在未被覆盖的空档（bearish FVG）或蜡烛1高点与蜡烛3低点之间的空档（bullish FVG）。
- **原文出处**: PDF p.141（ch10 line 45–49）
- **可编码为检查项**: 是。`if candle1.high >= candle3.low (bullish) || candle1.low <= candle3.high (bearish) → NOT_FVG`。

---

## cx-08 · 止损不要急于移动

- **失败模式名称**: 入场后立即收紧止损导致被正常波动扫出
- **作者原话警告**: "Whatever you use as the initial Stop loss - Do Not Rush to move it."（ch32）
- **触发条件**: 交易者入场后因焦虑过早将止损移至盈亏平衡点或更紧位置，价格正常回撤时被扫出后朝原方向运行。
- **对应正向规则**: 初始止损按规则设定（CBDR overlap 15点、Asian Range run 20点、Sell Stop Raid 15点等），给价格足够呼吸空间。
- **原文出处**: PDF p.634（ch32 line 146–147）
- **可编码为检查项**: 否（纪律性规则，需人工遵守；可编码为提醒：`if stop_moved_within(X_min_of_entry) → WARNING`）。

---

## cx-09 · London Close 可能反转日/周方向

- **失败模式名称**: 在伦敦收盘时段忽视反转风险，继续持有顺势仓位
- **作者原话警告**: "London Close can be used for intraday reversals on Large Range Days for scalps. The large range day that exceeds its 5 ADR tends to retrace about 20% of its total daily range at 10:00 am to Noon NY time."（ch11）；"What was the main movement of the Day or the Week may change during the London Close."（ch11）
- **触发条件**: 大范围日（超过5倍ADR）在伦敦收盘时段（10:00am–Noon NY），价格已完成主要目标，算法开始反向交付。
- **对应正向规则**: 大范围日在London Close时段考虑减仓/反转；不要用日内趋势惯性思维忽略此时段。
- **原文出处**: PDF p.179–180（ch11 line 397–412）
- **可编码为检查项**: 是。`if daily_range > 5 * ADR_5day && time_in(10:00-12:00 NY) → ALERT_REVERSAL_RISK`。

---

## cx-10 · 8:30 有重大新闻则 9:30 无 Judas Swing

- **失败模式名称**: 8:30已有新闻发布后仍在9:30等待Judas Swing入场
- **作者原话警告**: "When significant market-moving news is released at 8:30 am, it often means that there won't be a Judas Swing at 9:30 am."（ch13）
- **触发条件**: 8:30 AM已有NFP/CPI等高影响新闻发布，新闻解禁已触发波动和流动性猎取，9:30股票开盘时的典型Judas Swing不再发生。
- **对应正向规则**: 8:30有重大新闻时，将Judas Swing窗口调整到新闻发布后的10分钟内（如8:30–8:40），而非9:30。
- **原文出处**: PDF p.260（ch13 line 754–757）
- **可编码为检查项**: 是。`if high_impact_news_at(08:30) → JUDAS_WINDOW = 08:30-08:40, NOT 09:30`。

---

## cx-11 · Consolidation 后不会直接 Retracement / Reversal

- **失败模式名称**: 预期盘整后直接回撤或反转而跳过扩张阶段
- **作者原话警告**: "Again, Consolidation cannot be followed by Retracement or Reversal. Consolidation is always followed by Expansion."（ch13）；"The market does NOT do Consolidation -> Expansion -> Consolidation."（ch13）
- **触发条件**: 交易者在盘整结束后预期价格会直接回撤或反转，但实际上下一步永远是Expansion（扩张），回撤/反转只在扩张之后才可能发生。
- **对应正向规则**: 正确序列是 Consolidation → Expansion → Retracement/Reversal；盘整后应预期扩张方向并顺势操作。
- **原文出处**: PDF p.227（ch13 line 217–226）
- **可编码为检查项**: 是。状态机规则：`if current_phase == CONSOLIDATION → next_phase MUST BE EXPANSION; RETRACEMENT/REVERSAL only after EXPANSION`。

---

## cx-12 · 周三低点后继续下跌当日停手

- **失败模式名称**: 看涨周内周三已形成低点后价格继续下跌仍坚持做多
- **作者原话警告**: "If Wednesday puts in the low and we go lower, stand sideways on the day. Stop and submit to the fact you are wrong. It will happen, it happened to me."（ch13）
- **触发条件**: 在看涨周的PO3模型中，周三已形成周低点但价格继续走低，说明本周偏向判断错误或市场节奏异常。
- **对应正向规则**: 周三低点后若继续下跌，当日停止交易，承认错误，不逆势加仓。
- **原文出处**: PDF p.252（ch13 line 594–597）
- **可编码为检查项**: 是。`if day_of_week == WED && weekly_low_formed && price < weekly_low → STOP_TRADING_TODAY`。

---

## cx-13 · CBDR > 20 点不适合日内

- **失败模式名称**: CBDR范围过大时仍按标准参数日内交易
- **作者原话警告**: "Refer to the CBDR and determine if it is less than 20 points (ES/SP500) ideally."（ch32，买入日和卖出日条件均重复此条）
- **触发条件**: CBDR（14:00–20:00 NY的1h蜡烛体范围）超过20点，表明市场已在该时段过度波动，后续STD投影失真，标准止损/目标参数不再适用。
- **对应正向规则**: CBDR < 20点时才使用标准1-2 STD投影和15/20点止损；超阈值时降低仓位或跳过。
- **原文出处**: PDF p.630, 637（ch32 line 69–70, 227–228）
- **可编码为检查项**: 是。`if CBDR_points > 20 → REDUCE_POSITION_OR_SKIP`。

---

## cx-14 · ITH/ITL 被违反则场边观望

- **失败模式名称**: ITH/ITL被突破后仍按原偏向交易
- **作者原话警告**: "The ITH/ITL shouldn't be violated, it's a key high/low. If the ITH/ITL gets broken wait on the sidelines and observe. If you think price can go either way and have no clear bias then that's low probability."（ch32）
- **触发条件**: 内部时间框架高点(ITH)或低点(ITL)被价格突破，原有市场结构被破坏，方向偏向失去依据。
- **对应正向规则**: ITH/ITL被违反后立即停止交易，在场边观察直到新的清晰偏向形成。
- **原文出处**: PDF p.644（ch32 line 356–362）
- **可编码为检查项**: 是。`if price_breaks(ITH) || price_breaks(ITL) → SIDELINE_MODE`。

---

## cx-15 · 弹跳越多的支撑阻力越容易被扫

- **失败模式名称**: 把多次反弹的支撑/阻力当作"强"水平而依赖其防守
- **作者原话警告**: "Where price consistently bounces from the level of support or the level of resistance several times, there is a huge number of stops of some players and orders in the opposite direction of other players... The more bounces, the better."（ch03）
- **触发条件**: 某个支撑/阻力位被反复测试和反弹，散户认为该水平"很强"而在此设置止损，但实际上该水平积累了大量流动性，是做市商优先猎取的目标。
- **对应正向规则**: 多次反弹的水平是高概率流动性猎取目标；应在该水平被扫后寻找入场，而非依赖该水平防守。
- **原文出处**: PDF p.52–53（ch03 line 343–351）
- **可编码为检查项**: 是。`bounce_count(level) >= 3 → MARK_AS_HIGH_PROBABILITY_LIQUIDITY_TARGET`。

---

## cx-16 · 盲目跟随交易模式或指标而不考虑市场动态

- **失败模式名称**: 仅靠技术指标/形态交易，忽视流动性和叙事
- **作者原话警告**: "Many retail traders fall into the trap of blindly following trading patterns or indicators without considering the underlying market dynamics."（ch09）
- **触发条件**: 交易者看到技术形态（头肩顶、双底等）或指标信号就直接入场，没有分析当前的流动性分布、DOL、时段和机构叙事。
- **对应正向规则**: 技术分析只是拼图的一块；必须以流动性分析和市场叙事为核心框架。
- **原文出处**: PDF p.88（ch09 line 88–93）
- **可编码为检查项**: 否（认知层面的纪律，无法直接编码；可作为检查清单提醒项）。

---

## cx-17 · 无效订单块不应交易

- **失败模式名称**: 在不满足有效性条件的OB上入场
- **作者原话警告**: "Invalid order blocks lack the necessary conditions and should not be considered for trading."（ch29）；有效OB四条件：smart money支持、动量方向最高蜡烛、央行目标、之后无重大修正。（ch29）
- **触发条件**: 识别出的"OB"缺少Displacement、不是动量最后一推、之后有大幅修正穿透mean threshold，或未被聪明钱赞助。
- **对应正向规则**: OB必须满足四个有效性条件；最佳OB不应看到价格交易超过蜡烛体50%（mean threshold）。
- **原文出处**: PDF p.577–580（ch29 line 509–564）
- **可编码为检查项**: 是。`if OB && (penetration > 50% body || no_displacement_after || significant_correction) → INVALID_OB`。

---

## cx-18 · Propulsion Block 极敏感，不应超过 mean threshold

- **失败模式名称**: 把Propulsion Block当普通OB处理，给予过宽容忍度
- **作者原话警告**: "This new so-called OB will be very sensitive, it should never see the mean threshold exceeded, 50% of the body."（ch29）
- **触发条件**: Propulsion Block（推进块）是特殊类型的OB，如果价格穿透其蜡烛体50%，则该块失效，不应继续持有基于它的仓位。
- **对应正向规则**: Propulsion Block的容忍度严于普通OB；超过50%即判定失效。
- **原文出处**: PDF p.608（ch29 line 922–924）
- **可编码为检查项**: 是。`if block_type == PROPULSION && penetration > 50% body → INVALIDATE`。

---

## cx-19 · 安静时段避免开新仓

- **失败模式名称**: 在纽约收盘与亚洲开盘之间的低流动性时段开新仓
- **作者原话警告**: "During these times, traders may want to avoid taking new positions and instead focus on managing existing positions."（ch13）
- **触发条件**: 纽约收盘后至亚洲开盘前的安静期，流动性稀薄，滑点增大，价格行为不可靠。
- **对应正向规则**: 安静时段只管理现有仓位，不开新仓。
- **原文出处**: PDF p.251（ch13 line 552–559）
- **可编码为检查项**: 是。`if time_in(NY_close_to_Asia_open) → BLOCK_NEW_ENTRY`。

---

## cx-20 · 重新平衡 FVG 的高/低点不应被突破

- **失败模式名称**: FVG被重新平衡后其锚定高/低点被突破仍维持原偏向
- **作者原话警告**: "The high/low that rebalances a FVG should not get taken out, otherwise you might have the wrong bias."（ch32）
- **触发条件**: 用于重新平衡FVG的那根蜡烛的高点或低点被后续价格突破，说明该FVG的机构赞助可能已失效，原偏向可能错误。
- **对应正向规则**: FVG重新平衡的锚定K线高/低点被突破 → 重新评估偏向。
- **原文出处**: PDF p.644（ch32 line 353–355）
- **可编码为检查项**: 是。`if FVG_rebalance_candle.high_taken_out || .low_taken_out → REASSESS_BIAS`。

---

## cx-21 · 不要在新闻发布前10分钟内交易

- **失败模式名称**: 新闻发布瞬间抢单
- **作者原话警告**: "Don't trade the first 10 minutes of the news: If the news is at 10 a.m., then we will look for a setup from 10:10 a.m. to 12:00."（ch09）
- **触发条件**: 新闻发布后的前10分钟，价差极大、滑点严重、方向混沌，算法正在猎取两侧流动性。
- **对应正向规则**: 新闻后等10分钟，待订单流稳定后再寻找setup。
- **原文出处**: PDF p.88–89（ch09 line 106–109）
- **可编码为检查项**: 是。`if time_since(news_release) < 10 min → BLOCK_TRADE`。

---

## cx-22 · 避免分析过度复杂化

- **失败模式名称**: 叠加过多指标和分析维度导致分析瘫痪
- **作者原话警告**: "Avoid overcomplicating your analysis and focus on key concepts."（ch01）
- **触发条件**: 交易者试图同时使用多个时间框架、多种指标、多个理论，导致互相矛盾的信号和决策延迟。
- **对应正向规则**: 聚焦核心概念（时间、价格、结构三轴），保持分析简洁。
- **原文出处**: PDF p.17（ch01 line 104）
- **可编码为检查项**: 否（认知纪律，可作为检查清单提醒）。

---

## cx-23 · 10:00 AM 有新闻时 Judas Swing 延后到 10:00–10:10

- **失败模式名称**: 10:00有预定新闻时仍在9:30等待Judas Swing
- **作者原话警告**: "When news is scheduled for 10:00 am, we do not expect to see a Judas Swing at 9:30 am. Instead, we wait between 10:00 am and 10:10 am for the liquidity level to be taken out, giving us the Judas Swing."（ch13）
- **触发条件**: 10:00 AM有预定高影响新闻，算法将Judas Swing推迟到新闻发布时刻，9:30不会出现典型的假突破。
- **对应正向规则**: 10:00有新闻时，Judas Swing窗口 = 10:00–10:10；9:30不做Judas预期。
- **原文出处**: PDF p.262（ch13 line 790–798）
- **可编码为检查项**: 是。`if scheduled_news_at(10:00) → JUDAS_WINDOW = 10:00-10:10`。

---

## cx-24 · 避免伦敦开盘的明显原因

- **失败模式名称**: 在利率公告、关键演讲、假日、全球事件、周目标已达成时仍交易伦敦开盘
- **作者原话警告**: "WHEN TO AVOID LONDON OPEN: Interest rate announcement, Key Speeches, Holiday trading, Global and Economic events, Weekly Range objective achieved."（ch11）
- **触发条件**: 上述任一条件成立时，伦敦开盘的典型模板（Judas Swing → Expansion）不适用，算法行为偏离常态。
- **对应正向规则**: 盘前检查这些条件，任一命中则跳过伦敦Killzone。
- **原文出处**: PDF p.170–171（ch11 line 253–267）
- **可编码为检查项**: 是。布尔检查清单：`rate_announcement || key_speech || holiday || global_event || weekly_target_met → SKIP_LONDON`。

---

## 提取器补充，非原文

> 以下为提取器基于原文逻辑推断的风险，作者未在目标章节中明确以警告形式表述。

### cx-supp-01 · 模拟交易心态不等于实盘

- **推断依据**: ch01讨论了demo trading的挑战（line 66–77），但作者未明确说"demo成功≠实盘成功"作为警告，而是以建议形式呈现。
- **风险**: 模拟交易中无情绪压力，可能导致过度自信进入实盘。

### cx-supp-02 · 跨品种参数未换算

- **推断依据**: BOOK_OVERVIEW批判部分指出所有精确参数仅针对ES/SP500，但作者未在目标章节中明确警告"不要直接套用到其他品种"。
- **风险**: 将15/20点止损直接用于NQ、外汇或加密货币可能导致过紧或过宽。

---

## 统计

- 原文反例总数：**24 条**（cx-01 至 cx-24）
- 提取器补充：**2 条**（cx-supp-01, cx-supp-02）
- 可编码为检查项：**20/24 条**（cx-16, cx-22 为认知纪律不可直接编码；cx-08 可编码为提醒）
- 覆盖章节：ch01(2), ch03(3), ch04(1), ch09(3), ch10(3), ch11(3), ch12(1), ch13(5), ch29(2), ch32(4)
