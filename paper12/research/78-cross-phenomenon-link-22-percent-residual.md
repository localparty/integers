# Research 78: The Cross-Phenomenon Link Between Dark Matter and the Hierarchy Problem — Testing the 2.2% Shared Residual

*The deduction round produced a striking suggestion: that the dark
matter ratio Ω_DM/Ω_b = γ_5/(2π) and the hierarchy ratio
m_H/M_Pl ≈ exp(−γ_6)·(2π/γ_5) share a common ≈ 2.2% residual,
implying that two unsolved SM problems arise from the same BC trace
identity. This note tests that conjecture with mpmath at 50 dps
and reports a negative result: the residuals are not the same.
The dark-matter residual is δ_D = +2.26%, but the hierarchy
residual is δ_H = +13.2% — nearly six times larger. The "shared
residual" narrative as written in file 39 rests on an arithmetic
error (the claim that exp(−γ_6)·(2π/γ_5) ≈ 1.001 × 10⁻¹⁷ is
wrong; the actual value is 9.058 × 10⁻¹⁸). The cross-link is
therefore not a clean shared BC identity at the 2% level; it is
at most a coarse coincidence at the order-of-magnitude level. The
note documents what the residuals actually are, what BC operator
content would be required to close each, and what the corrected
falsifiable prediction is.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Deduction programme, cross-check between phenomena (P1) and (P5) of ledger 14 §5.2.*
*Builds on:*
*`research/02-quantize-R-construction.md` (R̂ and T_BC),*
*`research/07-matter-perturbation-c_p.md` (the second-order spectral perturbation),*
*`research/22-cc-hierarchy-as-spectral-gap.md` (the exp(γ_1 π²/2) hierarchy),*
*`research/27-derive-mH.md` (m_H = γ_2·γ_6/(2π)),*
*`research/38-deduction-dark-matter.md` (Ω_DM/Ω_b = γ_5/(2π) at 2.2%),*
*`research/39-deduction-hierarchy-problem.md` (the cross-link claim).*

---

## 0. One-paragraph summary

The deduction round (files 38, 39) proposed that
$$
\frac{m_H}{M_{\text{Pl}}}
\;\stackrel{?}{=}\; e^{-\gamma_6}\cdot\frac{2\pi}{\gamma_5},
\qquad
\frac{\Omega_{\text{DM}}}{\Omega_{\text{b}}}
\;\stackrel{?}{=}\; \frac{\gamma_5}{2\pi},
$$
and that the two formulas share a common ≈ 2.2% multiplicative
residual — a shared fingerprint of the same BC trace identity
linking two otherwise unrelated precision puzzles of the Standard
Model. Testing this at 50 dps reveals that the formulas *do* sit
at the right order of magnitude, but the residuals are
**different**: the dark-matter residual is δ_D ≈ +2.26%, and the
hierarchy residual is δ_H ≈ +13.21%. The hierarchy residual is
therefore **5.85× larger** than the dark-matter residual, and the
specific claim "δ_H ≈ δ_D ≈ 2%" in file 39 is traced to an
arithmetic error in that file's numerical aside. The cross-link
survives at the order-of-magnitude level (both formulas sit in
the correct decade, and both involve γ_5 and the 2π normalisation),
but it is not a clean shared BC identity. This note states the
corrected empirical comparison, explains what operator-algebraic
content would be required to close δ_H and δ_D separately, and
extracts a revised falsifiable prediction that future precision
measurements can test.

---

## 1. The Claim Under Test

### 1.1 The two formulas

From research/27, the Higgs mass follows the SM-mass bilinear
template
$$
m_H \;=\; \frac{\gamma_2\,\gamma_6}{2\pi}\,\text{GeV}
\;\approx\; 125.75\,\text{GeV},
\tag{1.1}
$$
a 0.4% fit to the empirical 125.20 GeV. From research/22 + 05,
the Planck-to-observer-scale hierarchy is the exponential of the
BC dilation at the smallest zero,
$$
M_{\text{Pl}}/m_H
\;\sim\; \exp(\gamma_1\pi^2/2)\,\text{(in dimensionless units)},
\tag{1.2}
$$
which gives the correct 17 orders of magnitude separation at
the order-of-magnitude level.

