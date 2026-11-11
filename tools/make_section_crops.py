#!/usr/bin/env python3
"""Build the "Know Your Mixer" section crops from the official manual figures.

Source figures: images/manual-figures/ (embedded originals pulled with `pdfimages -all`
from the official VB-Audio "User Manual - Voicemeeter Potato 3.1.3.0", see SOURCES.md).
Each crop is cut from ONE real manual figure, enlarged with Lanczos resampling (this
adds size for print, not detail) and given numbered callouts. Nothing is drawn onto
the screenshot except callout badges, leader lines, target dots and section outlines.

Callout tuple: (label, x, y, side[, badge_pos]) in the SOURCE figure's pixel coords.
side = L/R/T/B margin the badge sits in; badge_pos optionally fixes the badge position
along that margin (output px). Run:  python3 tools/make_section_crops.py
When real Windows captures arrive, swap SRC/boxes/coordinates here and re-run.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, 'images', 'manual-figures')
OUT = os.path.join(ROOT, 'images', 'section-crops')
RED = (214, 40, 57); WHITE = (255, 255, 255)
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def annotate(src, box, s, callouts, out, margin='auto', r=26, minsp=62,
             boxes=(), markers=(), dot=7):
    im = Image.open(os.path.join(FIG, src)).convert('RGB').crop(box)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    if margin == 'auto':  # badge margins sized to the badge radius, 10px elsewhere
        used = {c[3] for c in callouts}
        margin = tuple(2 * r + 28 if sd in used else 10 for sd in 'LRTB')
    minsp = max(minsp, 2 * r + 10)
    L, R, T, B = margin
    W, H = im.width + L + R, im.height + T + B
    can = Image.new('RGB', (W, H), WHITE); can.paste(im, (L, T))
    d = ImageDraw.Draw(can)

    def P(x, y):
        return (L + (x - box[0]) * s, T + (y - box[1]) * s)

    def badge(bx, by, lab, rr=r):
        d.ellipse([bx - rr - 3, by - rr - 3, bx + rr + 3, by + rr + 3], fill=WHITE)
        d.ellipse([bx - rr, by - rr, bx + rr, by + rr], fill=RED)
        lab = str(lab)
        f = ImageFont.truetype(FB, int(rr * (1.15 if len(lab) < 3 else 0.85)))
        d.text((bx, by + 1), lab, fill=WHITE, font=f, anchor='mm')

    for bx in boxes:  # section outlines (overview map)
        x0, y0 = P(bx[0], bx[1]); x1, y1 = P(bx[2], bx[3])
        d.rectangle([x0, y0, x1, y1], outline=WHITE, width=10)
        d.rectangle([x0 + 3, y0 + 3, x1 - 3, y1 - 3], outline=RED, width=5)

    groups = {}
    for c in callouts:
        groups.setdefault(c[3], []).append(c)
    placed = []
    for side, cs in groups.items():
        horiz = side in 'TB'
        key = (lambda c: c[4] if len(c) > 4 else P(c[1], c[2])[0 if horiz else 1])
        cs = sorted(cs, key=key)
        pos = []
        for c in cs:
            want = key(c)
            pos.append(max(want, (pos[-1] + minsp) if pos else r + 4))
        lim = (W if horiz else H) - r - 4
        if pos and pos[-1] > lim:
            pos = [p - (pos[-1] - lim) for p in pos]
        for c, p in zip(cs, pos):
            if side == 'L': placed.append((c, (L / 2, p)))
            elif side == 'R': placed.append((c, (W - R / 2, p)))
            elif side == 'T': placed.append((c, (p, T / 2)))
            else: placed.append((c, (p, H - B / 2)))
    for c, (bx, by) in placed:
        d.line([(bx, by), P(c[1], c[2])], fill=WHITE, width=max(9, r // 4))
    for c, (bx, by) in placed:
        tx, ty = P(c[1], c[2])
        d.line([(bx, by), (tx, ty)], fill=RED, width=max(4, r // 8))
        d.ellipse([tx - dot, ty - dot, tx + dot, ty + dot], fill=RED, outline=WHITE, width=3)
    for c, (bx, by) in placed:
        badge(bx, by, c[0])
    for lab, x, y in markers:  # big in-picture badges (overview map)
        badge(*P(x, y), lab, rr=int(r * 1.35))
    can.save(os.path.join(OUT, out), optimize=True)
    print(f'{out:40s} {can.size[0]}x{can.size[1]}  from {src} crop {box} x{s}')


FULL = 'p10-full-window-clean.jpg'          # manual p.10, 967x453
SEL = 'p14-a1-output-device-selector.png'   # manual p.14, 964x781
STRIP = 'p49-streamer-view-over-window.jpg' # manual p.49, 975x457 (strip 1 is uncovered)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    # 0. Overview map: the whole window, sections 1-7
    annotate(FULL, (0, 0, 967, 453), 2,
             [(1, 330, 12, 'T', 660), (1, 912, 14, 'T', 1824), (4, 760, 4, 'T', 1520)],
             '00-overview-map.png', r=40,
             boxes=[(1, 1, 658, 24), (860, 1, 966, 30), (1, 26, 464, 452), (466, 26, 660, 452),
                    (663, 1, 857, 50), (676, 55, 852, 168), (855, 31, 966, 168), (663, 172, 966, 452)],
             markers=[(2, 233, 240), (3, 563, 240), (5, 750, 112), (6, 910, 136), (7, 815, 300)])
    # 1. Top bar - left end (manual p.10) and right end (manual p.14, newer build with "?")
    annotate(FULL, (0, 0, 330, 30), 4, [(1, 162, 20, 'B', 650)],
             '01a-top-bar-left.png', r=34)
    annotate(SEL, (115, 3, 712, 44), 2.5,
             [(2, 155, 35, 'B'), (3, 260, 41, 'B'), (4, 569, 38, 'B'), (5, 632, 40, 'B'),
              (6, 663, 40, 'B'), (7, 690, 40, 'B')],
             '01b-top-bar-right.png', r=34)
    # 2. Hardware input strip 1 (manual p.49 figure, 3.1.3.0-era strip)
    annotate(STRIP, (0, 20, 94, 447), 4,
             [(1, 5, 36, 'L'), (2, 40, 115, 'L'), (3, 90, 70, 'R'), (4, 15, 184, 'L'),
              (5, 41, 177, 'L', 540), (6, 68, 184, 'R'), (7, 25, 226, 'L'), (8, 56, 226, 'R'),
              (9, 10, 237, 'L'), (10, 32, 270, 'L'), (11, 14, 380, 'L'), (12, 46, 319, 'L'),
              (13, 88, 325, 'R'), (14, 88, 377, 'R'), (15, 88, 404, 'R'), (16, 88, 419, 'R'),
              (17, 88, 436, 'R')],
             '02-hardware-input-strip.png', r=38, dot=9)
    # 3. Virtual inputs (manual p.10) + K / M.C buttons (manual p.14, newer build)
    annotate(FULL, (462, 25, 662, 453), 3,
             [(1, 470, 48, 'L'), (2, 487, 90, 'L'), (3, 495, 180, 'L'), (4, 524, 180, 'R'),
              (5, 480, 210, 'L'), (6, 487, 325, 'L'), (7, 531, 320, 'R'), (8, 531, 372, 'R'),
              (9, 531, 400, 'R'), (10, 531, 416, 'R'), (11, 531, 432, 'R')],
             '03a-virtual-inputs.png', r=40, dot=9)
    annotate(SEL, (0, 480, 200, 760), 3, [('K', 40, 684, 'L'), ('M.C', 190, 684, 'R')],
             '03b-k-and-mc-buttons.png', r=40, dot=9)
    # 4. Hardware Out A1-A5 (manual p.10) + device selector (manual p.14)
    annotate(FULL, (662, 0, 860, 50), 6,
             [(1, 683, 3, 'T'), (2, 702, 3, 'T'), (3, 720, 3, 'T'), (4, 702, 48, 'B'),
              (5, 720, 48, 'B'), (6, 790, 3, 'T'), (7, 810, 39, 'B')],
             '04a-hardware-out.png', r=34, dot=9)
    annotate(SEL, (210, 40, 964, 780), 1.5,
             [('A', 233, 145, 'L'), ('B', 660, 240, 'R'), ('C', 245, 567, 'L'),
              ('D', 245, 647, 'L'), ('E', 245, 727, 'L')],
             '04b-device-selector.png', r=42, dot=10)
    # 5. Cassette recorder (manual p.10) + Recorder Options (manual p.45)
    annotate(FULL, (676, 55, 852, 168), 7,
             [(1, 730, 74, 'T'), (2, 748, 98, 'T'), (3, 797, 99, 'T'), (4, 693, 117, 'L'),
              (5, 712, 128, 'L'), (6, 692, 162, 'B'), (7, 717, 162, 'B'), (8, 743, 162, 'B'),
              (9, 775, 162, 'B'), (10, 803, 162, 'B'), (11, 846, 110, 'R')],
             '05a-cassette-recorder.png', r=46, dot=10)
    annotate('p45-recorder-options.png', (0, 0, 1056, 398), 1.4,
             [('A', 40, 90, 'L'), ('B', 40, 155, 'L'), ('C', 60, 213, 'L'), ('D', 150, 262, 'B'),
              ('E', 730, 242, 'R'), ('F', 150, 333, 'B'), ('G', 520, 345, 'B'), ('H', 720, 333, 'B')],
             '05b-recorder-options.png', r=42, dot=10)
    # 6. Special FX + External FX Return (manual p.10)
    annotate(FULL, (855, 30, 967, 170), 8,
             [(1, 866, 66, 'L'), (2, 952, 66, 'R'), (3, 866, 123, 'L'), (4, 866, 146, 'L'),
              (5, 930, 163, 'B')],
             '06-special-fx.png', r=40, dot=10)
    # 7. Master section (manual p.10)
    annotate(FULL, (662, 172, 967, 453), 4,
             [(1, 676, 190, 'L'), (2, 676, 209, 'L'), (3, 680, 245, 'L'), (4, 680, 275, 'L'),
              (5, 676, 299, 'L'), (6, 676, 315, 'L'), (7, 676, 331, 'L'), (8, 674, 410, 'L'),
              (9, 697, 372, 'L', 760), (10, 760, 447, 'B'), (11, 912, 447, 'B')],
             '07-master-section.png', r=44, dot=10)
