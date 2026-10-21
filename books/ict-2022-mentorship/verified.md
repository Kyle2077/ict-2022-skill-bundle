# verified.md — 阶段 1.5 三重验证通过的能力单元（ICT 2022 Mentorship）

> validation_version: task-first-v2。候选合并自 candidates/{framework,principle,case,counter-example,glossary}.md；出处均为 PDF 页序（source_id: src-ict2022）。
> V2 的 check_mode 全部为 walkthrough（纸面演练）；阶段 4 须另行实测，未做不得声称"已实测"。

## cap-01 交易时段与禁忌日过滤（Killzone Session & Taboo-Day Filter）

```yaml
id: cap-01
title: 交易时段与禁忌日过滤
type: procedure / time-filter
merged_from: [fw-07, pr-01, pr-21, pr-31, pr-40, pr-41, cx-02, cx-03, cx-21, cx-24]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.156（五 Killzone 时间窗）, p.157–166（Asia）, p.167–170（London+回避条件）, p.171–177（NY）, p.178–180（London Close）, p.82–83, p.196
V1_source_sufficiency:
  passed: true
  reason: 五个时间窗、各时段行为模板、亚洲区间阈值(>15–20pt ES 等纽约)、回避条件（利率公告/演讲/假日/全球事件/周目标达成）均单处或多处完整给出
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 日期=周二、当前纽约本地时间 03:10、经济日历无事件、Asian range=12pt(ES)
  expected: 处于 London Open KZ；无回避条件；Asian<15pt → 可执行 London 流程
  observed: 与 p.156/p.167/p.170 规则一致
V3_task_utility:
  passed: true
  expected_benefit: 纯时间计算零主观；直接避免"错时段/禁忌日交易"这一全书首要警告
decision: verified
boundary_notes: 时区口径见 needs-review nr-01（NY 本地时间解释）；回避清单为枚举式，日历输入需外部提供
```

## cap-02 每日静态价位锚计算（Daily Static Anchors）

```yaml
id: cap-02
title: 每日静态价位锚计算（PDH/PDL、NMO/NYO、Asian Range、CBDR 标记）
type: calculation
merged_from: [pr-11, pr-12, pr-16, fw-02 部分, cx-13]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.152–153（MNO/NYO 定价参考）, p.156（CBDR 14:00–20:00）, p.157–166（Asian range 画法=20:00–00:00 最高最低）, p.183–185（PDH/PDL 流动性池）, p.630（CBDR<20pt、Asian 10–15pt 过滤）
V1_source_sufficiency:
  passed: true
  reason: 每个锚的定义、取数窗口、画法均有明确原文；CBDR 偏差投影(±STD)在 Ch31，属试点外，见 coverage-audit
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 某日 1m/15m 数据 + 前日 OHLC
  expected: 输出 PDH/PDL、NY 00:00 开盘价、NY 09:30 开盘价、Asian(20:00–00:00 NY)高/低与幅度、CBDR(14:00–20:00 NY, 1h 蜡烛体)高/低与中点
  observed: 全部为确定性取数，可程序化
V3_task_utility:
  passed: true
  expected_benefit: 盘前即得坐标系；统一各能力共用的锚口径
decision: verified
boundary_notes: CBDR 标记"仅蜡烛体"（p.622 在试点外章节，时间窗在 p.156 试点内）；±STD 投影 deferred
```

## cap-03 流动性分类与 DOL 识别（Liquidity & Draw-on-Liquidity）

```yaml
id: cap-03
title: 流动性七分类 + ERL/IRL 交替 + DOL 识别
type: procedure / state-machine
merged_from: [fw-01, fw-06, pr-08, pr-23, pr-24, pr-32, cx-01, cx-15]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.41–52（七类流动性+陷阱警告）, p.54–59（DOL+ERL/IRL 循环）, p.60–74, p.127–128, p.184–185, p.200
V1_source_sufficiency:
  passed: true
  reason: 七类流动性枚举、ERL↔IRL 转换规则、DOL 候选清单均完整；"价格只做两件事"为作者公理（进 B）
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 已标注图表：昨日高低、亚洲区间高低、一个未回补 FVG；观察到亚洲低点刚被扫
  expected: ERL 被吸收 → 下一 DOL 转为 IRL（该 FVG）；方向结合 HTF order flow
  observed: 与 p.57–59 循环规则一致
V3_task_utility:
  passed: true
  expected_benefit: 把"价格要去哪"从直觉变为状态机；统一 DOL 口径
decision: verified
boundary_notes: LRLR/HRLR 无量化度量 → needs-review nr-02，能力内只做定性标注不做评分；"不在旧高买/旧低下卖"与"弹跳多的水平更易被扫"作为 B 内检查项
```

