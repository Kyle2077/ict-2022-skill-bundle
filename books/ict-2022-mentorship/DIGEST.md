# DIGEST — 开启ICT 2022导师计划的成功之门（精华长文）

> 蒸馏自 671 页 / 33 章 / 767 图的 ICT 2022 Mentorship 精翻本（LumiTraders，2023）。**全书 33 章已完整覆盖**（2026-10-21 补齐 Ch5/7/8/14–28/30/31/33）。本文只呈现通过三重验证的方法论；所有数值保留原书口径与品种限定。配套技能：[dist/ict-intraday-playbook](../dist/ict-intraday-playbook/SKILL.md)（28 个能力单元）。

## 这本书在讲什么

一句话：把日内交易变成一套"时间—价格—结构"三轴的读取程序——算法在固定时间窗猎取流动性，价格永远在"重新平衡不平衡"与"寻求流动性"之间往返，交易者要做的不是预测，而是在聪明钱扫完止损之后，站到折价/溢价区的正确一侧。

全书骨架七层：①市场由做市商/算法（IPDA）驱动，散户止损即流动性；②价格只做两件事（平衡不平衡 / 寻流动性），外部与内部流动性交替；③时间先于价格（5 个 Killzone + PO3 三阶段节奏）；④结构确认方向（MSS 必须带位移，FVG 是机构脚印）；⑤入场在折价/溢价的 PD Array；⑥风控纪律（禁忌日、阈值过滤、止损止盈数值化、"不是每天都有交易"）；⑦静态坐标层（前日高低、亚洲区间、CBDR、缺口）。Ch19 与 Ch32 是把全部要素组装成完整流程的集成层。

## 方法论一：时间过滤——先问"能不能交易"，再问"交易什么"

核心逻辑：算法在不同时间窗行为不同。五个 Killzone（纽约时间）：亚洲 20:00–00:00 造区间；伦敦开 02:00–05:00 造当日高低点；纽约开 07:00–10:00 延续或反转；伦敦收 10:00–12:00 修正；14:00–20:00 央行交易商区间定基准。叠加回避规则：利率公告/演讲/假日/全球事件/周目标达成避开伦敦开盘；亚洲区间 >15–20 点(ES) 时等纽约窗；新闻前 10 分钟不交易。

原书示例：Ch11 伦敦窗剧本——看涨日伦敦造日低：突袭亚洲高点止损→回落测试支撑与 OTE→在开盘价与亚洲摆动低点下方买入。

何时失效：作者未说明夏令时处理（全书标 EST/纽约时间），全年运行会整体偏移一小时；禁忌日清单是枚举式，未列事件不等于安全。
→ 技能：session-taboo-filter

## 方法论二：流动性状态机——价格下一站去哪

核心逻辑：两类磁吸目标交替。外部流动性（ERL，旧高/旧低上方的止损簇）被扫后，下一目标转为内部流动性（IRL，FVG/OB 等不平衡）；不平衡回补后，目标又回到外部。DOL（Draw on Liquidity）就是"下一个磁吸目标"。七类流动性：日/周/月高低、15m/1h 高低、1–5m 高低、等高/等低、摆动点、区间外、趋势线后。

原书示例：Ch3 的月/周/日/4H 交替图——扫旧低后价格转向未回补 FVG，回补后再转向对面旧高；作者以此定日线偏向。

何时失效：LRLR/HRLR（低/高阻力流动性运行）无量化度量，只能定性；"价格只做两件事"是作者公理，基本面单边行情可能长期不遵守交替。两条内建警告：不在破旧高买/破旧低卖；弹跳越多的支撑阻力越容易被扫。
→ 技能：liquidity-dol-state-machine、daily-bias-checklist

## 方法论三：FVG 与位移——机构赞助的脚印

核心逻辑：FVG 是三根连续K线之间的空档。Bearish：蜡烛1低点→蜡烛3高点；bullish 镜像。它由"位移"（有力突破前高/前低的收盘运动）产生，因此既是入场区、目标区，也是"这次突破是否机构赞助"的证据。反过来，lack of displacement（扫了流动性却没有位移）本身就是反向信号。无空档即平衡价格行为，非 FVG。

