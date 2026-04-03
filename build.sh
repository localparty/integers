#!/bin/bash
# Build both papers: md → latex → pdf (with bibtex)
set -e

cd "$(dirname "$0")"

echo "=== Converting markdown to LaTeX ==="
python3 etc/md2latex.py

for paper in paper1 paper2; do
    if [ "$paper" = "paper1" ]; then
        texfile="main"
        dir="paper1/etc/arxiv"
    else
        texfile="paper2"
        dir="paper2/etc/arxiv"
    fi

    echo ""
    echo "=== Building $paper ==="
    cd "$dir"

    # Clean stale aux files
    rm -f ${texfile}.aux ${texfile}.bbl ${texfile}.blg

    # Full build cycle: pdflatex → bibtex → pdflatex → pdflatex
    pdflatex -interaction=nonstopmode ${texfile}.tex > /dev/null 2>&1 || true
    bibtex ${texfile} > /dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode ${texfile}.tex > /dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode ${texfile}.tex > /dev/null 2>&1 || true

    # Report
    errors=$(cat ${texfile}.log | grep -c "^!" || true)
    undef=$(cat ${texfile}.log | grep -c "Citation.*undefined" || true)
    pages=$(grep -o "([0-9]* pages" ${texfile}.log | tail -1 | grep -o "[0-9]*" || echo "?")
    echo "  ${texfile}.pdf: ${pages} pages, ${errors} errors, ${undef} undefined citations"

    cd - > /dev/null
done

echo ""
echo "Done. PDFs at:"
echo "  paper1/etc/arxiv/main.pdf"
echo "  paper2/etc/arxiv/paper2.pdf"
