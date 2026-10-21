# Group A 补充提取候选（Ch5 / Ch7 / Ch8 / Ch15 / Ch18）

> 提取纪律：仅原文有的内容；缺参数标"原文未给出"；每段引用≤150字；需看图标注【需看图 PDF p.N】。
> 已有15能力防重复：cap-01~cap-15 见 BOOK_OVERVIEW.md。

---

## [GA-01] London Session Highs/Lows 三用途与时间窗
- type: procedure
- source: PDF p.84–87
- mechanism:
  伦敦时段定义为纽约时间 02:00–05:00。该时段形成的高点和低点有三个用途：
  1. **Market Sweeping**：市场可能短暂超越这些水平后反转方向（扫流动性）。
  2. **Key Support/Resistance**：接近时遇到增大的买/卖压力，可作为反转区域。
  3. **Intraday Trading Opportunities**：在股市开盘前监控这些水平的形成，用于规划突破或反转交易。
  
  识别步骤：①确定伦敦时段 02:00–05:00 NY；②标记该时段最高价和最低价；③观察价格接近时的反应（反转或突破迹象）。
  
  交易时间窗规则：通常交易时间为 08:30–11:00 NY，可延长至纽约午餐时段；一般建议避免纽约中午之后交易，等到 13:30–16:00 NY 利用下午走势。
- chart_dependency: 低（概念性描述，无特定图表依赖）
- counterexamples: 无明确失效条件；作者仅提示"these times may vary depending on your timezone"。
- mapping: 建议并入 cap-01 session-taboo-filter（补充伦敦高低点作为静态锚的用途说明）+ cap-02 daily-static-anchors（London Session H/L 作为价位锚来源之一）。理由：cap-02 已含 Asian Range/PDH/PDL，但 London Session H/L 未显式列入；cap-01 已有 Killzone 时段但缺少伦敦高低的三用途操作指引。

---

## [GA-02] Three Drives Pattern 结构定义与 Stop Hunt 判别
- type: framework
- source: PDF p.95–100
- mechanism:
  **三驱结构定义**：价格以三个驱动朝 HTF PD Array 方向运动。
  - 第一驱：趋势方向的初始移动至 HTF PD Array（上升=HH+HL，下降=LL+LH）。
  - 第二驱：对 HTF PD Array 的第二次推动（同向 HH+HL 或 LL+LH）。
  - 第三驱：最终移动，应超过第一驱的高点（上升）或低点（下降）。
  
  **关键规则**：若看到3个驱动力朝向流动性池，不需要第三驱实际猎取该流动性池——每次创出新的短期高点时市场已在耗尽短期流动性。"This is how Smart Money established a new position."
  
  **Displacement+FVG 衔接**：三驱完成后，寻找 Displacement（"so obvious similar to how an Elephant would jump into a Children's pool"），Displacement 应打印出 FVG，入场点在 FVG。
  
  **与 Stop Hunt 的判别**：若价格没有像三驱模式那样逐步推进（pressing higher），则预期 Stop Hunt。研究价格突破近期短期高点时的反应——若非逐步推进式上涨，即为 Stop Hunt 而非三驱。
  
  **未达 POI 的强信号**：若第三驱未到达流动性区域/POI 即强烈反弹，这是更强信号——确认对面没有订单，机构已建仓。
- chart_dependency: 高【需看图 PDF p.97, p.99, p.100】
- counterexamples: 
  - 第三驱不必实际扫掉旧高/旧低；
  - 若无三驱形态而价格直接突破短期高点，应预期 Stop Hunt 而非延续。
- mapping: 建议新增能力「three-drives-pattern」。理由：现有15能力中无三驱模式的独立识别框架；cap-05 MSS 判定关注单次位移突破，cap-12 Turtle Soup 关注假突破反转，均不覆盖三驱渐进式流动性耗尽的结构定义。此能力可与 cap-05/cap-06 联动使用。

---

## [GA-03] Morning Trade 四步流程与 8:30/NMO 溢价折价判定
- type: procedure
- source: PDF p.101–107
- mechanism:
  **早盘四步流程**（简化版）：
  1. 08:30 前：识别市场中的流动性池。
  2. 15分钟图准备好后，降至5分钟图寻找入场。
  3. 寻找发生在流动性池下方的价格位移（Displacement）。
  4. 使用 FVG 概念确定入场点。
  
  **8:30 Open 与 Midnight Open (NMO) 溢价/折价判定**：
  - 卖出日：价格在 8:30 Open 之上 = 溢价 → 卖出机会；价格在 NMO 之上 = 溢价 → 卖出机会。
  - 买入日：价格在 8:30 Open 之下 = 折价 → 买入机会；价格在 NMO 之下 = 折价 → 买入机会。
  - 在这些参考水平内寻找 LTF setup（15m/30m 图表），分析 PD Arrays 作为额外确认。
  - 8:30 Open 和 NMO 也可作为目标位或止损参考点。
  
  **Judas Swing 捕捉**：
  - 卖出日：Judas Swing 发生在 8:30 Open 和 NMO 之上（虚假上冲后反转下跌）。
  - 买入日：Judas Swing 发生在 8:30 Open 和 NMO 之下（虚假下探后反转上涨）。
  - NMO = 纽约时间 00:00 开盘价。期望价格在 08:30–09:45 EST 之间朝 MNO 价格交易作为 Manipulation，充当 Judas Swing，与真实方向相反。
  
  **下午 PO3 参考**：若看跌，可使用纽约时间 13:30 开盘价，用法同 Midnight/8:30 Open。
