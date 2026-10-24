#!/usr/bin/env python3
"""Render the social preview and cards in assets/ with headless Chrome.

Card text must be quoted verbatim from skills/survivecorporate/references/examples.md.
Requires google-chrome (or chromium) and the Noto Serif/Sans CJK fonts.
Usage: python3 scripts/render_assets.py
"""

import html
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
REPO = "github.com/Rswcf/survive-corporate"

STYLE = """
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: %(w)dpx; height: %(h)dpx; overflow: hidden; }
body {
  background: #17140f;
  background-image: radial-gradient(circle at 85%% 10%%, #2a241b 0, transparent 55%%);
  color: #efe6d2;
  font-family: "Noto Serif CJK SC", "Noto Serif", serif;
  padding: %(pad)dpx;
  display: flex; flex-direction: column;
}
.seal {
  width: %(seal)dpx; height: %(seal)dpx; background: #a8261c; color: #f6ead6;
  display: flex; align-items: center; justify-content: center; text-align: center;
  font-weight: 700; font-size: %(sealfont)dpx; line-height: 1.05; border-radius: 6px;
  flex-shrink: 0;
}
.kicker { color: #c9a66b; font-family: "Noto Sans CJK SC", sans-serif; letter-spacing: 2px; }
.sans { font-family: "Noto Sans CJK SC", "Noto Sans", sans-serif; }
.muted { color: #9d927c; }
.rule { height: 2px; background: #3a3226; margin: 0; }
"""


def page(width, height, body, pad=80, seal=96, sealfont=34):
    css = STYLE % dict(w=width, h=height, pad=pad, seal=seal, sealfont=sealfont)
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


def social_preview():
    body = f"""
<div style="display:flex; gap:44px; align-items:center;">
  <div class="seal">職場<br>軍師</div>
  <div>
    <div style="font-size:64px; font-weight:700; letter-spacing:1px;">SurviveCorporate</div>
    <div class="kicker" style="font-size:24px; margin-top:6px;">AGENT SKILL · CLAUDE CODE · CLAUDE.AI · CURSOR</div>
  </div>
</div>
<div style="margin-top:56px; font-size:50px; font-weight:700; line-height:1.35;">把两千年帝王心术，装进你的 AI 助手</div>
<div style="margin-top:18px; font-size:30px; line-height:1.5;">被抢功、被甩锅、被架空时，它像一位读过韩非子的前辈，<br>心平气和地讲出合法又管用的应对。</div>
<div class="sans muted" style="margin-top:22px; font-size:27px; line-height:1.45;">A calm AI mentor for office politics: legal moves from Han Feizi, Guiguzi and Machiavelli.</div>
<div style="flex:1"></div>
<div class="sans muted" style="font-size:24px;">{REPO}</div>
"""
    return page(1280, 640, body, pad=72)


def card(scene, lines, quote, source, lang="zh"):
    label = "示例回答节选 · 实际回答因模型与上下文而异" if lang == "zh" else "Excerpt from an example answer · real answers vary"
    you = "你" if lang == "zh" else "You"
    lines_html = "".join(f"<p style='margin-bottom:34px;'>{html.escape(l)}</p>" for l in lines)
    body = f"""
<div style="display:flex; gap:28px; align-items:center;">
  <div class="seal">職場<br>軍師</div>
  <div>
    <div style="font-size:44px; font-weight:700;">SurviveCorporate</div>
    <div class="kicker" style="font-size:22px; margin-top:4px;">{"一位读过古书的 AI 前辈" if lang == "zh" else "A WELL-READ AI MENTOR"}</div>
  </div>
</div>
<div class="sans" style="margin-top:80px; font-size:32px; color:#c9a66b;">{you}</div>
<div style="margin-top:14px; font-size:46px; line-height:1.5; font-weight:700;">{html.escape(scene)}</div>
<div class="rule" style="margin:60px 0;"></div>
<div style="font-size:44px; line-height:1.7;">{lines_html}</div>
<div style="flex:1"></div>
<div style="border-left:6px solid #a8261c; padding-left:28px; margin-bottom:56px;">
  <div style="font-size:40px; font-weight:700; color:#e7d3a8;">{html.escape(quote)}</div>
  <div class="sans muted" style="font-size:26px; margin-top:10px;">{html.escape(source)}</div>
</div>
<div class="sans muted" style="font-size:24px; line-height:1.6;">{label}<br>{REPO}</div>
"""
    return page(1080, 1440, body, pad=90)