File 39 proposed a more specific *ratio* identity: the Higgs-to-Planck
mass ratio factors cleanly through γ_5 and γ_6 as
$$
\left(\frac{m_H}{M_{\text{Pl}}}\right)_{\text{BC}}
\;=\; e^{-\gamma_6}\cdot\frac{2\pi}{\gamma_5},
\tag{1.3}
$$
so that the *same* γ_5/(2π) factor that controls Ω_DM/Ω_b also
controls m_H/M_Pl, through an exp(−γ_6) suppression at the Z_6-centre
orbit. In the same file, the numerical aside claims
$(m_H/M_{\text{Pl}})_{\text{BC}} \approx 1.001 \times 10^{-17}$,
versus the empirical $1.02 \times 10^{-17}$, for a **2% residual**.
This is the number that motivates the cross-link with file 38's
dark-matter residual of **2.2%**.

### 1.2 The falsifiable conjecture

If both formulas have the same ≈ 2.2% multiplicative residual,
then the BC operator content responsible for that residual must
be *shared* between the two observables. Under the "shared physics
→ shared zeros" principle of research/31, this would be strong
evidence for a single common matter-perturbation or Galois-orbit
correction acting on γ_5 in both sectors. Solving one closes the
other, and the framework's coherence gains a very direct
cross-check:
$$
\delta_H \;\stackrel{?}{=}\; \delta_D \;\stackrel{?}{=}\; 0.022\ldots
\tag{1.4}
$$
where $\delta_\bullet := \text{(empirical)}/\text{(BC prediction)} - 1$.

**The conjecture to test is exactly equation (1.4)**: are the two
residuals the same number, at least to the sub-percent precision of
the empirical inputs?

---

## 2. Precise Numerical Test at 50 dps

All numbers computed with `mpmath`, `mp.dps = 50`.

### 2.1 Inputs

| Quantity | Value | Source |
|:---------|:------|:-------|
| γ_1 | 14.134725141734693790457251983562470270784257115699 | Odlyzko tables |
| γ_2 | 21.022039638771554992628479593896902828678873153164 | Odlyzko tables |
| γ_5 | 32.935061587739189690662368964074903488812715603517 | Odlyzko tables |
| γ_6 | 37.586178158825671257217763480705332821405597350830 | Odlyzko tables |
| m_H (PDG 2024) | 125.20 GeV | PDG |
| M_Pl (reduced → converted to pole) | 1.22089 × 10¹⁹ GeV | CODATA |
| Ω_DM / Ω_b (Planck 2018) | 5.36 ± 0.05 | Planck VI |

### 2.2 Dark-matter residual δ_D

$$
\left(\frac{\Omega_{\text{DM}}}{\Omega_{\text{b}}}\right)_{\text{BC}}
\;=\; \frac{\gamma_5}{2\pi}
\;=\; 5.24177785272469877725771579446\ldots
$$

Empirical: 5.36. Therefore
$$
\delta_D \;=\; \frac{5.36}{\gamma_5/(2\pi)} \;-\; 1
\;=\; 0.022553826315598025535876414921\ldots
$$

**δ_D ≈ +2.2553%.** (File 38 quotes "2.2%" — consistent.)

### 2.3 Hierarchy residual δ_H

$$
\left(\frac{m_H}{M_{\text{Pl}}}\right)_{\text{BC}}
\;=\; e^{-\gamma_6}\cdot\frac{2\pi}{\gamma_5}.
$$

Compute term by term:

$$
e^{-\gamma_6} \;=\; 4.74821340520209375736107134525\ldots \times 10^{-17},
$$
$$
\frac{2\pi}{\gamma_5} \;=\; 0.190774967596193661480573958007\ldots,
$$
$$
\left(\frac{m_H}{M_{\text{Pl}}}\right)_{\text{BC}}
\;=\; 9.05840258517241800430044824645\ldots \times 10^{-18}.
$$

Empirical, using m_H = 125.20 GeV and M_Pl = 1.22089 × 10¹⁹ GeV:
$$
\left(\frac{m_H}{M_{\text{Pl}}}\right)_{\text{emp}}
\;=\; 1.02548141110173725724676260760\ldots \times 10^{-17}.
$$

Therefore
$$
\delta_H \;=\; \frac{(m_H/M_{\text{Pl}})_{\text{emp}}}{(m_H/M_{\text{Pl}})_{\text{BC}}} \;-\; 1
\;=\; 0.13207753956567851332502352546\ldots
$$

