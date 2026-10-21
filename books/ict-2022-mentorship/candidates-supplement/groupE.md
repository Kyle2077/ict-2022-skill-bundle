# Group E 补充提取候选（Ch27 / Ch28 / Ch30 / Ch31 / Ch33）

> 提取范围：PDF p.523–536, p.537–546, p.617–621, p.622–626, p.660–671
> 对照已有能力 cap-01…cap-15 + ref-05/ref-06，仅提取增量。

---

## [GE-01] PDH/PDL 流动性池四步识别法 + NY Midnight 分界 + Fade 两场景
- type: procedure
- source: PDF p.523–536
- mechanism:
  **四步识别 Buy-Side Liquidity Pool（p.527）：**
  1. 分析日线图，确定前一天高点；
  2. 寻找 Inside Bar（未突破前日高低的K线），预示潜在反转；
  3. 标记前一天高点作为参考；
  4. 识别潜在买方流动性池。
  Sell-Side 镜像：跌破前日低点 = 卖压信号，继续寻求卖方流动性（p.528–529）。

  **NY Midnight Opening Price 分界（p.529）：**
  定义：纽约东部标准时间(EST)午夜 12:00 AM 的开盘价。
  用法：价格在其上方交易后开始下跌 → 潜在看跌订单流；持续停留在其上方 → 看涨订单流，尤其当突破前日高点时。交易者用此价格在图表上分隔每个交易日。

  **两种 Fade 场景（p.531）：**
  1. 扩张波动中的正常回撤：前日低点被扫 → 价格反弹走高（买入机会）；
  2. 反向扩张波动中的回撤：前日高点被扫 → 价格下跌（卖出机会）。

  **关键纪律（p.533–536）：**
  "We do not simply Buy under a PDL on sole basis Price moves beyond the Previous Day's Low." 必须寻找 PD Array 汇合（discount array）+ HTF institutional order flow 确认（周/日/4H 暗示方向一致）。无汇合不交易。

  **参考最近3天（p.531）：** "Always refer to the last 3 days" — 不仅前一日，还包括前两日的高低点。

  **波动幅度（p.524）：** 日线高低点可产生 25–50 点波动（ES/SP500）。
- chart_dependency: 高【需看图 PDF p.525（5张图）、p.530、p.531、p.532、p.533、p.534、p.535（3张图）、p.536（3张图）】
- counterexamples:
  - 仅因价格超过 PDL/PDH 就入场是明确禁止的（p.533/535）；
  - 必须有 HTF context（周/日/4H）+ PD Array 汇合才能执行 fade。
- mapping:
  - cap-02 已覆盖 PDH/PDL 标记；此处增量为**四步识别流程、Inside Bar 信号、NY Midnight 分界用法、fade 两场景模板、3天回溯窗口、25-50pt 波动预期**。
  - 建议并入 cap-04（Daily Bias Checklist）作为 PDH/PDL 反应判定子流程；
  - NY Midnight Opening Price 建议并入 cap-02 作为额外静态锚（当前 cap-02 仅有 NMO/NYO = NY 00:00 开盘价，与此处 12:00 AM EST 为同一概念，确认已覆盖）。

---

## [GE-02] Hours of Operation 完整时段模板（AM/PM/Lunch/London Raid）
- type: framework
- source: PDF p.537–546
- mechanism:
  **PM Session 13:30–16:00 EST（p.538）：**
  - 关注 RTH（Regular Trading Hours），排除隔夜交易；
  - 目标：识别 HH 和 LL；
  - 看涨时：PM session 最低低点下方 SSL 被扫 = 有利信号（p.539）；
  - PM Session BSL/SSL 抓取可用于 Silver Bullet 或 Judas Swing 设置。

  **Opening Range（p.538）：** 9:30 EST 开市铃后 30 分钟。

  **London Session Raid 02:00–05:00 AM（p.540–541）：**
  - 若开盘后前 30 分钟未接近 PM range，则寻找 London Session Raid；
  - 范围在 ETH（Electronic Trading Hours）图上查找。

  **例行流程（p.541–542）：**
  9:30 开后 30 分钟评估相对 PM/London 位置 → 等待 10:00–11:00 Displacement → Silver Bullet 设置。

  **NY Lunch Raid 12:00–13:30（p.542–544）：**
  - 通常盘整期（除非大趋势日）；
  - 非趋势日：早盘创造低点 → 午餐反弹至午餐高点/早盘高点；
  - 趋势日：价格继续沿早盘方向运行至 15:00–16:00，代表完整日线范围。

  **看涨日午后模式（p.544）：**
  早盘上涨 → 12:00–13:00 盘整 → 14:00–16:00 重复早盘动作但时间框架更短。

  **AM Session 09:30–12:00（p.544–546）：**
  下午回顾 AM range，用于预期市场反转轮廓。若当日 AM + Lunch 均盘整，可参考前一交易日电子盘活动。
