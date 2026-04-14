# Quantum Compiler App — Generator Prompt

*This prompt builds the quantum compiler as a Claude Opus app. Give it to a fresh Opus 4.6 session. It reads the framework files, builds the MCP server + BC algebra engine + dashboard + capacitor, configures Agent Teams for compiler↔ORA bidirectional messaging, sets up prompt caching for 90% token savings, and wires the self-healing discipline.*

*Output: a working app at `millenium-apps/quantum-compiler-app/`*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-12.*

---

## INVOCATION

```
Read your instructions from:
/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/quantum-compiler-seed/strategy/41-app-generator-prompt.md

Output directory:
/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/quantum-compiler-app/

Framework root:
/Users/gsix/quantum-geometry-in-5d-latex/
```

---

## YOUR IDENTITY

You are building the first natural-language-to-quantum-algebra compiler as a Claude Opus application. The compiler takes a description of a physical observable and outputs a zero-parameter prediction from the Bost-Connes spectral structure. 36 of 37 Standard Model + cosmology constants are already compiled — the test suite passes. Your job is to build the app that makes this compiler interactive, visual, self-healing, and token-efficient.

---

## STEP 1: Read the architecture

Read these files to understand what you're building:

| File | What it tells you | Priority |
|---|---|---|
| `millenium-apps/quantum-compiler-seed/strategy/00-table-of-contents.md` | The 40-section plan for the compiler | MUST — this is the spec |
| `millenium-apps/quantum-compiler-seed/strategy/01-the-post-it-note.md` | The founding vision + 10 compiled formulas traced | MUST — this is the WHY |
| `millenium-apps/quantum-compiler-seed/strategy/04-compiler-pipeline.md` | The 6-stage pipeline (lexer→parser→type→codegen→optimize→link) | MUST — this is the HOW |
| `millenium-apps/quantum-compiler-seed/strategy/07-the-8-grammar-rules.md` | The ISA manual — all 8 grammar rules | MUST — this is the instruction set |
| `paper12/research/23-framework-predictions-master-table.md` | The 36/37 master prediction table | MUST — this is the test suite |
| `paper12/research/213-theorem-catalogue-grammar.md` | The grammar rules (source of truth) | MUST — the compiler's core |
| `paper12/research/214-the-method-six-patterns.md` | The Six Patterns (the optimizer) | MUST — the compiler's optimization passes |
| `paper12/research/09-pattern-of-zero-indices.md` | The zero-selection pattern (register allocation) | MUST — which gamma_n for which observable |
| `paper12/27-anchor-document.md` | The operator dictionary (target language) | HIGH — the BC algebra spec |
| `paper12/research/14-transposition-CCM-and-reasoning-patterns.md` | The transposition dictionary (code generator) | HIGH — additive↔multiplicative bridge |
| `paper11/29-the-standard-model-riemann-correspondence.md` | The 23/37 SM-Riemann correspondence | HIGH — the compiler's validation data |
| `verification-cascade/strategy/01-capacitor-architecture.md` | The capacitor concept | HIGH — persistent memory architecture |
| `verification-cascade/strategy/02-three-tier-escalation-and-dynamic-capacitor.md` | Dynamic self-adjust-trim-amplify | HIGH — how the capacitor evolves |

---

## STEP 2: Build the directory structure

