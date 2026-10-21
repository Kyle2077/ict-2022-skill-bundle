# 日线偏向判定检查清单（Daily Bias Checklist）

## R — Reading (原文)

> "Are we at Premium zone? … we anticipate price will go down. Are we at Discount zone? … we anticipate higher prices."（PDF p.183–184）
> 偏向不是盘前预设偏见，基于规则与经验动态确定；确定后不要反复翻转（p.204–206）。PDH/PDL 是每日流动性池：触及未破且无位移=潜在反转参考（p.183–185）。Dealing range = 双边流动性都被扫过的区间，上半=溢价、下半=折价、中点=均衡（最难预测）（p.128–132）。

出处：Ch12 PDF p.181–210；Ch9 p.128–132；Ch32 p.628–631。

## I — Interpretation (自述)

把"今天偏多还是偏空"从感觉变成一条可复核的依据链：先看价格在 HTF dealing range 的哪一半（溢价→预期向下、折价→预期向上、均衡→观望倾向），再确认下一个 DOL 在哪侧（用 liquidity-dol-state-machine），再用 PDH/PDL 的触及反应做日内修正，最后可选地用 SMT 背离在预定水平上做确认。输出必须带依据链而非单一结论；且一旦给出偏向，在 DOL 到达或出现明确反向证据前不翻转——这条纪律本身是能力的一部分。

## A1 — Application Example

原书案例：Ch12 p.202–203 的 ES 小时图月度图例，作者标出按"小时图结构突破 + 前摆动点一半止损 + 2:1 盈亏比 + 1:1 移保本"规则的一组交易并称结果为 6 胜 1 负；作者明示这是示例、要求读者自行验证（非系统回测）。该例演示偏向与结构配合的用法，不演示本清单全流程。

## A2 — Future Trigger

情境：盘前问"今天偏多还是偏空"；盘中问"我的多头想法还成立吗"；问"价格在溢价还是折价"；问"均衡区该怎么办"。
语言信号：daily bias / 日线偏向 / 今天方向 / 偏多偏空 / premium discount / 溢价折价 / equilibrium / 均衡 / 我的看法对不对。
区分：只回答方向与依据；"几点能交易"→ session-taboo-filter；"入场挂哪"→ ote-entry-zone / high-probability-entry-risk；"下一目标价位"→ liquidity-dol-state-machine。

## E — Execution

输入契约：HTF（日/4H）dealing range 高低、当前价、PDH/PDL、已标注 DOL 候选、（可选）SMT 配对数据。缺 HTF 区间先询问。
1. 定位折溢价：当前价 vs dealing range 中点；输出 溢价/折价/均衡。均衡→直接输出"最难预测，观望倾向"并判停。
2. 取下一 DOL（调 liquidity-dol-state-machine 口径）：与折溢价预期同向→偏向确立；反向→输出冲突并列出两方证据，不强行二选一。
3. PDH/PDL 修正：触及未破且无位移→偏向该侧反转参考；带位移穿透→偏向穿透方向。
4. （可选）SMT 确认：仅在已有想法+预定水平附近使用（调 smt-divergence-confirm）。
5. 输出：{偏向, 依据链[1..4], 失效条件（DOL 到达/反向位移证据）, 置信标注}。
判停：步骤 2 冲突且步骤 3 无位移证据→输出"无偏向/观望"。

## B — Boundary

- 不预设：盘前无证据时输出观望，不硬给方向（作者明示）。
- "禁止反复翻转"缺客观判据（nr-03 类）：能力以"失效条件触发才允许改"为约定。
- SMT 只确认不入场；背离单独出现不构成偏向。
- 作者盲点进边界：整套偏向逻辑建立在 IPDA/做市商叙事上，无统计验证；事件驱动日可能整体失效（配合禁忌日过滤）。

## 补章并入（2026-10-21，Ch14/16/27 逐页细读）

- Bias 三问（Ch14 p.273–276）并入步骤 2 后：①市场是否提取了重要流动性池？②是否触及重大 FVG？③是否产生带 Displacement 的 MSB？
- 七步系统法（Ch16 p.332–354）作为完整模式并入：外部市场 P/D→Impulse 结构→结构绘图→流动性定位→P/D 评估→顺流入场→无位移穿结构则预期反转。
- Bias 第二三问（Ch16 p.349）：What was taken? Where can this lead? What hasn't been taken?
- 心态执行规则（Ch14 p.278–279）：看跌日每根上涨蜡烛=卖出机会（等 POI/开盘价上方/LTF 取 BSL），目标日线旧低/前日低；看涨日镜像。
- PDH/PDL fade 两场景（Ch27 p.531）：扩张回撤中 PDL 被扫→反弹做多；反向扩张回撤中 PDH 被扫→回落做空；纪律：必须 PD Array 汇合+HTF IOF 确认，无汇合不交易（并入步骤 3）。
- 警告并入 B：犹豫蜡烛单独无意义（Ch16）；单向 bias 执行纪律（Ch16 p.354）；避免抄底摸顶（Ch14 p.276）。
