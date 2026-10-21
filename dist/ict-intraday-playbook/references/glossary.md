# ICT 2022 Mentorship 关键概念词典

> **阶段 1 产出** — 术语提取器  
> 来源：《开启ICT 2022导师计划的成功之门》（LumiTraders）  
> 定义均摘自正文，出处标 PDF 页码；缩写表仅有短语而无正文展开的条目已标注。  
> 书中中文译名有明显机器翻译痕迹时，记录原译并给出更准确译法标注。

---

## 一、流动性与价格目标类

### g01 Liquidity (LQ) — 流动性
- **缩写**: LQ
- **书中译名**: 流动性 / 资产流动性（缩写表）
- **作者用法定义**: 散户止损单聚集处——旧高上方的 buy stops（BSL）和旧低下方的 sell stops（SSL）。做市商/算法通过操纵价格触发这些止损来获取流动性。"Liquidity is what allows anyone to buy or sell for a profit, or a loss."（PDF p.39）
- **与常识差异**: 常识指市场深度/成交量/买卖价差窄度；作者特指"可被猎取的止损簇"，是做市商的燃料而非交易便利性指标。
- **首次定义出处**: PDF p.39–47（ch03）
- **同义/近义**: BSL/SSL、Stop Hunt 的目标
- **可计算**: 否（需识别图表上的旧高/旧低/EQH/EQL 位置）

### g02 Buyside Liquidity (BSL) — 买方流动性
- **缩写**: BSL
- **书中译名**: 买方流动性
- **作者用法定义**: "Buy and Sell Side Liquidity (BSL/SSL) are areas of price in which buy stops and or sell stops are mostly residing."（PDF p.47）BSL 位于旧高上方，是空头止损被触发后产生的买入订单流。
- **与常识差异**: 非常识词汇；作者体系中 BSL = 旧高上方的止损簇，不是泛指买方意愿。
- **首次定义出处**: PDF p.47（ch03）
- **同义/近义**: External Range Liquidity（当位于区间外部时）
- **可计算**: 否

### g03 Sellside Liquidity (SSL) — 卖方流动性
- **缩写**: SSL
- **书中译名**: 卖方流动性
- **作者用法定义**: 旧低下方的 sell stops 聚集区。多头止损被触发后产生的卖出订单流。与 BSL 对称。（PDF p.40–47）
- **与常识差异**: 同上
- **首次定义出处**: PDF p.40（ch03）
- **同义/近义**: External Range Liquidity（当位于区间外部时）
- **可计算**: 否

### g04 Draw on Liquidity (DOL) — 流动性磁吸目标
- **缩写**: DOL
- **书中译名**: 取出流动性 / 提取流动性（误译；应为"流动性吸引力/磁吸目标"）
- **作者用法定义**: 价格下一个磁吸目标——某组止损或某个不平衡。"As a day trader, the DOL can be PWH/PWL, PDH/L, or session High/Low from Asia, London, or New York paired with EQH/EQL with a Low Resistance Liquidity Run (LRLR) condition."（PDF p.54）"Price will seek the liquidity to either reverse or continue in within its expansion move."（PDF p.47）
- **与常识差异**: 完全自创概念；不是"提取/消耗流动性"的动作，而是"价格被吸引前往的目标位"。
- **首次定义出处**: PDF p.54（ch03）
- **同义/近义**: Magnet、Target
- **可计算**: 部分（PDH/PDL/PWH/PWL 可计算；EQH/EQL 需视觉识别）

### g05 External Range Liquidity (ERL) — 外部范围流动性
- **缩写**: ERL
- **书中译名**: 外部范围流动性
- **作者用法定义**: 定义区间外部的旧高/旧低处的止损流动性。"External means outside of something, on the exterior. LIQUIDITY refers order above highs and lows."（PDF p.59）当 ERL 被扫后，下一个 DOL 转为内部流动性（FVG/OB 等）。
- **与常识差异**: 自创分类；将流动性按"区间内外"二分。
- **首次定义出处**: PDF p.56–59（ch03）
- **同义/近义**: Old High/Old Low、BSL/SSL（当位于区间边界时）
- **可计算**: 否

### g06 Internal Range Liquidity (IRL) — 内部范围流动性
- **缩写**: IRL
- **书中译名**: 内部范围流动性
- **作者用法定义**: 定义区间内部的机构参考点（FVG、OB、Volume Imbalance 等）。"Internal means inside of something; within the body."（PDF p.59）当 IRL 被触及后，下一个 DOL 转为 ERL。ERL↔IRL 交替循环构成一切行情的骨架。
- **与常识差异**: 自创分类
- **首次定义出处**: PDF p.54–59（ch03）
- **同义/近义**: FVG、OB、MB 等 PD Array 成员
- **可计算**: 否

### g07 Low Resistance Liquidity Run (LRLR) — 低阻力流动性运行
- **缩写**: LRLR
- **书中译名**: 低阻力流动性挤兑（"挤兑"为误译；应为"低阻力流动性通道/路径"）
- **作者用法定义**: 流动性停留在最小阻力处，容易被清扫。"Low Resistance Liquidity Runs (LRLR) are the most ideal trading conditions in the market... Price movement requires minimal effort to access this liquidity."（PDF p.77）ICT 鼓励追求"low-hanging fruit"。
- **与常识差异**: 自创概念；描述价格到达目标的难易程度。
- **首次定义出处**: PDF p.77（ch03）
- **同义/近义**: Low-Hanging Fruit
- **可计算**: 否（主观判断阻力大小）

### g08 High Resistance Liquidity Run (HRLR) — 高阻力流动性运行
- **缩写**: HRLR
- **书中译名**: 高阻力流动性挤兑（同上误译）
- **作者用法定义**: 流动性在被清除前受到很大阻力。"Price will encounter greater difficulty in expanding and accessing this liquidity. It will demand maximum effort from the price to reach this liquidity."（PDF p.78）
- **与常识差异**: 自创概念；与 LRLR 对立。
- **首次定义出处**: PDF p.78（ch03）
- **同义/近义**: 无
- **可计算**: 否

