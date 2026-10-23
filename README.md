# SurviveCorporate

[English](./README.en.md) · 中文

# 把两千年帝王心术，装进你的 AI 助手

**SurviveCorporate** 是一个开源 [Agent Skill](https://github.com/anthropics/skills)（兼容 Claude Code / Claude.ai / Cursor 等）。  
它不灌鸡汤。它用法家、兵家、纵横家、《政事论》《君主论》的冷酷视角拆职场局，给出**合法但强硬**的上中下三策——每条标注典籍出处与风险等级。

[![GitHub stars](https://img.shields.io/github/stars/Rswcf/survive-corporate?style=social)](https://github.com/Rswcf/survive-corporate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Skill](https://img.shields.io/badge/Anthropic-Agent%20Skill-black)](./skills/survivecorporate/SKILL.md)
[![Language](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87%20%7C%20English-blue)](./README.en.md)

> 「事以密成，语以泄败。」——《韩非子·说难》  
> 计划没落地之前，知道的人越少越好。

---

## 效果展示

**用户**：周会上同事 A 把我做的方案当成他的成果汇报。

**SurviveCorporate**：

| 模块 | 输出 |
|---|---|
| 局势判读 | A 抢的是评价权（二柄之「德」）。你的软肋是没有书面痕迹。 |
| 对手之术 | 窃二柄 + 截留信息 |
| 上策 | 当日邮件抄送相关人，附 V1–V3 与数据，抢先定义叙事（风险：低） |
| 今天三事 | ① 整理时间线 ② 发抄送邮件 ③ 约跨部门证人下周评审现身 |
| 出处 | 《韩非子·二柄》「二柄者，刑德也」 |
| 反噬 | 当众羞辱 A → 死敌。韩非知说难，仍死于构陷。 |

另一个高频局：**被集体投诉** → 识别为「罗织」信号 → 分离询问 + 事实包抢先送达决策者（不用反咬构陷）。

更多示例见 skill 附录 D：架空、甩锅、空降领导、下属不服。

---

## 30 秒上手

### Claude Code
```bash
mkdir -p ~/.claude/skills
cp -r skills/survivecorporate ~/.claude/skills/
# 重启或新开会话后，描述你的职场情形即可
```

### Claude.ai
1. 将 `skills/survivecorporate/` 打成 zip  
2. 在项目或 skill 上传入口导入  
3. 直接说：「同事抢功，用 SurviveCorporate 分析」

### Cursor / 其他 Agent
把 `SKILL.md` 放到该产品的 skills / rules / 自定义指令目录（路径因产品而异），确保 agent 能读到 YAML `name` 与 `description`。

### 本地预览
```bash
git clone https://github.com/Rswcf/survive-corporate.git
open skills/survivecorporate/SKILL.md
```

---

## 内含什么

| 项 | 数量 / 说明 |
|---|---|
| 核心法则 | **68** 条，每条含原文、职场用法、风险等级、规避 |
| 主题 | **10**：藏心 / 控权 / 识人测忠 / 进言 / 结盟 / 情报 / 反罗织 / 离间识别 / 立威 / 退路 |
| 对手手段谱系 | **18** 种常见职场招数对照表 |
| 典籍底座 | **14+** 本：韩非、商君、六韬、鬼谷、政事论、君主论、罗织史料、审判官手册… |
| 示例情形 | 抢功、架空、甩锅、集体投诉、空降、下属不服 |
| 研究附录 | `research/` 中古典总览 + 全球阴暗文本精选 |

---

## 精选金句（职场翻译）

- **握二柄**：「二柄者，刑德也。」→ 争评审权与预算权，而不是虚衔。  
- **避逆鳞**：「人主亦有逆鳞。」→ 先摸清上级绝对不能碰的痛点。  
- **密成泄败**：「事以密成，语以泄败。」→ 未落地的计划不要分享。  
- **公不如结**：「公不如私，私不如结。」→ 大会表态不如利益同盟。  
- **识破飞箝**：先捧后套 → 不口诺，书面确认。  
- **反罗织**：多人同步、口径一致的投诉 → 时间线与证据包抢先交决策者。

---

## 典籍清单（节选）

中国：《韩非子》《商君书》《六韬·文伐》《鬼谷子》、罗织经**史料**（今本伪书已标明）、酷吏传  
印度：《政事论》密探与测忠（不涉及制毒步骤）  
欧洲：《君主论》核心章、审判官手册（仅作识别诱导审问）、马萨林《政客心经》（归属有争议）  
伪书警示：今本《罗织经》、Monita Secreta、《锡安长老议定书》——只作危害说明，不作「秘籍」推荐

完整考证见 [`research/`](./research/)。

---

## 为什么值得 Star

1. **真的能用**：不是「厚黑语录合集」，而是带流程、模板、风险规避的 Agent Skill。  
2. **出处可核**：关键原文已对维基文库 / 通行英译；伪书单独标红。  
3. **有刹车**：范围写死——合法强硬。罗织与审判官材料只用于**反制**。  
4. **中英双 README**，方便传播与 awesome 列表收录。  
5. **你也可以贡献**新法则与匿名案例，见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Rswcf/survive-corporate&type=Date)](https://star-history.com/#Rswcf/survive-corporate&Date)

---

## 仓库结构

```
skills/survivecorporate/SKILL.md   # Anthropic Agent Skill 正文
research/                          # 典籍研究整理
docs/LAUNCH.md                     # 推广标题草稿（不自动发布）
README.md / README.en.md
CONTRIBUTING.md
LICENSE
```

---

## 免责声明

本仓库是**历史与策略研究**及 AI skill 工程。SurviveCorporate 只输出合法应对（留痕、叙事、结盟、HR/法律通道等），不提供伪造证据、诬告、骚扰、侵入隐私或歧视性操作。使用者自行遵守所在地法律与公司合规政策。典籍中的阴暗手段用于识别与防范，不用于伤害他人。

## License

代码与 skill：MIT。文档建议遵循同一 MIT 授权分发；引用古籍原文请遵循公有领域惯例并标注出处。

---

如果这个项目让你少踩一次职场暗桩——请点一个 Star，让更多人的 AI 助手学会「先判利害，再谈忠奸」。
