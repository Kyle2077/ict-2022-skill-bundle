# 下午与跨时段剧本（Afternoon & Hours-of-Operation Playbook）

## R — Reading (原文)

> 下午三策略：延续 / 反转 / Measured Move（上午幅度 1:1 复制，例 NQ 70 点）；13:30 NY 后关注 Swing Highs/Lows；加速时点约 15:40 与 15:50（market-on-close 订单）（Ch8 p.107–111）。
> Hours of Operation：PM Session 13:30–16:00（RTH，识别 HH/LL；看涨时 PM 最低低点下方 SSL 被扫=有利信号）；Opening Range=9:30 EST 后 30 分钟；London Session Raid 02:00–05:00（开盘 30 分钟未接近 PM range 则转向）；NY Lunch Raid 12:00–13:30（非趋势日反弹早盘高点/趋势日延续至 15:00–16:00）；AM Session 09:30–12:00（午后回顾参照）；看涨日午后模式=早盘涨→12–13 盘整→14–16 重复早盘（更短 TF）（Ch28 p.537–546）。
> 警告：午餐时段非趋势日"通常会完全逆转早盘走势"，不宜追早盘趋势（p.543）。

出处：Ch8 PDF p.107–111；Ch28 p.537–546。

## I — Interpretation (自述)

把 9:30 之后的全天切成可查剧本：AM（09:30–12:00）造参照、Lunch（12:00–13:30）非趋势日反转/趋势日延续、PM（13:30–16:00）识别 HH/LL 并用"PM 低点下方 SSL 被扫"作为看涨有利信号、尾盘 15:40/15:50 加速。下午入场三选一：延续、反转、Measured Move（上午幅度等量复制）。价值在于纠正最常见错误——午餐追早盘趋势，以及给"下午还能不能做、按哪个剧本"一个查表答案。

## A1 — Application Example

原书案例：Ch8 p.109–111 下午模板图与 Ch28 p.538–546 各时段标注图（【图 prepared-unreviewed】）。Measured Move 原文用 possibility 表述，非保证。

## A2 — Future Trigger

情境：午盘问"下午按哪个剧本做"；问"午餐时段能追早盘吗"；问"PM 时段等什么信号"；问"尾盘加速几点"。
语言信号：下午 / afternoon / PM session / lunch / 午餐 / measured move / 13:30 / 15:40 / opening range / 午后。
区分：管 9:30 后时段剧本；上午 Killzone→ session-taboo-filter；NY 早盘九步→ ny-scalp-nine-step。

## E — Execution

输入契约：当前纽约本地时刻、当日 AM 走势摘要（高/低/方向）、趋势日判定（可缺→按非趋势日保守处理）。
1. 定位时段：AM/Lunch/PM/加速窗（15:40/15:50）。
2. 时段行为输出：AM=造参照；Lunch=非趋势日反转预警/趋势日延续；PM=HH/LL 识别 + 看涨时 PM 低点下 SSL 被扫=有利；加速窗=波动预期。
3. 下午策略选择：延续/反转/Measured Move（Measured Move=上午幅度数值复制，标注 possibility）。
4. Opening Range（9:30 后 30 分钟）作为 PM 评估参照；London Raid 条件（开盘 30 分钟未接近 PM range）。
5. 输出：{时段, 剧本, 关键信号, measured move 数值或 null, 禁止事项}。
判停：趋势日判定缺→按非趋势日输出并标注保守口径。

## B — Boundary

- 时区按纽约本地（nr-01）；Measured Move 仅示例 NQ，跨品种无换算。
- 午餐反转是"通常"而非必然；趋势日例外。
- 不用于上午 Killzone 决策。
- 图依赖未全核（nr-11）。
