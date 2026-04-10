# Tier 3D (G4d): Operator Product Expansion — Draft Outline and Gap Analysis

**Status:** Draft outline. This file does **not** solve Gap G4(d); it is a staged plan toward a Clay-submission-ready statement, with honest identification of which steps are rigorous, which are conjectural, and which are open. A rigorous, non-perturbative OPE for 4D non-Abelian Yang–Mills is a known open problem in mathematical physics, comparable in difficulty to the construction of the theory itself.

**Scope constraint.** The preprint is *not* edited by this file. "The preprint" refers to `/Users/gsix/yang-mills/preprint/` as of the current run.

**Sister documents.** `G4a-renormalized-composite-operators.md` (supplies $Z_O(a)$ and the renormalized Schwinger function $S_2^{\mathrm{ren}}$); `G4b-af-short-distance-match.md` (supplies the conjectural short-distance form $S_2^{\mathrm{ren}} \sim C_N|x|^{-8}(\ln 1/|x|\Lambda)^{-2}$); `../tier-2-fixes/F1-coincident-point-singularities.md` (Källén–Lehmann derivation of the coincident-point bound *without* an OPE).

---

## Section 1 — The gap, precisely

The Jaffe–Witten (J–W) problem statement (Clay, §4) demands:

> "*… including … the existence of a stress tensor and an **operator product expansion**, having prescribed local singularities predicted by asymptotic freedom.*"

This asks for an OPE *as a structural piece of the Wightman theory*, not merely a bound on Schwinger functions at coincident points.

**What is in the preprint.** §5.7(f) "Coincident-point singularities" (lines ~2313–2361 of `preprint/sections/05-continuum-limit.md`), inside its Local Integrability lemma, asserts:

> "*… for gauge-invariant operators in a massive theory, the OPE gives $|S_n| \leq C^n n! \prod_{i=1}^{n-1}|x_i - x_{i+1}|^{-2}$ (with only $n-1$ singular factors from the tree-level structure).*"

This *asserts* an OPE but the preprint never constructs one. (Its $|x|^{-2}$ exponent is also the *free*-scalar power, not the AF-corrected $|x|^{-8}(\log)^{-2}$ expected for $\mathrm{Tr}\,F^2$; that separate error belongs to G4(a)/(b). The core issue for G4(d) is the absence of any constructed OPE.)

**Closure status after Tier 2 F1.** F1 removes the OPE appeal from §5.7(f) by deriving the coincident-point *bound* directly from the Källén–Lehmann representation, the linked-cluster theorem, and Glimm–Jaffe tree-edge spectral estimates. That closes the *bound* — hence OS0' local integrability and OS-axiom verification — *without* any OPE. But F1 does not provide an OPE *structure*: an asymptotic decomposition $\mathcal{O}_1(x)\mathcal{O}_2(y) \sim \sum_k C^k_{12}(x-y)\mathcal{O}_k(\tfrac{x+y}{2})$.

**G4(d) therefore remains open** even after F1. F1 removes the logical *dependence* of the preprint's OS-axiom verification on an OPE; it does not remove J–W's structural demand that the theory *possess* an OPE with AF-prescribed short-distance singularities.

---

## Section 2 — What an OPE actually is

For two gauge-invariant local operators $\mathcal{O}_1, \mathcal{O}_2$ of scaling dimensions $d_1, d_2$ at points $x, y$ with $|x-y| \to 0$, the Wilson OPE asserts:

$$\mathcal{O}_1(x)\,\mathcal{O}_2(y) \;\sim\; \sum_{k}\; C^{k}_{12}(x-y)\;\mathcal{O}_k\!\Bigl(\tfrac{x+y}{2}\Bigr). \tag{1}$$

Structural content: (i) $\{\mathcal{O}_k\}$ is a complete basis of local composites ordered by scaling dimension; in pure 4D YM, gauge-invariant polynomials in $F_{\mu\nu}$ and covariant derivatives modulo EOMs (Kluberg-Stern–Zuber). (ii) $C^k_{12}(x-y)$ are *c-number* tempered distributions, smooth away from $x=y$. (iii) At leading order $C^k_{12}(x-y) \sim |x-y|^{d_k - d_1 - d_2}$ modulo logs controlled by anomalous dimensions; channels with $d_k > d_1 + d_2$ are sub-leading. (iv) (1) is *asymptotic* as $|x-y| \to 0$, not a global identity; the infinite sum need not converge.

