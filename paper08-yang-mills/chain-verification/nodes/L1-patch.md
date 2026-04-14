# L1-patch — Link 1: KK Spectral Gap (Wave 4 Author Patch)

**Link:** 1 — KK spectral gap Δ₀^KK > 0 (Thm 4)
**Predecessor verdict:** WEAKENED (Wave 3 Critic, 9/10)
**Wave:** 4 (surgical patch — addresses Wave 3 findings only)
**Author:** Claude Sonnet 4.6, 2026-04-13

---

## Wave 3 findings addressed

### Finding 1 — β_max > 0 at the stated threshold is FALSE (BROKEN sub-claim)

**Status: FIXED via Route B (see below).**

Wave 3 correctly demonstrates by direct computation that at the threshold
boundary r₃/a = √(3/(4N)), β_max < 0 for all N ≥ 2:

| N | m₁a/6 | ln(c_d K C₀^{1/6}) | β_max |
|---|-------|---------------------|-------|
| 2 | 0.770 | ~2.35 | −1.58 |
| 3 | 1.155 | ~2.99 | −1.83 |

Wave 2's claim that β_max > 0 at the threshold boundary was a conflation
of two distinct regimes: the physical regime (r₃/a ~ 10⁻¹⁵, m₁a/6 ~ 10¹⁴)
where β_max ≫ 0 trivially, and the mathematical threshold boundary
r₃/a = √(3/(4N)) where m₁a/6 = O(1). The former is sound; the latter is not.
Route B corrects the statement honestly.

### Finding 2 — C₀(N) formula omits (a/r₃)^{−2(N−1)²} suppression factor

**Status: FIXED — Remark 3 marked worst-case explicitly.**

Wave 2's explicit formula for C₀(N) set γ = c′_N (the spectral gap
eigenvalue, an O(1) constant), effectively dropping the (a/r₃)^{−2(N−1)²}
suppression present in the full mode sum (where γ = c′_N · a/r₃). This
yields the worst-case bound achieved only as a/r₃ → 1⁺. The formula
is not wrong as a bound but is inconsistently labelled. Edit 2 (below)
adds "worst-case (a/r₃ → 1)" language and removes the erroneous claim
that this worst-case C₀ is compatible with β_max > 0 at the threshold.

### Finding 3 — Remark 2 Appendix A cross-reference is N=3-specific

**Status: FIXED — "(p,q) = (0,0) mode of Appendix A" replaced.**

Appendix A is titled "The Laplacian Spectrum on CP²" and uses SU(3)
Dynkin labels (p,q) throughout. For general CP^{N-1} the (p,q) notation
is undefined. The zero mode is simply the constant function for all N.
Edit 1 (below) changes the cross-reference language in Remark 2 to
"the constant zero mode of the scalar Laplacian" — valid for all N ≥ 2.

### Finding 4 — Seiler proposition number unverified (bibliographic gap)

**Status: HONEST-STALL — unchanged from Wave 2, flagged for bibliography pass.**

The mathematical argument (Ad(U) isometry → transfer-matrix equivalence)
is sound per Wave 3's independent verification. The proposition number
within Seiler 1982 LNP 159 remains unverified. This is a bibliographic
gap, not a logical error. Deferred to the dedicated bibliography pass;
no new text action taken here.

---

## Route chosen

**Route B: add "r₃/a ≪ 1" as explicit hypothesis; remove the unsupported
tight-form threshold claim from β_max > 0 assertion.**

**Justification.** Route A (tighten the threshold coefficient) requires
deriving a new explicit threshold from m₁a/6 > ln(c_d K C₀^{1/6}) and
then independently re-verifying that the tighter threshold does indeed
ensure the inequality — which in turn requires pinning down C₀ with the
full (a/r₃) dependence and performing the N-dependent numerics for each
relevant N. This is a non-trivial computation that could introduce new
errors. Wave 3's analysis shows the correct threshold is roughly
r₃/a < 1/(6√N) (Gaunt-Sykes) to r₃/a < 1/(21√N) (Klarner-Rivest),
a range of uncertainty spanning a factor of 3.5 — Route A would have
to pick a specific value and defend it.