## cap-04 日线偏向判定（Daily Bias Checklist）

```yaml
id: cap-04
title: Daily Bias 判定检查清单
type: decision-framework / checklist
merged_from: [fw-02, fw-20, pr-42, cx-20]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.128–132（Dealing Range 溢折价）, p.183–185（偏向框架+PDH/PDL）, p.204–206（不预设+不反复翻转）, p.628–631
V1_source_sufficiency:
  passed: true
  reason: 判定步骤（溢折价位置→DOL→PDH/PDL 反应→SMT 辅助→结构）完整成链
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 价格处 HTF dealing range 折价区；DOL=上方溢价 FVG；PDH 触及未破无位移
  expected: 输出看涨偏向 + 依据链；均衡区则输出"最难预测/观望倾向"
  observed: 与 p.183–184 规则一致
V3_task_utility:
  passed: true
  expected_benefit: 把主观偏向变为可复核的依据链；禁止翻转规则减少盘中反复
decision: verified
boundary_notes: "禁止反复翻转"缺客观判据（nr-03 类主观项）；SMT 仅作确认（cap-14）
```

## cap-05 MSS/结构突破判定（含 Displacement 代理判据）

```yaml
id: cap-05
title: MSS/市场结构突破有效性判定
type: procedure / boolean-decision
merged_from: [fw-03, pr-04, cx-06]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.80–83, p.143–144（无位移=反向信号）, p.301–331 在试点外（结构层级 deferred）
V1_source_sufficiency:
  passed: true
  reason: 看涨/看跌 MSS 条件、无效情形、"structure means nothing without narrative"验证要求均完整
V2_executability:
  passed: true
  check_mode: walkthrough
  input: K线序列：跌破前 STL 后出现收盘有力下移并留下 FVG；对照组：仅影线刺破无 FVG
  expected: 前者=有效 MSS；后者=无效（且 lack of displacement 记为潜在反向信号）
  observed: 与 p.81/p.144 一致；Displacement 的"energetic"以"收盘越位+留下 FVG"为可计算代理（nr-03）
V3_task_utility:
  passed: true
  expected_benefit: 入场确认的布尔门；统一"什么才算结构突破"
decision: verified
boundary_notes: 主观力度无阈值 → 用 FVG 存在+收盘越位代理，阶段 4 实测该代理的边界
```

## cap-06 FVG 三蜡烛判定

```yaml
id: cap-06
title: FVG（Fair Value Gap）三蜡烛判定与 Displacement 关联
type: procedure / pattern-recognition
merged_from: [fw-04, pr-05, cx-07]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.139–154（图 p.140–141/147/149–151；书 p.119 已核图）
V1_source_sufficiency:
  passed: true
  reason: bearish/bullish FVG 的三蜡烛边界定义、最佳形态条件（流动性被扫后）、非 FVG 情形（前K高点抵消第三K低点）均完整；图已实际核对
V2_executability:
  passed: true
  check_mode: walkthrough
  input: c1(L=100), c2 大阴线, c3(H=98)
  expected: bearish FVG 区间 [98,100]；若 c3 高点≥c1 低点则平衡非 FVG
  observed: 与 p.140–141/147 定义一致
V3_task_utility:
  passed: true
  expected_benefit: 全书最核心的入场/目标工具；OHLC 即可程序化
decision: verified
boundary_notes: FVG 最小宽度未定义（nr 已记）→ 能力输出原始区间不做宽度过滤；visual_evidence 登记 p.147
```

## cap-07 PD Array/Block 类型识别词典

```yaml
id: cap-07
title: PD Array/Block 类型识别（OB/BB/MB/RB/PB/VB）+ 有效性条件
type: classification / decision-framework
merged_from: [fw-17, pr-17, pr-25, pr-26, pr-27, pr-38, pr-39, cx-17, cx-18]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.547–616（书 p.451 已核图）, p.131–134（PD Array 清单）
V1_source_sufficiency:
  passed: true
  reason: 每类 Block 的定义、要素序列（BB: L-H-LL-HH / MB: failure swing）、有效性条件（OB 四条件、Mean Threshold 50%、PB 敏感性）均完整
V2_executability:
  passed: true
  check_mode: walkthrough
  input: K线序列含脉冲前最后反向蜡烛 + 后续穿透无回拉
  expected: 分类为 Breaker（成功摆动）而非 Mitigation（失败摆动）；OB 有效性按四条件与 50% 中点核验
  observed: 与 p.577/p.600 判别规则一致
V3_task_utility:
  passed: true
  expected_benefit: 统一入场位(PD Array)的识别口径；区分易混淆的 BB/MB
decision: verified
boundary_notes: "强脉冲/长影线"无量化阈值 → 识别输出置信标注，主观项进 B；RB/PB 定义为低置信子类
```