- chart_dependency: 中【需看图 PDF p.104, p.105】
- counterexamples: 无明确失效条件；作者强调早盘波动大、风险增加，需有清晰交易计划。
- mapping: 建议并入 cap-13 po3-amd-state-machine（补充 8:30/NMO 溢价折价判定的具体操作规则和 Judas Swing 的时间窗 08:30–09:45 EST）+ cap-04 daily-bias-checklist（补充买入日/卖出日的溢价折价参考水平）。理由：cap-13 已有 PO3/AMD 阶段但缺少 8:30/NMO 的具体溢价折价操作化定义；cap-04 有偏向检查清单但缺少这两个关键参考价格的判定规则。

---

## [GA-04] Afternoon Session 三策略与加速时点
- type: procedure
- source: PDF p.107–111
- mechanism:
  **下午时段摆动高低点识别**：特别关注 13:30 NY 之后形成的 Swing Highs/Lows。理想形态：每根蜡烛左边有更高的低点、右边也有更高的低点（看涨积累模式）。
  
  **下午三策略**：
  1. **Continuation Trades**：上午看涨 + 下午同向延续 → 按早盘逻辑入场，骑乘动量。
  2. **Reversal Trades**：上午看涨但下午反转 → 注意市场情绪转变或价格行为显著变化，反向交易。
  3. **Measured Moves**：衡量上午移动幅度，预期下午同向等幅移动。例：上午 NQ 移动 70 点 → 下午可能再移 70 点同向。
  
  **下午加速时点**：下午时段常在约 15:40 NY（"20 minutes to four"）和 15:50 NY（"10 minutes before four"）出现加速波动，由 market-on-close orders 驱动。
  
  **Market Profile 三模板**：
  - Template 1：上午趋势 + 下午反转。
  - Template 2：上午趋势 + 下午延续（1:1 Measured Move）。
  - Template 3：上午盘整 + 下午趋势。
- chart_dependency: 中【需看图 PDF p.109, p.110, p.111】
- counterexamples: 无明确失效条件；Measured Move 用"possibility"表述，非保证。
- mapping: 建议新增能力「afternoon-session-playbook」。理由：现有15能力聚焦上午/Killzone 时段，无下午专属策略框架；三模板+加速时点+Measured Move 构成独立的下午操作体系，与 cap-09 NY Scalp 互补但不重叠。

---

## [GA-05] Market Structure 层级定义：STL/STH → ITL/ITH → LTL/LTH
- type: framework
- source: PDF p.301–306
- mechanism:
  **三级结构层级精确定义**：
  1. **STL/STH（Short-Term Low/High）**：市场从 STL 到 STH 再到新 STL 的基本节奏单元。
  2. **ITL（Intermediate Term Low）**：任何 STL 其两侧都有更高的 STL → 该 STL 为 ITL。
  3. **ITH（Intermediate Term High）**：任何 STH 其两侧都有更低的 STH → 该 STH 为 ITH。
  4. **LTL（Long Term Low）**：任何 ITL 其两侧都有更高的 ITL → 该 ITL 为 LTL。
  5. **LTH（Long Term High）**：任何 ITH 其两侧都有更低的 ITH → 该 ITH 为 LTH。
  
  **核心原则**："Interbank Traders do not view Market Structure with Retail's method. Interbank Traders view Price in terms of Liquidity and Imbalances."
  
  **Rebalanced ITH 信号**：若看到 Rebalanced ITH（价格回填了中间高点），表明市场"VERY weak"，是市场向银行间交易者"tipping its hand"的信号。【需看图 PDF p.306】
  
  **不平衡蜡烛验证**：看图表时检查市场是否在回溯一根不平衡蜡烛线，将其归类为 Intermediate H/L，然后确保价格不违反它。若看跌且 Intermediate High 被打破 → 退出等待新设置。
