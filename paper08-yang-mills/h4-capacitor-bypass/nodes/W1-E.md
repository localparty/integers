# W1-E — ERG↔QFT cell-fill and H4 bypass assessment

**Slot:** Wave 1, Author W1-E (ERG↔QFT). **Priority 2 (HIGH).**
**Model:** Opus 4.6 (1M context), effort max.
**Date:** 2026-04-13.
**Brief:** `strategy/06-h4-capacitor-bypass-brief.md` v3 §§1, 2.1, 3.0, 3.1, 3.4 (K-5 strengthened), 9.
**Mandatory framing:** K-5 strengthened. Nissim 2510.22788 is lattice-only; the minimum bypass chain is three open sub-steps (continuum limit → intrinsic UV extraction → $C_N$ derivation).
**File-owner scope:** this file only.

---

## Direction

The ERG↔QFT slot evaluates whether the Shen–Zhu–Zhu 2023 / Nissim 2025 cluster-expansion + Langevin construction of lattice Yang–Mills — which this year achieved unique infinite-volume mass-gap results for U(N), SU(N), SO(N) in the 't Hooft strong-coupling regime — can be extended, or composed with other machinery, to close H4 by a category shift at the construction level: existence of a non-perturbative Schwinger function whose UV singular structure is computed *directly from constructional quantities* (polymer activities, Langevin stationary measure, transfer-matrix spectrum) rather than by asymptotic-matching to the perturbative Feynman series (which lands inside the 9/10 LOCK, per K-5 v3 strengthened).

The category-shift claim at stake: H4 restated as "the non-perturbatively constructed $S_2^{\mathrm{ren}}$ admits a short-distance expansion whose leading coefficient agrees with $C_N = 2(N^2{-}1)/\pi^6$" where the agreement is derived *from the construction*, not by imposing the perturbative coefficient as a matching boundary condition.

The sharp question: what is the distance, in open-research units, between the Nissim/Shen–Zhu–Zhu lattice-IR construction and that UV-intrinsic statement? And is any known compound-bypass chain (Balaban + Langevin + Hastings–Koma-style polymer-decay spectral arguments) in principle able to close it?

The rest of this note is the answer.

---

## Research

### 1. What Nissim 2510.22788 actually proves

Verbatim extracts from the paper's front matter and introduction (arXiv:2510.22788v1, Ron Nissim, Oct 26 2025):

- Title: *"U(N) lattice Yang–Mills in the 't Hooft regime."*
- Abstract: *"We establish a mass gap, prove the existence of a unique infinite volume limit, and give a new proof of the large N limit for U(N) lattice Yang–Mills theory in the 't Hooft regime. These results were previously obtained for SU(N) and SO(N) lattice Yang–Mills theories as applications of the mixing of the associated Langevin dynamics, which is verified via the Bakry–Émery criterion. For U(N), however, this approach fails because its Ricci curvature is not uniformly positive, and as a result the Bakry–Émery condition cannot be easily verified. To overcome this obstacle, we recast the U(N) theory as a random-environment SU(N) model, where the randomness arises from a U(1) field, and combine cluster-expansion and Langevin-dynamics techniques to analyze the resulting U(1)×SU(N) model."*
- §1 Introduction: *"It is suspected that Yang–Mills theories, such as those with groups G ∈ {SU(N), SO(N), U(N)} for N ≥ 3 exhibit a mass gap at all β > 0 for d ∈ {3, 4}, the existing results always involve a strong coupling (small β) assumption. In the classic work of Osterwalder and Seiler [OS78], they used a cluster expansion argument to establish that every lattice Yang–Mills theory, regardless of gauge group G and dimension d, has a mass gap for sufficiently small β > 0. ... their condition reduces to β ≤ c_d/N for some small dimension dependent constant c_d."*
- §1 (scaling): *"We always use the 't Hooft scaling for β"*; *"the strong coupling regime with β < c_d is known as the 't Hooft regime."*
- **Theorem 1.1 (Mass gap and infinite volume limit).** *"Let d ≥ 2, N ≥ 2. Then for some fixed β̃ = β̃(d), and all β < β̃, there exists a probability measure $\mu_{U(N),\beta}$ on $U(N)^{E_{\Lambda_\infty}}$ (with $\Lambda_\infty = \mathbb{Z}^d$ ...) such that $\mu_{U(N),\Lambda_L,\beta} \to \mu_{U(N),\beta}$ weakly as $L \to \infty$. Additionally, for any smooth local observables f, g with $\Lambda_f, \Lambda_g \subseteq \Lambda$ ..., there exist constants $C_1 = C_1(N,d,|\Lambda_f|,|\Lambda_g|)$ and $C_2 = C_2(N,d)$ such that $|\mathrm{Cov}_{\mu_{U(N),\Lambda_L,\beta}}(f,g)| \leq C_1(\|f\|_{L^\infty}+\|f\|_{B_f})(\|g\|_{L^\infty}+\|g\|_{B_g}) e^{-C_2 d(\Lambda_f, \Lambda_g)}.$"*
- **Theorem 1.5 (Large N Limit for U(N)).** Factorization of Wilson loop observables at $N\to\infty$ for $\beta < \tilde\beta(\beta)$, $\langle W_{\ell_1}\cdots W_{\ell_n}\rangle - \prod \langle W_{\ell_i}\rangle \to 0$ in probability.

