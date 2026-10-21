# ICT 2022 Mentorship — 案例提取 (Case Extractor 产出)

> 提取范围：ch02, ch03, ch09, ch10, ch11, ch12, ch13, ch29, ch32
> 提取标准：图文完整、机制归属明确、可作为下游能力卡 A1 使用
> 纪律：不编造结果；原文未给盈亏标"原文未给结果"；引用 ≤150 字；图证据页标【需看图】

---

## cs-01 | Turtle Soup / Stop Run 机构摆动点示意

- **类型**: 合成示意图
- **案例描述**: Ch02 展示 Institutional Swing Points 中的 Stop Run / Turtle Soup 模式。图示为 K 线标注图，展示价格假突破旧高（或旧低）后 V 型反转的过程。文中说明"市场创造一个更高高点，失败（假突破），然后下跌并在高点被拒绝"。品种/时段未指定，为通用教学示意。
- **支撑机制**: Turtle Soup / Stop Run / Institutional Swing Points
- **原文出处**: PDF p.30–33（书 p.30–33）
- **图证据页**: PDF p.30【需看图】(images=2)、PDF p.31【需看图】(images=1)、PDF p.33【需看图】(images=1)
- **成功/失败**: 成功例（模式本身定义为有效反转信号）
- **原文引用**: "What is this pattern? Market makes a higher high, fails (false break above old high/below old low), then break down and has a rejection at the highs."
- **结果**: 原文未给具体盈亏数值

---

## cs-02 | Failure Swing 故障摆动示意

- **类型**: 合成示意图
- **案例描述**: Ch02 展示 Failure Swing 模式：价格突破关键水平但未能持续，回撤后再次尝试测试该水平失败，形成短期结构突破。蓝线标注 PD Array，要求价格 V 型离开后回测失败。品种/时段未指定。
- **支撑机制**: Failure Swing / PD Array 尊重与失效
- **原文出处**: PDF p.36–38（书 p.36–38）
- **图证据页**: PDF p.37【需看图】(images=1)、PDF p.38【需看图】(images=1)
- **成功/失败**: 成功例
- **原文引用**: "The blue line is a PD array. You want to see price move away from it aggressively (V-shape) and try to come down/up again but fail and break a short-term low/high."
- **结果**: 原文未给具体盈亏数值

---

## cs-03 | ERL↔IRL 交替循环（月线→日线多时间框架）

- **类型**: 合成示意图
- **案例描述**: Ch03 用多张折线/K线标注图演示 External Range Liquidity → Internal Range Liquidity 的交替循环。示例从月线 Old Low 被扫（ERL taken）→ 价格回到月线 FVG（IRL）→ 再向外部扩展。随后切换到日线视角重复同一逻辑。品种未指定，为教学演示。
- **支撑机制**: ERL↔IRL 交替循环 / DOL（Draw on Liquidity）
- **原文出处**: PDF p.57–67（书 p.57–67）
- **图证据页**: PDF p.57【需看图】(images=1)、PDF p.58【需看图】(images=2)、PDF p.59【需看图】(images=2)、PDF p.62【需看图】(images=2)、PDF p.63【需看图】(images=2)、PDF p.67【需看图】(images=2)
- **成功/失败**: 成功例（演示价格按预期在 ERL/IRL 间交替运动）
- **原文引用**: "When external range liquidity is taken, a FVG becomes the next draw on liquidity. And when a FVG is stacked, an old low or an old high - External Range Liquidity - becomes the next draw."
- **结果**: 原文未给具体盈亏数值

---

## cs-04 | LTCM 长期资本管理公司失败案例（转述）

- **类型**: 作者转述
- **案例描述**: Ch09 在讨论 Speculative Uninformed Money 时，转述 LTCM（Long-Term Capital Management）案例。LTCM 成立于 1994 年，曾是世界上最成功的对冲基金之一，但 1998 年因一系列交易出错遭受重大损失，最终由主要银行财团纾困。用于说明即使大型基金也可能属于"投机不知情资金"。
- **支撑机制**: Speculative Uninformed Money 分类 / 风险管理重要性
- **原文出处**: PDF p.120（书 p.92）
- **图证据页**: 无图
- **成功/失败**: 失败例（基金崩溃被纾困）
- **原文引用**: "One of the most famous hedge fund failures is Long-Term Capital Management (LTCM). LTCM was founded in 1994...in 1998, the fund suffered significant losses due to a series of trades that went wrong and eventually had to be bailed out by a consortium of major banks."
- **结果**: 重大损失，被银行财团纾困

