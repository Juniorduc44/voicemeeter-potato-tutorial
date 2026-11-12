Section: Cover
Claim: Anyone can do this - one click per page, picture for every step.
Source: verbatim request + parent tutorial.

Section: The one idea
Claim: Potato is a traffic controller; A is for your ears, B is for other people.
Source: parent tutorial.

Section: Step 1 Download
Claim: Only vb-audio.com is safe; file Voicemeeter8Setup_v3130.zip, 72.2 MB, v3.1.3.0.
Source: browser.search official VB-Audio page result.

Section: Step 2 Install and restart
Claim: Extract, Run as administrator, Install, then reboot - do not skip restart.
Source: official VB-Audio installation line in search result.

Section: Step 3 A1 headphones first
Claim: Set A1 before anything else or you hear nothing; prefer WDM.
Source: parent tutorial.

Section: Step 4 Microphone Input 1
Claim: Pick mic on Hardware Input 1; talking should make bars dance.
Source: parent tutorial.

Section: Step 5 Make Potato Windows default - Playback
Claim: Win+R, mmsys.cpl, Playback tab, Voicemeeter Input VAIO = Set Default.
Source: parent tutorial + search results.

Section: Step 5 continued - Recording
Claim: Recording tab, Voicemeeter Output VAIO = Set Default; names look backwards and that is correct.
Source: parent tutorial.

Section: Step 6 Golden routing
Claim: Mic strip B1 on / A1 off; computer strip A1 on, B1 only to share.
Source: parent tutorial.

Section: Way 1 Everything together
Claim: Day 1 method - one Windows default, one strip controls all computer sound.
Source: parent tutorial.

Section: Way 2 Split apps in Windows
Claim: Volume mixer sends Game to VAIO, Discord to Aux, Music to VAIO3.
Source: parent tutorial.

Section: Way 3 Inside the app
Claim: In Discord/Zoom/OBS set mic to Voicemeeter Output B1, speaker to Aux Input.
Source: parent tutorial.

Section: No-sound checklist
Claim: Check in order: Potato open, A1 picked, A1 lit, Restart Audio Engine.
Source: parent tutorial.

Section: Quick reference card
Claim: The whole setup on one tear-off page to keep by the computer.
Source: synthesis of steps above.

Edit 2026-11-04 (real button crops): Every specifically referenced button that could be sourced from a real screenshot is now a tight crop of that very button, in place of the drawn icon: Step 3 HARDWARE OUT A1-A5 crop (A1 red-boxed) + big A1; Step 4 HARDWARE INPUT 1 header crop; Step 5 real Sound tabs, real Set Default (x2), full real Recording-tab Sound box with VoiceMeeter Output row + Set Default red-boxed, real OK; Step 6 real strip button columns (mic: B1 green ON / A1 grey OFF; computer: A1 green ON / B1 grey OFF, incl. mono/solo/Mute); checklist real Menu button. Crops live in .src/media/btn-*.png + sound-dialog-annotated.png, cut from potato-linus.png (1645x770), potato-real.jpg, and a real Sound dialog screenshot (via klop.solutions). Steps 1-2 (ZIP download, Extract All / Run as administrator / INSTALL) remain labelled diagrams - no verified real installer/context-menu screenshot could be sourced; last page states this. Still NOT error-checked end-to-end or trainee-tested, per Junior.

Edit 2026-11-04 (v3, manual error-check): Error-checked against the official VoiceMeeter Potato User Manual, Voicemeeter 3.1.3.0 (SEP 2026). Exactly four fixes applied, everything else unchanged: (1) newer recording-device name note "Can't see Voicemeeter Output? Look for Voicemeeter Out B1 - same thing, newer name" added in Step 5 Part 2, Way 3, and the quick reference card (manual p.18); (2) new "Run at Startup" panel in Step 3 (Menu -> turn ON Run at Startup; manual post-install checklist item 8); (3) new Communications tab sub-step in Step 5 Part 2 (choose "Do nothing" for VOIP/Discord/Zoom; manual Quick Startup Guide); (4) Step 3 A1 box now adds "or ASIO, if you see it and you use a proper audio interface" while keeping WDM as the main instruction (Step 4 mic wording untouched). Last page now states the v3 manual check and lists the four fixes, and keeps the honest notes: Steps 1-2 pictures are still labelled diagrams and a live Windows run-through is still pending. Layout only: Step 3 and Step 5b pictures slightly reduced to fit the new panels at full type size; still 14 pages.

