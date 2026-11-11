# Official manual figures — sources

All images in this folder are **embedded originals** extracted unchanged (`pdfimages -all -p`)
from the official VB-Audio manual:

- **Document:** *User Manual — Voicemeeter Potato, version 3.1.3.0* (SEP 2026), V. Burel /
  VB-Audio Software, 122 pages, A4.
- **URL:** https://vb-audio.com/Voicemeeter/VoicemeeterPotato_UserManual.pdf
  (linked from the official Potato page https://vb-audio.com/Voicemeeter/potato.htm).
  Downloaded 2026-11-11, 12,180,012 bytes, PDF ModDate 2026-09-15.
- © VB-Audio Software / V. Burel. Used as interim training illustrations until real
  Windows captures replace them (user decision, 2026-11-11).

The manual does not number its figures, so each is identified by **page + what it shows +
`pdfimages` image index** (`pdfimages -list` "num" column). Pixel sizes are the native
embedded resolution — nothing higher exists in the PDF (rendering the page at 300–600 dpi
only resamples these same pixels), so these are the best available originals.

| File | Manual page | Figure (what it shows) | pdfimages # | Native size |
| --- | --- | --- | --- | --- |
| `p09-general-diagram-window-with-devices.jpg` | 9 | Introduction diagram: full Potato window with mics, apps and output devices around it | 1 | 958×718 |
| `p10-full-window-clean.jpg` | 10 | "Voicemeeter Potato General Diagram" page: clean full Potato main window, no overlays (older build: no **?** button, AUDIBILITY label, M.C on AUX) | 3 | 967×453 |
| `p13-quick-startup-4-steps.png` | 13 | Quick Startup Guide 4-panel figure (Install, default device, select A1, System Tray menu) | 6 | 1133×775 |
| `p14-a1-output-device-selector.png` | 14 | "Select A1 Output Device" list over the top-right of a newer build (VBAN, A1–A3, HARDWARE OUT, Menu, **?**, _, X; AUX strip with **K**, VAIO3 with **M.C**) | 7 | 964×781 |
| `p16-input-device-selector.png` | 16 | "Select Input Device #1" list (WDM / KS / MME / ASIO tabs) | 12 | 849×837 |
| `p22-pan-pot-mode-menu.png` | 22 | Pan-pot right-click mode menu (Normal, MONO, Repeat…, REAR RIGHT Only) | 24 | 262×364 |
| `p30-virtual-strip-apps-vs-windows-mixer.png` | 30 | Virtual-strip application list linked to the Windows Volume Mixer (VB-Audio's own callouts) | 40 | 774×552 |
| `p31-virtual-strip-app-list.jpg` | 31 | Extended application list on a virtual strip ("Right Click to extend…") | 41 | 751×395 |
| `p31-master-bus-controls-labelled.png` | 31 | Two master bus columns labelled by VB-Audio: SELECT MIX, BUS Mode, Reverb Return, Delay Return, Mono / Cross, Master EQ, Mute, Gain Slider | 42 | 504×784 |
| `p32-bus-sub-mix-view.jpg` | 32 | BUS SEL sub-mix view (3.1.3.0 strips: Comp / Gate / Denoiser, EQ button, K button) | 43 | 1133×670 |
| `p39-special-fx-reverb-panel.png` | 39 | Special FX: Reverb button + JustVerb III panel, arrows from strip send to bus return | 69 | 961×557 |
| `p45-recorder-labelled.png` | 45 | Tape recorder labelled by VB-Audio (filename, input level, armed strip/bus, sound format, REW/FF/Play/Stop/Record, BUS routing) | 76 | 554×276 |
| `p45-recorder-options.png` | 45 | "Recorder Options : I/O Arming" dialog (right-click the tape deck) | 77 | 1056×398 |
| `p47-main-menu.png` | 47 | Potato main Menu opened (Restart Audio Engine … Check Driver Installation) | 78 | 356×796 |
| `p49-streamer-view-over-window.jpg` | 49 | VM-Streamer View over the main window — hardware strip 1 ("Mic") is fully visible on the left, 3.1.3.0-era layout | 82 | 975×457 |
| `p60-vban-network-diagram.jpg` | 60 | VBAN network diagram (Talkie / Receptor / Voicemeeter as audio hub) | 99 | 900×604 |
| `p20-intellipan-color-panel-labelled.png` | 20 | INTELLIPAN Color Panel, labelled by VB-Audio (double voice / more treble / more bass / more medium) | 19 | 346×220 |
| `p20-position-3d-panel.png` | 20 | INTELLIPAN Position 3D (binaural) panel examples | 20 | 518×567 |
| `p21-modulation-panel.png` | 21 | INTELLIPAN Modulation panel | 21 | 149×136 |
| `p24-strip-limiter.png` | 24 | Strip limiter set in the meter ("Lim -12") | 29 | 99×166 |
| `p28-strip-parametric-eq.png` | 28 | 6-band parametric EQ of a hardware input (right-click the small EQ button) | 37 | 1026×769 |
| `p29-strip-menu-hardware.png` | 29 | Strip Menu of a hardware input (right-click INTELLIPAN label): Reset / Copy / Paste / Save / Load | 38 | 246×558 |
| `p29-strip-menu-virtual.png` | 29 | Strip Menu of a virtual input (click EQUALIZER label) | 39 | 238×287 |
| `p33-master-eq-dialog.jpg` | 33 | Master bus EQ dialog (EQpro-G6) | 44 | 1174×677 |
| `p40-justverb-reverb-panel.png` | 40 | JustVerb III reverb panel (presets, DRY, WET, DELAY, E.Ref, DECAY, BYP, EQ) | 70 | 580×344 |
| `p41-multitap-delay-panel.png` | 41 | MultiTap Delay panel (Balance, Delay controls, Taps, Tap tempo, Dry/Wet) | 71 | 721×515 |
| `p52-audio-map-button-menu.jpg` | 52 | The settings-style icon right of VBAN = Windows Audio Map button, with its right-click menu | 87 | 1138×232 |
| `p56-vaio-latency-menu.png` | 56 | Virtual input latency menu (right-click the virtual input caption), 7168 samples (Default) ticked | 94 | 331×415 |
| `p61-vban-configuration-dialog.jpg` | 61 | VBAN configuration dialog, labelled by VB-Audio | 100 | 975×689 |

Section crops are now cut from the user's real Windows 10 captures (see
`../source-screenshots/SOURCES.md` and `../section-crops/SOURCES.md`). The figures here are
used only for things that are not visible on the main window until you click or right-click
(Menu, device list, Recorder Options, effect panels, EQ dialogs, strip menus, latency menu,
VBAN dialog, Audio Map menu, INTELLIPAN alternative panels, pan-mode menu); the handout
labels each one "official manual figure, p.N".