---

## cs-05 | ES 小时图流动性水平回测（6胜1负回测式图例）

- **类型**: 原书实盘图例
- **案例描述**: Ch12 p.202–203 作者在 ES（E-mini S&P 500）小时图上随机选取超过一个月的交易，绘制蓝线（流动性水平导致市场结构突破 = 成功）和红线（流动性水平重测发生在结构突破失败中 = 失败）。采用 2:1 风险回报比、止损为前一个摆动高低的一半、1:1 移至保本。结果：仅交易蓝色流动性水平，可得 6 胜 1 负。
- **支撑机制**: Trading Off Liquidity Levels / 市场结构突破确认 / 流动性水平回测
- **原文出处**: PDF p.202–203（书 p.174–175）
- **图证据页**: PDF p.202【需看图】(images=3)
- **成功/失败**: 成功例（6 胜 1 负，2:1 R:R）
- **原文引用**: "If you had only traded at the liquidity levels in blue...it would have led to potentially 6 winners for 2:1 risk to reward and 1 loser."
- **结果**: 6 胜 1 负（2:1 R:R），但作者注明需自行回测验证

---

## cs-06 | Daily Bias 用 PDH/PDL 构建反转（Previous Day Low 示例）

- **类型**: 合成示意图
- **案例描述**: Ch12 展示用 Previous Day Low 作为 Draw on Liquidity 并构建反转的教学图。价格在 PDL 处未能位移突破（failure to displace），随后反转上行。图示标注了 PDL 作为流动性池及反转触发点。
- **支撑机制**: Daily Bias / PDH-PDL 作为 DOL / Failure to Displace 反转
- **原文出处**: PDF p.207–208（书 p.125–126）
- **图证据页**: PDF p.207【需看图】(images=1)、PDF p.208【需看图】(images=2)
- **成功/失败**: 成功例
- **原文引用**: "In the example above, Previous Day Low used as a draw on liquidity and being used to frame a reversal."
- **结果**: 原文未给具体盈亏数值

---

## cs-07 | Bearish FVG 三蜡烛形态（书 p.119 = PDF p.147 已核图）

- **类型**: 合成示意图
- **案例描述**: Ch10 核心教学图，展示 Bearish FVG 的三蜡烛序列：蜡烛1低点为 FVG 起点，蜡烛2为缺口形成区，蜡烛3高点为 FVG 终点。右侧折线图标注 Displacement High/Low 与"FVG forms inside this range"橙色区间。已在阶段 0 核查确认。
- **支撑机制**: Fair Value Gap (FVG) 三蜡烛判定 / Displacement
- **原文出处**: PDF p.147（书 p.119）
- **图证据页**: PDF p.147【已核图】(images=1)
- **成功/失败**: 教学示意（非实盘结果）
- **原文引用**: "Candle 1: This candle represents the high of the fair value gap...Candle 2: This candle is where the fair value gap is formed...Candle 3: This candle represents the low of the fair value gap."
- **结果**: 不适用（定义性示意图）

---

## cs-08 | Bullish FVG + NY Session 8:30 AM Stop Run 时序示例

- **类型**: 合成示意图
- **案例描述**: Ch10 p.151–152 展示 Bullish FVG 在 SSL 被扫后形成的三蜡烛序列，并结合纽约时段 8:30 AM 新闻解禁时间窗口。说明 8:30 AM 寻找 stop run，9:30 AM 股市开盘波动激增常造成 Judas Swing。配有 MNO/NYO 溢价折价判断规则。
- **支撑机制**: Bullish FVG / Killzone 时间窗口 / News Embargo / Judas Swing
- **原文出处**: PDF p.151–152（书 p.123–124）
- **图证据页**: PDF p.151【需看图】(images=2)、PDF p.152【需看图】(images=2)
- **成功/失败**: 教学示意
- **原文引用**: "At 8:30 AM we are looking for a stop run to occur...Equity market opens at 9:30 AM. This creates surge in volatility. Many times surge in volatility creates a Judas Swing."
- **结果**: 不适用（流程教学）

