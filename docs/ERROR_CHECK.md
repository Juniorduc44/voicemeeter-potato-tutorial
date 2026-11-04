# Error-check log — handout v2 checked against the official manual

Date: 2026-11-04
Reference: *User Manual — Voicemeeter Potato, version 3.1.3.0* (SEP 2026, VB-Audio Software, 122 pages), plus the official VB-Audio Potato download page.
Method: every factual claim in the v2 handout text was compared with the manual. A live Windows run was **not** part of this check (no Windows machine available to Muse) — that remains the final verification step.

## Verified correct (no change needed)

- Download file: `Voicemeeter8Setup_v3130.zip`, Voicemeeter 3.1.3.0, 72.2 MB, from vb-audio.com only; the package also installs Voicemeeter (standard) and Banana. (Official Potato page; manual p.1.)
- Potato is donationware. (Manual p.6.)
- Install: run the Setup program in administrator mode, push the button literally labelled **INSTALL**, then **reboot** — the driver needs the reboot to finalize. (Manual, "First Installation".)
- A1 is the main output: it gives the **master clock** to the whole audio engine and sets the main sample rate. Set A1 first is correct advice. (Manual, "Connecting Voicemeeter to Audio device".)
- Hardware device choice: the manual says it is better to select the **WDM** driver; use MME only if WDM is not present or does not work. Handout's "pick WDM" is right. (Manual, device selector remarks.)
- Windows device names (manual p.17 table, and the manual's own Sound-dialog picture):
  - Playback: **Voicemeeter Input** → Virtual Input #1; **Voicemeeter Aux Input** → #2; **Voicemeeter VAIO3 Input** → #3.
  - Recording: **Voicemeeter Output** ← BUS B1; **Voicemeeter Aux Output** ← B2; **Voicemeeter VAIO3 Output** ← B3.
  - So Way 2's and Way 3's device names in the handout are exactly right.
- Master section: BUS A1–A5 go to physical devices; BUS B1–B3 go to virtual outputs that appear as Windows **recording** devices. The handout's A/B teaching is accurate. (Manual p.30.)
- **Restart Audio Engine** is an entry in Potato's main **Menu**. (Manual, "Voicemeeter Main Menu".)
- "No Potato open = no sound": the manual states that if a Voicemeeter device is set as the Windows default, **Voicemeeter must be running**. Checklist item 1 is correct. (Manual, Q&A section.)

## Fixes applied in v3

1. **Newer recording-device names (Step 5 Part 2, Way 3, quick card).** With the new VAIO driver, the manual (p.18) says the recording devices are now also called **"Voicemeeter Out B1"**, "Voicemeeter Out B2", "Voicemeeter Out B3". A trainee on a fresh 3.1.3.0 install might not find "Voicemeeter Output" at all. v3 adds: *"Can't see Voicemeeter Output? Look for **Voicemeeter Out B1** — same thing, newer name."*
2. **Missing "Run at Startup" step (real training gap).** The manual's own post-install checklist (item 8) says to re-check the Menu options **System Tray, Run at Startup, Show App on Startup**. Without it, after any reboot Potato may not be running while Windows still points at it — the exact "no sound at all" panic the checklist describes. v3 adds a small panel: **Menu → turn ON "Run at Startup"** (and System Tray), placed after Step 3.
3. **Communications tab → "Do Nothing" (Step 5).** The manual's Quick Startup Guide: in the Windows Sound dialog, *"the Communications option has to be set to 'Do Nothing' if you use Voicemeeter with VOIP applications."* Otherwise Windows can turn everything else down during Discord/Zoom calls. v3 adds this as a short sub-step in Step 5 while the Sound box is already open.
4. **A1 driver wording (Step 3, minor precision).** The manual recommends for A1: *"select first ASIO (if exists) or WDM."* v3 keeps "pick WDM" as the main instruction and adds: *"or ASIO, if you see it and you use a proper audio interface."* Step 4's mic wording stays WDM-only, which the manual supports.

## Still open (needs a real Windows PC)

- Steps 1–2 pictures (ZIP download, right-click → Extract All / Run as administrator, the INSTALL button screen) are still labelled diagrams. The manual contains an installer-adjacent screenshot set, but not a clean, verifiable shot of the actual Setup window with its INSTALL button at a size safe to crop — and faking one would break the project's own rule. A real run-through remains the gold source.
- Whether a fresh 3.1.3.0 install shows the classic recording names, the new "Out B1/B2/B3" names, or both, can only be settled on a real install — v3 covers both wordings.
- Live audio flow (meters, monitoring, per-app routing) has never been tested end-to-end. Trainee run-through still pending, as before.