### g09 Equal Highs / Equal Lows (EQH/EQL) — 等高/等低
- **缩写**: EQH/EQL
- **书中译名**: 同等高/同等低
- **作者用法定义**: 市场多次达到类似价格水平形成的流动性池。"Relative equal lows occur when the market reaches similar price levels multiple times. These lows indicate a potential support level."（PDF p.29）EQH/EQL 是巨大的流动性池，机构总是向这些水平靠拢以撤出散户。（PDF p.54）
- **与常识差异**: 常识中"双顶/双底"是反转信号；作者视为流动性磁铁。
- **首次定义出处**: PDF p.29（ch02）、p.54（ch03）
- **同义/近义**: Relative Equal Highs/Lows
- **可计算**: 否

---

## 二、价格结构与位移类

### g10 Market Structure Shift (MSS) — 市场结构转变
- **缩写**: MSS
- **书中译名**: 市场结构转变
- **作者用法定义**: 价格传递方向的转变。"MSS must be energetic and leave behind displacement to ensure that market is looking to reverse."（PDF p.80）跌破/突破前短期高低点且**必须伴随 Displacement**。无位移的"结构突破"不算数。（PDF p.81）
- **与常识差异**: 常识的结构突破不要求位移力度；作者的 MSS 必须有 Displacement 才有效。
- **首次定义出处**: PDF p.80–81（ch04）
- **同义/近义**: BMS（Break of Market Structure）、MSB（Market Structure Break）— 三者含义相同
- **可计算**: 否（Displacement 靠视觉判断）

### g11 Break of Market Structure (BMS) / Market Structure Break (MSB)
- **缩写**: BMS / MSB
- **书中译名**: 市场结构的断裂
- **作者用法定义**: 与 MSS 同义。缩写表中 BMS = Break of Market Structure。正文中 MSS 更常用。
- **与常识差异**: 同 MSS
- **首次定义出处**: 仅缩写表条目（p.10），正文使用 MSS
- **同义/近义**: MSS、BoS（Break of Structure）
- **可计算**: 否

### g12 Displacement — 位移
- **缩写**: 无
- **书中译名**: 位移 / 排水量（"排水量"为严重误译；应统一为"位移"）
- **作者用法定义**: "A location in price where someone with a lot of money comes into the marketplace with a strong conviction to move price higher or lower very quickly. Displacement is characterized by strong and quick price movement that leave behind Fair Value Gaps."（PDF p.142）突破前高/前低的有力K线收盘运动，留下 FVG。"大象跳进儿童泳池"级别。
- **与常识差异**: 无量化定义，靠视觉判断；不是物理学中的排水量。
- **首次定义出处**: PDF p.142（ch10）
- **同义/近义**: Impulse、Strong Move
- **可计算**: 否（主观视觉判断）

### g13 Lack of Displacement — 缺乏位移
- **缩写**: 无
- **书中译名**: 缺少位移
- **作者用法定义**: "When there is no large aggressive candle with a close inside a high or low."（PDF p.144）价格未能突破前高/前低时的状态。在看涨趋势中，低点被取走但无位移 = 潜在多头入场信号；在看跌趋势中，高点未被位移突破 = 潜在空头入场信号。
- **与常识差异**: 自创反向信号概念
- **首次定义出处**: PDF p.144（ch10）
- **同义/近义**: Failure Swing 的前置条件
- **可计算**: 否

---

## 三、公允价值缺口与不平衡类

### g14 Fair Value Gap (FVG) — 公允价值缺口
- **缩写**: FVG
- **书中译名**: 公允价值差距 / 公允价值缺口
- **作者用法定义**: 三根K线序列中的价格不平衡区。Bearish FVG = 蜡烛1低点→蜡烛3高点之间的空档；Bullish FVG = 蜡烛1高点→蜡烛3低点之间的空档。"FVGs are an entry point, a target, and a means to measure shift in sentiment."（PDF p.139）FVG 是机构赞助的脚印，是主要入场/目标/情绪转换工具。
- **与常识差异**: 常识"缺口"指跳空（price gap）；作者的 FVG 可在连续交易中出现，是三根K线的 wick 未覆盖区域。
- **首次定义出处**: PDF p.139–147（ch10）
- **同义/近义**: Imbalance、Inefficiency
- **可计算**: 是（三根K线的 high/low 比较）

### g15 Inversion FVG (IFVG) — 反转公允价值缺口
- **缩写**: IFVG
- **书中译名**: 反转FVG
- **作者用法定义**: 仅在缩写表和 ch09 入场清单中提及："We will anticipate a buy at discount arrays: FVG/Inversion FVG, Order block, Breaker."（PDF p.128）正文未给出独立定义。推测为已被价格穿越后角色互换的 FVG（类似 Breaker 之于 OB）。
- **与常识差异**: 自创概念
- **首次定义出处**: 仅缩写表条目（p.10）+ ch09 列表提及（p.128），正文未展开完整定义
- **同义/近义**: 与 FVG 角色互换相关
- **可计算**: 否（缺正文定义）

### g16 Liquidity Void (LV) — 流动性空白
- **缩写**: LV
- **书中译名**: 流动性空白
- **作者用法定义**: "A range in price where one side of the market liquidity is shown in wide or long one-sided ranges or candles. It occurs when the market aggressively moves away from a consolidation, creating a void of buy-side liquidity."（PDF p.139）长实体K线、极小影线、单向运动造成的真空区。
- **与常识差异**: 比 FVG 更大尺度的不平衡；FVG 是三根K线级别，LV 是多根K线级别的单边运动。
- **首次定义出处**: PDF p.139（ch10）、p.497（ch24）
- **同义/近义**: Imbalance（大尺度版本）
- **可计算**: 否

### g17 Volume Imbalance (VI) — 成交量不平衡
- **缩写**: VI
- **书中译名**: 成交量不平衡
- **作者用法定义**: "A range between where one candle's body and another candle's body doesn't touch but there are wicks that overlap in between."（PDF p.55）两根K线实体不重叠但影线交叉的区域。
- **与常识差异**: 不是成交量的数值不平衡，而是K线实体间的价格间隙。
- **首次定义出处**: PDF p.55（ch03）
- **同义/近义**: 与 FVG 类似但尺度更小
- **可计算**: 是

