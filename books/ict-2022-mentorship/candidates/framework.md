# Framework Candidates — ICT 2022 Mentorship

> 阶段 1 产出：从 ch01/ch02/ch03/ch04/ch06/ch09/ch10/ch11/ch12/ch13/ch29/ch32 全量扫描提取的决策框架 / 思维模型 / 流程 / 状态机候选单元。

---

## fw-01 ERL↔IRL 交替状态机

- **id**: fw-01
- **title**: ERL↔IRL 交替状态机（External/Internal Range Liquidity Alternation）
- **type**: procedure / state-machine
- **source_chapter**: Ch3 (PDF p.56–74), Ch9 (PDF p.127–128), Ch12 (PDF p.200)
- **source_quote**: |
    "Price only does two things: it goes to old highs and old lows or seeks to reprice into imbalances. When external range liquidity is taken, a FVG becomes the next draw on liquidity. And when a FVG is stacked, an old low or an old high — External Range Liquidity — becomes the next draw."
- **summary**: |
    价格仅在两种状态间交替：(1) 寻求外部范围流动性（ERL = 旧高/旧低上方的止损簇）；(2) 寻求内部范围流动性（IRL = FVG/OB/MB 等 PD Array）。
    
    **状态转换规则**：
    - ERL 被扫 → 下一个 DOL 变为 IRL（FVG/OB）
    - IRL 被标记/tagged → 下一个 DOL 变为 ERL
    - 在月/周/日/4H 上均适用此循环
    
    **方向判定补充**：
    - 需结合 HTF Order Flow 判断上下方向
    - Displacement 从 FVG 向上 → 目标为外部 BSL
    - Displacement 从 FVG 向下/不尊重 FVG → 目标为外部 SSL
    - K线强弱（engulfing vs weakness）辅助确认
    
    **输入**: HTF 结构、已标注的 ERL/IRL 位置、Displacement 观察
    **输出**: 下一个 DOL 方向与类型
    **缺失条件**: LRLR/HRLR 无量化度量标准
- **tags**: [liquidity, state-machine, DOL, core-model]
- **chart_dependency**: 【需看图 PDF p.57–59, p.62–63, p.67–74】ERL/IRL 交替示意图与多时间框架示例
- **relations**: fw-02 (Daily Bias 使用 ERL/IRL 循环作为上游输入), fw-04 (FVG 是 IRL 的主要形式), fw-06 (DOL 识别)

---

## fw-02 Daily Bias 判定流程

- **id**: fw-02
- **title**: Daily Bias 判定流程
- **type**: decision-framework / checklist
- **source_chapter**: Ch12 (PDF p.183–210), Ch32 (PDF p.628–631, p.646–658)
- **source_quote**: |
    "Are we at Premium zone? When we are at premium zone or the algorithm takes buy side liquidity, we anticipate price will go down. Are we at Discount zone? Similarly when we at discount zone or the algorithm takes sell side liquidity, we anticipate higher prices."
- **summary**: |
    确定当日方向偏向的多步检查清单：
    
    1. **HTF 溢价/折价位置**：当前价格在 HTF dealing range 的溢价区→预期下跌；折价区→预期上涨；均衡区→最难预测
    2. **DOL 识别**：价格将向折价 FVG/旧低 或 溢价 FVG/旧高 运动；直到达到 DOL 前坚持该想法，禁止反复翻转
    3. **PDH/PDL 作为流动性池**：前一天高/低点可作为反转的流动性池；价格触及但未能突破+无位移=潜在反转
    4. **SMT 背离确认**（仅辅助）：在预定水平附近、已有交易想法时使用
    5. **日线摆动结构**：看涨时等待日线 swing high 被打破→寻找 swing low 形成但不破近期 swing low→第3根蜡烛高点预计被突袭
    6. **季节性/季度倾向**（非必须）
    
    **输入**: HTF 图表、PDH/PDL、DOL、SMT
    **输出**: 当日看涨/看跌/观望结论
    **缺失条件**: "反复翻转"的禁止缺少客观判据
- **tags**: [bias, daily-routine, checklist, HTF]
- **chart_dependency**: 【需看图 PDF p.183–184, p.204–210】溢价/折价区域图、PDH/PDL 反转示例
- **relations**: fw-01 (ERL/IRL 循环是偏向的上游逻辑), fw-05 (SMT 确认工具), fw-11 (Ch32 入场检查清单使用 bias 作为前提)

---

## fw-03 MSS 判定流程（含 Displacement 要求）

- **id**: fw-03
- **title**: MSS（Market Structure Shift）判定流程
- **type**: procedure / decision-framework
- **source_chapter**: Ch4 (PDF p.80–83), Ch10 (PDF p.143–144)
- **source_quote**: |
    "MSS must be energetic and leave behind displacement to ensure that market is looking to reverse. Remember that structure means nothing without narrative. Lose sight of the draw on price, HTF structure, and resting liquidity and you are vulnerable to being faked out."
