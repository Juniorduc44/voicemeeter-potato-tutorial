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

## Repository layout

| Folder | Contents |
| --- | --- |
| `handout/` | The printable PDF handout. `-v1`, `-v2`, `-v3` are frozen versions; the un-suffixed file is always the current version (currently v3). |
| `docs/` | `ERROR_CHECK.md` — the v2 handout checked claim-by-claim against the official Potato 3.1.3.0 manual: what was verified, the four v3 fixes, and what still needs a real Windows PC. |
| `images/source-screenshots/` | Full original screenshots the handout pictures were taken from. |
| `images/button-crops/` | Tight crops of the very buttons the steps reference (A1, Set Default, OK, Menu, strip A1/B1 columns, …), plus the annotated Sound dialog. |
| `images/page-previews/` | A PNG render of every handout page (current version). |
| `source/v1/`, `source/v2/`, `source/v3/` | The build source (HTML + outline) that produced each PDF version. |

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

See `CHANGELOG.md` for what changed between versions.
