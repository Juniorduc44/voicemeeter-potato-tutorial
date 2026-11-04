# Changelog

## v3 — 2026-11-04 (manual-based polish + error-check)
Checked line-by-line against the official *User Manual — Voicemeeter Potato 3.1.3.0*.
Full log: `docs/ERROR_CHECK.md`. Four fixes, nothing else changed:
1. "Voicemeeter Out B1" newer-name note added in Step 5 Part 2, Way 3, and the
   quick reference card (manual p.18: new VAIO driver names).
2. New panel after Step 3: **Menu → turn ON "Run at Startup"** (manual's own
   post-install checklist, item 8) — prevents the after-reboot no-sound panic.
3. Step 5 sub-step: Sound box **Communications tab → "Do nothing"**, so Windows
   doesn't turn sound down during Discord/Zoom calls (manual, Quick Startup Guide).
4. Step 3 precision: A1 driver choice now reads WDM "or ASIO, if you see it and
   you use a proper audio interface" (manual's A1 recommendation).
Still open: Steps 1–2 pictures are labelled diagrams, and no live Windows
run-through / trainee test has happened yet.

## v2 — 2026-11-04 (button crops)
- Every specifically referenced button that could be sourced from a real
  screenshot is now a tight crop of that very button, replacing drawn icons:
  A1 / HARDWARE OUT corner, HARDWARE INPUT 1 strip header, Windows Sound
  Playback/Recording tabs, Set Default, OK, the real strip A1/B1 button
  columns (mic: B1 lit / A1 grey; computer: A1 lit / B1 grey), and Potato's
  Menu button.
- Cover now states the rule: when a step names a button, the picture IS that button.
- Steps 1–2 remain labelled diagrams (no trustworthy real installer screenshot
  sourced yet) — stated on the handout's last page.

## v1 — 2026-11-04 (first illustrated handout)
- 14 pages, Letter, one step per page, big type.
- Cover + the one idea (A = Actual ears / B = Broadcast) with a real Potato screenshot.
- Steps 1–6, the 3 configuration methods, no-sound checklist, tear-off quick
  reference card. Each step page: large labelled picture, STOP warning where
  beginners panic, green CHECK box.
