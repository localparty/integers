"""Quantum Compiler MCP Server — FastMCP interface.

Exposes the quantum compiler as MCP tools that Claude can call.
Handles: compilation, register lookup, grammar application,
correspondence checking, capacitor management, simulation.

Usage:
    python server.py
    # or via FastMCP:
    fastmcp run server.py
"""

import sys
import json
from pathlib import Path
from mpmath import mp, mpf, pi

from fastmcp import FastMCP

from bc_engine import BCAlgebra
from register_file import RegisterFile
from grammar import Grammar
from zero_selection import ZeroSelector
from six_patterns import SixPatterns
from correspondence import CorrespondenceLinker
from transposition import Transposer
from capacitor import DynamicCapacitor
from self_healing import SelfHealingRuntime
from master_table import MASTER_TABLE, get_by_name, get_by_sector, get_by_register

# ── Initialize ────────────────────────────────────────────────────────

CAPACITOR_PATH = Path(__file__).parent.parent / "capacitor" / "capacitor-v1.json"

mcp = FastMCP("Quantum Compiler",
              instructions="Natural-language-to-quantum-algebra compiler. "
                           "Compiles physical observables into zero-parameter "
                           "predictions from Bost-Connes spectral structure.")

engine = BCAlgebra(dps=50)
selector = ZeroSelector()
patterns = SixPatterns()
linker = CorrespondenceLinker()
transposer = Transposer()
capacitor = DynamicCapacitor(CAPACITOR_PATH)
healer = SelfHealingRuntime(capacitor)


# ── Core compilation tools ────────────────────────────────────────────

@mcp.tool()
def compile(observable: str, dps: int = 50) -> dict:
    """Compile a natural language observable description into a BC algebra
    formula with zero-parameter prediction.

    Pipeline: lexer (Six Patterns) → parser (zero-selection) → type checker
    (grammar rules) → code gen (transposition) → optimizer (LOCK) → linker
    (correspondence tables).

    Returns: formula, value, experimental, match_pct, grammar_rule,
             registers_used, compilation_trace.
    """
    mp.dps = dps + 10
    local_engine = BCAlgebra(dps=dps)

    # Try to match observable to master table
    observable_lower = observable.lower().strip()

    # Search master table for matching observable
    match = None
    for entry in MASTER_TABLE:
        name_match = entry["name"].lower().replace("_", " ")
        desc_match = entry["description"].lower()
        if (observable_lower in name_match or
                observable_lower in desc_match or
                name_match in observable_lower or
                any(word in observable_lower
                    for word in desc_match.split() if len(word) > 3)):
            match = entry
            break

    if match is None:
        healer.log_event({
            "status": "FAIL",
            "failure_mode": "no_match",
            "input": observable,
        })
        return {
            "error": f"Could not match '{observable}' to any known formula",
            "suggestion": "Try: 'top quark mass', 'fine structure constant', "
                          "'Hubble constant', 'W boson mass', etc.",
            "known_observables": [e["name"] for e in MASTER_TABLE],
        }

    # Run the 6-stage pipeline
    trace = []

    # Stage 1: Lexer (Six Patterns)
    metadata = {
        "sector": match["sector"],
        "type": match.get("unit", ""),
        "properties": [],
    }
    tokens = patterns.classify(metadata)
    trace.append({"stage": "LEXER", "tokens": tokens})

    # Stage 2: Parser (zero selection)
    parse_meta = {
        "sector": match["sector"],
        "generation": None,
        "color": "singlet",
    }
    allocation = selector.select(parse_meta)
    trace.append({"stage": "PARSER",
                  "actual_registers": match["operands"],
                  "allocation_hint": allocation})

    # Stage 3: Type checker (grammar rules)
    trace.append({"stage": "TYPE_CHECKER",
                  "rule": match["rule"],
                  "formula": match["formula_str"]})

    # Stage 4: Code generator (transposition)
    rule = match["rule"]
    if isinstance(rule, int) and rule in (1, 8):
        template = "sum" if rule == 1 else "difference"
    elif rule in (2, "3a", "3b"):
        template = "product"
    elif rule == 7:
        template = "ratio"
    elif rule == 5:
        template = "log"
    elif rule == 6:
        template = "power"
    elif rule == 4:
        template = "exponential"
    else:
        template = "product"
    code = transposer.generate_code(template)
    trace.append({"stage": "CODE_GEN", "bc_expression": code})

    # Stage 5: Optimizer (LOCK)
    result = local_engine.compile_formula(match)
    optimized = patterns.optimize(result, tokens)
    lock = patterns.lock_verify(result)
    trace.append({"stage": "OPTIMIZER",
                  "passes": optimized.get("optimization_passes", []),
                  "lock": lock})

    # Stage 6: Linker (correspondence)
    link_result = linker.link(match["name"])
    trace.append({"stage": "LINKER", "link_result": link_result})

    # Log success
    healer.log_event({
        "status": result["verdict"],
        "name": match["name"],
        "grammar_rule": match["rule"],
        "operands": match["operands"],
        "deviation_pct": result["deviation_pct"],
        "input": observable,
    })

    return {
        "name": match["name"],
        "description": match["description"],
        "formula": match["formula_str"],
        "rule": match["rule"],
        "registers_used": match["operands"],
        "compiled_value": result["compiled_value"],
        "experimental": result["experimental"],
        "deviation_pct": round(result["deviation_pct"], 6),
        "unit": result["unit"],
        "verdict": result["verdict"],
        "compilation_trace": trace,
    }