原书示例：书 p.119（PDF p.147）三蜡烛标注图，本蒸馏已实际看图核查：红烛 1/2/3 与蓝色 FVG 区间边界逐一对应。

何时失效：FVG 最小宽度原书未定义；"高概率回补"从未给出数值，也不讨论不回补条件。
→ 技能：fvg-three-candle、mss-displacement-gate

## 方法论四：PO3 节奏——一天是一出三幕剧

核心逻辑：积累（盘整造流动性）→操纵（Judas 假突破扫止损）→分配（真实扩张）。剧本语法两条铁律：盘整后只能接扩张，绝不直接回撤/反转；不做"盘整→扩张→盘整"。日线窗口表（纽约时间）：20–00 积累、00–05 操纵（日高低常在此形成）、05–08 小盘整、08–08:30 回撤、08:30–10 扩张或反转、10–12 反转、16 收盘盘整。新闻改写剧本：8:30 有重大新闻则 9:30 无 Judas，改 10:00–10:10。周线：周高低常在周一二形成；周三低点后继续下跌→当日停手。

原书示例：书 p.142（PDF p.224）Reversal/Consolidation 段图，已核查：伦敦开盘扫止损后扩张"直到纽约 5 点"，05:00–08:00 回到均衡盘整。

何时失效：阶段切换没有客观实时信号，确认依赖 MSS+回到午夜开盘价另一侧（滞后证据）；三阶段语法是不可证伪的叙事框架。
→ 技能：po3-amd-state-machine

## 方法论五：执行链与风控——全书唯一的数值层

核心逻辑：ICT 2022 Model 六步：扫主要流动性→反向位移留 FVG→摆动点与 FVG 蜡烛对齐=MSS→50% Fib→FVG 位于均衡/流动性一侧→FVG 内限价入场。Ch32 把它落成参数表（ES/SP500）：盘前硬门=HTF 方向+CBDR<20 点+亚洲区间 10–15 点+非禁忌日+（NY 剧本）9:00 前存在 7–10 点回撤；止损六档（CBDR+PDA 重叠 15 点、亚洲下方运行 20 点、Stop Raid 15 点、首次回撤+OB 为 LOD 下 5 点、二次回报 15 点、兜底=5 日 50% ADR−亚洲低）；止盈七路分批（10–15 点先取、每 2 倍区间减仓、PDH+2–7 点、1h 范围 50%、5 日 ADR 处 60–80%、时间止盈节点）。OTE 入场区=Fib 0.62–0.79，0.705 甜蜜点。

原书示例：书 p.303（PDF p.407）模型双图（Old High 版与 Old FVG 版），已核查：绿线目标、黄色 FVG 带、品红 MSS 线与短期低点对齐。

何时失效：全部点数仅 ES 标定，跨品种无换算；清单是"组合增信"非严格 AND；"高概率"无统计依据；"clear unobstructed path"无判定法。纪律原文："Whatever you use as the initial Stop Loss — Do Not Rush to move it."
→ 技能：ict-2022-model、high-probability-entry-risk、ote-entry-zone、ny-scalp-nine-step、turtle-soup-entry

## 方法论六：结构层级——"破位"的分量由级别决定

核心逻辑：结构点递归升级。STL 两侧邻居都更高→升为 ITL；ITL 两侧邻居都更高→升为 LTL（高点侧同理 STH→ITH→LTH）。级别决定突破分量：只破 STL 是噪音级，破 ITL/ITH 才是 BMS/MSB（重大结构突破）。配套两个工具：持仓验证（看跌时 up-close 蜡烛应持续压制价格，被收盘越过=结构存疑）、目标投射（ITH→LTL 锚 Fib，投射 -2.0 STDV）。SMR 的 MSB 判据更严：扩张腿内必须含 FVG，"If this FVG is not present, we don't class this as a valid break"；且有 FVG 时不必收盘低于摆动低点即算确认。

