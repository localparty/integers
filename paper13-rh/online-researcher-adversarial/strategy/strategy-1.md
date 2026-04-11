# Strategy — Cycle 1 (tuned)

*Strategist: ORA tuned-prompt run, 2026-04-10*
*North star: prove RH from inside the Bost–Connes algebra.*

---

## Reading of the ledger

**What is alive.** No live leads carried over. The ledger is fresh
for Cycle 1 under the tuned prompt; §G was empty before this file.

**What is dead.** 19 killed approaches in §F, organized along a
single arc: every one of K1–K19 dies on the **H₁-vs-H_R wall** —
the space naturally carrying the Bost–Connes dynamics is H₁, whose
spectrum is {log n}, not {γ_n}; and H_R (the "real" space carrying
{γ_n}) only exists if RH is already proved. The pattern categories
distribute as:

- Wrong-space: K4, K7, K9, K12, K13, K17, K18 (seven)
- Circular: K11, K14, K16 (three)
- Vacuous: K2, K10 (two)
- Distributional: K3, K15 (two)
- Topological: K1, K5 (two)
- Spectral: K8 (one)
- Algebraic: K6 (one)
- Numeric: K19 (one)

The dominant category is Wrong-space. This is the fingerprint of
a STRUCTURAL bottleneck: a space problem, not a technique problem.

**What the bottleneck is.** See §C, repeated in "Current bottleneck"
below. The CCM third space L²([λ⁻¹,λ]) bypasses the H₁-vs-H_R
wall by providing a genuinely new Hilbert space, not derived from
BC dynamics, on which the Connes–Consani–Moscovici 2025 operator
D(λ,N) is self-adjoint with spectrum numerically matching the γ_n.
The Bottleneck History §H row already records this. But the cross
is only *formal* — CCM gives finite-(λ,N) operators; the open
problem is the **limit**: proving the spectrum of D(λ,N) converges
to exactly {γ_n} as (λ,N) → ∞, with no spurious eigenvalues and
no zeros missed.

**Load-bearing §D toolkit pieces for this cycle.**
- **CCM-2025** (D(λ,N) on L²([λ⁻¹,λ])). The finite-rank operator.
- **Connes-Letter-2026** (newly added this cycle). A conditional
  exact-on-critical-line theorem at finite prime cutoff; the
  condition is "CF smallest eigenvalue is simple and even".
- **Teschl-gsrc-2026**. Generalized strong resolvent convergence
  across different Hilbert spaces with identification maps.
  Directly usable for D(λ,N) → D(∞) transfer because the spaces
  H_N = L²([λ⁻¹,λ]) form a parameter family, not a single fixed H.
- **Boegli-2017**. Spectral exactness for non-self-adjoint
  perturbations under gsrc + discrete compactness. Insurance for
  the case where self-adjointness is lost at intermediate λ.
- **Hurwitz-1893**. If we can rephrase spec D(λ,N) convergence as
  uniform-on-compacts convergence of a determinant-like entire
  function, zero convergence is automatic.
- **ITPFI-ω₁** and **Bridge-k**. Our internal proved results that
  supply an ALGEBRAIC side (positivity on the BC algebra) that
  might transfer to the CCM operator side via identification.
- **Archimedean-1/λ**. The archimedean decay rate O(1/λ) could
  be the rate at which spurious eigenvalues vanish, if we can
  tie the tail of the τ^{(R)} correction to the deviation of
  spec D(λ,N) from {γ_n}.

## Web scan findings

- **arXiv:2602.04022 (Connes, 2026, "Letter Through Time").** The
  most important new source. Contains a general result: whenever
  the smallest eigenvalue of the CF (Carathéodory–Fejér) quadratic
  form at a given (λ,N) is simple and even, the approximating
  values form the spectrum of a self-adjoint operator and are
  therefore all real — lying exactly on the critical line. This
  is *conditional* but *exact* at finite cutoff. Added to §D as
  toolkit entry **Connes-Letter-2026**. Gap: the condition has
  to be proved to hold generically (or shown to fail in a way
  that still yields realness).
