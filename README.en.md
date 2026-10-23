<div align="center">

# SurviveCorporate

**Two thousand years of statecraft, packed into your AI assistant.**

A coworker takes credit for your work. You get blamed for a slipped deadline. Your reports get quietly moved to someone else. Ask a generic AI and you mostly hear "communicate openly and stay positive."  
SurviveCorporate makes it weigh interests the way Han Feizi would, then return **hard but legal** upper / middle / lower strategies, each with a classical source and a risk rating.

[![GitHub stars](https://img.shields.io/github/stars/Rswcf/survive-corporate?style=social)](https://github.com/Rswcf/survive-corporate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Claude%20Code%20%7C%20Claude.ai%20%7C%20Cursor-black)](./skills/survivecorporate/SKILL.md)
[![Validate](https://github.com/Rswcf/survive-corporate/actions/workflows/validate.yml/badge.svg)](https://github.com/Rswcf/survive-corporate/actions/workflows/validate.yml)

[中文](./README.md) · **English**

</div>

> "Affairs succeed through secrecy and fail through leaks." — *Han Feizi*, "The Difficulties of Persuasion"  
> Until a plan lands, the fewer people who know, the better.

## Contents

- [Demo](#demo)
- [Install in 30 seconds](#install-in-30-seconds)
- [How to use it](#how-to-use-it)
- [What's inside](#whats-inside)
- [Hard limits](#hard-limits)
- [Sources](#sources)
- [Repository layout](#repository-layout)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer) · [License](#license)

---

## Demo

**You**: In the weekly meeting, coworker A presented my proposal as his own.

**SurviveCorporate** (illustrative output adapted from example 1 in [`references/examples.md`](./skills/survivecorporate/references/examples.md); real answers vary by model and context):

```text
Situation        A is seizing the power to evaluate (the "reward" handle of Han Feizi's two handles).
                 Your weak point: no written trail.
Opponent's play  Stealing the two handles + withholding information
Risk assessment  Calling A out publicly: medium exposure, makes a permanent enemy.
                 Written follow-up: low exposure.
Upper strategy   Same-day email to stakeholders with V1–V3 and the data: "I'll walk through
                 rollout next week." | Risk: low | Mitigation: state facts, never write "A stole it"
Middle strategy  At the next meeting: "I ran the numbers — two additions." | Risk: medium
Lower strategy   Agree on attribution rules with A privately | Risk: medium (promises are cheap)
Three moves today 1. Build a timeline  2. Send the cc email  3. Line up a cross-team witness for next review
Sources          Han Feizi, "The Two Handles": 二柄者，刑德也 ("the two handles are punishment and reward")
Blowback         Han Feizi understood persuasion and still died framed. Humiliating A = a lifelong enemy.
```

Another common case: **three similar complaints in one week** → flagged as a *luozhi* (coordinated frame-up) pattern → ask for separate interviews and get a timeline plus original records to the decision-maker first. No counter-accusations, no digging into complainants' private lives.

Ask in English and the skill answers in English; classical quotes stay in Chinese with a translation.

---

## Install in 30 seconds

### Claude Code (recommended: plugin marketplace)

Inside Claude Code:

```text
/plugin marketplace add Rswcf/survive-corporate
/plugin install survivecorporate@survive-corporate
```

### Claude Code (manual copy)

```bash
git clone https://github.com/Rswcf/survive-corporate.git
mkdir -p ~/.claude/skills
cp -r survive-corporate/skills/survivecorporate ~/.claude/skills/
```

Start a new session and describe your situation.

### Claude.ai

1. Zip the skill folder (the zip must contain the `survivecorporate/` folder at its root):

   ```bash
   git clone https://github.com/Rswcf/survive-corporate.git
   cd survive-corporate/skills && zip -r ../survivecorporate.zip survivecorporate
   ```

2. Make sure **Settings → Capabilities → Code execution and file creation** is on (skills need it).
3. Go to **Customize → Skills**, click **+** → *Create skill* → *Upload a skill*, and upload `survivecorporate.zip`.
4. In a new chat: "A coworker took credit for my work — analyze it with SurviveCorporate."

### Cursor

```bash
git clone https://github.com/Rswcf/survive-corporate.git
mkdir -p ~/.cursor/skills
cp -r survive-corporate/skills/survivecorporate ~/.cursor/skills/
```

Cursor also reads `~/.claude/skills/`, so a Claude Code install already works. For a project-level install, use `.cursor/skills/` inside the repo. Check **Customize → Skills** to confirm it loaded, or type `/survivecorporate` in Agent to invoke it manually.

### Other Agent Skills–compatible tools

Copy the whole `skills/survivecorporate/` folder (including `references/`) into the tool's skills directory, e.g. `~/.agents/skills/`. Copying only `SKILL.md` is not enough: the full rule text lives in `references/`.

---

## How to use it

No commands to memorize. Describe the situation as you would to an advisor. Some openers to copy:

- "A new director was parachuted in with two of his old reports, and my projects are slowly being taken away."
- "The project slipped and the PM told everyone they were waiting on me, but requirements were only signed off last week."
- "A senior report goes over my head to my boss and quietly ignores my instructions."
- "HR wants to meet about 'several complaints' and asked me to write a statement first."
- "My boss praised me in front of everyone, then handed me the project nobody wants. What's the play?"

Tip: say **your level and reporting line, who the other party is, what written records exist, and what outcome you want**. If something key is missing, the skill asks up to three questions first.

> About the "lower strategy": here it means the **exit plan** (cut losses, transfer, negotiate a departure), not "the worst move."

---

## What's inside

| Item | Detail |
|---|---|
| Rules | **68** (the twelve "civil offensive" moves count as one), each with source, workplace translation and risk level; most include mitigation |
| Themes | **10**: concealment, power, reading people & loyalty tests, persuasion, alliances, intelligence, anti-frame-up, flattery & sabotage detection, authority, exit |
| Opponent playbook | **18** common office moves → classical name → first counter |
| Worked examples | **6**: credit theft, being sidelined, blame-shifting, coordinated complaints, parachuted boss, insubordinate report |
| Blowback cases | Shang Yang, Wu Qi, Han Feizi, Li Si, Wen Zhong, Lai Junchen, Zhou Xing: how each move bit back |
| Research | [`research/`](./research/): Chinese classics overview + global "dark manuals" with forgeries flagged |

### How it differs from a "dark wisdom" quote dump

| | Quote collections | SurviveCorporate |
|---|---|---|
| Form | A pile of aphorisms | An Agent Skill: fixed workflow + output template |
| Gives you | An attitude | Three strategies + three moves for today + wording |
| Risk | Not mentioned | Exposure odds, consequences, deniability, exit trigger for every option |
| Sources | Often misattributed | Key quotes checked against Wikisource / standard translations; uncertain ones marked; forgeries flagged |
| Limits | None | Legal moves only; dark texts used for recognition and defense |

---

## Hard limits

No fabricated evidence, false accusations, harassment or intimidation, account intrusion or snooping, discrimination, or retaliation against whistleblowers. When asked for these, the skill substitutes an equally effective legal move: paper trail, framing the narrative first, alliances, pulling decisions upward, HR or legal channels. For harassment, discrimination, unpaid wages or workplace injury, it tells you to preserve evidence and talk to a labor authority or lawyer.

The frame-up archives and inquisitors' manuals are used only to **recognize and counter** frame-ups aimed at you.

---

## Sources

- **China**: *Han Feizi*, *Book of Lord Shang*, *Six Secret Teachings* ("Civil Offensive"), *Guiguzi*, *Records of the Grand Historian*, *Zizhi Tongjian*, and Tang-dynasty records of Lai Junchen's frame-ups (the modern "Luo Zhi Jing" is a forgery and is labeled as such)
- **India**: *Arthashastra* on spies and the four loyalty tests (no poison recipes)
- **Europe**: core chapters of *The Prince*; Eymerich and Bernard Gui's inquisitors' manuals (only to recognize leading interrogation); Mazarin's *Breviarium* (attribution disputed)
- **Forgeries flagged**: the modern *Luo Zhi Jing*, *Monita Secreta*, *Protocols of the Elders of Zion*: documented as harms, never recommended

Verification notes: [`references/sources.md`](./skills/survivecorporate/references/sources.md). Full research: [`research/`](./research/) (Chinese).

---

## Repository layout

```text
skills/survivecorporate/
├── SKILL.md              # Core: scope, workflow, output template, opponent playbook, rule index
└── references/
    ├── rules.md          # Appendix A: all 68 rules
    ├── history.md        # Appendix C: blowback cases and risk patterns
    ├── examples.md       # Appendix D: 6 worked examples
    └── sources.md        # Appendix E: citation verification notes
.claude-plugin/           # Claude Code plugin + marketplace manifests
.cursor-plugin/           # Cursor plugin + marketplace manifests
research/                 # Research on the source texts
docs/LAUNCH.md            # Launch copy drafts (never auto-posted)
```

`SKILL.md` holds only what every run needs; the full rule text loads on demand to save context.

---

## Contributing

New rules (with verifiable original text), anonymized workplace cases, citation fixes and translations are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) or open an [issue](https://github.com/Rswcf/survive-corporate/issues/new/choose).

Anonymize scenarios completely — no real names, companies or teams. Issues are public.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Rswcf/survive-corporate&type=Date)](https://star-history.com/#Rswcf/survive-corporate&Date)

---

## Disclaimer

Historical and strategic research plus AI skill engineering; not legal or HR advice. The skill proposes **lawful** responses only (documentation, narrative, alliances, HR/legal channels). Follow your local law and company policy. Dark techniques from the classics are for recognition and defense, not for harming others.

## License

[MIT](./LICENSE). Cite classical sources when you quote them.

---

<div align="center">

If this saves you from one political ambush, star the repo so more AI assistants learn to weigh interests before loyalty.

</div>
