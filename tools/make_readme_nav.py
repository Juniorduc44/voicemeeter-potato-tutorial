#!/usr/bin/env python3
"""Rewrite the newcomer part of README.md (between the README-NAV markers) from
flipbook/pages.js, so page numbers and titles always match the built SOP.
Run after make_flipbook.py (build_pdf.sh does)."""
import json, re
from pathlib import Path
root = Path(__file__).resolve().parent.parent
pages = json.loads(re.search(r'=\s*(\[.*\]);', (root / 'flipbook/pages.js').read_text(), re.S).group(1))
T = {p['n']: p['title'] for p in pages}
N = len(pages)
FB = 'https://juniorduc44.github.io/voicemeeter-potato-tutorial/'
def find(prefix):
    return next(n for n, t in T.items() if t.startswith(prefix))
def prev(n): return f'images/page-previews/page-{n:02d}.png'
def flip(n): return f'{FB}#page={n}'
def L(n): return f'[{n}]({flip(n)})'            # markdown: the page number itself is the link
def A(n): return f'<a href="{flip(n)}">{n}</a>'  # same, for HTML blocks
quick = [
 ('🚀', 'Start here - the one idea', 'What Potato does, in one picture: A = your ears, B = other people.', find('The one idea')),
 ('⬇️', 'Install (Steps 1-2)', 'Download from the official site, install, restart.', find('Step 1')),
 ('🎧', 'Set up sound (Steps 3-6)', 'Headphones on A1, mic on Input 1, Windows defaults, golden routing.', find('Step 3')),
 ('🔀', 'Route your apps (Ways 1-3)', 'Discord, Zoom, OBS, games - three ways to split them.', find('Way 1')),
 ('🗺️', 'Mixer map', 'The whole Potato window split into 7 numbered sections.', find('Know Your Mixer')),
 ('🎛️', 'Top bar and Menu', 'Menu item by item, VBAN, Audio Map.', find('Section 1 - Top bar: what')),
 ('🎤', 'Hardware inputs (mics)', 'INTELLIPAN, EQ, Comp / Gate / Denoiser, sends, fader.', find('Section 2 - Hardware inputs: what')),
 ('💻', 'Virtual inputs (computer sound)', 'VAIO, AUX, VAIO3, app list, M.C and K.', find('Section 3 - Virtual inputs: what')),
 ('🔊', 'Hardware Out A1-A5', 'Picking your headphones and speakers.', find('Section 4 - Hardware Out: what')),
 ('📼', 'Cassette recorder', 'Record and play back, Recorder Options.', find('Section 5 - Cassette recorder: what')),
 ('✨', 'Special FX', 'Reverb and Delay panels, External FX.', find('Section 6 - Special FX: what')),
 ('🎚️', 'Master section', 'All 8 outputs, SEL, bus modes, bus EQ.', find('Section 7 - Master section: what')),
 ('⌨️', 'Mouse and keyboard cheat sheet', 'Every click trick and Ctrl shortcut on one page.', find('Cheat sheet')),
 ('🆘', 'No sound? checklist', 'Check in this order - most problems die at 1, 2 or 3.', find('No-sound')),
 ('📋', 'Quick reference card', 'Print it and keep it by the computer.', find('Quick reference')),
]
o = []
o.append(f'''<p align="center">
  <a href="{FB}"><img src="images/page-previews/page-01.png" width="380" alt="Cover of the SOP - click to flip through it"></a>
</p>

<h2 align="center"><a href="{FB}">📖 Click Here to Flip Through</a></h2>
<p align="center"><sub>Opens the interactive flipbook: turn the pages right there with the big arrows, your ← → keys or a swipe. Nothing to download.</sub></p>

<h3 align="center">Learn VoiceMeeter Potato on Windows - one click at a time.</h3>
<p align="center">{N} illustrated pages · real screenshots · every button explained · nothing to install to read it</p>

<p align="center">
  <a href="{FB}"><b>📖 Open the interactive flipbook</b></a> &nbsp;·&nbsp;
  <a href="handout/voicemeeter-potato-sop.pdf"><b>⬇️ Download the PDF</b></a> &nbsp;·&nbsp;
  <a href="#browse-every-page">🖼️ Browse every page below</a>
</p>

> **New here?** Read page {L(find("The one idea"))} (*the one idea*), then do Steps 1-6 in order (pages {L(find("Step 1"))}-{L(find("Step 6"))}).
> Each step is one page with a picture and a green **CHECK** box - tick it before you turn the page.
> Stuck with no sound? Jump straight to the [No-sound checklist]({flip(find("No-sound"))}) (page {L(find("No-sound"))}).
> *Every page number in this README is a link - click it to open that page in the flipbook.*
''')
o.append('## 🧭 Quick navigation\n')
o.append('| | Go to | What you get | Page | Open |\n| --- | --- | --- | :-: | --- |')
for ic, name, what, n in quick:
    o.append(f'| {ic} | **[{name}]({prev(n)})** | {what} | {L(n)} | [picture]({prev(n)}) · [flipbook]({flip(n)}) |')