- **arXiv:2511.22755 (CCM, 2025, "Zeta Spectral Triples").** Already
  in §D. Matches 50 zeros to 10⁻⁵⁵ at primes ≤ 13 — extraordinary
  numerical fit, but no asymptotic proof.
- **arXiv:2408.15135 (Yakaboylu, 2024–2026, v15).** Already in §D.
  Constructs positive-semidefinite W intertwining a non-symmetric
  R with R*. Positivity W ≥ 0 is **assumed, not proved** — this
  is the explicit gap. But W ≥ 0 is Bombieri's operator-theoretic
  form of Weil positivity, and Weil positivity is precisely what
  the Bost–Connes ITPFI side may be able to supply.
- **arXiv:2601.10476 (Teschl et al., 2026).** Already in §D.
  Streamlined gsrc across different Hilbert spaces. This is the
  tool for L1 below.
- **arXiv:2511.20971 (Ascent-Descent).** Already in §D. Non-self-
  adjoint fallback.
- **ScienceDirect S3050475925008978 (2025, SUSY spectral embedding).**
  New source. Reframes Hilbert–Pólya: the zeros are a SPARSE
  SUBSEQUENCE of a Hamiltonian's spectrum, not the whole spectrum.
  This is structurally different: it converts the "no spurious
  eigenvalues" part of the CCM wall into an explicit SELECTION
  question. Added to §D as **SUSY-embedding-2025**. Provides an
  orthogonal-insurance direction.
- **arXiv:2503.09644 (Majorana–Rindler).** Already in §D. Deficiency-
  index / boundary-triplet / Krein extension. Orthogonal construction;
  worth comparing but not load-bearing this cycle.

Minimum web-scan threshold met: 5 WebSearch queries and 3 WebFetch
deep reads (2408.15135, 2602.04022 abs, 2602.04022 html). No new
PDFs downloaded to sources/ this cycle because the four pre-loaded
PDFs already cover everything load-bearing; sources/INDEX.md is
updated below with the two new §D entries marked as EXT references.

## Current bottleneck

**The finite-to-infinite transfer wall on the CCM third space.**

CCM-2025 gives, for each finite cutoff (λ,N), a self-adjoint
operator D(λ,N) on L²([λ⁻¹,λ]) whose low eigenvalues match the
imaginary parts of nontrivial Riemann zeros to 10⁻⁵⁵ using only
primes ≤ λ². Connes-Letter-2026 proves (conditional on an
evenness/simplicity hypothesis on the CF smallest eigenvalue)
that these approximating values lie *exactly* on the critical
line — not just numerically. The wall is the **limit**: proving
that as (λ,N) → ∞ the eigenvalues of D(λ,N) converge to ALL and
ONLY the imaginary parts {γ_n}, with no spurious limit eigenvalue
(upper bound, "no garbage") and no γ_n lost (lower bound,
"completeness"), and in a mode strong enough that the Connes
conditional-on-evenness result can be upgraded to unconditional.

**Classification: STRUCTURAL.** It is not a technical gap in a
single proof — it is a convergence problem on a parameter family
of Hilbert spaces, which requires importing machinery (gsrc,
Boegli, Hurwitz) that only recently became available for the
non-fixed-space setting. Four of the six toolkit pieces most
relevant (CCM, Letter-2026, Teschl, Boegli) were all published
in or after 2024. This is a bottleneck you could only attack now.

It is NOT FUNDAMENTAL: no no-go theorem has been produced or
even conjectured. It is NOT TECHNICAL: the tools needed are
cross-field imports, not tweaks to a single proved lemma. It is
the right target for a 3–5 lead fan-out.

## Leads for this cycle

### Lead 1 — CCM finite→∞ transfer via gsrc + discrete compactness
- Pattern/toolkit: **CCM-2025**, **Teschl-gsrc-2026**, **Boegli-2017**,
  **Hurwitz-1893**.
