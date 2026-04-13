# Route 2: Borel Summability + Watson's Theorem

*ORA v8 Tier B excision run. Route 2 of 4.*
*Target: Prove H4 via Borel summability of the perturbative series + Watson's theorem.*

---

## 1. Strategy

If the perturbative series for the Schwinger functions is Borel summable in the coupling g^2, then Watson's theorem (or its Nevanlinna improvement) gives:

- The Borel sum is the UNIQUE function in a sector of the complex g^2 plane that is analytic and has the perturbative series as its asymptotic expansion.
- If the non-perturbative Schwinger function is also analytic in the same sector, the Borel sum must agree with the non-perturbative answer.

Combined with the gradient-flow analyticity (F(t) analytic in t, hence the coupling-dependence is controlled), this could close H4.

## 2. Analysis: Borel summability of 4D SU(N) YM

### 2.1 What is known

**Positive results (lower dimensions / simpler models)**:
- phi^4 in 2D and 3D: Borel summable (Eckmann-Magnen-Seneor 1975, Feldman-Osterwalder 1976, Magnen-Seneor 1977).
- Gross-Neveu in 2D: Borel summable (Feldman-Magnen-Rivasseau-Seneor 1986).
- 2D YM: Borel summable (trivially, since 2D pure YM is exactly solvable).

**Negative indicators (4D)**:
- IR renormalons: In 4D YM, the perturbative coefficients grow as c_n ~ n! * beta_0^n from infrared renormalon singularities at positive real values of the Borel variable u = n * beta_0. These lie ON the integration contour of the Borel integral, potentially obstructing Borel summability.
- UV renormalons: Located at u = -n * beta_0 (negative real axis), these do NOT obstruct the Borel integral but contribute to the factorial growth.
- Instantons: The instanton-anti-instanton amplitude ~ exp(-16pi^2/g^2) produces singularities at u = 4 in the Borel plane, on the positive real axis.

### 2.2 The renormalon obstruction (detailed)

The leading IR renormalon in the two-point correlator <Tr F^2(x) Tr F^2(0)> produces a Borel-plane singularity at:

$$u_{\text{IR}} = 2 \quad (\text{first IR renormalon})$$

This corresponds to factorial growth c_n ~ n! * (beta_0/2)^n in the perturbative coefficients. The singularity is on the positive real axis (u > 0), which IS the integration contour for the Borel integral:

$$\text{Borel sum} = \int_0^\infty du \, e^{-u/g^2} \, \hat{F}(u)$$

where hat{F}(u) is the Borel transform. The singularity at u = 2 makes the integral AMBIGUOUS — different integration prescriptions (above/below the singularity) give different answers differing by O(exp(-2/g^2)).

### 2.3 Can the Balaban construction resolve the ambiguity?

The Balaban construction provides an UNAMBIGUOUS non-perturbative answer F(t). If we could show:

(a) F(t) at fixed t > 0 is the UNIQUE function in a sector containing the positive real g^2 axis whose perturbative expansion matches the perturbative series,

then the Borel ambiguity would be resolved by the construction itself — F(t) would SELECT the correct integration prescription.

However, establishing (a) requires precisely the kind of non-perturbative control that H4 provides. The Balaban construction gives F(t) as a well-defined number for each g^2 > 0, but it does not come with a proof that F(t) is the unique Borel sum.

### 2.4 Watson's theorem: requirements and obstacles

Watson's theorem (1912; see Hardy, "Divergent Series" Ch. 8) states: if f(z) is analytic in a sector S = {z : |arg z| < pi/2 + epsilon} and |f(z)| <= C e^{A|z|} in S, and f has asymptotic expansion sum a_n z^n as z -> 0 in S, then f is the unique such function and the Borel sum of sum a_n z^n equals f(z).

Applied to the YM correlator as a function of g^2:
- z = g^2 (coupling)
- S must be a sector of opening > pi centered on the positive real axis
- f(g^2) = F(t; g^2) at fixed t

**Obstacle A**: We need F(t; g^2) to be analytic in g^2 in a sector wider than {Re(g^2) > 0}. The Balaban construction works for g^2 > 0 small and provides analyticity in g^2 by property (B1), with k-independent radius rho > 0. But (B1) gives analyticity in a DISK |g^2| < rho, not in a sector. For Watson's theorem we need analyticity in a sector of opening > pi.

**Obstacle B**: The exponential bound |F| <= C exp(A/|g^2|) is needed in the sector. This requires UNIFORM bounds on F as g^2 -> 0 along complex directions, which the Balaban construction does not currently provide for complex g^2.

**Obstacle C**: Even granting analyticity in a sector, the IR renormalon singularity at u = 2 means the perturbative series is NOT Borel summable in the standard sense — we would need a resurgent extension (Ecalle 1981) or a medial summation (averaging above and below the singularity), and proving that the non-perturbative F(t) equals the medial sum requires knowledge of the non-perturbative corrections (instantons, renormalons), which circles back to H4.