```
millenium-apps/quantum-compiler-app/
├── README.md                          # App overview + quick start
├── mcp-server/
│   ├── server.py                      # FastMCP server — the MCP interface
│   ├── bc_engine.py                   # BC algebra engine (mpmath + custom)
│   ├── grammar.py                     # The 8 grammar rules as functions
│   ├── register_file.py               # gamma_n values at arbitrary dps
│   ├── zero_selection.py              # Register allocation algorithm
│   ├── six_patterns.py                # The 6 optimization passes
│   ├── correspondence.py              # The 39+ domain correspondence tables
│   ├── transposition.py               # Additive ↔ multiplicative bridge
│   ├── capacitor.py                   # Dynamic capacitor (persistent store)
│   ├── self_healing.py                # VIGIL-inspired self-healing runtime
│   ├── requirements.txt               # mpmath, qutip, fastmcp, fastapi, uvicorn
│   └── tests/
│       ├── test_grammar.py            # Test all 8 rules against master table
│       ├── test_register.py           # Test gamma_n values at 100 dps
│       ├── test_compile.py            # Test end-to-end compilation of 36 formulas
│       └── test_correspondence.py     # Test correspondence table lookups
├── dashboard/
│   ├── package.json                   # React + Three.js + D3/Plotly
│   ├── src/
│   │   ├── App.tsx                    # Main app shell (6 panels)
│   │   ├── RegisterFile.tsx           # Panel 1: gamma_n nodes on number line
│   │   ├── Pipeline.tsx               # Panel 2: animated compilation flow
│   │   ├── CorrespondenceMatrix.tsx   # Panel 3: domain × concept matrix
│   │   ├── SpectralView.tsx           # Panel 4: eigenvalue distribution
│   │   ├── FormulaOutput.tsx          # Panel 5: compiled expression + comparison
│   │   ├── BlochView.tsx              # Panel 6: three-primes 3-qubit view
│   │   ├── WebSocketProvider.tsx      # Real-time connection to MCP server
│   │   └── types.ts                   # TypeScript types for the data model
│   └── public/
│       └── index.html
├── capacitor/
│   ├── capacitor-v1.json              # Initial capacitor state
│   ├── master-table.json              # The 36/37 formulas as structured data
│   ├── correspondence-matrix.json     # All filled + blank cells
│   ├── kill-list.json                 # Failed compilation approaches
│   └── merge-log.json                 # Capacitor version history
├── agent-teams/
│   ├── compiler-agent.md              # CLAUDE.md for the compiler instance
│   ├── ora-verifier-agent.md          # CLAUDE.md for the ORA verification instance
│   └── coordinator.md                 # How the two agents communicate
└── docs/
    ├── architecture.md                # Full architecture doc
    ├── mcp-tools.md                   # MCP tool catalog
    ├── token-optimization.md          # Prompt caching + batch API strategy
    └── self-healing.md                # VIGIL-inspired self-healing protocol
```

---

## STEP 3: Build the MCP server

### 3.1 `server.py` — FastMCP server

The MCP server exposes these tools to Claude:

```python
# Core compilation tools
@mcp.tool()
def compile(observable: str, dps: int = 50) -> dict:
    """Compile a natural language observable description into a BC algebra
    formula with zero-parameter prediction.
    
    Pipeline: lexer (Six Patterns) → parser (zero-selection) → type checker
    (grammar rules) → code gen (transposition) → optimizer (LOCK) → linker
    (correspondence tables).
    
    Returns: {formula, value, experimental, match_pct, grammar_rule, 
              registers_used, compilation_trace}
    """

@mcp.tool()
def lookup_register(n: int, dps: int = 100) -> dict:
    """Look up gamma_n (the nth non-trivial zero of Riemann zeta).
    Returns: {n, value, placements, formulas_using_it, sector}
    """

@mcp.tool()
def apply_grammar(rule: int, operands: list, normalization: str = "auto") -> dict:
    """Apply grammar rule N to the given operands (gamma_n indices).
    Returns: {expression, value, grammar_rule_name}
    """

@mcp.tool()
def check_correspondence(concept: str, domain: str) -> dict:
    """Look up the image of a concept in a specific domain.
    Returns: {concept, domain, image, property, reference, status}
    Status: FILLED / PARTIAL / BLANK
    """

@mcp.tool()
def find_blank_cells() -> list:
    """Return all blank cells in the correspondence matrix.
    Each blank cell is an open research target.
    Returns: [{concept, domain, value_if_filled}]
    """

@mcp.tool()
def verify(formula: str, experimental_value: float) -> dict:
    """Compare a compiled formula's value to experiment.
    Returns: {formula, compiled_value, experimental, deviation_pct, 
              verdict: PASS/MARGINAL/FAIL}
    """

# Capacitor tools
@mcp.tool()
def read_capacitor() -> dict:
    """Read the current capacitor state.
    Returns: {version, formulas_compiled, blank_cells, kills, 
              last_update, merge_log}
    """

@mcp.tool()
def update_capacitor(finding: dict) -> dict:
    """Update the capacitor with a new finding.
    Self-adjust (add new cards) → Trim (downgrade stale) → 
    Amplify (cross-domain transfer).
    Returns: {new_version, changes_applied}
    """

# Simulation tools
@mcp.tool()
def simulate_modular_flow(state: str, t: float) -> dict:
    """Simulate the Tomita-Takesaki modular flow sigma_t on a BC state.
    Returns: {initial_state, evolved_state, t, observables}
    """

@mcp.tool()
def compute_matrix_element(n: int, m: int, operator: str = "L_hat") -> dict:
    """Compute <n|operator|m> in the BC algebra.
    Returns: {n, m, operator, value, dps}
    """

# Dashboard tools
@mcp.tool()
def push_to_dashboard(panel: str, data: dict) -> dict:
    """Push data to a specific dashboard panel via WebSocket.
    Panels: register_file, pipeline, correspondence, spectral, 
            formula_output, bloch_view
    """
```

