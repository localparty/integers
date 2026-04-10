# Ledger — Prove the Riemann Hypothesis

*The compressed state of the investigation.*
*READ THIS FIRST — EVERY LINE — strategist AND executors.*
*Do NOT skim. Do NOT skip sections. INTERNALIZE every line.*
*This is the only file that carries state across sessions.*
*If you skim it, you'll re-explore dead leads, forget tools,*
*miss the context, and waste the cycle.*
*Read it like your proof depends on it. Because it does.*

*Keep this file UNDER 200 lines. Details live in leads/ and*
*strategy/. This file is an INDEX with references.*

---

## North Star

> Prove the Riemann hypothesis: all non-trivial zeros of ζ(s)
> lie on Re(s) = 1/2. Use the Integers programme's toolkit
> (Bost-Connes algebra, ITPFI factorization, bridge family,
> 387 theorems, Six Patterns) combined with any external
> constructions found via web search.

## Context

> The Integers programme (CBCBS) derives 36 physical constants
> from zero parameters via the Bost-Connes algebra at β=1.
> Yang-Mills mass gap proved. ITPFI factorization of ω₁ proved
> (three ways). Bridge family at formal lemma grade (k=2,3,4,6).
> 387 theorems catalogued. The Six Patterns are the meta-method
> that produced Yang-Mills, Integers, and BSD. RH is the
> consistency condition of the programme — the integers exist,
> the zeros should be on the line. SP1: crack RH from INSIDE
> the BC algebra.

## Who reads this

- **The Strategist** reads this FIRST at every cycle (mandatory)
- **The Executors** read this FIRST before their lead (mandatory)
- **The Adversary** reads this for context on what matters

Why executors read it: during deep web search, an executor might
find something that affects OTHER leads. Without the ledger's
context, they can't recognize strategic insights. With it, they
become scouts — reporting not just their lead's result but
cross-lead connections.

---

## The Toolkit (ALWAYS AVAILABLE — do not forget these exist)

### Files to read for full context
| File | What it gives you |
|:--|:--|
| paper12/27-anchor-document.md | CBB system, 5 axioms, zero parameters, 36 predictions |
| paper12/29-theorem-catalogue.md | 387 theorems from the full programme (use by name!) |
| paper12/research/200-rh-evidence-compendium.md | 37 R-Theorems, 15 empirical bounds |
| paper12/research/214-the-method-six-patterns.md | The Six Patterns (meta-method) |

### The Six Patterns (strategic compass)
1. **Geometric Reinterpretation** — mystery in 4D = fact in higher dim
2. **Holonomy Correspondence** — gauge phase = geometry
3. **Casimir Energy** — vacuum energy sets the scale
4. **Topological Rigidity** — discrete invariants lock results
   ⚠️ BUT: can't detect continuous perturbations (coboundary lesson!)
5. **Zeta Regularization** — compactness → discrete sums
6. **Projection** — apparent pathology = projection artifact

### G's Five Strategic Principles
**SP1.** Crack RH from INSIDE the BC algebra (not outside)
**SP2.** Transpose every theorem → the 37 R-Theorems = the LOCK
**SP3.** Quantize everything, trace discrepancies
**SP4.** Reality = projection of Riemann → deduct everything
**SP5.** Be hella explicit — document everything

### The 37 R-Theorems (the LOCK on RH)
Six categories: D(5), C(2), S(12), QM(5), GR(10), numbered(3+4)
Each forces γ_n ∈ ℝ from independent mathematical machinery.
Full list: paper12/research/200-rh-evidence-compendium.md
Key ones for current proof:
- S.5 (Källén-Lehmann + Weil): iff condition
- S.6 (Borchers): powers ITPFI
- D.1 (BC index): JLO Chern character
- QM.1 (Stone): self-adjointness chain

### Predictive grammar
linear→SUM, quadratic→PRODUCT, bilinear→PRODUCT/(2π),
exponential→exp(γ_n·π²/2), log→log(γ_n),
3rd gen=PRODUCT, 2nd=RATIO, 1st=DIFFERENCE

### Proved results (USE THESE — they're theorems)
- ITPFI: ω₁ = ⊗_p ω₁^p (research/265, proved 3 ways)
- Bridge lemmas k=2,3,4,6 (research/162, 263)
- Uniqueness: 3 sub-claims all closed (research/268)
- AE simplicity: certified N=1..20 (research/42)
- γ_E elimination from overlaps (research/28)
- Estimate 1: archimedean O(1/λ) (research/20)
- Gradient flow L.1-L.5 on H₁ (research/09-13)
- Compact resolvent on H₁ (research/09)
- CF decay ρ ≥ 4.27 uniform in N (research/35)

### Computation (179 scripts in code/)
`ls [DIRECTORY]/code/` to browse. Key scripts:
certify_k3.py, ccm_perturbation_bound.py,
r42_ae_simplicity_certified.py, r55_even_sector_ccm.py,
r40_delta_N_bound.py, cycle4_itpfi.py
mpmath: `mp.dps=50`, `zetazero(n)`, `zeta(s)`, `euler`

### Downloaded papers (in sources/)
See sources/INDEX.md. Key papers:
- CCM zeta spectral triples 2025 (Layer 1 of the proof)
- Yakaboylu 2024 (W ≥ 0 criterion)
- CCM prolate wave 2024 (Sonin space)
- Bombieri RH Clay description (official problem)

### The 18 killed approaches (DO NOT RE-EXPLORE without new reason)
Full list: paper13-rh/strategy/10-state-after-18-kills.md
Key kills: coboundary (H² can't detect continuous perturbation),
H₁ vs H_R wall (GNS spectrum = {log n} not {γ_n}),
predictions invisible (extras contribute zero to formulas)

---

## Instructions for the Strategist

**READ THIS FILE at the start of every cycle.** It tells you:
- Which leads are alive (pursue them)
- Which leads are dead and WHY (don't re-explore unless
  a NEW reason to reopen is found)
- Which leads are blocked and on WHAT (check if the blocker
  has been resolved)
- The current strongest direction
- The overall feasibility

**WRITE to this file at the end of every cycle.** Append a new
cycle section. Never delete previous cycles — they're the history.

---

## Cycle 0 — Pre-investigation

*No leads yet. The investigation begins at Cycle 1.*

**Target:** Prove RH from inside the BC algebra
**Starting feasibility:** ?/10
**Toolkit:** anchor doc, theorem catalogue (387 entries), Six
Patterns, 37 R-Theorems, 179 computation scripts, sources library
**Strategy file:** strategy/strategy-0.md (if exists)