@mcp.tool()
def compile_all(dps: int = 50) -> dict:
    """Compile all 36 formulas in the master table.

    Returns: summary with pass/fail counts and per-formula results.
    """
    mp.dps = dps + 10
    local_engine = BCAlgebra(dps=dps)
    results = local_engine.compile_all()

    passed = sum(1 for r in results if r["verdict"] == "PASS")
    failed = sum(1 for r in results if r["verdict"] == "FAIL")

    return {
        "total": len(results),
        "passed": passed,
        "failed": failed,
        "pass_rate": f"{passed}/{len(results)}",
        "results": results,
    }


@mcp.tool()
def lookup_register(n: int, dps: int = 100) -> dict:
    """Look up γ_n (the nth non-trivial zero of Riemann zeta).

    Returns: n, value, placements, formulas_using_it, sector.
    """
    rf = RegisterFile(dps=dps)
    return rf.lookup(n)


@mcp.tool()
def apply_grammar(rule: str, operands: list,
                  normalization: str = "auto") -> dict:
    """Apply grammar rule to given operands (gamma_n indices).

    Rules: SUM, PRODUCT, YUKAWA_QUARK, YUKAWA_LEPTON, EXPONENTIAL,
           LOG, FRACTIONAL, RATIO, DIFFERENCE.

    Returns: expression, value, grammar_rule_name.
    """
    g = Grammar(dps=50)

    # Parse operands
    if len(operands) >= 2:
        a, b = operands[0], operands[1]
    elif len(operands) == 1:
        a = operands[0]
        b = None
    else:
        return {"error": "Need at least one operand"}

    rule_upper = rule.upper()
    try:
        if rule_upper in ("SUM", "1"):
            val = g.rule_sum(a, b)
        elif rule_upper in ("PRODUCT", "2"):
            norm = pi if normalization == "auto" else mpf(normalization)
            val = g.rule_product(a, b, norm)
        elif rule_upper in ("YUKAWA_QUARK", "3A"):
            val = g.rule_yukawa_quark(a, b)
        elif rule_upper in ("YUKAWA_LEPTON", "3B"):
            val = g.rule_yukawa_lepton(a, b)
        elif rule_upper in ("EXPONENTIAL", "4"):
            val = g.rule_exponential(a)
        elif rule_upper in ("LOG", "5"):
            power = operands[1] if len(operands) > 1 and b else 1
            val = g.rule_log(a, power)
        elif rule_upper in ("FRACTIONAL", "6"):
            p = operands[1] if len(operands) > 1 else 1
            q = operands[2] if len(operands) > 2 else 3
            val = g.rule_fractional(a, p, q)
        elif rule_upper in ("RATIO", "7"):
            val = g.rule_ratio(a, b)
        elif rule_upper in ("DIFFERENCE", "8"):
            val = g.rule_difference(a, b)
        else:
            return {"error": f"Unknown rule: {rule}"}
    except Exception as e:
        return {"error": str(e)}

    return {
        "rule": rule_upper,
        "operands": operands,
        "value": float(val),
        "value_full": str(val),
    }


@mcp.tool()
def check_correspondence(concept: str, domain: str) -> dict:
    """Look up the image of a concept in a specific domain.

    Returns: concept, domain, image, status (FILLED/PARTIAL/BLANK).
    """
    return linker.check(concept, domain)


@mcp.tool()
def find_blank_cells() -> list:
    """Return all blank cells in the correspondence matrix.

    Each blank cell is an open research target.
    """
    return linker.find_blank_cells()


@mcp.tool()
def verify(formula_name: str,
           experimental_value: float = None) -> dict:
    """Compare a compiled formula's value to experiment.

    Returns: formula, compiled_value, experimental, deviation_pct,
             verdict (PASS/FAIL).
    """
    return engine.verify(formula_name, experimental_value)


# ── Capacitor tools ───────────────────────────────────────────────────

@mcp.tool()
def read_capacitor() -> dict:
    """Read the current capacitor state.

    Returns: version, formulas_compiled, blank_cells, kills,
             last_update, merge_log.
    """
    return capacitor.read()


@mcp.tool()
def update_capacitor(finding: dict) -> dict:
    """Update the capacitor with a new finding.

    Self-adjust (add new cards) → Trim (downgrade stale) →
    Amplify (cross-domain transfer).

    finding types: 'formula', 'kill', 'correspondence', 'blank_cell_priority'.
    """
    return capacitor.update(finding)


# ── Simulation tools ──────────────────────────────────────────────────

@mcp.tool()
def simulate_modular_flow(n: int, t: float) -> dict:
    """Simulate the Tomita-Takesaki modular flow σ_t on state |n⟩.

    Returns: initial_state, evolved_state, t, phase, observables.
    """
    return engine.modular_flow(n, t)


@mcp.tool()
def compute_matrix_element(n: int, m: int = None,
                           operator: str = "L_hat") -> dict:
    """Compute ⟨n|operator|m⟩ in the BC algebra.

    Operators: L_hat (log of scaling), R_hat (scaling).
    """
    val = engine.matrix_element(n, m, operator)
    return {
        "n": n,
        "m": m if m is not None else n,
        "operator": operator,
        "value": float(val),
        "value_full": str(val),
    }


# ── Health tools ──────────────────────────────────────────────────────

@mcp.tool()
def health_status() -> dict:
    """Return the self-healing runtime's health status."""
    return healer.get_status()


@mcp.tool()
def transpose(concept: str) -> dict:
    """Look up the additive ↔ multiplicative transposition of a concept."""
    return transposer.transpose(concept)


# ── Entry point ───────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