**Rigorous distributional form** (Wilson–Zimmermann 1972; Hollands 2007): let $X$ be a product of renormalized operators at points in a compact set $K$ disjoint from $\{x,y\}$. For every $\Delta > d_1 + d_2$, there exists $\eta > 0$ with

$$\bigl\langle \mathcal{O}_1(x)\,\mathcal{O}_2(y)\,X\bigr\rangle \;=\; \sum_{k: d_k \leq \Delta} C^{k}_{12}(x-y)\,\bigl\langle \mathcal{O}_k\!\bigl(\tfrac{x+y}{2}\bigr)\,X\bigr\rangle \;+\; R_\Delta(x,y;X), \tag{2}$$

with $|R_\Delta(x,y;X)| \leq C(K,X)\,|x-y|^{\Delta - d_1 - d_2 + \eta}$.

---

## Section 3 — Status of OPE for various theories

| Theory | OPE status | Rigor |
|---|---|---|
| Free fields, Minkowski & curved spacetime | Wick products via locality + covariance (Hollands–Wald, CMP 223 (2001), CMP 231 (2002); Brunetti–Fredenhagen–Verch, CMP 237 (2003)) | rigorous |
| Perturbative interacting QFT, Minkowski | Wilson–Zimmermann CMP 24 (1972); Zimmermann "Normal products" (1973) | rigorous perturbatively |
| Perturbative QFT, curved spacetime | Hollands CMP 273 (2007); Hollands–Wald CMP 293 (2010) | rigorous perturbatively |
| Perturbative $\phi^4_4$, convergence of the OPE | Hollands–Kopper CMP 313 (2012); Holland–Kopper–Tanase, later | rigorous perturbatively |
| $\phi^4_3$ (super-renorm.), Bostelmann–Fewster | CMP 292 (2009) | rigorous |
| Model-independent, phase-space approach | Bostelmann, JMP 46 (2005) 082304 (arXiv:math-ph/0502004) | rigorous conditional on phase-space nuclearity |
| QCD physics (SVZ sum rules) | Shifman–Vainshtein–Zakharov Nucl. Phys. B147 (1979) 385, 448 | *physical hypothesis*, not a theorem |
| 4D non-Abelian Yang–Mills, non-perturbative | — | **OPEN** |

**Key observations.** (1) Hollands–Wald (2001–2010) builds perturbative OPEs for free and interacting theories on curved spacetimes, uniquely up to finitely many curvature counterterms, but has no non-Abelian gauge extension in 4D. (2) Bostelmann (2005, 2009) derives an OPE from a phase-space nuclearity axiom — which presumes the QFT already exists in a form satisfying that axiom, exactly what is missing for 4D YM. (3) SVZ sum rules *assume* an OPE for QCD with perturbatively computed Wilson coefficients and non-perturbative "condensates" as matrix elements; phenomenological success is strong but not a theorem. (4) For 4D non-Abelian YM specifically, no rigorous OPE — perturbative or not — has been constructed. The obstructions are (a) no positive-metric Wightman reconstruction for $A_\mu^a$, (b) no non-perturbative composite operators (Gap G4(a)), (c) no phase-space condition proved.

---

## Section 4 — A staged construction sketch

Conditional on Tier 3A (renormalized composites exist) and Tier 3B (AF short-distance matching hypothesis H4 of `G4b`). Neither is rigorously established; both are, at present, conjectures.

### Step 4a — Local operator basis

Gauge-invariant scalar local operators in pure 4D YM up to dim 8, modulo EOM and $\mathcal{C}$-parity:

| dim | operator(s) | notes |
|---|---|---|
| 0 | $\mathbb{1}$ | identity |
| 4 | $[\mathrm{Tr}\,F_{\mu\nu}F^{\mu\nu}]_R$ | trace-anomaly; $\gamma_O = -2\beta/g$ exact (Spiridonov 1984) |
| 4 | $[\mathrm{Tr}\,F_{\mu\nu}\tilde F^{\mu\nu}]_R$ | $\mathcal{C}$-odd; does not mix into the $F^2$ channel |
| 6 | $[\mathrm{Tr}(D_\rho F_{\mu\nu})^2]_R$ | EOM-independent |
| 6 | $[\mathrm{Tr}(F_\mu{}^\nu F_\nu{}^\rho F_\rho{}^\mu)]_R$ | eliminated by $\mathcal{C}$ in pure YM |
| 8 | $[\mathrm{Tr}(F^2)^2]_R$, $[\mathrm{Tr}(F^4)]_R$, double-trace (mixing) | tower begins |

The stress tensor $[T_{\mu\nu}]_R$ (dim 4, spin-2) also appears on the RHS of the $\mathcal{O}\cdot\mathcal{O}$ OPE and is tied to Tier 3C.

### Step 4b — Perturbative leading coefficients

For $\mathcal{O}(x) := [\mathrm{Tr}\,F_{\mu\nu}F^{\mu\nu}]_R(x)$,

$$\mathcal{O}(x)\,\mathcal{O}(0) \;\sim\; C^{\mathbb{1}}(x)\,\mathbb{1} \;+\; C^{\mathcal{O}}(x)\,\mathcal{O}(0) \;+\; \sum_{k\geq 6} C^k(x)\,\mathcal{O}_k(0). \tag{3}$$

Leading coefficients, absorbing anomalous-dimension logs (see `G4b` §2 and SVZ 1979; Novikov–Shifman–Vainshtein–Zakharov Nucl. Phys. B249 (1985) 445; Zoller–Chetyrkin JHEP 12 (2012) 119 and JHEP 10 (2014) 169):

- **Identity:** $C^{\mathbb{1}}(x) \sim \dfrac{C_N}{|x|^{8}}\Bigl(\ln\tfrac{1}{|x|\Lambda}\Bigr)^{-2}[1 + O((\ln)^{-1})]$, $C_N = 2(N^2-1)/\pi^6$. This is precisely `G4b` §2's conjectural AF matching form, evaluated on the vacuum.

- **$\mathcal{O}$ channel:** $C^{\mathcal{O}}(x) \sim A\,|x|^{-4}\,(\ln)^{c}$ (power $d_\mathcal{O} - 2 d_\mathcal{O} = -4$); constant $A$ appears as the coupling to the gluon condensate in SVZ phenomenology.

- **Dim-6 channel:** $C^{6}(x) \sim B\,|x|^{-2}$; dim-8 and higher regular as $|x| \to 0$.

Explicit values are computed to three loops in $\overline{\mathrm{MS}}$ (Zoller–Chetyrkin 2012, 2014). These are *perturbative* inputs; the non-perturbative coefficients are conjectured to agree at leading order in $\alpha_s(1/|x|)$ (Hypothesis H4 of `G4b`).

### Step 4c — Distributional OPE statement

**Conjecture (OPE for 4D YM).** *There exist c-number tempered distributions $\{C^{k}(x-y)\}$, labelled by a dimension-ordered basis $\{\mathcal{O}_k\}$, Euclidean-invariant and scale-covariant with the AF-corrected anomalous dimensions, such that for every $\Delta > d_1 + d_2$ equation (2) holds with $\eta > 0$, and the $C^k$ agree at leading order in $\alpha_s(1/|x-y|)$ with the perturbative coefficients of Step 4b.* This is the rigorous form for 4D YM. It is **open**.

### Step 4d — Matching perturbative and non-perturbative coefficients

Stating that the non-perturbative $C^k$ equal their perturbative values at leading order is precisely Hypothesis H4 of `G4b`, lifted from the identity channel to all channels. It is the content underlying every SVZ / Wilson-coefficient / short-distance factorization computation in QCD. For 4D non-Abelian YM it is not a theorem.

---

## Section 5 — Rigor vs. conjecture vs. open

| Step | Status | Justification |
|---|---|---|
| 4a (local operator basis) | **[OK]** conditional on Tier 3A | Kluberg-Stern–Zuber EOM quotient and $\mathcal{C}$-elimination; rigorous within perturbation theory. Non-perturbative existence of basis elements is Tier 3A. |
| 4b (perturbative coefficients) | **[OK]** perturbatively | Identity channel from `G4b` §2; higher channels from SVZ 1979 and Zoller–Chetyrkin 2012/2014. Rigorous to three loops. |
| 4c (non-perturbative OPE statement) | **[OPEN]** | Non-perturbative OPE for 4D non-Abelian YM. Not constructed by any existing framework. |
| 4d (non-pert = pert at leading order) | **[OPEN / CONJECTURE]** | Standard SVZ hypothesis; ubiquitous in lattice QCD; not a theorem for 4D YM. |