- Feasibility: **7/10**.
- Engages bottleneck: **crosses** (directly attacks the named wall).
- Rationale. The four tools together are exactly the right
  instrument: CCM provides the finite-rank self-adjoint operators;
  Teschl gsrc-2026 gives convergence across varying Hilbert spaces
  with identification maps; Boegli-2017 upgrades gsrc to spectral
  exactness under discrete compactness; Hurwitz closes the zero
  side if a determinantal form exists. The chain is
  D(λ,N) → D(λ,∞) → D(∞) using Teschl's identification maps
  J_{λ,N}: L²([λ⁻¹,λ]) ↪ L²((0,∞)). The executor's job is to
  (a) verify discrete compactness of the family, (b) verify gsrc
  under J_{λ,N}, (c) apply Boegli to get spectral exactness.
- What would close. A rigorous statement: "spec D(λ,N) → {γ_n}
  pointwise, with discrete compactness, as (λ,N)→∞, in the sense
  of Boegli 2017 Thm X." That's Layer 4 of the six-layer chain.
- What would kill. (i) Discrete compactness fails for the D(λ,N)
  family at any intermediate λ. (ii) gsrc holds but the limit
  operator has spurious eigenvalues (non-zero residue outside
  {γ_n}). (iii) Identification maps J_{λ,N} force a domain that
  excludes some γ_n.

### Lead 2 — Upgrade Connes-Letter-2026 to unconditional CF-evenness
- Pattern/toolkit: **Connes-Letter-2026**, **CF-ρ≥4.27**, **AE-simp-N≤20**,
  **Six-Patterns P5 (zeta-reg)**.
- Feasibility: **6/10**.
- Engages bottleneck: **crosses** (if the condition holds, we get
  exactness at every finite cutoff and the limit is "just" a
  continuity argument).
- Rationale. Connes 2026 says: *if* the smallest eigenvalue of
  the CF quadratic form at (λ,N) is simple and even, the
  approximating values lie exactly on the critical line. We
  have **AE-simp-N≤20** in the toolkit — simplicity of the even
  sector spectrum for N ≤ 20 at 120-digit precision — and
  **CF-ρ≥4.27** giving uniform Carathéodory–Fejér decay. These
  two toolkit pieces are exactly the structures Connes' conditional
  theorem is conditional on. The lead is: use AE-simp + CF-ρ≥4.27
  to prove the condition holds for all sufficiently large N,
  perhaps all N, and derive the exactness unconditionally.
- What would close. A lemma: "For all N ≥ N₀, the smallest
  eigenvalue of the CF quadratic form at (λ,N) is simple and
  even." With AE-simp-N≤20 + analytic continuation in N via
  CF-ρ decay.
- What would kill. (i) Evenness fails at some N₀ (would be a
  new "evenness" killed approach). (ii) Simplicity fails (and
  multiplicity hits a parity-forbidden sign). (iii) The Connes
  2026 paper's conditional does not extend — e.g., its proof
  is specific to a smaller family of operators than CCM's D(λ,N).

### Lead 3 — Completeness: Weyl-law count matches N(T) for D(λ,N)
- Pattern/toolkit: **CCM-2025**, Riemann–von Mangoldt (classical),
  **Six-Patterns P4 (topological/counting)**, **Archimedean-1/λ**.
- Feasibility: **6/10**.
- Engages bottleneck: **crosses** (this is the "no zero missed"
  half of the limit wall, orthogonal to Lead 1's "no spurious"
  half).
- Rationale. Even if Lead 1 delivers spectral exactness, exactness
  alone does not guarantee every γ_n is hit — a subsequence {γ_{n_k}}
  could be hit and the rest missed. We need a counting lower bound.
  Riemann–von Mangoldt says N(T) ~ (T/2π) log(T/2πe). If we can
  prove #{eigenvalues of D(λ,N) in [0,T]} ≥ N(T) − o(1) as
  λ → ∞, completeness is forced. The CCM operator has enough
  prime-side structure to admit such a count: each Euler factor
  at a prime p ≤ λ² contributes a predictable number of
  eigenvalues via the rank-one perturbation.
