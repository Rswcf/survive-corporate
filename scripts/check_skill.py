#!/usr/bin/env python3
"""Check SKILL.md frontmatter against the Agent Skills spec and keep counts in sync."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "survivecorporate"
errors = []

text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not match:
    sys.exit("SKILL.md: missing YAML frontmatter")
fields = dict(re.findall(r"^(\w[\w-]*): (.*)$", match.group(1), re.M))

name = fields.get("name", "")
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
    errors.append(f"name {name!r}: must be lowercase letters, digits and single hyphens, max 64 chars")
if name != SKILL_DIR.name:
    errors.append(f"name {name!r} must match folder name {SKILL_DIR.name!r}")
description = fields.get("description", "")
if not description or len(description) > 1024:
    errors.append(f"description: must be 1-1024 chars (got {len(description)})")
if re.search(r"[<>]", description):
    errors.append("description: must not contain angle brackets")

body_lines = text.count("\n") - match.group(0).count("\n")
if body_lines > 500:
    errors.append(f"SKILL.md body is {body_lines} lines; keep it under 500 and move detail to references/")

for ref in re.findall(r"\]\((references/[^)#]+)", text):
    if not (SKILL_DIR / ref).is_file():
        errors.append(f"SKILL.md links to missing file {ref}")

rules = (SKILL_DIR / "references" / "rules.md").read_text(encoding="utf-8")
rule_count = len(re.findall(r"^\*\*A\d+\.\d+", rules, re.M))
index_count = sum(
    len(re.findall(r"(?:^|· )\d+\.\d+", line.split("：", 1)[1]))
    for line in text.splitlines()
    if line.startswith("- **A") and "：" in line
)
if rule_count != index_count:
    errors.append(f"rules.md has {rule_count} rules but the SKILL.md index lists {index_count}")
for readme in ("README.md", "README.en.md"):
    if f"**{rule_count}**" not in (ROOT / readme).read_text(encoding="utf-8"):
        errors.append(f"{readme}: rule count **{rule_count}** not found")

if errors:
    print("\n".join(f"✘ {e}" for e in errors))
    sys.exit(1)
print(f"✔ {name}: description {len(description)} chars, body {body_lines} lines, {rule_count} rules")