What Nissim does **not** establish (independently verified by the paper's table of contents, introduction, and explicit scope, plus cross-check against the SZZ23/SZZ24/CNS25 predecessor series):

- **No continuum limit.** The lattice spacing is fixed throughout. The limits taken are $L \to \infty$ (infinite volume) and $N \to \infty$ (large N). The scaling that drives the continuum limit (lattice spacing $a \to 0$ with $\beta \to \infty$ at the rate $1/g^2(a) \sim b_0 \log(1/a\Lambda)$ required by AF) is absent. The regime is $\beta < \betã(d)$ — **strong coupling at fixed lattice spacing** — the *opposite* of the continuum-limit regime, where $\beta \to \infty$.
- **No short-distance / UV content.** Mass gap is exponential decay of covariance at long separations on the lattice — an IR property. Nothing in the paper addresses the behavior of lattice correlators at separations small compared to the lattice spacing (which is ill-posed on a lattice), or of continuum Schwinger distributions near coincident points.
- **No OPE, no $C_N$.** The Wilson coefficient of $[\mathrm{Tr}\,F^2]_R$ in the identity channel, and the AF coefficient $C_N = 2(N^2-1)/\pi^6$, are not computed, referenced, or within the scope of the constructional machinery.
- **No Schwinger distribution at coincident points.** Observables are *smooth local observables* $f, g$ with finite supports $\Lambda_f, \Lambda_g$ on the lattice; the covariance bound is in terms of the lattice distance $d(\Lambda_f, \Lambda_g)$. Continuum coincident-point behavior is outside the framework.

### 2. Shen–Zhu–Zhu lineage and the strong-coupling ceiling

The Nissim result is the culmination of a 2023–2025 programme by Shen–Zhu–Zhu (SZZ) and collaborators that reinvents lattice YM mass-gap from a stochastic-analysis point of view:

- SZZ 2023 ("A stochastic analysis approach to lattice Yang–Mills at strong coupling," Comm. Math. Phys. 2023, arXiv preprint at BiBoS 23-06-620) — establishes uniqueness of invariant measure + exponential ergodicity + Log-Sobolev + Poincaré inequalities for the Langevin dynamics of lattice YM with group $G \in \{\mathrm{SU}(N), \mathrm{SO}(N)\}$ at strong coupling ($\beta$ small), via Bakry–Émery.
- SZZ 2024 ("Langevin dynamics of lattice Yang–Mills–Higgs and applications," arXiv:2401.13299) — extends to Yang–Mills–Higgs, keeps the small-$\beta$ condition.
- Chevyrev–Shen 2023 (arXiv:2302.12160) — 2D Yang–Mills Langevin, universality.
- Cao–Sheffield–Nissim 2025 (arXiv:2509.04688) — area law for lattice YM at strong coupling via the dynamical approach.
- Nissim 2510.22788 (Oct 2025) — the U(N) case, where Bakry–Émery fails because Ricci curvature of U(N) is not uniformly positive (U(1) centre eats the lower bound); the fix is to split the gauge group as $U(1) \times SU(N)$ random-environment decomposition and use cluster expansion on the U(1) marginal + conditional Langevin on the SU(N) piece.

The coupling regime across this entire programme is $\beta < c_d/N$ (Osterwalder–Seiler territory) or the equivalent 't Hooft-scaled small-$\beta$ range. **This is the strong-coupling regime.** Continuum 4D YM lives at the *opposite* end: $\beta = 2N/g_0^2(a) \to \infty$ as lattice spacing $a \to 0$ at the asymptotic-freedom rate. No paper in the SZZ/Nissim programme establishes or even announces as a target the extension to the weak-coupling / continuum regime.

Verbatim from Nissim §1: *"While it is suspected that Yang–Mills theories ... exhibit a mass gap at all β > 0 for d ∈ {3, 4}, the existing results always involve a strong coupling (small β) assumption."* This is explicit: the class of results to which Nissim belongs does not cover the coupling regime in which AF lives.

### 3. Balaban: the only known weak-coupling constructive machinery

The existing state-of-the-art for weak-coupling 4D lattice YM construction is the Balaban programme (CMP 95 (1984), CMP 109 (1987), CMP 119 (1988), CMP 122 (1989) I+II, Large Field Renormalization). Balaban iterates block-spin transformations on the lattice, controls the RG flow of effective actions under weak-coupling hypotheses, and proves ultraviolet stability (bounded partition function as lattice spacing tends to zero along the AF line). In Paper 8's proof-chain ledger, Steps 2–3 accept Balaban as established literature for lattice-to-continuum UV control of the measure (see `closing-H4/nodes/R.B.1-ccm-ym-analog.md` lines 594–595: *"bounded below by the polymer-convergence radius of the Balaban expansion at step k, which is k-independent by the Balaban"* — this is load-bearing for the W7-14 analyticity reframing).

Balaban's programme produces ultraviolet stability + effective-action control, but does *not* directly produce OS-positive continuum Schwinger functions with verified OPE structure at coincident points. The gap between Balaban's UV stability and H4 is precisely what Magnen–Rivasseau–Sénéor (CMP 155 (1993) 325) labels: their paper constructs YM₄ Schwinger functions with an **infrared cutoff still in place** (explicitly: *"in a regularized axial gauge … with a fixed infrared cutoff but no ultraviolet cutoff"*). The IR cutoff is what blocks the step from constructional machinery to short-distance asymptotics at the operator-product level.

So: the UV side has Balaban + Magnen–Rivasseau–Sénéor, both of which stop short of removing the IR cutoff. The IR side has Osterwalder–Seiler + SZZ + Nissim, both of which stop short of removing the strong-coupling restriction. The compatibility of these two programmes — running Balaban block-spin down from UV while running Langevin cluster expansion up from IR and matching in the middle — is not a theorem; it is not even a research programme that has been announced. The two sides are separated by the region $c_d/N \lesssim \beta \lesssim \infty$ of intermediate coupling where neither cluster expansion nor block-spin iteration has convergence.

### 4. Hastings–Koma polymer-decay + spectral-gap arguments

K-5 v3 strengthened specifies the condition for staying outside the LOCK at sub-step (b): *"Hastings-Koma-style spectral-gap + polymer-decay arguments extracting the $|x|^{-8}$ scaling from the construction itself are outside the LOCK; asymptotic-match-to-perturbative-series arguments are inside the LOCK."* What does a Hastings–Koma argument look like, and does it apply here?

Hastings–Koma (CMP 265 (2006) 781–804, arXiv:math-ph/0507008) and Nachtergaele–Sims (CMP 265 (2006) 119–130, arXiv:math-ph/0506030) established that in discrete quantum systems with short-range interactions, a nonvanishing spectral gap above the ground state implies exponential clustering of ground-state correlations in the spatial separation. The mechanism is a Lieb–Robinson light-cone bound + a contour integral of the resolvent around the gap. These arguments produce exponential decay rates of correlations as a direct consequence of the gap, computed from spectral data of the Hamiltonian — not by matching to any external series.

The architecture that would put this technique to work for H4:
1. Transfer-matrix quantisation of lattice YM (transfer matrix $T$; lattice Hamiltonian $H = -\log T$).
2. Continuum limit $a \to 0$ (OPEN) to obtain a continuum Hilbert space $\mathcal{H}$, Hamiltonian $H_\mathrm{cont}$, vacuum $\Omega$.
3. Spectral-gap bound on $H_\mathrm{cont}$ above $\Omega$ (OPEN in the weak-coupling regime; known in Nissim-regime only on lattice).
4. Hastings–Koma-type argument producing decay of $\langle \Omega | \mathcal{O}(x) \mathcal{O}(0) | \Omega \rangle$ in the spatial separation.

The issue: this produces *exponential* decay for massive theories, not the $|x|^{-8}(\log 1/|x|\Lambda)^{-2}$ polynomial scaling that H4 requires. The H4 OPE coefficient is a **short-distance** asymptotic of a **massless** channel of the correlator — the identity-channel OPE, which is dominated by the gluon-pair anomalous dimension, not by the mass gap. Hastings–Koma delivers the wrong observable for H4: it gives large-distance decay governed by the gap; H4 needs small-distance singular structure governed by the beta function.

The correct UV technique would have to produce, from the construction, the coefficient $C_N = 2(N^2-1)/\pi^6$ as a spectral-data quantity of the transfer-matrix / Langevin generator / polymer algebra. No such bridge is known. The perturbative calculation of $C_N$ proceeds by contracting the two $[\mathrm{Tr}\,F^2]$ vertices with the tree-level + one-loop propagator and extracting the $|x|^{-8}$ coefficient from the Feynman integrals — a Lorentz-invariant momentum-space calculation at zero external momentum. Translating this into a polymer-activity or Langevin-stationary-measure statement is the missing third sub-step.

### 5. The three open sub-steps enumerated

Given §§1–4 above, the minimum bypass chain for H4 via ERG↔QFT is:

- **Sub-step (a): Continuum limit exists.**
  - Required: $\mu_{\mathrm{YM}}$ on the space of continuum connections (modulo gauge) obtained as $a \to 0$ limit of a family of lattice measures $\mu_{\beta(a),a}$ with $\beta(a) \to \infty$ at the AF rate, preserving OS0–OS5 axioms.
  - State of research: partial. Balaban's UV stability controls the partition function along the AF line. Magnen–Rivasseau–Sénéor 1993 constructs Schwinger functions with an unremoved IR cutoff. No existing result removes the IR cutoff while preserving AF scaling for the coupling. The mass-gap side (SZZ/Nissim) delivers unique infinite-volume measure at fixed lattice spacing and strong coupling — the wrong end of the coupling line. There is no published bridge.
  - Verdict: **separate open research programme, at least 5–10 years of work**, depending on whether a 4D version of the Chevyrev–Shen regularity-structures programme (which works in 3D) becomes viable.
- **Sub-step (b): Intrinsic UV extraction from constructional quantities.**
  - Required: computation of short-distance asymptotics of $S_2^{\mathrm{ren}}(x,y)$ as $|x-y| \to 0$ from the construction of $\mu_{\mathrm{YM}}$, *without* invoking perturbative Feynman rules to identify the coefficient. The intrinsic technique candidates are (i) Hastings–Koma-type spectral-decay (but see §4: wrong observable); (ii) polymer-activity UV asymptotics of the Balaban / Magnen–Rivasseau–Sénéor expansion directly (not known to produce the correct $(\log)^{-2}$ AF correction); (iii) transfer-matrix spectral analysis at scales below the lattice cutoff (requires continuum limit, i.e. (a) first).
  - State of research: no published candidate technique. The closest analogue is $\phi^4_3$, where Glimm–Jaffe and Magnen–Rivasseau–Sénéor explicitly compute short-distance asymptotics from the construction — but $\phi^4_3$ is super-renormalisable; the divergences are finite-order, there is no AF, and the technique does not port. 4D YM is asymptotically free, not super-renormalisable; the infinite tower of UV divergences is absorbed into the running coupling, and intrinsic UV extraction must reproduce this.
  - **Structural risk (Fix 2 of Wave 0 Critic v2):** this sub-step is precisely where K-5 v3 strengthened bites. An Author who asymptotic-matches $S_2^{\mathrm{ren}}$ constructed non-perturbatively against $F^{\mathrm{pert}}(t)$ re-introduces Taylor-coefficient identification in disguise and lands inside the LOCK. The condition for staying outside: $C_N$ must emerge from constructional spectral / polymer data, not from external matching.
  - Verdict: **no candidate technique published or announced**, and the only available spectral-decay machinery (Hastings–Koma) gives the wrong observable.
- **Sub-step (c): $C_N = 2(N^2-1)/\pi^6$ derivation.**
  - Required: the specific coefficient $C_N$ appears as output of the construction, derived from a combinatorial / spectral / probabilistic quantity of the polymer algebra + Langevin generator + transfer-matrix spectrum.
  - State of research: none. $C_N$ is a perturbative quantity: it is the product of the gauge-group dimension $N^2-1$ (a representation-theoretic constant), the two-point function normalisation $1/\pi^6$ (a one-loop position-space integral), and a factor of 2 (combinatoric). Its perturbative origin is explicit. No non-perturbative derivation is known.
  - Verdict: **no viable programme exists.** The closest analogue is the large-$N$ master-loop equation (Chatterjee, Jafarov, Cao–Park–Sheffield), which gives Wilson-loop expectations in terms of string-length combinatorics — but only at large $N$ and only for Wilson loops, not for the local composite $[\mathrm{Tr}\,F^2]_R$ OPE.

### 6. Compound-bypass shape if the three sub-steps were closed

For the record, if all three sub-steps were available, the bypass chain would be:

1. **ERG↔QFT sub-step (a):** Balaban UV + Magnen–Rivasseau–Sénéor + (future) IR-cutoff removal → continuum $\mu_{\mathrm{YM}}$ with OS0–OS5.
2. **SPEC↔QFT (existing capacitor cell, ESTABLISHED):** transfer-matrix Hilbert space + Hamiltonian $H$ from OS Wightman reconstruction.
3. **ERG↔QFT sub-step (b):** intrinsic UV extraction via spectral/polymer technique (OPEN, no candidate).
4. **ERG↔QFT sub-step (c):** $C_N$ derivation from constructional quantities (OPEN, no candidate).
5. **Output:** $S_2^{\mathrm{ren}}(x,y) = C_N |x|^{-8}(\log 1/|x|\Lambda)^{-2}(1 + O((\log)^{-1}))$ with matching $C_N$.

Steps 3 and 4 are the load-bearing novelty. Nothing in the Nissim 2510.22788 machinery touches either.

---

## Cell-fill

Capacitor v1 format entry for ERG↔QFT:

### ERG ↔ QFT: Cluster-expansion + Langevin construction of lattice Yang–Mills at strong coupling (Shen–Zhu–Zhu / Nissim programme)

**Statement**: For every $G \in \{\mathrm{SU}(N), \mathrm{SO}(N), \mathrm{U}(N)\}$ with $N \geq 2$ and $d \geq 2$, there exists $\tilde\beta(d) > 0$ such that for all $\beta < \tilde\beta$, the lattice Yang–Mills theory on $\mathbb{Z}^d$ with $G$-valued link variables admits a unique infinite-volume Gibbs measure with strictly positive mass gap (exponentially decaying covariance of smooth local observables) and, for $G = \mathrm{U}(N)$, a large-$N$ Wilson-loop factorisation limit. Construction is via Langevin dynamics (whose stationary measure is the YM measure) combined with cluster expansion on the polymer representation. For $G \in \{\mathrm{SU}(N), \mathrm{SO}(N)\}$, the Langevin generator satisfies a Bakry–Émery Ricci lower bound; for $G = \mathrm{U}(N)$, the Ricci bound fails due to the $\mathrm{U}(1)$ centre, and the $\mathrm{U}(1) \times \mathrm{SU}(N)$ random-environment decomposition + cluster expansion on the $\mathrm{U}(1)$ marginal rescues the argument.

**Mechanism**: The Langevin dynamics drive any initial distribution to the YM Gibbs measure exponentially fast (verified via Log-Sobolev / Poincaré inequalities at small $\beta$), making the YM measure ergodic and characterised as the unique invariant measure. The cluster expansion on the polymer algebra provides convergence estimates (polymer activities decay exponentially in the polymer size at small $\beta$) and produces exponential covariance decay of local observables in the spatial lattice separation — the mass gap. The combination gives a non-perturbative construction of the infinite-volume lattice YM measure in the strong-coupling ('t Hooft small-$\beta$) regime. **No continuum limit is taken; no UV asymptotics are extracted; no OPE coefficients are computed.**

**Source**: Nissim, arXiv:2510.22788 (Oct 2025, U(N) case); Shen–Zhu–Zhu, Comm. Math. Phys. 2023 (arXiv BiBoS 23-06-620, SU(N)/SO(N) case); Shen–Zhu–Zhu, arXiv:2401.13299 (Jan 2024, YM–Higgs); Cao–Sheffield–Nissim, arXiv:2509.04688 (Sep 2025, area law). Historical antecedents: Osterwalder–Seiler, Ann. Phys. 110 (1978) 440–471 (original strong-coupling cluster-expansion mass-gap).

**Status**: **ESTABLISHED** for the cell as stated (strong-coupling lattice mass gap via cluster expansion + Langevin). **CONJECTURED-NEGATIVE for H4 bypass applicability** — see Load-bearing row below.

**Verification data**: none required; the cell records published peer-reviewed results (SZZ 2023 in CMP) and a preprint verified during Paper 8 v3 calibration (Nissim 2510.22788 abstract + theorem statements quoted verbatim in §1 of this node).

**Load-bearing for**:
- **H4 (Paper 8 Link 18) — CONJECTURED-NEGATIVE.** This cell does NOT provide a single-step bypass of H4. A compound bypass via this cell requires three separate open sub-steps — (a) continuum limit of the Nissim / SZZ construction (no published programme; the construction is intrinsically at fixed lattice spacing and strong coupling, the opposite end of the coupling line from where AF lives); (b) intrinsic UV extraction of short-distance asymptotics from constructional quantities (no candidate technique; Hastings–Koma spectral-decay produces the wrong observable — exponential long-distance decay governed by the gap, not polynomial short-distance singularity $|x|^{-8}$ governed by the beta function); (c) derivation of $C_N = 2(N^2-1)/\pi^6$ from constructional spectral / polymer data (no known mechanism; $C_N$ is intrinsically perturbative). The LOCK is not formally hit because the three sub-steps lie outside the Taylor-coefficient identification attack surface, but two of the three are open at the level of "no candidate programme has been published or announced."
- **Large-$N$ limit of SU(N) YM observables (framework-wide).** Nissim's dynamical proof of Wilson-loop factorisation gives an independent route to the large-$N$ limit; this is valuable for cross-verification with 't Hooft's perturbative large-$N$ result and with Makeenko–Migdal master-loop-equation approaches.
- **Area law at strong coupling (Paper 8 §confinement auxiliary).** Cao–Sheffield–Nissim 2509.04688 establishes area law via the dynamical approach, a useful independent check on the Wilson-confinement side of the YM package even if not directly load-bearing for H4.

**Transposition recipe**: If stuck on a lattice-gauge existence / uniqueness / mass-gap / ergodicity statement in the strong-coupling regime, use the Langevin + cluster-expansion construction as the non-perturbative existence proof, the Bakry–Émery / Log-Sobolev route (or its U(N) random-environment extension) for exponential ergodicity, and the polymer cluster expansion for covariance decay. **Do NOT transpose to the continuum, to short-distance asymptotics, or to OPE coefficient extraction — those lie outside the construction's reach.** For H4 specifically: this cell is a *negative transposition signal* — it tells the Author that the ERG↔QFT direction does not give H4 closure within the construction's scope, and any argument invoking "Nissim gives non-perturbative Schwinger functions therefore H4 follows" is either a category error (confusing lattice mass-gap for continuum short-distance asymptotics) or a K-5 trap (implicit perturbative matching at the point where $C_N$ must appear).

---

## Bypass assessment

**Verdict: CONJECTURED-NEGATIVE.**

The minimum bypass chain via ERG↔QFT is three open sub-steps. For each:

- **Sub-step (a) continuum limit.** **Separate open research programme, not in reach of Nissim's machinery.** The Nissim / SZZ programme is intrinsically strong-coupling (small $\beta$, 't Hooft-scaled as $\beta \leq c_d/N$). The continuum limit requires $\beta \to \infty$ along the AF line, which is the opposite regime. Balaban's block-spin RG controls the weak-coupling UV; Magnen–Rivasseau–Sénéor constructs weak-coupling Schwinger functions with unremoved IR cutoff. Neither programme meets the Nissim programme — there is no overlap or matching condition in the literature. Closing (a) would require: either extending Nissim-type Langevin-ergodicity to weak coupling (unlikely; Bakry–Émery already degrades going from SU(N) to U(N); it will not survive the $\beta \to \infty$ limit), or extending Balaban / Magnen–Rivasseau–Sénéor to IR-cutoff removal (the subject of three decades of stalled effort). A 3D-style Chevyrev–Shen regularity-structures construction for 4D is beyond current regularity-structures reach per Shen Feb/Mar 2025 IAS talks. **Status: 5–10 year open programme, no announced attack plan.**
- **Sub-step (b) intrinsic UV extraction.** **No candidate technique.** Hastings–Koma / Nachtergaele–Sims spectral-decay is the only general polymer-decay-from-spectral-gap technique, and it delivers exponential large-distance decay — the wrong observable for H4, which needs polynomial short-distance asymptotics governed by the AF beta function, not by the mass gap. Polymer-activity direct UV analysis in Balaban's expansion or Magnen–Rivasseau–Sénéor's expansion has not been pushed to extracting OPE coefficients; that direction has not been attempted in the literature. The only known non-perturbative route to short-distance asymptotics is via perturbative matching — which is exactly what K-5 v3 strengthened forbids. **Status: no candidate technique, not obvious where a technique would come from.**
- **Sub-step (c) $C_N$ derivation.** **No viable programme.** $C_N = 2(N^2-1)/\pi^6$ is a perturbative Feynman-diagram quantity: the $1/\pi^6$ factor is a one-loop position-space integral, $N^2-1$ is $\dim \mathfrak{su}(N)$, and the factor 2 is combinatorial. No non-perturbative constructional quantity has been proposed to produce this specific combination. The closest existing non-perturbative bridge is the large-$N$ master-loop equation (Chatterjee 2016; Park–Pfeffer–Sheffield; Jafarov 2016–2024; Cao–Park–Sheffield 2024), but it addresses Wilson loops, not local-composite two-point functions, and gives no short-distance structure at all. **Status: no programme, no candidate observable, no bridge.**

**Compound-bypass shape (if it existed):** would require at minimum four capacitor-cells — ERG↔QFT (this cell) + SPEC↔QFT (transfer matrix) + MICRO↔QFT (wave-front-set / OPE framework, W1-M slot) + a fourth bridge closing the $C_N$ derivation. Total: 4-cell compound bypass, with two of the three ERG-side sub-steps being open research programmes of decade-plus depth. **This is not a 2-year Clay-window-feasible bypass.**

**External unlocks that would change the verdict:**
- **A Nissim follow-up (12–36 months) extending the construction to $a \to 0$ along the AF line.** This would require substantial new machinery — either Bakry–Émery at weak coupling (not known to hold), or a lattice-to-continuum RG bridge that matches SZZ/Nissim at strong coupling to Balaban at weak coupling at an intermediate scale (no current proposal). Probability: low, but a formal announcement of *intent* in this direction would upgrade (a) from "separate open programme" to "actionable with named attacker." No such announcement is in the 2023–2026 literature.
- **A Hastings–Koma extension to massless long-range correlators with power-law decay of known exponent.** If some descendant of the Hastings–Koma technique could extract short-distance asymptotics (rather than long-distance decay), (b) would become actionable. No current proposal.
- **A constructional derivation of $C_N$ via representation theory + polymer algebra.** The most speculative unlock: if a polymer-algebra quantity could be identified whose short-distance asymptotic produced the specific constant $2(N^2-1)/\pi^6$, (c) would collapse. No current proposal, no obvious candidate.
- **A 4D analog of the Chevyrev–Shen regularity-structures programme.** Currently beyond the 3D reach of regularity structures per Shen's 2025 talks; would require new machinery (integration of singular SPDEs in supercritical dimension).

**Cross-check against BYPASS-PREDICTION §K:** the runner's §K alternative-2 Tier 1 shape listed ERG↔QFT as *"possibly the non-perturbative object"* at Step 3 of a 3-step bypass — but that prediction assumed the continuum limit would be treated as inherited from SZZ/Nissim. This node's finding refutes that assumption: Nissim is lattice-only and the continuum limit is itself the hardest open sub-step. The BYPASS-PREDICTION is miscalibrated for the ERG↔QFT route; the compound bypass (if it existed) would need to absorb the continuum limit as its own load-bearing sub-step, not inherit it.

---

## Self-suspicion (Step 5.5 — three failure modes, ≥1 backward-verification)

The mandated self-check is against the three K-5-adjacent failure modes specified in the task prompt.

### Failure mode 1: "You claimed Nissim gives continuum limit when he only gives mass gap"

**Backward verification by verbatim quote.** The Nissim paper Theorem 1.1 (verbatim, §1 introduction):

> *"Theorem 1.1 (Mass gap and infinite volume limit). Let d ≥ 2, N ≥ 2. Then for some fixed β̃ = β̃(d), and all β < β̃, there exists a probability measure $\mu_{U(N),\beta}$ on $U(N)^{E_{\Lambda_\infty}}$ (with $\Lambda_\infty = \mathbb{Z}^d$ ...) such that $\mu_{U(N),\Lambda_L,\beta} \to \mu_{U(N),\beta}$ weakly as L → ∞."*

The object $U(N)^{E_{\Lambda_\infty}}$ is link variables on $\mathbb{Z}^d$ — a lattice. The limit $L \to \infty$ is infinite volume at fixed lattice spacing, not continuum. Nissim's abstract lists three achievements: "a mass gap, ... a unique infinite volume limit, and ... a new proof of the large N limit." The continuum limit is not among them. Nissim's introduction §1 explicitly identifies the "existing results" in this lineage as requiring small-$\beta$ strong coupling: *"the existing results always involve a strong coupling (small β) assumption."*

My node's characterisation (Cell-fill §Status, Bypass assessment §Sub-step (a)): *"No continuum limit; construction intrinsically at fixed lattice spacing and strong coupling, the opposite end of the coupling line from where AF lives."* **Consistent with verbatim Nissim.** No overclaim.

### Failure mode 2: "Your 'intrinsic UV extraction' is actually pert-matching in disguise (LOCK-adjacent)"

The K-5 v3 strengthened operational gating condition (from `critiques/wave0-lock-anatomy-critic-v2.md` §Fix 2):
- INSIDE the LOCK: asymptotic-matching the constructed Schwinger function against $F^{\mathrm{pert}}(t)$ to extract UV behavior.
- OUTSIDE the LOCK: UV singular structure computed intrinsically from constructional quantities (polymer activities, Langevin stationary measure, transfer-matrix spectrum), with $C_N$ produced directly.

My cell-fill proposes (candidate technique, §4 Research): Hastings–Koma-style spectral gap + polymer-decay arguments extracting $|x|^{-8}$ scaling from the construction itself. **I then note in the same §4 that this candidate fails structurally** — Hastings–Koma delivers exponential *large*-distance decay governed by the gap, not polynomial *short*-distance singularity $|x|^{-8}$ governed by the beta function. The H4 observable is wrong-observable for Hastings–Koma.

My Bypass assessment §(b) verdict: *"No candidate technique. ... the only known non-perturbative route to short-distance asymptotics is via perturbative matching — which is exactly what K-5 v3 strengthened forbids."* **This explicitly flags that any currently-known route to UV asymptotics from construction falls into the K-5 trap — there is no LOCK-free mechanism available.** No claimed bypass is actually proposed; the verdict is CONJECTURED-NEGATIVE precisely because every candidate technique either (a) gives the wrong observable (Hastings–Koma) or (b) is perturbative matching in disguise (K-5). **No overclaim of a non-LOCK route.**

### Failure mode 3: "You cite Nissim / Balaban for a claim they don't actually make — verify by verbatim quote"

Backward verification in two places.

**Nissim claim cited:** mass gap + infinite volume + large N for U(N) lattice YM at strong coupling. **Verbatim from Nissim abstract:** *"We establish a mass gap, prove the existence of a unique infinite volume limit, and give a new proof of the large N limit for U(N) lattice Yang–Mills theory in the 't Hooft regime."* **Consistent.**

**Balaban claim cited:** block-spin RG construction, UV stability along AF line, weak-coupling regime. **Verbatim from the Balaban corpus (CMP 109 (1987) abstract, as reported in the published record):** *"This program defines a sequence of block-spin transformations for the pure Yang–Mills theory in a finite volume on the lattice ... and shows that, as the lattice spacing tends to 0 and these transformations are iterated many times, the resulting effective action on the unit lattice remains bounded."* And (CMP 122 (1989) Large Field Renormalization I+II + as summarized in the Yang–Mills for Probabilists review, Chatterjee 2018 arXiv:1803.01950): the RG flow is controlled for weak coupling, matching AF's running coupling asymptotics. My citation: Balaban's programme produces UV stability + effective-action control but does not produce OS-positive continuum Schwinger functions with OPE structure at coincident points. **Consistent with what Balaban proves and stops short of.**

**Magnen–Rivasseau–Sénéor claim cited:** construction of YM₄ Schwinger functions with IR cutoff, UV cutoff removed, axial gauge. **Verbatim (from the CMP 155 (1993) 325 review / introduction):** *"The paper provides the basis for a rigorous construction of the Schwinger functions of the pure SU(2) Yang–Mills field theory in four dimensions (in the trivial topological sector) with a fixed infrared cutoff but no ultraviolet cutoff, in a regularized axial gauge."* **Consistent.**

**Hastings–Koma claim cited:** nonvanishing spectral gap ⟹ exponential clustering of ground-state correlations. **Verbatim (from CMP 265 (2006) 781–804 / arXiv:math-ph/0507008):** *"if two observables anticommute with each other at large distance, then the nonvanishing spectral gap implies exponential decay of the corresponding correlation. When two observables commute with each other at large distance, the connected correlation function decays exponentially under the gap assumption."* **Consistent.** Note: Hastings–Koma is a lattice-quantum-spin result; porting it to continuum 4D YM requires the continuum limit — an additional sub-step (a) load.

**No overclaim in any cited result.** Each claim is backed by verbatim quoted text from the primary literature or its review.

---

## External unlocks

Named external developments that would change the Bypass assessment verdict from CONJECTURED-NEGATIVE toward PARTIAL or VIABLE. Each is a concrete, currently unpublished advance; a 12–36 month horizon is named where plausible.

1. **A Nissim–SZZ follow-up extending construction to weak coupling ($\beta \to \infty$).** An announcement of a programme to bridge SZZ strong-coupling to Balaban weak-coupling by RG matching at an intermediate coupling scale would upgrade sub-step (a) from "no announced attack plan" to "actionable." Probability of materialising in 12–36 months: low. No current announcement in the 2023–2026 literature.
2. **A 4D extension of Chevyrev–Shen regularity-structures 3D YM Inventiones 2024 paper.** Shen's Feb/Mar 2025 IAS talks explicitly state 4D is beyond current regularity-structures reach. An advance in supercritical regularity structures (Hairer's programme) would be the enabling discovery. Probability: very low in 12–36 months; depends on a general-theory breakthrough.
3. **A non-perturbative OPE coefficient derivation via large-$N$ master-loop-equation extension to local composites.** Current master-loop equations (Chatterjee; Jafarov; Cao–Park–Sheffield 2024) give Wilson-loop expectations in terms of string-length combinatorics. Extending to $\langle [\mathrm{Tr}\,F^2]_R(x) [\mathrm{Tr}\,F^2]_R(y) \rangle$ and extracting short-distance asymptotics would address sub-step (c) at large $N$. Probability: plausible in 12–24 months at least for the loop-equation side; the leap to coincident-point asymptotics is the harder step.
4. **A constructional identification of $C_N$ via a representation-theoretic + polymer-algebra quantity.** Speculative: if $N^2-1 = \dim \mathfrak{su}(N)$ can be identified as the spectral multiplicity of a polymer observable, and $1/\pi^6$ as a polymer integral, $C_N$ might emerge constructionally. No current proposal; no obvious candidate observable.
5. **Hastings–Koma-style polynomial-decay extension.** The Hastings–Koma technique requires a gap; at the continuum level, the gluon-pair channel has no gap (the AF correction is polynomial $(\log)^{-2}$, not exponential). An extension of Hastings–Koma to massless channels with power-law decay of prescribed exponent would address sub-step (b). No current proposal.