何时失效：-2.0 STDV 无成功率数据、"为何 -2.0"原文未论证；层级判定依赖摆动点口径（TF/影线），口径不同结论不同。作者警告：不理解银行间结构观会成为虚假 MSB 的受害者；ITH 被打破必须 step aside。
→ 技能：market-structure-hierarchy（图证已核：书 p.215 层级圈注图）

## 方法论七：MMXM——把"做市商送价"写成状态机

核心逻辑：HTF 看跌时的完整路径。Initial Consolidation（起点）→ Buy Program 沿 BDR（起点盘整低点→HTF level）逐级积累，用 Fib 分 25% 象限，50% 处出现 Measuring Gap（不回填，用作 terminus 校验）→ 最后的 Manipulation Swing 诱多 → SMR 翻转（Type1 = 创更高高后破旧摆动低；Type2 = 第二峰不创新高，需 SMT 背离佐证）→ Sell Program 沿 SDR 分配到 calibrated terminus。Terminus 校准三重汇合：起点盘整下方 point-range 增量（NQ 5/10/15/20 点、ES 2/5/7/10 点）+ Manipulation Swing 的 2–2.5 STD 投影 + HTF level。分配循环四要素：run liquidity→rebalance/run stops→在曲线左侧 mitigate→继续走低。SMR 后入场三选一：2022 Model / OFED / Breaker+FVG；Low Risk Sell = change in state 确认后回撤至 bearish OB（不收盘破 mean threshold）。

原书示例：书 p.323（BDR 边界=起点盘整→HTF Level）与书 p.337（Type1 理想反转 vs Type2 红 X 失败峰 + SMT 确认条件），两图均已实际看图核查。

何时失效：积累/分配阶段"可以超过两个"但无计数停止规则；Calibration 数值为经验值、无波动率调整；仅在 HTF 方向明确时启动（方向不明=不启动）。
→ 技能：mmxm-state-machine（ref-01 概念模型升级为可执行能力）

## 方法论八：周初与区间剧本

核心逻辑：Monday Range 有严格的"周一不交易"纪律——周一只造区间，收盘后标记高低；周二起等"一侧止损被扫 + 价格收回区间内"这个事件，事件后 MSS 确认入场、目标区间对面；HTF order flow 不明就在 midrange(50%) 止盈转无风险。放弃条件明确：只有一侧被扫后变成支撑/阻力、或价格远离不回。配套两个通用工具：区间边界四种确定法（引发对面横扫的极值/同侧扫前极值/EQH-EQL/前期高低，影线或实体以 midrange 对齐为准），以及亚洲幅度双叙事分流（Asian ≤10–15pt→伦敦反转剧本；>15pt→避开 LOKZ 等 NYKZ；链式 bias：Asia→London→NY）。

何时失效：作者明示"有些周只有一侧被扫"→该周剧本失效；点数阈值仅 ES；假期周处理原文未给。
→ 技能：monday-range-procedure

## 方法论九：9:30 之后的全天剧本

核心逻辑：AM（09:30–12:00）造参照；Lunch（12:00–13:30）非趋势日通常完全逆转早盘、趋势日延续至 15:00–16:00；PM（13:30–16:00）识别 HH/LL，看涨时"PM 最低低点下方 SSL 被扫"是有利信号；15:40 与 15:50 因 market-on-close 订单出现加速。下午入场三选一：延续、反转、Measured Move（上午幅度 1:1 复制，原文用 possibility 表述）。另有四种日内模板：Classic Buy/Sell Day（主要周一二、开盘价到支撑 7–12pt、超 12pt 等纽约、趋势至 11:00 EST、12:00 前锁 5–7pt、开盘先涨不追）、Reversal（伦敦造极值+纽约反转，监控 4–5am/7–8am）、Range to NY Open Rally（新闻日破 London lows 后反弹）、Consolidation Raid on News（消息破盘整扫止损→走真方向；**消息后 5 分钟内未在支撑/阻力被拒绝=离场**）。