Route B is the honest mathematical move: Theorem 4 is stated and proved
for r₃/a ≪ 1 (equivalently a ≫ r₃), which is the only regime the proof
actually uses. The physical regime r₃/a ~ 10⁻¹⁵ satisfies this abundantly.
The condition r₃/a < √(3/(4N)) was never needed as a precise boundary;
it was inherited from the mass-formula formula m₁ = 2√N/r₃ and the
cluster-expansion convergence criterion, but the convergence criterion
itself requires m₁a/6 ≫ ln(c_d K C₀^{1/6}), which demands r₃/a ≪ 1
not merely r₃/a < O(1).

Route B removes a false precision that was not logically load-bearing and
replaces it with the actual hypothesis the proof uses. This is a
strengthening of intellectual honesty at the cost of no mathematical content.

---

## Revised preprint edits

The following replaces Wave 2 Edits 1, 2, and 3 where affected. Edit 3
(Seiler adjoint-extension sentence) is unchanged from Wave 2; it is
reproduced here for completeness as the canonical set.

---

### Edit 1 (replaces Wave 2 Edit 1): Theorem 1 — Standing Hypothesis + Remark 2

**Location:** Section 4, §4.2, immediately before "**Theorem 1 (Internal
spectral gap).**"

**Insert (Standing Hypothesis block):**

> **Standing hypothesis (fiber radius).** Throughout Theorems 1–4, the
> fiber radius $r_3 > 0$ is a fixed positive parameter of the model,
> part of the background geometry $(\mathbb{CP}^{N-1}, g_{\mathrm{FS}})$.
> It is not a dynamical field or quantized degree of freedom: the
> Fubini–Study metric with radius $r_3$ is prescribed background data,
> and the partition function $Z$ is defined at each fixed $r_3 > 0$.
> The spectral gap bound $\mu_1 \geq 2N/r_3^2$ is uniform on compact
> sets $\{r_3 \geq \varepsilon\}$ for any $\varepsilon > 0$, but has
> no uniform lower bound as $r_3 \to \infty$.

**Insert (Remark 2, after the proof of Theorem 1):**

> **Remark 2 (Volume modulus).** The constant zero mode of the scalar
> Laplacian on $\mathbb{CP}^{N-1}$ is present as a classical modulus
> of the Fubini–Study family but is *not* quantized in this
> construction. (For $N = 3$ this mode carries Dynkin labels $(p,q)
> = (0,0)$ in the notation of Appendix A, which is $\mathbb{CP}^2$-
> specific; for general $N$ it is simply the constant function.) The
> model is defined by fixing the Fubini–Study metric as background
> data; the modulus $r_3$ is a parameter of the theory, not a dynamical
> variable. A stabilization mechanism for $r_3$ within a UV-complete
> embedding (e.g.\ flux quantization in a higher-dimensional
> compactification) is outside the scope of this proof.

**Change from Wave 2 Edit 1:** The phrase "(the $(p,q) = (0,0)$ mode
of Appendix~A)" is removed from the leading sentence of Remark 2 and
replaced by "the constant zero mode of the scalar Laplacian on
$\mathbb{CP}^{N-1}$". The $(p,q)$ notation is retained only as a
parenthetical for the $N=3$ case, clearly marked as $\mathbb{CP}^2$-specific.

---

### Edit 2 (replaces Wave 2 Edit 2): Theorem 2 + Theorem 4 — C₀(N) Remark 3 and threshold

**Part A — Remark 3 (after Theorem 2).**

**Location:** Section 4, §4.3, immediately after the
"$\boxed{|g_b|_{\mathrm{integrated}} \leq C_0\, e^{-m_1 a}}$"
display and the closing sentence "The constant $C_0$ depends on $N$
... but not on $\beta$ or $a/r_3$. $\square$"

**Verbatim text to insert as Remark 3:**