- chart_dependency: 高【需看图 PDF p.538（2张）、p.540（2张）、p.541、p.542（2张）、p.543、p.544（2张）、p.545、p.546】
- counterexamples:
  - 午餐时段"通常会完全逆转早盘走势"（p.543），不可盲目延续早盘方向；
  - 原文时区标注为 EST，未说明夏令时 EDT 处理（全书局限）。
- mapping:
  - cap-01 已覆盖五 Killzone 时间窗；此处增量为 **PM Session 13:30–16:00 详细行为模板、Opening Range 30分钟定义、London Session Raid 02:00–05:00、Lunch Raid 12:00–13:30 双剧本、AM Session 09:30–12:00 回顾用法、看涨日午后重复模式**。
  - 建议并入 cap-01 作为时段行为模板扩展（cap-01 当前仅有五 Killzone 概要，缺 PM/Lunch/AM 的详细行为剧本）。

---

## [GE-03] BPR/RDRB 三段式定义 + Breakaway Gap 判定
- type: principle
- source: PDF p.617–621
- mechanism:
  **Balanced Price Range (BPR) 定义（p.617–618）：**
  - Bullish BPR = 价格交付 buy side → sell side → buy side again（UP, DOWN, UP AGAIN）；
  - Bearish BPR = sell side → buy side → sell side again（DOWN, UP, DOWN AGAIN）；
  - 代表买卖双方均衡期间。

  **RDRB = BPR 别名（p.617）：** Redelivered Rebalanced PD Array，与 BPR 完全等价。

  **Breakaway Gap 判定（p.619）：**
  FVG 上方/下方存在 BPR → 该 FVG 保持开放（不会被回填）→ 此 FVG 即为 Breakaway Gap。
  原文："The FVG will stay open because there is a balanced price range above/below it."
- chart_dependency: 高【需看图 PDF p.619（2张图）、p.620（3张图）、p.621（1张图）】
- counterexamples:
  - 原文未给出 BPR 的最小幅度/时间跨度阈值；
  - Breakaway Gap 的"保持开放"是定性判断，无量化确认条件。
- mapping:
  - GLOSSARY g28/g29 已有摘要级定义；此处增量为**三段式精确序列定义 + FVG 保持开放的因果机制**。
  - 建议并入 cap-06（FVG 三蜡烛判定）作为 FVG 有效性修正规则：当 FVG 邻接 BPR 时标记为 Breakaway Gap（不回填预期）；
  - 或建议新增能力「BPR/Breakaway Gap 识别」，理由：BPR 是独立于 FVG 的价格形态，且影响 FVG 回填预期，属于 cap-06 的上游输入。

---

## [GE-04] CBDR ±STD 投影完整规则（扩展 cap-02 标记）
- type: calculation
- source: PDF p.622–626
- mechanism:
  **基础标记（已覆盖于 cap-02）：** 14:00–20:00 NY Time，1h 蜡烛体高低（忽略影线），标记中点。

  **±STD 投影规则（增量）：**
  - 测量 14:00–20:00 范围的点数（低到高）= 1 STD（原文称 deviation，实为范围倍数）；
  - **卖出日：** 预期高点在范围上方 1 STD 形成（常在伦敦时段）→ 然后跌至范围下方 2 STD；
  - **买入日：** 镜像，低点在范围下方 1 STD → 反弹至范围上方 2 STD；
  - **理想止盈：** 2 STD，可达 3 STD（p.624）；
  - **反转轮廓：** 2 STD（London Close / NY Open Reversal）（p.624）；
  - **极高影响新闻：** 可达 4 STD（p.626）；
  - **Judas Swing / Protraction 阶段：** 市场可移动 1–2 STD（p.624）。

  **高概率条件（p.624）：**
  - CBDR < 20 points（ES/SP500）；
  - Asian session range 10–15 points（ES/SP500）；
  - 周二至周四最准确（本周大部分交易量集中于此）。

  **叠加要素（p.626）：**
  季节性倾向 + Daily Premium/Discount Array + IPDA PD Arrays 未满足 → 融合后更高概率。
  例：进入日线溢价阵列 + 预期看跌 → 伦敦开盘 1-2-3 STD 更高创造日高。

  **失效条件（p.626）：**
  - CBDR > 20 points → 不能用 CBDR 做日内交易，只能刷单（scalping）；
  - 价格有时略超 flout（偏差线），属正常现象（p.623）；
  - 日线蜡烛一般 40–50 points（ES/SP500），需结合 bias 判断。

  **影线 vs 实体（p.626）：** ICT 偏好只用实体，但每次仍须查看影线范围。