- What would close. Inequality #spec D(λ,N) ∩ [0,T] ≥ N(T) − C/λ
  for an explicit C, via a direct counting of the rank-one
  contributions. Then Lead 1's exactness + this lower bound
  forces bijection onto {γ_n}.
- What would kill. (i) The CCM rank-one structure systematically
  miscounts by a positive fraction of N(T) (then no transfer
  closes the chain). (ii) Spurious eigenvalues do exist and
  contribute to the count, so the lower bound is vacuous.

### Lead 4 — Orthogonal insurance: BC-ITPFI positivity → Yakaboylu W ≥ 0
- Pattern/toolkit: **ITPFI-ω₁**, **Bridge-k**, **Yakaboylu-2024**,
  **R-Theorems** (from paper12 — 37 transposed positivity theorems),
  **SP1 (crack RH from inside BC)**.
- Feasibility: **4/10** (orthogonal insurance, capped).
- Engages bottleneck: **orthogonal insurance** (does not cross
  the CCM finite→∞ wall; provides an independent route via
  Weil-positivity that would make the CCM chain optional).
- Rationale. Yakaboylu-2024 reduces RH to the positivity W ≥ 0
  of an explicit operator built from the non-symmetric R on
  L²([0,∞)). He proves the intertwining R_Z* = W R_Z W but
  leaves W ≥ 0 as the open assumption. Our toolkit has
  **ITPFI-ω₁** (the BC KMS₁ factorization) and **Bridge-k**
  (formal bridge cocycles at k=2,3,4,6). The BC algebra supplies
  positive functionals naturally; if one of them can be pushed
  forward through the Bridge to Yakaboylu's L²([0,∞)), we
  get W ≥ 0 for free. This is SP1's core move: crack RH from
  INSIDE the BC algebra. Completely disjoint from the CCM chain.
  Even if CCM collapses, this lead is an independent shot.
- What would close. A positive functional on the BC algebra
  whose pushforward through some explicit intertwiner equals W,
  together with a proof that pushforward preserves positivity.
- What would kill. (i) No intertwiner BC → L²([0,∞)) that maps
  a positive BC functional to W (category error — the BC space
  and the Yakaboylu space are not comparable). (ii) Yakaboylu's
  proof that W ≥ 0 ⇒ RH has a gap we didn't notice. (iii) The
  Bridge cocycles are only formal and can't be upgraded to the
  required analytic form.

## Fan-out audit

Four leads:
- **L1, L2, L3** all touch the CCM operator D(λ,N) or its
  Connes-Letter-2026 conditional. That's 3/4 = **75%** on the
  same construction.
- **L4** is structurally disjoint (BC-side positivity transfer).

75% is **below the 80% threshold** from §f of the prompt. Spawning
L4 was deliberate precisely to satisfy fan-out discipline: after
a 3-lead cluster on the warmest path (CCM), the strategist must
include at least one orthogonal probe. L4 is that probe. Its
feasibility is correctly capped at 4/10 (orthogonal insurance
ceiling ≤ 5/10 per the prompt).

Rationale for not spawning a 5th lead: the three CCM leads cover
three genuinely different sub-obstructions (gsrc-transfer /
finite-exactness / completeness-counting). Adding a fourth CCM
lead would be redundant. A second orthogonal lead (e.g., Majorana–
Rindler or SUSY-embedding) is available if Cycle 1 collapses; we
defer it to Cycle 2 to avoid over-fanning.

## What I deliberately rejected

1. **Redoing a gradient-flow-on-H_R lead.** That pattern died as
   K17 / K18 — every gradient-flow lead on H_R is either wrong-
   space or circular. The premise check (d) kills any shadow of
   it immediately. Re-entry would require constructing H_R
   intrinsically *without* knowing the γ_n first, and no new
   construction has surfaced that supplies this. So no lead
   this cycle on H_R gradient flow.
