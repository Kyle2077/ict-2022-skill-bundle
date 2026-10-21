# test-results.md — 阶段 4 压力测试报告（ICT 2022 Mentorship）

- 日期：2026-10-20；宿主：Qwen 工作助理 / qwen3.8-max；方式：独立 sub-agent 盲测（非 fallback 自测）
- 触发盲测：3 组干净 sub-agent，42 条提示（含 8 条跨 skill 混淆诱饵、7 条路由可达性）
- 输出盲测：5 组干净执行 sub-agent（只见卡+任务，不见断言）+ 1 组无卡基线（B1-B3）
- 回归复测：修正后 1 组触发（6 条）+ 1 组输出（5 条）

## 触发精度（首轮 42 条）

通过 36 / 42。失败 6 条及处置：

| 提示 | 首轮判给 | 期望 | 根因 | 处置 |
|---|---|---|---|---|
| p11 算BTC亚洲区间 | none | daily-static-anchors(降级) | 描述未声明"锚值与品种无关、仅过滤降级" | 修 skill 描述+卡片 E 段（输出契约固定字段+非ES filter=not_applicable） |
| p13 溢价区该预期什么 | router/liquidity | daily-bias-checklist | 偏向卡描述未覆盖"溢价/折价该预期什么"信号 | 修 skill 描述（触发词补 premium discount 预期）——实际卡 A2 已含，描述补强 |
| p16 今天几点开始看盘 | session-taboo-filter | top-down-workflow(或session) | 两卡描述对"看盘顺序/起始时段"信号重叠 | 修两卡描述边界（session 不答顺序；top-down 触发词补看盘顺序/起始） |
| p21 FVG回补概率 | null(拒答) | fvg 卡应激活并答"无统计依据" | 描述未声明"回补概率问题应激活并说明无依据" | 修 skill：B/A2 明确该问题应激活并输出"作者未验证" |
| p25 9点没回撤还做吗 | po3 | high-probability-entry-risk | 回撤门写在 hpe 卡但描述触发词未含 | 修 skill 描述（触发词补 9点没回撤） |
| p30/p35 CPI/NFP后找设置·Judas时点 | session | ict-2022-model / po3 | 新闻日设置查找与 Judas 时点归属不清 | 修两卡描述（model 覆盖新闻后设置查找；po3 触发词补 Judas 时点；session 声明不答 Judas 时点） |

回归复测（修正描述后）：r01-r06 全部 6/6 正确。

## 路由可达性（7 条）：7/7 正确（route-01..07 均指向预期卡）。

## 输出质量（首轮 28 用例：15 能力 × 正常+边界）

- 计划 28，完成 28；机械断言通过 24；失败 4：
  1. fvg-boundary：断言设计错误（数据按作者规则实为有效 bullish FVG，执行器答 true 正确）→ 修测试，理由入 audit；旧用例保留为 -old-wrongcase（断言改 true）。
  2. anchors 字段名：执行器输出嵌套 asian_range{...}，suite 期望扁平 asian_range_width → 修 skill 输出契约（固定字段名）；回归 R4/R5 通过。
  3. po3-normal：执行器答 accumulation（把 03:20 当亚洲窗）→ 根因=卡未给"阶段窗口表"（阶段窗口≠Killzone 会话窗）→ 修 skill；回归 R2 答 Manipulation/Judas 正确。
  4. model-boundary：执行器 status="unmet"，suite 期望 stop_step1 → 修 skill 固定 status 词汇；回归 R3 正确。
- 基线对照（无卡 B1-B3）：B1/B2 数值与有卡组一致（FVG 区间、OTE 三档为通用算术，skill 增益在口径统一与边界处理）；B3 无卡组答出 cbdr_mid/width 但**缺口径声明**（未标 1h 实体、未标时区、无过滤降级），有卡组输出含 timezone 与 filter_verdict——skill 增益=口径与降级契约，符合 V3 预期。
- 硬门/判停类（session-boundary、hpe-boundary、ny-boundary、model-boundary、po3-boundary、smt-boundary、liq-boundary、anchors-missing、ote-missing、topdown-boundary、bias-boundary、mss-boundary、pdarray-boundary、fvg 旧边界）：修正后全部按卡约定输出（不交易/null/询问/observe_only/stop_*），0 例猜值。

## 缺失与未测

- 图文评测（08 §4）：资源完整性已验（4 图可解码、manifest 哈希一致）；"新图任务应用/反例图/模糊图判停"未做（需真实未参与生成的新 K 线图，本次试点不伪造）→ 记入 needs-review nr-11，交付标为部分完成。
- old_skill 变体：首次蒸馏无旧版，仅 new/without 两组。
- Token/耗时：未采集（宿主未暴露），不宣称。

## 结论

触发与输出在修正后全部通过训练集回归；保留用例（B 组基线 + 回归集 r01-r06/R1-R5）未参与调优，作为验收集通过。阶段 4 判为通过（带上述未测项声明）。


---

# 补章压力测试（2026-10-21，全书 33 章补齐后）

- 方式：独立 sub-agent 盲测（触发 1 组 20 条 + 输出 4 组 25 用例）；执行器只见能力卡与任务输入。
- **触发/路由精度：20/20 通过**（13 张新卡各 1 条正向 + 3 条跨卡诱饵（q14/q15/q17 正确让位既有卡）+ 1 条无关诱饵（q16 正确拒绝）+ 3 条新卡近邻场景（q18/q19/q20 全部路由正确））。
- **输出质量：25/25 通过**，覆盖 13 张新卡中 11 张的正常+边界用例（opening-range-cpe、nwog-ndog-anchors、ipda-data-range-builder、mmxm-state-machine、market-structure-hierarchy、three-drives-pattern、monday-range-procedure、afternoon-hours-playbook、daily-templates-playbook、order-flow-formation-gate、institutional-perception-model、ict-atm-method、dxy-seasonal-filter）。全部判停门（ETH-only 停、HTF 缺失停、profile 门、5 分钟门、9 点回撤门镜像、数据不足降级）按卡约定触发，0 例猜值。
- 训练期修正 1 处：opening-range-cpe 原文公式量纲歧义（nr-16），按 1:1 对称偏离语义修正实现并登记；修正后 T1/T2 通过。
- 未测项延续首轮声明：图文"新图应用/反例图/模糊判停"未做（nr-11）；无 old_skill 变体；Token/耗时未采集。
- 结论：补章后触发与输出回归全部通过，进入阶段 5 重编译。
