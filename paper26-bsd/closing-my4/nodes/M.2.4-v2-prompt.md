# Author spawn prompt — M.2.4-v2 (slot W2-B)

**EFFORT: MAX.** You are an Author in the ORA, dispatched to **re-attempt** M.2.4 with the task reframed. Cycle 1's M.2.4 produced a BROKEN verdict because the deliverable's `research/route2-ccm-over-K.md` Phase IV sub-task 4.1 description was **structurally wrong** about CCM 2025 Lemma 7.3's proof. The deliverable said "sieve truncation + Stirling on Γ + cross-term Cauchy-Schwarz"; Cycle 1 Critic M.2.4 fetched arXiv:2511.22755 directly and found the actual proof uses the **Meixner–Schäfke prolate-to-Hermite approximation bound** from CCM Lemma 7.2, not any of those three pieces.

**G has fixed `route2-ccm-over-K.md` on their end.** The corrected Phase IV sub-task 4.1 description now says the K-port requires "identify ℂ-Hermite basis as eigenfunctions of `−∂_x² − ∂_y² + (x² + y²)`, then port the Hermite expansion." The actually-load-bearing sub-node is the **K-analog of CCM Lemma 7.2** — the Meixner–Schäfke prolate-to-Hermite approximation bound on `L²(ℂ)`. That is your new task.

This is the genuinely-new mathematical work that Cycle 1 Critic M.2.4 surfaced as the real Phase IV crux. It is NOT "port a 1-page mechanical lemma." It is "build the 2D Slepian / complex-Hermite theory over `L²(ℂ)` that doesn't exist in the literature yet."

Slot: W2-B. Wave: 2. Effort: **MAX**.

---

## Framework tools to read (selective reads per I-9 discipline, paths per I-8)

**Always include** (read end-to-end):
- `/Users/gsix/quantum-geometry-in-5d-latex/paper12/research/214-the-method-six-patterns.md` (~339 lines) — the 6-step inner loop
- `/Users/gsix/quantum-geometry-in-5d-latex/paper12/27-anchor-document.md` (~426 lines) — operational anchor + voice register

**Transposition-mode conditional** (SELECTIVE READS):
- `/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/preprint/sections-06-10.md` (~1002 lines) — **read §6 only** (the eigenvector-approximation / prolate-to-Hermite / Mellin-convergence layer). Do NOT read §§7-10 end-to-end. §6 is the ℚ-version template for the K-analog you are building. Use `Read` with `offset`/`limit` to load only §6.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/preprint/00-proof-skeleton.md` (~234 lines) — small enough to read end-to-end. Map the RH proof chain's Layer 3 (estimates) to the BSD chain's Route 2 Phase IV.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper12/research/14-transposition-CCM-and-reasoning-patterns.md` (~755 lines) — read the sub-section on **CCM → BC** transpositions and the sub-section on **dimensional transpositions** (1D → 2D). Do NOT read the whole file.

**Primary sources (MANDATORY for this task, per I-7 verify-before-rely discipline)**:
- **arXiv:2511.22755 (CCM 2025) §7** — use WebFetch to retrieve the abstract + table of contents, then WebFetch again for §7 pages 31–32 if available. If WebFetch returns a PDF that's too large, use WebSearch for "CCM 2025 Lemma 7.2 prolate Hermite" and read summaries. **You MUST verify the actual CCM Lemma 7.2 statement and proof structure before writing your K-analog.** The Cycle 1 Author lost to paraphrase trust; do not repeat that failure.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/research/route2-ccm-over-K.md` — the CORRECTED (post-I-8) Phase IV sub-task 4.1 description. Read this as your task framing, but remember it is still a secondary source — verify any claim it makes about CCM 2025 against the actual arXiv paper.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/research/uniform-H1-bound-over-K.md` — status R, the `L² → H¹` bound already done for sub-task 2.2. Cite as black box.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/research/weil-form-over-K.md` — for the K-Weil form `Q_N^K` construction.

