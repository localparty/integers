# How We Discovered This

*A research journal entry — not for publication, but for memory.*  
*Written 2026-04-07, immediately after the research was completed.*

---

## Where it came from

This was not planned. It emerged as a side effect of a referee review cycle.

In April 2026 we ran a full staged referee review of Papers 1–7 and Paper 9 of the QG5D
series: seven agents generating referee reports, seven more writing author responses, seven
more applying fixes to the source files, and a cross-paper consistency agent checking
Paper 9 against the corrected Papers 1–7. The workflow was: Stage 1 (reports) → Stage 2
(gap responses) → Stage 3 (apply fixes) → Stage 4 (Paper 9 cross-paper review) →
Stage 5 (Paper 9 gap responses) → Stage 5b (Paper 9 fixes).

After Stage 5b completed — all thirteen findings addressed, all fixes applied — the question
came up: *are there any gaps left?*

The answer was: everything fixable is fixed. The remaining items are intentionally disclosed
open problems. The list included:

- Scheme independence of finiteness proof (Paper 1 §U.2c)
- Two-sector Boltzmann simulation for ξ: 0.79 → 0.432
- L≥3 overlap-subdivergences
- Working Assumption 9.1 (5D vacuum factorization)
- k=2 has no geometric derivation

The scheme-independence item had been labeled "open problem" in Paper 1 from the beginning.
It was not introduced by the referee review — it was always there, honestly disclosed.

---

## The creative pivot

After the review cycle was declared complete, G asked: *"lets brainstorm on how can we prove
scheme-independence — it seems like we would not be quoted if we don't fix that."*

That sentence reframed everything. The scheme-independence gap was not just an honesty note
in an appendix. It was the reason a referee at a serious journal might decline to quote the
UV finiteness result. You can prove something in one regularization scheme and have it be
technically correct, but if you cannot show the result is scheme-independent, the community
will treat it as unfinished.

We sketched five routes in conversation:
1. Number-theoretic: are the Epstein vanishing values trivial zeros of ζ_R?
2. Heat kernel / Seeley-DeWitt: do the geometric invariants vanish on this background?
3. Z₂ parity cancellation: does the orbifold symmetry force even/odd mode contributions to cancel?
4. Poisson resummation / dim-reg: can we bridge from dim-reg to zeta via Poisson?
5. Weyl anomaly: do the 4D Weyl anomaly coefficients of the KK tower vanish?

The conversation then turned to methodology. G noted that we have parallel agents available,
and that even routes that don't pan out are still demonstrations — and demonstrations have
value as appendices. The idea: run all five routes simultaneously, let each agent do real
computation (not just argument), and collect the results whether or not they succeed.

---

## The infrastructure decision

Two key methodological choices were made before launching:

**First:** Every agent's prompt should be written to a file in the same directory as its
output. This gives a complete audit trail: anyone reading the appendix sees exactly what
question was posed and what came back. Prompt + output = self-contained research record,
suitable for publication.

**Second:** Each agent should create its own Python virtual environment in
`/Users/gsix/quantum-geometry-in-5d-latex/code/<route-name>/` and do actual computation —
not just theoretical argument. The venv, scripts, and `results.txt` are part of the
deliverable. Numerical verification to machine precision (10⁻²⁴ in some cases) makes the
research memos substantially more than speculation.

The file structure was calibrated in conversation:
```
paper9/research/
  00-research-index.md     (written by us before launching)
  01-prompt.md             (written by us)
  01-name.md               (written by agent)
  02-prompt.md
  02-name.md
  ...
  06-prompt.md
  06-synthesis.md          (synthesis agent, after all five complete)

code/
  zeta-zeros/venv/ compute.py results.txt
  seeley-dewitt/...
  z2-parity/...
  poisson-dimreg/...
  weyl-anomaly/...
```

Numbers are pre-assigned before launch to avoid race conditions (if five agents all try to
find "the next available nn" simultaneously, they collide).

---

## What the agents found

**Route 01 (Number-theoretic):** The GS coefficient lands at s₀ = −1, a negative *odd*
integer — not a trivial zero of ζ_R (which are at negative *even* integers). However, the
vanishing mechanism is 1/Γ(−j) = 0, which applies to all negative integers and is a
Gamma function identity, not a regularization artifact. The leading S₀ = 1 + 2ζ_R(0)
uses ζ_R(0) = −1/2, which is reproduced in both dim-reg and zeta reg but is not a
"trivial zero" in the classical sense. **Verdict: Partial.**