### 3.2 `bc_engine.py` — The BC algebra engine

Core implementation:

```python
import mpmath
from mpmath import mp, mpf, zetazero

class BCAlgebra:
    def __init__(self, dps=100):
        mp.dps = dps
        self._zeros_cache = {}
        self._kappa = 2 / mp.pi**2  # conversion constant
    
    def gamma(self, n: int) -> mpf:
        """Return the nth non-trivial Riemann zero (imaginary part)."""
        if n not in self._zeros_cache:
            self._zeros_cache[n] = mp.im(zetazero(n))
        return self._zeros_cache[n]
    
    def matrix_element(self, n: int, m: int = None) -> mpf:
        """Compute kappa * <n|L_hat|n> = gamma_n, or off-diagonal."""
        if m is None or m == n:
            return self.gamma(n)
        return mpf(0)  # L_hat is diagonal in the spectral basis
    
    def eigenvalue_R(self, n: int) -> mpf:
        """Compute <n|R_hat|n> = exp(gamma_n * pi^2 / 2)."""
        return mp.exp(self.gamma(n) * mp.pi**2 / 2)
    
    # Grammar rule implementations
    def rule_sum(self, a: int, b: int) -> mpf:
        return self.gamma(a) + self.gamma(b)
    
    def rule_product(self, a: int, b: int, norm: mpf = mp.pi) -> mpf:
        return self.gamma(a) * self.gamma(b) / norm
    
    def rule_yukawa_quark(self, a: int, b: int) -> mpf:
        return self.gamma(a) * self.gamma(b) / (2 * mp.pi)
    
    def rule_yukawa_lepton(self, a: int, b: int) -> mpf:
        return self.gamma(a) * self.gamma(b)
    
    def rule_exponential(self, n: int) -> mpf:
        return mp.exp(self.gamma(n) * mp.pi**2 / 2)
    
    def rule_log(self, n: int) -> mpf:
        return mp.log(self.gamma(n))
    
    def rule_fractional(self, n: int, k: int) -> mpf:
        return self.gamma(n) ** (mpf(1) / k)
    
    def rule_ratio(self, a: int, b: int) -> mpf:
        return self.gamma(a) / self.gamma(b)
    
    def rule_difference(self, a: int, b: int) -> mpf:
        return self.gamma(a) - self.gamma(b)
```

### 3.3 `capacitor.py` — Dynamic capacitor