## 3. The flow-time variable: a different Borel structure?

One new angle from the brief: the perturbative expansion in the FLOW-TIME variable t may have a different Borel structure than the expansion in g^2.

At fixed x,y with |x-y| > 0, the rescaled correlator F(t) is analytic in t on |t| < r_t (Lemma L.3.7 Step 2) with CONVERGENT Taylor series. This means:

**The t-expansion is NOT a formal asymptotic series — it is a CONVERGENT series.**

A convergent series is trivially Borel summable. Its Borel sum equals its ordinary sum, which equals F(t).

**But this does not help**: The convergence of the t-expansion is a statement about the non-perturbative F(t). The PERTURBATIVE expansion of F(t) in powers of g^2 at fixed t is a DIFFERENT expansion, and this is the one with renormalon problems.

The two expansions (in t and in g^2) are not interchangeable: the t-expansion is a Taylor series of the non-perturbative function F around t=0, while the g^2-expansion is a perturbative expansion at fixed t. They live in different parameter spaces.

## 4. Rivasseau's constructive approach

The brief mentions Rivasseau's constructive QFT results on Borel summability of phi^4_4.

**Status**: Rivasseau's programme (with Magnen and Seneor) proved Borel summability for:
- phi^4_2 (CMP 56, 1977)
- phi^4_3 (Feldman-Magnen-Rivasseau-Seneor, CMP 98, 1985)
- Gross-Neveu in 2D (Feldman-Magnen-Rivasseau-Seneor, CMP 103, 1986)

For phi^4_4 (the 4D case): NOT proved. The theory is believed to be trivial (Aizenman-Frohlich), so Borel summability of the perturbative series around the free field is meaningful but different from the interacting case.

For 4D SU(N) YM: No constructive Borel summability result exists. The asymptotic freedom makes the UV behavior better than phi^4_4, but the IR renormalon problem (Obstacle C above) remains.

**Can Rivasseau's methods be ported?** The key technique is the "phase space expansion" — a multi-scale cluster expansion that controls each RG scale independently. The Balaban construction IS such an expansion for YM. But Rivasseau's Borel summability proofs for lower-dimensional models rely on:
1. Super-renormalizability (for phi^4_2, phi^4_3) or asymptotic freedom (Gross-Neveu 2D).
2. Absence of IR renormalons in those models.

4D YM has asymptotic freedom but ALSO has IR renormalons, which are absent in super-renormalizable theories and in 2D models. The IR renormalon problem is specific to 4D gauge theories and has no precedent in the constructive QFT literature.

## 5. Verdict: BLOCKED

Route 2 is BLOCKED by the IR renormalon obstruction. The specific blockers are:

**(a) IR renormalons at u = 2 on the positive real Borel axis** make the perturbative series for <Tr F^2 Tr F^2> NOT Borel summable in the standard sense. A resurgent or medial summation might work, but proving the non-perturbative answer equals the medial sum requires control of non-perturbative corrections that is equivalent to H4.

**(b) Watson's theorem requires analyticity in a sector of g^2**, not just a disk. The Balaban analyticity (B1) gives a disk |g^2| < rho, not a sector. Extending to a sector requires new estimates for complex coupling.

**(c) No constructive QFT precedent** for Borel summability of 4D non-Abelian gauge theories exists.

**What is new compared to prior work**: The distinction between the t-expansion (convergent) and the g^2-expansion (divergent) is now clear. The flow-time analyticity is a genuine asset but addresses the wrong variable — it gives convergence in t, not in g^2.

**Re-entry gate**: A proof that IR renormalons cancel in the gradient-flow-renormalized correlator F(t) = S_{2,t}^c/c_1(t)^2. If the c_1(t)^2 rescaling absorbs the IR renormalon ambiguity, the RESCALED perturbative series might be Borel summable even though the unrescaled one is not. This is speculative but would be a natural consequence of the gradient flow's UV-IR interplay.

---

## What the next runner needs to know

- **State at handoff**: BLOCKED. IR renormalon obstruction is the fundamental issue.
- **Open dependencies**: Resurgence programme for 4D SU(N) YM; IR renormalon cancellation in gradient-flow correlators.
- **Watch out for**: The t-expansion convergence (Lemma L.3.7) is NOT the same as Borel summability in g^2. Do not conflate them.
- **Preferred next move**: Investigate whether the c_1(t)^2 rescaling in F(t) = S_{2,t}^c/c_1(t)^2 absorbs the IR renormalon ambiguity. If c_1(t) is computed perturbatively and the renormalon ambiguity in S_{2,t}^c is cancelled by the ambiguity in c_1(t)^2, the rescaled series for F(t) might be Borel summable.
- **Voice canon citation**: P6 — the renormalon is a projection artifact of organizing the non-perturbative answer as a power series in g^2.
