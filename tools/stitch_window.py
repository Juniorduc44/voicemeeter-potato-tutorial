#!/usr/bin/env python3
"""Stitch the two real Win10 captures of Voicemeeter Potato into one full-window image.

The two captures were taken separately, so the window was a few pixels different in
size: the RIGHT capture sits 799 px to the right of the LEFT one, and the layout rows
shift by 2 px (top) -> 1 px (rows 194-575) -> 0 px (bottom). We map the LEFT rows into the
RIGHT capture's row positions (only ever dropping a LEFT row that is an exact copy of its
neighbour - checked below), then join at a column inside the overlap where both captures
are pixel-identical in every row. Rows 0-1 and 767 of the RIGHT capture have no LEFT
counterpart and are cropped off, so nothing is invented.
"""
import numpy as np
from PIL import Image
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SS = ROOT / 'images' / 'source-screenshots'
DX = 799            # RIGHT x=0 == LEFT x=799
SEAM = 60           # join column, in RIGHT coordinates (overlap is identical for x 52..334)

def row_shift(y):   # LEFT row = RIGHT row + shift
    return -2 if y < 194 else (-1 if y < 576 else 0)

def main():
    L = np.asarray(Image.open(SS / 'potato-win10-left.png').convert('RGB'))
    R = np.asarray(Image.open(SS / 'potato-win10-right.png').convert('RGB'))
    rows = range(2, 767)
    src = np.array([y + row_shift(y) for y in rows])
    left = L[src, :DX + SEAM]
    right = R[2:767, SEAM:]
    # verification: the whole remaining overlap must match exactly
    ov = np.abs(L[src, DX + SEAM:].astype(int) - R[2:767, SEAM:L.shape[1] - DX].astype(int)).max()
    assert ov == 0, f'overlap mismatch {ov}'
    dropped = sorted(set(range(L.shape[0])) - set(src.tolist()))
    for r in dropped:
        if 0 < r < L.shape[0] - 1:
            same = (L[r, :DX] == L[r - 1, :DX]).all(1) | (L[r, :DX] == L[r + 1, :DX]).all(1)
            assert same.all(), f'dropped LEFT row {r} is not a duplicate'
    out = np.concatenate([left, right], axis=1)
    Image.fromarray(out).save(SS / 'potato-win10-full-stitched.png', optimize=True)
    print('stitched', out.shape[1], 'x', out.shape[0], 'dropped LEFT rows', dropped)

if __name__ == '__main__':
    main()