- **summary**: |
    市场结构转变的有效判定流程：
    
    **看涨 MSS 条件**：
    1. 价格跌破旧低/多个旧低
    2. 迅速（quick）向上位移
    3. 位移必须是有力K线收盘运动（不是小蜡烛或仅影线）
    4. 蜡烛收盘后确认
    
    **看跌 MSS 条件**：
    1. 价格突破旧高/多个旧高
    2. 迅速向下位移
    3. 同上力度要求
    
    **无效 MSS**：无位移的结构突破不算数；无位移本身可作为反向信号（lack of displacement = 潜在同向入场）
    
    **POI 发生位置**：支撑/阻力位、时段高低点（Asian/London/NY Killzone）
    
    **输入**: K线序列、前短期高低点、Displacement 观察
    **输出**: 布尔判定（有效 MSS / 无效 / Lack of Displacement）
    **缺失条件**: Displacement 的"明显性"无量化阈值，靠视觉主观判断
- **tags**: [structure, MSS, displacement, confirmation]
- **chart_dependency**: 【需看图 PDF p.81–83】MSS 示意图与 Displacement 标注
- **relations**: fw-04 (FVG 常伴随 Displacement 出现), fw-08 (PO3 阶段切换需 MSS 确认), fw-11 (Ch32 入场前提)

---

## fw-04 FVG 三蜡烛判定机制

- **id**: fw-04
- **title**: FVG（Fair Value Gap）三蜡烛判定机制
- **type**: procedure / pattern-recognition
- **source_chapter**: Ch10 (PDF p.139–154)
- **source_quote**: |
    "Fair Value Gaps are created within a three-candle sequence and are commonly visualized on the chart as a large candle whose neighboring candles' upper and lower wicks do not fully overlap the large candle."
- **summary**: |
    FVG 三蜡烛序列判定规则：
    
    **Bearish FVG**：
    - Candle 1 的低点 = FVG 起点（上界）
    - Candle 2 = 形成 FVG 的大蜡烛（脉冲）
    - Candle 3 的高点 = FVG 终点（下界）
    - 最佳形态出现在 BSL 被扫之后、相对等高（双顶）上方
    - 若 Candle 1 高点已被 Candle 3 低点抵消 → 平衡，非 FVG
    
    **Bullish FVG**：
    - Candle 1 的高点 = FVG 起点（下界）
    - Candle 2 = 大蜡烛
    - Candle 3 的低点 = FVG 终点（上界）
    - 最佳形态出现在 SSL 被扫之后、相对等低（双底）下方
    
    **用途**：入场点、目标位、情绪转换衡量工具
    **Displacement 关联**：FVG 由 Displacement 产生；Displacement = 有力突破前高/前低的K线运动，留下 FVG
    
    **输入**: 三根连续K线的 OHLC
    **输出**: FVG 存在/不存在 + 区间范围
    **缺失条件**: FVG 最小宽度未定义
- **tags**: [FVG, pattern, three-candle, imbalance, entry]
- **chart_dependency**: 【需看图 PDF p.140–141, p.147, p.149–151】三蜡烛 FVG 标注图、Bearish/Bullish FVG 完整示例
- **relations**: fw-01 (FVG 是 IRL 的主要形式), fw-03 (Displacement 产生 FVG), fw-09 (OTE 入场常在 FVG 区域)

---

## fw-05 SMT 背离确认流程

- **id**: fw-05
- **title**: SMT Divergence 确认流程
- **type**: decision-framework / confirmation-tool
- **source_chapter**: Ch12 (PDF p.186–192)
- **source_quote**: |
    "You are not looking for SMT divergence to take a trade, you use it only around predetermined levels with trade idea in mind. Then once pattern unfolds that is the green light to get into the trade."
- **summary**: |
    SMT（Smart Money Technique）背离作为确认工具的流程：
    
    **定义**：两个密切相关品种（EURUSD/GBPUSD、ES/NQ、BTC/ETH、DXY/ES）之间创新高/新低不同步的裂缝
    
    **使用规则**：
    1. 不作为独立入场信号
    2. 仅在预定水平附近、已有交易想法时使用
    3. 溢价区：某品种未能创新高 = 看跌背离
    4. 折价区：某品种未能创出新低 = 看涨背离
    5. 模式展开后 = 绿灯入场
    
    **配对选择**：EUR/USD & GBP/USD（外汇）、ES & NQ（股指）、BTC & ETH（加密）
    
    **输入**: 两个相关品种的 K 线对比
    **输出**: 确认/不确认现有交易想法
    **缺失条件**: SMT 比对的时间框架未规定
- **tags**: [SMT, confirmation, correlation, divergence]
- **chart_dependency**: 【需看图 PDF p.187–191】SMT 背离示意图
- **relations**: fw-02 (Daily Bias 的辅助确认), fw-11 (Ch32 盘前过滤清单的一项)

---

## fw-06 DOL（Draw on Liquidity）识别流程

- **id**: fw-06
- **title**: DOL（Draw on Liquidity）识别流程
- **type**: procedure / decision-framework
- **source_chapter**: Ch3 (PDF p.54–56, p.60–74), Ch12 (PDF p.184–185)
- **source_quote**: |
    "First thing, price is always either rebalancing or taking liquidity. Next, price is going from P/D array to P/D array. Hence, you must annotate your P/D zones to know if price rebalanced or will rebalance."