2. **A spectral-measure-algebraic lead on H_R.** K11 circular.
   Same reason. Requires H_R to exist before we can compute a
   spectral measure on it.
3. **The Majorana–Rindler 2025 deficiency-index path.** Listed
   in sources/INDEX.md. It's a plausible independent construction,
   but we already have L4 as orthogonal insurance, and Majorana–
   Rindler's relation to the Bost–Connes algebra is unclear at
   this point — it's a competing Hilbert–Pólya realization, not
   a BC-internal route. SP1 (crack from inside BC) argues
   against making it load-bearing in Cycle 1. Defer to Cycle 2+.
4. **A SUSY-embedding-2025 lead.** Attractive because it changes
   the question (from "full spectrum" to "sparse subsequence")
   and would naturally resolve the "no spurious eigenvalues" half
   of the L1 wall. But it is based on a variational/Gaussian
   trial-state argument, not a proved operator identity — the
   paper explicitly frames this as a "spectral selection
   principle" to be discovered, not a proof. It's the right
   flavor but too under-developed for Cycle 1. Added to §D for
   future use.

## Next phase handoff

**For the Phase 2 executors:**

- **L1 executor.** Your job is the **gsrc/Boegli/Hurwitz chain**.
  Read `sources/teschl-gsrc-norm-resolvent-2026.pdf` and
  `sources/ccm-zeta-spectral-triples-2025.pdf` first. The key
  identification map you need is J_{λ,N}: L²([λ⁻¹,λ]) → L²((0,∞))
  — extension by zero is the obvious choice; verify it satisfies
  Teschl's conditions (uniform bound, convergence on a dense
  core). Run the computational kill/advance rule: at mp.dps=50,
  compute the low eigenvalues of D(λ,N) for λ ∈ {2, 4, 8, 16}
  and N ∈ {5, 10, 20}, compare to the first 10 γ_n, and report
  the convergence rate. If the rate looks faster than O(1/λ),
  that's your entry point into Boegli.
- **L2 executor.** Read Connes 2026 (`sources/connes-rh-letter-through-time-2026.pdf`)
  in depth. Find the exact theorem statement and its hypotheses.
  Check whether AE-simp-N≤20 already satisfies the hypothesis for
  N ≤ 20. If yes, test the critical-line property numerically for
  N = 5, 10, 15, 20 and compare against Connes' 50-zero table.
- **L3 executor.** The counting lead. Start with the Riemann–von
  Mangoldt formula and the known prime counts for λ ∈ {2, 4, 8,
  16}. The goal is to write an explicit lower bound that makes
  the rank-one contribution to the spectral count auditable.
- **L4 executor.** Read `sources/yakaboylu-riemann-zeros-spectrum-2024.pdf`
  and find the exact W ≥ 0 open assumption. Then inspect
  `paper12/29-theorem-catalogue.md` (the 387-theorem catalogue)
  for the list of transposed positivity theorems (R-Theorems).
  Don't touch CCM unless a cross-lead insight demands it — the
  whole point of L4 is independence.

**What to avoid.**
- Do NOT invoke H_R. Any lead that requires a Hilbert space on
  which {γ_n} is already known to be the spectrum is a K-pattern
  shadow and will be killed by premise check (d).
- Do NOT compute on H₁ with {log n} spectrum and hope the answer
  transfers — K9, K17, K18 ate that family whole.
- Do NOT use the Brauer H² topological invariant (K1) or any
  discrete topological class to detect continuous perturbations.
  The coboundary lesson applies to every lead involving an
  integer-valued constraint.
- Do NOT use Weil/Li positivity in the K6 form (the sign flips).
  The Yakaboylu W-framing in L4 is a different operator-theoretic
  form and is not blocked by K6.

**Notation freeze (from §D).** D(λ,N), L²([λ⁻¹,λ]), ρ, C_N, τ^{(R)},
τ^{(p)}, ω₁, ω₁^p, e_k, γ_n, CF-even-simple. Use these names
exactly; do not rename or re-derive.

