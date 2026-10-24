# 发布与推广手册（由你本人决定是否发布）

这里是草稿和清单，**不要**由机器人代发帖、代提 PR 或代开账号。所有数字只写真实的；没有就不写。

---

## 1. 定位

- **一句话（中）**：被抢功、被甩锅、被架空时，一位读过《韩非子》的 AI 前辈，心平气和地讲出合法又管用的应对。
- **一句话（英）**：A calm AI mentor for office politics: firm, legal moves from Han Feizi and Machiavelli, packaged as a Claude Code / Cursor skill.
- **对外口径**：重点讲「自保」和「看清局面」，不讲「整人」。古书是卖点，合法和风险提醒是信任来源。

---

## 2. 发布前必做（只能你在 GitHub 网页上操作）

- [ ] **About → Description**（仓库简介会出现在搜索结果和分享卡片里，中英都放进去）：

  ```text
  A calm AI mentor for office politics. Claude Code / Claude.ai / Cursor skill: credit theft, blame-shifting, being sidelined, handled with legal moves from Han Feizi & Machiavelli. 职场军师：被抢功、被甩锅、被架空时怎么办。
  ```

- [ ] **About → Topics**（最多 20 个）：保留 `agent-skills` `claude-skills` `office-politics` `career` `chinese-classics` `han-feizi` `machiavelli` `arthashastra` `strategy`；新增 `claude-code` `claude-code-plugin` `cursor` `workplace` `career-advice` `ai-mentor` `chinese`；去掉 `awesome`（这个 topic 约定给精选列表用）、`anthropic`（不是官方项目，避免误会）、`prompt-engineering`（不贴切）。
- [ ] **About → Website**：先填 `https://github.com/Rswcf/survive-corporate/blob/main/README.en.md`，方便英文访客。
- [ ] **Settings → General → Social preview**：上传 `assets/social-preview.png`（1280×640）。不上传的话，X、LinkedIn、微信里分享链接只会显示一张默认灰图。
- [ ] **Settings → General → Features**：打开 **Discussions**，给「我遇到了这样的事」类讨论一个去处，Issue 只留给 bug 和勘误。
- [ ] **发布 v0.1.0**：本地 `git tag v0.1.0 && git push origin v0.1.0`，`Release` workflow 会自动附上 `survivecorporate.zip`，Claude.ai 用户就不用自己打包了。
- [ ] **个人主页**：在 GitHub Profile 填写 Bio、所在地、个人网站或社交账号；把本仓库 **Pin** 到主页；可以建一个 `Rswcf/Rswcf` 仓库写个人 README。访客从项目点进你的主页时，这是建立个人名字的地方。
- [ ] **录一段真实 GIF**（15–30 秒，真实对话，不摆拍）：放到 `assets/demo.gif`，再把两份 README 里预留的注释打开。
- [ ] **实测安装**：Claude Code 插件市场两行命令、Claude.ai 上传 zip、Cursor 复制目录，各跑一次真实问题。
- [ ] Validate workflow 在 main 上为绿色。

---

## 3. 素材

| 文件 | 尺寸 | 用在哪里 |
|---|---|---|
| `assets/social-preview.png` | 1280×640 | GitHub 社交预览、X、LinkedIn、Product Hunt 首图、HN 外链预览 |
| `assets/cards/*.png` | 1080×1440（3:4） | 小红书、即刻、微博、朋友圈；英文卡可用于 X、LinkedIn |
| `assets/icon.png` | 512×512 | 插件目录图标、Product Hunt 缩略图 |
| `assets/demo.gif`（待录） | — | README、X、B 站 / YouTube 封面截图 |

卡片文字全部摘自 `references/examples.md`，由 `python3 scripts/render_assets.py` 生成，改文案就改脚本后重新生成。

---

## 4. 节奏建议

不要同一天把同一段话贴满所有平台，既像刷屏，也没时间回复评论。大致顺序：

1. **第 1 天**：中文社区先发（V2EX、即刻），收集第一批真实反馈，修掉安装问题。
2. **第 2–3 天**：Hacker News（美东时间周二到周四上午较常见），发完当天守着回复。
3. **随后几天**：Reddit 各版块分开发，每个版块写不同的开头；X 和 LinkedIn 同步。
4. **一周后**：小红书、知乎、B 站等内容型平台，用卡片和真实对话做内容；有了稳定的版本再考虑 Product Hunt。
5. 提交到 awesome 列表和插件目录。

不要请人集中点赞或刷票：HN、Reddit、Product Hunt 都会识别并降权，反而伤名声。

---

## 5. 各平台草稿

### Hacker News（Show HN）

