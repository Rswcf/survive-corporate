# SurviveCorporate

[中文](./README.md) · English

# Two thousand years of statecraft — packed into your AI assistant

**SurviveCorporate** is an open-source [Agent Skill](https://github.com/anthropics/skills) for Claude Code, Claude.ai, Cursor, and similar agents.  
No pep talks. It dissects workplace politics through Han Feizi, the *Six Secret Teachings*, Guiguzi, the *Arthashastra*, and *The Prince*, then returns **hard but legal** strategies — each with classical citations and a risk rating.

[![GitHub stars](https://img.shields.io/github/stars/Rswcf/survive-corporate?style=social)](https://github.com/Rswcf/survive-corporate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Skill](https://img.shields.io/badge/Anthropic-Agent%20Skill-black)](./skills/survivecorporate/SKILL.md)
[![Language](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87%20%7C%20English-blue)](./README.md)

> “Affairs succeed through secrecy and fail through leaks.” — *Han Feizi*, “The Difficulties of Persuasion”

---

## Demo

**User**: In the weekly meeting, coworker A presented my proposal as his own.

**SurviveCorporate** maps it to “stealing the two handles” (reward/punishment discourse), then returns an upper/mid/lower stratagem, three actions for today, sources, and blowback risk — e.g. same-day email with version history to redefine the narrative (low risk), instead of public humiliation (creates a permanent enemy).

Another common case: **coordinated complaints** → treat as a “frame-up / luozhi” pattern → separate interviews + fact pack to decision-makers first.

---

## Install in 30 seconds

### Claude Code
```bash
mkdir -p ~/.claude/skills
cp -r skills/survivecorporate ~/.claude/skills/
```

### Claude.ai
Zip `skills/survivecorporate/` and upload via the skill/project import UI.

### Cursor / other agents
Place `SKILL.md` where that product loads Agent Skills / rules. Keep the YAML `name` + `description` intact so the agent can auto-trigger.

```bash
git clone https://github.com/Rswcf/survive-corporate.git
```

---

## What’s inside

| Item | Detail |
|---|---|
| Rules | **68**, each with quote, workplace translation, risk level, mitigation |
| Themes | **10** (concealment, power, loyalty tests, persuasion, alliances, intel, anti-frame, flattery detection, authority, exit) |
| Opponent playbook | **18** common office moves |
| Sources | **14+** classics across China, India, Europe |
| Research | See [`research/`](./research/) |

---

## Why star

1. Usable as a real Agent Skill, not a quote dump.  
2. Citations checked against Wikisource / standard translations; forgeries labeled.  
3. Built-in brakes: legal counters only; inquisitorial & frame-up materials for **defense**.  
4. Bilingual docs ready for awesome-lists.  
5. PRs welcome — see [CONTRIBUTING.md](./CONTRIBUTING.md).

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Rswcf/survive-corporate&type=Date)](https://star-history.com/#Rswcf/survive-corporate&Date)

---

## Disclaimer

Historical and strategic research plus AI skill engineering. The skill proposes **lawful** responses only (documentation, narrative control, alliances, HR/legal channels). No guidance on fabricating evidence, false accusations, harassment, privacy intrusion, or discrimination. Dark techniques from the classics are for recognition and defense.

## License

MIT for code and skill. Cite classical sources when you quote them.

---

If this saves you from one political ambush — star the repo so more agents learn to judge interests before loyalty.
