# Lead 6: Attack SB-3 (Gate II) via Archimedean-1/λ + CCM Lemma 7.3

## Direction (written by Strategist, Cycle 2)

Status: OPEN
Pattern: `Archimedean-1/λ` (our proved O(1/λ) archimedean
tail bound) + `CCM-2025` §7 Lemma 7.3 (kbλ → Ξ uniformly on
closed substrips) + `Connes-Letter-2026` §6.4 (Poisson-formula
approximation kλ of θ_x) + `Hurwitz-1893` (zero convergence
under uniform-on-compacts convergence) + `Gate-II`.
Feasibility: **5/10**
Engages bottleneck: **yes — crosses** (directly attacks SB-3a,
which two Cycle 1 adversaries independently identified as a
real open step).
Rationale: Cycle 1 L1 Adversary and L2 Adversary both found
Gate II open from different angles. Verbatim from
Connes-Letter-2026 §6.6 "Remaining steps" (page 30):

> "In order to apply Theorem 6.1 one needs to show that the
>  smallest eigenvalue of the Weil quadratic form QW_λ is
>  simple with even eigenvector. The analogue of this property
>  is known for the prolate wave operator. Moreover it still
>  remains to show that k_λ is a sufficiently good approximation
>  of θ_x, λ = √x."

And verbatim from CCM-2025 §8 "The missing steps" (page 33):

> "There are two essential steps still missing to justify our
>  tentative proof of the Riemann Hypothesis. The first is
>  that, in order to apply Theorem 5.10 to the Weil quadratic
>  form QW_λ, one must prove that its smallest eigenvalue —
>  whose existence is ensured by Theorem 3.6 — is simple and
>  that its corresponding eigenvector ξ_λ is even. The second
>  step is to establish that k_λ provides a sufficiently
>  accurate approximation to (a scalar multiple of) ξ_λ, in
>  order to justify the convergence of the zeros of ξ̂_λ
>  towards the non-trivial zeros of ζ(½ + is)."

Both sources name the SAME pair of remaining items; L6 targets
the second item (in Connes-Letter's terminology
"k_λ ≈ θ_x, λ = √x", in CCM's terminology
"k_λ ≈ (scalar) · ξ_λ"). These two statements are equivalent
because θ_x is, up to scalar, the eigenvector that Connes-Letter
expects QW_λ to converge towards — the Poisson-formula image of
the prolate h_{0,λ}, h_{4,λ} combination.

**What is already available.** CCM-2025 Lemma 7.3 (verbatim,
page 32):

> "The Fourier transform of k_λ converges, when λ → ∞, towards
>  the Ξ-function of Riemann uniformly on closed substrips of
>  the open strip |ℑ(z)| < ½."

And Connes-Letter §6.5 Fact 6.4 (same statement, page 29).
These cover the kbλ → Ξ side — the FOURIER TRANSFORM of kλ
converges to Ξ on strips. What is still NEEDED is that kλ
itself (before Fourier transforming) approximates θ_x
(equivalently ξ_λ up to scalar) in a norm strong enough to
feed into the operator-side Hurwitz closure. The two are NOT
automatically equivalent because the Fourier transform is on
different spaces (functions of u ∈ [λ⁻¹, λ] vs tempered
distributions on ℝ).

**The attack.** Use `Archimedean-1/λ` — our proved bound
‖τ^{(R)}‖ / ‖Σ_p τ^{(p)}‖ = O(1/λ) — together with Lemma 7.3
to derive a quantitative ‖kλ − θ_x‖ bound in the right norm.
The strategy is:
- Connes-Letter §6.4 defines kλ := E(hλ) where hλ is a
  specific linear combination of prolate functions h_{0,λ},
  h_{4,λ} with vanishing integral. Inverting this via Poisson
  summation + the isomorphism κ gives an explicit relationship
  between kλ on [λ⁻¹, λ] and θ_x on the same interval.
- The difference kλ − θ_x can be written in terms of the
  residual "near-radical" obstruction Pλ ∩ Pbλ which
  Connes-Letter §6.3–6.4 bounds in terms of 1 − χ₂(λ) ~
  (const) · λ^{−4π e^L + 9/2L} — a double-exponential decay
  bound.
- Alternatively, use Archimedean-1/λ on the O(1/λ) tail of
  the trace formula — the archimedean correction that
  controls the operator side of the bridge from primes to
  kλ.

Toolkit connection: §D rows `CCM-2025` (§7 Lemma 7.3, §6
Poisson formula, §8 missing steps), `Connes-Letter-2026`
(§6.3 near-radical obstruction, §6.4 Poisson approximation,
§6.5 Fact 6.4, §6.6 item ii), `Archimedean-1/λ`,
`Hurwitz-1893`, `Gate-II`, `γ_E-elim`.

Investigate:
1. **Identify the norm.** What norm is "sufficiently good
   approximation" in §6.6 item (ii)? (L² on [λ⁻¹, λ] with
   d*u measure? Sup norm on compact strips? A weighted
   Sobolev norm? Or a convergence at the level of Fourier
   transforms?) Read CCM-2025 §7 proof of Lemma 7.3 to see
   what norm is used for the kbλ → Ξ convergence, and
   read Connes-Letter §6.5 for the same.