- **summary**: |
    识别下一个流动性磁吸目标（DOL）的流程：
    
    **核心原则**：价格永远在做两件事之一——重新平衡不平衡 或 寻求流动性
    
    **DOL 候选类型**：
    - PWH/PWL（前周高/低）
    - PDH/PDL（前日高/低）
    - Session High/Low（亚洲/伦敦/纽约时段高低）
    - EQH/EQL（等高/等低）配合 LRLR 条件
    - FVG / OB / MB 等 PD Array
    
    **识别步骤**：
    1. 标注所有 P/D zones 和流动性位置
    2. 跟踪 Displacement 后的反应
    3. 在 P/D array 上的反应确定下一个 DOL
    4. 结合 HTF Order Flow 判断方向
    
    **LRLR vs HRLR 分类**：
    - LRLR（Low Resistance Liquidity Run）：最理想交易条件，"刀子切黄油"
    - HRLR（High Resistance Liquidity Run）：价格需最大努力，交易时间更长
    
    **输入**: 已标注的图表、HTF 偏向
    **输出**: 下一个 DOL 位置与类型
    **缺失条件**: LRLR/HRLR 无量化度量
- **tags**: [DOL, liquidity, magnet, procedure]
- **chart_dependency**: 【需看图 PDF p.54–56, p.60–74】DOL 识别与 ERL/IRL 交替图
- **relations**: fw-01 (ERL/IRL 交替是 DOL 的状态机基础), fw-02 (Daily Bias 依赖 DOL)

---

## fw-07 Killzone 时段流程与禁忌日过滤

- **id**: fw-07
- **title**: Killzone 时段流程与禁忌日过滤
- **type**: procedure / time-filter
- **source_chapter**: Ch11 (PDF p.155–180), Ch4 (PDF p.82–83)
- **source_quote**: |
    "Algorithmic theory is based on time and price, price levels are useless until Time is considered, Time is of no use unless Price is at a key PD array. Blending the two yield astonishing results and precision."
- **summary**: |
    五个 Killzone 时段及其行为模板：
    
    1. **Asia Killzone** (20:00–00:00 NY): 通常盘整；决定 London/NY 方向偏差；AUD/NZD/JPY 活跃；范围高度 = 20:00–午夜最高最低差
    2. **London Open Killzone** (02:00–05:00 NY): 通常创造日低（看涨日）或日高（看跌日）；首个目标突袭 Asian 高/低止损
    3. **NY Open Killzone** (07:00–10:00 NY): 最容易交易（London 高/低已就位）；多数时候延续 London 方向；可能反转
    4. **London Close Killzone** (10:00–12:00 NY): 修正运动；大范围日（>5ADR）回撤约 20%；可用于日内反转 scalp
    5. **CBDR** (14:00–20:00 NY): Central Bank Dealers Range
    
    **亚洲区间阈值过滤**：若 Asian range > 15–20 points (ES/SP500)，等待 NY 交易更安全
    
    **禁忌日/回避条件**：利率公告、关键演讲、假日交易、全球经济事件、周范围目标已达成
    
    **输入**: 当前时间、经济日历、Asian range 点数
    **输出**: 可交易/回避 + 当前时段行为预期
    **缺失条件**: 夏令时(EDT)处理未说明
- **tags**: [killzone, time, session, filter, procedure]
- **chart_dependency**: 【需看图 PDF p.156–157, p.159–166, p.175–178】Killzone 时段图与 Asian range 标注
- **relations**: fw-08 (PO3 各阶段对应特定时段), fw-11 (Ch32 入场时间窗口)

---

## fw-08 PO3/AMD 状态机（Accumulation→Manipulation→Distribution）

- **id**: fw-08
- **title**: PO3/AMD 三阶段状态机（Power of 3 / Accumulation-Manipulation-Distribution）
- **type**: state-machine / procedure
- **source_chapter**: Ch13 (PDF p.215–265), Ch9 (PDF p.128)
- **source_quote**: |
    "Consolidation cannot be followed by Retracement or Reversal. Consolidation is always followed by Expansion. After Expansion comes either Retracement or Reversal. The market does NOT do Consolidation -> Expansion -> Consolidation."
- **summary**: |
    日内/周度节奏恒为三阶段循环：
    
    **阶段定义**：
    1. **Accumulation（积累）**：盘整、低波动、聪明钱建仓；对应 Asian session
    2. **Manipulation（操纵）**：假突破/Judas Swing，扫止损，诱导散户反向；通过新闻事件驱动
    3. **Distribution（分配）**：真实扩张运动，聪明钱出货给散户
    
    **状态转换铁律**：
    - Consolidation → Expansion（永远，不会直接到 Retracement/Reversal）
    - Expansion → Retracement 或 Reversal
    - 不做 Consolidation → Expansion → Consolidation
    
    **日线 PO3 模板**：
    - Asian = Consolidation/Accumulation
    - 午夜后下跌/上涨 = Manipulation/Judas Swing
    - London 反转 = Expansion（直到 5am NY）
    - 5:00–8:00 AM = 小 Consolidation
    - 8:00–8:30 AM = Retracement
    - NY session = Expansion 或 Reversal
    - London Close = Reversal
    - ~16:00 EST = Consolidation 收盘
    
    **周线 PO3 模板**：
    - 周日开盘 = Consolidation
    - 周一 = Expansion
    - 周一/周二 = Reversal（周高/低通常此时形成）
    - 其他 Expansion
    - 周中 = Consolidation
    - 再 Reversal 或 Retracement
    
    **确认 Manipulation**：需看到 MSS + 价格回到午夜开盘价之上/之下
    
    **输入**: 当前时段、午夜开盘价、MSS 观察
    **输出**: 当前阶段状态 + 预期下一步动作
    **缺失条件**: 阶段切换的实时判定缺客观信号