**Combined probability of compound-bypass materialising in the Paper 8 Clay 2-year window: <2%.**

The ERG↔QFT direction's primary value for the Millennium deliverable is as a **negative signal** — knowing that this route is blocked by three separate open sub-steps, each requiring its own decade-plus programme, sharpens the boundary of what a 2-year-window Paper 8 can reach. The capacitor entry serves future runners (this run, RH/BSD/PvNP adjacent future runs) by naming the obstruction precisely.

---

## Next-runner

The next runner (Wave 2 or successor) should:

1. **Treat this cell as ESTABLISHED for its stated scope** (strong-coupling lattice mass gap via Langevin + cluster expansion) and **CONJECTURED-NEGATIVE for H4 bypass applicability** per the three sub-step analysis. Do not re-open the ERG↔QFT direction for H4 closure within the current Clay window unless one of the five External unlocks above materialises.

2. **Do not dispatch a Wave 2 proof Author on this cell for H4** — the sub-steps (a) and (b) and (c) each exceed Wave 2's scope (each is a multi-year external research programme, not a multi-hour agent dispatch). The cell-fill is the durable Millennium deliverable for this slot.

3. **Pin this cell in future toolkit-scans** — the next time a proof chain in any paper (RH, BSD, PvNP, future papers) encounters a stuck link requiring lattice-gauge existence / mass-gap / ergodicity in strong coupling, this cell is the transposition resource. For weak-coupling or continuum-limit-needing questions, this cell is the explicit "NOT a resource" warning.

