# Gap B2 — Fredenhagen–Marcu direction of implication

## 1. Statement of the gap

Section 4.3 ("Consequences" item 4, `04-lattice-proof-part1.md` L704–722) and
Section 4.4 (Theorem 4(e), L794–800) cite Fredenhagen–Marcu (CMP 92, 1986) as
if it gives "$\sigma > 0 \Rightarrow \Delta > 0$". In fact, the FM theorem
runs in the *converse* direction: the vanishing of the gauge-invariant order
parameter $\rho_{\mathrm{FM}}$ *diagnoses* confinement (absence of charged
finite-energy states), not a mass gap from an area law. The separate
quantitative claim "$\Delta \geq c\sqrt\sigma$" cited in Theorem 4(e) is the
heuristic flux-tube/closed-string argument of Appendix F.3, not a theorem.
Independently, the sentence at L719 ("area-law decay $e^{-\sigma TR}$
requires $E_1\geq\sigma R$ for all $R$") is mathematically wrong: it would
force $E_1 = \infty$. The rigorous mass gap comes from a completely
different chain that is already implicit in the preprint but obscured by
the FM framing.

## 2. The corrected rigorous chain

**Proposition B2.1 (Cluster expansion ⇒ exponential clustering).** *For
$\beta < \beta_{\max}(a) = m_1 a/6 - \ln(c_d K C_0^{1/6})$ with
$m_1 = 2\sqrt N/r_3$, the Kotecký–Preiss cluster expansion of §4.3
converges absolutely, and connected correlators of local gauge-invariant
lattice observables satisfy*
$$|\langle \mathcal O(x_1)\cdots\mathcal O(x_n)\rangle_c|
\ \leq\ C_n\,\exp\!\big(-(\alpha/a)\,\mathrm{diam}(\{x_i\})\big)$$
*with Kotecký–Preiss weight $\alpha > 0$.*

*Citation.* Theorem 2 of §4.3 (`04-lattice-proof-part1.md` L394–563) plus
the Kotecký–Preiss lemma (Kotecký–Preiss CMP 103, 1986; Brydges, *A short
course on cluster expansions*, Les Houches 1984).

**Proposition B2.2 (Reflection positivity).** *The KK-enhanced lattice action
$S = S_{4\mathrm D}[U] + S_{\mathrm{int}}[U,A] + \sum_\ell V_\ell$ satisfies
reflection positivity with respect to time reflection $\theta$. The
transfer matrix $\hat T$ exists, is bounded, self-adjoint, and
positivity-preserving on the GNS Hilbert space.*

*Citation.* Lemma D.2 of Appendix D (`D-reflection-positivity.md` L172–226),
with the bond kernel $e^{-c\|A'-UAU^{-1}\|^2}$ of positive type by
Bochner / Schur. Compare Osterwalder–Seiler CMP 60 (1978); Glimm–Jaffe 1987
Ch. 6; Seiler 1982 Ch. 6.

**Proposition B2.3 (Cluster rate ≤ transfer-matrix gap).** *Let $\hat T$ be
the transfer matrix of B2.2 with eigenvalues $\lambda_0 > \lambda_1 \geq
\cdots$ and lattice mass gap $\Delta_0 = -(1/a)\log(\lambda_1/\lambda_0)$.
For any centered local gauge-invariant $\mathcal O$, the spectral theorem
gives*
$$\langle\mathcal O(0,\vec 0)\,\mathcal O(t,\vec 0)\rangle
\ =\ \int_{\Delta_0}^{\infty}\,e^{-mt}\,d\rho_{\mathcal O}(m),$$
*with $\rho_{\mathcal O}$ positive. Any exponential clustering rate for
such 2-point functions is therefore a lower bound on $\Delta_0$; in
particular the rate $\alpha/a$ of B2.1 gives $\Delta_0 \geq \alpha/a > 0$.*

*Citation.* Transfer-matrix construction: Appendix C
(`C-transfer-matrix.md`). Spectral theorem / Källén–Lehmann:
Reed–Simon Vol. I Theorem VII.3 and Vol. IV §XIII.1. Exponential
decay ⇒ spectral gap: Simon, *The $P(\phi)_2$ Euclidean Quantum Field
Theory*, Princeton 1974, §III.3.

**Theorem B2.4 (Lattice mass gap, rigorous form).** *Combining B2.1–B2.3,
for $\beta < \beta_{\max}(a)$ the KK-enhanced lattice theory has
$\Delta_0(\beta) \geq \alpha/a > 0$, uniform in lattice volume.*

The chain is self-contained: (i) cluster expansion converges (Weitzenböck +
Kotecký–Preiss) → (ii) exponential clustering of connected correlators →
(iii) reflection positivity → (iv) spectral decomposition of $\hat T$ →
(v) mass gap = clustering rate. No area law, no FM criterion, no flux-tube
heuristic enters the rigorous argument.

## 3. Corrected statements for §4.3 item 4 and §4.4 Theorem 4(e)

**§4.3 "Consequences" item 4 (replacement for L704–722).**

> 4. *The mass gap satisfies $\Delta_0(\beta) \geq \alpha/a > 0$.* The
> Kotecký–Preiss weight $\alpha$ controls the exponential decay of
> *connected* correlators of centered local gauge-invariant observables
> (consequence (c)). By reflection positivity (Lemma D.2) the transfer
> matrix $\hat T$ is self-adjoint, and by the spectral theorem its mass
> gap $\Delta_0$ is bounded below by any exponential clustering rate of
> such 2-point functions. Hence $\Delta_0 \geq \alpha/a > 0$, uniformly
> in the lattice volume.
>
> *Remark 4.1 (area law as consistency check).* The same cluster bound
> yields an area law for Wilson loops, $\sigma_0 \geq \alpha > 0$
> (consequence (d)), whence $\rho_{\mathrm{FM}} = 0$. By the
> Fredenhagen–Marcu theorem this certifies the confined phase (no
> charged finite-energy states) — a physical-interpretation consistency
> check on $\Delta_0$, not a step in the mass-gap proof. The gap is
> already established above from the cluster expansion + RP.

**§4.4 Theorem 4(e) (replacement for L794–800).**

> *(e) $\Delta_0(\beta) \geq \alpha/a > 0$ for all $\beta < \beta_{\max}(a)$.*
> By Theorem 2 of §4.3 the cluster expansion produces exponential decay
> of connected correlators with rate $\alpha/a$ (part (c)); by Lemma D.2
> the transfer matrix is self-adjoint and every gauge-invariant 2-point
> function admits a positive spectral measure; by the spectral theorem
> (Reed–Simon Vol. IV §XIII.1) the infimum of the support of that
> measure — which is $\Delta_0$ — is at least $\alpha/a$.
>
> *Remark 4.2 (area law, Fredenhagen–Marcu, flux tube).* The area law
> $\sigma_0 > 0$ of (d), the Fredenhagen–Marcu diagnostic
> $\rho_{\mathrm{FM}} = 0$, and the heuristic flux-tube estimate
> $\Delta_0 \gtrsim 2\sqrt{\pi\sigma/3}$ of Appendix F.3 are physical
> consistency checks consistent with lattice-QCD phenomenology but are
> **not** steps in the rigorous chain. The rigorous lower bound is the
> cluster-expansion rate $\alpha/a$ above.

## 4. Clarifying remark on the status of FM and the flux-tube argument

Fredenhagen–Marcu (1986) is a *confinement diagnostic*: it characterizes
the absence of charged finite-energy states via a gauge-invariant order
parameter. It is important for verifying that the constructed theory is
genuinely confining, but it is a *consequence*, not an input, of the main
result. The heuristic flux-tube derivation in Appendix F.3 ($L_{\min}\sim
1/\sqrt\sigma$ from the uncertainty principle plus the Lüscher
$-\pi c/(6L)$ correction giving $m_{\mathrm{glueball}}\sim 2\sqrt{\pi\sigma/3}$)
is a *physical estimate* that matches phenomenological $\mathrm{SU}(3)$
lattice data but is not a theorem. Appendix F.3's "Theorem F.1" should be
relabeled "Heuristic estimate F.1" with a preface stating that the
rigorous lower bound on $\Delta_0$ used in the main proof is the
cluster-expansion rate $\alpha/a$ of Theorem 2, not $c\sqrt\sigma$.

With these edits, the rigorous backbone — cluster expansion (Theorem 2) →
exponential clustering → reflection positivity (Lemma D.2) → spectral
decomposition of $\hat T$ → mass gap — is cleanly separated from the
physics-level consistency checks (area law, FM, flux tube, Lüscher term).
The mass gap $\Delta_0>0$ is a theorem of the cluster expansion alone, as
already implicit in the preprint; the FM framing was obscuring this.