何时失效：模板是经验归纳无频率统计；午餐反转是"通常"非必然；4–5am/7–8am 原文未标时区。
→ 技能：afternoon-hours-playbook、daily-templates-playbook

## 方法论十：跨日跨周缺口与 IPDA 坐标

核心逻辑：NWOG = 周五 17:00（NY）收盘到周日 18:00 开盘之间的真空区，画法用 5m 图且仅 RTH 可见（ETH 图上不存在）；CE = 该区间 50% 中点，价格尊重它；上缺口=支撑、下缺口=阻力；至少记录最近 5 个（ICT：前 4 周 NWOG = 算法回访真实公允价值的"X-ray view"）；多个聚集→区间震荡。NDOG = 每日 17:00–18:00 的同类缺口。Event Horizon = 相邻两 NWOG 的中点位置，阻止价格逃离缺口吸引。IPDA Data Range 则是周度坐标：仅日线、只数工作日，取 20/40/60 日回溯窗高低与窗内 PD Arrays，60 日范围切半标折溢价；结构转变后 20/40/60 天内预期设置发生。

原书示例：书 p.390 NWOG 标注图已核查——粉色区间=NWOG High/Low、绿线 C.E.=50%、蓝色注释框给出周日首根 18:00 NY 与周五末根 17:00 NY。

何时失效：作者亲自警告"IPDA lookback data ranges alone does not tell you where to buy and sell"；20/40/60 回溯期与季度轮换频率均无统计验证；缺口回填非即时；经纪商 RTH/ETH 定义差异会改变缺口。
→ 技能：nwog-ndog-anchors、ipda-data-range-builder（图证已核）

## 方法论十一：三个补充判别器

- **三驱模式**：朝 HTF 阵列的三次脉冲=流动性耗尽计数；第三驱不必实际猎取流动性池（每次创新短期极值已在耗尽）；三驱后等位移打印 FVG 入场。关键判别：逐级推进=三驱，单针式突破短期极值=预期 Stop Hunt（转反手逻辑）。第三驱未达 POI 即强反转是更强信号。→ three-drives-pattern
- **Order Flow 形成门**：单次 MSS 只说明结构变了，OF 形成才说明机构开始持续交付——三条件（破结构或沿趋势攫流动性 / 取对侧止损 / 创同向新极值对）齐备才算成立，回调退出 OF 区=激活。内建反直觉警告："It is unprofitable to enter from the Order Flow zone itself, the stop loss is already too big." 入场在 OF 内的 OB。→ order-flow-formation-gate
- **机构感知区间模型**：range-bound 市的独立反转模型——BSL/EQH 被扫后，发动扫掠的最后一根 down-close 蜡烛 = bearish breaker；突破它后回踩卖出；止损在 breaker 或其上方 bearish OB；跌破 SSL 即出场。顶层铁律：Never buy above old highs, never sell below old lows。→ institutional-perception-model
- **ATM 方法**：60 分钟图的 stop-hunt 回踩——Key High 形成时先打破其前方短期低点，之后回踩该被破低点，突破结构并取满 2 个 STL 后在 Breaker Block 回调入场；止损 Key High 或 Breaker，止盈看向第二个 STL 之外。作者明示"this is only a setup, you have to frame context behind every setup"。→ ict-atm-method
- **Opening Range 投影与 CPE**：Range = HOD − Opening Price，开盘价下方 1:1 对称偏离带即预期空间；CPE = 开盘价附近区域，是错过初始入场与金字塔加仓的 FVG/Imbalance/Raid 聚集处；开盘区间两侧均被 take 才构成 dealing range（折溢价划分的前提）。注：原文投影公式字面量纲不通，本蒸馏按"1:1 deviation below"的对称语义实现并登记为实现约定。→ opening-range-cpe
- **DXY 联动与季节性**：DXY 跌→指数涨、DXY 涨→指数跌、DXY 盘整→指数涨（复苏期存在同涨例外）；月度季节结构可查表。作者三重免责（not absolute / not guarantees / not a panacea），10 月后 EURUSD/DXY 均值背离信号不可靠——因此只作先验加权标记，不单独产生结论。→ dxy-seasonal-filter