---

# PHASE 5 — CYCLE 1 CLOSEOUT (post Phase 2, Phase 3, and reconciliation)

*Written by the orchestrator after the four executor reports, the
three adversary reports, and the L1/L2 matrix reconciliation.*

## What actually happened

**Phase 2** (parallel executors on L1–L4) produced:
- L1 ADVANCED with strong numerics (|γ₁−eig₁| = 1.78×10⁻⁴⁹ at (λ=4, N=30), mp.dps=60) + 5-step transfer chain sketched
- L2 ADVANCED with CF simplicity/evenness verified at 5 (λ,N) points to ≥60σ / ≥120σ + new sub-bottleneck SB-2.1
- L3 ADVANCED with exact Weyl count match (|Δ|=0) across 15 test points + K9 re-entry gate claimed closed + precision-floor operating rule `dps ≥ 1.86·N + 30` discovered
- L4 BLOCKED (wrong-space, non-CCM paths inherit simplicity-of-zeros)

Phase 2 also produced two cross-lead discoveries from the executor
reports:
- L4 observed that the BC/Yakaboylu path inherits a simplicity-of-zeros conjecture while the CCM path does NOT — pushes CCM further into load-bearing status
- L1 and L2 each discovered a sub-bottleneck (SB-1 and SB-2.1 respectively) and both believed they were attacking the same analytic pinch-point

**Phase 3** (adversaries on L1, L2, L3) produced WEAKENED verdicts
on all three and discovered:
- L1 Adversary: Boegli Def 2.5 misquote; narrative drift on CCM Thm 5.10(iii) (executor implied dependence on Connes-Letter 6.1, but 5.10(iii) is self-contained at finite N); decay constant eyeball-fit was 10^(−4.5λ²) but true slope is 10^(−3.37λ²); Teschl Lemma 2.7 hypothesis list hand-waved; **new open step: CCM §8 Gate II (k_λ ≈ ξ̂_{λ,N}) elided** — needed for Hurwitz λ→∞ closure
- L2 Adversary: Connes-Letter §6.6 actually has **TWO remaining items**, not one — the executor flagged only the first (simple-even); the second is "k_λ is a sufficiently good approximation of θ_x", which is **the same step the L1 Adversary caught as Gate II**. Two independent adversaries identified Gate II from different angles; Theorem 6.1 gives "zeros ∈ ℝ", not "zeros = γ_n"; executor's glib waving of negative μ_0 flagged; **extension test at 7 new (λ,N) points including non-integer λ=5.5 and near-boundary λ=1.1 passed** (adds genuine genericity evidence); **critical finding: L1 and L2 disagree by 47 orders of magnitude on what is claimed to be the same QW^N_λ matrix at (λ=4, N=30)**
- L3 Adversary: precision-floor rule empirically VINDICATED and predictive (under breakdown, artifacts cluster at odd Fourier ladder {2πk/L : k=1,3,5,7}); **new sub-bottleneck SB-4: ladder-truncation tail** — for T > 2πN/L, operator-real eigenvalues {2πk/L : |k|>N} inflate the count by up to +38 at T=100; L1/L3 9th-10th zero disagreement RESOLVED as bisection-heuristic (L1) vs whole-interval scan (L3); **K9 re-entry gate closed with a beautiful witness**: under precision-floor breakdown artifacts cluster at {2πk/L}, a THIRD ladder geometrically distinct from both H₁'s {log n} and the target {γ_n}

