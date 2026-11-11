# VoiceMeeter Potato Tutorial — GrandMa Proof

Training material for teaching **VoiceMeeter Potato** on Windows to complete beginners.

**GrandMa Proof rule:** ridiculously easy, anyone can do it. That means a screenshot
for every direction — and when a step names a specific button, the picture in the
tutorial *is* that button, cropped from a screenshot of the real screen, so what
trainees see in print matches exactly what they see on their PC.

## What the training covers

1. Download VoiceMeeter Potato from the only official source (vb-audio.com) and
   install it as administrator, then restart Windows.
2. Set A1 (headphones/speakers) first, then the microphone on Hardware Input 1.
3. Make VoiceMeeter the Windows default input and output
   (Win+R → `mmsys.cpl` → Playback: **Voicemeeter Input (VB-Audio Voicemeeter VAIO)**;
   Recording: **Voicemeeter Output (VB-Audio Voicemeeter VAIO)**).
4. The beginner's golden routing — mic: **B1 on / A1 off**; computer sound: **A1 on**.
   (A = Actual ears, for you. B = Broadcast, for other people.)
5. The three ways to configure inputs/outputs, in teaching order:
   everything together (Windows default), split apps per-app in the Windows
   Volume mixer (VAIO / Aux / VAIO3), and setting devices inside an app
   (Discord / Zoom / OBS).
6. **Part 2 — Know Your Mixer** (pages 13–27): a section-by-section tour of the whole
   Potato window, in screen order — (1) top bar, (2) hardware inputs 1–5, (3) virtual
   inputs VAIO / AUX / VAIO3, (4) Hardware Out A1–A5, (5) cassette recorder,
   (6) Special FX + External FX Return, (7) Master section (A1–A5 physical,
   B1–B3 virtual). Each section: an annotated picture with numbered callouts, a
   "number / control / what it does" table, real-world examples (Discord gaming,
   Zoom/Teams training, OBS streaming, podcast recording), a *Try it now* exercise,
   a STOP box and a CHECK box. Every explanation is sourced from the official manual
   (see `source/OUTLINE.md`).

## Repository layout

| Folder | Contents |
| --- | --- |
| `handout/` | The printable PDF handout, built from `source/`. Earlier versions are kept as git tags (`v1`, `v2`, `v3`), not as files. |
| `docs/` | `ERROR_CHECK.md` — the v2 handout checked claim-by-claim against the official Potato 3.1.3.0 manual: what was verified, the four v3 fixes, and what still needs a real Windows PC. |
| `images/source-screenshots/` | Full original screenshots the handout pictures were taken from. |
| `images/button-crops/` | Tight crops of the very buttons the steps reference (A1, Set Default, OK, Menu, strip A1/B1 columns, …), plus the annotated Sound dialog. |
| `images/manual-figures/` | Official figures extracted unchanged from the VB-Audio *Voicemeeter Potato 3.1.3.0* user manual, plus `SOURCES.md` (manual page + figure for each, and what each crop is cut from). |
| `images/section-crops/` | The numbered "Know Your Mixer" crops (overview map + one or two per section), generated from `manual-figures/`. |
| `images/page-previews/` | A PNG render of every handout page (current version, 150 dpi). |
| `tools/` | `make_section_crops.py` (cuts + numbers the section crops; every crop box and callout position lives here) and `build_pdf.sh` (renders the PDF with headless Chrome and refreshes the page previews). |
| `source/` | The single working build source: `index.html` (the handout) and `OUTLINE.md` (claim-by-claim outline with sources and edit log). Started from v3. Part 2 pictures are linked from `../images/section-crops/` (Part 1 pictures are still embedded). |

## Building

```
python3 tools/make_section_crops.py   # only if figures or callouts changed
./tools/build_pdf.sh                  # PDF + page previews
```

## Status / known limitations

- **Error-checked 2026-11-04** against the official Voicemeeter Potato 3.1.3.0
  user manual — see `docs/ERROR_CHECK.md` (four fixes landed in v3).
  **Not yet trainee-tested, and never run live on a real Windows PC** — that
  run-through is still the next step before using this with a real class.
- The VoiceMeeter Potato pictures and the Windows Sound dialog are real
  screenshots. Steps 1–2 (download ZIP, Extract All / Run as administrator /
  Install) are still labelled diagrams — no trustworthy real screenshot of the
  installer / right-click menu has been sourced yet. Swapping those in from a
  real Windows PC run-through is the gold version.
- `images/button-crops/btn-input1-header.png` is a little soft: its only real
  source is a 900px-wide screenshot. A larger original would improve it.

- **Part 2 (Know Your Mixer) pictures are interim:** they are official VB-Audio manual
  figures (native 450–1000 px, enlarged for print, so slightly soft), not captures of
  our own setup — device names and settings are VB-Audio's. Real Windows captures at
  150–200 % display scaling will replace them (swap the sources in
  `tools/make_section_crops.py`, re-run, rebuild). Manual gaps (things the manual does not
  explain, stated as such on the pages) are listed in `source/OUTLINE.md`.

See `CHANGELOG.md` for what changed between versions.
