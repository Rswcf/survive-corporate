<div align="center">

# SurviveCorporate

**Two thousand years of statecraft, packed into your AI assistant.**

A coworker takes credit for your work. You get blamed for a slipped deadline. Your reports get quietly moved to someone else. Ask a generic AI and you mostly hear "communicate openly and stay positive."  
SurviveCorporate turns it into a seasoned mentor who has read Han Feizi: it weighs whose interests are at stake, then calmly walks you through **hard but legal** options, telling you which classic each one comes from and where it could backfire.

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

**SurviveCorporate** (excerpt from the English example in [`references/examples.md`](./skills/survivecorporate/references/examples.md); real answers vary by model and context):

> I've seen this one many times. Before you say anything in the team chat, take a breath.
>
> What he's really taking isn't just this proposal; it's the right to say whose work it was. Han Feizi opens his chapter "The Two Handles" with 二柄者，刑德也 — "the two handles are punishment and reward." Whoever controls how work gets judged is holding one of those handles. You're exposed right now not because you can't speak up, but because there's no written trail.
>
> The safest move is to create that trail today. Send a short follow-up to everyone who was in the meeting and to your manager: "Following up on the proposal we discussed — I've attached versions 1 through 3 and the numbers behind them. Happy to walk through the rollout next week." State facts and leave his name out entirely. There's almost no risk here; it just looks thorough.
>
> If he keeps presenting it, you can add calmly at the next meeting, "I ran those numbers — let me add two points." That's a little riskier because it's face to face; if your tone slips, it sounds like you're grabbing the mic. …
>
> Three things to do today: write down the timeline from the first draft to now, send that follow-up email, and ask a colleague from another team who has seen your work to attend the next review.
>
> One last thing: don't call him out in public. You'd win one meeting and gain someone who remembers it for years. Han Feizi understood the dangers of speaking up better than anyone, and he still died after his former classmate Li Si framed him.

No tables, no scores. It talks you through the situation the way a well-read senior colleague would: what's really going on, three ways forward, where each one can go wrong, and what to do today. Another common case is **three similar complaints in one week**. It will point out that this resembles the *luozhi* frame-ups of Tang-dynasty secret police, help you ask for a proper process and get your timeline to the decision-maker first, and talk you out of counter-accusations or digging into anyone's private life.

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
| Rules | **68** (the twelve "civil offensive" moves count as one), each with its source, how it plays out at work and how risky it is; most include how to avoid the trap |
| Themes | **10**: concealment, power, reading people & loyalty tests, persuasion, alliances, intelligence, anti-frame-up, flattery & sabotage detection, authority, exit |
| Opponent playbook | **18** common office moves → classical name → first counter |
| Worked examples | **6**: credit theft, being sidelined, blame-shifting, coordinated complaints, parachuted boss, insubordinate report |
| Blowback cases | Shang Yang, Wu Qi, Han Feizi, Li Si, Wen Zhong, Lai Junchen, Zhou Xing: how each move bit back |
| Research | [`research/`](./research/): Chinese classics overview + global "dark manuals" with forgeries flagged |

### How it differs from a "dark wisdom" quote dump

| | Quote collections | SurviveCorporate |
|---|---|---|
| Form | A pile of aphorisms | A well-read mentor who talks your situation through |
| Gives you | An attitude | Three ways forward + three things to do today + words you can use as-is |
| Risk | Not mentioned | For every option: where it can go wrong, how to guard against it, when to stop |
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
├── SKILL.md              # Core: scope, reasoning steps, answer voice, opponent playbook, rule index
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