- **tags**: [PO3, AMD, state-machine, rhythm, Judas-swing]
- **chart_dependency**: 【需看图 PDF p.224, p.226–228, p.230–232, p.237–241】PO3 日线/周线模板图
- **relations**: fw-07 (Killzone 时段对应 PO3 各阶段), fw-03 (MSS 确认 Manipulation 结束), fw-11 (Ch32 入场时机)

---

## fw-09 OTE（Optimal Trade Entry）入场计算

- **id**: fw-09
- **title**: OTE（Optimal Trade Entry）入场计算机制
- **type**: procedure / calculation
- **source_chapter**: Ch9 (PDF p.131–132), Ch32 (PDF p.655)
- **source_quote**: |
    "How to identify discount? First, look for a bullish displacement in price. Once that occur in price, you want to see price forming a swing high. Now you can draw your Fibonacci tool from swing high to swing low. Wait for price return back to discount and look for longs there."
- **summary**: |
    OTE 入场区的计算流程：
    
    **看涨 OTE**：
    1. 确认看涨 Displacement
    2. 识别 swing high 形成
    3. Fib 从 swing high 拉到 swing low
    4. 等待价格回撤至折价区（0.62–0.79）
    5. 0.705 为甜蜜点
    6. 在折价区寻找多头入场（FVG/OB/Breaker）
    
    **看跌 OTE**：
    1. 确认看跌 Displacement
    2. 识别 swing low 形成
    3. Fib 从 swing low 拉到 swing high
    4. 等待价格回升至溢价区（0.62–0.79）
    5. 在溢价区寻找空头入场
    
    **NY Scalp 中的 OTE**：步骤 8 明确 "enter on 62% fib as it drops/rallies"
    
    **输入**: Displacement 后的 swing high/low
    **输出**: 入场区间价位
    **缺失条件**: "80% 情况有效"无数据来源
- **tags**: [OTE, fibonacci, entry, discount, premium]
- **chart_dependency**: 【需看图 PDF p.131–132】OTE Fib 标注图
- **relations**: fw-04 (FVG 常在 OTE 区域), fw-10 (ICT 2022 Model 六步的第4步), fw-11 (Ch32 入场参数)

---

## fw-10 ICT 2022 Model 六步执行流程

- **id**: fw-10
- **title**: ICT 2022 Model 六步执行流程
- **type**: procedure / execution-model
- **source_chapter**: Ch9 (PDF p.116–118), Ch32 (PDF p.628–631)（综合多处）
- **source_quote**: |
    "Buy Side Oriented Market: 1. We will wait for a big bearish displacement after a news embargo. 2. Don't trade the first 10 minutes of the news. 3. We will wait & observe order flow: a. Wait for Bearish PD arrays to fail. b. Want to see Bullish displacement. c. Want to see a change in order flow."
- **summary**: |
    ICT 2022 模型的完整执行流程（以买入为例，卖出镜像）：
    
    1. **扫流动性**：等待价格扫过旧低/SSL（通常在新闻解禁后 8:30 AM）
    2. **Displacement + FVG**：扫完后出现看涨 Displacement，留下 FVG
    3. **MSS 确认**：短期结构转变（伴随 Displacement）
    4. **50% Fib / OTE**：回撤至 0.62–0.79 Fib 区（0.705 甜蜜点）
    5. **FVG 位置**：在 FVG 处或 OB/Breaker 处设限价单
    6. **限价入场**：在折价 PD Array 挂买入限价单；止损 5 点 (ES)；目标 10 点
    
    **新闻日特殊规则**：
    - 新闻后等 10 分钟再找设置
    - 新闻 embargo 可充当 Judas Swing
    - 适用新闻：NFP, CPI, FOMC, PPI, FED talks
    
    **卖方镜像**：等待看涨 Displacement → 看跌 PD arrays 失效 → 看跌 Displacement → 溢价区卖出
    
    **输入**: 新闻日历、K线序列、PD Array 标注
    **输出**: 入场/止损/止盈参数
    **缺失条件**: "clear unobstructed path" 无判定法
- **tags**: [2022-model, execution, six-step, news-trading]
- **chart_dependency**: 【需看图 PDF p.116–118】Buy/Sell Side Oriented Market 流程图
- **relations**: fw-03 (MSS 是第3步), fw-04 (FVG 是第2/5步), fw-09 (OTE 是第4步), fw-11 (Ch32 细化参数)

---

## fw-11 Ch32 高概率入场检查清单 + 止损止盈流程

- **id**: fw-11
- **title**: Ch32 高概率日内交易入场检查清单 + 止损止盈参数化流程
- **type**: procedure / checklist / risk-management
- **source_chapter**: Ch32 (PDF p.627–658)
- **source_quote**: |
    "When Daily and/or 4h direction is Bullish: 1. Use Previous Day's Low to High for Retracement Entries. 2. Use Previous Day's NY Session Low to High for Retracement Entries. 3. Use Previous Day's Low for Sell Stop Raid to accumulation longs. 4. Focusing on the anticipated move from HTF Discount to Premium PD Arrays."
