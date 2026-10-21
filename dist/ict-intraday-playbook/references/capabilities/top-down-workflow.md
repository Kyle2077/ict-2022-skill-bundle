# Top Down 分析与 15m→5m 执行工作流（Top-Down Workflow）

## R — Reading (原文)

> "Large institutions and banks analyze charts on Day => Week => Month TFs. We determine price levels that correspond to the Institutional Order Flow. HTFs form slowly and allow enough time for planning."（PDF p.22–23 意旨，≤150字）
> 15m→5m：15m 识别关键高低/不平衡/FVG/OB 与 Killzone 预期猎取→切换 5m 精确入场；8:30–12:00 执行、11:00 前建仓目标（p.88–94）。层级：Long=周/日，Intermediate=4H/1H，Short=15m/5m（p.121）。"Daily FVG → 1h structure → 15m entries，不要过度降帧"（p.642–643）。

出处：Ch2 p.22–27；Ch6 p.88–94；Ch9 p.121；Ch32 p.627、p.642–643。

## I — Interpretation (自述)

每日操作的顺序协议：先在慢帧定大局（月/周/日的偏向、主要流动性池与 PD Array），再到中帧（4H/1H）划 dealing range 折溢价，然后 15m 标注当日关键高低/不平衡与 Killzone 预期猎取位，最后只在 5m 做精确入场；并规定执行时段与"11:00 前建仓"的目标时间。它的价值是防两种常见故障：分析瘫痪（信息堆太多）与帧错配（在 1m 上找 HTF 意义）。能力输出是一张带顺序与完成标准的盘前-盘中检查单。

## A1 — Application Example

原书未提供完整盘前演练记录；明确标记的合成演练：盘前 8:20，日线折价+DOL=上方旧 FVG→4H dealing range 中点以下→15m 标出亚洲高低与两个未回补 FVG、伦敦窗预期猎取亚洲高点→8:35 切 5m，等待价格进入 15m FVG 且出现 MSS 后入场，10:40 建仓完成。全流程各步完成标准均引用原书页（p.88–94/p.121）。

## A2 — Future Trigger

情境：盘前问"今天按什么顺序看盘"；问"该看哪个时间框架"；问"分析太多理不清"。
语言信号：top down / 多时间框架 / 看盘顺序 / 盘前流程 / 15m 5m / 时间框架 / timeframe / 工作流 / routine。
区分：管"顺序与帧"；每帧内的具体判定调对应能力（偏向/流动性/FVG/入场）。

## E — Execution

输入契约：品种、日期、可用数据帧集合。
1. 月/周/日：输出偏向参考、主要流动性池与 PD Array 清单（调 daily-bias-checklist 口径）。
2. 4H/1H：dealing range 与折溢价划分。
3. 15m：关键高低、未回补 FVG/OB、Killzone 预期猎取位（调 session-taboo-filter 窗口）。
4. 执行窗（8:30–12:00 纽约本地）：切 5m；入场须有 15m 级依据，禁止降到 1m 找理由。
5. 输出：{各帧结论, 5m 触发条件, 建仓目标时间, 禁止事项}。
判停：HTF 数据缺失→从可用最高帧开始并显式降级标注。

## B — Boundary

- 不产出方向或价位结论本身（由被调能力产出）。
- 执行时段为原书 ES 日内口径； swing/持仓交易者不适用 11:00 建仓目标。
- 作者警告内建：避免过度复杂化（cx-22）与过度降帧。
- 时区按纽约本地（nr-01）。

## 补章并入（2026-10-21，Ch14/15 逐页细读）

- TDA 六步（Ch14 p.284–292）替换原步骤 1–4 表述：4H 主趋势→4H SSL/BSL→1H order flow 整合区→15M SSL/BSL+SMT+FVG 汇合→5M 入场时机→1M 微调止损止盈。终止规则：在 Displacement 内开始 TDA；5M 找到 FVG 即停；2M 找到即停；1M 无 FVG=无交易。
- 三 TF 角色（Ch15 p.303–304,315）：HTF=理念/偏向/管理；Mid=结构细化/管理；LTF=入场计时/早期反转信号。日线优先原则："the daily chart is exactly what institutions and banks are using"；逆日线=asking for failure。交易者类型→TF 组合表原文仅在图中（p.315–316 未核）→标缺口不编。
