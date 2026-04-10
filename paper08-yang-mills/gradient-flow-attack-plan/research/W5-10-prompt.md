# W5-10: The Cauchy Estimate for the Rescaled Correlator (Lemma 3.7) + Extraction (Lemma 3.8)

## Task
Write the centerpiece proof memo of the entire programme: the Cauchy estimate for the rescaled correlator F(t) = S_{2,t}^c(x,y)/c_1(t)² as t → 0⁺, and the extraction of the renormalized operator [Tr F²]_R. This is Lemma 3.7 (the formerly "hard" lemma, now M-rated in the KK framework) and Lemma 3.8.

## Statements to prove

**Lemma 3.7 (Cauchy estimate).** For fixed non-coincident x, y:
|F(t) - F(t')| ≤ L(x,y)·|t - t'|
uniformly as t, t' → 0⁺, where L(x,y) < ∞ depends on |x-y| and Δ_∞ but not on t or t'.

**Lemma 3.8 (Extraction).** S₂^ren(x,y) := lim_{t→0⁺} S_{2,t}^c(x,y)/c_1(t)² exists as a finite tempered distribution on {x ≠ y}, satisfying OS positivity and clustering at rate Δ_∞. By GNS reconstruction, [Tr F²]_R(f) exists as operator-valued distribution on H.

## The proof structure (6 steps from strategy document 03-)

The full proof skeleton is in `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/03-the-cauchy-estimate-for-the-rescaled-correlator.md`. You should read this carefully — it contains the complete argument. Your job is to make it fully rigorous by incorporating all the Wave 1-4 results.

### Step 1: F(t) is well-defined for all t ≥ 0 in the KK theory
- At t > 0: Luscher-Weisz theorem (UV finiteness)
- At t = 0: Theorem K.1 (Epstein vanishing) kills KK mode sums. Established in W1-04.
- Scheme-independence: Paper 10 Theorem 1 (C_GS = 0 all schemes). Established in W1-04.
- Weyl anomaly protection: Paper 10 Route 05 (Wess-Zumino). Established in W1-04.
- **F(0) is finite** — this is Pillar A.

### Step 2: F(t) is analytic in t for |t| < r_t
- Balaban (B1) + ODE analyticity + heat kernel entirety → composition gives analyticity
- k-independent radius r_t ≈ 3.16 × 10⁻⁴. Established in W1-05.
- Removable singularity: F analytic on punctured disk + F(0) finite → extends to full disk
- **Small-flow-time expansion converges** (not asymptotic) — this is Pillar B.

### Step 3: Subleading terms are O(t)
- No mixing at dim 4: unique operator Tr F² (Lemma 3.2, from W1-04)
- dev ≥ 2 at dim ≥ 6: spectral lemma suppression (Lemma 3.3, from W1-04)
- |R(t)| ≤ C_sub · t · g_k⁴ · Δ̂² / |x-y|^{10}

### Step 4: The Cauchy estimate
- F analytic on disk |t| < r_t (Step 2), F(0) finite (Step 1)
- Cauchy integral formula: |F'(t)| ≤ M_F/r_t
- M_F bounded by: UV (e^{-r_t p²} damping), IR (Δ_∞ > 0 clustering from Theorem 8(d)), Schwinger function bounds (OS0, K-uniform)
- **|F(t) - F(t')| ≤ (M_F/r_t)|t - t'|** — Lipschitz, α = 1.

### Step 5: K-uniformity and double limit
- r_t K-uniform (from B1 + Appendix M mechanism)
- M_F K-uniform (from OS bounds)
- L(x,y) = M_F/r_t K-uniform
- Moore-Osgood: limits in a and t commute

### Step 6: KK → 4D via Theorem 5
- Feshbach projection: |F^{KK}(t) - F^{4D}(t)| ≤ C·e^{-m₁|x-y|}
- Correction t-independent, exponentially small
- Z₂ parity: KK modes n ≥ 1 cancel pairwise (Lemma 3.5) → only n=0 (4D) sector survives

## Key inputs from ALL previous waves

| Wave | Output | Role in this proof |
|------|--------|-------------------|
| W1-01 | Flow well-posedness | V_t exists for all t (Step 1) |
| W1-02 | Flow contractivity | Vacuum isolation, Lyapunov (Step 1) |
| W1-03 | Heat kernel factorization | Product structure, S₀ = 0 (Steps 1, 2) |
| W1-04 | Established lemmas | Theorem K.1, Z₂, GS=0, no mixing, dev≥2 (Steps 1, 3) |
| W1-05 | Analyticity in t | r_t > 0, k-independent, composition theorem (Step 2) |
| W2-06 | Preserves Ω_s | Flow stays in small-field domain (Step 2) |
| W2-07 | Numerical verification | All numerics confirmed independently (Step 1) |
| W3-08 | Polymer decay | κ(t) ≥ κ_B, K-uniform (Step 4) |
| W4-09 | Continuum limit flowed | S_{n,t} exists at fixed t > 0, OS axioms (Steps 4, 5) |

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/03-the-cauchy-estimate-for-the-rescaled-correlator.md` — THE PROOF SKELETON. Read this first and thoroughly.
- All Wave 1-4 outputs in `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/`:
  - W1-01, W1-02, W1-03, W1-04, W1-05
  - W2-06, W2-07
  - W3-08
  - W4-09
- `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md` — Theorem 5 (Section 4.5, Feshbach projection)
- `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` — Section 5.5.3 (spectral lemma), Section 5.7 (Theorem 8)

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W5-10-cauchy-estimate-and-extraction.md`

## Output format
The most important proof memo in the programme. Must be:
- **Self-contained**: a reader with access to the preprint and Paper 10 can verify every step
- **Complete**: all 6 steps of the proof fully elaborated, no gaps
- **Explicit**: every hypothesis discharged by citing a specific prior lemma or theorem
- **Publication-quality**: theorem/proof environments, consistent notation
- Structure: (1) Lemma 3.7 statement, (2) Proof in 6 steps, (3) Lemma 3.8 statement, (4) Proof of 3.8 from 3.7, (5) Summary proof chain, (6) What is new vs. what is cited
- Include the parallel with Theorem M.2.1 (table comparing continuum limit and flow-time limit)
- Include the complete QG5D input table from the strategy document