- chart_dependency: 高【需看图 PDF p.303, p.305, p.306, p.319】
- counterexamples: 
  - "FAILURE TO UNDERSTAND MARKET STRUCTURE LIKE AN INTERBANK TRADER WILL LEAD YOU TO FALL VICTIM TO FALSE MARKET STRUCTURE BREAKS."
  - 若 Intermediate High 被打破，必须 step aside，不能再次入场。
- mapping: 建议新增能力「market-structure-hierarchy」（补已知缺口 nr-10）。理由：现有 cap-05 mss-displacement-gate 仅处理 MSS 判定（单次突破+位移），不包含 STL→ITL→LTL 的递归层级定义体系。这是全书结构分析的骨架级概念，缺失会导致无法区分短期噪声与真正的结构转变。

---

## [GA-06] 三时间框架体系与交易者类型映射
- type: framework
- source: PDF p.303–304, p.315
- mechanism:
  **三时间框架角色分配**：
  1. **HTF（最高时间框架）**：提供交易理念、方向偏向、管理交易。日线图是机构和银行使用的级别，"that's where the money is"。
  2. **Mid-level（中级时间框架）**：基于 HTF Level 给出更多结构定义；管理交易。
  3. **LTF（最低时间框架）**：提供更精细的结构定义；用于计时入场和寻找早期反转信号以确定获利时机。
  
  **交易者类型→时间框架映射**【需看图 PDF p.315, p.316】：
  - 不同交易者类型（Scalp/Day/Swing/Position）对应不同的三时间框架组合。
  - 原文提到"3 timeframes per type of trade(r)"但未在文本中列出具体组合表，需从图中读取。
  
  **日线优先原则**："The daily chart is exactly what institutions and banks are using. That's where the money is. This is also where your preferences will be determined." 大部分学习时间应集中在判断日线未来1-2天或一周的走向。逆日线交易="asking for failure"。
- chart_dependency: 高【需看图 PDF p.315, p.316 获取交易者类型-时间框架对照表】
- counterexamples: 作者承认可以在日线看跌时做多，但反问"why would you swim against the tide?"
- mapping: 建议并入 cap-15 top-down-workflow（补充三时间框架的角色分配和日线优先原则的具体操作化定义）。理由：cap-15 已有自上而下工作流但可能缺少 HTF/Mid/LTF 三级角色的精确定义和交易者类型映射表。

---

## [GA-07] BMS/MSB 判定与 Fib STD 投射（-2.0 STDV）
- type: calculation
- source: PDF p.322–325
- mechanism:
  **BMS/MSB 判定**：
  - "Once a ITH/ITL is broken, you have a significant break in market structure (BMS/MSB)."
  - 打破 STL+ITL 或仅 ITL/ITH → 重大结构突破。这比简单地说"it took out a short-term low"更有意义。
  - 入场应基于三个时间框架中最低的那个。
  
  **Fib STD 投射方法**：
  - 在 MSS 并找到入场后，使用标准差进行目标投射。
  - 锚定方式：从 ITH（顶部）到 LTL（范围底部）画 Fib。原因："that's the up move, so the swing, from where the decline starts. It's the retracement swing up that fails that starts to decline."
  - 投射目标：**-2.0 STDV**。
  - 一旦低点被取出，即可使用该摆动投射确定目标。【需看图 PDF p.324, p.325】
  
  **持仓验证**：看跌时，所有 up-close 蜡烛应保持价格不高于其水平（作为阻力）；看涨时，down-close 蜡烛应支撑价格。
- chart_dependency: 高【需看图 PDF p.324, p.325, p.326】
- counterexamples: 无明确失效条件；作者强调"-2.0 STDV"为投射目标但未给成功率数据。
- mapping: 建议并入 cap-05 mss-displacement-gate（补充 BMS/MSB 的精确定义：必须打破 ITL/ITH 级别才算重大突破）+ 建议新增或并入 cap-11 ote-entry-zone（补充 Fib STD -2.0 投射作为目标计算方法，与 OTE 入场互补）。理由：现有 cap-05 关注 MSS 发生条件但未量化 BMS vs 普通 STL 突破的区别；Fib STD 投射是独立的目标计算工具，不属于现有任何能力的覆盖范围。

---

## [GA-08] OB 入场前两问与高概率 OB 条件
- type: principle
- source: PDF p.329
- mechanism:
  **进入 Order Block 之前必须回答的两个问题**：
  1. Does Price want to reach higher?（价格想要达到更高吗？）
  2. Does Market Structure support your Order Block?（市场结构支持你的订单块吗？）
  
  **替代方案**：可以使用 Imbalance 代替 Order Block 作为支撑。
  
  **高概率 OB 的两个条件**：
  1. High Probability Order Blocks have an FVG paired with them.（高概率 OB 伴随 FVG。）
  2. High Probability Order Blocks are blended with Time Theory.（高概率 OB 与时间理论融合。）