**Reconciliation** (research/01-reconciliation-L1-L2-matrix.md):
- **Both L1 and L2 mis-read CCM 2025.** The paper has an internal inconsistency between eq (4.11)/(4.14) on page 14 and a "simplified" form on page 15. Each executor picked a different wrong form.
- **L1's error is benign**: pure diagonal shift T_L1 = T_correct − 1.38832·I. Eigenvalue gaps, eigenvectors, simplicity and evenness are all preserved. One-line fix.
- **L2's error is structural**: different wrong γ_L (+0.61496 diagonal shift) AND a wrong sign on W_R off-diagonal (`/(m−n)` vs paper's `/(n−m)`). The sign bug is a rank-~2 perturbation on the (n=0) cross, giving L2 a *genuinely different* operator, not a shift of the correct one. Two-line fix needed.
- **SB-1 ≡ SB-2.1? NO.** L1 (after fix) is the correct QW^N_λ up to a harmless shift. L2 (even after both fixes) is computing a structurally different matrix. The merge recommendation is refuted.
- **The true simplicity gap at (λ=4, N=30)** is μ_1−μ_0 ≈ 3.78×10⁻⁵⁰, with cascading further zeros at the precision floor. **CCM's ε_N-simple hypothesis is numerically unverifiable at dps<150.** Connes himself uses dps=200. Both executors ran at dps=60 and were observing numerical-floor artifacts, not true eigenvalue gaps.

## Current bottleneck — refined

The Cycle 1 Strategist's "CCM finite→infinite transfer wall" is
correct as a high-level framing but Phase 3 + reconciliation have
decomposed it into FIVE distinct open pieces:

1. **SB-1**: simple-even uniformity of the (fixed) full QW^N_λ matrix — the correct CCM construction per eq (3.10), verified at dps≥150
2. **SB-3 (Gate II)**: CCM §8 Gate II = Connes-Letter §6.6 item (ii). Uniform closeness k_λ ≈ θ_x ≈ ξ̂_{λ,N}. Needed for Hurwitz λ→∞ closure AND for identifying η̂_N zeros with Riemann γ_n (not just "real"). Confirmed by two independent adversaries from different angles.
3. **SB-4 (ladder tail)**: operator-real Fourier-ladder eigenvalues {2πk/L : |k|>N} inflate the count past T > 2πN/L. Need a convergence argument showing these tail eigenvalues move to infinity in the N→∞ limit (or are identifiable as non-γ_n spectrum).
4. **Q2-outer**: uniform-in-λ discrete compactness of {D(λ,N)} for Bögli's hypothesis at outer λ→∞. Reduces to Archimedean-1/λ + CCM Lemma 7.3 uniformity but reduction not closed.
5. **Precision-floor discipline**: dps ≥ 150 for any CCM CF-matrix simple-even verification.

## Lead status post-Phase 3

| Lead | Pre-Phase 2 | Post-Phase 2 | Post-Phase 3 | Feasibility change |
|------|-------------|--------------|--------------|---------------------|
| L1 (CCM→gsrc→Boegli→Hurwitz transfer) | 7/10 | ADVANCED | WEAKENED | 7 → 6 (still strongest) |
| L2 (Connes-Letter CF-even-simple) | 6/10 | ADVANCED | WEAKENED (+ matrix bug) | 6 → 4 |
| L3 (Weyl count completeness) | 6/10 | ADVANCED | WEAKENED (+ ladder tail discovery) | 6 → 7 (unexpectedly, because K9 gate is robustly closed) |
| L4 (BC-ITPFI → Yakaboylu) | 4/10 | BLOCKED | (no adversary — only ADVANCED get adversaries) | 4 → 2 (served orthogonal-insurance purpose) |

## Convergence check (from Phase 6 template)

- **North star**: OPEN. Chain self-grade: **5/10**. Load-bearing path (CCM arc) is now structurally understood but open in multiple places.
- **All leads closed or with feasibility ≥ 3/10?** L1 (6), L3 (7) are clean; L2 (4) barely passes; L4 (2) should be archived.
- **Has the current bottleneck been crossed?** NO. It has been *decomposed* into 5 named sub-bottlenecks. The H₁-vs-H_R wall (historical) is crossed (L3 provided the robust witness); the new transfer wall is open.
- **Ready to close?** NO. Next cycle must attack SB-1, SB-3, SB-4, Q2-outer — and apply the precision-floor discipline throughout.

## Next cycle recommendation