**Honest summary.** 4a and 4b are rigorous (4a conditional on Tier 3A, 4b perturbatively from existing literature). 4c and 4d are the *real* open problems and comprise the bulk of what Clay asks in G4(d). An outline can state them as explicit conjectures with concrete perturbative input; it cannot prove them.

---

## Section 6 — A weaker "leading-order OPE" deliverable

Restrict to the identity channel at leading order:

**Leading-order OPE conjecture.** *Let $\mathcal{O}(x) = [\mathrm{Tr}\,F_{\mu\nu}F^{\mu\nu}]_R(x)$. As $|x-y| \to 0$,*
$$S_2^{\mathrm{ren}}(x,y) \;=\; \bigl\langle \mathcal{O}(x)\,\mathcal{O}(y)\bigr\rangle \;=\; C^{\mathbb{1}}(x-y) \;+\; O\bigl(|x-y|^{-4}\bigr), \tag{4}$$
*with the identity-channel coefficient given by*
$$C^{\mathbb{1}}(x-y) \;=\; \frac{C_N}{|x-y|^{8}}\Bigl(\ln\tfrac{1}{|x-y|\Lambda}\Bigr)^{-2}\,[1 + O((\ln)^{-1})], \qquad C_N = \frac{2(N^2-1)}{\pi^6}. \tag{5}$$

(4)–(5) is exactly the conjectural AF matching of `G4b`, reinterpreted as the leading (identity) term of the OPE. Sub-leading remainder $O(|x-y|^{-4})$ corresponds to the $\mathcal{O}$-channel; further channels are regular or weakly logarithmic.

**Does (4)–(5) satisfy "prescribed local singularities predicted by AF"?** Charitable reading (yes): the *leading* short-distance singularity is $|x|^{-8}(\ln)^{-2}$, matching the AF prediction; higher channels are sub-leading corrections. Strict reading (no): J–W's "having prescribed local singularities" suggests the *full* channel decomposition with AF-corrected anomalous dimensions, which (4)–(5) does not deliver. The leading-order version is honest: it gives the *dominant* singularity and its AF log factor conjecturally; it avoids the full operator basis, the dim-$\geq 6$ mixing matrix, the non-perturbative identification of all coefficients.

**For a Clay submission this is the maximum the current state of the art supports.** Stating (4)–(5) as a conjecture consistent with one-loop perturbative QCD and the Kluberg-Stern–Zuber / SVZ framework is defensible scholarship.

---

## Section 7 — Connection to F1 (coincident-point bound)

The F1 fix addresses a narrower question. It proves that §5.7(f)'s bound
$$|S_n(x_1,\ldots,x_n)| \;\leq\; C^n\,n!\,\prod_{i<j}(1 + |x_i - x_j|^{-2})\,e^{-\Delta\,\mathrm{diam}} \tag{6}$$
can be derived from (i) Källén–Lehmann applied to each connected 2-pt function, (ii) the mass gap $\Delta > 0$, (iii) the linked-cluster theorem, (iv) Glimm–Jaffe Theorem 8.4.3 iterating the spectral bound along any spanning tree. No OPE is used. The $-2$ exponent is the free-scalar Bessel-function bound — pessimistic at short distances (true AF power is $-8$ with logs) but sufficient for OS0' local integrability.

**Closure map.**

| Item | Tier 2 F1 | Tier 3 G4(d) |
|---|---|---|
| Bound (6) | **proved** (KL + cluster, no OPE) | irrelevant |
| OS0' local integrability | **proved** | irrelevant |
| OS-axiom verification | **closed** | not needed |
| OPE as structure of the QFT | not addressed | **OPEN** |
| AF-corrected short-distance power | not addressed | **OPEN / CONJECTURE (via §6)** |
| J–W "OPE with AF singularities" structural clause | **not met** | target, met only via §6 leading-order conjecture |

