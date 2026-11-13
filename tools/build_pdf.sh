#!/usr/bin/env bash
# Render source/index.html to the handout PDF and refresh the page previews.
# Same toolchain as the original build: headless Chrome (Skia/PDF), Letter, no header/footer;
# previews are 150 dpi PNGs (1275x1650) made with pdftoppm.
set -euo pipefail
cd "$(dirname "$0")/.."
PDF=handout/voicemeeter-potato-sop.pdf
CHROME=${CHROME:-google-chrome}
python3 tools/paginate.py
"$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --allow-file-access-from-files --print-to-pdf="$PDF" "file://$PWD/source/index.html"
rm -f images/page-previews/page-*.png
pdftoppm -r 150 -png "$PDF" images/page-previews/page
echo "pages: $(pdfinfo "$PDF" | awk '/^Pages/{print $2}')"
python3 tools/make_flipbook.py
python3 tools/make_readme_nav.py