- chart_dependency: 高【需看图 PDF p.622（1张）、p.624（3张）、p.625（1张）】
- counterexamples:
  - CBDR > 20pt 时日内交易失效，仅限 scalping（p.626）；
  - 周一也可发生但概率较低（p.625）；
  - "STD" 非统计标准差，而是范围倍数（BOOK_OVERVIEW 已注明）；
  - 原文时区标 NY Time，未区分 EST/EDT。
- mapping:
  - cap-02 已覆盖 CBDR 基础标记（高低+中点）；此处增量为 **±1/2/3/4 STD 投影计算、卖出/买入日模板、高概率阈值（<20pt + Asian 10-15pt）、失效条件（>20pt）、叠加要素清单**。
  - 建议并入 cap-02 作为 CBDR 投影扩展模块；或建议新增能力「CBDR STD Projection」，理由：投影计算是独立的数值输出层，与基础标记可分离，且含条件分支（卖出日/买入日/新闻日）。

---

## [GE-05] IPDA Data Range 构建六步 + 季度轮换前瞻应用
- type: procedure
- source: PDF p.660–671
- mechanism:
  **季度轮换（Quarterly Shift）（p.660）：**
  每 3 或 4 个月发生一次市场转变（也提及 6 个月，p.669），可能导致盘整或回撤。强上升趋势中更多表现为盘整而非回撤，Smart Money 借此积累新多头并可能扫日线短期低点后继续走高。

  **IPDA 定义（p.660–661）：** Interbank Price Delivery Algorithm，向全球金融机构提供报价，决定日/周/月/季/年交易范围。作者当作真实机制，未给证据。

  **Data Range 构建六步（p.667–668）：**
  1. 仅使用日线时间框架（Daily Time Frame ONLY）；
  2. 不包含周末，仅计工作日（Mon–Fri）；
  3. 在每个回溯范围（20、40、60 天）内找最高高点和最低低点；
  4. 寻找范围内的 PD Arrays（Old Monthly/Weekly/4H 高低、Gaps、Liquidity Voids、ICT Order Blocks 等）；
  5. 找过去 60 天最高高点和最低低点，将该范围切半；
  6. 在切半范围内定位所有明显的 premium 和 discount arrays。

  **前瞻应用（p.664–666）：**
  - 结构转变后头 20/40/60 天内预期设置发生；
  - 两侧止损清除 + 均衡后 → 看 60 天外下一个范围高低 = 下一个重大波动方向；
  - 结合周线和月线图，可在新市场划分后 20 天内预测重要波动；
  - 20 天 = 近期高低、40 天 = 短期高低、60 天 = 中期高低。

  **SMT 在季度周期中的应用（p.667）：**
  DXY 与 ES 之间 SMT（基础创更高低、基准创更高高），发生在 3/4 个月周期和 60 天展望期内。

  **旧高低长影线处理（p.663）：**
  若旧低/高有很多长影线 → 寻找 Rejection Block，扫的是实体而非影线（turtle soup 预期）。

  **警告（p.669）：**
  "IPDA lookback data ranges alone does not tell you where to buy and sell. There needs to be a blend of concepts, mainly time and price."
- chart_dependency: 高【需看图 PDF p.660（1张）、p.662（1张）、p.663（1张）、p.666（6张）、p.669（5张）】
- counterexamples:
  - IPDA 回顾数据范围单独不能告诉买卖点，必须融合时间和价格（p.669）；
  - 季度轮换"每3/4/6个月"无历史统计验证（BOOK_OVERVIEW 批判已记录）；
  - "obvious arrays" 选择主观，无量化筛选标准；
  - 20/40/60 天回溯期无理论推导。
- mapping:
  - ref-05/ref-06 已有摘要级覆盖；此处增量为**完整六步构建流程、前瞻应用规则（结构转变后20/40/60天）、SMT季度周期用法、旧高低长影线→Rejection Block处理**。
  - 建议新增能力「IPDA Data Range Builder」，理由：六步构建流程是可程序化的独立计算单元（仅日线+工作日+回溯+切半+PD Array定位），产出为 cap-04（Daily Bias）和 cap-15（Top Down）的上游输入；ref-05 仅为摘要级，此处落实为可执行步骤。

---

## glossary-supplement

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
