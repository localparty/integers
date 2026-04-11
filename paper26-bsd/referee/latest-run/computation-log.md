# Computation Log — BSD Math Referee Run r01

*All checks performed in the venv at*
*`/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/code/.venv/`*
*using mpmath at 60–150 digit working precision.*

---

## C1. Dedekind zeta Euler product for K = Q(i)

**Claim (Proposition 3.3):** ζ_K(s) = ∏_𝔭 1/(1 − N(𝔭)^{−s}), and
equivalently ζ_K(s) = ζ(s) · L(s, χ_{−4}) with residue π/4 at s = 1.

**Method.** Compute Euler product over Gaussian primes for the first
2000 rational primes, compare to ζ(s) · L(s, χ_{−4}).

```
s = 2:  Euler product = 1.506615...  |  zeta*L = 1.506702...  |  diff = 8.7e-5
s = 3:  Euler product = 1.164728...  |  zeta*L = 1.164728...  |  diff = 1.7e-8
s = 4:  Euler product = 1.070358...  |  zeta*L = 1.070358...  |  diff = 5.0e-12
```

Residue check: eps * ζ_K(1+eps) at eps = 0.001 → 0.7855 (vs π/4 =
0.7854).

**Verdict:** Standard identity, numerically verified. PASS.

---

## C2. Cocycle shift formula (Proposition 7.1, Table 7.4)

**Claim:** Δc(δ) = (1 − N(𝔭)^{−2δ}) / (N(𝔭) − N(𝔭)^{−2δ}),
vanishing iff δ = 0, with first-order expansion
2δ·log(N)/(N−1).

**Method.** Compute at δ = 0.01, 1e-8 for N ∈ {2, 5, 13, 17}.

```
δ = 0.01:
  N=2  exact=0.013580331   first-order=0.013862944  rel_err=2.04e-2
  N=5  exact=0.007856835   first-order=0.008047190  rel_err=2.37e-2
  N=13 exact=0.004149825   first-order=0.004274916  rel_err=2.93e-2
  N=17 exact=0.003431233   first-order=0.003541517  rel_err=3.11e-2

δ = 1e-8 (higher-order terms negligible):
  N=2  exact=1.38629e-8   first-order=1.38629e-8  rel_err=2.08e-8
  N=5  exact=8.04719e-9   first-order=8.04719e-9  rel_err=2.41e-8
  etc.
```

Δc(0) = 0 to 20+ digits for all N checked.

Paper's Table 7.4 values at δ = 0.01:
- N=5:  paper 7.856835e-3, computed 7.856835e-3  ✓
- N=13: paper 4.149825e-3, computed 4.149825e-3  ✓
- N=17: paper 3.431233e-3, computed 3.431233e-3  ✓

**Verdict:** Formula is correct; paper's Table 7.4 values are
accurate. PASS.

---

## C3. Baker inputs — log(N_1)/log(N_2) (Table 8.1)

**Claim:** Paper's Table 8.1 reports log-ratios to ~30 digits.

**Method.** Compute each ratio directly in mpmath at dps = 150.

```
log(5)/log(13):
  paper:    0.626812076465786243080248961
  computed: 0.627473563075303351628369692  ✗ MISMATCH at digit 3
  
log(5)/log(17):
  paper:    0.567841051792493535233139202
  computed: 0.568060967173732968865860498  ✗ MISMATCH at digit 4
  
log(13)/log(17):
  paper:    0.905992665499149750979065256
  computed: 0.905314583119033728085460359  ✗ MISMATCH at digit 4
  
log(5)/log(2):
  paper:    2.321928094887362347870319429
  computed: 2.321928094887362347870319429  ✓ exact match
  
log(13)/log(2):
  paper:    3.700439718141092319445758932
  computed: 3.700439718141092160396812654  ✗ MISMATCH at digit 17
```

**Four of five table entries are incorrect.** Only log(5)/log(2)
is right.

**Paper's conclusion still holds** — the log-ratios are irrational
(trivially, by unique factorization: N_1^a = N_2^b only if N_1 = N_2
and a = b, for distinct positive integer prime norms). Baker upgrades
to transcendence. The irrationality needed for the proof is
unaffected.

**But the specific numerical values reported in the paper are
wrong.** This is a concrete editorial/computational error.

**Verdict:** Formula and conclusion correct; specific Table 8.1
values WRONG in 4/5 entries. Flag as **Editorial Error E1**.