- 标题：`Show HN: SurviveCorporate – an AI mentor for office politics, built on Han Feizi`
- 链接：仓库地址
- 首条评论（发帖后立刻由你自己发）：

  ```text
  I kept noticing that when you ask an AI about a coworker taking credit for your work, it says "communicate openly". That's fine advice, but people who've lived through it know it's rarely enough.

  SurviveCorporate is an Agent Skill (Claude Code, Claude.ai, Cursor) that answers like a seasoned mentor who has read Han Feizi, Guiguzi and Machiavelli: it explains what's really going on, gives three options, says where each one could backfire, and lists three things to do today. It only suggests legal moves; the darker historical tactics (e.g. Tang-dynasty frame-ups) are there so you can recognize them.

  Key quotes are checked against Wikisource and standard translations, and uncertain ones are marked. It's MIT licensed. I'd love feedback on whether the advice feels useful or too clever by half.
  ```

  上面是参考，请换成你自己的真实动机。

### Reddit

- 版块：r/ClaudeAI、r/ClaudeCode、r/cursor。发之前读每个版块的置顶规则，很多版块要求自我推广帖打 flair，或限制频率。
- 不建议发 r/LocalLLaMA：这个 skill 针对 Claude / Cursor，与本地模型关系不大，容易被认为跑题。
- 职场类版块（如 r/careerguidance）一般不欢迎工具推广，除非规则允许，否则只在相关帖子里认真回答问题，不贴链接。
- 标题示例：`I turned Han Feizi and Machiavelli into a Claude skill that gives calm, legal advice on office politics`
- 正文：一段真实示例（抢功那段），然后是安装两行命令，最后一句说明它只给合法建议。

### X / Twitter（英文 thread）

1. Ask an AI what to do when a coworker steals credit and you get "communicate openly." I wanted something closer to a mentor who's read Han Feizi. So I built one.
2. 附英文卡片 `credit-theft-en.png`：It gives three options, where each can backfire, and three things to do today.
3. 附 GIF：real conversation in Claude Code.
4. Legal moves only. The dark tactics in the classics are there so you can spot them, not use them.
5. Free, MIT, works in Claude Code / Claude.ai / Cursor: 仓库链接

### LinkedIn

职场人群最贴合的平台。用第一人称讲你为什么做它（请写真实经历，不要编故事），配社交预览图或英文卡片，结尾放链接。语气克制，强调「保护自己、不踩雷」。

### Product Hunt

- 名称：SurviveCorporate
- Tagline（≤60 字符）：`A calm AI mentor for office politics, built on the classics`
- 图库：社交预览图、英文卡片、GIF
- Maker 首评：为什么做、它不做什么（红线）、欢迎反馈
- 等有了真实 GIF 和第一批反馈再发，第一印象只有一次。

### V2EX

- 节点：**分享创造**
- 标题：`开源了一个 Claude / Cursor Skill：被抢功、被甩锅时，让 AI 像读过韩非子的前辈一样帮你分析`
- 正文：一段示例回答节选 + 安装命令 + 「只给合法建议」+ 欢迎拍砖。

### 即刻

- 圈子：AI 探索站、独立开发者相关圈子
- 文案：同事抢功时，韩非会怎么劝你？我把它做成了一个 AI skill。配 3 张卡片。

### 小红书

- 用 3:4 卡片做图文，标题例：`被同事抢功，一位“读过韩非子”的 AI 这样劝我`
- 正文讲情境和建议本身，链接在小红书里不能点，写「GitHub 搜 survive-corporate」即可。
- 措辞偏「自保」「看清局面」，少用「权谋」「帝王心术」「厚黑」这类词做标题，内容平台对教人算计的内容比较敏感。

### 知乎

- 写一篇专栏文章：《用〈韩非子〉看职场抢功：一个 AI skill 的设计思路》，讲古书怎么翻译成可执行的、合法的建议。
- 在「同事抢功怎么办」这类问题下回答时，先把问题本身答好；提到项目时说明是自己做的。

### B 站 / YouTube

- 60–90 秒录屏：提一个真实问题 → 展示回答 → 讲一句它的红线 → 安装方式。
- 标题例：`我让 AI 读了韩非子，然后问它：同事抢功怎么办`

### awesome 列表与插件目录

- 由你本人向 awesome-claude-skills、awesome-agent-skills 等列表提交 PR，先读各自的贡献规则和分类。
- 在 Anthropic 的 Claude Code 插件目录提交（`assets/icon.png` 会作为首次提交时的图标）。
- Cursor：在 Cursor 中实测 Customize → From GitHub Repository 导入（使用 `.cursor-plugin/marketplace.json`）。

---

## 6. 可能的质疑和回应

- **「这是在教人搞办公室政治」**：它只给合法做法，红线写在 README 和 skill 里；古书里的阴招用来识破，不用来进攻。
- **「古文引用不准」**：欢迎开勘误 Issue；拿不准的引文已经标【待核】，伪书单独标明。
- **「这不就是一个 prompt」**：是 prompt 加上 68 条带出处的法则、18 种对手招数和完整示例，按需加载；欢迎对比效果。

---

## 7. 跟踪

- GitHub **Insights → Traffic** 看访问来源和热门页面，判断哪个平台值得继续投入。
- 只在对外内容里引用真实数字（star、下载）；没有就不提。