- **summary**: |
    **买入日检查清单**（HTF 看涨时）：
    - 使用 PD Low→High 做回撤入场
    - 使用前一天 NY Session Low→High 做回撤入场
    - 使用前一天 Low 做 Sell Stop Raid 累积多头
    - 关注 HTF Discount→Premium PD Arrays 的预期运动
    - CBDR < 20 points (ES/SP500)
    - Asian Range 10–15 points
    - 理想买入日：周一/二/三
    - 执行时间框架：5m 或 15m
    
    **买入位置清单**：
    - Asian Range 下方 +2–5 points
    - 前一天 NY Session 短期低点下方的 FVG
    - 短期低点下方的看涨 OB
    - London Killzone 内 1 STD + Discount PD Array
    - Turtle Soup（短期低点被扫两次无买方被扫）
    
    **止损参数表 (ES/SP500)**：
    - CBDR + PDA 重叠：15 点
    - Asian Range 下方运行：20 点
    - 任何 Sell Stop Raid：15 点
    - 第1次回撤至 +OB：5 点（LOD 下方）
    - 第2次 Sell Stop 回报：15 点（LOD 下方）
    - 其他设置：50% ADR(5日) 减去 Asian Range Low
    
    **止盈参数表 (ES/SP500)**：
    - 始终在 10–15 点先取部分利润
    - 每 2 STD of Asian Range/CBDR 分批减仓
    - PDH +2–7 点取部分
    - 1h 价格范围的 50% 取部分
    - 5 日 ADR 投影处取 60–80%
    - 时间止盈：5:00 AM / 7:00 AM 前短期高点 / 10:00–11:00 AM
    
    **卖出日**：完全镜像（Premium→Discount, Buy Stop Raid, HOD 上方止损等）
    
    **输入**: HTF 方向、PDH/PDL、Asian Range、CBDR、ADR
    **输出**: 入场/止损/止盈完整参数
    **缺失条件**: 仅 ES 标定，跨品种缺换算
- **tags**: [checklist, entry, stop-loss, take-profit, risk-management, Ch32]
- **chart_dependency**: 【需看图 PDF p.629, p.632, p.634–636, p.639, p.641】入场位置图与止损止盈标注
- **relations**: fw-02 (Daily Bias 是前提), fw-07 (Killzone 时间窗口), fw-09 (OTE 入场), fw-12 (NY Scalp 9步是本清单的子集)

---

## fw-12 NY Scalp 9 步流程

- **id**: fw-12
- **title**: NY Scalp 高概率剥头皮 9 步流程
- **type**: procedure / execution-model
- **source_chapter**: Ch32 (PDF p.655–658)
- **source_quote**: |
    "1. Confirm London session was bullish. 2. Wait for 7am NY time to stalk for longs. 3. Between 7am–9am NY time, setup will typically form. 4. After 7am NY time, wait for price retracement lower. ... 7. If no retracement of 7-10 points forms by 9AM - don't take anything. 8. If it does form - enter on 62% fib as it drops. 9. Expect price to retest high of day or previous day's high."
- **summary**: |
    NY Scalp 看涨 9 步（看跌镜像）：
    
    1. 确认 London session 看涨（尝试走低被拒绝 + 反弹 + Daily bias 看涨）
    2. 等待 7:00 AM NY 开始追踪多头
    3. 7:00–9:00 AM NY 之间设置通常形成
    4. 7:00 AM 后等待价格回撤走低
    5. NY 时段通常从 London 形成的日内 swing high 回撤
    6. 理想选择至少 7–10 点 (ES/SP500) 的回撤
    7. **若 9:00 AM 前无 7–10 点回撤 → 不交易**
    8. 若形成 → 在 62% Fib 下降时入场
    9. 预期价格重测日高或前一天高点 → 在 Fib 上寻找目标 1 & 2
    
    **看跌镜像**：确认 London 看跌 → 等待 7am → 回撤 7–10 点向上 → 62% Fib 入场做空 → 目标日低/PDL
    
    **输入**: London session 方向、NY 时段回撤幅度、Fib
    **输出**: 入场/目标/放弃决策
    **缺失条件**: 原文未给出 Fib 目标 1 & 2 的具体数值
- **tags**: [scalp, NY-session, 9-step, execution, intraday]
- **chart_dependency**: 【需看图 PDF p.656–659】NY Scalp 5m 图示例
- **relations**: fw-11 (Ch32 总清单的一部分), fw-09 (OTE/Fib 入场), fw-07 (NY Killzone 时间窗口)

---

## fw-13 15m→5m 日内工作流

- **id**: fw-13
- **title**: 15m→5m 日内分析-执行工作流
- **type**: procedure / workflow
- **source_chapter**: Ch6 (PDF p.88–94)
- **source_quote**: |
    "Once we have analyzed the 15-minute chart and identified relevant market conditions, we switch to the 5-minute chart for precise entry points. This allows us to make well-timed trades based on the information gathered."