**Cycle 2 focus:** four leads, all on the CCM arc (fan-out
exception invoked — post-bottleneck-cross assembly mode for the
sub-bottlenecks). The strategist should spawn:
- **Lead 5**: Fix L1 (one-line γ_L bug), re-run at dps≥200 (per CCM's own convention), re-verify headline |γ_n−eig_n| numbers at the higher precision, tighten Boegli Def 2.5 quote, make Teschl Lemma 2.7 hypotheses explicit.
- **Lead 6**: Gate II (SB-3) attack. Use Archimedean-1/λ + CCM Lemma 7.3 uniformity to prove k_λ ≈ ξ̂_{λ,N} uniformly on compacts. This is the two-adversary-confirmed structural step.
- **Lead 7**: Ladder-tail (SB-4). Prove that {2πk/L : |k|>N} eigenvalues move to infinity (or are identifiable as non-γ_n spectrum) as N→∞. This is L3's Adversary-discovered step.
- **Lead 8**: Rebuild L2 from scratch per the reconciliation note. Use the correct γ_L constant per CCM p.14, the correct W_R sign per Prop 4.3, address BOTH items of §6.6, verify at dps≥150.

L4 is archived as "served orthogonal-insurance purpose, feasibility
2/10, no reopening unless new external construction surfaces."

The Cycle 2 fan-out is 4/4 on CCM arc (100%). Normally this would
trigger the HARD FAIL rule in Role 1 item (f), but the assembly
mode exception applies: a bottleneck (CCM finite→infinite transfer)
has been identified as THE problem, and the cycle is now decomposing
and attacking its sub-steps. This is assembly, not over-investment.

## Step-back check (Phase 6b triggers)

- T1 (≥3 kills in a cycle): NO — 0 kills this cycle, 3 WEAKENED + 1 BLOCKED.
- T2 (≥50% of all kills share a pattern): N/A — no new kills this cycle.
- T3 (two consecutive cycles with no ADVANCED leads): NO — Cycle 1 had 3 ADVANCED.
- T4 ("I don't know what to try next"): NO — 4 concrete Cycle 2 leads above.
- T5 (human forces step-back): NO.

No step-back triggered. Proceed to Cycle 2 normally.

## Cycle 1 calibration signal summary for the tuning log

All signals compiled into tunning-changelog.md Round 003 entry.
Headlines:
- Byte-for-byte re-run + extension test + cross-lead consistency check caught FIVE genuine failure modes the executors missed (Boegli misquote, decay overstatement, matrix disagreement, §6.6 second item, ladder-tail boundary).
- Primary-source verbatim rule (Round 003 addition) is designed to prevent the "§6.6 two-items-not-one" failure mode from recurring.
- Precision declaration rule (Round 003) is designed to prevent the "dps=60 at a true-10⁻⁵⁰ gap" failure mode.
- CCM p.14/p.15 inconsistency is now a toolkit entry — future executors won't re-discover it.
- Fan-out integer-table rule (Round 002) was validated: tuned Strategist landed at 3/4 = 75%, flagged as soft-warning, spawned the mandated orthogonal lead.

## Files touched in Phase 4-5

- `ledger.md` — §C refined, §D gained 4 new rows (CCM-page-14-15-inconsistency, Precision-floor-rule, Ladder-tail, Gate-II) and a Min-dps column; §E Cycle 1 rows completed; §G post-Phase 3 state; §H gained SB-3, SB-4, CCM inconsistency, precision-floor entries; §I updated with executor/adversary reminders
- `strategy/strategy-1.md` — this closeout section appended
- `research/01-reconciliation-L1-L2-matrix.md` — created by reconciliation agent
- `tunning-changelog.md` — Round 003 entry pending (next write after this)
- `00-the-prompt.md` — Round 003 edits applied (extension test mandate, cross-lead consistency check, precision-floor discipline, primary-source verbatim rule, precision declaration rule, §D Min-dps column)

*Orchestrator, 2026-04-10, post-Cycle 1 Phase 3.*

