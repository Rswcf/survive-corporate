# 贡献指南 / Contributing

感谢你愿意让 SurviveCorporate 更锋利、也更负责。

*English summary: PRs for new rules (with a verifiable source), anonymized cases, citation fixes and translations are welcome. Never submit instructions for fabricated evidence, false accusations, harassment, privacy intrusion or discrimination, and never submit unverifiable "ancient quotes" or made-up metrics. Run `python3 scripts/check_skill.py` before opening a PR.*

## 可提交什么

1. **新法则**：必须带来源典籍 + 篇章 + 可核对原文（维基文库、通行点校本、可靠英译均可）。
2. **新职场案例**：匿名化后的情形 + 你建议的上中下策 + 对应法则编号。
3. **原文勘误**：指出引文错误并给出正确出处链接。
4. **多语言 README / 译文**。

## 不可提交什么

- 伪造证据、诬告、骚扰恐吓、侵入账户/隐私、歧视、报复举报人的可操作教程
- 毒药、武器、酷刑步骤
- 无法核实出处的「古书金句」
- 编造的 star 数、用户评价、效果数据

## 文件在哪

| 改什么 | 文件 |
|---|---|
| 法则全文 | `skills/survivecorporate/references/rules.md` |
| 法则索引、对手手段谱系、流程、模板 | `skills/survivecorporate/SKILL.md` |
| 示例 | `skills/survivecorporate/references/examples.md` |
| 反噬史例 | `skills/survivecorporate/references/history.md` |
| 核实说明 | `skills/survivecorporate/references/sources.md` |
| 典籍研究 | `research/` |

新增法则时，同时在 `SKILL.md` 的法则索引里加一行，并更新两份 README 中的法则数量。

### 仓库结构

```text
skills/survivecorporate/
├── SKILL.md              # 核心：范围、思考流程、回答语气、对手手段谱系、法则索引
└── references/
    ├── rules.md          # 附录A：68 条法则全文
    ├── history.md        # 附录C：反噬史例与风险规律
    ├── examples.md       # 附录D：完整示例回答
    └── sources.md        # 附录E：原文核实说明
.claude-plugin/           # Claude Code 插件与市场清单
.cursor-plugin/           # Cursor 插件与市场清单
assets/                   # 社交预览图与分享卡片（由 scripts/render_assets.py 生成）
research/                 # 典籍研究笔记
```

`SKILL.md` 只放每次都要用的内容，法则全文放在 `references/` 里按需加载，节省上下文。

### 分享卡片

`assets/` 里的图片由 `python3 scripts/render_assets.py` 生成（需要 Chrome/Chromium 与 Noto CJK 字体）。卡片上的文字必须逐字摘自 `references/examples.md`，不要另写「用户评价」或效果数据。

## 提交流程

1. Fork → 新建分支
2. 按上表修改对应文件
3. 本地运行 `python3 scripts/check_skill.py`（检查 frontmatter、引用文件与法则数量是否一致）
4. 打开 PR，说明：改了哪条、原文出处 URL、风险等级建议
5. 也可以先用 [Issue 模板](https://github.com/Rswcf/survive-corporate/issues/new/choose) 讨论

## 原文规范

- 优先繁简与底本保持一致，并注明版本
- 拿不准写【待核】，不要硬写成引号原文
- 伪书必须标明伪书（如今本《罗织经》、Monita Secreta、锡安议定书）