## cap-08 Ch32 高概率入场检查清单 + 止损止盈参数

```yaml
id: cap-08
title: 高概率日内入场检查清单 + 参数化止损/止盈（买入日/卖出日）
type: procedure / checklist / risk-management
merged_from: [fw-11, pr-09, pr-10, pr-11, pr-12, pr-13, pr-18, pr-36, pr-37, cx-04, cx-08, cx-13, cx-14]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.627–658（止损表 p.634–635、止盈表 p.635–636、纪律 p.634/641/644）
V1_source_sufficiency:
  passed: true
  reason: 买入/卖出日清单、8 类入场位置、6 档止损数值、7 类止盈分批、放弃条件全部为原文精确参数
V2_executability:
  passed: true
  check_mode: walkthrough
  input: HTF 看涨、周一、CBDR=18pt、Asian=12pt、ES
  expected: 清单通过；入场候选=Asian 下+2–5pt/前日 NY 低点下 FVG 等；止损按场景取 15/20/5pt；止盈分批按表
  observed: 全部参数可查表执行；"9AM 前无 7–10pt 回撤不交易"作为硬门生效
V3_task_utility:
  passed: true
  expected_benefit: 全书唯一成体系的执行+风控数值层；显著减少遗漏与随意移止损
decision: verified
boundary_notes: 仅 ES/SP500 标定（nr-05）；清单条件为"组合增信"非严格 AND（原文 bullet 形式），能力按计数+硬门实现并在 B 说明；"高概率"无统计依据进 B
```

## cap-09 NY Scalp 九步流程

```yaml
id: cap-09
title: NY Session Scalp 九步流程（伦敦确认后）
type: procedure / execution-model
merged_from: [fw-12, pr-33]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.655–658
V1_source_sufficiency:
  passed: true
  reason: 9 步完整含放弃门（9:00 前无 7–10pt 回撤不交易）与入场位（62% Fib）
V2_executability:
  passed: true
  check_mode: walkthrough
  input: London 看涨；NY 8:00 回撤 8pt(ES)
  expected: 通过第 7 步门 → 62% Fib 入场；目标=重测日高/前日高
  observed: 与 p.655–656 一致
V3_task_utility:
  passed: true
  expected_benefit: 把"等回撤"纪律化为可计时可计点的门
decision: verified
boundary_notes: Fib 目标 1&2 具体数值原文未给 → needs-review nr-06，能力只输出"重测日高/PDH"为目标语义
```

## cap-10 ICT 2022 Model 六步 + 新闻日订单流框架

```yaml
id: cap-10
title: ICT 2022 Model 六步执行流程 + Buy/Sell Side Oriented 新闻日框架
type: procedure / execution-model
merged_from: [fw-10, fw-19, pr-15, pr-21, pr-22]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.116–118（9 步+5pt/10pt）, p.151（8:30/9:30 节点）, p.628–631（图 p.407 书 p.303 已核图）
V1_source_sufficiency:
  passed: true
  reason: 六步（扫流动性→位移FVG→MSS→OTE→FVG位→限价）与新闻日 9 步观察框架均完整；模型图已实际核对
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 8:30 新闻后大看跌位移→10:10 后看跌 PD arrays 失效→看涨位移→订单流转变
  expected: Buy Side Oriented：折价阵列限价买入，止损≤5pt、目标 10pt(ES)
  observed: 与 p.116–117 一致
V3_task_utility:
  passed: true
  expected_benefit: 把分散概念组装为单一执行链；新闻日行为有明确门
decision: verified
boundary_notes: "clear unobstructed path" 无判定法 → B；5pt/10pt 仅 ES
```

## cap-11 OTE 入场区计算

```yaml
id: cap-11
title: OTE（0.62–0.79 / 0.705）折价溢价入场区计算
type: calculation
merged_from: [fw-09, pr-03]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.131–132, p.373（"80%"声明无来源）, p.655
V1_source_sufficiency:
  passed: true
  reason: Fib 锚定方向（看涨=高→低）、区间与甜蜜点明确
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 看涨位移后 swing high=110, swing low=100
  expected: OTE 区 = 106.2–107.9，甜蜜点 107.05
  observed: 纯斐波那契计算
V3_task_utility:
  passed: true
  expected_benefit: 统一入场区口径，避免随意挂单
decision: verified
boundary_notes: "80% 有效"无数据 → B 明确为作者未验证声明；价格不总进 OTE（50% 亦常见）进 B
```