o.append(f'\n*"picture" opens that page right here on GitHub; "flipbook" opens it in the page-turner. The full contents list is on page {L(find("Contents"))}.*\n')
o.append('<a id="browse-every-page"></a>\n\n## 🖼️ Browse every page\n\nClick a group to open it, then click any page to see it full size. No download needed.\n')
groups = []
for p in pages:
    if not groups or groups[-1][0] != p['group']: groups.append((p['group'], []))
    groups[-1][1].append(p)
# split Part 2 by section for easier browsing
out = []
for g, ps in groups:
    if g.startswith('Part 2'):
        cur = None
        for p in ps:
            m = re.match(r'(Section \d)', p['title'])
            key = m.group(1) if m else ('Mixer map' if p['title'].startswith('Know') else 'Cheat sheet')
            if cur is None or cur[0] != key: cur = (key, []); out.append(('Part 2 - ' + key, cur[1]))
            cur[1].append(p)
    else:
        out.append((g, ps))
names = {'Section 1': 'Top bar and Menu', 'Section 2': 'Hardware inputs', 'Section 3': 'Virtual inputs', 'Section 4': 'Hardware Out A1-A5',
         'Section 5': 'Cassette recorder', 'Section 6': 'Special FX', 'Section 7': 'Master section'}
for g, ps in out:
    label = g
    for k, v in names.items():
        if g.endswith(k): label = f'{g} - {v}'
    rng = f'page {A(ps[0]["n"])}' if len(ps) == 1 else f'pages {A(ps[0]["n"])}-{A(ps[-1]["n"])}'
    o.append(f'<details>\n<summary><b>{label}</b> ({rng})</summary>\n<br>\n')
    o.append('<table>')
    for i in range(0, len(ps), 4):
        row = ps[i:i+4]
        o.append('<tr>' + ''.join(f'<td align="center" valign="top" width="25%"><a href="{prev(p["n"])}"><img src="images/page-thumbs/page-{p["n"]:02d}.jpg" width="150" alt="Page {p["n"]}: {p["title"]}"></a><br><sub><b>{A(p["n"])}</b> · {p["title"]}</sub></td>' for p in row) + '</tr>')
    o.append('</table>\n</details>\n')
o.append(f'''## 📖 The flipbook

[`index.html`](index.html) is a page-turner for the whole SOP: single page or two-page spread,
big ⬅️ ➡️ arrows beside the page, Prev / Next buttons, ← → keys, swipe on phones, click the page edges, a contents sidebar with
thumbnails, a jump-to-page menu, zoom, light / dark mode and a Download PDF button.
Deep links work: [`{FB}#page={find("Know Your Mixer")}`]({flip(find("Know Your Mixer"))}) opens the mixer map (page {L(find("Know Your Mixer"))}); add `?view=spread` for the two-page view.

It is a plain static page (no build step) that shows the page pictures in `images/page-previews/`.
It is live at **<{FB}>** (GitHub Pages: *Deploy from a branch* → `main` / `/ (root)`). To try it locally:
`python3 -m http.server` in the repo folder, then open <http://localhost:8000/>.
''')
block = '\n'.join(o)
r = (root / 'README.md').read_text()
a, b = '<!-- README-NAV:START (generated by tools/make_readme_nav.py) -->', '<!-- README-NAV:END -->'
if a in r:
    r = r[:r.index(a)] + a + '\n' + block + '\n' + r[r.index(b):]
else:
    i = r.index('\n', r.index('# ')) + 1
    r = r[:i] + '\n' + a + '\n' + block + '\n' + b + '\n' + r[i:]
(root / 'README.md').write_text(r)
print('README nav written,', len(quick), 'quick links,', len(out), 'groups')
