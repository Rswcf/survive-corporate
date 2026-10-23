# 推广清单草稿（请你本人决定是否发布）

本文件只是标题与渠道草稿。**不要**由机器人代发帖或代提 PR。

## 一句话定位
把两千年帝王心术装进你的 AI 助手——68 条可执行法则，每条标明风险。

## 渠道与标题草稿

### Hacker News
- Show HN: SurviveCorporate – Han Feizi & Machiavelli as an AI agent skill for office politics
- 首段：Open-source Anthropic-style skill. Cold analysis, legal counters only. Sources cited.

### V2EX
- 标题：开源了个 Claude Skill：用法家/兵家典籍拆职场局（附风险等级）
- 节点：share / programmer

### 小红书 / 即刻
- 钩子：同事抢功时，韩非会怎么做？
- 钩子：AI 助手不鸡汤了，开始讲二柄与逆鳞
- 配图：README 金句截图 + GitHub 链接

### X / Twitter
- Thread：1) 定位语 2) 效果对话截断 3) 30 秒安装 4) 链接
- 标签：#Claude #AgentSkills #OfficePolitics

### awesome 列表
- 可考虑向 awesome-claude-skills / awesome-agent-skills 提交 PR
- PR 说明：category = workplace / productivity；附一句话描述
- **由仓库所有者本人提交**

### Reddit
- r/ClaudeAI r/LocalLLaMA r/productivity
- 避免过度营销口吻；强调 sources + risk controls

### 中文技术社区
- 少数派 / 即刻 / 知识星球：强调「反罗织识别」「合法硬招」

## 发布检查
- [ ] README 中英互链正常
- [ ] skill 路径 `skills/survivecorporate/SKILL.md` 可复制
- [ ] topics 已设置
- [ ] 免责声明可见
- [ ] 未编造 star / 用户数
- [ ] Validate workflow 在 main 上为绿色
- [ ] 上传社交预览图：Settings → General → Social preview（1280×640 PNG，建议：标题「把两千年帝王心术，装进你的 AI 助手」+ 英文副标题 + 一段真实输出截图）
- [ ] 录一段真实使用 GIF / 截图（真实对话，不摆拍），放进 README「效果展示」替换或补充文字示例
- [ ] 仓库 About 里填 Website（可填 README.en.md 链接）
- [ ] topics 建议追加：`claude-code`、`cursor`、`agent-skill`、`workplace`、`career-advice`；`awesome` 一般留给精选列表，可考虑去掉
- [ ] 打 tag（如 `v0.1.0`）并发布 GitHub Release，附 `survivecorporate.zip`，方便 Claude.ai 用户直接下载上传
- [ ] 在 Claude Code 中实测 `/plugin marketplace add Rswcf/survive-corporate`
- [ ] 在 Cursor 中实测 Customize → From GitHub Repository 导入（使用 `.cursor-plugin/marketplace.json`）