- chart_dependency: 中【需看图 PDF p.330, p.331】
- counterexamples: 无明确失效条件；两问本身即为过滤机制。
- mapping: 建议并入 cap-07 pd-array-block-dictionary（补充 OB 入场的两问前置检查和"高概率OB=FVG配对+时间理论融合"的质量分级标准）。理由：cap-07 已有 OB 识别规则但缺少入场前的结构化验证问题和质量分级。

---

## [GA-09] FOMC/NFP 禁忌日完整规则与两阶段操纵
- type: procedure
- source: PDF p.399–405
- mechanism:
  **禁忌日完整清单**：
  1. **FOMC 会议日**：每年8次，会议当天为禁忌日。FOMC 决定对市场有重大影响，交易者易做冲动决策。
  2. **NFP 日**：每月第一个周五发布，为禁忌日。
  3. **NFP 周的周四和周五**：ICT 建议避免交易。原因：大量操纵、市场不利、"wait and see"条件、市场在小范围内无目的震荡等待新闻。
  4. **NFP 报告后的周一**：若周初或周三前无假日，周一可能特别波动。
  5. **NFP 周周一/周二/周三有假日时**：周四和周五成为交易焦点，波动可能很大（但仍需谨慎）。
  6. **FOMC 事件后的伦敦开盘**：ICT 建议避免交易，因 whipsaw 风险。
  
  **FOMC 两阶段操纵**：
  - FOMC 是两阶段事件，发生在下午 2:00。
  - 第一次运行（initial run after the event）通常是假动作，旨在吸引不知情的交易者。
  - 会议期间市场常向相反方向移动（类比海啸：大浪前海水先退）。
  - 关键：不要被初始大动作套牢。
  
  **Seek and Destroy Profile**：预计在周四（周五）出现 Seek and Destroy profile。
  
  **其他回避条件**：
  - 大规模扩张移动之后。
  - 周四已达到 HTF 目标时的周五。
  - 机构人工干预时。
  
  **High Resistance Liquidity 条件**：
  - 当 DXY 价格在区间内不断上下波动时，观察期货市场哪一面移动更容易/更自由。
  - High Resistance = 已被诱导的区域，市场返回动力较小。
  - Low Resistance = 未被触及的流动性所在（较高低点和较低高点的序列）。
  - High Resistance Liquidity 条件下：精度偏差、PD Arrays 不如平时可靠。
- chart_dependency: 低【需看图 PDF p.402, p.404 辅助理解但规则本身为文字描述】
- counterexamples: 
  - "Sometimes price might not follow these rules and that creates high resistance liquidity runs."
  - "Sometimes staying on the sidelines and speculating is the best thing to do."
- mapping: 建议并入 cap-01 session-taboo-filter（补已知缺口 nr-09：将上述6类禁忌日+4类回避条件+FOMC两阶段操纵+High/Low Resistance Liquidity定义全部纳入过滤规则）。理由：此前 cap-01 仅有摘要级禁忌日信息，本次逐页细读给出了完整的精确规则集，包括 NFP 周特殊处理、FOMC 两阶段时序、Seek and Destroy profile、High Resistance Liquidity 的操作化定义。

---

## [GA-10] Market Narrative 与 Liquidity Draw 作为结构分析前置
- type: principle
- source: PDF p.307–312
- mechanism:
  **Narrative 优先于结构**：
  - "To effectively recognize Market Structure in a manner akin to that of an Interbank Trader, it's imperative to first grasp the prevailing market narrative."
  - Narrative 引导评估流动性状况；Liquidity Draw 是建立 Daily Bias 的基础。
  
  **三个核心问题**：
  1. What is the current market narrative?
  2. Is it going higher for Buy Side Liquidity or to Rebalance a SIBI?
  3. Is it going lower for Sell Side Liquidity or to Rebalance a BISI?
  
  **市场三阶段**（Accumulation/Manipulation/Distribution）：
  - Accumulation：做市商在不引起显著反向价格变动的情况下建立大头寸。
  - Manipulation：负面消息使弱势玩家恐慌抛售，供应大增。"Remember, market weakness manifests itself in moments of an uptrend, strength in downtrend."
  - Distribution：积累的逆过程。
  
  **SMR（Smart Money Reversal）触发位置**：在关键 HTF 支撑/阻力位发生，形式为 Turtle Soup 或 Failure Swing。
- chart_dependency: 中【需看图 PDF p.308, p.313】
- counterexamples: 无明确失效条件；Narrative 本身为主观判断层。
- mapping: 已覆盖于 cap-04 daily-bias-checklist（Narrative 三问）和 cap-13 po3-amd-state-machine（三阶段定义）。SMR 触发位置已覆盖于 cap-12 turtle-soup-entry。本条仅作交叉验证，不单独提取为新能力。

---

## glossary-supplement

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
