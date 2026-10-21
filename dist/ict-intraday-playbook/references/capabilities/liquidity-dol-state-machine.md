# 流动性分类与 DOL 识别（Liquidity & Draw-on-Liquidity）

## R — Reading (原文)

> "Price only does two things: it goes to old highs and old lows or seeks to reprice into imbalances. When external range liquidity is taken, a FVG becomes the next draw on liquidity. And when a FVG is stacked, an old low or an old high becomes the next draw."（PDF p.57–59 意旨，引用≤150字）
> 七类流动性：Major（日/周/月/季/年高低止损）、Medium（15m/1h）、Minor（1–5m）、Equal Highs/Lows、Swing Points、Range 高低外、Trendline 背后（p.44）。
> 警告：不在破旧高时买、破旧低时卖（p.51）；弹跳越多的支撑/阻力越容易被扫（p.52）。

出处：Ch3 PDF p.39–79；Ch9 p.127–128；Ch12 p.184–185、p.200。

## I — Interpretation (自述)

把"价格为什么往那里走"翻译成状态机：市场只有两类磁吸目标——外部流动性（旧高/旧低上方的止损簇，ERL）与内部流动性（FVG/OB 等不平衡，IRL），两者交替：扫完 ERL 下一个目标就是 IRL，回补完 IRL 下一个目标又回到 ERL。DOL（Draw on Liquidity）就是"下一个磁吸目标"的统称。使用时先按七类把图上所有流动性标出来，再按交替规则与 HTF order flow 判断当前状态与下一目标。它不预测幅度，只回答"下一站是哪类、在哪个方向"。

## A1 — Application Example

原书案例：Ch3 p.57–59 的 ERL/IRL 交替图例（【图 PDF p.57–59，prepared-unreviewed】）：月/周/日/4H 上标出旧高低与 FVG，演示扫旧低后价格转向未回补 FVG、回补后再转向对面旧高的循环；作者以此说明"在月/周/日/4H 用此循环定日线偏向"。原书未给盈亏结果。

## A2 — Future Trigger

情境：图上标了一堆水平线但不知道价格先去哪个；问"扫完这个低点下一目标是什么"；问"这里是外部还是内部流动性"；为偏向判定与入场选目标。
语言信号：流动性 / liquidity / BSL SSL / 止损簇 / DOL / draw on liquidity / 磁吸 / 下一目标 / ERL IRL / 扫完去哪。
区分：本能力管"目标分类与下一站"；"今天方向"→ daily-bias-checklist；"入场位"→ pd-array-block-dictionary / ote-entry-zone。

## E — Execution

输入契约：已标注图表或 OHLC 序列 + 时间框架集合（月/周/日/4H 至少其一）；缺失标注先询问。
1. 按七类枚举标注全部流动性位置（含 EQH/EQL、Range 外、趋势线后）。
2. 判定当前状态：最近一次位移吸收的是 ERL 还是 IRL（看位移起点扫了什么）。
3. 按交替规则输出下一 DOL 类型与方向：ERL 已吸收→下一站 IRL（列出未回补 FVG/OB 候选）；IRL 已回补→下一站 ERL（列出旧高/旧低候选）。
4. 结合 HTF order flow（缩小画面看位移前走向）修正方向；Displacement 自 FVG 向上→目标外部 BSL；向下/不尊重 FVG→目标外部 SSL。
5. 输出：{当前状态, 下一 DOL(类型+价位区间+方向), 依据K线}。
判停：图上无未回补不平衡且无可见旧高低→输出"无明确 DOL"，不猜。

## B — Boundary

- LRLR/HRLR 只做定性标注（nr-02），不输出评分。
- 作者警告内建为检查项：不在破旧高买/破旧低卖；多弹跳水平优先视为将被扫的对象而非支撑。
- "价格只做两件事"是作者公理（未证明），本能力只在其框架内工作；基本面驱动的单边行情可能长期不遵守交替。
- 不输出幅度与时间预测。