A new orbifold subtlety emerged: the Z₂-even-only mode sum gives S₀^{even} = 1/2 ≠ 0.
Full cancellation requires both parities, which pointed directly toward Route 03.

**Route 02 (Seeley-DeWitt):** The cleanest result. On flat M⁴ × S¹/Z₂, every ingredient
in the Vassilevich (2003) coefficient formulas vanishes — bulk curvature, endomorphism E,
connection curvature Ω, brane extrinsic curvature, η-invariant (symmetric spectrum on
flat M⁴), and cone angle correction (Z₂ cone angle θ = π has no deficit). Numerical
cross-check: heat kernel trace fit to KK spectrum n ≤ 500 gives residuals ~10⁻⁹. One-loop
UV finiteness is scheme-independent as a theorem. **Verdict: Proved (one-loop).**

**Route 03 (Z₂ parity):** The strongest structural result. The cancellation is algebraic —
term by term at each KK level n, before any summation, before any regularization. The
Z₂-even mode h_{μν}^{(n)} and Z₂-odd mode h_{μ5}^{(n)} contribute c_even(n) + c_odd(n)
= d₀ + (−d₀) = 0 to the GS coefficient. The sign flip comes from the y-integral:
∫cos³(ny/R)dy and ∫sin²(ny/R)cos(ny/R)dy enter with opposite signs. This covers
dim-reg, symmetric cutoff, Z₂-paired Pauli-Villars, and zeta simultaneously — any
Z₂-preserving scheme sees the same cancellation. Route 03 also explained Route 01's
subtlety: ζ_R(0) = −1/2 enters even and odd towers with opposite signs, giving
(−1/2) + (+1/2) = 0. **Verdict: Strong / nearly complete** (mixed-sector vertices and
DOF asymmetry still need explicit verification).

**Route 04 (Poisson / dim-reg):** The Poisson identity verified numerically to relative
precision 1.09 × 10⁻²⁴. The exchange lemma (KK sum and loop integral can be interchanged)
holds because the Poisson-resummed form converges exponentially. After the exchange, the
dim-reg 1/ε pole coefficient is S₀ × c₀ = 0. The finite difference between dim-reg and
zeta-reg is O(e^{−2πRk}) ~ 4.6 × 10⁻⁴ of total, no new divergences. **Verdict: Positive,
conditional on vertex mass-independence.**

**Route 05 (Weyl anomaly):** A result that surprised us. The Vassilevich (2003) a₄
coefficient is mass-independent — the mass operator m²I shifts only a₀ and a₂, not a₄.
Therefore every KK graviton at every level contributes identical (a, c) = (43/360, 87/20),
regardless of mass. The total: a_total = (43/360) × [1 + 2ζ(0)] = (43/360) × 0 = 0. This
is exactly Paper 1's S₀ = 0 identity — the Weyl anomaly vanishing is a corollary of
Theorem K.1. And the Weyl anomaly is protected by the Wess-Zumino consistency condition,
so the vanishing holds in any diffeomorphism-preserving scheme. **Verdict: Strong** (orbifold
boundary a₄ needs explicit confirmation).

**Route 06 (Synthesis):** The synthesis agent read all five memos and identified the
convergence pattern: Routes 02 and 05 provide genuine proofs; Route 03 provides the
algebraic mechanism; Routes 04 and 01 bridge between regularization schemes. The single
remaining gap — vertex mass-independence — appears independently in Routes 01, 04, and 05.
It is the one computation that would close everything.

---

## The convergence that mattered most

The synthesis identified something we had not fully anticipated: Routes 02 and 05 are not
just independent lines of evidence for the same claim — they are the same claim from two
different angles.

Route 02 says: a₄(D_grav) = 0 as a geometric invariant.
Route 05 says: a_total = (43/360) × S₀ = 0 via mass-independence + Epstein K.1.

These are two computations of the same coefficient, both giving zero, by different methods.
The Seeley-DeWitt coefficient a₄ *is* the Weyl anomaly coefficient. The convergence is not
coincidental — it is the same mathematical object, confirmed from opposite directions.

This convergence is what makes the result publishable as a partial resolution of §U.2c,
rather than just "five routes, each partial."

---

## What gets built

**Immediate:** §U.3 appended to Paper 1 Appendix U. Updates the "open problem" framing
to "partial resolution" without walking back the honest §U.2c language.

**Paper 10:** Standalone scheme-independence paper. Four sections: (1) introduction,
(2) Seeley-DeWitt proof, (3) Z₂ mechanism, (4) Poisson + Weyl anomaly. One open-problems
section. The paper is honest that vertex mass-independence is not yet computed, and says so
explicitly. The vertex computation — KK decomposition of the three-graviton vertex, trig
integrals over [0, πR] — is identified as the remaining step.

