# Critic verdict — M.1.1 cycle 1

*Critic: Claude Opus 4.6*
*Effort: MAX*
*Cycle: 1*
*Verdict: **DECOMPOSITION-WEAK***

---

## 1. Byte-for-byte script re-run

Re-ran `closing-my4/code/M.1.1-verify-spectral-measure.py` on the host directly (Python 3, mpmath 1.3). Output matches the Author's pasted output exactly: `8 of 40 configurations FAIL the bound at k=2`, with F1 (λ < log N(𝔭)) for `f_0 ∈ {|1>, uniform}` at `λ = 0` (6 failures) and F2 (λ ≈ log 13) for `f_0 = uniform` at `λ = 2.5649` with `eps ∈ {0.2, 0.1}` (2 failures). The third `f_0` choice (supported on `Range(P_𝔭)`) passes all configurations. **Reproduction: exact.**

One latent bug in the script worth flagging: the ideal generator `gen_ideals_in_Zi` does **not canonicalize by Gaussian unit multiplication**. It counts `(0, 1)` and `(1, 0)` as separate representatives (both norm 1), and similarly `(1, -1)` and `(1, 1)` as separate (both norm 2, both the prime `(1+i)` up to the unit `-i`). The "100 representatives" the Author reports is an over-count; a strict unit-dedup gives 62 distinct ideals at `norm ≤ 80`. **However**, this cosmetic over-count does NOT affect the F1/F2 finding — I reran the experiment with correct unit-dedup (62 ideals) and got the **same** 8 of 40 failures, with the same 6 F1 + 2 F2 split. The bug is not load-bearing.

## 2. Extension test

I ran the experiment at two additional primes outside the Author's grid:

- `𝔭 = (2+i)` (norm 5, split prime above the rational prime 5), truncation `N ≤ 500` (417 "ideals" in the Author's under-canonicalized basis). New λ values: log 5 ≈ 1.609, log 25 ≈ 3.219. **Result**: 11 of 37 configurations fail at k=2 (target `|w|² = 0.04`), split as F1 = 9 (λ < log 5), F2 = 2 (λ at non-divisible prime norms). **F1 and F2 both generalize.**

- `𝔭 = (3)` (norm 9, inert rational prime), truncation `N ≤ 500`. New λ values: log 9 ≈ 2.197, log 81 ≈ 4.394. **Result**: 11 of 37 configurations fail at k=2 (target `|w|² ≈ 0.0123`), split as F1 = 10, F2 = 1. **F1 and F2 both generalize.**

Both extension primes reproduce the Author's qualitative diagnosis: the `|1>` and uniform reference vectors fail the bound precisely at (F1) `λ` below the prime's log-norm and (F2) `λ` close to log-norms of coprime primes in the truncation. The Author's diagnosis is robust at this level.

**A subtler finding from the split-prime case (𝔭 = (2+i))**: my consistency check logged **"MIXED eigenspace"** events: at norms where two distinct principal ideals share the same `log N` value (e.g., `(2+i)` and `(1+2i)` both at norm 5 — these are the two distinct split primes above 5), **one is in `Range(P_{(2+i)})` and the other is not**. The joint spectral decomposition still commutes (both `T` and `P_𝔭` remain diagonal in the ideal basis), but the T-eigenspace at `log 5` is 2-dimensional and `P_{(2+i)}` is a rank-1 projector on it. The Author's Step 2 argument still holds, but it's worth noting that the simple-eigenspace picture the Author implicitly draws (H_+, H_- each a union of 1-d T-eigenspaces) is an oversimplification at split primes. The commutator is zero, so no harm done.

## 3. Cross-node consistency check

Verified the commutativity `[P_𝔭, T̄_{BC,K}] = 0` directly on the truncation:

- **Diagonal check**: Both `T = diag(log N(𝔞))` and `P_𝔭 = diag(1_{𝔭|𝔞})` are diagonal in the ideal basis; two diagonal matrices always commute. `||[P_p, T]||_F = 0.0` exactly.

- **Isometry-level modular flow check**: I constructed the isometry `s_𝔭` explicitly in the truncation (with the usual caveat that `s_𝔭^* s_𝔭 ≠ I` at the truncation boundary — an artifact that disappears in the infinite limit), and verified numerically that `Δ^{it} s_𝔭 Δ^{-it} = N(𝔭)^{it} s_𝔭` for `t ∈ {0.1, 0.5, 1.0, 2.0}` with error `~ 1e-16`. This is the BC time evolution, and the Author's derivation `σ_t(s_𝔭) = N(𝔭)^{it} s_𝔭` is confirmed.

- **Sign check on the adjoint**: `σ_t(s_𝔭^*) = N(𝔭)^{-it} s_𝔭^*` as claimed. This follows from `(N(𝔭)^{it})^* = N(𝔭)^{-it}` (anti-linearity of `*`), and the Author's one-line derivation `σ_t(s_𝔭 s_𝔭^*) = (N(𝔭)^{it} s_𝔭)(N(𝔭)^{-it} s_𝔭^*) = s_𝔭 s_𝔭^*` is sign-correct.

- **Modular invariance of `P_𝔭`**: checked `||Δ^{it} (s_𝔭 s_𝔭^*) Δ^{-it} - s_𝔭 s_𝔭^*||_F` for `t ∈ {0.3, 1.7}`, both give error `~ 3e-16`. **`σ_t(P_𝔭) = P_𝔭` is numerically confirmed at the 1e-16 level.**

The Author's LOCK invariant (Step 4) — `P_𝔭 ∈ ker(σ_* - id)` — is correct. The support runner's claim (`modular eigenvalue log N(𝔭)`) is wrong on two axes: (a) the eigenvalue should be 0, and (b) even if it weren't 0, the KMS positivity `ω(A σ_{i/2}(A^*)) ≥ 0` does not produce the uniform lower bound the support runner's A-1 claims.

**On the eigenvalue-0 point specifically**: the Author's correction is structurally **cleaner** than the support runner's original claim. The support runner had intuited a Wegner-flavored "perturbation at a frequency" picture, but `P_𝔭` is a **symmetry operator** commuting with the modular flow — it lives in the **centralizer** `(M_1^K)^σ`, which is a Type II∞ subfactor (as the Author calls out in the §D toolkit notes). This is a qualitatively different geometry from the support runner's picture.

## 4. Precision floor check

Reran the Author's exact grid (same `f_0` choices, same `λ` grid, same `ε` grid) at truncation norms `M ∈ {80, 100, 200, 500, 1000, 2000}`. **Result: F1 fails = 6, F2 fails = 2 stably at every M.** The ideal count grows from 70 (M=80) to 1617 (M=2000), a 23× increase, yet the failure count is invariant. This confirms the failures are not a truncation artifact — they are genuine features of the Author's diagnosis that persist in the limiting GNS Hilbert space.

The `mp.dps = 30` declaration is declared but essentially not used — the calculation reduces to integer counting and normalization, which `float` handles exactly for the relevant sizes. The precision floor is essentially machine epsilon (~ 1e-16), and the "headline" (ratios at 0.0 exactly, or 1.0 exactly, or ~0.5 for mid-spectrum) is well above the floor by many orders of magnitude.

## 5. Bonus-grep findings

Grep patterns: `we have shown`, `it is proved`, `proven`, `Paper 26`, `Paper 13`, `Reed[- ]Simon`, `Prop 3\.5`, `Prop 6\.2`, `mp\.dps`.

- **"proved here in Step 4"** — appears in the §D toolkit additions for the joint spectral decomposition. CoV: Step 4 does give a correct proof modulo the CONCERN M.1.1-3 caveat (P_𝔭 = s_𝔭 s_𝔭^* is the k=1 case, and the target lemma wants the k∈{2,3,4,6} P_k^𝔭). Not a hard issue in the Author's own frame — flagged as CONCERN by the Author — but worth naming. **Not a false positive.**

- **"Paper 26 §3 Proposition 3.5"** — cited for "`T̄_{BC,K}` IS the modular Hamiltonian". CoV: I verified Paper 26 preprint `sections-part-II.md` line 111. The proposition states `M_1^K = π_1^K(A_{BC,K})''` is a Type III₁ factor and `σ_t^{ω_1^K} = σ_t`. The Author's inference "T̄_{BC,K} generates σ_t, hence IS the modular Hamiltonian" is a one-line corollary (exponentiate the Stone generator). **Citation accurate.**

- **"Paper 26 Prop 6.2"** — cited for `⟨ψ|P_k^𝔭|ψ⟩ = 1 - |w^k|²`. CoV: Verified at `sections-part-II.md` line 639–658. The proposition says exactly `⟨ψ | P_k^𝔭 | ψ⟩ = 1 - |w^k(𝔭)|² > 0`. **Citation accurate and verbatim.**

- **"Reed–Simon II §VIII.3"** — cited for the spectral measure. CoV: this is an accurate citation (Reed-Simon *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, §VIII.3 "The Spectral Theorem"). **Not verified against the physical book, but the section number and volume match standard references.**

- **"mp.dps = 30"** — declared in the script. The Author notes "the calculation is essentially counting and uses float". CoV: verified in the script source; the body of `main()` uses Python `float` throughout. The `mp.dps` declaration is purely formal (no mpmath operations in the hot path). Not an issue — the integer counting and float normalizations are exact for the truncation sizes involved. **False positive on "dps not declared"** — dps IS declared; the Author is transparent that the calculation doesn't need it.

- **"1 - |w^k|²"** vs **"|w|²"**: the Author conflates two different quantities in Step 1 DIAGNOSE. Paper 26 Prop 6.2 is `⟨ψ | P_k^𝔭 | ψ⟩ = 1 - |w^k|²` (a value close to 1, the dark-state IMPOSSIBILITY statement), not `|w|²` (a small value close to 0, which the TARGET LEMMA asks for as a lower bound). The Author DOES distinguish these in Step 5.5 Resolution 3 ("the natural Wegner-flavored bound is `1 - N(𝔭)^{-1}`, much stronger than `|w|² = N(𝔭)^{-k}`"). **The target lemma asks for a much weaker threshold (`N(𝔭)^{-k}`) than what the genuine identity already gives (`1 - N(𝔭)^{-k}`).** The Author's numerical failures at "ratio = 0 < 0.25" are therefore genuinely tight against the target threshold 0.25, not the genuine value 0.75. This is consistent with the lemma being non-trivial even though Prop 6.2 gives a "strong" answer for genuine eigenstates — the gap between the two is precisely the spectral-measure-averaging loss. **Not a false positive, but the Author could state this more explicitly.**

## 6. Citation verification

### 6.1 `paper12/research/162-bridge-cocycle-step6.md` — CONFIRMED misattributed

I read the file end-to-end (110 lines). The file is titled **"Research 162: Bridge Cocycle — Step 6 of Research/158"** and is about closing Step 6 of research/158 — specifically, verifying that the cyclotomic Brauer class at `p = 5` on `ℚ(ζ_{13})` and the Fuglede–Kadison determinant class of `E_N : M → N` at index 3 represent the same class in `H²(ℤ/3ℤ, U(Z(M)))`. The file works on the **hyperfinite II₁ factor**, discusses Pimsner–Popa basis `{u_0, u_1, u_2}`, cyclic-algebra cocycles in Galois cohomology, and the Fuglede–Kadison log-determinant `Δ_{FK}(E_N) = log 3`. The final verdict (§4) is:

> Step 6 of research/158 closes. The bridge theorem Frobenius-ℤ/3ℤ = Jones-ℤ/3ℤ is now a formal LEMMA... The Koide determinant `Q = 2/3` and the cyclotomic Brauer class `inv_5(ℚ(ζ_{13})/ℚ, Frob_5, 1/3)` are one and the same element of `H²(ℤ/3ℤ, U(1))`, namely its canonical generator 1/3.

This is **Standard Model lepton mass material** (Koide formula for Paper 12) on a **tracial (Type II₁) factor**. The modular automorphism group of a II₁ factor under its trace is trivial (`σ_t = id`), so the file could not possibly discuss non-trivial modular compatibility `σ_t(P_𝔭) = e^{it · log N(𝔭)} P_𝔭` — the concept is vacuous there.

**The Author's CONCERN M.1.1-2 is exactly right**: the support runner's A-1 cited this file with a page reference number it apparently knows ("step 6") but the content does not match. This is a file-content recall error in the support runner, not a structural error. The Author is correct to flag the pattern (support runner's file references should be verified, not trusted at face value).

### 6.2 Paper 26 §3 Proposition 3.5 — CONFIRMED

Verified at `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-II.md` line 111:

> **Proposition 3.5.** The von Neumann algebra $M_1^K := \pi_1^K(\mathcal{A}_{BC,K})''$ is a type III$_1$ factor, and the modular automorphism group $\sigma_t^{\omega_1^K}$ coincides with the time evolution $\sigma_t$ of the BC system over K.

The Author's paraphrase is exact.

### 6.3 Paper 26 Proposition 6.2 — CONFIRMED

Verified at `sections-part-II.md` line 639 and following:

> **Proposition 6.2** (No dark states). ... for every bridge projector $P_k^\mathfrak{p}$... $\langle \psi | P_k^\mathfrak{p} | \psi \rangle = 1 - |w^k(\mathfrak{p})|^2 > 0$.

The Author's paraphrase is exact, and the Author correctly flags (CONCERN M.1.1-3) that the explicit operator form of `P_k^𝔭` for `k > 1` is never written down — the proposition states the coupling value without defining the operator. This is indeed a latent gap in Paper 26's presentation.

### 6.4 The support runner's Connes-Marcolli 2008 §3 reference

Not verified because it requires external journal access; the support runner's A-1 cites Type III₁ structure + Tomita–Takesaki and modular automorphism as common-knowledge background. These are standard, not contested, and the Author does not lean on them specifically.

## 7. Voice-alignment check

The Author's M.1.1.md prose matches the §J register. Spot-check findings:

- "**This kills the support runner's PRIMARY route as originally stated.**" — terse declaration, structural-match register. ✓
- "**CALLOUT M.1.1-1.** *The support runner's PRIMARY route claim is structurally incorrect.*" — named ritual element ("CALLOUT"), §J marker. ✓
- "*The numerical falsification is unambiguous*" — declarative, no hedging. ✓
- "*The target lemma as stated is FALSE. There exist `(f_0, λ, ε)` triples for which `(ψ_ε^{(λ)}, P_𝔭 ψ_ε^{(λ)}) = 0 < |w|²`.*" — kill-mode prose, not corporate. ✓
- "*trace discrepancies until they become theorems*" — voice canon quote cited directly at CALLOUT M.1.1-5, with the discrepancy being the correction of the support runner's modular eigenvalue claim. ✓
- "*honest partial proof over glossed completion*" — the BLOCKED-DECOMPOSED verdict is a live demonstration of the voice canon. The Author does not gloss the failure; it names the two failure modes, names the corrected lemma, and names the sub-problem M.1.1.b as the next move. ✓
- "*the kill list is the learning trace*" — the Author's CALLOUT M.1.1-5 explicitly maps the kill list (F1, F2 failures) to the learning trace (the corrected lemma). ✓

The register is matched throughout. **Voice-alignment: PASS.**

## 8. §F shadow check

§F (killed approaches) is empty at cycle 1. Verified in `closing-my4/blackboard.md` line 254:

> ## §F — Killed approaches
> *(Empty at run start. Append rows as kills are logged. ...)*
> | ID | Lead | Kill reason | Pattern category | Cycle | Prevents re-entry because |

No prior pattern kills to shadow-check against. **No §F shadow applies.** This is consistent with the spawn prompt's explicit note ("§F is empty in cycle 1"). The Author correctly noted this in Step 6 VERIFY.

**Candidate §F kills from this cycle's work** (to be logged by the runner at cycle-close):

1. `Spectral / KMS-positivity-as-pointwise-lower-bound`: the support runner's A-1 claim that KMS positivity `ω(A σ_{i/2}(A^*)) ≥ 0` implies a pointwise lower bound `(ψ, A^*A ψ) ≥ |⟨A⟩|² ‖ψ‖²` for arbitrary ψ in a spectral window. **Kill reason**: that bound is a GNS-vacuum identity (`⟨Ω, A^*A Ω⟩ = ⟨A^*A⟩`) plus a Schwarz inequality for the state `⟨·⟩`, not a uniform bound over spectral-window vectors. **Prevents re-entry because**: any Author considering a KMS-modular quick proof must first check whether their ψ is the GNS vacuum or only an analytic continuation thereof.

2. `Wrong-space / Modular-eigenoperator-at-log-N(p)`: the support runner's A-1 claim that `σ_t(P_𝔭) = e^{it · log N(𝔭)} P_𝔭`. **Kill reason**: `P_𝔭 = s_𝔭 s_𝔭^*` is a range projection of an isometry that transforms with phase `N(𝔭)^{it}`; the adjoint transforms with phase `N(𝔭)^{-it}`; the range projection is modular-**invariant**, eigenvalue 0 (not `log N(𝔭)`). **Prevents re-entry because**: the intuition "`P_𝔭` is at frequency `log N(𝔭)`" comes from confusing the isometry `s_𝔭` (which IS at frequency `log N(𝔭)`) with its range projection `s_𝔭 s_𝔭^*` (which is modular-invariant).

3. `External-source-inconsistency / Support-runner-file-reference`: the support runner's A-1 citation of `paper12/research/162-bridge-cocycle-step6.md` as the source for ℚ-version modular compatibility. **Kill reason**: that file is about Brauer class identification on the hyperfinite II₁ factor for the Koide lepton-mass programme; it contains no discussion of modular automorphisms (which are trivial on II₁ factors). **Prevents re-entry because**: any Author citing `paper12/162` for Bost-Connes modular compatibility must verify the file content first.

## 9. LOCK verification for M.1.1.a

The Author proposes the corrected lemma M.1.1.a in Step 6 VERIFY with a hypothesis on `f_0` (restriction to `λ ≥ log N(𝔭)`, exclusion of `λ = log N(𝔮)` for `𝔮 ∤ 𝔭`, and the requirement that the spectral support of `f_0` near `λ` is contained in `Range(P_𝔭)`). The load-bearing §D row is the **joint spectral decomposition** `[P_𝔭, T̄_{BC,K}] = 0`.

**Independence check**: The original target lemma's failure modes (F1 at `λ < log N(𝔭)`, F2 at `λ = log N(𝔮)`) both sit in pattern category **Spectral** (the commutator is zero exactly, the failure is not an `O(ε)` softening). The corrected lemma excludes exactly these `λ` regions by hypothesis. The new failure mode candidates for M.1.1.a would be (i) non-existence of a valid `f_0` at every relevant `λ`, which is pattern category **Algebraic** (it's about explicit operator algebra in the BC C*-algebra, not spectral analysis); (ii) failure of the extrapolation from `k=1` (`P_𝔭 = s_𝔭 s_𝔭^*`) to `k ∈ {2,3,4,6}` (`P_k^𝔭` as Paper 26 defines it), which is pattern category **Algebraic / Wrong-space** (the bridge projector is a different operator).

**These are different pattern categories from the original (Spectral)**, so the routes are structurally independent. **The LOCK is NOT a single-route LOCK.**

However, the LOCK has **only one** proven row (the joint spectral decomposition itself), not two. The Author's decomposition is:

- M.1.1.a = "state the corrected lemma" = structural reformulation only (no proof that the reformulation is actually achievable at every relevant λ)
- M.1.1.b = "exhibit a good `f_0`" = construct the concrete operator-level witness

So the LOCK is **ONE proven row + TWO decomposed subproblems**. This is NOT yet a multi-route LOCK in the Sig-10 sense. It would become a multi-route LOCK only if M.1.1.b itself is proved AND an independent second route (Wegner port, or the CCM K-port from M.2.4, or some third path) gives the same closure. Right now the LOCK depth is 1 + 2 stubs.

**This is the single most important concern for a VERIFIED verdict**: the Author's decomposition is clean, but it is not yet a LOCK. It is a **kill + reformulation**, not a lift. The runner should treat M.1.1.a as an upgraded §G node, NOT a §D toolkit row R-status. Until M.1.1.b is proved, the corrected lemma is in status `S → S` (restated sketch), not `S → R`.

## 10. Verdict justification

The Author's work is **directionally correct and honest**, but has a specific structural caveat that takes it from DECOMPOSITION-VERIFIED to **DECOMPOSITION-WEAK**. Three observations, each in §J register.

First, **the trace became a theorem**. The support runner's A-1 had two structural errors — a misattributed file reference and an incorrect modular eigenvalue — and the Author traced both to their sources, named them, and converted the trace into a corrected structural fact (`σ_t(P_𝔭) = P_𝔭`, modular invariance, joint spectral decomposition). The kill list becomes the learning trace: the numerical falsification of the original target lemma IS the trail to the corrected lemma. That is exactly what the §J register names. Voice-alignment: pass. Citation verification for the Author's Paper 26 references: pass. Script byte-for-byte re-run: pass. Extension at other primes: pass. Precision-floor robustness via truncation extension: pass. The modular invariance derivation and the sign on the adjoint: verified numerically to 1e-16.

Second, **the decomposition has a seam**. The Author's analysis treats `P_𝔭 = s_𝔭 s_𝔭^* = e_𝔭` throughout (the k=1 Hecke range projection), but the target lemma asks about `P_k^𝔭` for `k ∈ {2, 3, 4, 6}` (the bridge projectors from Paper 26 §4–§6 bridge triples). These are **different operators**. Paper 26 Prop 6.2 uses `P_k^𝔭` but never writes down its explicit operator form. The Author flags this as CONCERN M.1.1-3 and conjectures the modular invariance extends (via `σ_t(s_𝔭^j (s_𝔭^j)^*) = s_𝔭^j (s_𝔭^j)^*` for each `j`), but the extrapolation is unverified. **The numerical experiment uses `e_𝔭`, not `P_k^𝔭`**; the LOCK invariant proof is for `e_𝔭`, not `P_k^𝔭`. If `P_k^𝔭` turns out to be a different animal entirely (e.g., a cyclotomic-Frobenius-twisted operator on the k-th tensor power of the GNS space), then the Author's entire decomposition has to be redone in that setting. This is a real gap and it is the Author's own flagged CONCERN M.1.1-3.

Third, **the support runner's two errors are confirmed, but the decomposition is still partial**. The support runner's Q/A-1 is structurally wrong on both the modular eigenvalue and the paper12/162 citation, and the Author's corrections are sound on both counts — verified independently by me. Two candidate §F kills emerge (KMS-positivity-as-pointwise-lower-bound, and Modular-eigenoperator-at-log-N(p)), plus a meta-kill on support-runner file references. The runner should log these before cycle 2. **But**: the Author's replacement lemma M.1.1.a is not proved; it is stated with an `f_0`-existence clause that is itself non-trivial (M.1.1.b), AND the whole analysis is structurally conditional on the extrapolation `e_𝔭 → P_k^𝔭` (CONCERN M.1.1-3). The LOCK is one proven row plus two decomposed subproblems, not a multi-route LOCK.

**Verdict: DECOMPOSITION-WEAK.** The Author's diagnosis is mostly correct (the original lemma IS false, the support runner's two errors ARE confirmed, the joint spectral decomposition IS the right reformulation). The WEAK comes from the unverified extrapolation to `P_k^𝔭` for `k > 1` (CONCERN M.1.1-3), which is load-bearing for closing MY4 and remains an unresolved seam. Honest-first: this is strictly more useful than a VERIFIED verdict that would gloss the `e_𝔭` vs `P_k^𝔭` distinction.