## cap-12 Turtle Soup / Stop Run 与 Failure Swing 入场

```yaml
id: cap-12
title: 流动性池挂单入场（Turtle Soup/Stop Run）+ Failure Swing 备选
type: procedure / entry-model
merged_from: [fw-15, fw-16, pr-34, cx-01]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.28–37, p.77, p.197–198（三重确认）, p.592–596, p.631
V1_source_sufficiency:
  passed: true
  reason: 模式三段识别、双向挂单方式、V 型要求、假突破三重确认（FVG+MSS+流动性池）、Failure Swing 备选路径均完整
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 短期低点被扫两次、无买方流动性被取、随后 V 型收回
  expected: 低点处/略下方 Buy Limit；止损于扫荡影线外；备选：若无 stop run 则等 failure swing 重测入场
  observed: 与 p.28–37/p.197–198 一致
V3_task_utility:
  passed: true
  expected_benefit: 作者称最高概率条件；给出主/备两条路径减少踏空与追单
decision: verified
boundary_notes: V 型"立即反应"无时间阈值 → B；图依赖 p.30–37 待逐张核查
```

## cap-13 PO3/AMD 节奏状态机

```yaml
id: cap-13
title: PO3/AMD 三阶段状态机 + Judas Swing 触发规则
type: state-machine
merged_from: [fw-08, pr-19, cx-10, cx-11, cx-12, cx-23]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.215–265（日线模板 p.223–228 图 p.224 书 p.142 已核图；周线 p.217–219/252–257；Judas 参数 p.260–262）
V1_source_sufficiency:
  passed: true
  reason: 三阶段定义、转换铁律（Consolidation→Expansion 恒成立等）、日线/周线时段模板、新闻日 Judas 例外（8:30 有新闻则 9:30 无）均完整
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 纽约 03:20、价格低于 NMO、亚洲区间完好
  expected: 状态=Manipulation（Judas）；预期 Expansion 至 05:00 NY；确认需 MSS+回到 NMO 上/下
  observed: 与 p.223–228/p.230 一致
V3_task_utility:
  passed: true
  expected_benefit: 回答"现在该等还是该进"；新闻日例外规则防止错误期待 Judas
decision: verified
boundary_notes: 阶段切换实时判定缺客观信号 → 状态机输出"预期阶段"而非断言；周三低点后继续下跌当日停手为硬门
```

## cap-14 SMT 背离确认工具

```yaml
id: cap-14
title: SMT Divergence 确认（仅确认，不独立入场）
type: confirmation-tool
merged_from: [fw-05, pr-07, cx-05]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.186–192
V1_source_sufficiency:
  passed: true
  reason: 定义、双向规则、配对品种、"仅确认"用法边界完整
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 折价区预定水平：EURUSD 创新低而 GBPUSD 更高低
  expected: 看涨背离=对既有多头想法的绿灯；无想法时不产生信号
  observed: 与 p.188–190 一致
V3_task_utility:
  passed: true
  expected_benefit: 防止把背离当信号滥用（作者明令）；跨品种数据可程序化比对
decision: verified
boundary_notes: 比对时间框架原文未规定（nr-08）→ 能力要求调用方指定 TF 并记录
```

## cap-15 多时间框架分析-执行工作流（Top Down + 15m→5m）

```yaml
id: cap-15
title: Top Down 分析层级 + 15m→5m 执行工作流
type: procedure / workflow
merged_from: [fw-13, fw-14, pr-20, cx-22]
source_evidence:
  - source_id: src-ict2022
    location: PDF p.22–27, p.88–94, p.121, p.627, p.642–643
V1_source_sufficiency:
  passed: true
  reason: 层级（月/周→日→4H/1H→15m→5m）、各层任务、"不要过度降帧"、盘前/执行时段均完整
V2_executability:
  passed: true
  check_mode: walkthrough
  input: 盘前 8:20
  expected: 15m 标注关键高低/FVG/OB 与 Killzone 预期 → 8:30 后切 5m 精确入场，11:00 前建仓目标
  observed: 与 p.88–94 一致
V3_task_utility:
  passed: true
  expected_benefit: 防止分析瘫痪与帧错配；稳定每日操作顺序
decision: verified
boundary_notes: 无
```

---

## 分流统计

- verified: 15（cap-01…cap-15）
- reference: 见 references.md（MMXM 曲线模型、心态/导论内容、季节性、日内模板、术语词典 95 条、案例 22 条作 A1 证据池）
- needs_review: 见 needs-review.md（nr-01…nr-08）
- rejected/合并: 见 rejected/merge-notes.md（pr 与 fw 重复项合并、纯心态条目降级）