---

## cs-09 | Asia Killzone AUDJPY Turtle Soup 模型

- **类型**: 合成示意图
- **案例描述**: Ch11 给出 Asia Killzone 的具体交易模型：看涨时在 EST 8pm–12am 等待 15m swing low 被扫做 Turtle Soup Long；看跌时等 15m swing high 被扫做 Turtle Soup Short。配有亚洲区间高低标注图和趋势线延伸至 11am 的示意图。
- **支撑机制**: Asia Killzone / Turtle Soup / Asian Range
- **原文出处**: PDF p.157–158（书 p.129–130）
- **图证据页**: PDF p.158【需看图】(images=2)、PDF p.159【需看图】(images=2)
- **成功/失败**: 教学示意
- **原文引用**: "If we are bullish, we want to see a 15m swing low get run between 8pm–12am EST for Turtle Soup Long."
- **结果**: 原文未给具体盈亏数值

---

## cs-10 | London Killzone 买方/卖方操作流程

- **类型**: 合成示意图
- **案例描述**: Ch11 London Killzone 部分给出完整的买入/卖出操作模板。买入：伦敦开盘后先突袭亚洲高点止损 → 价格下跌测试关键支撑 & OTE → 从伦敦开盘到收盘建立日线区间。卖出：镜像操作。配有 3 张标注图（PDF p.169）。
- **支撑机制**: London Killzone / Asian Range Stop Raid / OTE 入场
- **原文出处**: PDF p.167–169（书 p.139–141）
- **图证据页**: PDF p.169【需看图】(images=3)
- **成功/失败**: 教学示意
- **原文引用**: "BUY: Raid Stops then shoot for Support. Goal is to dial in on the Low of the day to go long from. First objective after London Open is to raid Asian High stops."
- **结果**: 原文未给具体盈亏数值

---

## cs-11 | New York Session Reversal 条件图例

- **类型**: 合成示意图
- **案例描述**: Ch11 展示 NY Session Reversal 的经典条件：HTF Discount Array 低于市价尚未被满足 → 伦敦时段交易进入该区域 → 穿越至纽约开盘 → 形成反转。配有多张标注图展示 HTF PD Array 与日内时段交互。
- **支撑机制**: NY Session Reversal / HTF PD Array / Killzone 时段切换
- **原文出处**: PDF p.176–178（书 p.148–150）
- **图证据页**: PDF p.178【需看图】(images=3)
- **成功/失败**: 教学示意
- **原文引用**: "If there is a HTF Discount Array that is below the market price but has yet to be met - the day it trades down into it during London's move and crosses over to New York Open - this is classic New York Session Reversal conditions."
- **结果**: 原文未给具体盈亏数值

---

## cs-12 | PO3 日线模板：伦敦开盘经典 Reversal 场景（书 p.142 = PDF p.224 已核图）

- **类型**: 合成示意图
- **案例描述**: Ch13 Power of 3 日线模板图。展示 Accumulation（亚洲盘整）→ Manipulation（伦敦开盘扫止损后扩张，"Until 5am NY"）→ Distribution 的完整日内节奏。SSL/BSL 水平线配 V 型箭头；05:00–08:00 EST 回到 Consolidation。已在阶段 0 核查确认。
- **支撑机制**: Power of 3 (AMD) / Judas Swing / 日内节奏模板
- **原文出处**: PDF p.224（书 p.142）
- **图证据页**: PDF p.224【已核图】(images=2)
- **成功/失败**: 教学示意（节奏模板）
- **原文引用**: "Then the market moves to Reversal. A classic scenario for a London opening. When the market goes down, taking stops and then it expands again - Expansion. Until what time? - Until 5am NY."
- **结果**: 不适用（节奏模板）

---

## cs-13 | 周线 PO3 完整周期示例（SSL + EQL 目标）

