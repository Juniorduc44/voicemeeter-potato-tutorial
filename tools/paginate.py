#!/usr/bin/env python3
"""Number every page footer ("Page X of N") in source/index.html and rebuild the contents
list (<div id="toc">...</div>) from the footer titles. Run before rendering (build_pdf.sh
does). Each <section class="page"> must be exactly one printed page."""
import re, html
from pathlib import Path
p = Path(__file__).resolve().parent.parent / 'source' / 'index.html'
s = p.read_text()
foot = re.compile(r'(<div class="foot"><span>)(.*?)(</span><span>)Page \d+ of \d+(</span></div>)')
n = len(foot.findall(s))
assert n == s.count('<section class="page">'), 'every page needs exactly one footer'
titles, k = [], 0
def num(m):
    global k
    k += 1
    titles.append((k, m.group(2)))
    return f'{m.group(1)}{m.group(2)}{m.group(3)}Page {k} of {n}{m.group(4)}'
s = foot.sub(num, s)
part2 = next(i for i, t in titles if t.startswith('Know Your Mixer - the map'))
groups = [('Part 1 - Set it up', [t for t in titles if 3 <= t[0] < part2]),
          ('Part 2 - Know Your Mixer', [t for t in titles if t[0] >= part2 and not t[1].startswith(('No-sound', 'Quick'))]),
          ('Help and reference', [t for t in titles if t[1].startswith(('No-sound', 'Quick'))])]
out = []
for g, items in groups:
    out.append(f'<div class="tocg">{g}</div>')
    out += [f'<div class="toci"><span>{html.escape(html.unescape(t))}</span><span>{i}</span></div>' for i, t in items]
s = re.sub(r'<div id="toc">.*?</div><!--/toc-->', '<div id="toc">' + ''.join(out) + '</div><!--/toc-->', s, flags=re.S)
p.write_text(s)
print('pages:', n)
