# PD Array/Block 类型识别词典（PD Array & Block Dictionary）

## R — Reading (原文)

> OB：脉冲前最后一根反向蜡烛；上涨前最后下跌收盘蜡烛=bullish OB（p.584）。有效性：最低下跌收盘蜡烛的高点被更近蜡烛穿过时生效；理想 OB 价格不破实体中点（Mean Threshold 50%，p.577）。
> Breaker：被强脉冲穿透而无回拉的 OB；bullish 要素序列 Low–High–Lower Low–Higher High（p.547、p.555，图已核查 reviewed）。
> Mitigation：failure swing 结果，未创新高/低+结构突破；与 Breaker 区别=失败摆动 vs 成功摆动（p.592、p.600）。
> Rejection：新高/低处长影线扫流动性后反转，取该 Swing 最高收盘/开盘价（p.602）。Propulsion：在 OB 内交易的蜡烛，极敏感不超 50%（p.607–609）。Vacuum：事件造成的缺口（p.611）。

出处：Ch29 PDF p.547–616；Ch9 p.131–134；图文证据 resources/figures/breaker-p0555/（reviewed）。

## I — Interpretation (自述)

把"入场该挂在哪种块上"变成分类器：七类 Block 各有结构指纹——OB 看脉冲前最后一根反向蜡烛；Breaker 看四要素序列（低-高-更低低-更高高）；Mitigation 看失败摆动；Rejection 看长影线扫掠；Propulsion 看是否嵌在 OB 内；Vacuum 看事件缺口。每类附有效性条件（OB 四条件、50% 中点阈值、Breaker 双层流动性加分）与用途（入场/目标/失效）。识别输出带置信标注：结构序列可判定的给高置信，依赖"强脉冲/长影线"主观量度的给中低置信。

## A1 — Application Example

原书案例：PDF p.555（书 p.451）bullish breaker 双图（折线+K线），已实际看图核查：四要素 Low–High–Lower Low–Higher High 标注与橙色 breaker 区一致；正文明示 breaker 也可预示延续而非仅反转。原书未给盈亏结果。

## A2 — Future Trigger

情境：问"这根蜡烛是 OB 还是 Breaker"；问"这个块还有效吗"；为入场能力选挂单位置；问"MB 和 BB 怎么分"。
语言信号：order block / OB / breaker / mitigation / rejection / propulsion / vacuum / PD array / 订单块 / 突破块 / 块有效性 / mean threshold。
区分：只做识别与有效性；"在块的哪一档挂单"→ ote-entry-zone；"块被扫后去哪"→ liquidity-dol-state-machine。

## E — Execution

输入契约：K线序列 + 待分类对象（或全序列扫描请求）。
1. 按七类指纹逐一匹配（OB→BB→MB→RB→PB→VB 顺序，互斥时按定义优先级：先判是否 failure swing 决定 MB/BB）。
2. 有效性核验：OB 四条件与 50% 中点；BB 需先有流动性被扫（旧低/旧高被违反）；PB 超 50% 即失效标记。
3. 置信标注：序列可判定=high；依赖强脉冲/长影线主观量度=medium；跨多蜡烛组合=low。
4. 输出：{类型, 区间, 方向, 有效性, 置信, 依据K线索引}。
判停：对象不匹配任何指纹→输出"非 PD Array 候选"，不硬分类。

## B — Boundary

- "强脉冲""长影线"无量化阈值（nr-03）：不补阈值，用置信标注诚实表达。
- RB/PB/ROB 定义嵌套且主观，默认低置信子类；ROB 在试点内定义模糊，仅作术语不用于判定。
- 作者盲点：块有效性叙事（机构订单残留）未被证明。
- 不输出"哪个块最好"的排序结论（原书未给显式优先级表，仅隐含使用频率）。

## 补章并入（2026-10-21，Ch15/16/21/24 逐页细读）

- OB 入场两问（Ch15 p.329）前置检查：①价格想达到更高吗？②市场结构支持你的 OB 吗？高概率 OB 两条件：伴随 FVG + 与时间理论融合（输出增加 quality 标记）。
- POI 七类清单与选择规则（Ch16 p.359–363）：EQL/EQH、Liquidity Levels、FVG、OB、BB、MB、RB；无强弱之分；多 POI 重叠按 R/R 选+等 LTF 确认；TF 配对 15m-5m/1h-15m/4h-1h/1D-4h。
- Dealing Range 形成（Ch16 p.276–277）：开盘区间两侧均被 take=dealing range 成立（折溢价划分前提）。
- P/D 四细分（Ch16 p.364–377）：premium within premium / discount within premium / premium within discount / discount within discount。
- Dealing Range 高低点四步（Ch16）：Fib 最高到最低→算法盘整区对齐→50% 与盘整对齐取最近高→回调作低。
- 公允价值三要素（Ch24 p.497–498）：宏观范围→Equilibrium 相对位置→做市商参考点（FVG/Void/OB）；Equilibrium 处方向歧义处理=看最近 MSS 方向+范围内位置。
- Bearish Breaker 精确口径（Ch21 p.477–478）：扫 BSL 的最后一根 down-close 蜡烛；独立入场模型见 institutional-perception-model 卡。

## 图文证据

涉及图形、编号或图文对应时，先实际打开完整图与核查记录，再按需放大局部。当前宿主不能看图时说明限制；记录中的推断不能冒充图中事实。

- 图例 fig-breaker-p0555 — 来源 src-ict2022，PDF 页序 555，书本页码 451；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/breaker-p0555/page-0555.png) · [图文核查记录](../../resources/figures/breaker-p0555/figure-notes.md)

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/figures/breaker-p0555/page-0555.png](../../resources/figures/breaker-p0555/page-0555.png)
- [resources/figures/breaker-p0555/figure-notes.md](../../resources/figures/breaker-p0555/figure-notes.md)