- **类型**: 合成示意图
- **案例描述**: Ch13 展示周线级别的 PO3 完整周期：周线图上有 SSL + 前 2 周 Equal Lows 作为目标 → 新一周开盘盘整 → 测试 EQL 并吸收 SSL → 流动性被取走后价格上涨。随后切到 1h 时间框架展示同一过程的细节，包括积累始于上周。
- **支撑机制**: Weekly PO3 / EQL 作为 DOL / 多时间框架对齐
- **原文出处**: PDF p.237–241（书 p.155–159）
- **图证据页**: PDF p.239【需看图】(images=2)、PDF p.240【需看图】(images=4)、PDF p.241【需看图】(images=6)
- **成功/失败**: 成功例（价格按预期从 SSL sweep 后上涨）
- **原文引用**: "After the liquidity pool was taken, the price began to go up. This works on absolutely all TFs."
- **结果**: 原文未给具体盈亏数值

---

## cs-14 | Bullish Breaker Block 完整要素序列（书 p.451 = PDF p.555 已核图）

- **类型**: 合成示意图
- **案例描述**: Ch29 展示 Bullish Breaker 的关键要素序列：Low → High → Lower Low → Higher High。折线图与 K 线图均标橙色 breaker 区域（含 HIGH 蜡烛的范围）。定义 = 旧低被违反前最近 Swing High 中的 up-close 蜡烛，止损被扫且突破该 Swing High 后生效。已在阶段 0 核查确认。
- **支撑机制**: Bullish Breaker Block / Stop Hunt / OB 失效转化
- **原文出处**: PDF p.555（书 p.451）
- **图证据页**: PDF p.555【已核图】(images=2)
- **成功/失败**: 教学示意（定义性图例）
- **原文引用**: "Key Elements – Low – High – Lower Low – Higher High...Bullish Breaker – a bullish range or up-close candle in the most recent Swing High prior to an Old Low being violated."
- **结果**: 不适用（定义性图例）

---

## cs-15 | Bearish Breaker 进阶理论：A-B 腿 1STD 投影

- **类型**: 合成示意图
- **案例描述**: Ch29 展示 Breaker Block Projection 方法：测量 A-B 价格腿（非操纵腿），用 Fibonacci 工具取 1 Standard Deviation 作为目标。示例中 1 STD below 给出 4496.50 的测量移动，标注为"easy bread and butter setup"。同时说明可结合 HTF 流动性使用 2/3/4 STD。
- **支撑机制**: Breaker Block Projection / Fibonacci STD 目标 / A-B 腿测量
- **原文出处**: PDF p.567–569（书 p.463–465）
- **图证据页**: PDF p.567【需看图】(images=2)、PDF p.569【需看图】(images=2)
- **成功/失败**: 教学示意
- **原文引用**: "Breaker Block Projection: We measure A-B leg NOT manipulation leg...We want to use 1 STD as our target...the one standard deviation below gives us a measured move of 4496.50."
- **结果**: 原文未给具体盈亏数值

---

## cs-16 | Order Block Mitigation 机制示意

- **类型**: 合成示意图
- **案例描述**: Ch29 解释 OB 为何有效的机制图：大玩家在 OB 区域双向开仓以填充主仓位量 → 价格交付后主仓位分配完毕 → 市场回测 OB 以让做市商在盈亏平衡价平仓亏损头寸（Mitigation）。图示展示价格从 OB 位移离开后回测的过程。
- **支撑机制**: Order Block / Mitigation / 机构订单流逻辑
- **原文出处**: PDF p.575–577（书 p.471–473）
- **图证据页**: PDF p.575【需看图】(images=1)、PDF p.577【需看图】(images=1)
- **成功/失败**: 教学示意（机制解释）
- **原文引用**: "Mitigation - the process of closing unprofitable positions with smart capital...the market will most likely try to test the order block, since the market maker is interested in closing its unprofitable positions at breakeven."
- **结果**: 不适用（机制解释）

---

## cs-17 | Ch32 买入日交易完整检查清单示例