---

## C4. BSD formula for y² = x³ − x and Ω formula (§13.3)

**Claims:**
1. Ω_E = Γ(1/4)² / (2π)^{3/2} ≈ 2.62205755
2. L(E, 1) = Ω_E / 4 ≈ 0.6555
3. BSD formula: L(E,1) = (|Ш| · Ω · R · ∏ c_p) / |E_tors|²
   = (1 · 2.622 · 1 · 4) / 16 = 0.6555 ✓

**Finding 1 — Ω formula is wrong:**

```
Γ(1/4)² / (2π)^(3/2)      = 0.834626841674  ✗ (paper's formula)
Γ(1/4)² / (2·√(2π))       = 2.622057554292  ✓ (correct)
Γ(1/4)² / √(8π)           = 2.622057554292  ✓ (equivalent)
```

The paper's stated formula `Γ(1/4)² / (2π)^(3/2)` gives 0.8346, NOT
2.62205755. The correct formula is `Γ(1/4)² / (2·√(2π))`. The two
differ by a factor of π exactly (0.8346 × π = 2.622).

The **numerical value** stated (2.62205755) is correct. The
**formula given to derive it** is wrong.

**Finding 2 — direct integral check:**

```
2 · ∫_1^∞ dx / √(x³ − x) = 5.244115108584  (full real period)
```

This is the period over **both** real components. With c_∞ = 2
(y² = x³ − x has two real components, since x³ − x has three real
roots), the period over one component is 5.244/2 = 2.622 = Ω_E^+.

**Finding 3 — BSD formula closure:**

With Ω_E^+ = 2.622, |Ш|=1, R=1, c_2=4, |E_tors|²=16, no c_∞
factor in LMFDB convention:

```
RHS = (1 · 2.622 · 1 · 4) / 16 = 0.65551438
L(E,1) = Ω_E^+/4 = 0.65551438
```

These match. BSD formula **closes** at rank 0 for this curve with
c_2 = 4. **The earlier c_2 = 1 that was flagged in the internal
adversarial review has been corrected to c_2 = 4 in the current
preprint; the fix is in place.**

**Verdict:** Closes correctly at rank 0 with c_2 = 4; Ω formula as
**written** is wrong but the numerical value and BSD closure are
correct. Flag as **Editorial Error E2** (Ω formula).

---

## C5. Proposition 4.3 bridge table — THE CRITICAL CHECK

**Claim (Proposition 4.3):** Minimal conductors for the four bridge
indices k ∈ {2, 3, 4, 6} are {3, 5, 7} with product 105.

**Table as stated (after the k=2 ERRATUM):**

| k | Min conductor | Bridge prime | Order in (ℤ/NNℤ)^× | Paper's claim |
|:--|:--|:--|:--|:--|
| 2 | [ERRATUM] | (1+i), N=2 | (paper: "ord=1"; erratum: "not a valid bridge") | BROKEN |
| 3 | 7 | (3+2i), N=13 | ord=2, k=φ(7)/2=3 | claims ✓ |
| 4 | 5 | (2+i), N=5 | "ord=1", k=φ(5)/1=4 | claims ✓ |
| 6 | 7 | (1+i), N=2 | "ord=1", k=φ(7)/1=6 | claims ✓ |

**Method.** Compute `multiplicative_order(a, n)` in Python for each
row.

### Row k=3: (3+2i), N=13, conductor 7

```
ord_{(Z/7Z)^*}(13) = ord(13 mod 7) = ord(6) = ord(-1) = 2  ✓
k = φ(7)/ord = 6/2 = 3  ✓
```

**Verdict:** This row is **CORRECT.**

### Row k=4: (2+i), N=5, conductor 5

```
ord_{(Z/5Z)^*}(5) = UNDEFINED  (5 ≡ 0 mod 5, not a unit)
```

More fundamentally: the Gaussian prime (2+i) has norm 5, which
**divides** the conductor ideal (5). The Frobenius element
`Frob_𝔭` is only defined when 𝔭 is **coprime** to the conductor.
Since (2+i) | (5), the Frobenius is not defined.

**Verdict:** This row is **MATHEMATICALLY INVALID as stated.** The
bridge triple ((2+i), (5), k=4) does not exist — the Frobenius is
undefined.

### Row k=6: (1+i), N=2, conductor 7

