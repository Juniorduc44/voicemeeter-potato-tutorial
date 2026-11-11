#!/usr/bin/env python3
"""Cut single-control "button crops" for the handout from the user's real Win10 captures.

Boxes are given in the coordinates of the stitched 100 % window
(images/source-screenshots/potato-win10-full-stitched.png) and cut from the matching 1.5x
zoom capture (left / middle / right). Mapping zoom = (x - ox) * 1.5, (y - oy) * 1.5 with
the template-matched offsets below. Output = zoom crop enlarged x2 (Lanczos), so each crop
is about 3x the 100 % screen size. Nothing is drawn on them.
Run:  python3 tools/make_button_crops.py
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, 'images', 'source-screenshots')
OUT = os.path.join(ROOT, 'images', 'control-crops')
FIT = {'left': (-1, -2.3), 'middle': (802, -3), 'right': (1136.3, -6.3)}
ZS, UP = 1.5, 2.0

BTN = {  # name: (zoom capture, (x0, y0, x1, y1) in stitched 100 % coords)
    'vban': ('middle', (1031, 3, 1094, 33)),
    'audio-map-icon': ('middle', (1099, 6, 1131, 34)),
    'menu': ('right', (1460, 6, 1549, 37)),
    'help-min-close': ('right', (1550, 6, 1644, 37)),
    'a1-top': ('right', (1144, 1, 1180, 40)),
    'hardware-out-header': ('right', (1246, -4, 1458, 34)),
    'strip-name': ('left', (2, 42, 145, 84)),
    'intellipan-label-eq': ('left', (35, 100, 149, 124)),
    'intellipan-panel': ('left', (3, 124, 147, 250)),
    'comp-gate-denoiser': ('left', (0, 260, 149, 332)),
    'fx-sends': ('left', (0, 338, 149, 410)),
    'ext-fx-sends': ('left', (0, 412, 149, 475)),
    'post': ('left', (5, 386, 34, 407)),
    'strip-meter-fader': ('left', (5, 486, 100, 748)),
    'strip-a1': ('left', (103, 493, 149, 513)),
    'strip-b1': ('left', (103, 599, 149, 620)),
    'strip-mono-solo-mute': ('left', (103, 664, 149, 743)),
    'virtual-caption': ('middle', (805, 60, 1135, 92)),
    'equalizer-label': ('middle', (805, 96, 900, 122)),
    'virtual-eq': ('middle', (805, 92, 908, 262)),
    'virtual-pan': ('middle', (803, 266, 906, 334)),
    'mc': ('middle', (860, 665, 905, 690)),
    'k': ('middle', (970, 665, 1015, 690)),
    'cassette-top': ('right', (1168, 117, 1384, 156)),
    'record': ('right', (1350, 250, 1392, 278)),
    'play': ('right', (1243, 250, 1290, 278)),
    'stop': ('right', (1292, 250, 1346, 278)),
    'reverb-off': ('right', (1455, 107, 1546, 148)),
    'delay-off': ('right', (1547, 107, 1640, 148)),
    'ext-fx-return': ('right', (1455, 154, 1645, 280)),
    'bus-sel': ('right', (1146, 305, 1195, 332)),
    'bus-mode': ('right', (1146, 333, 1195, 374)),
    'bus-fx-ret': ('right', (1144, 378, 1200, 480)),
    'bus-mono-eq-mute': ('right', (1146, 488, 1195, 570)),
    'bus-a1-fader': ('right', (1143, 580, 1195, 748)),
}


def main():
    os.makedirs(OUT, exist_ok=True)
    cache = {}
    for name, (cap, (x0, y0, x1, y1)) in BTN.items():
        if cap not in cache:
            cache[cap] = Image.open(os.path.join(SS, f'potato-win10-zoom-{cap}.png')).convert('RGB')
        im = cache[cap]
        ox, oy = FIT[cap]
        zb = [round((x0 - ox) * ZS), round((y0 - oy) * ZS), round((x1 - ox) * ZS), round((y1 - oy) * ZS)]
        zb = [max(0, zb[0]), max(0, zb[1]), min(im.width, zb[2]), min(im.height, zb[3])]
        c = im.crop(zb)
        c = c.resize((round(c.width * UP), round(c.height * UP)), Image.LANCZOS)
        c.save(os.path.join(OUT, f'{name}.png'), optimize=True)
        print(f'{name:22s} {c.width}x{c.height}  from zoom-{cap} {tuple(zb)}')


if __name__ == '__main__':
    main()