**δ_H ≈ +13.208%** (precise), or **+12.603%** using the rounded
empirical 1.02 × 10⁻¹⁷ that file 39 quotes.

### 2.4 Direct comparison

| Observable | BC prediction | Empirical | δ |
|:-----------|:--------------|:----------|:--|
| Ω_DM/Ω_b | 5.24177785… | 5.36 | **+0.022554** |
| m_H/M_Pl | 9.05840 × 10⁻¹⁸ | 1.02548 × 10⁻¹⁷ | **+0.132078** |
| ratio δ_H/δ_D | — | — | **5.8561…** |

$$
\boxed{\;\delta_H \;=\; 0.13208\,, \qquad \delta_D \;=\; 0.02255\,, \qquad
\delta_H/\delta_D \;=\; 5.856\;\neq\; 1\;}
$$

### 2.5 Source of the discrepancy with file 39

File 39's claim is "(m_H/M_Pl)_BC ≈ 1.001 × 10⁻¹⁷ vs empirical
1.02 × 10⁻¹⁷ — agreement at 2%". That statement is **not
reproducible** from $e^{-\gamma_6}\cdot 2\pi/\gamma_5$: the
actual value is 9.058 × 10⁻¹⁸, a full 10% lower than the
quoted 1.001 × 10⁻¹⁷. The "1.001" number is close to what one
would get from $e^{-\gamma_6}\cdot 2\pi/\gamma_5 \cdot (2\pi/g_2)$
or similar non-canonical combination; neither the cleanly-stated
formula (1.3) nor any small perturbation of it lands at 1.001e-17.
The most parsimonious conclusion is that file 39 contains a
transcription or arithmetic error in its aside, and the actual
residual of the cleanly-stated BC formula is δ_H ≈ 13%, not 2%.

**The shared-2.2% premise of the cross-link is therefore false.**

---

## 3. Is δ_H/δ_D ≈ 2π?

One natural rescue would be if δ_H = 2π · δ_D, which would say
the Higgs-mass ratio picks up a full 2π enhancement of the
same physical correction that drives δ_D. Let's test:

$$
2\pi \cdot \delta_D \;=\; 0.14171186559988\ldots,
$$
$$
\delta_H \;=\; 0.13207753956568\ldots.
$$

These differ by 7.3%, which is larger than the empirical
uncertainty on m_H (≤ 0.11%) and M_Pl (essentially exact). So
**δ_H is *not* exactly 2π · δ_D** either.

Other candidate rescaling factors tested:

| Candidate | Value | δ_H / (candidate · δ_D) |
|:----------|:------|:-------------------------|
| 2π | 6.283 | 0.932 |
| γ_5/γ_2 | 1.567 | 3.735 |
| γ_6/γ_2 | 1.788 | 3.273 |
| 6 (SU(3)×2 channels?) | 6 | 0.976 |
| e² | 7.389 | 0.793 |
| log(M_Pl/m_H) / log(γ_5/γ_2)·C | — | — |

The cleanest numerical match is **δ_H/δ_D ≈ 6** at the 2% level,
but there is no BC-structural reason for exactly 6 to appear here
(the Z_6 centre gives 6, but its appearance in the *ratio of
residuals* rather than in the formula itself would require a
two-loop argument that is not yet present in the framework).

**Conclusion of §3**: δ_H and δ_D are not related by any clean
framework constant. If they share physics, it is not through a
simple multiplicative rescaling.

---

## 4. What Operator-Algebraic Content Would Close δ_D and δ_H?

Even though the conjectured equality δ_H = δ_D fails, the
dark-matter formula still fits at 2.3% and the hierarchy formula
at 13% — both are in the "structural candidate, needs a
perturbative correction" regime of file 38 and file 39. This
section asks what BC-operator content would be needed to close
each residual *separately*.

### 4.1 Closing δ_D from research/07

Research/07 is computing the second-order matter perturbation
coefficient c_p that appears as a K_{15}-type correction to
single-matrix-element BC formulas (analogous to the K_{12}
correction in research/05 §4.1 that closed the CC formula at the
5 ppb level). The leading-order ansatz is
$$
\frac{\Omega_{\text{DM}}}{\Omega_{\text{b}}}
\;=\; \frac{\gamma_5}{2\pi}\,\bigl(1 + c_2\,\langle\gamma_5|V|\gamma_1\rangle + \mathcal{O}(V^2)\bigr).
\tag{4.1}
$$