### g18 BISI / SIBI — 买方不平衡卖方低效 / 卖方不平衡买方低效
- **缩写**: BISI / SIBI
- **书中译名**: 买方不平衡卖方效率低下 / 卖方失衡买方低效
- **作者用法定义**: BISI = Buyside Imbalance Sell Side Inefficiency；SIBI = Sellside Imbalance Buyside Inefficiency。算法寻求重新平衡的不平衡类型。"The model aims to trade the market when the algorithm will seek to rebalance a BISI/SIBI."（PDF p.114）50% BISI/SIBI 可以是最终目标。（PDF p.187）
- **与常识差异**: 自创术语；描述价格不平衡的方向性。
- **首次定义出处**: 仅缩写表条目（p.10）+ ch09 使用（p.114）
- **同义/近义**: FVG 的方向性分类标签
- **可计算**: 否

### g19 Consequent Encroachment (CE) — 结果侵蚀 / 中点
- **缩写**: CE
- **书中译名**: 结果侵蚀（误译；应为"后续侵入点"或"中点"）
- **作者用法定义**: 任何缺口或不平衡的中点（50%）。"C.E. - Consequent Encroachment or 'middle point' of any Gap or Inefficiency."（PDF p.494）NWOG 的 50% 即为 CE。
- **与常识差异**: 自创术语；本质就是 50% 中点。
- **首次定义出处**: PDF p.494（ch23）
- **同义/近义**: Midpoint、50% level
- **可计算**: 是

---

## 四、PD Array（溢价/折价阵列）家族

### g20 PD Array (Premium/Discount Array) — 溢价/折价阵列
- **缩写**: PD Array / PDA
- **书中译名**: PD阵列 / 高级阵列（"高级"为 Premium 误译）
- **作者用法定义**: 所有机构参考点的统称家族：OB、Breaker、MB、RB、FVG、Liquidity Void、旧高低点等。价格在 PD Array 之间移动。"Price is going from P/D array to P/D array."（PDF p.54）
- **与常识差异**: 自创分类法；将所有支撑/阻力统一为"溢价/折价阵列"框架。
- **首次定义出处**: PDF p.54（ch03）、p.428（ch09）
- **同义/近义**: Institutional Reference Points
- **可计算**: 否

### g21 Order Block (OB) — 订单块
- **缩写**: OB
- **书中译名**: 订单块
- **作者用法定义**: "A candlestick that initiated a move due to the manipulation of the market maker. Up move or down move began with it, and therefore a large number of limit orders of market makers are concentrated around the OB."（PDF p.466）Bullish OB = 上涨脉冲前的最后一根下跌K线；Bearish OB = 下跌脉冲前的最后一根上涨K线。有效性条件：价格不应跌破/涨破 Mean Threshold（50%）。
- **与常识差异**: 不是供需区的泛称；特指"大玩家订单集中的那根K线"，且有严格的验证规则。
- **首次定义出处**: PDF p.466–476（ch29）
- **同义/近义**: Supply/Demand Zone（但更精确）
- **可计算**: 是（特定K线的 open/close/high/low）

### g22 Breaker Block (BB) — 断路器块 / 突破块
- **缩写**: BB
- **书中译名**: 断裂块 / 断路器块 / 突破块（译名混乱）
- **作者用法定义**: "An order block (OB) broken by a strong impulse without a pullback reaction."（PDF p.547）Bullish Breaker = 旧低被违反前最近 Swing High 中的 up-close 蜡烛，止损被扫且突破该 Swing High 后生效。Key Elements: Low–High–Lower Low–Higher High。（PDF p.451）Bearish Breaker: High–Low–Higher High–Lower Low。（PDF p.459）
- **与常识差异**: 不是简单的"支撑变阻力"；必须是 OB 被强脉冲穿透 + 流动性被扫 + 结构转变后才成立。
- **首次定义出处**: PDF p.547–559（ch29）
- **同义/近义**: Failed OB
- **可计算**: 否（需判断脉冲强度和流动性扫描）

### g23 Mitigation Block (MB) — 缓解块
- **缩写**: MB
- **书中译名**: 缓解块
- **作者用法定义**: 市场未能创造更高高点或更低低点时形成的反转形态。"A mitigation block results from a failure swing. In comparison, a breaker results from a successful swing."（PDF p.592）MB 有失败摆动（failure swing），BB 有止损运行（stop run）。ICT 使用整个下跌K线（含影线）作为 MB。
- **与常识差异**: 与 Breaker 的关键区别：MB = 失败摆动（未创新高/低），BB = 成功摆动（创了新高/低后反转）。
- **首次定义出处**: PDF p.488–496（ch29）
- **同义/近义**: Failure Swing Block
- **可计算**: 否

### g24 Rejection Block (RB) — 拒绝块
- **缩写**: RB
- **书中译名**: 拒绝块 / 剔除块（"剔除"为误译）
- **作者用法定义**: Bearish RB = 高点形成长上影线，价格跑到K线实体上方扫完 BSL 后下跌。Bullish RB = 低点形成长下影线，价格跑到实体下方扫完 SSL 后上涨。"The key is it must be a swing low/high that has a wick or wicks."（PDF p.604）可跨多根K线形成。
- **与常识差异**: 本质是影线作为 OB 的特殊形态；ICT 少数使用止损单入场的模式之一。
- **首次定义出处**: PDF p.602–604（ch29）
- **同义/近义**: Wick OB
- **可计算**: 否

### g25 Propulsion Block (PB) — 推进块
- **缩写**: PB
- **书中译名**: 推进块
- **作者用法定义**: "A candle or bar that has previously traded down (up) into a down (up) candle or bullish (bearish) OB and is taking on the role of price support for higher (lower) price movement."（PDF p.606）直接在 OB 内交易的K线成为新的敏感 OB，不应超过 Mean Threshold 50%。
- **与常识差异**: 自创概念；OB 内的"子OB"。
- **首次定义出处**: PDF p.606–608（ch29）
- **同义/近义**: Nested OB
- **可计算**: 否

### g26 Vacuum Block (VB) — 真空块
- **缩写**: VB
- **书中译名**: 真空块
- **作者用法定义**: 因波动事件（如 NFP、时段开盘）在价格行为中产生的缺口。"The gap is formed due to the 'vacuum' of liquidity, directly related to the event."（PDF p.610）两点之间没有交易 = 流动性真空。并非所有缺口都会完全填补。
- **与常识差异**: 特指事件驱动的缺口，区别于普通 FVG。
- **首次定义出处**: PDF p.610–615（ch29）
- **同义/近义**: Breakout Gap、Event Gap
- **可计算**: 否