## 反例与陷阱（作者亲自警告的）

1. 不在旧高之上买、旧低之下卖——全书铁律。
2. FOMC/NFP 周与公告日是"寻求并摧毁"剧本：大量操纵、无意义盘整、PD Arrays 失效。
3. 亚洲区间过宽（>15–20 点 ES）时伦敦剧本危险，等纽约。
4. 9:00 前没有 7–10 点回撤→当天不做 NY 剧本。
5. SMT 背离只作确认：没有交易想法时的背离不是信号。
6. 无位移的"结构突破"是诱骗；无位移本身才是信号。
7. 止损不要急于移动；不挑顶底；ITH/ITL 被违反就场边观望。
8. 弹跳越多的支撑/阻力，越可能是下一个被扫的流动性池（反直觉）。
9. London Close 可能反转日/周方向，不可盲目延续早盘趋势。
10. 周三低点后继续下跌→承认错误，当日停手。
11. Monday Range："有些周只有一侧被扫"→该周剧本失效，远离或换品种；价格远离区间不回来=放弃。
12. 午餐时段（12:00–13:30）非趋势日"通常会完全逆转早盘走势"，不可追早盘方向。
13. 新闻盘整扫掠：消息发布后 5 分钟内价格未在支撑/阻力被拒绝→分析可能错误，离场。
14. Order Flow 区本身不是入场点："stop loss is already too big"——入场在 OF 内的 OB。
15. IPDA 回溯范围单独不告诉买卖点："There needs to be a blend of concepts, mainly time and price."
16. 季节性只是路线图不是保证（作者三重免责）；10 月后 EURUSD/DXY 均值背离，信号不可靠。
17. 无 FVG 的结构突破不算有效 break（SMR/MSB 判据）；ITH 被打破必须 step aside。

## 作者的局限（批判性阅读必需）

- **零统计证据**：全书无回测、无胜率、无样本量。仅有的两个量化声明——"OTE 80% 有效"与一张"6 胜 1 负"图例——都没有测试条件，作者自己也要求读者自行验证。
- **不可证伪的叙事**：IPDA（银行间价格传递算法）、做市商统一意图、"机构订单残留在蜡烛上"都是公理式假设；"价格要么寻流动性、要么平衡不平衡"的二分法使任何走势都能被事后解释。
- **幸存者偏差**：767 张图几乎全是事后标注的成功案例，失败形态的频率从未展示。
- **口径缺口**：夏令时未说明（全书标 EST/纽约时间）；点数仅 ES 标定；Displacement/"强脉冲"/"长影线"无量化阈值；Ch14 的 Opening Range 投影公式字面量纲不通（按对称偏离语义实现并登记）；NDOG 5PM/6PM 时区未标；假期周的 Monday Range 处理未给。
- **立场**：LumiTraders 是 ICT 概念的二次传播者与社群运营者，利益在推广而非独立验证；中文译文存在机器翻译痕迹（如 stop hunt 译"停止狩猎"、Turtle Soup 译"甲鱼汤"）。

把这本书当"一套自洽的观察语法 + 一组可执行的纪律"来用，比当"被验证的盈利系统"来用更接近它的真实价值。

## 术语速览（完整词典见技能包 references/glossary.md，含补章新增术语）

FVG=三蜡烛不平衡空档；OB=脉冲前最后反向蜡烛；Breaker=被穿透的 OB（成功摆动）；Mitigation=失败摆动块；MSS=带位移的结构转变；DOL=下一磁吸目标；ERL/IRL=外部/内部流动性；OTE=0.62–0.79 回撤入场区；PO3/AMD=积累-操纵-分配；Judas Swing=操纵期假突破；Killzone=会话重叠时间窗；CBDR=14:00–20:00 纽约的基准区间；SMT=相关品种极值裂缝（仅确认）。