4. **Coordinate with Wave 2 MICRO↔QFT (W1-M) synthesis.** The category-shift compound-bypass §K alternative-1 shape listed ERG↔QFT at Step 3 as "the non-perturbative object" for the MICRO-framework's input. This node's finding refutes that composition — Nissim does not provide a continuum non-perturbative object, only a lattice one. The MICRO↔QFT Author (W1-M) needs to know that the ERG↔QFT Schwinger-distribution existence input is NOT inherited from Nissim and must either come from an independent construction (Balaban + IR-removal) or be assumed as a framework-level axiom. This is a coordination signal: synthesis of W1-M + W1-E should flag that the compound-bypass shape has a gap at Step 3 that neither author can close alone.

5. **Propagate to BLACKBOARD.md §F a mildly-updated K-5 v3 note** — add a one-line cross-reference from K-5 to this node, confirming that the W1-E investigation corroborates the K-5 v3 strengthening rather than softening it. The three sub-steps are not merely "three open steps" but "three sub-steps each requiring its own decade-scale programme, with no announced attack plans." K-5 stands.

6. **Voice canon compliance.** The ERG↔QFT direction falls into the §J canon: *"H4 stood this attack. The capacitor gained 1 cell; the wall stayed named."* This node does not constitute a bypass; it documents the wall's shape precisely on the ERG↔QFT face.

---

## Metadata

**Agent slot:** W1-E (ERG↔QFT, Priority 2).
**Mode:** capacitor-first cell-fill + bypass assessment.
**Verdict:** **CONJECTURED-NEGATIVE** (three open sub-steps, each a decade-scale programme).
**Cell status:** filled (Statement / Mechanism / Source ESTABLISHED for stated scope; H4 Load-bearing line is CONJECTURED-NEGATIVE).
**Contribution to capacitor fill rate:** +1 cell (ERG↔QFT, previously listed only in §Priority to fill).
**Self-suspicion pass:** 3/3 failure modes checked; 4/4 primary citations backward-verified by verbatim quote (Nissim, Balaban, Magnen–Rivasseau–Sénéor, Hastings–Koma).
**Voice:** §J canon; "the wall stayed named" register.

*W1-E — 2026-04-13. G Six and Claude Opus 4.6.*
