#!/bin/bash
# Convert each .jsx React figure to a self-contained .html file
# Usage: ./etc/jsx2html.sh [paper1|paper2|all]
set -e

cd "$(dirname "$0")/.."

convert_jsx() {
    local jsx="$1"
    local html="${jsx%.jsx}.html"
    local name=$(basename "$jsx" .jsx)
    local title=$(echo "$name" | sed 's/-/ /g; s/^[0-9]* //')

    # Extract the component name from "export default function Foo()"
    local component=$(grep -o 'export default function [A-Za-z0-9]*' "$jsx" | awk '{print $NF}')
    if [ -z "$component" ]; then
        echo "  SKIP $name (no export default function found)"
        return
    fi

    # Read the JSX source:
    # - Strip import lines (React is loaded via CDN)
    # - Strip "export default" (component is called directly)
    # - Convert \uXXXX in JSX text to actual Unicode (Babel standalone doesn't process these)
    local jsx_source=$(grep -v '^import ' "$jsx" | sed 's/^export default function /function /')
    jsx_source=$(python3 -c "
import sys, re
text = sys.stdin.read()
text = re.sub(r'\\\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), text)
sys.stdout.write(text)
" <<< "$jsx_source")

    # Write HTML header (no variable interpolation in JSX needed)
    cat > "$html" << HTMLEOF
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title}</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #f8f9fa; font-family: system-ui, -apple-system, sans-serif; }
  #root { width: 100%; max-width: 900px; padding: 20px; }
</style>
<script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
<script crossorigin src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const { useRef, useEffect, useState, useCallback, useMemo } = React;

HTMLEOF
    # Append JSX source verbatim (no shell interpolation of \u escapes)
    printf '%s\n' "$jsx_source" >> "$html"
    # Append footer
    cat >> "$html" << HTMLEOF

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(React.createElement(${component}));
</script>
</body>
</html>
HTMLEOF
    echo "  OK $name → $(basename $html)"
}

targets="${1:-all}"

if [ "$targets" = "all" ] || [ "$targets" = "paper1" ]; then
    echo "=== Paper 1 figures ==="
    for f in paper1/figures/*.jsx; do
        [ -f "$f" ] && convert_jsx "$f"
    done
fi

if [ "$targets" = "all" ] || [ "$targets" = "paper2" ]; then
    echo "=== Paper 2 figures ==="
    for f in paper2/figures/*.jsx; do
        [ -f "$f" ] && convert_jsx "$f"
    done
fi

echo ""
echo "Done. Open any .html file in a browser to view."
