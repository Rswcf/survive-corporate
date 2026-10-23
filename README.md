<div align="center">

# SurviveCorporate

**把两千年帝王心术，装进你的 AI 助手。**

同事抢功、被甩锅、被架空、被集体投诉——问普通 AI，多半只能得到「多沟通、保持积极」。  
SurviveCorporate 让它先像韩非一样算清利害，再给出**合法但强硬**的上中下三策：每一策都标出典籍出处和风险等级。

[![GitHub stars](https://img.shields.io/github/stars/Rswcf/survive-corporate?style=social)](https://github.com/Rswcf/survive-corporate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Claude%20Code%20%7C%20Claude.ai%20%7C%20Cursor-black)](./skills/survivecorporate/SKILL.md)
[![Validate](https://github.com/Rswcf/survive-corporate/actions/workflows/validate.yml/badge.svg)](https://github.com/Rswcf/survive-corporate/actions/workflows/validate.yml)

**中文** · [English](./README.en.md)

</div>

> 「事以密成，语以泄败。」——《韩非子·说难》  
> 计划没落地之前，知道的人越少越好。

## 目录

- [效果展示](#效果展示)
- [30 秒安装](#30-秒安装)
- [怎么用](#怎么用)
- [内含什么](#内含什么)
- [红线：它不做什么](#红线它不做什么)
- [典籍清单](#典籍清单)
- [仓库结构](#仓库结构)
- [参与贡献](#参与贡献)
- [免责声明](#免责声明) · [License](#license)

---

## 效果展示

**你**：周会上同事 A 把我做的方案当成他的成果汇报了。

**SurviveCorporate**（示例输出，按 [`references/examples.md`](./skills/survivecorporate/references/examples.md) 例 1 整理；实际回答因模型与上下文而异）：

```text
【局势判读】A 抢的是评价权（二柄之「德」）。你的软肋：没有书面痕迹。
【对手在用什么术】窃二柄 + 截留信息
【风险评估】当众撕破：暴露概率中，后果是结死仇；书面补证：暴露概率低
【上策】当日邮件抄送相关人，附 V1–V3 与数据，「下周我汇报落地节奏」| 风险：低 | 规避：只陈述事实，不写「A 抢功」
【中策】下次会上补一句：「数据是我跑的，补充两点。」| 风险：中
【下策】私下与 A 谈署名规则 | 风险：中（口惠而实不至）
【今天就做的三件事】1. 整理时间线  2. 发抄送邮件  3. 约跨部门证人下周评审现身
【出处】《韩非子·二柄》「二柄者，刑德也」——争的是评价权，不是一次功劳
【反噬风险】韩非懂说难，仍死于构陷。当众羞辱 A = 多一个死敌。
```

另一个高频局：**一周内三份口径相近的投诉** → 识别为「罗织」信号 → 要求分离询问，把时间线与原始记录抢先交给决策者，不反咬、不调查投诉人隐私。

---

## 30 秒安装

### Claude Code（推荐：插件市场）

在 Claude Code 里依次执行：

```text
/plugin marketplace add Rswcf/survive-corporate
/plugin install survivecorporate@survive-corporate
```

### Claude Code（手动复制）

```bash
git clone https://github.com/Rswcf/survive-corporate.git
mkdir -p ~/.claude/skills
cp -r survive-corporate/skills/survivecorporate ~/.claude/skills/
```

新开一个会话，直接描述你的职场情形即可。

### Claude.ai

1. 打包 skill 文件夹（zip 根目录必须是 `survivecorporate/` 文件夹）：

   ```bash
   git clone https://github.com/Rswcf/survive-corporate.git
   cd survive-corporate/skills && zip -r ../survivecorporate.zip survivecorporate
   ```

2. 确认 **Settings → Capabilities** 中已开启 *Code execution and file creation*（skills 依赖它）。
3. 打开 **Customize → Skills**，点 **+** → *Create skill* → *Upload a skill*，上传 `survivecorporate.zip`。
4. 新对话里说：「同事抢功，用 SurviveCorporate 分析」。

### Cursor

```bash
git clone https://github.com/Rswcf/survive-corporate.git
mkdir -p ~/.cursor/skills
cp -r survive-corporate/skills/survivecorporate ~/.cursor/skills/
```

Cursor 也会读取 `~/.claude/skills/`，所以已按 Claude Code 方式安装的无需重复。项目级安装则放到仓库内的 `.cursor/skills/`。可在 **Customize → Skills** 中确认已加载，或在 Agent 里输入 `/survivecorporate` 手动调用。

### 其他支持 Agent Skills 标准的工具

把整个 `skills/survivecorporate/` 文件夹（含 `references/`）放进该工具的 skills 目录，例如 `~/.agents/skills/`。只复制 `SKILL.md` 不够：法则全文在 `references/` 里。

---

## 怎么用

不需要记命令，像跟军师说话一样描述局面。可以直接复制这些开头：

- 「新领导空降，带了两个旧部，我原来的项目被慢慢收走了，怎么办？」
- 「项目延期，PM 在会上说一直在等我的交付，但需求是上周才确认的。」
- 「资深下属绕过我直接找大老板，我的指令他软抵制。」
- 「HR 约我谈话，说收到几份对我的投诉，让我先写份情况说明。」
- 「老板当众夸我，然后让我接一个没人要的烂项目。这是什么套路？」

提示：交代清楚**你的职级与汇报线、对手是谁、已有哪些书面痕迹、你想要什么结果**，输出会更准。信息不够时，skill 会先问你最多 3 个问题。

> 关于「下策」：本 skill 里的下策指**退出与切割方案**（止损、转岗、谈补偿离职），不是「最差的招」。

---

## 内含什么

| 项 | 说明 |
|---|---|
| 法则 | **68** 条（文伐十二节合为一条），附出处、职场用法、风险等级，多数附规避 |
| 主题 | **10**：藏心 / 控权 / 识人测忠 / 进言 / 结盟 / 情报 / 反罗织 / 离间识别 / 立威 / 退路 |
| 对手手段谱系 | **18** 种常见职场招数 → 对应古典术名 → 首选反制 |
| 完整示例 | **6** 个：抢功、架空、甩锅、集体投诉、空降领导、下属不服 |
| 反噬史例 | 商鞅、吴起、韩非、李斯、文种、来俊臣、周兴——每一招历史上怎样反咬回来 |
| 研究附录 | [`research/`](./research/)：中国古典总览 + 全球阴暗文本精选（含伪书辨析） |

### 精选金句（职场翻译）

- **握二柄**：「二柄者，刑德也。」→ 争评审权与预算权，而不是虚衔。
- **避逆鳞**：「人主亦有逆鳞。」→ 先摸清上级绝对不能碰的痛点。
- **密成泄败**：「事以密成，语以泄败。」→ 未落地的计划不要分享。
- **公不如结**：「公不如私，私不如结。」→ 大会表态不如利益同盟。
- **识破飞箝**：先捧后套 → 不口诺，书面确认。
- **反罗织**：多人同步、口径一致的投诉 → 时间线与证据包抢先交决策者。

### 和「厚黑语录合集」有什么不同

| | 语录 / 鸡汤 | SurviveCorporate |
|---|---|---|
| 形态 | 一堆金句 | Agent Skill：固定流程 + 输出模板 |
| 给什么 | 态度 | 上中下三策 + 今天就做的三件事 + 话术 |
| 风险 | 不提 | 每策标暴露概率、后果、可否认性、止损预案 |
| 出处 | 常有伪托 | 关键原文对维基文库 / 通行英译核实；拿不准标【待核】；伪书单独标明 |
| 边界 | 无 | 只出合法招，阴暗典籍只用于识别和反制 |

---

## 红线：它不做什么

不提供伪造证据、诬告、骚扰恐吓、侵入账户或窥探隐私、歧视、报复举报人等手段。用户提出这类需求时，skill 会换成效果相当的合法硬招：书面留痕、抢先定义叙事、结盟、上收决策权、走 HR 或法律通道。涉及性骚扰、歧视、欠薪、工伤等法定权益事项时，会提示保存证据并咨询劳动监察部门或律师。

《罗织经》史料与审判官手册只用于**识别并反制**别人对你的构陷。

---

## 典籍清单

- **中国**：《韩非子》《商君书》《六韬·文伐》《鬼谷子》《史记》《资治通鉴》、两唐书酷吏传与《大唐新语》中的罗织**史料**（今本《罗织经》为伪书，已标明）
- **印度**：《政事论》（Arthashastra）密探与四诱测忠（不涉及制毒步骤）
- **欧洲**：《君主论》核心章、Eymerich 与 Bernard Gui 的审判官手册（仅用于识别诱导式审问）、马萨林《政客心经》（归属有争议）
- **伪书警示**：今本《罗织经》、Monita Secreta、《锡安长老议定书》——只作危害说明，不作「秘籍」推荐

核实说明见 [`references/sources.md`](./skills/survivecorporate/references/sources.md)，完整考证见 [`research/`](./research/)。

---

## 仓库结构

```text
skills/survivecorporate/
├── SKILL.md              # 核心：范围、流程、输出模板、对手手段谱系、法则索引
└── references/
    ├── rules.md          # 附录A：68 条法则全文
    ├── history.md        # 附录C：反噬史例与风险规律
    ├── examples.md       # 附录D：6 个完整示例
    └── sources.md        # 附录E：原文核实说明
.claude-plugin/           # Claude Code 插件与市场清单
.cursor-plugin/           # Cursor 插件与市场清单
research/                 # 典籍研究整理
docs/LAUNCH.md            # 推广草稿（不自动发布）
```

`SKILL.md` 只放每次都要用的内容，法则全文按需加载，省上下文。

---

## 参与贡献

欢迎提交新法则（必须附可核对原文）、匿名化职场案例、引文勘误和译文。见 [CONTRIBUTING.md](./CONTRIBUTING.md)，或用 [Issue 模板](https://github.com/Rswcf/survive-corporate/issues/new/choose) 先讨论。

提交职场情形时请彻底匿名：不写真实姓名、公司、部门，Issue 是公开的。

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Rswcf/survive-corporate&type=Date)](https://star-history.com/#Rswcf/survive-corporate&Date)

---

## 免责声明

本仓库是**历史与策略研究**及 AI skill 工程，不构成法律或人力资源专业意见。SurviveCorporate 只输出合法应对（留痕、叙事、结盟、HR/法律通道等）。使用者自行遵守所在地法律与公司合规政策。典籍中的阴暗手段用于识别与防范，不用于伤害他人。

## License

[MIT](./LICENSE)。引用古籍原文请标注出处。

---

<div align="center">

如果它帮你少踩一次职场暗桩，点个 Star，让更多人的 AI 助手学会「先判利害，再谈忠奸」。

</div>
