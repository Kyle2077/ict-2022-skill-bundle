# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| cap.ict2022.session-taboo-filter | 交易时段与禁忌日过滤 | critical | 今天几点可以交易；现在是哪个时段；今天有FOMC/NFP能不能做；亚洲区间很宽还能做伦敦剧本吗 | killzone、session、时段、伦敦开盘、纽约开盘、FOMC、NFP、禁忌日、亚洲区间、taboo day | capabilities/session-taboo-filter.md |
| cap.ict2022.daily-static-anchors | 每日静态价位锚计算 | critical | 把今天关键价位列出来；亚洲区间多宽；CBDR中点在哪；盘前准备 | PDH、PDL、前日高低、午夜开盘、NMO、NYO、Asian range、CBDR、锚、anchors、premarket | capabilities/daily-static-anchors.md |
| cap.ict2022.liquidity-dol-state-machine | 流动性分类与 DOL 识别 | high | 扫完这个低点下一目标是什么；这里是外部还是内部流动性；价格会先去哪个水平 | liquidity、BSL、SSL、DOL、draw on liquidity、ERL、IRL、流动性、止损簇、磁吸 | capabilities/liquidity-dol-state-machine.md |
| cap.ict2022.daily-bias-checklist | 日线偏向判定检查清单 | critical | 今天偏多还是偏空；我的多头想法还成立吗；价格在溢价还是折价；均衡区怎么办 | daily bias、日线偏向、偏多偏空、premium、discount、equilibrium、溢价、折价、均衡 | capabilities/daily-bias-checklist.md |
| cap.ict2022.mss-displacement-gate | MSS/结构突破有效性判定 | high | 这次突破算结构转变吗；为什么这次突破是假的；有没有位移 | MSS、BMS、market structure shift、displacement、位移、结构突破、假突破 | capabilities/mss-displacement-gate.md |
| cap.ict2022.fvg-three-candle | FVG 三蜡烛判定 | critical | 这里有没有FVG；缺口区间在哪；这个FVG算好FVG吗 | FVG、fair value gap、公允价值缺口、三蜡烛、imbalance、不平衡、回补 | capabilities/fvg-three-candle.md |
| cap.ict2022.pd-array-block-dictionary | PD Array/Block 类型识别词典 | high | 这根蜡烛是OB还是Breaker；这个块还有效吗；MB和BB怎么分 | order block、OB、breaker、mitigation、rejection、propulsion、vacuum、PD array、订单块、mean threshold | capabilities/pd-array-block-dictionary.md |
| cap.ict2022.high-probability-entry-risk | 高概率入场检查清单与止损止盈参数 | critical | 今天按清单能不能做；这单止损放几点；止盈怎么分批；9点没回撤还做吗 | checklist、止损、stop loss、止盈、take profit、分批、风险、high probability、入场清单 | capabilities/high-probability-entry-risk.md |
| cap.ict2022.ny-scalp-nine-step | NY Scalp 九步流程 | medium | 纽约开盘能追吗；回撤到哪儿进；9点没回撤还做吗 | NY scalp、纽约时段、剥头皮、回撤入场、62%、9点前、retest high of day | capabilities/ny-scalp-nine-step.md |
| cap.ict2022.ict-2022-model | ICT 2022 Model 六步执行流程 | critical | 按2022模型现在第几步；扫完高点等什么信号；新闻日解禁后怎么找设置 | 2022 model、六步、ICT model、news embargo、buy side oriented、sell side oriented、displacement FVG MSS | capabilities/ict-2022-model.md |
| cap.ict2022.ote-entry-zone | OTE 入场区计算 | high | 回撤到哪儿挂单；0.705是什么；挂单区算一下 | OTE、optimal trade entry、0.62、0.79、0.705、甜蜜点、fib 回撤、挂单区 | capabilities/ote-entry-zone.md |
| cap.ict2022.turtle-soup-entry | Turtle Soup/Stop Run 与 Failure Swing 入场 | high | 刚扫了前低能反手吗；turtle soup怎么挂单；没有stop run只有假突破怎么办 | turtle soup、stop run、扫止损、假突破、反手、failure swing、三重确认、V型 | capabilities/turtle-soup-entry.md |
| cap.ict2022.po3-amd-state-machine | PO3/AMD 节奏状态机 | high | 现在是操纵还是真突破；Judas什么时候出现；周三还在跌要不要停手 | PO3、power of three、AMD、accumulation、manipulation、distribution、Judas swing、操纵、阶段 | capabilities/po3-amd-state-machine.md |
| cap.ict2022.smt-divergence-confirm | SMT 背离确认工具 | medium | ES和NQ背离了吗能进吗；SMT怎么用 | SMT、divergence、背离、ES NQ、EUR GBP、BTC ETH、DXY、裂缝、green light | capabilities/smt-divergence-confirm.md |
| cap.ict2022.top-down-workflow | Top Down 分析与 15m→5m 执行工作流 | medium | 今天按什么顺序看盘；该看哪个时间框架；分析太多理不清 | top down、多时间框架、看盘顺序、盘前流程、15m、5m、timeframe、工作流 | capabilities/top-down-workflow.md |
