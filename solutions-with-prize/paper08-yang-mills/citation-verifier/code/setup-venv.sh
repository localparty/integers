#!/usr/bin/env bash
# setup-venv.sh — (re)build a clean Python venv for citation-verifier
# and archive any prior run. Non-destructive: previous latest-run/ is
# moved to runs/r{NN}/ (zero-padded), not deleted.
#
# Usage:
#   bash code/setup-venv.sh
#   source code/.venv/bin/activate

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VENV="$HERE/.venv"
REQ="$HERE/requirements.txt"
LATEST="$ROOT/latest-run"
RUNS="$ROOT/runs"

echo "[setup-venv] working dir: $HERE"

# 0. Archive any prior latest-run/ into runs/r{NN+1}/ (non-destructive).
mkdir -p "$RUNS"
if [ -d "$LATEST" ] && [ -n "$(ls -A "$LATEST" 2>/dev/null)" ]; then
  last=$(ls -1 "$RUNS" 2>/dev/null | grep -E '^r[0-9]+$' | sed 's/^r//' | sort -n | tail -1 || true)
  next=$(printf "r%02d" $(( ${last:-(-1)} + 1 )))
  echo "[setup-venv] archiving latest-run/ -> runs/$next/"
  mv "$LATEST" "$RUNS/$next"
elif [ -d "$LATEST" ]; then
  echo "[setup-venv] removing empty latest-run/"
  rm -rf "$LATEST"
fi
mkdir -p "$LATEST"
echo "[setup-venv] fresh latest-run/ ready at $LATEST"

# 1. Wipe and rebuild venv for reproducibility.
if [ -e "$VENV" ]; then
  echo "[setup-venv] removing existing .venv"
  rm -rf "$VENV"
fi
find "$HERE" -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null || true

if command -v uv >/dev/null 2>&1; then
  echo "[setup-venv] creating venv with uv"
  uv venv "$VENV"
  # shellcheck disable=SC1091
  source "$VENV/bin/activate"
  uv pip install -r "$REQ"
else
  echo "[setup-venv] uv not found; falling back to python3 -m venv"
  python3 -m venv "$VENV"
  # shellcheck disable=SC1091
  source "$VENV/bin/activate"
  python -m pip install --quiet --upgrade pip
  python -m pip install -r "$REQ"
fi

# 2. Smoke test.
python - <<'PY'
import pypdf, requests
print(f"[setup-venv] pypdf={pypdf.__version__} requests={requests.__version__}")
PY

echo "[setup-venv] ready. activate with: source code/.venv/bin/activate"
