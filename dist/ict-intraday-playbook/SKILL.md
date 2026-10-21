---
name: ict-intraday-playbook
description: |
  ICT 2022 导师计划日内交易方法论的单一入口手册：以时间（Killzone/时段节奏）、价格（流动性与 PD Arrays）、结构（MSS/FVG/Displacement）三轴读取机构订单流，提供盘前过滤、价位锚、偏向判定、入场与风控的完整检查单与计算口径；不含投资建议，全部参数按原书口径标注品种与时区限制。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.ict-2022-mentorship
  cangjie.capability-count: 28
  cangjie.entrypoint-count: 1
---
# 开启ICT 2022导师计划的成功之门 / Unlocking Success in ICT 2022 Mentorship — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 不提供投资建议或收益承诺；原书方法论无统计回测支持
- 不覆盖加密货币等 24/7 品种的时段适配
- 不处理跨品种点数换算（原书仅 ES 标定）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 时间先于价格：先查时段窗口与禁忌日，再看任何形态
2. 价格只做两件事：重新平衡不平衡或寻求流动性（ERL/IRL 交替）
3. 结构必须带位移：无位移的突破不算 MSS，无位移本身是反向信号
4. 折价买入溢价卖出：不在旧高之上买、不在旧低之下卖
5. 不是每天都有交易：硬门不过即空仓

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 今天几点可以交易；现在是哪个时段；今天有FOMC/NFP能不能做；亚洲区间很宽还能做伦敦剧本吗 | references/capabilities/session-taboo-filter.md | references/capabilities/po3-amd-state-machine.md、references/capabilities/high-probability-entry-risk.md |
| 把今天关键价位列出来；亚洲区间多宽；CBDR中点在哪；盘前准备 | references/capabilities/daily-static-anchors.md | references/capabilities/daily-bias-checklist.md、references/capabilities/high-probability-entry-risk.md |
| 扫完这个低点下一目标是什么；这里是外部还是内部流动性；价格会先去哪个水平 | references/capabilities/liquidity-dol-state-machine.md | references/capabilities/daily-bias-checklist.md、references/capabilities/fvg-three-candle.md |
| 今天偏多还是偏空；我的多头想法还成立吗；价格在溢价还是折价；均衡区怎么办 | references/capabilities/daily-bias-checklist.md | references/capabilities/liquidity-dol-state-machine.md、references/capabilities/smt-divergence-confirm.md、references/capabilities/daily-static-anchors.md |
| 这次突破算结构转变吗；为什么这次突破是假的；有没有位移 | references/capabilities/mss-displacement-gate.md | references/capabilities/fvg-three-candle.md、references/capabilities/ict-2022-model.md |
| 这里有没有FVG；缺口区间在哪；这个FVG算好FVG吗 | references/capabilities/fvg-three-candle.md | references/capabilities/mss-displacement-gate.md、references/capabilities/liquidity-dol-state-machine.md |
| 这根蜡烛是OB还是Breaker；这个块还有效吗；MB和BB怎么分 | references/capabilities/pd-array-block-dictionary.md | references/capabilities/ote-entry-zone.md、references/capabilities/fvg-three-candle.md |
| 今天按清单能不能做；这单止损放几点；止盈怎么分批；9点没回撤还做吗 | references/capabilities/high-probability-entry-risk.md | references/capabilities/daily-bias-checklist.md、references/capabilities/session-taboo-filter.md、references/capabilities/ote-entry-zone.md |
| 纽约开盘能追吗；回撤到哪儿进；9点没回撤还做吗 | references/capabilities/ny-scalp-nine-step.md | references/capabilities/session-taboo-filter.md、references/capabilities/ote-entry-zone.md |
| 按2022模型现在第几步；扫完高点等什么信号；新闻日解禁后怎么找设置 | references/capabilities/ict-2022-model.md | references/capabilities/mss-displacement-gate.md、references/capabilities/fvg-three-candle.md、references/capabilities/ote-entry-zone.md |
| 回撤到哪儿挂单；0.705是什么；挂单区算一下 | references/capabilities/ote-entry-zone.md | references/capabilities/pd-array-block-dictionary.md、references/capabilities/high-probability-entry-risk.md |
| 刚扫了前低能反手吗；turtle soup怎么挂单；没有stop run只有假突破怎么办 | references/capabilities/turtle-soup-entry.md | references/capabilities/mss-displacement-gate.md、references/capabilities/liquidity-dol-state-machine.md |
| 现在是操纵还是真突破；Judas什么时候出现；周三还在跌要不要停手 | references/capabilities/po3-amd-state-machine.md | references/capabilities/session-taboo-filter.md、references/capabilities/mss-displacement-gate.md |
| ES和NQ背离了吗能进吗；SMT怎么用 | references/capabilities/smt-divergence-confirm.md | references/capabilities/daily-bias-checklist.md |
| 今天按什么顺序看盘；该看哪个时间框架；分析太多理不清 | references/capabilities/top-down-workflow.md | references/capabilities/daily-bias-checklist.md、references/capabilities/session-taboo-filter.md、references/capabilities/fvg-three-candle.md |
| 这次破的是哪一级结构；现在趋势的ITL/LTL在哪；破位后目标投射到哪儿 | references/capabilities/market-structure-hierarchy.md | references/capabilities/mss-displacement-gate.md、references/capabilities/daily-bias-checklist.md |
| 现在是buy program还是sell program；SMR确认了吗Type几；这轮分配terminus大概在哪 | references/capabilities/mmxm-state-machine.md | references/capabilities/mss-displacement-gate.md、references/capabilities/ict-2022-model.md、references/capabilities/pd-array-block-dictionary.md |
| 这是三驱吗第几驱了；三驱完了等什么入场；这次突破是三驱还是stop hunt | references/capabilities/three-drives-pattern.md | references/capabilities/mss-displacement-gate.md、references/capabilities/fvg-three-candle.md、references/capabilities/turtle-soup-entry.md |
| 这周区间怎么用；区间高低点该取哪个；亚洲走了趋势今天剧本变吗 | references/capabilities/monday-range-procedure.md | references/capabilities/session-taboo-filter.md、references/capabilities/daily-static-anchors.md |
| 未来几周算法参考哪些价位；20/40/60日范围怎么画；结构转变后多久有大波动 | references/capabilities/ipda-data-range-builder.md | references/capabilities/daily-bias-checklist.md、references/capabilities/top-down-workflow.md |
| 下午按哪个剧本做；午餐能追早盘吗；PM时段等什么信号；尾盘加速几点 | references/capabilities/afternoon-hours-playbook.md | references/capabilities/session-taboo-filter.md、references/capabilities/ny-scalp-nine-step.md |
| 今天像哪种剧本；开盘先涨了还追吗；消息砸下去又拉回来按哪个模板做 | references/capabilities/daily-templates-playbook.md | references/capabilities/session-taboo-filter.md、references/capabilities/high-probability-entry-risk.md |
| 这个季节对ES/欧元偏多偏空；DXY盘整对指数意味什么 | references/capabilities/dxy-seasonal-filter.md | references/capabilities/daily-bias-checklist.md、references/capabilities/smt-divergence-confirm.md |
| 今天开盘区间投影多少下方空间多大；错过开盘入场在哪补；dealing range成立了吗 | references/capabilities/opening-range-cpe.md | references/capabilities/daily-static-anchors.md、references/capabilities/po3-amd-state-machine.md |
| MSS后这个新方向成立了吗；order flow形成了吗激活了吗；OF区能直接进吗 | references/capabilities/order-flow-formation-gate.md | references/capabilities/mss-displacement-gate.md、references/capabilities/market-structure-hierarchy.md、references/capabilities/pd-array-block-dictionary.md |
| 这周NWOG在哪CE多少；缺口当支撑还是阻力；好几个缺口叠一起意味什么 | references/capabilities/nwog-ndog-anchors.md | references/capabilities/daily-static-anchors.md、references/capabilities/fvg-three-candle.md |
| 区间市扫完前高在哪空；breaker standalone怎么用；EQH被扫了能反手吗 | references/capabilities/institutional-perception-model.md | references/capabilities/pd-array-block-dictionary.md、references/capabilities/smt-divergence-confirm.md、references/capabilities/turtle-soup-entry.md |
| 1H关键高扫完低点后怎么接；ATM模式现在第几步；breaker回踩入场用哪个模型 | references/capabilities/ict-atm-method.md | references/capabilities/pd-array-block-dictionary.md、references/capabilities/ict-2022-model.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 缺关键输入（日历、K线、锚数据）时先询问，不猜值
- 禁忌日/硬门失败时输出不交易并停止下游能力
- 时段口径存疑（夏令时）时显式声明约定后再执行