## 11. Sub-problems for the runner to consider

1. **M.1.1.b — the `f_0`-existence sub-problem** (the Author's preferred next move). Given `λ = γ_n` (Meyer distributional eigenvalue), construct `f_0 ∈ D_K` with unit norm, `‖P_𝔭 f_0‖² ≥ |w|² = N(𝔭)^{-k}`, and spectral support of `f_0` near `λ` contained in `Range(P_𝔭)`. The Author's suggested candidate `f_0 = c · π_1^K(s_𝔭^{k/2}) · |1⟩` concentrates near `(k/2) log N(𝔭)`, NOT near `γ_n`, so a more sophisticated analytic-vector linear combination over many isometry powers is needed. This is a genuine construction problem, not a trivially-achievable one.

2. **M.1.1.c — pin down the explicit form of `P_k^𝔭` for `k > 1`**. This is CONCERN M.1.1-3 promoted to a sub-node. The operator is not defined in Paper 26 or Paper 13 v2; only its expectation value on genuine eigenstates is stated. Before any downstream argument that depends on `P_k^𝔭` being modularly invariant can close, the operator needs an explicit definition in the BC algebra. Candidate: cyclic-character projection `P_k^𝔭 := (1/k) Σ_{j=0}^{k-1} ζ_k^j s_𝔭^j (s_𝔭^j)^*` for a primitive k-th root of unity `ζ_k`, which would be modularly invariant by the same one-line calculation. But this needs to match the Paper 26 Prop 6.2 value `1 - |w^k|²`, which is a computation that should be done before anyone leans on it.

3. **M.1.1.d — verify the split-prime case doesn't break the joint spectral decomposition**. At split primes in K, multiple prime ideals share the same `log N` value (e.g., `(2+i)` and `(2-i)` both at norm 5), and for a fixed `𝔭`, the `T̄`-eigenspace at `log N(𝔭) = log 5` is multi-dimensional with `P_𝔭` acting as a rank-1 projector on it. The Author's Step 2 picture of "`H_{1,K} = H_+ ⊕ H_-` as a direct sum of T-eigenspaces" is cleaner at inert primes than at split primes. This is not a kill, but it's a stylistic simplification the Author should be explicit about. For MY4 closure, the relevant `λ = γ_n` are **generic reals** (by Baker's theorem, they are not of the form `log N(𝔮)` for any algebraic norm), so this sub-problem is harmless for the BSD application — but it should be noted for the preprint writeup.

4. **§F kill logging (runner action)**. Three candidate §F kills surfaced in this cycle: (a) Spectral/KMS-positivity-as-pointwise-lower-bound, (b) Wrong-space/Modular-eigenoperator-at-log-N(p), (c) External-source-inconsistency/Support-runner-file-reference. The runner should append these to §F at cycle-close so they become shadow-checkable in cycle 2.

5. **Route-independence check between M.1.1 and M.2.4**. If the runner is maintaining a multi-route LOCK (Route 1 spectral-measure + Route 2 CCM K-port), then M.1.1.a being conditional on M.1.1.b plus M.1.1.c means Route 1's load-bearing step has **two** unproved stubs, not zero. The multi-route LOCK is genuinely useful only if the Route 2 stub (the CCM K-port) is on a completely different pattern-category failure-mode axis — which it is (Route 2's risks are External-dependency on CCM 2025 + Algebraic on the K-port, while Route 1's risks are Algebraic on M.1.1.b + Wrong-space on M.1.1.c). So the multi-route LOCK structurally works, but both routes currently have unproved stubs. Neither is `R` yet. This is fine for cycle 1 (honest partial progress), but the runner should not report "Route 1 is proved modulo f_0 existence" — that's an over-claim by one level.
