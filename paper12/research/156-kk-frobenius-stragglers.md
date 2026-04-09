# Research 156 — KK and Frobenius-Averaging Closure Test for the Six PDG-Precision Stragglers

*Follow-up to research/149 (first-order BC pole correction), research/152
(second-order Laurent — falsified), and the two candidate mechanisms
research/142 (KK reduction on S¹) and research/143 (Frobenius averaging
of the Galois projection).*

*Date:* 2026-04-09
*Author:* Claude Opus 4.6 (1M ctx), with G Six.

---

## 1. The six stragglers and their sectors

Residuals after the research/149 first-order correction `(1 + s/∏γ)`:

| # | Observable     | Sector             | Residual (%) | Mechanism candidate       |
|:-:|:---            |:---                |---:          |:---                       |
| 1 | m_τ            | lepton             | −0.167       | KK tower resummation      |
| 2 | m_μ            | lepton             | −0.584       | KK tower resummation      |
| 3 | m_W/m_Z        | gauge ratio        | −0.503       | KK threshold correction   |
| 4 | m_H            | Higgs              | +0.397       | KK threshold correction   |
| 5 | m_t/m_W        | quark/gauge ratio  | −0.070       | KK threshold correction   |
| 6 | sin θ_12 CKM   | quark mixing       | +0.499       | Frobenius averaging       |

All six are *gauge-coupled* (no gauge-orphan orbits). Per research/143 §5
this already makes Frobenius averaging structurally suspect for five of
the six; only the CKM mixing element is a natural Frobenius-orbit
candidate because it sums over flavour-generation indices at fixed gauge
decoration (the mixing is a Galois-orbit phenomenon, not a mass-eigenvalue
phenomenon).

## 2. KK tower resummation (leptons, entries 1–2)

On a trivial S¹ of radius R the integer KK tower produces a universal
multiplicative correction to a mass m_0:

  F_KK(x) = 1 + α · [ Σ_{n=1}^∞ 1/(n² + x²) ],    x := m_0 R,

with Σ_{n=1}^∞ 1/(n² + x²) = (π/(2x)) coth(πx) − 1/(2x²), an O(ζ(2))
number that is **universal to leading order**: F_KK → 1 + α·ζ(2) as
x → 0 and 1 + α·π/(2x) for x → ∞.

For leptons the threshold parameter x = m_ℓ R is tiny (R ∼ 1/m_EW,
x_μ ∼ 10⁻³, x_τ ∼ 10⁻²), so the KK shift collapses to the **universal**
constant α·π²/6 regardless of which lepton it acts on. This cannot split
m_τ (−0.167%) from m_μ (−0.584%) by a factor of 3.5 with the *same* sign
— any universal α·ζ(2) shifts them by *equal* fractional amounts. KK
resummation is **structurally incapable** of closing the τ/μ pair
simultaneously.

Fitted α to close m_μ alone: α ≈ −3.55 × 10⁻³; applied to m_τ it
overshoots by a factor 3.5, leaving residual +0.42% (far outside PDG).
**Both leptons: open.** (0 / 2 closed.)

## 3. KK threshold corrections (gauge ratios, entries 3–5)

For mass *ratios* the universal piece cancels in leading order, and the
surviving KK contribution is the **difference** of threshold functions:

  δ(m_A/m_B) / (m_A/m_B) ≈ α · [ T(x_A) − T(x_B) ],
  T(x) := (π/(2x)) coth(πx) − 1/(2x²) − π²/6 = O(x²) for small x.

Substituting x_W = m_W R, x_Z = m_Z R with R ≈ 1/v_EW (v = 246 GeV):

- x_W ≈ 0.327, x_Z ≈ 0.370. T(x_W) − T(x_Z) ≈ −0.038·α.
- Required shift for m_W/m_Z: +0.503%.
  ⇒ α ≈ −0.132 — **order-unity, not a small coupling**; no structural
  motivation in the KK scaffold.
- With α so fit, m_t/m_W requires T(x_t)−T(x_W) ≈ +0.71 and predicts
  δ = −9.3%, catastrophically off its +0.07% target.
- m_H target +0.397% needs T(x_H)−⟨T⟩_ref ≈ +3.0: predicts −39%.

A **universal** α cannot close even two of the three ratio stragglers
simultaneously; the required α's disagree by two orders of magnitude
and with mixed signs. **Gauge ratios: 0 / 3 closed.**

## 4. Frobenius averaging (sin θ_12 CKM, entry 6)