- **类型**: 合成示意图
- **案例描述**: Ch32 给出买入日交易的完整参数化检查清单：CBDR < 20 点、Asian Range 10-15 点、London Killzone 2-4am EST 寻找 LOD、FVG 低于前一天 NY Session 短期低点、止损 15/20 点、止盈 10-15 点起步。配有 6 张标注图（PDF p.629）展示看涨条件下的设置框架。
- **支撑机制**: High Probability Daytrade Setup / 买入日检查清单 / CBDR + Asian Range 过滤
- **原文出处**: PDF p.628–631（书 p.384–387）
- **图证据页**: PDF p.629【需看图】(images=6)
- **成功/失败**: 教学示意（检查清单模板）
- **原文引用**: "Refer to the CBDR and determine if it is less than 20 points (ES/SP500) ideally. Determine the Asian Range be in a 10-15 points range ahead of Frankfurt Open."
- **结果**: 不适用（参数化模板）

---

## cs-18 | Ch32 Scalp 9 步实例（ES 5m 看涨 Scalp）

- **类型**: 原书实盘图例
- **案例描述**: Ch32 p.655–656 给出高概率 Scalp 的 9 步指南，以 ES 5m 图为载体。步骤：①确认伦敦时段看涨（尝试走低被拒+反弹+日线偏向看涨）→ ②等 7am NY 追踪多头 → ③7-9am 形成设置 → ④等回撤至少 7-10 点 → ⑤若无回撤则不交易 → ⑥在 62% Fib 进场 → ⑦目标当日高点或前日高点。配有 ES 5m 标注图。
- **支撑机制**: High Probability Scalp / OTE (62% Fib) / NY Session Retracement / 无回撤不交易纪律
- **原文出处**: PDF p.655–656（书 p.411–412）
- **图证据页**: PDF p.656【需看图】(images=3)
- **成功/失败**: 成功例（9 步流程演示完整入场）
- **原文引用**: "If no retracement of 7-10 points (ES/SP500) forms by 9AM - don't take anything. If it does form - enter on 62% fib as it drops."
- **结果**: 原文未给具体盈亏数值

---

## cs-19 | Ch32 Scalp 9 步实例（ES 看跌 Scalp 镜像）

- **类型**: 原书实盘图例
- **案例描述**: Ch32 p.657–658 给出看跌 Scalp 的 9 步镜像指南。步骤：①确认伦敦时段看跌（午夜 NY 开盘价上方后被拒走低）→ ②等 7am NY 追踪空头 → ③7-9am 形成设置 → ④等回撤至少 7-10 点上行 → ⑤若无回撤则不交易 → ⑥在 62% Fib 反弹时进场做空 → ⑦目标当日低点或前日低点。
- **支撑机制**: High Probability Scalp / OTE (62% Fib) / NY Session Bearish Retracement
- **原文出处**: PDF p.657–658（书 p.413–414）
- **图证据页**: PDF p.659【需看图】(images=4)
- **成功/失败**: 成功例（9 步流程演示完整做空入场）
- **原文引用**: "Confirm London session was bearish: Want to see price move above opening price at midnight NY time then rejects and goes lower."
- **结果**: 原文未给具体盈亏数值

---

## cs-20 | Monthly Chart IOF：卖方流动性被取后寻求买方

- **类型**: 原书实盘图例
- **案例描述**: Ch09 在 Institutional Order Flow 部分展示一张月度图表，标注卖方流动性被吸收后价格的下一步行动——在顶部寻找流动性。图中可见蜡烛体尊重中间水平，价格可能略高于影线。随后价格到达该流动性区域后将寻求对侧（下方）流动性。
- **支撑机制**: Institutional Order Flow / ERL→IRL 循环 / 月度时间框架
- **原文出处**: PDF p.124–126（书 p.96–98）
- **图证据页**: PDF p.124【需看图】(images=5)、PDF p.125【需看图】(images=4)、PDF p.126【需看图】(images=5)
- **成功/失败**: 成功例（IOF 逻辑演示）
- **原文引用**: "After the market took Sell side liquidity, what will it do next? Look for liquidity at the top."
- **结果**: 原文未给具体盈亏数值

---

## cs-21 | Dealing Range 双侧清扫后底部形成示例

