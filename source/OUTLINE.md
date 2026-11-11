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

Source for every claim below unless marked otherwise: **[P]** = official *User Manual - Voicemeeter Potato 3.1.3.0* (SEP 2026), https://vb-audio.com/Voicemeeter/VoicemeeterPotato_UserManual.pdf - page numbers are the manual's own page footers. The Potato manual (p.2) says it covers only Potato's additions and tells readers to read the Standard/Banana manual first, so three basic strip controls are sourced from **[S]** = official *User Manual - Voicemeeter Standard 1.1.3.0* (SEP 2026), https://vb-audio.com/Voicemeeter/Voicemeeter_UserManual.pdf (linked from the official Potato page). Pictures: official [P] figures, see images/manual-figures/SOURCES.md.

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
GAPS: the manual never says in words that A2-A5 are picked "the same way" as A1 (it explains the A1 button and the shared device selector); the "512" after the sample rate in the HARDWARE OUT header is not explained next to it (p.97 explains "buf" as buffer size in another dialog) - the page says "leave it".

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
