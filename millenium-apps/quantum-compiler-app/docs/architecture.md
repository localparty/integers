# Quantum Compiler — Architecture

## Overview

The quantum compiler transforms natural language descriptions of physical observables into zero-parameter predictions from the Bost-Connes spectral structure. It is isomorphic to a standard compiler (Dragon Book, Aho et al.):

```
SOURCE: Natural language observable
    ↓ [LEXER: Six Patterns]
TOKENS: Classified metadata
    ↓ [PARSER: Zero-selection rules]
AST: Register assignments
    ↓ [TYPE CHECKER: 8 Grammar rules]
TYPED_AST: Formula template
    ↓ [CODE GENERATOR: Transposition dictionary]
BC_EXPR: Operator expression on H_R
    ↓ [OPTIMIZER: LOCK + Six Patterns]
OPT_CODE: Verified, simplified
    ↓ [LINKER: 39+ domains]
EXECUTABLE: Multi-domain verified numerical result
```

## Components

### MCP Server (`mcp-server/`)
- `server.py` — FastMCP server exposing 14 tools to Claude
- `bc_engine.py` — BC algebra engine (mpmath + custom operators)
- `grammar.py` — The 8 grammar rules as callable functions
- `register_file.py` — γ_n values at arbitrary precision (15 placed zeros)
- `zero_selection.py` — Register allocation from observable metadata
- `six_patterns.py` — Lexer classification + optimizer passes
- `correspondence.py` — 39+ domain correspondence tables + linker
- `transposition.py` — Additive ↔ multiplicative bridge (Mellin duality)
- `capacitor.py` — Dynamic persistent memory with Self-Adjust-Trim-Amplify
- `self_healing.py` — VIGIL-inspired failure monitoring + healing
- `master_table.py` — The 36/37 master prediction table (test suite)

### Dashboard (`dashboard/`)
Six-panel React + SVG visualization:
1. **Register File** — γ_n nodes on number line (color = sector)
2. **Pipeline** — Animated compilation flow stages
3. **Correspondence Matrix** — Domain × concept grid (green/yellow/red)
4. **Spectral View** — Eigenvalue distribution with placed zeros
5. **Formula Output** — Compiled expression + comparison to experiment
6. **Bloch View** — Three-primes {2,3,5} generation structure

### Capacitor (`capacitor/`)
Persistent knowledge store:
- `capacitor-v1.json` — Current state (formulas, kills, correspondence)
- `master-table.json` — All 36/37 compiled formulas as structured data
- `correspondence-matrix.json` — Filled + blank cells
- `kill-list.json` — Failed compilation approaches
- `merge-log.json` — Version history

### Agent Teams (`agent-teams/`)
- `compiler-agent.md` — CLAUDE.md for the compiler instance
- `ora-verifier-agent.md` — CLAUDE.md for the ORA verification instance
- `coordinator.md` — Bidirectional messaging protocol

## Key Constants
- κ = 2/π² — BC scale factor
- L̂ = log R̂ — spectral operator
- R̂ eigenvalues = exp(γ_n · π²/2)
- Gauge-distinguished set: {γ₁, γ₄, γ₆, γ₈}
- Minimal conductor: 1729 = 7 × 13 × 19
