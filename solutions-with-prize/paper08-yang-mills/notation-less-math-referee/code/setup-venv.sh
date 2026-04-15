#!/usr/bin/env bash
# setup-venv.sh — (re)build a clean Python venv for notation-math-referee
# computational verification. Wipes any existing .venv on every run so each
# referee session starts from a known, reproducible state.
#
# Usage:
#   bash code/setup-venv.sh
#   source code/.venv/bin/activate
#
# After activation, `python -c "import sympy, mpmath, numpy, scipy, networkx"`
# should succeed.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VENV="$HERE/.venv"
REQ="$HERE/requirements.txt"
LATEST="$ROOT/latest-run"
RUNS="$ROOT/runs"

echo "[setup-venv] working dir: $HERE"

# 0. Archive the previous run (if any) into runs/r{NN+1}/ so the new
#    referee starts with an empty latest-run/ and CANNOT read prior
#    findings — past runs live in runs/ which the prompt declares
#    out of scope.
mkdir -p "$RUNS"
if [ -d "$LATEST" ] && [ -n "$(ls -A "$LATEST" 2>/dev/null)" ]; then
  # Find highest existing rNN in runs/, increment, zero-pad to width 2.
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

# 1. Nuke any prior venv + caches so each run is reproducible.
if [ -e "$VENV" ]; then
  echo "[setup-venv] removing existing .venv"
  rm -rf "$VENV"
fi
find "$HERE" -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null || true
find "$HERE" -type d -name ".pytest_cache" -prune -exec rm -rf {} + 2>/dev/null || true

# 2. Create the venv. Prefer uv (fast); fall back to stdlib venv.
if command -v uv >/dev/null 2>&1; then
  echo "[setup-venv] creating venv with uv"
  uv venv "$VENV"
  # shellcheck disable=SC1091
  source "$VENV/bin/activate"
  echo "[setup-venv] installing requirements with uv pip"
  uv pip install -r "$REQ"
else
  echo "[setup-venv] uv not found; falling back to python3 -m venv"
  python3 -m venv "$VENV"
  # shellcheck disable=SC1091
  source "$VENV/bin/activate"
  python -m pip install --quiet --upgrade pip
  python -m pip install -r "$REQ"
fi

# 3. Smoke test.
python - <<'PY'
import sympy, mpmath, numpy, scipy, networkx, pypdf
print(f"[setup-venv] sympy={sympy.__version__} mpmath={mpmath.__version__} "
      f"numpy={numpy.__version__} scipy={scipy.__version__} "
      f"networkx={networkx.__version__} pypdf={pypdf.__version__}")
PY

echo "[setup-venv] ready. activate with: source code/.venv/bin/activate"