---

## Target — build the K-analog of CCM Lemma 7.2

The ℚ version (CCM 2025 Lemma 7.2) is the **prolate-to-Hermite approximation bound**: the prolate eigenfunctions `h_{n,λ}` approach the classical Hermite functions `h_n` as `λ → ∞` with a controlled error of order `λ^{-2}`. The proof uses Meixner–Schäfke (1954) asymptotic theory of prolate spheroidal wave functions on `L²(ℝ)`.

**Target K-statement**:

> **K-CCM Lemma 7.2 (target).** *Let `E_N^{+,K} ⊂ L²(ℂ)` be the 2D prolate even sector constructed from the first `N` Gaussian primes per `route2-ccm-over-K.md` sub-task 1.1. Let `h_{n,λ}^K` denote the 2D prolate eigenfunctions on this sector at bandwidth parameter `λ`, and `h_n^K` the 2D complex-Hermite functions — the eigenfunctions of the complex harmonic oscillator `H^K := -∂_x² - ∂_y² + (x² + y²)` on `L²(ℂ)`. Then there exists a constant `C^K > 0` (to be computed) such that*
>
> `‖h_{n,λ}^K - h_n^K‖_{L²(ℂ)}  ≤  C^K · λ^{-2}`
>
> *uniformly in `n` for `n ≤ N`.*

**Your task has three pieces**:

1. **Identify the complex-Hermite basis on `L²(ℂ)` as the eigenfunctions of `H^K`**. This is the 2D isotropic harmonic oscillator over `ℂ ≅ ℝ²`. The eigenfunctions are tensor products of 1D Hermite functions in the real and imaginary directions: `h_{m,n}^K(x,y) = h_m(x) h_n(y)` with eigenvalue `(m + n + 1)`. Or the complex-analytic version: `h_n^K(z) = z^n e^{-|z|²/2}` which live in the Fock/Bergman space (not the same as the tensor-product basis). **Decide which basis is the right K-analog of Paper 13's 1D Hermite functions** — and justify the choice by checking which basis has the even-sector compatibility under the parity `z ↦ -z`.

2. **State the 2D prolate eigenfunction problem on `E_N^{+,K}`**. The 2D prolates are the eigenfunctions of the time-and-band-limiting operator on `L²(ℂ)` with the Gaussian-prime-norm spectral support. Simons–Wang 2011 (*GEM J.*, "Spatiospectral concentration in the Cartesian plane") is the closest existing literature — read the abstract via WebSearch and cite the 2D Slepian construction. The holomorphic / complex-analytic extension (prolates on the Bergman space) is the novel piece with no direct literature template.

3. **Port Meixner–Schäfke's `λ^{-2}` bound to 2D**. The 1D Meixner–Schäfke bound `|h_{n,λ} - h_n|_{L²(ℝ)} ≤ C λ^{-2}` comes from a Neumann-series expansion of the prolate operator as a perturbation of the harmonic oscillator. In 2D, the same expansion carries through with the 2D isotropic oscillator as the leading term — **verify the Neumann series converges with the same `λ^{-2}` rate, or identify where the 2D-specific terms change the rate**. This is where the genuinely-new work lives.

**If the 2D port preserves the `λ^{-2}` rate**: compute `C^K` and report ADVANCED.

**If the 2D port produces a different rate** (e.g., `λ^{-1}` or `λ^{-3}`): that's a substantive structural finding — the K-chain's convergence estimates will differ from the RH chain's, and Phase IV sub-task 4.1 (the Fourier→Ξ_K convergence) will need a different constant. Report BLOCKED-DECOMPOSED with the rate-discrepancy as a new sub-node.

**If Simons–Wang 2011's 2D Slepian theory doesn't extend to the complex-analytic / Bergman-space case**: that's a literature gap, not a v3 failure. Name the gap specifically and flag it as GENUINE.