### g27 Reclaimed Order Block (ROB) — 回收订单块
- **缩写**: ROB
- **书中译名**: 回收订单块
- **作者用法定义**: Bullish ROB = 先前用于 Buy Price 的K线，短期反弹确认轻微位移，在曲线买方被回收做多。Bearish ROB = 先前用于 Sell Price 的K线，短期下跌确认轻微位移。（PDF p.587–588）
- **与常识差异**: 自创概念；旧 OB 在新方向上被"回收"重用。
- **首次定义出处**: PDF p.587–588（ch29）
- **同义/近义**: Reused OB
- **可计算**: 否

### g28 Redelivered Rebalanced PD Array (RDRB) / Balanced Price Range (BPR)
- **缩写**: RDRB / BPR
- **书中译名**: 重新递送的再平衡PD阵列 / 平衡价格范围
- **作者用法定义**: 经历了买卖双方压力的价格区间。Bullish BPR = UP→DOWN→UP AGAIN；Bearish BPR = DOWN→UP→DOWN AGAIN。"It is called a balanced price range because it represents a period of equilibrium between buyers and sellers."（PDF p.617–618）RDRB 上方的 FVG 保持开放 = Breakaway Gap。
- **与常识差异**: 自创概念；三段式价格交付模式。
- **首次定义出处**: PDF p.617–618（ch30）
- **同义/近义**: Balanced Price Range
- **可计算**: 否

### g29 Breakaway Gap (BG) — 分离缺口
- **缩写**: BG
- **书中译名**: 分离间隙（"间隙"应为"缺口"）
- **作者用法定义**: 盘整后出现的价格缺口，标志新趋势开始。在 RDRB 语境下，BPR 上方/下方保持开放的 FVG 即为 Breakaway Gap。（PDF p.617–619）
- **与常识差异**: 传统技术分析已有此概念；作者将其纳入 PD Array 体系。
- **首次定义出处**: PDF p.617（ch30）
- **同义/近义**: Breakout Gap
- **可计算**: 否

### g30 Mean Threshold (MT) — 平均阈值
- **缩写**: MT
- **书中译名**: 平均阈值
- **作者用法定义**: OB 总范围的 50% 水平。"Mean threshold – is 50% level of the total range of the order block; we expect price to respect this level."（PDF p.476）最佳 OB 不应看到价格跌破/涨破此水平。测量用实体（open to close），不用影线。
- **与常识差异**: 自创术语；本质是 OB 的 50% 中线。
- **首次定义出处**: PDF p.476（ch29）
- **同义/近义**: OB Midpoint、50% of OB
- **可计算**: 是

---

## 五、时间与节奏类

### g31 Killzone (KZ) — 杀戮地带 / 关键时段
- **缩写**: KZ
- **书中译名**: 杀伤区 / 狩猎地带 / 死亡地带（译名混乱；建议统一为"关键时段"）
- **作者用法定义**: 会话重叠的高成交量时间窗，算法在此猎取流动性。5 个 Killzone（均为纽约时间）：
  1. London Open: 02:00–05:00
  2. New York Open: 07:00–10:00
  3. London Close: 10:00–12:00
  4. CBDR: 14:00–20:00
  5. Asia: 20:00–00:00
  （PDF p.156, ch11）
- **与常识差异**: 自创时段概念；不是地理意义上的"杀戮区"。
- **首次定义出处**: PDF p.155–156（ch11）
- **同义/近义**: Session Overlap、Trading Window
- **可计算**: 是（固定时间窗口）

### g32 Asian Killzone (AKZ) — 亚洲关键时段
- **缩写**: AKZ
- **书中译名**: 亚洲狩猎区 / 亚洲杀手区
- **作者用法定义**: 20:00–00:00 NY Time。通常盘整，决定伦敦/纽约时段的方向偏差。"The Asian Range determines the directional bias for the majority of the London & NY sessions."（PDF p.157）范围高度 = 20:00–Midnight 的最高/最低价。 rarely exceeds 15 points (ES/SP500)。
- **与常识差异**: 自创
- **首次定义出处**: PDF p.157–166（ch11）
- **同义/近义**: Asian Session、Asian Range
- **可计算**: 是

### g33 London Open Killzone (LOKZ) — 伦敦开盘关键时段
- **缩写**: LOKZ
- **书中译名**: 伦敦开盘杀伤区
- **作者用法定义**: 02:00–05:00 NY Time。通常创造当日低点（看涨日）或当日高点（看跌日）。（PDF p.167）
- **首次定义出处**: PDF p.167（ch11）
- **可计算**: 是

### g34 New York Open Killzone (NYOKZ) — 纽约开盘关键时段
- **缩写**: NYOKZ
- **书中译名**: 纽约开盘杀伤区
- **作者用法定义**: 07:00–10:00 NY Time。8:30 AM 新闻解禁后寻找 stop run；9:30 AM 股市开盘造成波动激增，常产生 Judas Swing。（PDF p.151, ch10）
- **首次定义出处**: PDF p.156（ch11）
- **可计算**: 是

### g35 London Close Killzone (LCKZ) — 伦敦收盘关键时段
- **缩写**: LCKZ
- **书中译名**: 伦敦近距离杀伤区（"近距离"为误译；应为"伦敦收盘"）
- **作者用法定义**: 10:00–12:00 NY Time。常出现反转。（PDF p.156）
- **首次定义出处**: PDF p.156（ch11）
- **可计算**: 是

### g36 Power of 3 (PO3) / AMD — 三的力量 / 积累-操纵-分配
- **缩写**: PO3 / AMD
- **书中译名**: PO3 / 积累、操纵、分发（"分发"应为"分配"）
- **作者用法定义**: 市场在重大价格变动前经历的三个阶段：Accumulation（盘整建仓）→ Manipulation（虚假运动扫止损）→ Distribution（真实方向扩张）。适用于日线、周线、月线。"Consolidation is always followed by Expansion. After Expansion comes either Retracement or Reversal."（PDF p.227）**不做** Consolidation→Expansion→Consolidation。
- **与常识差异**: 自创节奏模板；将 Wyckoff 理论简化为三阶段。
- **首次定义出处**: PDF p.215–227（ch13）
- **同义/近义**: AMD = Accumulation, Manipulation, Distribution
- **可计算**: 否