---

# Part 2 - Know Your Mixer (added 2026-11-11, branch know-your-mixer)

Source for every claim below unless marked otherwise: **[P]** = official *User Manual - Voicemeeter Potato 3.1.3.0* (SEP 2026), https://vb-audio.com/Voicemeeter/VoicemeeterPotato_UserManual.pdf - page numbers are the manual's own page footers. The Potato manual (p.2) says it covers only Potato's additions and tells readers to read the Standard/Banana manual first, so three basic strip controls are sourced from **[S]** = official *User Manual - Voicemeeter Standard 1.1.3.0* (SEP 2026), https://vb-audio.com/Voicemeeter/Voicemeeter_UserManual.pdf (linked from the official Potato page). Pictures: since 2026-11-12 real screenshots of the user's own Windows 10 VM running Potato 3.1.3.0 x64 (images/source-screenshots/SOURCES.md); things that only open on a click are official [P] figures, labelled as such on the page (images/manual-figures/SOURCES.md).

Section: KYM intro - the map
Claim: Potato has 8 inputs (5 physical, 3 virtual) and 8 buses (A1-A5, B1-B3); the window splits into top bar, hardware inputs, virtual inputs, Hardware Out, recorder, Special FX, Master section.
Source: [P] p.9 (8 in / 8 buses), p.10 full-window figure (layout), p.31 (Master section), p.39 (Special FX), p.45 (recorder). Picture: [P] p.10 figure.

Section: 1 Top bar
Claim: VBAN button opens the VBAN configuration box; VBAN sends / receives audio to / from computers on the local network.
Source: [P] p.60 ("Click on VBAN icon to open the configuration dialog box"), p.12.
Claim: Menu lists Restart Audio Engine, Load/Save Settings, Reset Settings, System Tray, Run on Windows Startup, Lock Graphic User Interface, Eject Cassette, System Settings, MacroButtons / Streamer View launch, etc.
Source: [P] p.47 text + p.47 menu figure (exact item names taken from the figure).
Claim: Macro buttons are a separate app (MacroButtons) launched from the Menu, not part of the main window.
Source: [P] p.12, p.47 ("To Run Macro Button or Streamer View on Voicemeeter launch").
Claim: Restart Audio Engine fixes the stream stopping after plugging/unplugging a USB device.
Source: [P] p.117 ("simply restart audio engine").
Claim: Reset Settings resets Voicemeeter's complete settings.
Source: [P] p.47 ("To reset Voicemeeter complete settings").
Claim: Lock Graphic User Interface prevents changing settings.
Source: [P] p.47.
Claim: Save Settings / Load Settings keep and restore a setup file.
Source: [P] p.47 ("To load or save current settings in a given filename").
Claim: If Potato is closed while it is the Windows default device, there is no sound.
Source: [P] p.117 ("Voicemeeter must be running ... otherwise there might be no sound").
NOT IN MANUAL (stated as such on the page): the small R/A boxes beside the logo; the **?** button. The _ and X buttons are described from the usual Windows convention (minimise / close), not from the manual.

