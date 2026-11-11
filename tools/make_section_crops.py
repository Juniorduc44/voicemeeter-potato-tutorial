#!/usr/bin/env python3
"""Build the "Know Your Mixer" section crops.

Main source: the user's own real screenshots of a fresh Voicemeeter Potato 3.1.3.0 (x64)
on a Windows 10 VM at 100 % display scaling (images/source-screenshots/, 2026-11-12),
stitched into one full window by tools/stitch_window.py (run that first).
Things not visible on the main window (device selector list, Recorder Options box) still
come from the official VB-Audio manual figures in images/manual-figures/ (see SOURCES.md)
and stay labelled as manual figures in the handout.

Each crop is cut from ONE source image, enlarged with Lanczos resampling (adds size for
print, not detail) and given numbered callouts. Nothing is drawn onto the screenshot
except callout badges, leader lines, target dots and section outlines.

Callout tuple: (label, x, y, side[, badge_pos]) in the SOURCE image's pixel coords.
side = L/R/T/B margin the badge sits in; badge_pos optionally fixes the badge position
along that margin (output px). Run:  python3 tools/make_section_crops.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'images')
OUT = os.path.join(ROOT, 'images', 'section-crops')
RED = (214, 40, 57); WHITE = (255, 255, 255)
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def annotate(src, box, s, callouts, out, margin='auto', r=26, minsp=62,
             boxes=(), markers=(), dot=7, zoom=None):
    """box / callouts are in `src` pixel coords. zoom=(file, x0, y0): cut the picture from
    that 1.5x zoomed capture instead - (x0, y0) is where box's top-left corner sits in it
    (found by template matching, see ZOOM below) - so fewer pixels have to be invented."""
    if zoom:
        zf, zx, zy = zoom
        zb = (zx, zy, zx + round((box[2] - box[0]) * ZS), zy + round((box[3] - box[1]) * ZS))
        im = Image.open(os.path.join(IMG, zf)).convert('RGB').crop(zb)
        src = f'{zf} crop {zb} (= {src} {box})'
        im = im.resize((round((box[2] - box[0]) * s), round((box[3] - box[1]) * s)), Image.LANCZOS)
    else:
        im = Image.open(os.path.join(IMG, src)).convert('RGB').crop(box)
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
        d.rectangle([x0 - 3, y0 - 3, x1 + 3, y1 + 3], outline=WHITE, width=7)
        d.rectangle([x0 - 1, y0 - 1, x1 + 1, y1 + 1], outline=RED, width=4)

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
    print(f'{out:28s} {can.size[0]}x{can.size[1]}  from {src} x{s if not zoom else round(s / ZS, 3)}')


REAL = 'source-screenshots/potato-win10-full-stitched.png'  # 1645x765, real Win10 capture (100 %)
# The user's three 1.5x zoomed captures of the same window (primary source for the crops).
# Callouts stay in REAL coordinates; ZOOM = where each crop box's top-left lands in the zoom
# capture (template-matched: 1.5x scale, residual <= 2 px at 100 %).
ZS = 1.5
ZL = 'source-screenshots/potato-win10-zoom-left.png'    # 1201x1151: logo + Stereo Input 1-5
ZM = 'source-screenshots/potato-win10-zoom-middle.png'  # 501x1151: VBAN + virtual inputs
ZR = 'source-screenshots/potato-win10-zoom-right.png'   # 761x1151: Hardware Out .. master
SEL = 'manual-figures/p14-a1-output-device-selector.png'   # manual p.14, 964x781
OPT = 'manual-figures/p45-recorder-options.png'            # manual p.45, 1056x398

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    # 0. Overview map: the whole real window, sections 1-7
    annotate(REAL, (0, 0, 1645, 765), 1.2,
             [(1, 172, 2, 'T'), (1, 1081, 2, 'T'), (4, 1299, 2, 'T'), (1, 1552, 2, 'T')],
             '00-overview-map.png', r=40,
             boxes=[(3, 3, 343, 39), (1030, 3, 1135, 38), (1461, 3, 1642, 38), (3, 44, 793, 762),
                    (799, 44, 1137, 762), (1142, 3, 1456, 88), (1145, 95, 1453, 281),
                    (1460, 66, 1642, 281), (1145, 286, 1642, 762)],
             markers=[(2, 400, 420), (3, 967, 405), (5, 1300, 192), (6, 1551, 186), (7, 1395, 470)])
    # 1. Top bar - left end and right end
    annotate(REAL, (0, 0, 345, 42), 3.8, [(1, 262, 37, 'B')],
             '01a-top-bar-left.png', r=34, zoom=(ZL, 2, 4))
    annotate(REAL, (1028, 0, 1645, 41), 2.4,
             [(2, 1062, 31, 'B'), (3, 1114, 31, 'B'), (4, 1195, 37, 'B'), (5, 1504, 33, 'B'),
              (6, 1566, 33, 'B'), (7, 1596, 33, 'B'), (8, 1626, 33, 'B')],
             '01b-top-bar-right.png', r=34)
    # 2. Hardware input strip 1 ("Stereo Input 1")
    annotate(REAL, (0, 40, 149, 748), 2.5,
             [(1, 5, 52, 'L'), (2, 22, 180, 'L'), (3, 148, 111, 'R'), (4, 12, 305, 'L'),
              (5, 70, 322, 'L'), (6, 147, 305, 'R'), (7, 40, 390, 'L'), (8, 122, 385, 'R'),
              (9, 12, 397, 'L'), (10, 42, 455, 'L'), (11, 25, 640, 'L'), (12, 70, 700, 'L'),
              (13, 146, 543, 'R'), (14, 146, 630, 'R'), (15, 146, 677, 'R'), (16, 146, 700, 'R'),
              (17, 146, 724, 'R')],
             '02-hardware-input-strip.png', r=38, dot=9, zoom=(ZL, 2, 63))
    # 3. Virtual inputs (numbers on the first strip, "Voicemeeter Input") + M.C / K buttons
    annotate(REAL, (803, 44, 1136, 748), 2.2,
             [(1, 807, 72, 'L'), (2, 812, 150, 'L'), (3, 812, 300, 'L'), (4, 893, 285, 'R'),
              (5, 830, 400, 'L'), (6, 822, 590, 'L', 1150), (7, 864, 543, 'L', 1060),
              (8, 864, 631, 'L', 1240), (9, 864, 677, 'L', 1330), (10, 864, 702, 'L', 1420),
              (11, 864, 724, 'L', 1510)],
             '03a-virtual-inputs.png', r=40, dot=9, zoom=(ZM, 1, 71))
    annotate(REAL, (803, 600, 1136, 740), 2.4,
             [('M.C', 864, 677, 'L'), ('K', 992, 690, 'B'), ('M.C', 1124, 677, 'R')],
             '03b-k-and-mc-buttons.png', r=40, dot=9, zoom=(ZM, 1, 906))
    # 4. Hardware Out A1-A5 (real) + device selector (manual p.14 - not open in the capture)
    annotate(REAL, (1140, 0, 1460, 90), 4,
             [(1, 1162, 4, 'T'), (2, 1195, 4, 'T'), (3, 1228, 4, 'T'), (4, 1195, 86, 'B'),
              (5, 1228, 86, 'B'), (6, 1375, 1, 'T'), (7, 1416, 1, 'T'), (8, 1300, 31, 'B'),
              (9, 1440, 31, 'B')],
             '04a-hardware-out.png', r=34, dot=9, zoom=(ZR, 3, 5))
    annotate(SEL, (210, 40, 964, 780), 1.5,
             [('A', 233, 145, 'L'), ('B', 660, 240, 'R'), ('C', 245, 567, 'L'),
              ('D', 245, 647, 'L'), ('E', 245, 727, 'L')],
             '04b-device-selector.png', r=42, dot=10)
    # 5. Cassette recorder (real) + Recorder Options (manual p.45 - a right-click box)
    annotate(REAL, (1143, 93, 1455, 282), 4.5,
             [(1, 1260, 119, 'T'), (2, 1190, 172, 'L'), (3, 1359, 162, 'T'), (4, 1176, 194, 'L'),
              (5, 1226, 216, 'L'), (6, 1179, 270, 'B'), (7, 1220, 270, 'B'), (8, 1266, 270, 'B'),
              (9, 1319, 270, 'B'), (10, 1370, 270, 'B'), (11, 1440, 190, 'R')],
             '05a-cassette-recorder.png', r=46, dot=10, zoom=(ZR, 7, 145))
    annotate(OPT, (0, 0, 1056, 398), 1.4,
             [('A', 40, 90, 'L'), ('B', 40, 155, 'L'), ('C', 60, 213, 'L'), ('D', 150, 262, 'B'),
              ('E', 730, 242, 'R'), ('F', 150, 333, 'B'), ('G', 520, 345, 'B'), ('H', 720, 333, 'B')],
             '05b-recorder-options.png', r=42, dot=10)
    # 6. Special FX + External FX Return (real)
    annotate(REAL, (1452, 66, 1645, 280), 5.5,
             [(1, 1460, 125, 'L'), (2, 1638, 125, 'R'), (3, 1460, 203, 'L'), (4, 1460, 243, 'L'),
              (5, 1580, 277, 'B')],
             '06-special-fx.png', r=40, dot=10, zoom=(ZR, 471, 104))
    # 7. Master section (real)
    annotate(REAL, (1142, 283, 1645, 763), 2.6,
             [(1, 1150, 318, 'L'), (2, 1150, 350, 'L'), (3, 1152, 415, 'L'), (4, 1152, 460, 'L'),
              (5, 1150, 502, 'L'), (6, 1150, 530, 'L'), (7, 1150, 557, 'L'), (8, 1150, 690, 'L'),
              (9, 1181, 720, 'L', 1100), (10, 1295, 763, 'B'), (11, 1545, 763, 'B')],
             '07-master-section.png', r=44, dot=10, zoom=(ZR, 6, 430))
