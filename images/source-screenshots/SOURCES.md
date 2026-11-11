# Source screenshots (real captures)

Provenance: the user's own captures of a **fresh install of Voicemeeter Potato 3.1.3.0 (x64)**
on a **Windows 10 VM**, sent 2026-11-12. Nothing selected yet (no A1 device, no input
devices, no apps playing), so the window shows Potato's defaults. These are the primary
picture source for Part 2 of the handout.

| File | Size | What it shows |
| --- | --- | --- |
| `potato-win10-left.png` | 1134x767 | 100 % display scaling. Left half: logo / top bar left, Stereo Input 1-5, the three VIRTUAL INPUTS strips (Voicemeeter Input, AUX, VAIO3) incl. M.C / K. |
| `potato-win10-right.png` | 846x768 | 100 %. Right half: VBAN + settings icon, virtual inputs again (overlap), HARDWARE OUT A1-A5 + header (48kHz &#124; 512 / Internal Master CLOCK / 11 ms), Menu ? _ X, cassette recorder, SPECIAL FX, External FX Return, MASTER SECTION. |
| `potato-win10-full-stitched.png` | 1645x765 | Made by `tools/stitch_window.py` from the two 100 % captures (see below). Source of the overview map and of the top-bar-right crop. |
| `potato-win10-zoom-left.png` | 1201x1151 | ~1.5x zoomed capture: logo / top bar left + Stereo Input 1-5. |
| `potato-win10-zoom-middle.png` | 501x1151 | ~1.5x: VBAN + settings icon, VIRTUAL INPUTS (3 strips incl. M.C / K). |
| `potato-win10-zoom-right.png` | 761x1151 | ~1.5x: HARDWARE OUT A1-A5, Menu ? _ X, cassette recorder, SPECIAL FX, External FX Return, MASTER SECTION. |

The zoomed captures look like a scaled view of the same 100 % window (template matching
against the stitched image gives a 1.50x scale with a 1-3 px residual); they are smoother
but carry no extra UI detail. They are still the best source, so the section crops are cut
from them (`tools/make_section_crops.py`, `zoom=` argument).

## How the stitch was made (`tools/stitch_window.py`)
- The RIGHT capture's x=0 is the LEFT capture's x=799 (found by exhaustive search).
- The two captures came from slightly different window heights, so rows shift by
  2 px (rows < 194), 1 px (194-575) and 0 px (576+). LEFT rows are mapped into the RIGHT
  capture's rows; only LEFT rows 192 and 575 are dropped, and the script asserts each is an
  exact copy of a neighbouring row.
- Join column: RIGHT x=60 (inside the virtual inputs). After the row mapping the whole
  remaining overlap (RIGHT x 60-334) matches pixel-for-pixel in every row (script asserts 0
  difference), so there is no seam and no duplicated strip. RIGHT rows 0-1 and 767 have no
  LEFT counterpart and are cropped off. Checked visually at the seam as well.