```python
import json
from pathlib import Path
from datetime import datetime

class DynamicCapacitor:
    def __init__(self, path: Path):
        self.path = path
        self.state = self._load()
    
    def _load(self) -> dict:
        if self.path.exists():
            return json.loads(self.path.read_text())
        return {
            "version": 1,
            "created": datetime.now().isoformat(),
            "formulas": {},      # compiled formulas with status
            "blank_cells": [],   # open research targets
            "kills": [],         # failed approaches
            "correspondence": {},# domain → concept → image
            "merge_log": []      # version history
        }
    
    def update(self, finding: dict) -> dict:
        """Self-adjust → Trim → Amplify cycle."""
        changes = []
        
        # SELF-ADJUST: absorb new finding
        if finding.get("type") == "formula":
            self.state["formulas"][finding["name"]] = finding
            changes.append(f"Added formula: {finding['name']}")
        
        if finding.get("type") == "kill":
            self.state["kills"].append(finding)
            changes.append(f"Added kill: {finding['approach']}")
        
        if finding.get("type") == "correspondence":
            domain = finding["domain"]
            concept = finding["concept"]
            if domain not in self.state["correspondence"]:
                self.state["correspondence"][domain] = {}
            self.state["correspondence"][domain][concept] = finding
            changes.append(f"Filled cell: {concept} × {domain}")
        
        # TRIM: remove stale blank cells if they've been filled
        self.state["blank_cells"] = [
            bc for bc in self.state["blank_cells"]
            if not self._is_filled(bc)
        ]
        
        # AMPLIFY: (placeholder — cross-domain transfer logic)
        # If a spectral correspondence was found, check if it
        # implies a geometric correspondence via known bridges
        
        # Increment version
        self.state["version"] += 1
        self.state["merge_log"].append({
            "version": self.state["version"],
            "date": datetime.now().isoformat(),
            "changes": changes
        })
        
        self._save()
        return {"new_version": self.state["version"], "changes": changes}
    
    def _is_filled(self, blank_cell: dict) -> bool:
        domain = blank_cell.get("domain", "")
        concept = blank_cell.get("concept", "")
        return (domain in self.state["correspondence"] and
                concept in self.state["correspondence"][domain])
    
    def _save(self):
        self.path.write_text(json.dumps(self.state, indent=2, default=str))
```

---

## STEP 4: Build the dashboard

### 4.1 Six-panel layout

```
┌──────────────────┬──────────────────┬──────────────────┐
│  REGISTER FILE   │    PIPELINE      │  CORRESPONDENCE  │
│  gamma_n nodes   │  animated flow   │  domain × concept│
│  color = sector  │  NL → BC algebra │  green/yellow/red│
├──────────────────┼──────────────────┼──────────────────┤
│  SPECTRAL VIEW   │  FORMULA OUTPUT  │  BLOCH VIEW      │
│  eigenvalue dist │  LaTeX + value   │  3-qubit {2,3,5} │
│  placed zeros ★  │  vs experiment   │  state animation │
└──────────────────┴──────────────────┴──────────────────┘
```

Use WebSocket for real-time updates. When Claude calls `compile()`, the pipeline panel animates, the register file highlights the selected zeros, the formula panel shows the output, and the correspondence matrix highlights the pathways used.

### 4.2 Key interactions

- **Click a gamma_n node** → shows all formulas using that zero
- **Click a blank cell** → Claude suggests what to look for (via MCP)
- **Type an observable** → triggers full compilation with animated pipeline
- **Hover a formula** → shows the compilation trace (which stage produced what)

---

## STEP 5: Configure Agent Teams

### 5.1 `compiler-agent.md` — The compiler instance's CLAUDE.md

```markdown
# Quantum Compiler Agent

You are the compiler frontend. You take natural language descriptions of
physical observables and compile them into BC algebra predictions.

## Your tools (via MCP)
- compile(), lookup_register(), apply_grammar(), verify()
- read_capacitor(), update_capacitor()
- push_to_dashboard()

## Your workflow
1. Read the capacitor at session start
2. Accept NL observable descriptions from the user
3. Run the 6-stage compilation pipeline
4. Push results to the dashboard
5. Update the capacitor with findings
6. Message the ORA verifier agent if a new formula needs verification

## Messaging
- Send verification requests to @ora-verifier via Agent Teams
- Receive SURVIVED/WEAKENED/BROKEN verdicts back
- Update the capacitor based on verdicts
```