- **类型**: 合成示意图
- **案例描述**: Ch09 展示 Dealing Range 概念：买卖双方流动性均被清扫后，开始寻找底部形成。一旦看到明显反转，保持看涨偏向直到交易区间均衡点。图示展示多种形式的 dealing range 及其内部嵌套结构。
- **支撑机制**: Dealing Range / Premium-Discount-Equilibrium / 双侧流动性清扫
- **原文出处**: PDF p.128–131（书 p.100–103）
- **图证据页**: PDF p.130【需看图】(images=4)、PDF p.131【需看图】(images=1)
- **成功/失败**: 教学示意
- **原文引用**: "Generally, after we have swept liquidity on both sides, you start looking for a bottom to form, and once you see a clear reversal, you can start maintaining a bullish bias up until the equilibrium of the dealing range."
- **结果**: 原文未给具体盈亏数值

---

## cs-22 | SMT Divergence EURUSD/GBPUSD 确认示例

- **类型**: 合成示意图
- **案例描述**: Ch12 展示 SMT Divergence 作为确认工具的用法：GBPUSD 创新高而 EURUSD 未能同步（显示弱势），暗示做空 EURUSD 的机会。强调 SMT 不单独入场，只在预定水平附近、已有交易想法时使用。配有多张对比图。
- **支撑机制**: SMT Divergence / Intermarket Analysis / 确认工具
- **原文出处**: PDF p.187–190（书 p.159–162）
- **图证据页**: PDF p.187【需看图】(images=3)、PDF p.189【需看图】(images=1)、PDF p.190【需看图】(images=1)
- **成功/失败**: 教学示意
- **原文引用**: "You are not looking for SMT divergence to take a trade, you use it only around predetermined levels with trade idea in mind."
- **结果**: 原文未给具体盈亏数值

---

## 统计摘要

| 维度 | 数量 |
|------|------|
| 总案例数 | 22 |
| 原书实盘图例 | 4 (cs-05, cs-18, cs-19, cs-20) |
| 作者转述 | 1 (cs-04) |
| 合成示意图 | 17 |
| 成功例 | 12 |
| 失败例 | 1 (cs-04 LTCM) |
| 教学示意/不适用 | 9 |
| 覆盖章节 | ch02(2), ch03(1), ch09(3), ch10(2), ch11(3), ch12(3), ch13(2), ch29(3), ch32(3) |

### 每例一行摘要

| ID | 机制归属 | PDF 页 |
|----|----------|--------|
| cs-01 | Turtle Soup / Stop Run | p.30–33 |
| cs-02 | Failure Swing / PD Array | p.36–38 |
| cs-03 | ERL↔IRL 交替循环 | p.57–67 |
| cs-04 | Speculative Uninformed Money | p.120 |
| cs-05 | Trading Off Liquidity Levels (6W1L) | p.202 |
| cs-06 | Daily Bias / PDH-PDL 反转 | p.207–208 |
| cs-07 | Bearish FVG 三蜡烛 | p.147 |
| cs-08 | Bullish FVG + NY 8:30 Stop Run | p.151–152 |
| cs-09 | Asia Killzone Turtle Soup | p.157–158 |
| cs-10 | London Killzone 买卖流程 | p.167–169 |
| cs-11 | NY Session Reversal | p.176–178 |
| cs-12 | PO3 日线 AMD 模板 | p.224 |
| cs-13 | Weekly PO3 + EQL 目标 | p.237–241 |
| cs-14 | Bullish Breaker 要素序列 | p.555 |
| cs-15 | Breaker A-B 腿 1STD 投影 | p.567–569 |
| cs-16 | OB Mitigation 机制 | p.575–577 |
| cs-17 | 买入日交易检查清单 | p.628–631 |
| cs-18 | Scalp 9 步（ES 5m 看涨） | p.655–656 |
| cs-19 | Scalp 9 步（ES 看跌镜像） | p.657–659 |
| cs-20 | Monthly IOF ERL→IRL | p.124–126 |
| cs-21 | Dealing Range 双侧清扫 | p.128–131 |
| cs-22 | SMT Divergence 确认 | p.187–190 |