Section: 2 Hardware inputs
Claim: Click the strip's input area to select its input device; prefer WDM, MME only if WDM fails.
Source: [P] p.16.
Claim: INTELLIPAN Color Panel changes the colour of the voice (3 bands + tiny reverb); right-click switches panels (Modulation, Position 3D).
Source: [P] p.20-21.
Claim: Right-click the small EQ button opens a 6-band parametric EQ for the hardware input.
Source: [P] p.28.
Claim: Comp (auto make-up: big boost, then lower fader), Gate, Denoiser (0-10, adds latency when not 0).
Source: [P] p.22; Gate behaviour (closes below threshold) [P] p.23.
Claim: Right-click Comp/Gate opens detailed view; right-click again goes back.
Source: [P] p.22, p.24.
Claim: Reverb / Delay send knobs; POST button = send follows the fader.
Source: [P] p.39.
Claim: The send labelled C5 instead of Delay means C5 was selected to replace the Delay in System Settings.
Source: [P] p.41; figure [P] p.49 shows "C5".
Claim: External FX sends work only with an ASIO device on A1 with channels assigned.
Source: [P] p.9, p.43, p.44.
Claim: Click in the meter to set the strip limiter.
Source: [P] p.24.
Claim: Double-click a control returns it to default.
Source: [P] p.24 ("All controls go back to default value if double click on it").
Claim: A buttons send to physical buses, B to virtual buses (what apps record from).
Source: [P] p.10, p.17, p.31; [S] p.11.
Claim: solo = listen to one or several strips only; Mute mutes the strip; Fader Gain sets the strip volume.
Source: [S] p.11 (not described in [P]).
Claim: mono makes the strip mono.
Source: [P] p.22 only says pan-pot MONO mode "works like the MONO button on stereo strips" - no fuller definition in [P] or [S]; the page says "the manual gives no more detail".
Picture: [P] p.49 figure, strip 1 (renamed "Mic" in VB-Audio's example).

Section: 3 Virtual inputs
Claim: VAIO / AUX / VAIO3 strips are fed by the Windows playback devices Voicemeeter Input / Aux Input / VAIO3 Input.
Source: [P] p.17.
Claim: 3-band EQ (bass, medium, treble) and 5.1 pan pot; double-click pan resets to centre; right-click for pan mode menu.
Source: [P] p.21-22. (Which knob is "medium": the figure labels only Treble (top) and Bass (bottom); middle = medium inferred from the 3-band description - flagged.)
Claim: Strip shows the first applications connected through Windows, each with volume + M (mute) linked to the Windows Volume Mixer both ways; right-click extends the list; Restart Audio Engine refreshes it; Discord may appear on all strips because it opens every device.
Source: [P] p.30-31.
Claim: M.C mutes the centre channel (channel 3, film dialogue) on 5.1/7.1 material.
Source: [P] p.25; [S] p.26.
Claim: K button on the AUX strip = Karaoke voice remover, modes K-m, K-1, K-2, Kv.
Source: [P] p.27 (since Potato 3.0.1.3); figure [P] p.14.
Picture: [P] p.10 figure (older build shows M.C on AUX) + [P] p.14 figure (newer build, K on AUX).

Section: 4 Hardware Out A1-A5
Claim: Click A1 to pick the main output; A1 gives the master clock and the main sample rate; prefer ASIO (if exists) or WDM.
Source: [P] p.14.
Claim: With no device on A1, Potato runs on its internal clock; Remove Selection un-picks the device.
Source: [P] p.14, p.16; figure [P] p.14 ("Internal Master CLOCK", "Remove Selection").
Claim: Open Windows Sound button opens the Windows Sound dialog.
Source: [P] p.15.
Claim: A1-A5 are physical buses (real devices); Potato can manage 5 headsets.
Source: [P] p.9, p.31.
Claim: WDM / KS outputs are used in exclusive mode by default; other apps may not be able to use them.
Source: [P] p.14, p.117.
Claim: Several outputs are not exactly synchronised - a small echo is normal and can be compensated with a delay in System Settings.
Source: [P] p.117.
GAPS: the manual never says in words that A2-A5 are picked "the same way" as A1 (it explains the A1 button and the shared device selector); the "512" after the sample rate in the HARDWARE OUT header is not labelled in the manual (2026-11-12 update: page 4C says "most likely the buffer size" because [P] p.98 says A1 sets sample rate and buffer size, WDM default 512, MME 1024, and the p.52 figure shows 256 with ASIO - still marked "not labelled in the manual"); "11 ms" is not explained (p.52 figure shows 5 ms with ASIO).

Section: 5 Cassette recorder
Claim: Click cassette top to choose a file; click progress bar to jump; Record writes to Documents\Voicemeeter with prefix + date + time; playable formats WAV, AIFF, MP3, M4A, MP4, MOV, AVI, WMA, WMV.
Source: [P] p.45.
Claim: Labelled parts (filename/directory, current input level, armed strip/bus, sound format, REW/FF/Play/Stop/Record-Pause, BUS routing for playback).
Source: [P] p.45 labelled figure.
Claim: Right-click tape deck = Recorder Options: pre-fader inputs, post-fader outputs (one bus = what you hear on it), folder/prefix, pre-recording buffer, file type WAV/BWF/AIFF/MP3 (MP3 stereo only), multitrack, play on load, loop, playback gain, stop record after duration.
Source: [P] p.45-46.
Claim: Menu > Eject Cassette releases the audio file.
Source: [P] p.47 ("To Release Audio File (used by the tape recorder)") + menu figure.

Section: 6 Special FX
Claim: Internal Reverb and MultiTap Delay work by send (knob on each physical strip) and return (knob on each bus); POST = send follows fader.
Source: [P] p.39.
Claim: Click the Reverb / Delay button to switch the effect on/off; right-click opens its panel.
Source: [P] p.39 figure callout ("Switch Special FX On/Off, Right click to open the Graphic User Interface").
Claim: Delay can be replaced by the C5 multiband compressor in System Settings.
Source: [P] p.41.
Claim: External FX Return 1/2 knobs per bus; External FX works only with an ASIO device on A1 and the External FX patch.
Source: [P] p.43-44.
Claim: The button shows the current preset name.
Source: inferred from figures [P] p.10 ("Big Hall") and p.39 ("Vocal med").

Section: 7 Master section
Claim: SEL selects the bus mix (input sliders then show that mix; CTRL+click several); Bus mode changes channel organisation (Normal = as is; 14 modes); mono (click twice = cross ch 1/2); EQ on/off, right-click opens it; Mute; Gain slider.
Source: [P] p.31 (text + labelled figure: SELECT MIX, BUS Mode, Reverb Return, Delay Return, Mono / Cross, Master EQ, Mute, Gain Slider), p.33, p.38.
Claim: FX RET. second knob reads C when C5 is used.
Source: [P] p.32 figure.
Claim: B1-B3 appear in Windows as recording devices Voicemeeter Output / Aux Output / VAIO3 Output, newer names Voicemeeter Out B1/B2/B3.
Source: [P] p.17, p.18, p.31.
Claim: Bus limiter -20 to 0 dB, like the strip limiter.
Source: [P] p.25 (not used on the page; noted for later).
GAPS: the manual does not say how to change Bus mode back to Normal (the page says "ask your trainer"); it does not explicitly say clicking a lit SEL again de-selects it (the STOP box says so - verify on a real PC).

Section: Use-case examples (Discord gaming, Zoom/Teams training, OBS stream, podcast)
Claim: each example only combines controls whose behaviour is sourced above; app device names follow Way 2 / Way 3 and [P] p.17. Advice wording ("a little goes a long way", "keep Reverb OFF on calls") is training judgement, not a manual claim.

Edit 2026-11-11 (Part 2 - Know Your Mixer): Added 15 pages after Way 3 (before the no-sound checklist): map page + 2 pages for each of 7 sections (what's what: annotated crop + number/control/what-it-does table; using it: 3 real-world examples, Try it now, STOP, CHECK). Handout is now 29 pages. Pictures are official [P] figures enlarged with red numbered callouts (tools/make_section_crops.py); the user chose these as interim images - real Windows captures will replace them. Cover and last page mention Part 2. Images are referenced by relative path (../images/...) instead of base64 so a later swap is just "re-run the crop script, re-render". Observation for later (not changed): the p.47 menu figure calls it "Run on Windows Startup" while Step 3 says "Run at Startup" (which matches the p.13 figure "System Tray (Run at Startup)"); Part 2 mentions both names.


# Part 2 in depth (added 2026-11-12, branch know-your-mixer)

Same sources: [P] = Potato 3.1.3.0 manual, [S] = Standard manual. Real = the user's Win10 captures (control crops in images/control-crops/, made by tools/make_button_crops.py). "Not explained in the manual" on a page = listed under GAPS here.

Section: Contents page
Claim: none (generated list of page titles, tools/paginate.py).

Section: 1C The Menu, item by item
Claim: Every Menu item and what it does: Restart Audio Engine; Auto restart (A1 / any device disconnected); Eject Cassette; Load / Save Settings and load on startup; Reset Settings; System Tray; Run on Windows Startup; Show on launch / Always on top; Lock GUI; Run MacroButtons / Streamer View on launch; keyboard volume keys for A1/A2/Strip 1; limit remote gain to 0 dB (MIDI); contextual help in caption (ON by default); Preset Scene on startup (64 scenes, Documents\Voicemeeter); System Settings / Recording options / MIDI Mapping / VBAN; About / VAIO Extension / Check Driver Installation (VBDeviceCheck); Shutdown.
Source: [P] p.47 text + menu figure, p.48. Real: menu crop.
GAPS: the manual does not list which keyboard keys control the volume.

Section: 1D VBAN
Claim: VBAN ON/OFF, UDP port 6980, incoming streams (name + IP must match; right-click name/IP to pick a found stream), outgoing streams (source bus, stream name, IP), Net Quality, error lights; 8 in / 8 out streams, 11025 Hz-96 kHz, 16/24 bit, 1-8 ch; .255 address = broadcast.
Source: [P] p.60-63, figure p.61. Real: vban crop.
Claim: "ask your trainer about the firewall" - training judgement.

Section: 1E Audio Map
Claim: The icon right of VBAN is the Windows Audio Map button; click opens the map; right-click gives Windows Sound Settings, Apps Volume and Device Preferences, Privacy for Microphone, Sounds Playback / Recording Devices; in the map drag, wheel or +/- zoom, right-click Refresh.
Source: [P] p.52 (text + figure with help line "AUDIO MAP: CLICK to open the Windows Audio Map"), p.55. Real: audio-map-icon crop. (Replaces the earlier GAP "settings icon not explained".)

Section: 2C INTELLIPAN
Claim: 3 panels switched by right-click (Color Panel, Position 3D, Modulation); Color: 3 bands + reverb top half, up = treble, left = bass, right = medium, top-left "double voice"; Position 3D = binaural room effect, stereo only, helps intelligibility; Modulation: chorus/phasing bottom, modulation top, left feedback; 3 dots turn orange when a panel is not neutral; double-click resets any control.
Source: [P] p.20-21 (+ labelled figure p.20), p.24 (double-click). Real: intellipan-panel crop.

Section: 2D Strip EQ and Strip Menu
Claim: Right-click EQ = 6-band parametric EQ per strip, same as bus EQ, -36 to +18 dB; right-click the word INTELLIPAN = Strip Menu (Reset / Copy / Paste / Save / Load, per effect or All); fader, solo/mute, A/B not affected.
Source: [P] p.28-29, figures p.28, p.29. 3-step copy/paste visual from the p.29 figure items.

Section: 2E Comp, Gate, Denoiser
Claim: Comp = compressor with auto make-up (boosts, so lower the fader); Gate closes below a level; Denoiser 0-10, adds a small delay when not 0; right-click = detailed view (Comp: Input Gain, Ratio, Threshold, Attack, Release, Knee, Output Gain, Auto make-up; Gate: Threshold, Damping Max, BP Sidechain, Attack, Hold, Release; Denoiser: Noise Floor Remover + Voice Modeler: Enable, Dry/Wet, Pitch, Formants -12..+12, 8 presets); CTRL+right-click type a value; SHIFT+click precision; PRG label; CTRL+right-click knob = undo.
Source: [P] p.22-24, p.26. Real: comp-gate-denoiser crop.
GAPS: no number range given for the plain Comp. and Gate knobs.

Section: 2F Sends, meter, fader, buttons
Claim: Reverb/Delay send + Post; External FX sends need ASIO on A1; meter click = limiter -40..+12 dB, right-click type it, CTRL+click yellow/green limiter (green avoids crackle, +5 ms), limiter is before fader; double-click fader = default; right-click A/B = all bus mixes; mono/solo/Mute; right-click fader bottom = strip name (needed by Streamer View).
Source: [P] p.24-25, p.32, p.39, p.43, p.49 (names); [S] p.11 (solo, Mute, Fader Gain). Figure [P] p.24 (limit -12).
GAPS: the manual gives no further detail on the strip mono button.

Section: 3C Virtual strips: name, delay setting, EQ
Claim: "7168 L" = VAIO latency in samples, 7168 default expected to work 100%, 3072 or less reduces latency (may break up), Voicemeeter Input linked to B1, right-click the name for the menu, Show Control Panel; EQUALIZER 3 knobs treble / medium / bass, double-click resets; click the word EQUALIZER = Strip Menu of a virtual strip.
Source: [P] p.56 (+ figure), p.100 (lower latency can break the stream), p.21, p.29 (+ virtual menu figure). p.21: "3 Bands Equalizer to boost or remove bass, medium and high frequency (treble)"; the middle knob = medium is from the layout (Treble / Bass labelled on screen).

Section: 3D Pan, apps, M.C and K
Claim: 5.1 pan box ([P] p.21); double-click = Normal mode centre; right-click = pan-mode menu (Normal, MONO, Repeat Mono, Repeat Stereo, Mix Down, Up Mix, ... Only); app list first 4 apps with meter, slider, M, linked to Windows Volume Mixer, right-click shows up to 32; M.C mutes channel 3 (centre); K on AUX: K-m, K-1, K-2, Kv (200-4000 Hz).
Source: [P] p.21-22 (+ figure p.22), p.25, p.27, p.30. Real: virtual-pan, mc, k crops.
GAPS: how to step through K modes is not explained.

Section: 4C HARDWARE OUT readout and picking A1
Claim: 48kHz = sample rate set by A1 (32-192 kHz list); 512 not labelled (see GAPS above); Internal Master CLOCK when nothing on A1; 11 ms not explained; 4 steps to pick A1 (tab ASIO / WDM / MME); WDM/KS exclusive by default; buffer below 256 samples can bring stability problems.
Source: [P] p.100 (256), p.14, p.52 figure, p.98, p.100, p.117. Real: hardware-out-header, a1-top crops.

Section: 5C Recorder Options
Claim: A pre-fader inputs (default), B post-fader one bus, C folder/name, D file type WAV/BWF/AIFF/MP3 32-320 kbps, E pre-recording buffer (20 s), F play on load / loop, G playback gain, H stop record after, Multitrack (one file per channel); 4-step record visual.
Source: [P] p.45-46 (+ figure p.45). Real: record, stop crops.

Section: 6C Reverb panel
Claim: JustVerb III: presets 10 x 3, DRY minimum and WET 0 dB with send/return, pre-delay up to 1000 ms, E.Ref, Decay 50-200%, BYP, 3-band EQ; needs send + return.
Source: [P] p.39-40 (+ figure p.40). Real: reverb-off crop.

Section: 6D Delay panel and C5
Claim: MultiTap Delay: 8 taps with gain/pan/filter, tempo / time ratio, Tap (red after 4 taps), Scale Fit / Fix Delay / Auto Fit, Set Note, dry/wet/pre-delay/bypass, balance, feedback; C5 replaces Delay via System Settings, labels C5 / C, A/B off on buses receiving the C5 return.
Source: [P] p.40-43 (+ figure p.41), p.98. Real: delay-off crop.

Section: 7C Bus modes and SEL
Claim: 8 channels per bus; Normal, Mix Down A/B, Stereo Repeat (with EQ for active speakers), Composite (System Settings), Up Mix TV/2.1/4.1/6.1, Left/Right/Center/LFE/Rear Only; SEL = per-bus mix, CTRL+click several, CTRL+wheel / CTRL+click in the bus-mix view.
Source: [P] p.31-32 (+ figure p.32), p.34-38. Real: bus-mode, bus-sel crops.
GAPS: how to step through the modes on the button; clicking a lit SEL again to de-select.

Section: 7D Bus EQ, returns, limiter, names
Claim: FX RET R / D (C with C5); mono, click twice swaps L/R; EQ click on/off, right-click window, EQ colours green/red/yellow/black; Mute; meter limiter -20..0 dB, output limiter ON by default; right-click fader bottom = name; EQ window: 6 cells x 8 channels, FLAT, A/B memories, CH COPY / COPY ALL, right-click to type, Load/Save.
Source: [P] p.25, p.31, p.33-34 (+ figure p.33), p.49, p.98. Real: bus-fx-ret, bus-mono-eq-mute crops.

Section: Cheat sheet - mouse and keyboard tricks
Claim: one row per trick; every row repeats a claim sourced in the sections above (p.16 for click strip name = pick device).

GAPS (remaining, 2026-11-12): small R and A boxes in the top bar; the ? button; strip mono button detail; how to step through bus modes and K modes; SEL de-select; plain Comp./Gate knob ranges; Menu keyboard-volume keys; A2-A5 picked like A1 (implied, not stated); 512 (likely buffer) and 11 ms in the HARDWARE OUT readout.

Edit 2026-11-12 (real captures): All Part 2 section crops regenerated from the user's own Windows 10 VM captures of Potato 3.1.3.0 x64 (two 100% halves, stitched pixel-exactly for the overview map by tools/stitch_window.py; three 1.5x zoom captures as the primary crop source). Manual figures kept only for things not visible on the closed window, each labelled. Tables/captions updated to what the real screen shows (Stereo Input 1, 48.0 kHz - 7168 L, 48kHz | 512, Internal Master CLOCK, 11 ms).

Edit 2026-11-12 (full SOP): Handout renamed to handout/voicemeeter-potato-sop.pdf and retitled "VoiceMeeter Potato - Setup and Training SOP"; all former "GrandMa" wording removed from trainee-facing text, title and metadata. Added a Contents page and 16 "in depth" pages (1C-1E, 2C-2F, 3C-3D, 4C, 5C, 6C-6D, 7C-7D, cheat sheet) - 46 pages total, footers and contents generated by tools/paginate.py. 35 zoomed control crops (images/control-crops/) for named buttons, step-by-step visuals for multi-step actions. Recorder Options figure moved from 5A to 5C. 1A row 3 now names the Windows Audio Map button.


Section: 1C The Menu, item by item (now 2 pages, 2026-11-12)
Claim: Item names, order, grouping and shortcuts (CTRL+R, CTRL+4, CTRL+',', CTRL+5, CTRL+3, CTRL+1, CTRL+2, CTRL+6) exactly as in the user's real Win10 Menu capture (item list relayed by the parent agent from images/source-screenshots/potato-win10-menu.png - file still to be added, see edit log); cross-checked against the [P] p.47 figure, which has the same items except Windows Audio Map... [CTRL+6] and Windows Audio Settings... (submenu), which only the real capture shows.
Source for what each item does: [P] p.47-48 (menu text); Preset Scene 64 presets in Documents\Voicemeeter, ENTER / CTRL+click recall, F1-F24: [P] p.51; VBAN Chat: [P] p.62; Tape Recorder Options = Recorder Options: [P] p.45; Windows Audio Map: [P] p.52; Run other Voicemeeter tools (8x8 Gain Matrix, 15 Bands graphic EQ, VBAN2MIDI): [P] p.48; Shortcut Key (Hook) = hook keys to control A1 / A2 / Strip 1 volume: [P] p.47.
GAPS: Shortcut Key (Hook) submenu contents (not visible in the capture, keys not listed in the manual); Windows Audio Settings submenu contents (not visible); Online Help / Support (not explained in the manual); Run other Voicemeeter tools submenu contents (not visible; manual names the tools).

Edit 2026-11-12 (real Menu capture): Menu reference split into 2 pages with every item in the real capture's exact wording and order, grouped, with shortcut keys; added items: Auto Restart (A1 / All Device) as separate rows, Run other Voicemeeter tools, Shortcut Key (Hook), Preset Scene..., Tape Recorder Options..., VBAN Chat Room..., Windows Audio Map..., Windows Audio Settings..., Online Help / Support.... Cheat sheet gets a keyboard-shortcut block (+ Preset Scene keys, [P] p.51). The real capture confirms "Run on Windows Startup": Part 1 Step 3, the 1B Try-it and the last-page note now use only that wording (supersedes the earlier "Run at Startup" observation). The p.47 manual figure on page 16 stays until the capture file itself is on the box. 46 -> 47 pages.