**Key distinction.** F1 closes the preprint's *use* of an OPE for the coincident-point bound and OS-axiom verification. G4(d) closes the *structural requirement* that the theory possesses an OPE. These are logically independent: F1 is sufficient for the mass-gap proof but not for J–W §4; G4(d) would sharpen F1's bound to $|x|^{-8}(\log)^{-2}$ but is not required for OS-axiom verification.

After F1, §5.7(f) should be rewritten so that OS verification makes no reference to an OPE; a separate subsection may state the leading-order OPE conjecture (4)–(5) as the residual G4(d) obligation.

---

## Section 8 — Recommended next steps for the authors

- **(a) Cite SVZ / Zoller–Chetyrkin.** For perturbative $\mathrm{Tr}\,F^2$-channel Wilson coefficients: SVZ Nucl. Phys. B147 (1979) 385, 448; NSVZ Nucl. Phys. B249 (1985) 445; Pascual–de Rafael Z. Phys. C12 (1982) 127; Zoller–Chetyrkin JHEP 12 (2012) 119, JHEP 10 (2014) 169; Collins "Renormalization" (1984) Ch. 10. For rigorous OPE precedents: Wilson–Zimmermann CMP 24 (1972); Hollands CMP 273 (2007); Hollands–Wald CMP 293 (2010); Bostelmann JMP 46 (2005) 082304.

- **(b) State (4)–(5) as a conjecture in the preprint.** Add a subsection "Short-distance OPE (conjectural)" immediately after the F1-patched coincident-point discussion, stating (4)–(5) with explicit $C_N$ and log exponent, flagged as "conditional on the standard QCD OPE hypothesis and on Tier 3A composite-operator renormalization".

- **(c) Distinguish bound vs. OPE structure.** Label (6) as a Källén–Lehmann *upper bound* (per F1) and (4)–(5) as the *asymptotic* OPE leading term (per G4(d)). Remove the phrase "the OPE gives" from the §5.7(f) Local Integrability lemma — after F1 the lemma needs no OPE at all.

- **(d) Clay scope declaration.** Add a Scope section enumerating J–W §4 requirements and their post-closure status. For G4(d): either (i) restrict the Clay claim to "Schwinger functions of gauge-invariant composites with the correct short-distance *bound* but without a rigorously constructed non-perturbative OPE"; or (ii) acknowledge the non-perturbative OPE as the residual open structural problem, with (4)–(5) as the leading-order conjectural replacement. An honest Clay submission cannot claim the full OPE structural requirement is met; it can state the leading-order conjectural form and the rigorous bound-via-F1, and name the remainder as a known open problem.

---

## Honest assessment

The outline above gets **at most 10–15%** of the way to a Clay-eligible Tier 3D deliverable. A rigorous, non-perturbative OPE for 4D non-Abelian Yang–Mills is a known open problem comparable in difficulty to the construction of the theory itself. Neither Hollands–Wald's perturbative framework nor Bostelmann's phase-space one extends to the 4D gauge case, and the SVZ OPE underlying QCD phenomenology is a physical hypothesis, not a theorem. What *is* closable without new mathematics is (i) the coincident-point *bound* via F1 (Källén–Lehmann + linked cluster, no OPE) and (ii) a leading-order OPE *conjecture* (4)–(5) recovering the AF-predicted identity-channel singularity $|x|^{-8}(\ln)^{-2}$ with explicit constants from SVZ/Zoller–Chetyrkin. The leading-order conjecture satisfies the J–W "prescribed local singularities predicted by asymptotic freedom" clause only under a *charitable* reading — where the dominant short-distance singularity plus its AF log counts as "the" prescribed singularity. A strict reading requires the full channel decomposition, mixing matrices at dim $\geq 6$, and non-perturbative identification of all $C^k$, none achievable today. The honest Tier 3D deliverable for a Clay submission is therefore: (a) F1 for the bound; (b) the leading-order OPE conjecture (4)–(5) as the residual structural content; (c) citation of Hollands–Wald, Bostelmann, Wilson–Zimmermann, SVZ as precedents and as scope markers; (d) explicit acknowledgement that the full non-perturbative OPE for 4D non-Abelian YM remains open. This file is the roadmap for that deliverable.