- **summary**: |
    日内交易的标准时间框架降级工作流：
    
    **盘前（8:30 AM 前）**：
    1. 在 15m 图上识别关键高/低点、不平衡、FVG、OB
    2. 特别关注 London/NY Killzone 的预期流动性猎取
    3. 寻找潜在的 stop hunt 区域
    
    **执行（8:30 AM – 12:00 PM）**：
    4. 切换到 5m 图寻找精确入场点
    5. 目标在 11:00 AM 前建仓
    6. 若关键流动性未达到，可在 NY Lunch/Afternoon Session 继续持有
    
    **多时间框架层级**（Ch9 p.121）：
    - Long-term: Weekly/Daily
    - Intermediate-term: 4H/1H
    - Short-term: 15m/5m
    
    **输入**: 15m 分析结果
    **输出**: 5m 精确入场点
    **缺失条件**: 无
- **tags**: [workflow, timeframe, 15m-5m, intraday-routine]
- **chart_dependency**: 无特定图表依赖
- **relations**: fw-07 (Killzone 时段), fw-11 (Ch32 执行时间框架), fw-14 (Top Down 分析)

---

## fw-14 Top Down 多时间框架分析流程

- **id**: fw-14
- **title**: Top Down 多时间框架分析流程
- **type**: procedure / analysis-framework
- **source_chapter**: Ch2 (PDF p.22–27), Ch9 (PDF p.121), Ch32 (PDF p.627, p.642–643)
- **source_quote**: |
    "Large institutions and banks analyze charts on Day => Week => Month TFs. We determine price levels that correspond to the Institutional Order Flow. This is key. HTFs form slowly and allow enough time for planning."
- **summary**: |
    自上而下的分析层级：
    
    1. **月/周线**：建立 HTF 偏向、识别主要流动性池与 PD Array
    2. **日线**：确定 Daily Bias、定位 PDH/PDL/NMO/NYO、识别 dealing range
    3. **4H/1H**：中间层结构、dealing range 内的溢价/折价划分
    4. **15m**：识别关键高/低点、FVG、OB、Killzone 内的流动性猎取
    5. **5m**：精确入场执行
    
    **关键原则**：
    - HTF 方向最重要（Daily/4H）
    - LTF 设置必须在 HTF 前提下进行
    - Daily FVG → 1h structure → 15m entries（不要过度降低时间框架）
    - LTH/LTL 通常链接到日线图
    
    **输入**: 多时间框架图表
    **输出**: 从 HTF 偏向到 LTF 入场的完整分析链
    **缺失条件**: 无
- **tags**: [top-down, multi-timeframe, analysis, hierarchy]
- **chart_dependency**: 无特定单一图表
- **relations**: fw-13 (15m→5m 是执行层), fw-02 (Daily Bias 是中间层), fw-01 (ERL/IRL 跨时间框架)

---

## fw-15 流动性池挂单入场流程（Turtle Soup / Stop Run）

- **id**: fw-15
- **title**: 流动性池挂单入场流程（Turtle Soup / Stop Run / False Breakout）
- **type**: procedure / entry-model
- **source_chapter**: Ch2 (PDF p.28–37), Ch12 (PDF p.197–198), Ch32 (PDF p.631)
- **source_quote**: |
    "Stop run or turtle soup - highest, most probable trading condition, you want to be looking for this one. The market trades to a key level or just short of it - but fails to immediately react - indicating another run deeper before a reversal. After the reversal - the opportunity is best taken when the short-term Market Structure breaking point is retested."
- **summary**: |
    Turtle Soup / Stop Run 入场流程：
    
    **模式识别**：
    1. 市场交易到关键水平或略低于该水平
    2. 未能立即反应 → 暗示还有一次更深的运行
    3. 反转后 → 短期 MSS 断点重测时入场
    
    **看涨 Turtle Soup**：
    - 短期低点被扫两次，无买方被扫 → 买入
    - 在低点下方或等于低点处挂 Buy Limit
    - 像银行间交易者一样买入 sell stops
    
    **看跌 Turtle Soup**：
    - 短期高点被扫两次，无卖方被扫 → 卖出
    - 在高点上方或等于高点处挂 Sell Limit
    - 像银行间交易者一样卖出 buy stops
    
    **假突破三重确认**（Ch12 p.197–198）：
    1. FVG 存在
    2. 市场结构转变
    3. 流动性池确认
    
    **V-shape 要求**：红三角（扫止损点）应成为影线，不希望价格徘徊，要立即 V 型反应远离
    
    **输入**: 关键高/低点、止损扫荡观察、MSS
    **输出**: 限价入场 + 止损位
    **缺失条件**: 无
- **tags**: [turtle-soup, stop-run, false-breakout, entry, liquidity-pool]
- **chart_dependency**: 【需看图 PDF p.30–31, p.33, p.35–37】Turtle Soup / Failure Swing 示意图
- **relations**: fw-03 (MSS 确认), fw-06 (DOL 识别), fw-11 (Ch32 止损参数)

---

## fw-16 Failure Swing 排障/备选入场流程

- **id**: fw-16
- **title**: Failure Swing 排障/备选入场流程
- **type**: troubleshooting / alternative-entry
- **source_chapter**: Ch2 (PDF p.36–37), Ch3 (PDF p.77), Ch29 (PDF p.592–596)
- **source_quote**: |
    "Failure Swings: The market trades through a key level initially but fails to immediately continue – after rejecting the new price level – the market retraces only to attempt to stage another drive to retest the new price level."