def icon():
    body = '<div class="seal" style="width:512px; height:512px; font-size:176px; border-radius:0;">職場<br>軍師</div>'
    return page(512, 512, body, pad=0)


ASSETS = {
    "icon.png": (512, 512, icon()),
    "social-preview.png": (1280, 640, social_preview()),
    "cards/credit-theft.png": (1080, 1440, card(
        "周会上，同事把我做的方案当成他的成果汇报了。",
        [
            "最稳的一步，是今天之内把痕迹补上。只摆事实，一个字都别提 A。",
            "千万别当众揭穿他。你赢了一场会，却会多一个记你很多年的人。",
        ],
        "「二柄者，刑德也。」", "《韩非子·二柄》",
    )),
    "cards/sidelined.png": (1080, 1440, card(
        "汇报线被改到了副手那里，头衔没变，但事情一件件不经过我了。",
        [
            "头衔还在、实权在走，这是最常见也最容易被忽视的一种架空。",
            "你要盯的不是名分，而是那些离了你就转不动的东西。",
        ],
        "「权轻而臣重者，可亡也。」", "《韩非子·亡征》",
    )),
    "cards/blame.png": (1080, 1440, card(
        "项目延期了，主导方在会上说一直在等我的交付，可需求上周才确认。",
        [
            "被甩锅时最怕的是急着辩解，越辩越像心虚。好在这种事，靠的从来不是嘴，而是记录。",
            "你要的是把锅放回原处，不是再结一个仇。",
        ],
        "「言已应，则执其契；事已增，则操其符。」", "《韩非子·主道》",
    )),
    "cards/complaints.png": (1080, 1440, card(
        "一周里有三个人陆续投诉我，说法都差不多。HR 让我先写份情况说明。",
        [
            "先深呼吸。一周之内三份口径相近的投诉，这本身就值得留意。",
            "你可以配合，但请对方先给出书面问题，再书面作答，不当场签任何东西。",
        ],
        "「请兄入此瓮。」", "《资治通鉴》",
    )),
    "cards/credit-theft-en.png": (1080, 1440, card(
        "In the weekly meeting, a coworker presented my proposal as his own.",
        [
            "State facts and leave his name out entirely. There's almost no risk here; it just looks thorough.",
            "Don't call him out in public. You'd win one meeting and gain someone who remembers it for years.",
        ],
        "二柄者，刑德也", "\"The two handles are punishment and reward.\" — Han Feizi",
        lang="en",
    )),
}


def main():
    chrome = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    if not chrome:
        raise SystemExit("google-chrome or chromium is required")
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        for name, (w, h, doc) in ASSETS.items():
            src = Path(tmp) / (name.replace("/", "_") + ".html")
            src.write_text(doc, encoding="utf-8")
            dest = OUT / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.unlink(missing_ok=True)
            # Some headless Chrome builds write the screenshot but never exit, so stop it ourselves.
            proc = subprocess.Popen(
                [chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                 f"--user-data-dir={tmp}/profile", f"--window-size={w},{h}",
                 f"--screenshot={dest}", src.as_uri()],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            for _ in range(120):
                if proc.poll() is not None or (dest.exists() and dest.stat().st_size > 0):
                    break
                time.sleep(0.5)
            time.sleep(1)
            proc.kill()
            proc.wait()
            if not dest.exists():
                raise SystemExit(f"failed to render {name}")
            print(f"wrote {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