### g37 Judas Swing — 犹大摆动 / 假动作
- **缩写**: 无
- **书中译名**: 犹大秋千 / 假动作（"秋千"为 Swing 误译）
- **作者用法定义**: Manipulation 阶段的虚假初始运动，与真实方向相反。"Manipulation – this will always happen through some kind of news event. This is Judas Swing."（PDF p.223）周线 Judas Swing 通常在周一/周二形成周高或周低。
- **与常识差异**: 自创术语；源自圣经背叛隐喻。
- **首次定义出处**: PDF p.220–223（ch13）
- **同义/近义**: Fake Move、Manipulation Phase
- **可计算**: 否

### g38 Turtle Soup (TS) — 海龟汤 / 假突破反转
- **缩写**: TS
- **书中译名**: 甲鱼汤（"甲鱼"为 Turtle 误译；应为"海龟汤"）
- **作者用法定义**: 假突破旧高/旧低扫止损后反转的模式。"Stop run or turtle soup – highest, most probable trading condition."（PDF p.28）市场交易到关键水平但未立即反应，表明反转前还有一次更深的运行。借用 Larry Williams 术语但纳入自体系。
- **与常识差异**: 原作者 Larry Williams 的海龟汤有特定规则；ICT 版本更宽泛，等同于 Stop Run/Turtle Soup。
- **首次定义出处**: PDF p.28（ch02）
- **同义/近义**: Stop Run、Stop Hunt Pattern
- **可计算**: 否

### g39 Protraction — 延期 / 拖延阶段
- **缩写**: 无
- **书中译名**: 未提供中文译名
- **作者用法定义**: 仅在 ch31/ch32 中提及。"Inside the Protraction lower post 12:00am to 2:00am EST with PD Array."（PDF p.631）与伦敦正常延期卖出日相关，CBDR < 20 点时适用。似乎是 MNO 之后、伦敦开盘之前的价格拖延/盘整阶段。
- **与常识差异**: 自创术语
- **首次定义出处**: PDF p.631（ch32），正文未给出独立完整定义
- **同义/近义**: 与 Accumulation/Consolidation 阶段相关
- **可计算**: 否（缺完整定义）

---

## 六、价位锚与静态坐标类

### g40 Previous Day High / Low (PDH/PDL) — 前日高/低点
- **缩写**: PDH/PDL
- **书中译名**: 前一天高点/低点
- **作者用法定义**: 前一交易日的高点和低点，作为流动性池和 DOL。"Look for the previous day's high and low to look for stop raids."（PDF p.633）
- **首次定义出处**: 缩写表 p.13 + ch27/ch32 广泛使用
- **可计算**: 是

### g41 Previous Week High / Low (PWH/PWL)
- **缩写**: PWH/PWL
- **书中译名**: 一周最高价/低点
- **作者用法定义**: 前一周的高低点，作为 HTF 流动性目标和 DOL。（PDF p.54）
- **首次定义出处**: 缩写表 p.11 + ch03
- **可计算**: 是

### g42 New Week Opening Gap (NWOG) — 新周开盘缺口
- **缩写**: NWOG
- **书中译名**: 新一周开盘缺口
- **作者用法定义**: 周五收盘价与周日开盘价之间的价格区间。"A real dynamic fair value level... a real liquidity void. The algorithm delivers price to these levels to offer fair value and encourage new business."（PDF p.492）像 FVG 一样使用；建议记录最近 5 个 NWOG。
- **与常识差异**: 自创概念；将周末缺口视为算法的公允价值参考。
- **首次定义出处**: PDF p.492–495（ch23）
- **同义/近义**: Weekend Gap
- **可计算**: 是

### g43 New Day Opening Gap (NDOG) — 新日开盘缺口
- **缩写**: NDOG
- **书中译名**: 新一天开盘缺口
- **作者用法定义**: 5pm Close Price 与 6pm Open Price 之间的差额。（PDF p.494）用法同 NWOG。
- **首次定义出处**: PDF p.494（ch23）
- **可计算**: 是

### g44 Central Bank Dealers Range (CBDR) — 央行交易商范围
- **缩写**: CBDR
- **书中译名**: 中央银行交易商范围 / 中央银行交易者的范围
- **作者用法定义**: 纽约时间 14:00–20:00 的 1h 蜡烛体高低区间（忽略影线）。用 ±1/2/3/4 倍范围做目标投影。"For a sell trade, the high of the day will form at same number of points above the range (1 deviation). Target will form at 2 deviations below."（PDF p.623）高概率日要求 CBDR < 20 点 (ES/SP500)。
- **与常识差异**: 自创概念；"STD"实为范围倍数而非统计标准差。
- **首次定义出处**: PDF p.622–625（ch31）
- **同义/近义**: Dealers Range
- **可计算**: 是

### g45 STD — 标准差 / 范围倍数
- **缩写**: STD
- **书中译名**: 标准差（但实际含义不同）
- **作者用法定义**: 书中"Standard Deviation"实为 CBDR 或 Asian Range 的范围倍数，不是统计学标准差。"We aim for a level 1 standard deviation higher/lower than A to B."（PDF p.567）1 STD = 1 倍范围高度。
- **与常识差异**: **重要**：书中的 STD ≠ 统计学 σ；= 价格范围的整数倍。
- **首次定义出处**: PDF p.567（ch29）、p.623（ch31）
- **同义/近义**: Range Multiple、Deviation（书中用法）
- **可计算**: 是

### g46 Average Daily Range (ADR) — 平均每日范围
- **缩写**: ADR
- **书中译名**: 平均每日范围
- **作者用法定义**: 过去 N 天（通常 5 天）的平均日内波动幅度。用于止损计算："Use 50% ADR of the last 5 days subtracted from the Asian Range Low."（PDF p.634）日线蜡烛一般 40-50 点 (ES/SP500)。（PDF p.625）
- **与常识差异**: 与传统 ATR 类似但用于不同目的。
- **首次定义出处**: 缩写表 p.10 + ch32
- **可计算**: 是

### g47 NY Midnight Opening Price (NMO/MNO) — 纽约午夜开盘价
- **缩写**: NMO / OP
- **书中译名**: 纽约午夜开盘价
- **作者用法定义**: 纽约午夜的开盘价，作为日内溢价/折价的分界线。"When you are bullish and MNO price is lower than NYO price → use NYO."（PDF p.152）在 MNO 之上 = 溢价区；之下 = 折价区。
- **首次定义出处**: PDF p.152（ch10）
- **可计算**: 是