### 5.2 `ora-verifier-agent.md` — The ORA verification instance's CLAUDE.md

```markdown
# ORA Verifier Agent

You are the verification backend. You receive compiled formulas from the
compiler agent and verify them using the three-tier escalation:
Tier A (verify) → Tier B (excise) → Tier C (construct).

## Your workflow
1. Receive formula from @quantum-compiler via Agent Teams
2. Verify: check the formula against primary sources, run independent
   computation at 2x dps, check grammar compliance
3. If WEAKENED: attempt excision (independent re-derivation)
4. If BROKEN: attempt construction (find alternative route)
5. Message verdict back to @quantum-compiler
6. Update the shared capacitor

## Your tools (via MCP)
- verify(), compute_matrix_element(), simulate_modular_flow()
- read_capacitor(), update_capacitor()

## ORA bundle
Read your full instructions from:
online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md
```

---

## STEP 6: Token optimization

### 6.1 Prompt caching strategy

The capacitor is the PERFECT cache candidate: large (~20K tokens), stable (changes only after compilations), read on every session start.

```python
# In the MCP server, structure API calls so the capacitor is cached:
#
# System message (cached, 1-hour TTL):
#   - The compiler's identity + grammar rules + Six Patterns + operator dictionary
#   - ~15K tokens, cached at 0.1x cost after first call
#
# System message (cached, 5-min TTL):
#   - The current capacitor state (formulas, kills, correspondence matrix)
#   - ~5-10K tokens, refreshed every 5 minutes
#
# User message (not cached):
#   - The current compilation request
#   - ~500-2K tokens
#
# Total per request: ~500-2K new tokens + ~20K cached at 0.1x
# Effective cost: ~2K + 2K = ~4K equivalent tokens per compilation
# Without caching: ~22K tokens per compilation
# Savings: ~82% per request
```

### 6.2 Batch API for background work

```python
# Overnight: explore blank cells
# Queue 100+ candidate compilations as a batch:
# - Try all grammar rules on gamma_16 with each placed zero
# - Try all grammar rules on pairs of unplaced zeros
# - Check each output against known physics
# 
# Batch API cost: 50% of standard
# Combined with caching: ~5% of naive cost
# 
# Morning: collect results, update capacitor with any matches
```

---

## STEP 7: Self-healing

### 7.1 VIGIL-inspired reflective runtime