2. **Compute the explicit form of kλ − θ_x.** Use Connes-Letter
   §6.4 equation (17): kλ(u) = E(hλ)(u) on [λ⁻¹, λ]. The
   question is: what is θ_x (Connes-Letter's notation — this
   is the Weil-positive "target" function) and how does it
   relate to ξ_λ (CCM's notation for the minimizing
   eigenvector)?
3. **Can Archimedean-1/λ be converted into a direct
   ‖kλ − θ_x‖ bound?** The Archimedean bound is on the tail
   of the trace formula; the question is whether the
   Poisson-summation bridge from trace-formula tail to kλ
   preserves the O(1/λ) rate.
4. **Does Fact 6.4 (kbλ → Ξ uniform on compacts) + Poisson
   summation automatically give kλ → θ_x?** The Poisson
   summation formula is a bridge; the question is in which
   direction (frequency → space or space → frequency) it
   preserves uniformity.
5. **What does CCM §8 indication (1) give us?** The indication
   says "The simple-even condition holds for all values of λ
   for the prolate-wave operator PW_λ." Recent work (Comptes
   Rendus Vol 363, 2025) rigorously proves the prolate
   negative-part conjecture. Does the proof technique (complex
   analytic eigenvalue characterization) transfer to kλ ≈ θ_x?

Would close if: An explicit lemma of the form

> **Target Lemma (SB-3a closure).** There exists α > 0 and a
> finite constant C such that
>   ‖kλ − θ_x‖_Ω ≤ C / λ^α   for λ ≥ λ₀
> where Ω is the norm identified in (1) above, and the bound
> is uniform on compact substrips of |ℑ(z)| < ½.

plus a one-line application to the Hurwitz closure:
"From Theorem 5.10(iii) (finite-N) + Target Lemma + Hurwitz
1893, the zeros of ξ̂_{λ,N} converge to the zeros of Ξ
uniformly on compact substrips, hence spec(D^(λ,N)_log) ∩
compact → {γ_n} ∩ compact as (λ, N) → ∞."

Would kill if:
- The required norm Ω turns out to be a Sobolev norm of
  high order that Archimedean-1/λ cannot bound. (The
  archimedean bound is on a moment / L¹ quantity; upgrading
  to a high-order Sobolev norm may be structurally
  impossible.)
- The §6.4 Poisson-formula construction of kλ introduces a
  fixed O(1) error relative to θ_x that does NOT vanish as
  λ → ∞ in the required norm. (If the double-exponential
  bound on 1 − χ₂(λ) is only on a specific "near-radical"
  quantity and does not translate to ‖kλ − θ_x‖, the lead
  is stuck.)
- The prolate-wave proof technique does not transfer (the
  kλ construction is more complex than the bare prolate
  h_{0,λ}, h_{4,λ} pair).
- Numerically, ‖kλ − θ_x‖ does NOT decay as any power of
  1/λ for λ ∈ {2, 4, 8, 16, 32} at dps=100 (the lead
  becomes a candidate KILL with pattern category "Numeric").

Source: `sources/connes-rh-letter-through-time-2026.pdf` §6.3–§6.6,
`sources/ccm-zeta-spectral-triples-2025.pdf` §7 (Lemma 7.3) and
§8, `research/01-reconciliation-L1-L2-matrix.md` (for the
`CCM-page-14-15-inconsistency` row), Comptes Rendus Math Vol
363 (2025) for the prolate-negative-part rigorous result
(referenced, not downloaded per Round 002 "only if new" rule).

---

## Premise check (written by Strategist, Cycle 2, BEFORE Phase 2)

(a) **Non-vacuous.** The constraint "‖kλ − θ_x‖_Ω ≤ C/λ^α"
can in principle fail: numerically, if one computes
‖kλ − θ_x‖ at increasing λ and the value does not decay, the
lead is killed. Analytically, the bound is a concrete
quantitative statement with a specific rate α > 0, and
distinguishes "kλ is a good approximation" from "kλ is just
an ad hoc guess". **Test**: would ~RH falsify the Target
Lemma? Yes, indirectly: if ~RH then Weil positivity fails,
QW_λ fails to be ≥ 0 at some λ, and the entire construction
of kλ as an approximation of θ_x breaks down (Connes-Letter
§6.4 explicitly says "the range of the map E is contained
in the radical of the global Weil quadratic form" — which
assumes Weil positivity, i.e. RH). So the Target Lemma
contrapositively carries information about RH. **PASS.**
**Adversary note**: this last point is the DELICATE one — if
the Target Lemma assumes RH in the construction of θ_x, then
it would be circular. Must be verified in premise (b).

(b) **Non-circular.** The construction of kλ uses only prolate
wave functions h_{k,λ} and the map E (Connes-Letter §6.4,
eq (17)); these are defined purely from the scaling structure
on L²([λ⁻¹, λ], d*u) with no reference to γ_n. The target
function θ_x is defined at the trace-formula level via
Connes-Letter §4.1 — again without γ_n input. The
approximation statement "kλ ≈ θ_x" is a statement about
explicit objects on the scaling site, not about zeta zeros.
Archimedean-1/λ is a norm bound on the trace formula's
archimedean tail, proved in our corpus (research/20) without
RH. Lemma 7.3 is a finite-λ uniform convergence theorem
whose proof in CCM-2025 §7 uses only Weil's unconditional
explicit formula, not RH.
**Subtle check**: the "range of E is in the radical of QW_λ"
statement in Connes-Letter §6.4 says "RH implies QW_λ is
strictly positive and the radical is {0}" — this is CONDITIONAL
phrasing, not an assumption. The construction of kλ is via
the *near-radical* of QW_λ (the obstruction Pλ ∩ Pbλ), not
its actual radical. So the construction does NOT require RH.
**PASS but with the sub-check that the executor must verify
on careful reading**: make sure no step in the kλ ≈ θ_x
derivation secretly assumes the radical is trivial (= assumes
RH). If any step does, the lead is CIRCULAR and must be
killed before Phase 3.

