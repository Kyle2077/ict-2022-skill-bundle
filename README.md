# ICT Intraday Playbook — 技能蒸馏产物

《开启ICT 2022导师计划的成功之门》（*Unlocking Success in ICT 2022 Mentorship: The Smart Money Guide to the Full ICT Day Trading Model*，LumiTraders，2023）的方法论蒸馏产物，由 [visual-book-skills](https://github.com/savagealexander/visual-book-skills)（图文知行 · Cangjie Tools v2.5.0）流水线生成。

---

## ⚠️ 版权与授权声明（务必先读）

本仓库包含受版权保护材料的衍生内容，包括但不限于：

- 原书页面渲染图（`dist/*/resources/figures/*.png`、`books/*/figures/*.png`）
- 原书全文文本提取与分章文本（`books/*/source/`，约 45 万字符）
- 原书术语、规则表述与简短引用（各能力卡 R 段，每处 ≤150 字）

原书版权页明确声明：

> "No part of this book may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of the publisher, except for brief quotations embodied in critical reviews and certain other non-commercial uses permitted by copyright law."

**因此本仓库必须保持私有（private）**：

- 不要设为公开仓库，不要 fork 到公开空间，不要分享仓库链接
- 不要将 `resources/figures/` 与 `books/*/source/`、`books/*/figures/` 内容发布到任何公开渠道
- 如需公开发布技能包，应先移除原书页面图与全文提取，仅保留自行转述的方法论描述，并取得出版商书面许可或确认符合"简短引用"范围

版权归原作者所有。本仓库内容仅用于个人学习与研究。

---

## 免责声明（Disclaimer）

原书免责声明同样适用于本产物：

> 本书内容仅用于教育与信息目的，不构成专业建议，也不应作为专业建议的替代。作者与出版商对基于本内容所做的任何决定不承担责任。

本仓库的技能产物：

- **不提供投资建议**，不预测价格，不给出买卖指令
- 输出为价位区间、检查清单结论与风控参数，需使用者自行判断并自担风险
- 原书**未提供任何回测数据、胜率统计或样本量**；"高概率"等表述属作者叙事而非统计结论
- 全部点数参数仅按原书 **ES/SP500 期货**标定，跨品种换算原书未提供
- 原书时段标注为 EST/纽约时间，**未说明夏令时（EDT）处理**；产物统一按纽约本地时间（America/New_York）解释并显式声明

交易有风险，入市需谨慎。

---

## 仓库结构

```
dist/ict-intraday-playbook/     # 编译产物（可安装的技能包本体）
├── SKILL.md                    # 单一入口：路由表 + 核心原则 + 判停条件
├── references/
│   ├── capability-index.md     # 28 个能力的索引表
│   ├── cheatsheet.md           # 一句话决策规则速查
│   ├── glossary.md             # 术语词典（含补章新增术语）
│   ├── overview.md             # 书级参考区（批判与未成能力的参考内容）
│   └── capabilities/           # 28 张 RIA++ 能力卡（R/I/A1/A2/E/B 六段）
├── resources/figures/          # 8 组已核查图文证据（原书页面 PNG + 核查记录）
└── BUILD_MANIFEST.json         # 构建清单（run_id、文件哈希）

books/ict-2022-mentorship/      # 蒸馏工作目录（流水线全量产物）
├── PIPELINE_STATE.md           # 流水线状态与收尾声明（缺口清单）
├── BOOK_OVERVIEW.md            # 阶段 0 整书理解（主旨/骨架/术语/批判/任务清单）
├── DIGEST.md                   # 面向读者的精华长文
├── GLOSSARY.md                 # 术语词典
├── verified.md                 # 阶段 1.5 三重验证记录（15 条首轮）
├── coverage-audit.md           # 任务覆盖审计（含补章审计）
├── needs-review.md             # 16 项来源/条件/测试缺口
├── references.md               # 参考级内容与交付映射
├── rejected/                   # 去重合并与降级说明
├── candidates/                 # 阶段 1 五组提取候选（试点轮）
├── candidates-supplement/      # 阶段 1 五组补充提取候选（补章轮）
├── evals/                      # 阶段 4 评测用例与测试报告
├── source/                     # ⚠️ 原书全文提取与分章文本
├── figures/                    # ⚠️ 45 页原书页面渲染图（含 manifest）
└── .cangjie/
    ├── capabilities/           # Capability Bundle（唯一可编译事实源）
    │   ├── verified.yaml       # 28 个能力的元数据与晋级去向
    │   ├── destinations.json   # 阶段 1.6 去向清单
    │   ├── cards/              # 28 张能力卡正文
    │   ├── book/               # overview.md + glossary.md
    │   └── resources/figures/  # 随包交付的图证
    ├── snapshots/              # 编译快照（可回滚）
    └── runs/                   # 构建运行记录

scripts/                        # 可复现脚本（文本提取、章节切分、页面渲染、校验）
```

---

## 能力概览

28 个能力单元，覆盖全书 33 章。按功能分组：

| 分组 | 能力 |
|---|---|
| **时间与过滤** | session-taboo-filter（五 Killzone + 禁忌日）、afternoon-hours-playbook（AM/Lunch/PM 剧本）、daily-templates-playbook（四种日内模板）、dxy-seasonal-filter（DXY 联动 + 季节性） |
| **价位坐标** | daily-static-anchors（PDH/PDL、NMO/NYO、Asian range、CBDR±STD）、nwog-ndog-anchors（周/日缺口 + CE + Event Horizon）、opening-range-cpe（开盘投影 + CPE）、ipda-data-range-builder（20/40/60 日回溯） |
| **方向判定** | daily-bias-checklist（偏向依据链）、liquidity-dol-state-machine（ERL/IRL 交替 + 下一目标）、po3-amd-state-machine（三阶段节奏 + Judas）、mmxm-state-machine（做市商模型 + terminus 校准） |
| **结构识别** | market-structure-hierarchy（STL/ITL/LTL 层级）、mss-displacement-gate（突破有效性）、fvg-three-candle（FVG 检测）、pd-array-block-dictionary（OB/BB/MB/RB/PB/VB）、three-drives-pattern（三驱模式）、order-flow-formation-gate（OF 形成门） |
| **买卖点与风控** | ict-2022-model（六步执行链）、high-probability-entry-risk（入场清单 + 止损止盈表）、ote-entry-zone（Fib 0.62/0.705/0.79）、turtle-soup-entry（扫掠反手）、ny-scalp-nine-step（NY 九步）、institutional-perception-model（区间 breaker 模型）、ict-atm-method（60m stop-hunt） |
| **确认与工作流** | smt-divergence-confirm（跨品种裂缝确认）、top-down-workflow（多帧顺序协议） |

---

## 安装与使用

### 环境要求

- Python 3.10+
- `PyYAML`、`pypdf`、`Pillow`（可选 `PyMuPDF` 用于 PDF 页面渲染；Poppler 非必需）
- 自检：`python scripts/cangjie.py doctor`（脚本来自 visual-book-skills）

### 安装产物

```bash
# 方式一：通过 visual-book-skills 的 SkillImport 安装 dist/ict-intraday-playbook 目录
# 方式二：复制到宿主技能的 skills 目录（Claude Code: ~/.claude/skills/，Cursor: .cursor/skills/）
```

安装后用一句触发语验证，例如：

- "今天 ES 偏多还是偏空？" → daily-bias-checklist
- "现在是哪个 killzone，能做吗？" → session-taboo-filter
- "这三根 K 线有没有 FVG？" → fvg-three-candle
- "这周 NWOG 和 CE 在哪？" → nwog-ndog-anchors

---

## 复现蒸馏流程

```bash
# 1. 提取全文与分章（需原书 PDF 路径）
python scripts/extract_text.py
python scripts/scan_chapters.py
python scripts/split_chapters.py

# 2. 渲染关键图页（需 PyMuPDF）
python scripts/render_figs.py

# 3. 从 Capability Bundle 编译（需 visual-book-skills 的 cangjie.py）
python <visual-book-skills>/scripts/cangjie.py compile \
  --bundle books/ict-2022-mentorship/.cangjie/capabilities \
  --out dist/ict-intraday-playbook --output single --yes

# 4. 校验产物
python <visual-book-skills>/scripts/validate_skill_pack.py dist/ict-intraday-playbook
```

> **Windows 注意**：编译器内部调用子进程读取 UTF-8 输出，需设置 `$env:PYTHONUTF8 = "1"`，否则会因 GBK 解码失败。

---

## 已知缺口

`books/ict-2022-mentorship/needs-review.md` 记录了 16 项缺口，全部在能力卡 B 段（Boundary）显式声明，未做臆造补全。其中影响使用的关键项：

| 编号 | 缺口 | 影响 |
|---|---|---|
| nr-01 | 原书未说明夏令时处理 | 全部时段类能力按纽约本地时间解释 |
| nr-05 | 点数参数仅 ES 标定 | 其他品种降级为仅结构判定，不输出点数 |
| nr-03 | Displacement 无量化阈值 | 采用"收盘越位 + 留下 FVG"作可计算代理 |
| nr-16 | Ch14 Opening Range 公式字面量纲不通 | 按 "1:1 deviation below" 对称语义实现 |

---

## 测试记录

见 `books/ict-2022-mentorship/evals/test-results.md`：

- 首轮（试点 15 能力）：触发盲测 42 条、输出盲测 28 用例、无卡基线对照；修正 5 处描述歧义与 2 处测试设计错误后回归通过
- 补章轮（新增 13 能力）：触发 20/20、输出 25/25 通过
- 方式：独立 sub-agent 盲测（执行器只见能力卡与任务输入，不见断言与预期答案）
- 未测项：图文"新图应用/反例图/模糊判停"评测未做（需真实未参与生成的新图）；无 old_skill 变体对照；Token/耗时未采集

---

## 致谢

- 原书内容版权归原作者与出版商所有
- 蒸馏流水线：[visual-book-skills](https://github.com/savagealexander/visual-book-skills)（基于 kangarooking/cangjie-skill）