```
ord_{(Z/7Z)^*}(2) = 3  (2, 4, 1 — period 3)
```

Paper claims "ord = 1", which would mean 2 ≡ 1 mod 7, false.

With correct ord = 3:

```
k = φ(7)/ord = 6/3 = 2  (NOT 6 as the paper claims)
```

**Verdict:** This row is **WRONG.** The bridge prime (1+i) at
conductor (7) gives k = 2, not k = 6. The paper's claim of k=6
is inconsistent with its own stated Frobenius order (and its
stated order is itself wrong).

### Summary of Proposition 4.3

| k row | Status |
|:--|:--|
| k=2 | Flagged by paper's own ERRATUM as "not a valid bridge" |
| k=3 | **CORRECT** |
| k=4 | **INVALID** (Frobenius undefined — prime not coprime to conductor) |
| k=6 | **WRONG** (ord(2) in (ℤ/7ℤ)^× is 3, not 1; gives k=2, not k=6) |

**Three of the four rows of the "minimal conductor" table are
broken or invalid.** Only the k=3 row survives.

**Implications for the proof:**

1. **The stated "minimal conductor product 105" claim is
   unsupported** as long as 3 of 4 rows are wrong.

2. **The stated "bridge extends more economically over Q(i) (105 vs
   1729)" rhetorical claim is unsupported.**

3. **However, the CORE argument of the proof** does not require
   minimal conductors. It requires only TWO bridge primes with
   **distinct norms** (for Baker's theorem to kill the integrality
   contradiction). If Proposition 4.2's claim of **355 bridge
   triples** for N(N) ≤ 50 is valid (not independently verified
   here), the core proof may survive on a different pair of bridges.

4. **But Proposition 4.3 is the only place where specific bridges
   are worked out in detail.** With 3 of 4 rows broken, the paper
   provides only ONE verified bridge at the level of explicit
   examples — the k=3 triple ((3+2i), (7)). The rest of the chain
   assumes at least one more valid bridge exists, without
   constructing it.

**Verdict:** Proposition 4.3 is substantially broken as written.
The paper's own [ERRATUM] acknowledges 1 row is wrong; this check
finds 2 more. Flag as **Mathematical Gap G1**.

---

## C6. Proposition 4.2 — "355 bridge triples"

**Claim:** For N(𝔑) ≤ 50, there are exactly 355 bridge triples
(𝔭, 𝔑, k) over Q(i) with k ∈ {2, 3, 4, 6}.

**Status:** NOT INDEPENDENTLY REPRODUCED in this run. The paper
cites research/02 for the computation. To independently verify would
require enumerating all Gaussian primes 𝔭 with N(𝔭) ≤ 50,
iterating over all ideals 𝔑 with N(𝔑) ≤ 50, checking coprimality,
computing Frobenius orders, and counting triples yielding
k ∈ {2, 3, 4, 6}. This is feasible but was not done here.

**Given the errors found in Proposition 4.3 (C5), the 355 count
should also be independently verified in a future run.**

**Verdict:** Not verified. Flag as **Unverified Claim U1**.

---

## Summary of findings

| # | Item | Status |
|:--|:--|:--|
| C1 | Dedekind zeta Euler product (Prop 3.3) | PASS |
| C2 | Cocycle shift formula + Table 7.4 values | PASS |
| C3 | Table 8.1 log-ratio values | **4 of 5 WRONG** (Editorial E1) |
| C4a | Ω_E formula in §13.3 | **WRONG by factor of π** (Editorial E2) |
| C4b | Ω_E numerical value and BSD closure | PASS |
| C4c | c_2 correction from 1 to 4 | PASS (fix applied) |
| C5 | Proposition 4.3 bridge table | **3 of 4 rows BROKEN** (Gap G1) |
| C6 | Proposition 4.2 "355 triples" | NOT VERIFIED (Unverified U1) |

**Two concrete mathematical gaps (G1, U1) and two editorial errors
(E1, E2).** None by itself kills the proof chain; collectively they
suggest the paper has not been carefully checked at the level of
specific computations.

**Most critical:** C5 (Proposition 4.3). The paper's own [ERRATUM]
admits the k=2 row is wrong; this check finds k=4 and k=6 are also
wrong. The minimal-conductor rhetorical claim ("105 < 1729") is
unsupported. The core proof requires the broader 355-triple
enumeration (C6) to be valid, which was not independently checked.
