# Tier 3A (G4a): Renormalized Composite Operators — Draft Construction and Gap Analysis

**Status:** Draft outline. This file does **not** solve Gap G4(a) — it is a staged plan for a Clay-submission-ready construction, with honest identification of which steps are rigorous, which are conjectural, and which require genuinely new mathematics.

**Scope constraint:** The preprint is not edited by this file. All references to "the preprint" are to `/Users/gsix/yang-mills/preprint/` as of the current run.

---

## Section 1 — The gap, precisely

The Jaffe–Witten (J–W) problem statement (Clay Mathematical Institute, §4, verbatim):

> "one should define a quantum field theory ... with **local quantum field operators** in correspondence with the gauge-invariant local polynomials in the curvature $F$ and its covariant derivatives, such as $\mathrm{Tr}\,F_{ij}F_{kl}(x)$. Correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory."

What "local quantum field operator" means in the Wightman framework: an operator-valued distribution
$$\mathcal{O} : \mathcal{S}(\mathbb{R}^4) \longrightarrow \mathrm{Op}(\mathcal{H}), \qquad f \mapsto \mathcal{O}(f) = \int \mathcal{O}(x)\, f(x)\, d^4x,$$
defined on a common dense invariant domain $\mathcal{D} \subset \mathcal{H}$, Poincaré-covariant, local (bosonic operators at spacelike separation commute), and whose vacuum expectation values are the Wightman functions.

**What is currently in the preprint.** §5.7(f), "Remark (Field operators and completeness)" (lines 2566–2592), asserts that "the reconstructed Wightman theory has field operators that are gauge-invariant composite operators — the continuum limits of plaquette traces $\mathrm{Tr}(F_{\mu\nu}^2(x))$, higher Casimir operators $\mathrm{Tr}(F^n(x))$, Wilson loops $W_C$, and products thereof." What is *actually* constructed in the preprint is:

1. Lattice Schwinger functions $\langle s_P(x_1) \cdots s_P(x_n)\rangle_a$ with $s_P(x) = 1 - (1/N)\mathrm{Re}\,\mathrm{Tr}\,U_P(x)$ (bare plaquette).
2. Uniform-in-$a$ bounds (the K-uniformity fix notwithstanding).
3. A subsequential continuum limit $S_n$ yielding Osterwalder–Schrader data.
4. A GNS reconstruction to obtain $(\mathcal{H}, \Omega, H)$ with a mass gap.

**What is missing.** The operator $\mathrm{Tr}\,F_{\mu\nu}^2(x)$ as an operator-valued distribution on $\mathcal{H}$ *with the correct normalization*. The lattice plaquette $s_P$ has the naive continuum expansion $s_P(x) \simeq (a^4 g^2/(2N))\,\mathrm{Tr}\,F_{\mu\nu}^2(x) + O(a^6)$. The rescaled operator $(2N/(a^4 g^2))\,s_P(x)$ does *not* have a finite limit as $a \to 0$: its two-point function diverges. A multiplicative renormalization $Z_O(a) \to 0$ is needed, with $Z_O$ carrying the anomalous dimension of the composite operator. The preprint constructs Schwinger functions of *bare* lattice objects only; it never defines $Z_O(a)$ or establishes that $Z_O(a)^2 \langle s_P(x) s_P(y)\rangle_a$ converges to a finite distribution with the AF-predicted short-distance behavior.

**Concrete deficit.** The preprint's bound $|S_2(x,y)| \leq C |x-y|^{-2} e^{-\Delta |x-y|}$ uses a *free*-propagator power $-2$. The correct AF prediction for a dimension-4 gauge-invariant composite is $|x-y|^{-8}$ (with logs from the running coupling). The two powers are incompatible; the preprint is implicitly describing the free (Gaussian) short-distance limit, not the interacting YM limit, and this is precisely because no renormalization of the composite has been performed.

**Related, distinct gap (G1a, not addressed here).** Even for the fundamental Wightman field $A_\mu^a(x)$, a non-Abelian gauge theory in 4D has no rigorous Wightman reconstruction in a positive-metric Hilbert space. The preprint sidesteps this by working only with gauge-invariant composites — which is the right move — but then owes a construction of the composites themselves, which is G4(a).

---

## Section 2 — The classical Symanzik / Brandt / Lowenstein framework

Perturbative composite-operator renormalization is a well-developed subject:

- **Bare lattice operator.** $\mathcal{O}^{\mathrm{bare}}_a(x) := (2N/(a^4 g_0^2)) \hat{s}_P(x)$, where $\hat{s}_P(x)$ is the symmetrized (hypercubic-invariant) average of $s_P$ over the six plaquettes containing site $x$, or — equivalently at leading order — the clover-improved lattice field-strength squared.

- **Multiplicative renormalization.** $[\mathcal{O}]_R(x) := Z_O(a) \cdot \mathcal{O}^{\mathrm{bare}}_a(x)$, with $Z_O(a)$ chosen so that renormalized correlators $\langle [\mathcal{O}]_R(x_1) \cdots [\mathcal{O}]_R(x_n)\rangle$ have a finite continuum limit as $a \to 0$ for non-coincident points.

- **Anomalous dimension.** Differentiating $Z_O$ with respect to the RG scale gives the anomalous dimension $\gamma_O(g)$. For a multiplicatively renormalizable scalar composite of engineering dimension $d_O$ in an asymptotically free theory,
$$Z_O(a) \;=\; \exp\!\left[-\int_{g(\mu)}^{g(1/a)} \frac{\gamma_O(g')}{\beta(g')}\,dg'\right] \;\sim\; \bigl(\log(1/(a\Lambda))\bigr)^{-\gamma_O^{(0)}/(2 b_0)} \times (1 + O(1/\log)),$$
where $b_0 = 11 N/(48\pi^2)$ is the YM one-loop coefficient and $\gamma_O^{(0)}$ is the leading coefficient of $\gamma_O(g) = \gamma_O^{(0)}\,g^2 + O(g^4)$.

- **Operator mixing.** At dimension 4 in pure YM, gauge-invariant scalar operators form a short list: $\mathrm{Tr}\,F^2$, $\mathrm{Tr}\,F\tilde F$ (CP-odd, does not mix with $\mathrm{Tr}\,F^2$ by parity), and operators vanishing by the equations of motion (e.g., $\mathrm{Tr}(D_\mu F^{\mu\nu})^2$). The Kluberg-Stern–Zuber theorem (Phys. Rev. D 12 (1975) 467) states that equation-of-motion operators do not mix into physical operators under renormalization in linear covariant gauges, so $\mathrm{Tr}\,F^2$ is multiplicatively renormalizable in a BRST-closed sector — modulo mixing with BRST-exact terms that drop out of physical matrix elements. (The subtlety that $\mathrm{Tr}\,F^2$ mixes with *gauge-non-invariant* operators in intermediate steps but becomes gauge-invariant-multiplicatively-renormalizable in the BRST-cohomology sense is well documented; see e.g. Henneaux 1993.)

- **Key fact for $\mathrm{Tr}\,F^2$.** The renormalization-group invariant combination is $[\beta(g)/g^3]\,\mathrm{Tr}\,F^2$ (Spiridonov 1984; Spiridonov–Chetyrkin, Sov. J. Nucl. Phys. 47 (1988) 522). This implies the exact relation
$$\gamma_O(g) \;=\; -\,2\,\frac{\beta(g)}{g}\;=\;-\,2\,b_0\,g^2 \;+\; O(g^4),$$
equivalently $\gamma_O^{(0)} = -\,2\,b_0$. Substituting,
$$Z_O(a) \;\sim\; \bigl(\log(1/(a\Lambda))\bigr)^{+1}.$$
That is, $Z_O$ grows logarithmically rather than shrinks; the bare operator $\mathrm{Tr}\,F^2$ becomes *larger* than the renormalized one at small $a$. (This is the origin of the power-law suppression of the gluon condensate $\langle G^2\rangle$ vs. its naive lattice sum.)

**References used.** Brandt (1971, point-splitting); Zimmermann (1973, Normal Products); Lowenstein–Zimmermann (1976, BPHZ composites); Kluberg-Stern–Zuber, Phys. Rev. D 12 (1975) 467; Spiridonov (1984); Spiridonov–Chetyrkin, Sov. J. Nucl. Phys. 47 (1988) 522; Caracciolo–Curci–Menotti–Pelissetto, Ann. Phys. 197 (1990) 119; Caracciolo–Menotti–Pelissetto, Nucl. Phys. B 375 (1992) 195; Capitani, Phys. Rep. 382 (2003) 113 [hep-lat/0211036].

**Crucial caveat.** This entire framework is *perturbative*. The claim that "$Z_O(a)$ exists such that renormalized correlators converge as $a\to 0$" has never been proved non-perturbatively for 4D non-Abelian gauge theory. It is assumed in lattice QCD phenomenology, correct to all known orders of lattice perturbation theory, but not a theorem.

---

## Section 3 — Status of the program across theories

| Theory | Composite operator construction | Rigor |
|---|---|---|
| Free scalar/spinor/Maxwell, Minkowski | Wick polynomials via point-splitting | rigorous (standard) |
| Free fields on curved spacetimes | Hollands–Wald (CMP 223, 2001; CMP 231, 2002); Brunetti–Fredenhagen–Verch (CMP 237, 2003) — locally covariant construction | rigorous |
| $P(\phi)_2$, Yukawa${}_2$ | Glimm–Jaffe; Simon | rigorous |
| $\phi^4_3$ (super-renormalizable) | Glimm–Jaffe–Spencer; Feldman–Osterwalder; Magnen–Sénéor | rigorous, including composites |
| 2D gauge theories (Yang–Mills${}_2$, Schwinger model, $QED_2$) | Driver, Sengupta, Fine, Gross | rigorous |
| $\phi^4_4$ | trivial in infinite volume (Aizenman; Fröhlich; Aizenman–Duminil-Copin 2021); interacting limit does not exist as a Wightman QFT | **open negatively** |
| 4D non-Abelian Yang–Mills | no rigorous construction of renormalized $[\mathrm{Tr}\,F^2]_R$; no rigorous non-perturbative OPE | **OPEN** |

Architectural points:

1. **Free-field case.** Hollands–Wald (2001) showed that imposing locality + covariance + scaling + continuity in the metric uniquely fixes Wick polynomials up to finitely many renormalization parameters, using the algebraic QFT framework of Brunetti–Fredenhagen–Verch (2003). This is the rigorous composite-operator template, but it is *linear* — free fields — and its extension to interacting theories passes through formal perturbation theory (Hollands–Wald 2003, 2005).

2. **Super-renormalizable case.** In $\phi^4_3$, the coupling has positive mass dimension and only finitely many diagrams diverge, so composites are built via lattice regularization + explicit counterterms (Glimm–Jaffe $:\!\phi^2\!:$, $:\!\phi^4\!:$, stress tensor). 4D YM is marginal, not super-renormalizable; this is what makes the composite problem hard.

3. **4D YM status.** Balaban (1984–1989), Magnen–Rivasseau–Sénéor (1993), Federbush (1987–1990) constructed the lattice continuum limit of pure YM in finite volume via block-spin RG, but none built renormalized composite operators as distributions. Whether $[\mathrm{Tr}\,F^2]_R$ exists non-perturbatively is recognized as open; see Hollands–Wald review, CMP 293 (2010) §5.

**The present preprint, even granted the K-uniformity fix, does not solve this problem.** It constructs Schwinger functions of *bare* lattice operators and reconstructs a Hilbert space from them. The resulting "operators" corresponding to plaquette traces are fine as elements of the abstract GNS algebra, but they are not normalized to the AF-predicted short-distance behavior; they are not "renormalized $\mathrm{Tr}\,F^2$" in the Jaffe–Witten sense.

---

## Section 4 — A staged construction sketch

The following is a draft of what a Clay-eligible Tier 3A construction would look like. It is *conditional* on the preprint's continuum-limit Schwinger functions existing (Tier 0 + Tier 1), and it does *not* claim to be a complete proof. Each step is tagged in Section 5.

**Step 4a. Bare lattice operator.** Define
$$\mathcal{O}^{\mathrm{bare}}_a(x) \;:=\; \frac{2N}{a^4\,g_0^2}\;\hat{s}_P(x), \qquad \hat{s}_P(x) := \frac{1}{6}\sum_{\mu<\nu}\bigl(1 - \tfrac{1}{N}\,\mathrm{Re}\,\mathrm{Tr}\,U_{P_{\mu\nu}}(x)\bigr),$$
averaged over the six oriented plaquettes at $x$ so that $\hat{s}_P$ is a scalar under the hypercubic group. The naive classical continuum limit is $\hat{s}_P(x) = (a^4 g_0^2/(4N))\,\mathrm{Tr}\,F_{\mu\nu}^a F^{a\mu\nu}(x) + O(a^6)$, so $\mathcal{O}^{\mathrm{bare}}_a(x) \to \tfrac12 \mathrm{Tr}\,F^2(x)$ classically. (Exact numerical coefficient is standard; we will not litigate it here.)

**Step 4b. Anomalous dimension.** Use the Spiridonov/Kluberg-Stern–Zuber result: since the trace anomaly
$$\Theta_\mu^\mu \;=\; \frac{\beta(g)}{2 g}\,\mathrm{Tr}\,F_{\mu\nu}^2 \qquad (\text{plus mass terms in QCD, absent in pure YM})$$
is renormalization-group invariant, the composite $\mathrm{Tr}\,F^2$ has exact anomalous dimension $\gamma_O(g) = -2 \beta(g)/g = -2 b_0 g^2 + O(g^4)$, with $b_0 = 11 N/(48\pi^2)$. In particular $\gamma_O^{(0)}/(2 b_0) = -1$.

**Step 4c. Renormalization constant.** Set
$$Z_O(a) \;:=\; \exp\!\left[-\int_{g(\mu_0)}^{g(1/a)} \frac{\gamma_O(g')}{\beta(g')}\,dg'\right].$$
To leading log and with $\gamma_O = -2\beta/g$, this gives exactly
$$Z_O(a) \;=\; \frac{g(1/a)^2}{g(\mu_0)^2} \;\sim\; \frac{1}{b_0\,g(\mu_0)^2 \cdot \log(1/(a\Lambda))} \qquad (a \to 0),$$
i.e. $Z_O(a) \to 0$ logarithmically. The renormalized operator is $[\mathrm{Tr}\,F^2]_R(x) := Z_O(a) \cdot \mathcal{O}^{\mathrm{bare}}_a(x)$. This is a perturbative prescription made non-perturbative by the running-coupling convention of Step 4c; the question is whether the non-perturbative $Z_O$ so defined in fact yields finite renormalized Schwinger functions.

**Step 4d. Renormalized two-point Schwinger function.** Define, for $x \neq y$,
$$S_2^{\mathrm{ren}}(x,y) \;:=\; \lim_{a\to 0}\; Z_O(a)^2\;\bigl\langle \mathcal{O}^{\mathrm{bare}}_a(x)\,\mathcal{O}^{\mathrm{bare}}_a(y)\bigr\rangle_a.$$
**Claim (Symanzik, conjectural).** The limit exists, is a tempered distribution on $\{(x,y) : x \neq y\}$, extends to a Schwartz distribution on $\mathbb{R}^4 \times \mathbb{R}^4$, and has short-distance asymptotics
$$S_2^{\mathrm{ren}}(x,y) \;\sim\; \frac{A}{|x-y|^8}\,\bigl(\log(1/(\Lambda|x-y|))\bigr)^{+2}\,(1 + O(1/\log)) \qquad (|x-y| \to 0),$$
matching the one-loop perturbative QCD prediction with the AF running coupling. The logarithmic *increase* (exponent $+2$, not $-2$) is exactly the $(g^2)^{-2}$ from $Z_O^2$ combined with the bare $|x-y|^{-8}$.

**This is the key conjectural step.** It encodes the classical Symanzik composite-operator program for 4D non-Abelian YM. It is the main open problem for Tier 3A.

**Step 4e. Operator definition via Wightman reconstruction.** Once $S_2^{\mathrm{ren}}$ (and higher $S_n^{\mathrm{ren}}$) are constructed as OS-positive, Poincaré-invariant, cluster-decomposing Schwartz distributions, the Osterwalder–Schrader / Wightman reconstruction theorem applies to the Schwinger functions of the *renormalized* composite. This yields an operator-valued distribution
$$[\mathrm{Tr}\,F^2]_R(f) \;=\; \int f(x)\,[\mathrm{Tr}\,F^2]_R(x)\,d^4x, \qquad f \in \mathcal{S}(\mathbb{R}^4),$$
on a dense invariant domain in the GNS Hilbert space $\mathcal{H}$ reconstructed by the preprint. Its vacuum expectation values are the $S_n^{\mathrm{ren}}$, and its short-distance behavior agrees with AF by construction.

*Important caveat:* Wightman reconstruction requires verifying OS-positivity (OS3) *for the renormalized Schwinger functions*. Since $Z_O(a)$ is a positive scalar, OS3 is preserved trivially from the lattice — *provided* the limit exists. That is the circularity: the whole existence-of-the-limit claim is Step 4d.

**Step 4f. Higher operators.** Repeat for $\mathrm{Tr}\,F_{\mu\nu} F_{\rho\sigma}$ (spin-2, giving the stress tensor after Belinfante–Rosenfeld; see G4c), $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ (dim 6), $\mathrm{Tr}(F_{\mu\nu}F_{\nu\rho}F_{\rho\mu})$ (dim 6, $\mathcal{C}$-odd), and Wilson loops (non-local, perimeter subtraction). Each gets its own $Z_{\mathcal{O}}(a)$; for dimension $> 4$, mixing with lower-dimension operators of the same quantum numbers produces a renormalization *matrix* rather than a scalar.

---

## Section 5 — Rigor vs. conjecture vs. open

| Step | Status | Justification |
|---|---|---|
| 4a (bare lattice operator) | **[OK]** | Elementary lattice definition; gauge-invariant; scalar under hypercubic group; classical continuum limit is standard computation. |
| 4b (one-loop anomalous dimension) | **[OK]** (perturbative identity) | $\gamma_O = -2\beta/g$ follows from the trace anomaly Ward identity and Kluberg-Stern–Zuber. Rigorous at the level of continuum perturbation theory. Lattice perturbative matching to this result is standard (Caracciolo–Menotti–Pelissetto 1992; Capitani 2003). |
| 4c (renormalization constant) | **[CONJECTURE]** | The formula for $Z_O(a)$ is a well-defined non-perturbative object *once* one fixes the scheme ($\overline{\mathrm{MS}}$, lattice scheme, etc.) and the scale $\Lambda$. That $Z_O$ defined this way absorbs lattice divergences to all orders non-perturbatively is conjectural (Symanzik). |
| 4d (existence of renormalized 2-point Schwinger function) | **[OPEN]** | This is the Symanzik composite-operator program for 4D non-Abelian YM. It has never been proved rigorously. For super-renormalizable theories ($\phi^4_3$) it is theorem; for marginal theories in 4D it is open. |
| 4e (Wightman reconstruction of the operator) | **[OK conditional on 4d]** | Standard OS reconstruction applied to $S_n^{\mathrm{ren}}$. The only issue is verifying OS3 for the renormalized $S_n^{\mathrm{ren}}$; since $Z_O$ is positive, it reduces to OS3 at the lattice level, which the preprint already has (subject to K-uniformity). |
| 4f (higher operators + mixing matrix) | **[OPEN]** | Operator mixing at dimension $\geq 6$ is much harder than the scalar renormalization of dimension 4; even the structure of the mixing matrix is non-trivial and requires all of Step 4d first. |

**Honest summary:** Steps 4a, 4b, 4e are *rigorous*. Step 4c is a *definition* that is well-posed modulo the non-perturbative definition of $\Lambda$. Steps 4d and 4f are the **real open problems**. They are the bulk of what Clay asks.

---

## Section 6 — A weaker "Schwinger function" version

A rigorous but weaker deliverable restricts attention to *correlators* (Euclidean or Minkowski Schwinger functions) rather than operator-valued distributions on $\mathcal{H}$.

**Weaker deliverable (Schwinger-function renormalization).** Construct a family of tempered distributions $\{S_n^{\mathrm{ren}}\}_{n\geq 1}$ on $(\mathbb{R}^4)^n$, symmetric, Euclidean-invariant, cluster-decomposing, OS-positive, satisfying:

(i) For non-coincident points, $S_n^{\mathrm{ren}}(x_1, \ldots, x_n) = \lim_{a \to 0} Z_O(a)^n\,\langle \mathcal{O}^{\mathrm{bare}}_a(x_1) \cdots \mathcal{O}^{\mathrm{bare}}_a(x_n)\rangle_a$.

(ii) The two-point function has short-distance asymptotics $S_2^{\mathrm{ren}}(x,y) \sim A |x-y|^{-8} (\log)^{+2}$ matching AF.

(iii) The higher Schwinger functions satisfy the bound $|S_n^{\mathrm{ren}}(x_1, \ldots, x_n)| \leq C^n n! \prod_{i<j} (1 + |x_i - x_j|^{-8})$ or similar, with AF-corrected power counting.

This deliverable *does not* require Wightman reconstruction of the composite operator, only the existence and short-distance behavior of its correlators. It sidesteps the subtleties of common invariant domain, local commutativity, and temperedness as distributions on $\mathcal{H}$.

**Does it satisfy J–W?** Charitable reading: J–W cares about *correlation functions matching AF*, with "field operators" a means to that end — so the weaker deliverable suffices, because given renormalized Schwinger functions the OS reconstruction produces operator-valued distributions automatically, and "AF at short distances" is a statement about correlators. Strict reading: J–W literally wants operator-valued distributions on $\mathcal{H}$ with common invariant domain, local commutativity, and an OPE — these are operator-theoretic data not extractable from Schwinger functions alone.

Even the weaker version is **not** proved by the current preprint. The preprint has Schwinger functions of *bare* lattice operators with a spurious free-propagator $|x|^{-2}$ short-distance bound, not renormalized Schwinger functions with the AF-predicted $|x|^{-8}(\log)^{+2}$ behavior. So even the weaker deliverable requires new work — at minimum Steps 4a–4d.

---

## Section 7 — Recommended next steps for the authors

Concrete actions to move Tier 3A toward Clay-eligible status without attempting a full non-perturbative construction:

- **(a) Explicit one-loop $\gamma_O$.** Self-contained lattice perturbative computation showing $\gamma_O(g) = -2 b_0 g^2 + O(g^4)$ for $\hat{s}_P$, citing Caracciolo–Menotti–Pelissetto (1992) and Capitani (2003). State as a Lemma with explicit coefficients.

- **(b) Conjecture + consistency check.** State existence of $S_2^{\mathrm{ren}}$ as a *Symanzik conjecture for 4D YM*. Verify consistency with the existing exponential-decay bound, making the AF-corrected short-distance power $|x-y|^{-8}(\log)^{+2}$ explicit. This eliminates the preprint's incorrect $|x-y|^{-2}$ claim.

- **(c) Restrict the Clay claim.** Add a Scope section: "This work establishes (i) Schwinger-function continuum YM, (ii) positive mass gap, (iii) OS reconstruction to a gapped Hilbert space; it does *not* establish renormalized composite operators as operator-valued distributions — that is deferred."

- **(d) Cite Hollands–Wald honestly.** Acknowledge the Hollands–Wald (2001, 2010) locally covariant framework as the template, and state the specific obstructions to extending it to 4D non-Abelian YM: (i) no positive-metric Wightman theory for $A_\mu^a$; (ii) no non-perturbative existence theorem for renormalized composites; (iii) no non-perturbative OPE.

- **(e) Downgrade the OPE bound to a conjecture.** The coincident-point lemma's $|S_n| \leq C^n n! \prod |x_i - x_{i+1}|^{-2}$ "by the OPE" is wrong (the OPE has not been constructed and the power is the free one). Restate as an *AF-corrected OPE conjecture* with $|x_i - x_{i+1}|^{-8}(\log)^{+2}$, and drop any use of it from the mass-gap proof (which should not depend on it).

- **(f) Separate papers.** Full Tier 3A (Steps 4a–4f rigorously) is 1–2 papers of original research, separate from the mass-gap paper. The mass-gap paper stands on Tier 0 + Tier 1; Tier 3A is Clay-structural polish upgrading the conclusion from "Schwinger-function mass gap" to "Wightman-theory mass gap with AF-matched composites."

---

## Final assessment

The outline above gets roughly **20–30%** of the way to a Clay-eligible Tier 3A deliverable:

- **Rigorous (10–15%):** Steps 4a, 4b, 4e — bare lattice operator, perturbative anomalous dimension, conditional Wightman reconstruction — can be written up tightly in ~10 pages.

- **Defensible as conjecture (10–15%):** Step 4c ($Z_O(a)$ prescription) and the weaker Schwinger-function version (Section 6) stated as conjectures with explicit one-loop consistency. Useful scholarship; meets J–W under a charitable reading.

- **Genuinely open (70–80%):** Steps 4d (non-perturbative existence of renormalized Schwinger functions for 4D YM), 4f (mixing matrices for higher composites), and a non-perturbative OPE (G4d). These are known open problems in mathematical QFT, arguably the hardest part of the Clay problem after the mass gap itself; no credible shortcut exists.

**Bottom line.** G4(a) in its full form is a known open problem. A draft outline + honest scoping is the right Tier 3A deliverable for a Clay submission; a fake solution would be detected by any referee. The authors can rigorously close the perturbative/formal half, state the non-perturbative half as a Symanzik-type conjecture with an explicit AF-consistent short-distance prediction, and be explicit about what remains open. This file is a roadmap for that deliverable.
