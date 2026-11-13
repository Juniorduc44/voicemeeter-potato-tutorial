# Project To-Do List

Everything still needed to replace remaining manual figures with real Windows 10 captures and close the open manual gaps in the SOP (`main`).

## 1. High-Priority Visuals (New / Replacement Screenshots)

- [ ] **Hover-caption before & after (for a new intro tip page before Step 1):**
  - Capture the full top bar (logo through A1–A5) at 150–200% Windows scaling with the mouse resting on empty space (normal caption).
  - Capture the same bar with the cursor visible (using ShareX or Greenshot) hovering over `A1` so the yellow contextual help line shows.
  - Capture one more control hover (e.g., a strip fader or `Mute`) to show the feature works everywhere.
- [ ] **Menu dropdown (page 16):** Resend the real Win10 Menu screenshot so we can swap out the manual p.47 figure.
- [ ] **Part 1 Steps 1–2 installer screenshots (pages 4–5):** Real Windows installer / reboot prompt captures to replace the labelled diagrams.

## 2. Pop-Up Windows Still Using Official Manual Figures

Right now these pages use figures from the official manual because the pop-ups weren't open in the main VM captures:

- [ ] **Page 19 — VBAN Configuration dialog** (`p61-vban-configuration-dialog.jpg`): Click **VBAN** in the top bar.
- [ ] **Page 20 — Audio Map right-click menu** (`p52-audio-map-button-menu.jpg`): Right-click the **Audio Map** icon next to VBAN.
- [ ] **Page 23 — INTELLIPAN Color Panel / 3D / Modulation** (`p20-intellipan-color-panel-labelled.png`): Optional real captures if needed.
- [ ] **Page 24 — Strip 6-band Parametric EQ & Hardware Strip Menu** (`p28-strip-parametric-eq.png`, `p29-strip-menu-hardware.png`): Right-click **EQ** / right-click **INTELLIPAN**.
- [ ] **Page 26 — Strip Limiter** (`p24-strip-limiter.png`): Click a strip meter and set a limit (e.g., `-12`).
- [ ] **Page 29 — Virtual Input Latency Menu & Virtual Strip Menu** (`p56-vaio-latency-menu.png`, `p29-strip-menu-virtual.png`): Right-click the virtual strip name / click **EQUALIZER**.
- [ ] **Page 30 — 5.1 Pan-Pot Mode Menu** (`p22-pan-pot-mode-menu.png`): Right-click the 5.1 pan box.
- [ ] **Page 39 — Reverb (JustVerb III) Panel** (`p39-special-fx-reverb-panel.png`, `p40-justverb-reverb-panel.png`): Right-click **Reverb**.
- [ ] **Page 40 — MultiTap Delay Panel** (`p41-multitap-delay-panel.png`): Right-click **Delay**.
- [ ] **Page 43 — Bus Sub-Mix View** (`p32-bus-sub-mix-view.jpg`): Right-click any strip's `A1`–`B3` routing button.
- [ ] **Page 44 — Master Bus EQ (`EQpro-G6`)** (`p33-master-eq-dialog.jpg`): Right-click **EQ** on any Master bus.

## 3. Open Questions / Manual Gaps to Verify on Live VM

- [ ] **Top bar `R` and `A` boxes & `?` button:** What each does when clicked.
- [ ] **Menu submenus:** What's inside `Shortcut Key (Hook)...` (and which keys control volume), `Windows Audio Settings...`, `Run other Voicemeeter tools...`, and what `Online Help / Support...` opens.
- [ ] **Hardware strip `mono` button:** Exact signal behavior vs. Master `mono`.
- [ ] **Comp / Gate knobs:** Exact numeric ranges on the plain strip knobs.
- [ ] **Stepping through modes:** Whether left-click, right-click, or a menu cycles through `K` modes (AUX) and Master bus modes.
- [ ] **Master `SEL` button:** Whether clicking a lit `SEL` again turns it off.
- [ ] **HARDWARE OUT readout:** Confirm `512` is the buffer size in samples and what `11 ms` measures.
- [ ] **Output devices `A2`–`A5`:** Confirm they are picked the exact same way as `A1`.
