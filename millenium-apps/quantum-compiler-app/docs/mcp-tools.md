# MCP Tool Catalog

## Core Compilation

| Tool | Arguments | Returns |
|------|-----------|---------|
| `compile` | `observable: str, dps: int = 50` | Full compilation result with trace |
| `compile_all` | `dps: int = 50` | All 36 formulas compiled with summary |
| `verify` | `formula_name: str, experimental_value: float?` | Comparison to experiment |

## Register & Grammar

| Tool | Arguments | Returns |
|------|-----------|---------|
| `lookup_register` | `n: int, dps: int = 100` | γ_n value + metadata + formulas using it |
| `apply_grammar` | `rule: str, operands: list, normalization: str` | Grammar rule evaluation |

## Correspondence & Transposition

| Tool | Arguments | Returns |
|------|-----------|---------|
| `check_correspondence` | `concept: str, domain: str` | Domain image + status |
| `find_blank_cells` | — | All BLANK/PARTIAL cells (research targets) |
| `transpose` | `concept: str` | Additive ↔ multiplicative bridge |

## Capacitor

| Tool | Arguments | Returns |
|------|-----------|---------|
| `read_capacitor` | — | Current state summary |
| `update_capacitor` | `finding: dict` | Self-Adjust-Trim-Amplify result |

## Simulation

| Tool | Arguments | Returns |
|------|-----------|---------|
| `simulate_modular_flow` | `n: int, t: float` | Tomita-Takesaki flow on state |n⟩ |
| `compute_matrix_element` | `n: int, m: int?, operator: str` | ⟨n|O|m⟩ in BC algebra |

## Health

| Tool | Arguments | Returns |
|------|-----------|---------|
| `health_status` | — | Self-healing runtime status |