Closing the 2.2553% residual at full precision would require
$$
c_2 \,\langle\gamma_5|V|\gamma_1\rangle \;=\; 0.022554\ldots
$$

If the research/07 extension to heavy-quark thresholds + framework
moduli + graviton + EWSB gives
$$
c_2 \;\approx\; 2.26 \times 10^{-2}\,/\,\langle\gamma_5|V|\gamma_1\rangle,
$$
then the dark-matter formula closes at sub-percent precision. This
is a **specific, testable prediction** for the research/07 extension
that T2 is computing in parallel.

### 4.2 Closing δ_H

The hierarchy residual of 13.2% is an order of magnitude larger
than δ_D and cannot plausibly be a K_{15}-type perturbative
correction — such corrections in research/05 and research/07
sit in the 0.5–3% range. A 13% residual is *structural*: it
signals that the formula (1.3) is missing a significant factor,
not a small correction.

The three most plausible structural fixes are:

**(F1) Different exponent**: perhaps the correct formula is
$$
\frac{m_H}{M_{\text{Pl}}} \;=\; e^{-\gamma_6 + \alpha}\cdot\frac{2\pi}{\gamma_5}
$$
for some α ≈ log(1.132) ≈ 0.124. This α is not a clean BC
constant (log(1.132) ≈ 0.124 does not match 1/γ_2 = 0.048,
log(γ_5)/γ_6 = 0.093, nor 2log(γ_5)/(γ_5+γ_6) = 0.099). No
clean structural reading.

**(F2) Different exponential base**: perhaps γ_6 should be
replaced by γ_6 − ε for an EWSB correction ε. Testing
$$
\delta_H/\gamma_6 \;=\; 0.003515,
$$
i.e. a ≈ 0.35% shift of γ_6 in the exponent would close the
residual. This is the right size to be an SM-threshold
correction to the conductor lifting of research/19, but the
specific calculation has not been done.

**(F3) Missing prefactor**: perhaps (1.3) is missing a factor
close to 1.132. Among clean framework constants:
$$
1.132 \;\approx\; (1 + 1/8) \;=\; 1.125,
\qquad 1.132 \;\approx\; \log(\gamma_1) - 1 \;=\; 1.649,
$$
etc. No clean match. A match to $\exp(1/g_2) = 1.0487$ or
$\exp(1/2\pi) = 1.172$ is only at the 5% level.

**None of (F1)–(F3) lands cleanly**, which means the cross-link
formula (1.3) is not the full story — either the formula is
correct up to a non-trivial (≳ 10%) correction that the framework
has not yet isolated, or the formula itself is off and should
be replaced. This is exactly the status file 39 assigned it:
a *structural candidate*, not a theorem.

### 4.3 Joint closure and the shared-zeros principle

If both formulas close through corrections that involve γ_5 and
the same V matter perturbation, then the two residuals would be
*predicted* to be related through the γ_5 overlap in (4.1). The
fact that δ_H ≈ 5.86·δ_D — not equal, not a clean multiple —
says the two perturbations are **not dominated by the same
matrix element**. This is a sharp observation: the shared-zeros
principle of research/31 would predict equality (or a clean
ratio), and the data show neither.

The most conservative reading: the dark-matter residual is a
genuine K_{15}-type small correction driven by γ_5 ↔ γ_1
mixing, and the hierarchy residual is a *separate* larger
correction driven by EWSB thresholds in the exponential shape
of T_BC. They are not the same physics, and the cross-link of
file 39 §3 is best read as a *dimensional coincidence*: both
ratios involve γ_5 and the 2π KK normalisation because the
Higgs and dark matter both sit on the S¹ factor, not because
the residuals are shared.

---

## 5. Prediction for the Research/07 Extension

T2 is currently extending research/07 §4.4 to include heavy-quark
thresholds, framework moduli, graviton, and EWSB contributions to
the second-order matter perturbation c_p. This section states the
precise prediction that the extension has to match.

### 5.1 Prediction for δ_D