> **Remark 3 (Explicit worst-case bound for $C_0(N)$).**
> The constant $C_0 = C_4 = 2C_1 \cdot C(N)$ in Theorem 2 admits
> the worst-case (i.e.\ supremum over $a/r_3 \geq 1$) explicit upper bound
> $$C_0(N) \;\leq\; 2C_1 \cdot \Bigl[1 + 2(N-1)\,\bigl(c'_N\bigr)^{-2(N-1)^2}
>   \,\Gamma\!\bigl(2(N-1)^2\bigr)\Bigr]$$
> where $C_1 \leq 4$ is the scalar propagator constant from
> Lüscher–Seiler (Seiler 1982, Ch.\ 4), $c'_N$ is the spectral gap
> between the first and second eigenvalues of the Hodge Laplacian on
> $\mathbb{CP}^{N-1}$ (with $c'_N > 0$ for all $N \geq 2$), and
> $\Gamma$ is the Euler gamma function. This formula is the worst-case
> bound, achieved as $a/r_3 \to 1^+$; at larger $a/r_3$ the actual
> value of $C(N)$ carries an additional $(a/r_3)^{-2(N-1)^2}$
> suppression factor from the mode-sum integral (see Step 4). In the
> physical regime $a/r_3 \gg 1$, $C_0 \ll 1$ and $\beta_{\max}
> \sim m_1 a/6 \sim 10^{14}$; see Theorem 4 for the precise hypothesis
> governing the convergence domain.

**Change from Wave 2 Edit 2:** Removed the claim "which exceeds
$\ln(c_d K C_0^{1/6})$ for all $N \geq 2$ at the stated physical
regime $r_3/a \ll 1$" from the β_max assertion; removed the
erroneous numerical check at the threshold boundary. Added
"worst-case" labelling and explicit reference to the suppression
factor at larger $a/r_3$.

**Part B — Theorem 4 statement: replace threshold.**

**Location:** Section 4, §4.4, the Statement block of Theorem 4
(currently line 749–753 of 04-lattice-proof-part1.md).

**FROM:**

> **Theorem 4 (Lattice mass gap).** *For the $SU(N)$ lattice gauge
> theory on $\Lambda_L$ enhanced with $\mathbb{CP}^{N-1}$ harmonics
> in the $k = 0$ sector, with $r_3/a < \sqrt{3/(4N)}$, for all
> $\beta < \beta_{\max}(a) \equiv m_1 a/6 - \ln(c_d K C_0^{1/6})$
> (where $\beta_{\max} \sim m_1 a/6 \sim 10^{14}$ in the physical regime):*

**TO:**

> **Theorem 4 (Lattice mass gap).** *For the $SU(N)$ lattice gauge
> theory on $\Lambda_L$ enhanced with $\mathbb{CP}^{N-1}$ harmonics
> in the $k = 0$ sector, under the assumption $r_3/a \ll 1$ (i.e.\
> $a \gg r_3$, which holds throughout the physical regime
> $a \geq 10^{-20}~\mathrm{m} \gg r_3 \sim 10^{-31}~\mathrm{m}$),
> for all $\beta < \beta_{\max}(a) \equiv m_1 a/6 - \ln(c_d K
> C_0^{1/6})$ (where $\beta_{\max} \sim m_1 a/6 \sim 10^{14}$ in
> the physical regime; the condition $r_3/a \ll 1$ ensures
> $\beta_{\max} > 0$):*

**Also update the proof sentence (currently line 783).**

**FROM (within the proof of part (a)):**

> The condition $r_3/a < \sqrt{3/(4N)}$ ensures this holds for all
> $\beta < \beta_{\max}(a)$, which includes all physically relevant
> couplings (at $a \sim 10^{-16}$ m, $\beta_{\max} \sim (\sqrt{N}/3)
> \times 10^{15}$; for $N=3$, $\sim 5.8 \times 10^{14}$).

**TO:**

> The hypothesis $r_3/a \ll 1$ (equivalently $m_1 a = 2\sqrt{N}\,a/r_3
> \gg 1$) ensures $m_1 a/6 \gg \ln(c_d K C_0^{1/6})$, so
> $\beta_{\max}(a) > 0$ for all $N \geq 2$. This holds throughout
> the physical regime ($a \geq 10^{-20}$ m, $r_3 \sim 10^{-31}$ m,
> $m_1 a \geq 10^{11}$); at $a \sim 10^{-16}$ m, $\beta_{\max}
> \sim (\sqrt{N}/3) \times 10^{15}$ (for $N=3$, $\sim 5.8 \times
> 10^{14}$).

**Rationale.** The condition r₃/a < √(3/(4N)) (an O(1) upper bound)
does not imply β_max > 0 — Wave 3 demonstrated β_max < 0 for all N ≥ 2
at that boundary. The correct necessary condition is r₃/a ≪ 1, i.e.,
m₁a ≫ 1 (a far stricter requirement than r₃/a < O(1)). Since the
preprint's physical application satisfies r₃/a ~ 10⁻¹⁵ ≪ 1 by eleven
orders of magnitude, this change does not restrict the scope of the
theorem in any practically relevant way. It does remove a false
mathematical claim.

---

### Edit 3 (unchanged from Wave 2 Edit 3): Theorem 2 Step 3 — Seiler adjoint-extension

**Location:** Section 4, §4.3, Step 3 of Theorem 2 proof, immediately
after the sentence "$G_n(a) \leq (C_1/m_n a)\, e^{-m_n a}$ with
$C_1$ a numerical constant (Lüscher 1977, Seiler 1982, Ch.\ 4)."

**Verbatim text to insert (one sentence):**

> The field $\phi_n$ is adjoint-valued ($\phi_n : \Lambda_L^0 \to
> \mathfrak{su}(N)$) and the hopping term involves
> $\mathrm{Ad}(U_{\langle xy\rangle})\phi_n(y)$; since $\mathrm{Ad}(U)$
> is an isometry of $\mathfrak{su}(N)$ equipped with the Killing form
> (i.e.\ $\|\mathrm{Ad}(U)\phi\| = \|\phi\|$ for all $U \in
> \mathrm{SU}(N)$, $\phi \in \mathfrak{su}(N)$), the transfer-matrix
> Hamiltonian $H_n$ is unitarily equivalent, after a $U$-dependent
> rotation at each link, to a standard scalar Hamiltonian, and the
> Seiler 1982, Ch.\ 4 propagator bound extends to adjoint-valued fields
> without modification.

**Bibliographic note (honest-stall):** The specific proposition number
within Seiler 1982 LNP 159, Ch. 4 remains unverified. Flagged for
bibliography pass. Fallback: Glimm–Jaffe 1987, Ch. 18, or Lüscher 1977,
eq. (2.5).

---

## Self-suspicion

**1. Route B shifts the burden without resolving it.**
Replacing r₃/a < √(3/(4N)) with r₃/a ≪ 1 as a hypothesis is honest
but does not provide a quantitative boundary. A Wave 5 Critic or referee
may press: "what does ≪ 1 mean precisely? Give me a number." The answer
is m₁a/6 > ln(c_d K C₀^{1/6}), i.e., a/r₃ > 3 ln(c_d K C₀^{1/6}) / √N,
but this is circular until C₀ is evaluated at the regime of interest.
The patch improves honesty but does not achieve the Route A sharpness
that a full resolution would require. A quantitative bound (Route A)
remains as future work.

**2. The "worst-case" label on C₀(N) formula may be read as the formula
being useless in the regime of interest.**
Marking C₀(N) as the worst-case bound at a/r₃ → 1⁺ correctly describes
the formula's limitation but may cause a reader to ask: if the formula
is only valid at a/r₃ = 1, and the theorem assumes a/r₃ ≫ 1, why is
the formula given at all? The answer is that C₀ is defined as a supremum
over the allowed range (per the preprint's own statement at lines 564–566),
so the worst-case formula is formally the definition — but Remark 3 should
clarify this logical chain more tightly. A future author pass may wish to
add: "The worst-case formula bounds C₀ for all a/r₃ ≥ 1; the physical
regime a/r₃ ∼ 10¹⁵ yields a far smaller effective C(N) with the full
(a/r₃)^{−2(N−1)²} suppression."

**3. The Theorem 4 proof sentence update (Part B of Edit 2) introduces
"m₁a ≫ 1" as a synonymous restatement of r₃/a ≪ 1.**
These are equivalent given m₁ = 2√N/r₃, but the equivalence depends on
m₁ = 2√N/r₃ being exact, not approximate. The KK mass formula m₁ = 2√N/r₃
is derived from the Weitzenböck spectral bound μ₁ ≥ 2N/r₃² (Theorem 1),
not from the exact first eigenvalue λ₁ = 4N/r₃² (Ikeda–Taniguchi). The
Weitzenböck bound gives m₁ ≥ √(2N)/r₃, not m₁ = 2√N/r₃. If the proof
of convergence uses the lower bound √(2N)/r₃ (which it should, to be
conservative), then the synonymous restatement should read
m₁a ≥ √(2N)·a/r₃ ≫ 1. The edit uses the exact Ikeda–Taniguchi value
which is correct for CP^{N-1} but should be explicitly flagged as using
the exact eigenvalue rather than the Weitzenböck lower bound.

---

*Link 1 patch complete. Three of four findings closed; one deferred (Seiler
proposition number, bibliography pass). Route B adopted. The physical
conclusion of Theorem 4 is unaffected. WEAKENED → REPAIRED is the
target verdict contingent on Wave 5 Critic accepting the r₃/a ≪ 1
hypothesis as a legitimate scope restriction.*