- **summary**: |
    当 Turtle Soup / Stop Run 未出现时的备选方案：
    
    **Failure Swing 定义**：
    - 市场初始穿过关键水平但无法立即继续
    - 拒绝新价格水平后回撤
    - 再次尝试测试/超越新价格水平但失败
    - 突破短期低/高点
    
    **与 Breaker 的关系**：
    - Breaker 来自成功的 swing（stop run）
    - Mitigation Block 来自失败的 swing（failure swing）
    - 若 stop run/turtle soup 未发生 → 仍有 failure swing 交易机会
    
    **看涨 Failure Swing**：低点未能突破前低 → 在看涨区域期望此形态
    **看跌 Failure Swing**：高点未能突破前高 → 在看跌区域期望此形态
    
    **入场**：反转后在初始关键水平重测或 MSS 断点重测时入场
    
    **输入**: 关键水平穿越观察、重试失败确认
    **输出**: 备选入场点
    **缺失条件**: 无
- **tags**: [failure-swing, troubleshooting, alternative, mitigation-block]
- **chart_dependency**: 【需看图 PDF p.36–37】Failure Swing 示意图
- **relations**: fw-15 (Turtle Soup 的首选替代), fw-17 (Breaker Block 的成功 swing 对应)

---

## fw-17 PD Array/Block 类型识别词典

- **id**: fw-17
- **title**: PD Array/Block 类型识别词典（OB/Breaker/MB/RB/PB/VB）
- **type**: decision-framework / classification
- **source_chapter**: Ch29 (PDF p.547–616), Ch9 (PDF p.131–134)
- **source_quote**: |
    "The LAST BULLISH or BEARISH candle before an IMPULSE up or down, represent Order Block. Breaker is an OB that fails to hold and the price finally breaks through it."
- **summary**: |
    PD Array 家族各类型的识别规则与有效性条件：
    
    **Order Block (OB)**：
    - 定义：脉冲前最后一根反向蜡烛（上涨前最后熊市蜡烛=看涨OB）
    - 验证：最低下跌收盘蜡烛的高点被近期蜡烛交易通过
    - 最佳 OB：价格不破蜡烛体中点（mean threshold = 50%）
    - 有效性四条件：聪明钱支持、动量方向最高蜡烛、央行目标、无重大后续修正
    
    **Breaker Block (BB)**：
    - 定义：被强脉冲穿透的 OB，无反弹
    - 看涨 BB 要素序列：Low → High → Lower Low → Higher High
    - 看跌 BB 要素序列：High → Low → Higher High → Lower Low
    - 投影目标：A-B 腿的 1 STD
    
    **Mitigation Block (MB)**：
    - 定义：failure swing 结果；市场未能创新高/新低
    - 与 BB 区别：MB = failure swing；BB = successful swing (stop run)
    - ICT 使用整个下跌蜡烛（含影线）作为 MB
    
    **Rejection Block (RB)**：
    - 定义：长影线在高/低点扫流动性后反转
    - 看跌 RB：高点长影线扫 BSL 后下跌
    - 看涨 RB：低点长影线扫 SSL 后上涨
    
    **Propulsion Block (PB)**：
    - 定义：之前交易进入 OB 的蜡烛，承担价格支撑角色
    - 敏感：不应超过 mean threshold (50%)
    
    **Vacuum Block (VB)**：
    - 定义：波动事件（NFP/开盘）造成的价格缺口
    - 流动性真空，高概率回填
    
    **优先级**：最佳 Breaker = 同时触及两级流动性（短期 + HTF）
    
    **输入**: K线序列、脉冲观察、流动性扫荡确认
    **输出**: Block 类型分类 + 有效性判定
    **缺失条件**: "强脉冲""长影线"无量化阈值
- **tags**: [PD-array, OB, breaker, mitigation, rejection, classification]
- **chart_dependency**: 【需看图 PDF p.549–555, p.570–577, p.587–599, p.602–614】各 Block 类型示意图
- **relations**: fw-04 (FVG 是另一种 PD Array), fw-09 (OTE 入场在 PD Array 处), fw-11 (Ch32 入场位置选择)

---

## fw-18 MMXM 状态机（Market Maker Buy/Sell Model）

- **id**: fw-18
- **title**: MMXM 状态机（Market Maker Buy/Sell Model）
- **type**: state-machine / conceptual-model
- **source_chapter**: Ch3 (PDF p.64–66), Ch29 (PDF p.586–590)
- **source_quote**: |
    "Market Maker Buy Model is understanding that the market is going lower to go higher. Same goes for the opposite, on the buy side of the curve smart money starts hedging that's why you already see premature bearish order blocks forming."
- **summary**: |
    做市商买卖模型的曲线状态机：
    
    **Market Maker Buy Model (MMBM)**：
    - 市场先走低再走高（"going lower to go higher"）
    - 曲线卖方 → 遇到 HTF Discount Array → 转入曲线买方
    - 聪明钱在对冲时已形成过早的看跌 OB
    
    **Market Maker Sell Model (MMSM)**：
    - 市场先走高再走低
    - 曲线买方 → 遇到 HTF Premium Array → 转入曲线卖方
    
    **状态转换触发**：
    - 触及 HTF PD Array（Discount/Premium）
    - ERL 被扫后进入 IRL
    - MSS + Displacement 确认方向变化
    
    **与 PO3 的关系**：MMXM 是 PO3 在价格曲线层面的表达
    
    **输入**: HTF PD Array 位置、曲线侧判断
    **输出**: 当前在曲线的哪一侧 + 预期转换点
    **缺失条件**: 曲线侧的实时判定缺客观信号
