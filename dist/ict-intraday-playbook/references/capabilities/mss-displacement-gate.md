# MSS/市场结构突破有效性判定（MSS Displacement Gate）

## R — Reading (原文)

> "MSS must be energetic and leave behind displacement to ensure that market is looking to reverse. Remember that structure means nothing without narrative."（PDF p.81）
> 无位移的多头信号：价格取低点但无大阴线且立即回到区间；无位移的空头信号：价格未能突破前高（p.143–144）。看涨 MSS：跌破旧低后迅速有力上移且蜡烛收盘确认；看跌镜像（p.80–83）。

出处：Ch4 PDF p.80–83；Ch10 p.143–144。

## I — Interpretation (自述)

结构突破本身不算信号，"带位移的结构突破"才算。判定器回答一个布尔问题：这次越位是不是机构赞助的？判据链：①越过了哪个前高/前低；②越位腿是否以有力收盘结束并留下 FVG（位移的可计算代理）；③是否结合了叙述（DOL、HTF 结构、静态流动性）——三者缺一即判无效。副产品同样重要：lack of displacement（扫了流动性却没有位移）本身被作者当作反向入场信号，因此输出是三态：有效 MSS / 无效 / 无位移反向信号。

## A1 — Application Example

原书案例：Ch4 p.81–82 的 bearish/bullish MSS 示意图（【图 PDF p.81–83，prepared-unreviewed】）：旧高上方反弹后迅速带位移下移= bearish MSS；旧低下方下跌后迅速带位移上移= bullish MSS。另 Ch10 p.143–144 给出"无位移"对照例。原书未给统计结果。

## A2 — Future Trigger

情境：价格刚破了前低/前高，问"这算结构转变吗"；问"为什么这次突破是假的"；为入场能力做确认门。
语言信号：MSS / market structure shift / BMS / 结构突破 / 结构转变 / displacement / 位移 / 这次突破有效吗 / 假突破。
区分：只判"突破是否有效"；"突破后去哪"→ liquidity-dol-state-machine；"在哪挂单"→ ote-entry-zone。

## E — Execution

输入契约：K线序列（至少含被越位的前高/低与越位腿 3 根以上）、被越位水平、（可选）HTF 叙述信息。
1. 确认越位对象：明确的前 STH/STL（或旧高/旧低）。无明确对象→判停输出"无可判定越位"。
2. 位移代理判定：越位腿是否以有力收盘越过该水平，且在该腿留下三蜡烛 FVG（调 fvg-three-candle 口径）。两者皆否→无效。
3. 叙述核对：越位方向与 DOL/HTF 结构是否自洽；不自洽→降级为"无效/警惕诱骗"。
4. 无位移分支：若流动性被扫但步骤 2 全否→输出"lack of displacement = 潜在反向信号"。
5. 输出：{有效/无效/无位移反向, 被越位水平, 位移证据K线, FVG 区间或 null, 叙述一致性}。

## B — Boundary

- Displacement 无量化阈值（nr-03）：本能力用"收盘越位+留下 FVG"作代理，主观力度判断不作硬门；阶段 4 需实测代理边界。
- 结构层级（STL/ITL/LTL）在试点外（nr-10），本能力不依赖层级即可运行。
- 作者警告：没有叙述的结构毫无意义——单看形态必被 fake out。
- 不用于回答方向幅度与目标位。

## 补章并入（2026-10-21，Ch15/19 逐页细读）

- BMS/MSB 分级（Ch15 p.322）：打破 ITL/ITH 级才算 significant break（BMS/MSB）；仅破 STL=minor。层级判定联读 market-structure-hierarchy 卡（输出中增加 broken_level 字段：STL/ITL/LTL）。
- SMR 增量（Ch19 p.437–445）：MSB 有效性=扩张腿内必须含 FVG，无 FVG 不视为有效 break；不需要收盘低于 swing low 即可确认（有 FVG 即可）；更高概率确认=收盘低于 swing low 且穿过最后一根 up-close candle 的开盘价（该蜡烛成为 bearish OB，其 open 被违反=change in state of delivery）。
- 持仓验证（Ch15 p.326）：看跌时 up-close 蜡烛应持续压制、看涨时 down-close 蜡烛应支撑；被收盘违反→结构存疑标注。
