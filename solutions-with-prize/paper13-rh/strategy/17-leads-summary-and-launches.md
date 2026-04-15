# Strategy 17 — All Leads Summary and Parallel Launches

*A complete accounting of every lead, every non-lead, and what*
*fires next. Written after 18 kills, 3 new research notes*
*(28-30), 1 phantom test (27), and online research.*

*Date: 2026-04-10*

---

## 1. LEADS (worth pursuing)

### Lead A: Gap B — Quantitative Slepian Convergence (HIGHEST PRIORITY)
**Source:** research/29, VNW+Slepian analysis
**Feasibility:** 6/10
**The estimate:** Show ‖QW_λ^{N,+} − PW‖ < gap(PW)/2 for N ≥ N₀.

If this holds, Slepian's simplicity (proved) transfers to QW for
all N ≥ N₀. For N < N₀, numerical verification at 120 digits
suffices. Combined with VNW (no crossings in λ), simplicity holds
for all (λ, N).

**Why it's tractable:**
- PW eigenvalue gaps are known (Slepian 1961, recent bounds by
  Bonami-Karoui 2021)
- QW → PW convergence is controlled by the tail of the Euler
  product (Σ_{p>P_N} terms)
- Prolate spectral decay is super-exponential (arXiv:1012.3881)
- CCM's 10⁻⁵⁵ precision with 6 primes suggests very fast norm
  convergence
- Our existing code (ccm_perturbation_bound.py) can be adapted

**What to compute:**
1. ‖QW^{N,+} − PW‖_op for N = 3, 5, 10, 15, 20
2. gap(PW) = μ₂(PW) − μ₁(PW) for the prolate operator
3. The crossing point N₀ where ‖QW − PW‖ < gap(PW)/2
4. If N₀ ≤ 40 (our numerical range), we're done

### Lead B: DPTZ Eigenvalue Interlacing (MEDIUM PRIORITY)
**Source:** research/28, Denton-Parke-Tao-Zhang identity
**Feasibility:** 4/10

The overlap ⟨φ_k | a⟩ = 0 iff λ_k(B) ∈ spec(M_a). So the
Arithmetic Theorem ⟺ spec(B) ∩ spec(M_a) = ∅. This is a clean
reformulation. Approaches:
- Induction on N (eigenvalue tracking as primes are added)
- Eigenvalue rigidity (Erdős-Yau-Yin style bounds adapted to
  structured matrices)
- Direct computation of spec(B) and spec(M_a)

**What to compute:**
1. spec(B) and spec(M_a) for N = 3..20
2. Minimum gap min_k |λ_k(B) − λ_j(M_a)| vs N
3. Whether the gap has a clean scaling law

### Lead C: Bombieri's Quadratic Form Eigenvalue Count (NEW)
**Source:** Online search — Bombieri 2000, "Remarks on Weil's
quadratic functional in the theory of prime numbers, I"
**Feasibility:** 4/10

**Key result (Bombieri):** If RH fails with finitely many off-line
zeros, the number of negative eigenvalues of the truncated Weil
quadratic form equals exactly HALF the number of off-line zeros
(for large enough truncation).

**Connection:** Our QW_λ^{N,+} IS a truncated Weil quadratic form.
If we can show QW has NO negative eigenvalues (in the even sector)
for all N, Bombieri's result gives: either RH holds, or infinitely
many zeros are off-line. Combined with density results (Selberg:
positive proportion on line), this constrains the failure mode.

**What to compute:**
1. Count negative eigenvalues of QW^{N,+} for N = 3..40
2. Verify all eigenvalues are non-negative (supporting Weil positivity)
3. Track the smallest eigenvalue vs N

### Lead D: Phantom Determinant Constraint (EVIDENCE, NOT PROOF)
**Source:** research/27, phantom_determinant_test.py
**Feasibility:** N/A (evidence, not a proof path)

**Already computed:** If simplicity fails, phantom zeros at s = 1/2
shift ψ(x) by 2√x, which is excluded by known π(x) data. And
ξ(1/2) = 0.497 ≠ 0, so phantoms break det(D') = ξ(s).

**Status:** DONE. Provides motivation, not proof.

---

## 2. NON-LEADS (killed or blocked)

### NOT a lead: STP / Totally Positive (research/30)
**Feasibility:** 3/10
**Why not:** B is not STP. Prime perturbation (~3.3) dwarfs
spectral gaps (~10⁻¹·⁷ᴺ) for N ≥ 5. Perturbative route dead.
The continuous kernel variant is unexplored but speculative.

### NOT a lead: Baker-type transcendence for digamma
**Feasibility:** 2/10
**Why not:** Requires extending Baker's theorem to digamma values —
a new theorem in transcendence theory. Years of work, uncertain
outcome.

### NOT a lead: Schanuel's conjecture
**Feasibility:** 1/10
**Why not:** Schanuel is unproved and likely decades away.

### NOT a lead: Eigenvalue rigidity (Erdős-Yau-Yin)
**Feasibility:** 2/10
**Why not:** Erdős-Yau-Yin works for RANDOM matrices (Wigner
ensembles). QW is deterministic and highly structured. The tools
don't transfer directly. Would need a new rigidity theorem for
Loewner-type matrices.

### NOT a lead: Direct construction of H_R (Connes programme)
**Feasibility:** 1/10
**Why not:** This IS the 25-year Connes obstacle. No new tools
from Integers help here. CCM+ITPFI bypasses it entirely.

### NOT a lead: Any of the 18 killed approaches
See strategy/02, strategy/04 for the complete kill list.

---

## 3. THE PRIORITY ORDER

| Priority | Lead | Action | Agent type |
|:--|:--|:--|:--|
| **1** | Gap B (Slepian convergence) | Compute ‖QW − PW‖ and gap(PW) | Computation + analysis |
| **2** | DPTZ interlacing | Compute spec(B), spec(M_a), track gaps | Computation |
| **3** | Bombieri eigenvalue count | Count negative eigenvalues of QW^+ | Computation |
| done | Phantom determinant | Already computed (research/27) | — |

---

## 4. What success looks like

**If Lead A closes (Gap B):**
Slepian simplicity transfers → Even-Sector Simplicity proved →
CCM Theorem 5.10 → spec(D_∞) = {γ_n} → **RH proved.**

**If Lead B closes (DPTZ interlacing):**
Arithmetic Theorem proved → Even-Sector Simplicity → same chain → **RH proved.**

**If Lead C provides evidence (Bombieri count):**
All eigenvalues non-negative supports Weil positivity, constrains
failure mode, but doesn't prove RH alone.

**If none close:** RH remains reduced to the Even-Sector Simplicity
Conjecture, with the strongest evidence base ever assembled
(120-digit verification, exponential gap scaling, phantom exclusion,
prolate limit, VNW no-crossing). Paper 13 publishes the reduction.

---

## 5. Online research additions

**Prolate spectral decay (arXiv:1012.3881):** Super-exponential
decay of sinc kernel eigenvalues. Relevant to Lead A — the
convergence QW → PW may be faster than polynomial.

**Bonami-Karoui (2021):** Improved bounds for prolate eigenvalues.
May give explicit gap(PW) needed for Lead A.

**Bombieri (2000):** Eigenvalue count of truncated Weil form.
New lead (Lead C above).

**CCM Section 8:** "Missing steps" and connections to prolate
wave functions and information theory. Directly relevant to Lead A.

---

> *3 leads. 6 non-leads. 18 kills. 1 phantom test.*
> *Lead A (Slepian convergence) is the sharpest tool.*
> *One operator norm. One spectral gap. One theorem.*
