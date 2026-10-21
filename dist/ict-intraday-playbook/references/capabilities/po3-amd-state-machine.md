# PO3/AMD 节奏状态机（PO3 AMD State Machine）

## R — Reading (原文)

> "Consolidation cannot be followed by Retracement or Reversal. Consolidation is always followed by Expansion. After Expansion comes either Retracement or Reversal. The market does NOT do Consolidation -> Expansion -> Consolidation."（PDF p.227）
> 日线模板：Asian=积累；午夜后操纵/Judas；伦敦反转=扩张至 5am NY；5–8am 小盘整；8–8:30 回撤；NY=扩张或反转；伦敦收=反转；~16:00 收盘盘整（p.223–228，图 p.224 书 p.142 已核查 reviewed）。
> 确认 Manipulation 结束：MSS + 价格回到午夜开盘价之上/下（p.230）。新闻例外：8:30 有重大新闻则 9:30 无 Judas，改 10:00–10:10（p.260–262）。周线：周高低常于周一二形成；周三低点后继续下跌→当日停手（p.252–257）。

出处：Ch13 PDF p.215–265；图文证据 resources/figures/po3-p0224/（reviewed）。

## I — Interpretation (自述)

把一天/一周的行情读成三阶段剧本：积累（盘整造流动性）→操纵（Judas 假突破扫止损）→分配（真实扩张）。两条铁律约束剧本语法：盘整后只能接扩张；扩张后接回撤或反转。用时段模板可以"预期"当前阶段（亚洲=积累、伦敦=操纵转扩张……），但阶段切换的确认需要客观证据（MSS+回到 NMO 另一侧），否则只输出"预期阶段"。新闻日改写 Judas 的时间表。它回答"现在剧本走到哪一幕、下一幕预期什么、何时该停手"。

## A1 — Application Example

原书案例：PDF p.224（书 p.142）Reversal/Consolidation 段图，已实际看图核查：伦敦开盘扫止损后扩张"直到纽约 5 点"、05:00–08:00 EST 回到均衡盘整（0/50/100% 带）；与 p.223–228 文本逐段对应。原书未给盈亏结果。

## A2 — Future Trigger

情境：盘中问"现在是操纵还是真突破"；问"Judas 什么时候出现/今天怎么没有"；问"周三还在跌要不要继续做"。
语言信号：PO3 / power of three / AMD / accumulation manipulation distribution / Judas swing / 操纵 / 假突破时段 / 现在哪一阶段 / 周线节奏。
区分：管"阶段与剧本预期"；"突破是否有效"→ mss-displacement-gate；"几点能交易"→ session-taboo-filter。

## E — Execution

输入契约：当前时刻（纽约本地）、NMO（午夜开盘价）、亚洲区间、MSS 观察、新闻日历、星期。
1. 按星期+时刻给出预期阶段。日线阶段窗口表（纽约本地）：20:00–00:00=Accumulation（亚洲窗盘整）；00:00–05:00=Manipulation/Judas（午夜后至伦敦窗，日高/低常在此形成）；05:00–08:00=小 Consolidation；08:00–08:30=Retracement；08:30–10:00=Expansion 或 Reversal（NY 窗）；10:00–12:00=Reversal（伦敦收）；~16:00=收盘 Consolidation。周线：周一二常形成周高/低。注意：阶段窗口≠Killzone 会话窗，勿混用。
2. 确认检查：Manipulation→Expansion 需 MSS + 价格位于 NMO 正确侧；未确认→输出"预期阶段（未确认）"。
3. 新闻例外核对：8:30 重大新闻→9:30 不预期 Judas，改 10:00–10:10 窗。
4. 停手门：周三（周线剧本）低点后继续同向下跌→输出"当日停手"；安静时段不开新仓。
5. 输出：{预期阶段, 确认状态, 下一幕预期与时间窗, 停手标记}。
判停：无 NMO/亚洲数据→仅输出时段预期并标注缺输入。

## B — Boundary

- 阶段切换无客观实时信号：确认依赖 MSS+NMO 侧，属滞后证据；不输出"现在一定是操纵"的断言。
- 三阶段语法是作者公理（未证伪设计）；趋势日可能长时间停留扩张。
- 时区按纽约本地（nr-01）。
- 不用于回答价位与入场档。

## visual_evidence 关联

- figure_id: fig-po3-p0224（reviewed，见 resources/figures/po3-p0224/figure-notes.md）

## 补章并入（2026-10-21，Ch8/14/16/20/24 逐页细读）

- 8:30/NMO 溢价折价操作化（Ch8 p.101–107）：卖出日=价格在 8:30 Open 或 NMO 之上=溢价卖出机会；买入日镜像；Judas 窗 08:30–09:45 EST 朝 NMO 运动=Manipulation；看跌日下午可用 13:30 NY 开盘价替代 NMO。
- CPE（Ch14 p.279–282）：Accumulation 阶段同义操作区=开盘价上方/接近区（看跌日做空）；适用=错过初始入场或金字塔加仓。
- Distribution 时间窗（Ch14 p.280）：15:30–15:45 NY。
- 算法时间线增量（Ch20 p.468–472）：08:30–09:30=1h 窗，bearish sentiment 预期价格上涨找 short setups；09:30=manipulation；bearish 日 premium 运行两原因（取 BSL 建空/在 buy stops 上卖后以更便宜 SSL 回补）。
- 做市商循环注释（Ch24 p.503–507）：buy stops→sell stops→buy stops；Fair Value→Discount→Premium→Fair Value；Fair Value in Discount=MM buy、in Premium=MM sell。

## 图文证据

涉及图形、编号或图文对应时，先实际打开完整图与核查记录，再按需放大局部。当前宿主不能看图时说明限制；记录中的推断不能冒充图中事实。

- 图例 fig-po3-p0224 — 来源 src-ict2022，PDF 页序 224，书本页码 142；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/po3-p0224/page-0224.png) · [图文核查记录](../../resources/figures/po3-p0224/figure-notes.md)

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/figures/po3-p0224/page-0224.png](../../resources/figures/po3-p0224/page-0224.png)
- [resources/figures/po3-p0224/figure-notes.md](../../resources/figures/po3-p0224/figure-notes.md)
