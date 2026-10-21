# Monday Range 与区间界定流程（Monday Range Procedure）

## R — Reading (原文)

> 区间高低点四种确定法：①导致对面横扫的高/低点；②同侧横扫前的高/低点；③Equal Highs/Lows；④前日/周/月高低（影线或实体，以 midrange 对齐为准）（p.482–483）。
> Monday Range 流程：周一仅观察→收盘后标记高低→等一侧被扫且价格回区间内→MSS 后入场→目标对面；HTF OF 不明时 midrange(50%) 止盈使交易无风险；放弃条件=仅一侧被扫变支撑阻力/价格远离不回（p.485–487）。
> Daily Range 双叙事：亚洲盘整≤10–15pt(ES)→伦敦扫亚洲 BSL/SSL(Judas)→扩张对面→LOKZ 内定高低反转→NY 回撤；亚洲趋势>15pt→避开 LOKZ 等 NYKZ 趋势突破后做反转/回撤至伦敦 BSL/SSL（p.488–491）。Session 链式 bias：Asia→London→NY。

出处：Ch22 PDF p.482–491。

## I — Interpretation (自述)

周初的区间交易剧本：周一不交易，只造区间；周二起等"一侧止损被扫+价格收回区间"这一事件，事件后用 MSS 确认入场，目标区间对面，方向不明就 50% 止盈转无风险。配套两个通用工具：区间边界的四种确定法（避免拿错高低点），与亚洲幅度阈值分流的双叙事（决定伦敦窗是反转剧本还是跟随剧本）。它把"周初怎么处理"从自由发挥变成带放弃条件的流程。

## A1 — Application Example

原书案例：Ch22 p.487 Monday Range 实例图（低被扫→equal lows→MSS→反弹至区间高；【图 prepared-unreviewed】）。原书未给结果统计。

## A2 — Future Trigger

情境：周一/周二问"这周区间怎么用"；问"区间高低点该取哪个"；问"亚洲走了趋势今天剧本变吗"。
语言信号：monday range / 周一区间 / 区间交易 / range trading / 区间高低点怎么定 / 亚洲趋势还是盘整 / session bias。
区分：管周初区间剧本与区间界定；时段可否→ session-taboo-filter；静态锚→ daily-static-anchors。

## E — Execution

输入契约：星期、周一 OHLC（或当周已形成区间）、亚洲区间点数(ES)、HTF order flow 方向（可缺）。
1. 区间界定：按四法选边界（优先①引发对面横扫的极值；④取影线或实体以 midrange 对齐为准），输出区间与 midrange。
2. 周一门：周一不交易；未收盘不标记。
3. 事件门：等一侧被扫且价格收回区间内；仅被扫不收回/远离不回→放弃或换品种。
4. 入场：收回后 MSS 确认→入场，目标对面；HTF OF 不明→midrange 止盈转无风险。
5. 双叙事分流：Asian ≤10–15pt→伦敦反转剧本；>15pt→避开 LOKZ、等 NYKZ 突破后反转/回撤剧本；输出当日叙事与链式 bias（Asia→London→NY）。
6. 输出：{区间, midrange, 事件状态, 入场/放弃, 目标, 当日叙事}。
判停：步骤 3 未发生→输出"等待"不入场。

## B — Boundary

- "有些周只有一侧被扫"→该周剧本失效，作者明示远离。
- 点数阈值仅 ES；时区按纽约本地（nr-01）。
- 区间四法中法①"tricky to spot"，误用第一个高点会错位 midrange。
- 不用于无周一区间的品种/假期周（原文未给假期周规则→标缺口）。