(c) **Well-posed.** All objects — kλ, θ_x, Ξ, the Hilbert space
L²([λ⁻¹, λ], d*u), the Fourier transform on this space, the
prolate functions h_{k,λ}, the map E, the norm Ω — are
standard constructions in Connes-Letter / CCM-2025. The
Hilbert space is standard. The Fourier transform is standard.
The isomorphism κ: L²([0, L], dx) → L²([λ⁻¹, λ], d*u) is
explicitly given in CCM-2025 Proposition 3.2. **PASS.**

(d) **Not a shadow of a killed approach.** Pattern-check
against §F:
- **K6 (Weil/Li positivity, wrong sign).** Superficially
  similar because L6 invokes "Weil-positivity" language via
  Connes-Letter §6.4 ("RH is equivalent to QW_λ ≥ 0 for all
  λ > 1"). BUT K6 was killed for the Li-coefficient sign-flip
  specifically: off-line zeros make Li coefficients MORE
  positive, wrong direction. L6 does NOT compute Li
  coefficients — it computes an approximation rate of an
  explicit function. **SAFE from K6.**
- **K8 (KMS → compactness).** Not relevant — L6 doesn't
  invoke KMS or type III₁.
- **K11 (Spectral measure algebraic — circular for H_R).**
  This is the most dangerous pattern. The risk is that the
  definition of θ_x itself uses {γ_n} somewhere, so the
  bound ‖kλ − θ_x‖ is circular (bounding an approximation to
  an object defined via the thing we're trying to prove).
  Checking: Connes-Letter's θ_x is defined at the
  trace-formula level WITHOUT {γ_n} input — it is the
  function whose explicit formula uses primes only.
  **SAFE, pending executor re-verification.**
- **K19 (Slepian norm transfer, numeric).** L6 does use a
  norm transfer (from the archimedean tail bound to the
  kλ − θ_x difference). K19 died by 10³⁵ off. Here the
  transfer is at the level of an O(1/λ^α) rate on an
  explicitly defined entire function; quantitatively
  incomparable. **SAFE but yellow card — L6 executor should
  compute a numerical proxy as a sanity check.**
- **K1 (Brauer H² coboundary).** No discrete invariant is
  used. **SAFE.**
- **K2 (Gelfond-Schneider vacuous integrality).** No
  integrality constraint. **SAFE.**

**Verdict: PASSED with two sub-checks the executor MUST
verify explicitly in Phase 2:**
  (i) the construction of kλ and θ_x does NOT secretly
      assume RH (i.e. does not use the radical of QW_λ
      being trivial);
  (ii) ‖kλ − θ_x‖ numerical evidence at λ ∈ {2, 4, 8, 16, 32}
       at dps ≥ 100 is consistent with a power-law decay
       (otherwise the lead is weakened before the analytic
       argument even starts).

Sub-bottleneck reality check: SB-3 is real because (a)
Connes-Letter §6.6 names it verbatim, (b) CCM §8 names it
verbatim, (c) two Cycle 1 adversaries found it independently.
The reduction to "Archimedean-1/λ + Lemma 7.3" is not a
tautological kick-the-can BECAUSE Archimedean-1/λ is a
PROVED bound in our corpus (§D row) and Lemma 7.3 is a
proved theorem in CCM-2025, and the concrete step is
combining them to get a quantitative bound on a specific
explicit quantity (‖kλ − θ_x‖). The reduction is not kicking
the can; it is proposing a specific derivation using two
cited inputs. It could still FAIL (if the inputs are not
strong enough), but it is not a trivial rebranding.

---

## Research (appended by Executor, Cycle 2)

Status: **BLOCKED** — the SB-3a bound splits into a controlled half
(k_λ → k via Lemma 7.2/7.3) and an uncontrolled half (θ_x → k,
which is exactly §8 indication (2) as a numerical observation with
no analytic proof). The "uniform closeness k_λ ≈ θ_x" step cannot
be derived from Archimedean-1/λ + Lemma 7.3 alone. It requires a
new input: either (a) a quantitative Davis-Kahan on the Weil
quadratic form's minimal-eigenvalue subspace, with a gap bound to
the next eigenvalue; or (b) a direct spectral-stability argument
linking 1 − χ_2(λ) (the near-radical obstruction) to the minimal
eigenvector. Neither lives in the §D toolkit as of Cycle 2.

Kill pattern category: N/A (BLOCKED, not killed).
Reason: the two primary sources treat SB-3a as an open problem
*by design* (CCM §8 names it as the second missing step, with three
"indications" supporting its plausibility; Connes-Letter §6.6 names
it verbatim as the second remaining step). The reduction to
Archimedean-1/λ + Lemma 7.3 proposed in the Direction section does
not close the gap because Archimedean-1/λ is a bound on QUADRATIC-
FORM MATRIX NORMS, while SB-3a requires an EIGENVECTOR-DIFFERENCE
bound, and the conversion costs a spectral gap that is precisely
the minuscule quantity ε(λ) ~ 1 − χ_2(λ).

Scripts: `code/lead-6-verify-gate-ii-closeness.py`
Strategic insights: See "Cross-lead insights" at end of section.

### Part A: Precise statement of SB-3a

**Verbatim primary source 1 (Connes-Letter §6.6, page 30):**

> "In order to apply Theorem 6.1 one needs to show that the
>  smallest eigenvalue of the Weil quadratic form QWλ is simple with
>  even eigenvector. The analogue of this property is known for the
>  prolate wave operator. Moreover it still remains to show that
>  kλ is a sufficiently good approximation of θx, λ = √x."

Pointer: pdftotext of
`sources/connes-rh-letter-through-time-2026.pdf`, lines 1687–1690.

**Verbatim primary source 2 (CCM §8 "The missing steps", page 33):**

> "There are two essential steps still missing to justify our
>  tentative proof of the Riemann Hypothesis. The first is that,
>  in order to apply Theorem 5.10 to the Weil quadratic form QWλ,
>  one must prove that its smallest eigenvalue — whose existence
>  is ensured by Theorem 3.6 — is simple and that its corresponding
>  eigenvector ξλ is even. The second step is to establish that kλ
>  provides a sufficiently accurate approximation to (a scalar
>  multiple of) ξλ, in order to justify the convergence of the
>  zeros of ξ̂λ towards the non-trivial zeros of ζ(½ + is).
>
>  There are, however, three indications supporting the feasibility
>  of these steps.
>
>  (1) The 'simple-even' condition holds for all values of λ for
>      the prolate-wave operator PWλ.
>  (2) The extremely small numbers ελ that occur as eigenvalues of
>      the Weil quadratic form QWλ also appear — see Figure 4 — when
>      evaluating the discrepancy for hλ to belong simultaneously to
>      Pλ and P̂λ.
>  (3) The numerical evidence for the proximity between kλ and ξλ
>      extends to the higher eigenfunctions of the Weil quadratic
>      form."

Pointer: pdftotext of `sources/ccm-zeta-spectral-triples-2025.pdf`
(copied to `/tmp/l6/ccm.txt` for this executor), lines 1787–1804.

**Verbatim primary source 3 (CCM Lemma 7.3, page 32):**

> "Lemma 7.3. The Fourier transform of kλ converges, when λ → ∞,
>  towards the Ξ-function of Riemann uniformly on closed substrips
>  of the open strip |ℑ(z)| < ½."

CCM's proof of Lemma 7.3, lines 1733–1784, gives the explicit
quantitative Mellin-transform bound
> |M(kλ)(s) − ∫_{λ⁻¹}^{λ} k(u) u^{s−1} du| = O(λ^{−1/2 − α})
for α = ℜ(s) ∈ (−½, ½), using only Lemma 7.2 (|h_{n,λ} − h_n| ≤
c λ^{−2} on [−λ, λ]) and the definition of the map E.

**Notation dictionary (for SB-3a).**

| Symbol | Meaning | Source |
|:---|:---|:---|
| λ | CCM bandwidth; period length L = 2 log λ | CCM §7, Connes-Letter §6.3 |
| x = λ² | eigenvalue-counter parameter | Connes-Letter §6.1 |
| Ω | [λ⁻¹, λ] ⊂ R*₊ | CCM eq (7.6) |
| d*u | multiplicative measure du/u on R*₊ | CCM §3.3 |
| H_Ω | L²(Ω, d*u) | CCM Prop 3.2 |
| QW_λ | restriction of Weil quadratic form to functions with support in Ω | Connes-Letter §6.4, CCM §5 |
| A_λ | the s.a. operator on H_Ω with QW_λ(f,f) = ⟨A_λ f, f⟩ | Connes-Letter eq (16), CCM Thm 3.6 |
| ε(λ) | smallest eigenvalue of A_λ; numerically ~ 1 − χ_2(λ) | Connes-Letter §6.4 |
| ξ_λ | normalized minimal eigenvector of A_λ (CCM notation) | CCM Thm 5.10 |
| η_x | same object in Connes-Letter notation, on [x⁻¹/², x¹/²] | Connes-Letter §6 intro |
| θ_x(u) | recentered minimal eigenvector: θ_x(u) := η_x(x^{1/2} u); equals ξ_√x up to normalization | Connes-Letter §6 intro, line 1450 |
| h_{n,λ} | nth prolate-spheroidal wave eigenfunction of PW_λ on [−λ, λ] | CCM eq (7.5), Connes-Letter §6.3 |
| h_λ | the unique linear combination of h_{0,λ}, h_{4,λ} with vanishing integral | CCM Lemma 7.2(ii) |
| k_λ(u) | "educated guess" := E(h_λ)(u) for u ∈ Ω | CCM eq (7.6), Connes-Letter eq (17) |
| k(u) | Riemann's limit function k(u) = E(h)(u) | CCM eq (7.1), Connes-Letter eq (13) |
| Ξ(z) | Riemann's Ξ-function; Fourier transform of k | CCM eq (7.1) |
| 1 − χ_2(λ) | "near-radical" obstruction; ~ (2¹⁴/3) √(2π)⁵ e^{−4π λ² + 9/2 log λ} | Connes-Letter §6.4, CCM Lemma 7.2 proof |
| Archimedean-1/λ | ‖τ^{(R)}‖_F / ‖Σ_p τ^{(p)}‖_F = O((log log λ)/λ) bound on Weil QF decomposition | §D row, research/20 |

**Precise statement of SB-3a.** Fix L > 0 and consider the
compact substrip Ω_s = {z ∈ C : |ℑ(z)| ≤ L} of width 2L < 1. Let
kλ, θ_x (x = λ²) live in H_Ω = L²(Ω, d*u). SB-3a asks for:
a constant C < ∞ and an exponent α > 0 such that
> ‖k_λ − θ_x‖_{H_Ω} ≤ C · λ^{−α}    for all λ ≥ λ_0.
The space H_Ω is standard; the norm is the L²(d*u) norm. For
Hurwitz closure at outer λ → ∞, a bound on the Fourier-transform
side uniform on compact substrips of |ℑ(z)| < ½ is sufficient;
but note that this bound CANNOT be derived from the operator-side
bound alone — an additional step is needed because the relevant
Fourier transform is the one on L²(Ω, d*u), i.e. the Mellin
transform, not the additive Fourier transform on ℝ.

### Part B: The attack — and why it stalls

1. **Lemma 7.3's own proof gives k_λ → k directly.** Reading the
   proof (lines 1733–1784):

   > "For u in this interval, the number of integers n such that
   >  n u ≤ λ is at most λ/u, thus with δ(λ) := max_{[−λ,λ]} |hλ(x)
   >  − h(x)| one gets, using the definition of E which involves
   >  u^{1/2}, |E(hλ)(u) − E(h)(u)| ≤ u^{1/2} δ(λ) (λ/u)."

   Substituting Lemma 7.2 (δ(λ) ≤ c λ^{−2}) gives
   > |kλ(u) − k(u)| ≤ c · λ · u^{−1/2} · λ^{−2} = c · λ^{−1} u^{−1/2}.
   
   Sup over u ∈ [λ⁻¹, λ]: the maximum of u^{−1/2} on the interval
   is at u = λ⁻¹, giving u^{−1/2} = λ^{1/2}, so
   > **‖kλ − k‖_∞  ≤  c · λ^{−1/2}.**

   In L²(d*u) on Ω: ∫_{λ⁻¹}^{λ} (c λ^{−1} u^{−1/2})² · du/u
   = c² λ^{−2} ∫_{λ⁻¹}^{λ} u^{−2} du = c² λ^{−2} (λ − λ^{−1})
   = c² λ^{−1} (1 − λ^{−2}). So
   > **‖kλ − k‖_{H_Ω}  ≤  c · λ^{−1/2}.**

   (Note: this bound is in L²(du) rather than L²(d*u) = du/u by
   accident of a clean integral; in L²(du/u) the bound is
   c λ^{−1} · [∫ u^{−1} · u^{−1} du]^{1/2} = c λ^{−1} (1−λ^{−2})^{1/2}
   = c λ^{−1}, giving **‖kλ − k‖_{L²(d*u)} ≤ c · λ^{−1}** — even
   better, clean power-law rate 1/λ in the natural d*u norm.)

2. **What Lemma 7.3 actually uses this for.** The Mellin transform
   of kλ is compared to the Mellin transform of k truncated to
   [λ⁻¹, λ]; the bound |M(kλ)(s) − ∫_{λ⁻¹}^{λ} k(u) u^{s−1} du|
   is O(λ^{−1/2 − α}) by the same u^{1/2} δ(λ) λ/u mechanism,
   integrated against u^{α − 1/2}. Then the tail of the Mellin
   transform of k itself past [λ⁻¹, λ] is estimated by the
   convergence of the integral. Crucially: the entire argument is
   about kλ vs k — the LIMIT — not about kλ vs θ_x — the ACTUAL
   eigenvector.

3. **CCM §8 indication (1) points to prolate, not to the bridge.**
   Indication (1) says "The 'simple-even' condition holds for all
   values of λ for the prolate-wave operator PW_λ" — this is a
   statement about SB-1 (simplicity of PW_λ's spectrum), NOT about
   SB-3a. It is evidence for the SIMPLICITY conjecture, by analogy.
   Indication (2) is the relevant one for SB-3a: the observation
   that ε(λ) (smallest Weil QF eigenvalue) and 1 − χ_2(λ)
   (near-radical obstruction) track each other numerically. This
   is the KEY empirical observation, but Connes-Moscovici-Consani
   are explicit that it is NOT a proof:
   > "It remains possible that our strategy for proving convergence
   >  towards the zeros of ζ(½ + is) will face significant obstacles."
   (CCM §8, line 1812.)

4. **The chain attempt.**
   
   Desired: ‖kλ − θ_x‖ ≤ C λ^{−α}.
   
   Split by triangle: ‖kλ − θ_x‖ ≤ ‖kλ − k‖ + ‖k − θ_x‖.
   
   - ‖kλ − k‖ ≤ c λ^{−1} in L²(d*u) norm. **PROVED** via Lemma 7.2
     + the E-map estimate from Lemma 7.3's proof.
   - ‖k − θ_x‖ = ?  **This is the open step.** It asks: does the
     minimal eigenvector of A_λ converge to k as λ → ∞?
   
   **This is not resolved by Archimedean-1/λ.** Archimedean-1/λ
   bounds ‖τ^{(R)}‖_F / ‖Σ_p τ^{(p)}‖_F in the Frobenius norm of
   the QW_λ matrix in the V_n basis, i.e. it bounds the
   archimedean part of the QUADRATIC FORM against the prime part.
   It does NOT bound the minimal-eigenvector DIFFERENCE of two
   operators. To convert matrix-entry perturbation to eigenvector
   perturbation, one uses Davis-Kahan, which costs a factor
   proportional to 1/gap, where gap is the distance from the
   minimal eigenvalue ε(λ) to the next eigenvalue. Both ε(λ) and
   the gap are minuscule (CCM Figure 4 shows ε(λ) ~ e^{−4π λ² +
   9/2 log λ}), so the Davis-Kahan factor is astronomical:
   
   > ‖δξλ‖ ≲ ‖δ A_λ‖ / gap ~ (log log λ / λ) / e^{−4π λ²}
   
   which EXPLODES. Archimedean-1/λ is therefore the wrong input
   for SB-3a in a naive Davis-Kahan sense.
   
5. **Alternative: use indication (2) directly.** CCM §8 indication
   (2) says ε(λ) ~ 1 − χ_2(λ) numerically. If this were proved
   analytically it would say: kλ is in the approximate kernel of
   A_λ up to error 1 − χ_2(λ), and since the next eigenvalue of
   A_λ is bounded away from zero by some ε_1(λ), Davis-Kahan gives
   > ‖kλ/‖kλ‖ − ξλ‖ ≤ (1 − χ_2(λ)) / (ε_1(λ) − ε(λ)).
   
   If ε_1(λ) is bounded AWAY FROM 0 (as is conjectured — CCM Thm
   3.6 says A_λ has discrete lower bounded spectrum), this would
   give super-exponential closeness. But neither the lower bound
   on ε_1(λ) nor the analytic bound QW_λ(kλ) ≤ (1 − χ_2(λ))‖kλ‖²
   is established in CCM or Connes-Letter — both are left as
   numerical observations in §8 indication (2) and Figure 4.

6. **The missing lemma.** A complete SB-3a proof would need:

   > **Missing Lemma (SB-3a closure).** There exist constants
   > c_1, c_2 > 0 and an exponent α > 0 such that for λ ≥ λ_0:
   >
   >   (i)  QW_λ(kλ, kλ) ≤ c_1 (1 − χ_2(λ)) ‖kλ‖²  [analytic
   >        proof of indication (2)],
   >   (ii) ε_1(λ) − ε(λ) ≥ c_2 λ^{−α}  [second-eigenvalue gap
   >        bounded away from zero, polynomially at worst].
   >
   > From (i) + (ii) + Davis-Kahan one would conclude
   >   ‖kλ − ξλ‖ ≤ c_1 (1 − χ_2(λ)) / (c_2 λ^{−α})
   > which is double-exponentially small in λ.

   Neither (i) nor (ii) is in §D or in CCM-2025 or Connes-Letter
   as a proved statement. Both are numerical observations.

### Part C: Numerical probe

Script: `code/lead-6-verify-gate-ii-closeness.py`, mp.dps = 150.

**Precision declaration** (lines 6–13 of the script):
> mp.dps = 150. Justification: CCM's own numerics use dps=200, but
> we are probing k_λ − k (NOT the operator-side eigenvalue ε(λ))
> and the relevant scale is the prolate deviation δ(λ) ~ λ^{−2},
> which at λ=16 is ~4e-3. dps=150 provides ~148 guard digits, far
> above the floor.

**What the script computes.** The Mellin bridge proof of Lemma 7.3
separates kλ − k into two components:
  (a) the PROLATE component (h_λ − h), bounded by Lemma 7.2 at
      c λ^{−2} uniformly on [−λ, λ];
  (b) the CUTOFF component: the difference between E(h) summed
      over n ≤ λ/u and the full Riemann k(u) = E(h)(u) = u^{1/2}
      Σ_{n≥1} h(nu) summed over all n.

Component (a) gives a polynomial λ^{−1/2} bound on the sup-norm of
kλ − k via the u^{1/2} · δ(λ) · (λ/u) expansion in Lemma 7.3's
proof. Component (b), the cutoff tail, is bounded by the rapid
decay of h(nu) = (π/2) nu (2π n² u² − 3) e^{−π n² u²}: the first
omitted term has n = ⌊λ/u⌋ + 1, contributing order e^{−π λ²} near
the point u ~ 1.

This script isolates component (b) — the cutoff tail — and measures
it directly, to give an honest lower bound on how fast the "pure
cutoff" part of kλ − k vanishes.

**Raw output (lambda ∈ {2, 3, 4, 5, 6, 7, 8, 10, 12, 16}):**

```
# mp.dps = 150
# Lead-6 SB-3a probe: k_lambda^{cut} vs k on [1/lambda, lambda]
# Sampling: 400 log-spaced points, trapezoidal L^2(d*u) on log-scale
#
# lambda |  sup-norm            |  L^2(d*u) norm       | x = lambda^2
# -------+----------------------+----------------------+--------------
     2   |  0.0002336307335      |  5.314424762e-5       |  4
     3   |  1.258563992e-10      |  2.875061803e-11      |  9
     4   |  9.783231966e-20      |  2.041489705e-20      |  16
     5   |  9.714285812e-32      |  2.004863239e-32      |  25
     6   |  1.949274726e-46      |  3.215974149e-47      |  36
     7   |  7.264872218e-64      |  1.244376809e-64      |  49
     8   |  1.6475284e-84        |  3.62818054e-85       |  64
    10   |  5.372661758e-133     |  7.379193621e-134     |  100
    12   |  9.096864974e-196     |  1.015255469e-196     |  144
    16   |  0.0                  |  0.0                  |  256

# Power-law fit on lambda in [3, 4, 5, 6, 7, 8, 10, 12]:
#   sup-norm     : ||.||_inf  ~ 5.1491e+158 / lambda^289.7328
#   L^2(d*u)     : ||.||_2    ~ 2.0332e+158 / lambda^290.1713
#
# The power-law slope is ENORMOUS (alpha >> 1), which indicates the
# decay is NOT a power law but an exponential or super-exponential.
#
# Test: fit exponential model log(norm) = -c * lambda^p + d
#   sup-norm : log|.| ~ -46.9893 * lambda^1.0 + 156.1529  (residual=5.3291e+03)
#   sup-norm : log|.| ~ -11.7114 * lambda^1.5 + 57.6873  (residual=1.3954e+03)
#   sup-norm : log|.| ~  -3.1511 * lambda^2.0 +  7.5957  (residual=2.6136e+01)
```

**Observed rate (cutoff component only).** Best fit:
> log ‖kλ^{cut} − k‖_∞ ≈ −3.1511 · λ² + 7.60,
with the exponent 3.1511 ≈ π (to 0.3% agreement). So
> ‖kλ^{cut} − k‖_∞ ≈ e^{7.6} · e^{−π λ²} = O(e^{−π x}).
This **exactly matches** Riemann's series: the first omitted term
of E(h)(u) = u^{1/2} Σ_n h(nu) at n = ⌊λ/u⌋ + 1 contributes
u · [factor] · e^{−π (⌊λ/u⌋+1)² u²} = e^{−π λ²} at the dominant
u ~ 1. At λ = 16 the rate floor is e^{−π · 256} ~ 10^{−350},
which is below our dps = 150 floor, so the λ = 16 value appears
as 0.0 (this is a precision-floor effect, not a violation of the
power law).

**Caveat: this is the cutoff half only.** The prolate half of
kλ − k is separately O(λ^{−1/2}) in sup-norm by Lemma 7.2 + the
E-map expansion. Since e^{−π λ²} ≪ λ^{−1/2} for λ ≥ 3, the prolate
half dominates at moderate and large λ. So the **actual** proved
rate of ‖kλ − k‖_∞ is O(λ^{−1/2}) — slower than the exponential
cutoff rate measured here, but still a power law.

**This numerical probe tells us: kλ → k is unconditionally O(λ^{−1/2})
in sup on [λ⁻¹, λ], and the "cutoff component" is exponential.
Neither tells us anything about kλ → θ_x.**

### Part D: Proof sketch (what SB-3a would need)

A complete proof of SB-3a would take the form:

> **Proposition (SB-3a closure, HYPOTHETICAL).** Let A_λ be the
> Weil QF operator on H_Ω, with smallest eigenvalue ε(λ),
> normalized minimal eigenvector ξλ, and second-smallest eigenvalue
> ε_1(λ). Assume:
>   (H1) Simple-even: the minimal eigenvalue ε(λ) is simple with
>        even eigenvector (= SB-1 / CCM §8 step 1);
>   (H2) Near-radical energy estimate: QW_λ(kλ, kλ) ≤
>        c_1 (1 − χ_2(λ)) ‖kλ‖² for some c_1 > 0  (= analytic
>        proof of CCM §8 indication (2));
>   (H3) Second-eigenvalue lower bound: ε_1(λ) ≥ c_2 · λ^{−α}
>        for some c_2 > 0, α ≥ 0.
> Then by Davis-Kahan applied to A_λ near ε(λ),
>   ‖kλ/‖kλ‖ − ξλ‖_{H_Ω}
>     ≤ 2 · QW_λ(kλ, kλ)^{1/2} / (‖kλ‖ · (ε_1(λ) − ε(λ)))
>     ≤ 2 √c_1 · (1 − χ_2(λ))^{1/2} / (c_2 λ^{−α} − ε(λ)).
> Since (1 − χ_2(λ))^{1/2} decays as e^{−2π λ² + const log λ} and
> (c_2 λ^{−α} − ε(λ)) is bounded below by ½ c_2 λ^{−α} for
> sufficiently large λ,
>   ‖kλ/‖kλ‖ − ξλ‖ ≤ c_3 λ^α · e^{−2π λ²}.
> Combined with ‖kλ − k‖ = O(λ^{−1/2}) (Lemma 7.3 proof) and
> the triangle inequality, one obtains SB-3a:
>   ‖kλ − ξλ‖ ≤ C · λ^{−1/2}.

**Hypotheses that need new input:**
- (H1) = SB-1 (L1 in Cycle 1): NOT proved, is one of the two CCM
  missing steps. [open]
- (H2) = CCM §8 indication (2) turned into a theorem. Needs a
  direct evaluation of ⟨A_λ kλ, kλ⟩ in terms of 1 − χ_2(λ) via
  the Poisson-formula bridge of Connes-Letter §6.4. Structurally
  available but not written out in either source. **[candidate
  new lead for Cycle 3]**
- (H3) = lower bound on the second smallest eigenvalue of A_λ.
  A_λ has discrete lower bounded spectrum by CCM Theorem 3.6 but
  the quantitative gap to the second eigenvalue is not in the
  cited sources. A Weyl-type upper bound on the eigenvalue
  counting function of A_λ (which is what L3 of Cycle 1 is
  pursuing for D^{(λ,N)}_log, a different but related operator)
  could give (H3). **[cross-lead dependency with L3 / L7]**

The SB-3a proof therefore **reduces to two new sub-bottlenecks**
(H2) and (H3), plus SB-1 (which is shared with Cycle 1 L1/L2).
The reduction uses `Archimedean-1/λ` ONLY as heuristic corroboration
of (H2) — Archimedean-1/λ itself is in the wrong norm (matrix
Frobenius vs. eigenvector L²) and does not plug into Davis-Kahan
directly.

### Sub-check (i): does the construction of kλ and θ_x secretly assume RH?

The Phase 1.5 premise check flagged this as a mandatory executor
verification. Reading Connes-Letter §6.4 (lines 1650–1667) in full:

> "The conceptual justification of this formula is as follows: The
>  range of the map E is contained in the radical of the global
>  Weil quadratic form (see [18]), but RH implies that QWλ is
>  strictly positive and that its radical is {0} so we should
>  expect that the domain of QWλ cannot contain any non-zero
>  element of the range of the map E. One can nevertheless
>  construct functions with support in [λ⁻¹, λ] which are in the
>  'near radical' of the Weil quadratic form..."

The construction of kλ is via the **near-radical** of the LOCAL
QW_λ (support in [λ⁻¹, λ]) — it does NOT use the radical of the
GLOBAL Weil QF. The hypothesis "RH ⇒ radical is {0}" is stated as
a consistency check, not as an input to the construction. The
construction itself proceeds via the projections P_λ, P̂_λ and the
Poisson formula E(f̂)(x) = E(f)(x⁻¹), which are unconditional.
So **the construction of kλ does not assume RH**. Similarly θ_x
is the minimal eigenvector of a specific unbounded self-adjoint
operator A_λ (CCM Theorem 3.6, Schmüdgen [12]) whose existence is
also unconditional. **Sub-check (i) PASSES.**

### Sub-check (ii): numerical evidence at λ ∈ {2, 4, 8, 16, 32} is consistent with power-law decay

Our script runs λ ∈ {2, 3, 4, 5, 6, 7, 8, 10, 12, 16} and finds
that the **cutoff component** decays as e^{−π λ²} (super-polynomial).
The **prolate component** is governed by Lemma 7.2 at O(λ^{−2}).
The triangle-inequality combination is dominated by O(λ^{−2}) for
the pointwise bound, O(λ^{−1/2}) for the sup-over-u bound, and
O(λ^{−1}) for L²(d*u). All are polynomial with α ≥ 1/2.
**Sub-check (ii) PASSES for kλ → k, but this is not the same as
kλ → θ_x.** The numerical verification of kλ → θ_x would require
an independent construction of θ_x, which requires solving the
Weil QF eigenvalue problem at dps ≥ 200 — outside the scope of
this lead by the precision-floor ceiling of CCM's own computations.

### Cross-lead insights

- **INSIGHT (affects L1 and L2):** the Hurwitz closure in L1 and
  the §6.6 second item in L2 both assume kλ → θ_x, but what the
  toolkit actually provides via Lemma 7.3 is only kλ → k (the
  LIMIT function). For outer Hurwitz convergence (zeros of ξ̂_{λ,N}
  → zeros of Ξ as λ → ∞), one needs spec(A_λ) to stabilize, which
  requires the θ_x → k step, which is SB-3a and is OPEN.
- **INSIGHT (affects L3):** the second-eigenvalue lower bound
  (H3) in the Proposition above is essentially the Weyl count for
  A_λ in a window [0, ε], and L3's ladder-tail work may port to
  this with a sign flip.
- **INSIGHT (affects L7):** the ladder-tail factor SB-4 and
  Gate II SB-3a are structurally dual — SB-4 asks whether the
  OPERATOR A_λ's large-eigenvalue tail is empty, SB-3a asks
  whether its smallest-eigenvalue LEADING vector is close to kλ.
  A uniform bound on the eigenvalue counting function of A_λ on
  a compact window would feed both.
- **INSIGHT (affects L8, if L8 revisits Connes-Letter's §4.1
  construction of η_x):** any reformulation of η_x that makes
  Connes-Letter §6.4 indication (2) into a lemma would immediately
  close SB-3a. This is the most direct "external theorem"
  candidate.

Status: **BLOCKED pending a new lemma bridging "(1 − χ_2(λ))
energy estimate" (= CCM §8 indication (2) as a theorem) and a
"second-eigenvalue gap lower bound" for A_λ (= variant of L3).**
Neither lemma is in §D as of Cycle 2. The lead does NOT die — it
correctly identifies what's missing and spawns two new
sub-bottlenecks. Added to §H as SB-3a.1 (energy estimate) and
SB-3a.2 (second-gap bound).

Scripts: `code/lead-6-verify-gate-ii-closeness.py` (dps=150, raw
output pasted above).

---

## Adversarial (appended by Adversary, Cycle 2)

*[To be appended by L6 adversary in Phase 3.]*

## Pattern check (appended by Adversary, Cycle 2)

*[To be appended by L6 adversary in Phase 3.]*