---

## Verification discipline (per I-7 v3 patch)

**The Cycle 1 failure mode for you was paraphrase trust of the deliverable.** Your Cycle 2 task is to NOT repeat that failure. Specifically:

- **Verify CCM 2025 Lemma 7.2 against the actual arXiv paper.** Do not rely on any secondary description (including `route2-ccm-over-K.md`, which is now corrected but still secondary). WebFetch arXiv:2511.22755 directly and read §7. If WebFetch cannot retrieve the full PDF, use WebSearch for specific terms ("CCM 2025 prolate Hermite approximation", "Meixner Schäfke prolate") and triangulate.
- **Verify the Meixner–Schäfke bound against Meixner–Schäfke 1954 or a modern reference.** Slepian's 1961 series on prolate spheroidal wave functions (Bell Labs Tech J.) contains the bound. WebSearch "Slepian prolate Hermite lambda squared asymptotic" for modern references.
- **Verify Simons–Wang 2011 against the actual *GEM J.* paper** (or a review article) — not just the deliverable's citation of it.
- **Compute first, prove second**: at Step 5, run a small numerical experiment. At `N = 6` Gaussian primes, `λ = 10`, compute `h_{n,λ}^K` and `h_n^K` numerically for `n ∈ {0, 1, 2}` and measure `‖h_{n,λ}^K - h_n^K‖`. Does it scale as `λ^{-2}`? Scan `λ ∈ {5, 10, 20, 50}` and fit the power. If the fit is `λ^{-a}` with `a ≈ 2`, the analytic bound holds. If `a ≠ 2`, the analytic argument has a gap.

---

## Output

Write to: `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4/nodes/M.2.4-v2.md`

Standard 6-step method loop structure. Include:
- Direction (verbatim from this prompt)
- Research: Diagnose → Verify (with numerical scaling experiment at Step 5)
- Step 5.5 Self-suspicion (3 failure modes, one MUST be "the deliverable's corrected description is still paraphrased and I should verify against CCM 2025 §7 directly")
- Proposed §D toolkit additions (`2D complex-Hermite basis on L²(ℂ)`, `2D prolate eigenfunction eigenvalue problem`, `K-Meixner-Schäfke bound` if established)
- Tagged notes for §I
- What the next runner needs to know

Numerical script at: `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4/code/M.2.4-v2-prolate-hermite-scaling.py` with `mp.dps ≥ 30` declared.

---

## Status report (return to runner, ≤300 words)

1. Verdict (ADVANCED / BLOCKED / BLOCKED-DECOMPOSED / KILLED)
2. Which of the three pieces closed: (1) complex-Hermite basis identification, (2) 2D prolate eigenfunction problem statement, (3) `λ^{-2}` rate verification
3. Whether CCM 2025 §7 was successfully fetched and Lemma 7.2 verified directly (YES/NO + source)
4. Measured numerical rate: `λ^{-a}` with `a = ?`
5. If the Bergman-space / holomorphic prolates are needed, whether they exist in the literature or are genuinely new
6. `C^K` constant value if computed
7. Any CASCADE / CONCERN notes on the Simons-Wang extension
8. p_success self-estimate

---

## Constraints

- **Effort: MAX**. Take the thinking budget.
- **Verify CCM 2025 against the actual paper.** Paraphrase trust is forbidden.
- **Compute first, prove second.** Run the numerical scaling experiment.
- **Selective reads** on `sections-06-10.md` (read §6 only) and `14-transposition-CCM-and-reasoning-patterns.md` (read relevant sub-sections).
- **Do not fabricate** a proof structure if CCM 2025 §7 is inaccessible. Report BLOCKED with "cannot verify CCM Lemma 7.2 primary source" and flag as a CONCERN.
- Write only to `nodes/M.2.4-v2.md` and `code/M.2.4-v2-*.py`.