- **tags**: [MMXM, market-maker, curve, state-machine]
- **chart_dependency**: 【需看图 PDF p.64–66, p.586–590】MMBM/MMSM 曲线示意图
- **relations**: fw-08 (PO3 是时间维度的表达), fw-01 (ERL/IRL 交替驱动曲线转换), fw-17 (PD Array 是转换触发器)

---

## fw-19 机构订单流观察框架（Buy/Sell Side Oriented Market）

- **id**: fw-19
- **title**: 机构订单流观察框架（Buy/Sell Side Oriented Market 9步）
- **type**: procedure / observation-framework
- **source_chapter**: Ch9 (PDF p.116–118)
- **source_quote**: |
    "Buy Side Oriented Market: 1. Wait for a big bearish displacement after a news embargo. 2. Don't trade the first 10 minutes. 3. Wait & observe order flow: a. Wait for Bearish PD arrays to fail. b. Want to see Bullish displacement. c. Want to see a change in order flow. 4. Down close candles act as support. 5. Up close candles invalidated. 6. Premium arrays invalidated. 7. Discount arrays respected. 8. Anticipate a buy at discount arrays. 9. Maximum 5 points stop loss, aim for 10 points."
- **summary**: |
    新闻日后的机构订单流观察与入场框架：
    
    **Buy Side Oriented（9步）**：
    1. 新闻解禁后等待大的看跌 Displacement
    2. 新闻后 10 分钟内不交易（10:10 AM – 12:00 PM 找设置）
    3. 观察订单流：看跌 PD arrays 失效 → 看涨 Displacement → 订单流变化
    4. 下跌收盘蜡烛充当支撑
    5. 上涨收盘蜡烛失效
    6. 溢价阵列失效
    7. 折价阵列被尊重
    8. 预期在折价阵列买入：FVG/Inversion FVG, OB, Breaker
    9. 最大 5 点止损，目标 10 点 (ES/SP500)
    
    **Sell Side Oriented（镜像9步）**：
    1. 等待大的看涨 Displacement
    2–9. 完全镜像（看涨 PD arrays 失效 → 看跌 Displacement → 溢价阵列卖出）
    
    **适用条件**：NFP, CPI, FOMC, PPI, FED talks; 趋势日
    
    **输入**: 新闻日历、Displacement 观察、PD Array 状态
    **输出**: 入场方向 + 止损/止盈参数
    **缺失条件**: 无
- **tags**: [order-flow, news-trading, buy-side, sell-side, 9-step]
- **chart_dependency**: 【需看图 PDF p.116–118】Buy/Sell Side Oriented 流程图
- **relations**: fw-10 (2022 Model 六步的新闻日变体), fw-11 (Ch32 止损参数一致)

---

## fw-20 Dealing Range 溢价/折价划分流程

- **id**: fw-20
- **title**: Dealing Range 溢价/折价划分与交易流程
- **type**: procedure / analysis-framework
- **source_chapter**: Ch9 (PDF p.128–132), Ch12 (PDF p.183–184)
- **source_quote**: |
    "A dealing range is a price range where both buy and sell sides have been taken out. It is a useful concept because it allows traders to anticipate the market's movement back to a discount and eventually to its sell side."
- **summary**: |
    Dealing Range 的识别与应用流程：
    
    **定义**：买卖双方都被扫过的价格区间
    
    **划分方法**：
    1. 识别关键支撑/阻力位确定范围
    2. 范围上半部 = Premium（溢价）
    3. 范围下半部 = Discount（折价）
    4. 中间 = Equilibrium（均衡，最难预测）
    
    **交易逻辑**：
    - 价格在 EQ 以上 → 技术上溢价，但不自动交易
    - 超买条件可保持溢价并继续走高
    - 关注价格的 DOL：看跌 DOL → 价格将跌破 dealing range 低点；看涨 DOL → 价格将升至 dealing range 高点
    - 扫完两边后寻找底部形成 → 明确反转后保持看涨偏向直到 equilibrium
    
    **嵌套特性**：Dealing range 内可有 dealing range，在所有时间框架上出现
    
    **输入**: 已扫过双边流动性的价格区间
    **输出**: Premium/Discount/Equilibrium 划分 + 交易方向预期
    **缺失条件**: 无
- **tags**: [dealing-range, premium, discount, equilibrium, analysis]
- **chart_dependency**: 【需看图 PDF p.128–132】Dealing Range 标注图
- **relations**: fw-02 (Daily Bias 使用溢价/折价判断), fw-09 (OTE 在折价/溢价区), fw-01 (ERL/IRL 在 dealing range 内交替)

---

## 自检清单

- [x] 每条都在书中有原文根据，不是脑补
- [x] 每条是思考结构或有条件/步骤的机制，而不是具体案例或一句金句
- [x] 原文引用 ≤150 字（英文 ≤100 词）
- [x] 至少标了 1 个 tag
- [x] 不做筛选 — 宁可多收有依据的候选，不因出现一次就漏收
- [x] 跨章节机制已合并并注明所有出处
- [x] 缺参数处已标注"原文未给出 X"或"缺失条件"
- [x] 必须看图的已标【需看图 PDF p.N】