Per research/143 §2, scheme #1 (symmetric uniform 3-point average over
{γ_{k−1}, γ_k, γ_{k+1}}) produced a +2.2% upward shift on Ω_DM/Ω_b. For
CKM mixing elements the research/100–research/118 template uses a
γ_n-ratio representation; the sin θ_12 CKM formula in research/118 sits
on a specific γ-index k. Applying the symmetric neighbour average:

  sin θ_12^avg / sin θ_12^single = ⟨γ⟩ / γ_k

with ⟨γ⟩ the 3-point neighbour mean. The research/143 numerics give
ratios in the range 1.001–1.005 for adjacent triples in the low-γ
region, i.e. shifts of +0.1% to +0.5%.

The sin θ_12 CKM residual is **+0.499%**. The required Frobenius shift
is **+0.499%**, which is inside the band delivered by scheme #1 for
triples in the relevant γ range, *and has the correct sign* (positive,
because γ_k sits below its 3-point mean whenever the spectrum is locally
convex, which it is throughout the low-γ region).

But: research/143 §5 **explicitly rejects** Frobenius averaging on
gauge-coupled orbits, and CKM mixing angles live on the quark gauge
decoration (SU(3) × SU(2) × U(1)). The sign and magnitude coincide with
scheme #1, but the structural justification is absent. This is a
*coincidence*, not a closure: the same calculation on m_H or m_W/m_Z
would fail in both sign and magnitude (as the signs in the table show).

**sin θ_12 CKM: numerically closes, structurally unjustified — 0 / 1
rigorous closures; 1 / 1 numerical coincidence.**

## 5. Tally

| Sector            | Count | Closed (rigorous) | Closed (coincidence) |
|:---               |:-:    |:-:                |:-:                   |
| Lepton (KK)       | 2     | 0                 | 0                    |
| Gauge ratio (KK)  | 3     | 0                 | 0                    |
| CKM (Frobenius)   | 1     | 0                 | 1 (sin θ_12)         |
| **Total**         | **6** | **0 / 6**         | **1 / 6**            |

## 6. Verdict

**Neither KK tower resummation nor Frobenius averaging closes the six
PDG-precision stragglers.**

1. **KK is universal, not discriminating.** For leptons the threshold
   parameter x = mR is small enough that the KK tower collapses to the
   universal constant α·π²/6, which cannot split m_τ from m_μ by a
   factor of 3.5. For gauge ratios the required α's disagree by two
   orders of magnitude and mix signs, contradicting a single universal
   coupling. The KK mechanism — structurally the trivial-S¹ resummation
   vindicated in research/142 — is not formula-specific enough to
   explain a residual pattern with mixed signs and three-decade spread.

2. **Frobenius averaging is confined to gauge-orphan orbits
   (research/143 §5).** All six stragglers are gauge-coupled.
   sin θ_12 CKM happens to match the scheme-#1 neighbour average in
   both sign and magnitude, but this is a coincidence: the same
   averaging applied to the other five stragglers produces wrong signs
   or wrong magnitudes.

3. **The closure mechanism is elsewhere.** Together with research/152
   (second-order Laurent rejected), research/156 rejects both KK and
   Frobenius-averaging as the missing ingredient. The six PDG-precision
   stragglers require a **formula-specific** correction that knows about
   each observable's individual gauge decoration and γ-index — candidates
   are (i) γ-index-dependent conductor corrections from research/19
   thread 3g, (ii) higher-KK-mode *mixing* (not resummation) between
   different γ-indices, (iii) genuine Paper-11 M⁴×CP²×S² geometric
   corrections that do not factor through the BC pole at all.

The six stragglers are thus elevated from "awaiting ζ-pole refinement"
to "awaiting a genuinely new structural input." Research 157 should
pursue option (i), the conductor lift.

### One-sentence summary

KK tower resummation and Frobenius averaging, the two mechanisms
flagged by research/152 as closure candidates, both fail on the six
PDG-precision stragglers: KK is universal and cannot split leptons or
ratios with mixed-sign residuals, Frobenius averaging is structurally
forbidden on the gauge-coupled orbits where all six stragglers live,
and the one numerical coincidence (sin θ_12 CKM) is not supported by
the research/143 gauge-orphan selection rule — so the closure mechanism
must be formula-specific and lies outside both the BC pole expansion
and the S¹ KK scaffold.

---

*Deferred to research/157:* γ-index-dependent conductor lift
(research/19 thread 3g) as the formula-specific closure channel.