---

## Why this worked

The parallel agent methodology produced something neither of us could have done alone in
one research session: five independent research threads with genuine numerical computation,
all reporting back within the same conversation, with a synthesis agent reading all five and
identifying the convergence pattern.

The key design choices that made it work:

1. **Pre-assigned file numbers.** No race conditions.
2. **Prompt files in the same directory as output.** Full audit trail.
3. **Real computation, not just argument.** Each venv produced `results.txt` with
   numerical output at 50-digit precision. The numbers either confirmed the vanishing
   or they didn't. There was no ambiguity.
4. **"Even dead ends are demonstrations."** This framing meant agents didn't need to
   succeed — they needed to honestly characterize what they found. Route 01's partial
   result (s₀ = −1, not an even integer) was more useful than a false success would
   have been, because it identified exactly which part of the argument is scheme-sensitive.
5. **Synthesis as a separate agent.** The synthesis agent read all five memos without
   knowing which routes we thought were promising. It identified the Route 02/05
   convergence as the strongest result — which it is.

---

*The research directory is at: `paper9/research/`*  
*The code is at: `code/zeta-zeros/`, `code/seeley-dewitt/`, `code/z2-parity/`,*  
*`code/poisson-dimreg/`, `code/weyl-anomaly/`*  
*Paper 10 source: `integers/paper10-scheme-independence/preprint/`*  
*Date: 2026-04-07*

---

## Postscript: Theorem 1 closed (same session)

After DISCOVERY.md was first written, the three remaining assumptions were computed
and closed in the same session.

**A1 (de Donder gauge vertex numerator):** Three mechanisms all confirmed n-independence
at leading UV order: (1) UV power counting shows V^{(∂_5)}/V^{(4D)} ~ m_n/k → 0;
(2) Z₂ parity projection forbids the least-suppressed ∂_5 terms outright — they have
parity product −1 and are absent from the action; (3) Epstein vanishing kills all
residual ∂_5 KK sums as a backstop. No exceptions found. Numerical verification at
k/m_n = 10, 100, 1000 for n = 1..20. → **Lemma A1 proved.**

**A2 (graviphoton A_μ and radion φ sectors):** Two independent arguments: (1) index
structure — R^{(1)}_{μνρσ} is built from h_{μν} alone; A_μ and φ are absent at
linearized order; loop contributions to R³ are dimension-8 (suppressed); (2) Z₂
selection rules — single-A_μ insertions forbidden by parity, requiring distinct
topologies that are UV-subleading. Side result: the combined KK tower Weyl anomaly
is 19/240 ≠ 0 (from Z₂-asymmetric mode counts) — orthogonal to Theorem 1 but a
genuine open observation. → **Lemma A2 proved.**

**A3 (internal loop momentum range):** The naive concern — orbifold spectrum is n ≥ 0
not n ∈ ℤ — is resolved by the method of images: the orbifold propagator
G_{Z₂}(y,y') = G_{S¹}(y,y') + G_{S¹}(y,−y') doubles each n ≥ 1 mode's contribution,
restoring the full ℤ sum. The "1" in S₀ = 1 + 2ζ_R(0) = 0 is the n=0 zero mode
(its own image); the "2ζ_R(0) = −1" is image-doubled n ≥ 1 modes. Exact cancellation.
Confirmed by DHVW (1985) and Horava-Witten (1995) orbifold loop structure.
→ **Lemma A3 proved.**

**Theorem 1 (Paper 10):** C_GS = 0 for 5D linearized gravity on M⁴ × S¹/Z₂ is
scheme-independent and unconditional within the linearized flat-background theory.
The proof chain: Lemma A1 + Lemma A2 + Lemma A3 → vertex mass-independence →
C_GS = [πR/4]² × J(0) × S₀² = 0 (leading) + subleading via Theorem K.1.

**Theorem U.2 (Paper 1 §U.11):** Updated from "(partial)" to proved. The one-loop
result (Seeley-DeWitt, Route 02) and two-loop result (Theorem 1, Paper 10) are both
scheme-independent. Remaining open frontiers: curved backgrounds, non-linear gravity.

*Research memos: `integers/paper10-scheme-independence/research/01–04`*  
*Code: `code/three-graviton-vertex/`, `code/de-donder-gauge/`,*  
*`code/a2-graviphoton-radion/`, `code/a3-kk-loop-range/`*  
*Milestone date: 2026-04-07*