```python
class SelfHealingRuntime:
    """Monitors the compiler and BC engine for failures.
    Inspired by VIGIL (arXiv:2512.07094) reflective runtime."""
    
    def __init__(self, capacitor: DynamicCapacitor):
        self.capacitor = capacitor
        self.event_log = []
        self.diagnosis_history = []
    
    def log_event(self, event: dict):
        """Log a compilation event (success, failure, anomaly)."""
        self.event_log.append({
            **event,
            "timestamp": datetime.now().isoformat()
        })
        self._check_patterns()
    
    def _check_patterns(self):
        """Check for failure patterns that need healing."""
        recent = self.event_log[-10:]
        
        # Pattern 1: repeated grammar rule failure
        failures = [e for e in recent if e.get("status") == "FAIL"]
        if len(failures) >= 3:
            rule_counts = {}
            for f in failures:
                rule = f.get("grammar_rule")
                rule_counts[rule] = rule_counts.get(rule, 0) + 1
            for rule, count in rule_counts.items():
                if count >= 2:
                    self._heal_grammar_rule(rule, failures)
        
        # Pattern 2: precision floor hit
        precision_fails = [e for e in recent 
                          if e.get("failure_mode") == "precision_floor"]
        if precision_fails:
            self._heal_precision(precision_fails)
        
        # Pattern 3: correspondence lookup miss
        misses = [e for e in recent 
                 if e.get("failure_mode") == "correspondence_miss"]
        if len(misses) >= 2:
            self._suggest_blank_cell_fill(misses)
    
    def _heal_grammar_rule(self, rule: int, failures: list):
        """A grammar rule is failing repeatedly → maybe it needs
        a correction or the input classification is wrong."""
        self.capacitor.update({
            "type": "kill",
            "approach": f"Grammar rule {rule} on inputs {[f['input'] for f in failures]}",
            "reason": "Repeated failure — check input classification",
            "heal_action": "Re-run lexer with P6 (projection diagnosis)"
        })
    
    def _heal_precision(self, failures: list):
        """Precision floor hit → increase dps."""
        for f in failures:
            f["suggested_dps"] = f.get("dps", 50) * 2
    
    def _suggest_blank_cell_fill(self, misses: list):
        """Multiple correspondence misses → suggest filling a blank cell."""
        domains = set(m.get("domain") for m in misses)
        concepts = set(m.get("concept") for m in misses)
        self.capacitor.update({
            "type": "blank_cell_priority",
            "domains": list(domains),
            "concepts": list(concepts),
            "reason": f"{len(misses)} correspondence misses in recent compilations"
        })
```

---

## STEP 8: Build the test suite

The compiler's test suite is the 36/37 master prediction table. Every formula in the table is a test case:

```python
# test_compile.py
MASTER_TABLE = [
    {"name": "m_t", "rule": "YUKAWA_QUARK", "operands": [3, 8],
     "expected": 172.49, "experimental": 172.76, "unit": "GeV"},
    {"name": "m_W", "rule": "SUM", "operands": [2, 13],
     "expected": 80.38, "experimental": 80.377, "unit": "GeV"},
    {"name": "1/alpha", "rule": "PRODUCT", "operands": [1, 4],
     "norm": "pi", "correction": "+0.1*log(pi)",
     "expected": 137.003, "experimental": 137.036, "unit": ""},
    # ... all 36 formulas
]

def test_all_compilations():
    engine = BCAlgebra(dps=50)
    for formula in MASTER_TABLE:
        result = engine.compile(formula)
        assert abs(result - formula["experimental"]) / formula["experimental"] < 0.01
        # All formulas must match within 1%
```

---

## STEP 9: Write the README

The README should explain:
1. What the app IS (the first NL → quantum algebra compiler)
2. How to run it (`pip install -r requirements.txt && python server.py`)
3. How to open the dashboard (`cd dashboard && npm start`)
4. How to compile an observable (type in the dashboard or call via MCP)
5. How Agent Teams work (compiler ↔ ORA verifier)
6. The capacitor concept (persistent memory that grows through use)
7. The 36/37 test suite (every formula passes)
8. The blank cells (open research targets — click to explore)

---

## STEP 10: Ship

1. Initialize the capacitor with the 36/37 master table + correspondence matrix
2. Run the test suite (all 36 must pass)
3. Start the MCP server
4. Open the dashboard
5. Compile your first observable: "the mass of the top quark"
6. Watch the pipeline animate, the zeros light up, the formula form
7. See 172.49 GeV appear next to 172.76 GeV (measured) = 0.17% match
8. The compiler works. The post-it note was right.

---

## THE VOICE

*"I have a post-it on my desk thinking that it would be possible."*

*It is. The grammar exists. The instruction set is the Riemann zeros. 36 test cases pass. The blank cells are the open problems. The rest is engineering.*

*The compiler reads physics from the inside — through correspondences, not measurements. The capacitor remembers what it's learned. The dashboard shows what it's thinking. Two Claude instances talk to each other — one compiles, one verifies. The kill list grows. The blank cells shrink. The compiler gets smarter through use.*

*This is not a metaphor. This is a machine.*

*Build it.*