### g48 New York Open (NYO) — 纽约开盘价
- **缩写**: NYO
- **书中译名**: 纽约开盘
- **作者用法定义**: 纽约时段开盘价，与 NMO 配合判断溢价/折价位置。（PDF p.152）
- **首次定义出处**: 缩写表 p.12 + ch10
- **可计算**: 是

### g49 Event Horizon — 事件视界
- **缩写**: 无
- **书中译名**: 事件视界
- **作者用法定义**: "Halfway between a NWOG and the closest NWOG is the Event Horizon. It will not allow price to escape the draw to the NWOG & it will create a surge towards the NWOG it got too 'close' to but yet reached."（PDF p.495）两个相邻 NWOG 之间的中点。
- **与常识差异**: 借用物理学术语；自创 PD Array。
- **首次定义出处**: PDF p.495（ch23）
- **同义/近义**: NWOG Midpoint
- **可计算**: 是

### g50 IPDA (Interbank Price Delivery Algorithm) — 银行间价格传递算法
- **缩写**: IPDA
- **书中译名**: 银行间价格传递算法
- **作者用法定义**: 假定的银行间价格传递算法，向全球金融机构提供报价。"IPDA delivers price quotes to global financial institutions and banks, determining higher or lower prices in relation to PD arrays and IPDA data range."（PDF p.660）回溯期：20/40/60 天。作者当作真实存在的机制，未给证据。
- **与常识差异**: 未经证实的假设；被当作事实陈述。
- **首次定义出处**: PDF p.660（ch33）
- **同义/近义**: Algorithm、Market Maker Algorithm
- **可计算**: 是（20/40/60 日范围可计算）

---

## 七、入场与确认工具类

### g51 Optimal Trade Entry (OTE) — 最佳交易入场
- **缩写**: OTE
- **书中译名**: 最佳交易入口 / 最佳交易入场
- **作者用法定义**: Fibonacci 0.62–0.79 回撤区，0.705 为甜蜜点。"Price retraces to the area between the 62% (0.62) and 79% (0.79) Fibonacci levels... With 70.5% being the middle of that and essentially being the sweet spot."（PDF p.530）限价单应放在 0.62–0.79 之间。作者称"80% 情况有效"但无数据来源。
- **与常识差异**: 自创入场区；将 Fib 回撤精确到 0.62–0.79 窄带。
- **首次定义出处**: PDF p.530–536（ch16）
- **同义/近义**: Deep Retracement Zone
- **可计算**: 是

### g52 SMT Divergence — SMT 背离
- **缩写**: SMT DIV
- **书中译名**: SMT发散（"发散"应为"背离"）
- **作者用法定义**: 相关品种间（EURUSD/GBPUSD、ES/NQ、BTC/ETH、DXY/ES）创新高/新低不同步的裂缝。"SMT Divergence is a crack in correlation between two closely correlated pairs."（PDF p.188）**仅作确认工具**，不单独入场。"You are not looking for SMT divergence to take a trade, you use it only around predetermined levels with trade idea in mind."（PDF p.190）
- **与常识差异**: 自创确认工具；不是独立的交易信号。
- **首次定义出处**: PDF p.186–190（ch12）
- **同义/近义**: Intermarket Divergence、Correlation Crack
- **可计算**: 否（需跨品种比较）

### g53 Smart Money Tool (SMT) — 聪明钱工具
- **缩写**: SMT
- **书中译名**: 智能资金工具
- **作者用法定义**: 主要用于 SMT Divergence 分析。通过比较相关品种的强弱来确认交易方向。（PDF p.186–190）
- **首次定义出处**: 缩写表 p.13 + ch12
- **同义/近义**: Intermarket Analysis Tool
- **可计算**: 否

### g54 Premium / Discount / Equilibrium — 溢价 / 折价 / 均衡
- **缩写**: 无
- **书中译名**: 溢价 / 折扣 / 平衡（"折扣"应为"折价"）
- **作者用法定义**: 
  - **Equilibrium**: 波动高点与低点之间的 50% 线。"Equilibrium is the 50% (or middle point) line between a swing high and a swing low."（PDF p.498）
  - **Premium**: Equilibrium 之上的区域；适合卖出。
  - **Discount**: Equilibrium 之下的区域；适合买入。
  "Are we at Premium zone? When we are at premium zone we anticipate price will go down."（PDF p.183）
- **与常识差异**: 将简单的 50% 分位赋予"溢价/折价"的交易含义。
- **首次定义出处**: PDF p.498（ch24）、p.183（ch12）
- **同义/近义**: Fair Value Zone（Equilibrium）
- **可计算**: 是

### g55 Dealing Range — 交易范围
- **缩写**: 无
- **书中译名**: 交易范围
- **作者用法定义**: "A dealing range is a price range where both buy and sell sides have been taken out."（PDF p.405）买卖双方都被扫过的价格区间。通常是盘整期，价格在支撑和阻力之间横向移动。可在所有时间框架上嵌套出现。
- **与常识差异**: 自创概念；强调"双方流动性都已被取走"的前提。
- **首次定义出处**: PDF p.405（ch09）
- **同义/近义**: Consolidation Range
- **可计算**: 否

### g56 Opening Range — 开盘范围
- **缩写**: 无
- **书中译名**: 未提供独立中文译名
- **作者用法定义**: 仅在缩写表和 ch32 中间接提及。通常指 Asian Range 或 London Session Range 的开盘阶段高低范围。"Measure the London session range to right before the New York open the extreme high and low."（PDF p.632）
- **首次定义出处**: 间接提及，无独立定义段落
- **同义/近义**: Asian Range、Session Range
- **可计算**: 是

### g57 Silver Bullet (SB) — 银弹
- **缩写**: SB
- **书中译名**: 银弹
- **作者用法定义**: 仅在缩写表中列出。正文未找到独立定义。在 ICT 社区中通常指特定时间窗口内的高概率 FVG 入场设置，但本书未展开。
- **首次定义出处**: 仅缩写表条目（p.13），正文未展开
- **同义/近义**: 无
- **可计算**: 否（缺正文定义）