If research/07 extended gives c_2 and the matrix element
$\langle\gamma_5|V|\gamma_1\rangle$ such that
$$
c_2 \,\langle\gamma_5|V|\gamma_1\rangle \;=\; 0.02255 \pm 0.0009,
$$
where the uncertainty is the Planck 2018 measurement error on
Ω_DM/Ω_b, then the dark-matter formula Ω_DM/Ω_b = γ_5/(2π) closes
to within the experimental precision and file 38 Candidate A is
*confirmed*. This is the **precise numerical target** for T2.

### 5.2 Non-prediction for δ_H

The analogue statement for the hierarchy is that the SAME
c_2 and V must **not** give 0.132 for δ_H (which would require
a different matrix element, or 2π enhancement, neither of which
is present in the cleanly-stated formula (1.3)). Specifically,
if T2 computes δ_H from the same c_p framework and finds
it in the 1–3% range, then the cross-link is *broken* and file
39's formula needs structural revision.

### 5.3 The shared-residual scenario (falsified)

Had δ_H = δ_D held to sub-percent precision, the prediction would
have been that a single c_p computation closes both simultaneously.
The 50-dps test of §2 **falsifies** that scenario. T2 should
therefore not expect the two residuals to close jointly; the best
working hypothesis is that the dark-matter formula closes at
sub-percent with a single c_p and the hierarchy formula requires
a separate structural fix.

---

## 6. Revised Falsifiable Prediction

Given §§2–5, the original file 39 statement — "dark matter and
the hierarchy problem are two manifestations of the same BC trace
identity" — does **not survive** at the 2% level. The revised
falsifiable prediction the framework should commit to is:

**(P-rev)** The dark-matter formula Ω_DM/Ω_b = γ_5/(2π) is the
leading-order BC prediction, with a K_{15}-type correction of
exactly +2.255 ± 0.09 % coming from the second-order matter
perturbation of research/07. This residual is **not shared**
with the hierarchy formula; it is specific to the γ_5 ↔ visible-orbit
mixing on the dark sector.