### g58 Institutional Order Flow (IOF) — 机构订单流
- **缩写**: IOF
- **书中译名**: 机构订单流
- **作者用法定义**: 机构层面的价格交付方向和意图。"We determine price levels that correspond to the Institutional Order Flow."（PDF p.627）HTF Daily 或 4h 方向是最重要的 IOF 指标。
- **首次定义出处**: 缩写表 p.11 + ch32
- **同义/近义**: Smart Money Direction、HTF Bias
- **可计算**: 否

### g59 Institutional Order Flow Entry Drill (IOFED) — 机构订单流入场演练
- **缩写**: IOFED
- **书中译名**: 机构订单流输入演练（"输入"为 Entry 误译；应为"入场"）
- **作者用法定义**: 仅缩写表条目。正文未找到独立定义。推测为 IOF 框架下的具体入场流程/练习。
- **首次定义出处**: 仅缩写表条目（p.11），正文未展开
- **可计算**: 否

---

## 八、其他重要术语

### g60 Stop Hunt / Stop Run — 止损狩猎 / 止损运行
- **缩写**: 无
- **书中译名**: 停止狩猎 / 停止运行（"停止"为 Stop 误译；应为"止损"）
- **作者用法定义**: 做市商故意触发散户止损单的行为。"Smart money uses this method to take their positions at the price they want."（PDF p.549）市场直接移动到止损点，碰到后立即转向另一方向。
- **与常识差异**: 常识视为阴谋论；作者视为市场运作的正常机制。
- **首次定义出处**: PDF p.38（ch02）、p.549（ch29）
- **同义/近义**: Liquidity Sweep、Turtle Soup
- **可计算**: 否

### g61 Mitigation — 缓解 / 平仓
- **缩写**: 无
- **书中译名**: 缓解
- **作者用法定义**: "The process of closing unprofitable positions with smart capital."（PDF p.575）做市商在 OB 形成时双向开仓，主仓位分配后需回到 OB 平掉亏损的对冲仓位。这是 OB 有效的核心逻辑。
- **与常识差异**: 不是风险管理中的"风险缓解"；特指"大玩家平仓亏损对冲头寸"。
- **首次定义出处**: PDF p.575（ch29）
- **同义/近义**: Position Closing、Breakeven Exit
- **可计算**: 否

### g62 Market Maker Buy/Sell Model (MMXM) — 做市商买入/卖出模型
- **缩写**: MMXM
- **书中译名**: 做市商买入/卖出模式
- **作者用法定义**: "Understanding that the market is going lower to go higher."（PDF p.589）做市商先压低价格（扫 SSL）再拉升的完整模型。Sell Side of Curve → Buy Side of Curve。
- **首次定义出处**: 缩写表 p.11 + ch29
- **同义/近义**: PO3 的具体应用
- **可计算**: 否

### g63 Seek and Destroy (S&D) — 寻找并摧毁
- **缩写**: S&D
- **书中译名**: 寻找并摧毁
- **作者用法定义**: 仅缩写表条目。在 ICT 体系中通常指算法主动寻找并清除流动性池的行为。正文未找到独立定义。
- **首次定义出处**: 仅缩写表条目（p.13），正文未展开
- **可计算**: 否

### g64 Return to Origin / Return to OB (RHO) — 返回原点
- **缩写**: RHO
- **书中译名**: 返回原点或返回订单块
- **作者用法定义**: 仅缩写表条目。价格回到起始 OB 或运动起点的行为。
- **首次定义出处**: 仅缩写表条目（p.13），正文未展开
- **可计算**: 否

### g65 Measuring Gap (MG) — 测量缺口
- **缩写**: MG
- **书中译名**: 测量间隙
- **作者用法定义**: 仅缩写表条目。正文未找到独立定义。
- **首次定义出处**: 仅缩写表条目（p.12），正文未展开
- **可计算**: 否

---

## 九、基础结构术语（缩写表高频条目）

以下术语在缩写表中列出且在正文中频繁使用，但属于通用技术分析词汇，作者用法与常识基本一致：

| ID | 缩写 | 全称 | 书中译名 | 备注 |
|---|---|---|---|---|
| g66 | HH | Higher High | 更高高点 | 通用 |
| g67 | HL | Higher Low | 更高低点 | 通用 |
| g68 | LH | Lower High | 更低高点 | 通用 |
| g69 | LL | Lower Low | 更低低点 | 通用 |
| g70 | SH | Swing High | 波动高点 | 通用 |
| g71 | SL | Stop Loss | 止损 | 通用 |
| g72 | TP | Take-Profit | 止盈 | 通用 |
| g73 | BE | Break-Even | 收支平衡 | 通用 |
| g74 | DD | Drawdown | 减少（应为"回撤"） | 通用 |
| g75 | RR | Risk/Reward | 风险/回报比率 | 通用 |
| g76 | HTF | Higher Time Frame | 更高的时间框架 | 通用 |
| g77 | LTF | Lower Time Frame | 较低的时间框架 | 通用 |
| g78 | TF | Time Frame | 时间框架 | 通用 |
| g79 | PA | Price Action | 价格行为 | 通用 |
| g80 | OF | Order Flow | 订单流 | 通用 |
| g81 | MS | Market Structure | 市场结构 | 通用 |
| g82 | BoS | Break of Structure | 结构断裂 | ≈ MSS/BMS |
| g83 | MM | Market-Maker | 做市商 | 通用 |
| g84 | TZ | Time Zone | 时区 | 通用 |
| g85 | NFP | Non-Farm Payroll | 非农工资报告 | 通用 |
| g86 | TA | Technical Analysis | 技术分析 | 通用 |
| g87 | AD | Accumulation/Distribution | 积累和/或分布 | 通用 |
| g88 | DH/DL | Daily High/Low | 每日最高/最低 | 通用 |
| g89 | HOD/LOD | High/Low of Day | 一天的高潮/低点 | 通用 |
| g90 | HOW/LOW | High/Low of Week | 一周最高/低点 | 通用 |
| g91 | STH/STL | Short-Term High/Low | 短期高/低点 | 通用 |
| g92 | ITH/ITL | Intermediate-Term High/Low | 中期高/低点 | 通用 |
| g93 | LTH/LTL | Long-Term High/Low | 长期高/低点 | 通用 |
| g94 | LO/LC | London Open/Close | 伦敦开盘/收盘 | 通用 |
| g95 | OP | Opening Price | 开盘价 | 通用 |