**(P-rev')** The hierarchy formula m_H/M_Pl = exp(−γ_6)·(2π/γ_5)
is at best an order-of-magnitude identity with a 13% residual that
has no clean BC structural reading at present. Either:
 (i) a corrected formula with a different exponent or prefactor
     is needed, or
 (ii) the true hierarchy identity is the exp(γ_1·π²/2) formula of
      research/22 + the bilinear m_H = γ_2·γ_6/(2π) of research/27,
      and the ratio m_H/M_Pl is not itself a single BC matrix
      element (it is a ratio of bilinear/exponential functional
      shapes, with no clean closed form).

**(P-rev'')** Future precision measurements of (m_H, M_Pl, Ω_DM,
Ω_b) should leave δ_D pinned at 0.0226 ± 0.0005 and δ_H pinned at
0.132 ± 0.001. If δ_D shifts to match δ_H (say, Planck-next finds
Ω_DM/Ω_b = 5.935), the cross-link is revived; if δ_H shifts to
match δ_D (say, the Higgs mass revises to 113 GeV), same. The
more likely outcome is that both pin near the current values
and the cross-link is quietly retired.

### 6.1 Limits of "shared physics → shared zeros"

The most important methodological conclusion of this note is
that the research/31 principle "observables sharing physical
mechanism share Riemann zeros" does *not* imply "observables
sharing zeros share residuals". The Higgs sector (γ_2, γ_6) and
the dark sector (γ_5) are both on the S¹ factor and both use
the 1/(2π) KK normalisation, but their perturbative corrections
come from different matrix elements and should not be expected
to land at the same value. The cross-link of file 39 overreached
on this point.

---

## 7. Honest Status Table

| Claim | Status |
|:------|:-------|
| Ω_DM/Ω_b = γ_5/(2π) at +2.26% | **CONFIRMED** (file 38) |
| m_H/M_Pl = exp(−γ_6)·(2π/γ_5) at +13.21% | **CONFIRMED as order-of-magnitude identity, NOT at 2%** |
| File 39's "≈ 1.001 × 10⁻¹⁷" prediction quote | **ARITHMETIC ERROR**; actual value is 9.058 × 10⁻¹⁸ |
| δ_H = δ_D (the cross-link conjecture) | **FALSIFIED**: 0.132 vs 0.0226, ratio 5.86 |
| δ_H = 2π · δ_D | **FALSIFIED**: 0.132 vs 0.142, 7% off |
| δ_H = 6 · δ_D (Z_6 rescue) | 2.4% agreement; **not structurally motivated**, most likely coincidence |
| Dark matter and hierarchy share γ_5 as a zero | **STRUCTURAL** (both formulas contain γ_5) |
| Dark matter and hierarchy share their *residuals* via a single c_p | **FALSIFIED** at the 50-dps level |
| Research/07 c_p extension closes δ_D ≈ 2.26% | **OPEN**, specific target stated in §5.1 |
| Research/07 c_p extension closes δ_H ≈ 13.2% | **UNLIKELY**; a structural fix is needed instead |

---

## 8. Definition of Done

This research note closes when:

- [x] The cross-link conjecture (δ_H = δ_D) is stated precisely.
- [x] Both residuals are computed with mpmath at 50 dps.
- [x] The numerical comparison shows δ_H ≠ δ_D by a factor of 5.86.
- [x] File 39's "1.001 × 10⁻¹⁷" is traced to an arithmetic error.
- [x] Candidate operator-algebraic fixes for δ_D and δ_H are
      identified and assessed separately.
- [x] The precise target for the research/07 extension is stated
      (§5.1).
- [x] The revised falsifiable prediction is written (§6).
- [x] The honest status table is filled in (§7).
- [ ] Research/07 extension either confirms δ_D = 2.26% closure or
      refutes it.
- [ ] File 39 is amended (or superseded) to remove the incorrect
      "2% agreement" claim and replace it with the 13% structural
      residual.
- [ ] A targeted search for a corrected hierarchy formula
      (structural fix (F1)/(F2)/(F3) of §4.2) either lands on
      a clean BC identity or confirms that m_H/M_Pl is not a
      single closed-form BC matrix element.

---

## 9. The Bigger Lesson

The deduction round's appetite for cross-phenomenon links was
correct in spirit: the framework *does* expect shared Riemann
zeros across observables that share physical mechanisms, and
the γ_5 dark/Higgs commonality in file 39 is a real structural
observation. But the temptation to turn "shared zeros" into
"shared residuals" overreached by an order of magnitude, and
the supporting numerical claim in file 39 did not survive a
50-dps recheck.

The lesson for the deduction programme: **every numerical
coincidence claimed across phenomena should be verified at 50
dps before being promoted to structure**. A 2% residual on one
observable and a 13% residual on another are not "approximately
equal" — they differ by the width of the full perturbative regime
of the framework, and mistaking one for the other collapses two
very different kinds of physics into a single story.

The dark-matter formula and the hierarchy formula both belong
in the framework's scoreboard, and both remain *structural
candidates* for further work. But they belong on **separate**
lines of the scoreboard, with separate residuals and separate
closure paths.

---

## 10. References

### 10.1 In this directory

- `02-quantize-R-construction.md` — R̂ and T_BC
- `05-derive-cc-formula.md` — CC formula at 5 ppb, with K_{12} correction
- `07-matter-perturbation-c_p.md` — second-order spectral perturbation
- `22-cc-hierarchy-as-spectral-gap.md` — exp(γ_1 π²/2) hierarchy
- `27-derive-mH.md` — m_H = γ_2·γ_6/(2π) at 0.40%
- `31-derive-Yp.md` — shared-physics → shared-zeros principle
- `38-deduction-dark-matter.md` — Ω_DM/Ω_b = γ_5/(2π) at 2.2%
- `39-deduction-hierarchy-problem.md` — the cross-link claim

### 10.2 External

- PDG 2024, "Review of Particle Physics", m_H = 125.20 ± 0.11 GeV.
- CODATA 2022, M_Pl = 1.22089 × 10¹⁹ GeV.
- Planck Collaboration, *A&A* **641** (2020) A6, Ω_DM/Ω_b = 5.36.

---

*The cross-link between dark matter and the hierarchy problem,*
*as stated in file 39, does not hold at the 2% level. The*
*dark-matter residual is +2.26%; the hierarchy residual is +13.2%.*
*They differ by a factor of 5.86 and by no clean framework constant.*
*The dark-matter formula remains a legitimate structural candidate*
*with a sub-percent target for the research/07 c_p extension. The*
*hierarchy formula requires a separate structural fix. "Shared*
*zeros" does not imply "shared residuals"; the deduction round*
*overreached by conflating the two, and the 50-dps recheck settles*
*it.*