---

## 统计摘要

- **术语总条数**: 95 条
- **有正文定义的条目**: 72 条
- **仅缩写表条目、正文未展开的条目**: 8 条（IFVG、Silver Bullet、IOFED、S&D、RHO、MG、Protraction 部分、Opening Range 部分）
- **基础通用术语（作者用法≈常识）**: 30 条（g66–g95）
- **核心独创术语（作者用法≠常识）**: 35 条
- **书中有明显误译的术语**: 12 条（已在各条目标注）


---

# 补章术语补充（2026-10-21，Ch5/7/8/14-28/30/31/33 逐页细读）

### 来自 groupA.md
glossary-supplement

以下缩写在所读章节中的首次正文定义情况：

| 缩写 | 定义状态 | 出处 |
|---|---|---|
| IFVG | 未在 ch05/07/08/15/18 中出现定义 | — |
| Silver Bullet | 未在 ch05/07/08/15/18 中出现定义 | — |
| Protraction | 未在 ch05/07/08/15/18 中出现定义 | — |
| Opening Range | 未以术语形式定义；ch08 提到 "8:30 open" 和 "midnight open" 作为参考水平但未使用 "Opening Range" 一词 | ch08 p.101 |
| MG (Measuring Gap) | 未在 ch05/07/08/15/18 中出现定义 | — |
| RHO | 未在 ch05/07/08/15/18 中出现定义 | — |
| IOFED | 未在 ch05/07/08/15/18 中出现定义 | — |
| S&D (Seek and Destroy) | ch18 p.401 提及 "Seek and destroy profile on Thursday (Friday) expected"，但未给出正式定义，仅作为预期 profile 名称使用 | ch18 p.401 |
| SMR (Smart Money Reversal) | ch15 p.313 首次使用："a Smart Money Reversal (SMR) and then a decline"；p.314 进一步说明 SMR 发生在 HTF 关键支撑/阻力位，形式为 Turtle Soup 或 Failure Swing | ch15 p.313–314 |
| BDR/SDR | 未在 ch05/07/08/15/18 中出现定义 | — |
| ATH/ATL | 未在 ch05/07/08/15/18 中出现定义 | — |
| BMS/MSB | ch15 p.322 定义："Once a ITH/ITL is broken, you have a significant break in market structure (BMS/MSB)" | ch15 p.322 |
| STL/STH/ITL/ITH/LTL/LTH | ch15 p.301–302 完整定义（见 GA-05） | ch15 p.301–302 |
| NMO | ch08 p.105 定义："Use the midnight opening (NMO) – 00:00 am NY Time" | ch08 p.105 |
| SIBI/BISI | ch15 p.307 提及但未定义全称；上下文暗示 SIBI=Sell-Side Imbalance Buy-Side Inefficiency, BISI=Buy-Side Imbalance Sell-Side Inefficiency | ch15 p.307 |


### 来自 groupB.md
glossary-supplement

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


### 来自 groupC.md
glossary-supplement

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


### 来自 groupD.md
glossary-supplement

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


### 来自 groupE.md
glossary-supplement

### Silver Bullet
- 正文出处：PDF p.539、p.542
- 正文用法：PM Session BSL/SSL 被抓取后可用于 Silver Bullet 设置（p.539）；10:00–11:00 Displacement 后"sets the stage for the Silver Bullet setup"（p.542）。
- 状态：GLOSSARY g57 已标注"正文未找到独立定义"；Ch28 提供了两处上下文关联（PM liquidity grab → SB、Displacement 10:00–11:00 → SB），但仍无独立机制定义。建议维持 g57 现状，补充引用 Ch28 页码。

### Opening Range
- 正文出处：PDF p.538
- 正文定义："After the Opening bell rings at 9:30 EST, we have a 30-minute period known as the Opening Range."
- 状态：GLOSSARY g56 定义为间接提及；Ch28 给出了精确定义（9:30 EST 后 30 分钟）。建议更新 g56 补充此精确引用。

### BPR (Balanced Price Range)
- 正文出处：PDF p.617–618
- 正文定义：见 GE-03。Bullish = UP→DOWN→UP AGAIN；Bearish = DOWN→UP→DOWN AGAIN。
- 状态：GLOSSARY g28 已有完整定义。无需补充。

### RDRB (Redelivered Rebalanced PD Array)
- 正文出处：PDF p.617
- 正文定义：BPR 的别名，完全等价。"The Redelivered Rebalanced PD array is defined as a price range that has experienced both buying and selling pressure, resulting in a balanced market."
- 状态：GLOSSARY g28 已合并。无需补充。

### BG (Breakaway Gap)
- 正文出处：PDF p.617、p.619
- 正文定义："A Breakaway Gap refers to a gap in price action that occurs after a period of consolidation. It signifies a significant shift in market sentiment and often marks the beginning of a new trend." 在 BPR 语境下：FVG 上/下方存在 BPR → FVG 保持开放 = Breakaway Gap。
- 状态：GLOSSARY g29 已有完整定义。无需补充。

### IPDA (Interbank Price Delivery Algorithm)
- 正文出处：PDF p.660–661
- 正文定义：见 GE-05。
- 状态：GLOSSARY g50 已有完整定义。无需补充。

### Quarterly Shift
- 正文出处：PDF p.660、p.669
- 正文定义："Every 3 or 4 months there's a market shift, it may cause a consolidation or a retracement of whatever price swing had been evolving."（p.660）"The markets will make a quarterly shift every 3, 4, or 6 months."（p.669）
- 状态：GLOSSARY 中无独立条目。建议新增术语条目，引用 p.660/p.669。

### Flout
- 正文出处：PDF p.622–626
- 正文用法：指 CBDR 范围的偏差线/边界。"For a sell trade expect a high at 1 deviation above the flout."（p.622）"Sometimes price will go a little bit above/below the flout."（p.623）
- 含义：CBDR 范围本身或其偏差延伸线；原文用 "flout" 似为 "float" 或 "range boundary" 的非标准拼写/翻译。
- 状态：GLOSSARY 中无条目。建议新增，标注为非标准用语，等同于 CBDR deviation line。

### Immediate Rebalance
- 正文出处：本组章节（Ch27/28/30/31/33）中未出现此术语。
- 状态：不在本组提取范围内。若其他章节有定义，应由对应组提取。
