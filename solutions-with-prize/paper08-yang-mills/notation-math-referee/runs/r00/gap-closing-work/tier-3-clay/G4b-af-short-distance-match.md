# Tier 3 / Gap G4(b): Asymptotic-Freedom Short-Distance Matching

**Status:** Draft matching argument. *Conditional on* Tier 3A (G4(a), renormalized composite operators) and on the standard non-perturbative-equals-perturbative hypothesis of the OPE in QCD.

**Scope:** Addresses the second of the four Jaffe–Witten §4 sub-requirements: correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory.

**Sister document:** `G4a-renormalized-composite-operators.md` (assumed to provide $Z_O(a)$ and the renormalized Schwinger function $S_2^{\mathrm{ren}}(x, y)$ as a finite distribution on $\mathbb{R}^4 \times \mathbb{R}^4 \setminus \{x = y\}$).

---

## Section 1 — The gap precisely

Jaffe–Witten §4 states (verbatim from the Clay official problem description):

> "Correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory."

In the preprint, §5.7(f) derives the short-distance bound
$$|S_2^c(x, y)| \leq C\,|x-y|^{-2}\,e^{-\Delta_\infty|x-y|} \tag{P1}$$
for the connected plaquette-plaquette Schwinger function $S_2^c(x, y) = \langle s_P(x) s_P(y)\rangle_c$. The exponent $-2$ in (P1) is the Källén–Lehmann bound for a free massive scalar propagator with mass $\Delta_\infty$; it is *not* the asymptotically free (AF) short-distance behavior of a non-Abelian gauge theory.

Two issues are conflated in (P1):

1. **Wrong engineering dimension.** The plaquette operator $s_P = 1 - (1/N)\mathrm{Re}\,\mathrm{Tr}\,U_P$ has classical continuum representative $\sim (a^4 g^2/(2N))\,\mathrm{Tr}(F_{\mu\nu}^2(x))$, so in the *physical* normalization $\mathcal{O}(x) = \mathrm{Tr}\,F_{\mu\nu}^2(x)$ the two-point function has engineering dimension $2 d_\mathcal{O} = 8$, not $2$. The preprint's (P1) is an *upper bound* from the free massive-scalar spectral representation, not the leading short-distance law.

2. **No logarithmic AF correction.** Even once the correct power $|x|^{-8}$ is recovered for $\langle \mathcal{O}(x) \mathcal{O}(0)\rangle$, asymptotic freedom predicts logarithmic corrections from the running of $\alpha_s(1/|x|)$ and from the anomalous dimension $\gamma_\mathcal{O}$ of $\mathcal{O}$. These logs are the *signature* of a non-trivial interacting AF theory and are exactly what Jaffe–Witten asks to be matched.

The preprint does not construct the renormalized two-point function, compute its short-distance asymptotic expansion, or compare with the one-loop perturbative result. All three are needed for J–W §4(b). **GENUINE GAP.**

---

## Section 2 — The perturbative AF prediction

**Operator.** Let $\mathcal{O}(x) = \mathrm{Tr}(F_{\mu\nu}(x) F^{\mu\nu}(x))$, engineering dimension $d_\mathcal{O} = 4$. A celebrated result of Chanowitz–Ellis (1972), Kluberg-Stern–Zuber (1974), and Nielsen (1977): $\mathrm{Tr}\,F^2$ is a *finite* composite operator ($\gamma_{\mathrm{Tr}\,F^2} = 0$ in $\overline{\mathrm{MS}}$), because it is proportional to the trace anomaly $T_\mu^\mu \propto (\beta(g)/g)\,\mathrm{Tr}\,F^2$, and the coupling renormalization absorbs all logs. Equivalently, $(\beta/g)\,\mathrm{Tr}\,F^2$ has anomalous dimension $\gamma_\mathcal{O}(g) = 2\beta(g)/g$.

**Tree level.** Standard textbook result (Peskin–Schroeder Ch. 17; Collins 1984 §14; Muta 1998 §5):
$$\langle \mathrm{Tr}\,F^2(x)\,\mathrm{Tr}\,F^2(0)\rangle^{(0)}_{\mathrm{pert}} \;=\; \frac{2(N^2 - 1)}{\pi^4}\,\frac{1}{|x|^8}\cdot\alpha_s^2 + \text{(contact)}. \tag{S2.1}$$
The power $|x|^{-8}$ is fixed by engineering dimension; the $\alpha_s^2$ prefactor comes from the explicit $g^2$ in $F^2 = (\partial A + gAA)^2$.

**One-loop.** Dressing with gluon self-energies, three- and four-gluon vertex corrections and ghost loops gives (Zoller–Chetyrkin, JHEP 12 (2012) 119; JHEP 10 (2014) 169):
$$\langle \mathrm{Tr}\,F^2(x)\,\mathrm{Tr}\,F^2(0)\rangle_{\mathrm{pert}} \;=\; \frac{2(N^2 - 1)}{\pi^4}\,\frac{\alpha_s(\mu)^2}{|x|^8}\!\left[1 + \frac{\alpha_s(\mu)}{\pi}\bigl(a_0 - b_0\ln(\mu^2 x^2)\bigr) + O(\alpha_s^2)\right] \tag{S2.2}$$
with $a_0$ scheme-dependent and the log coefficient fixed by RG. Pure $\mathrm{SU}(N)$: $\beta_0 = 11N/3$ (textbook); $b_0 = 11N/(48\pi^2)$ (preprint convention).

**RG improvement.** Choosing $\mu = 1/|x|$ kills the explicit log and replaces $\alpha_s(\mu)$ by the running coupling
$$\alpha_s(1/|x|) \;=\; \frac{2\pi}{\beta_0\,\ln(1/|x|^2\Lambda^2)}\,[1 + O(\log\log/\log)]. \tag{S2.3}$$
Substituting:
$$\boxed{\;\langle \mathrm{Tr}\,F^2(x)\,\mathrm{Tr}\,F^2(0)\rangle_{\mathrm{pert}} \;\sim\; \frac{C_N}{|x|^{8}}\cdot\left(\ln\frac{1}{|x|\Lambda}\right)^{-2}\cdot\bigl[1 + O((\ln)^{-1})\bigr]\;} \tag{S2.4}$$
as $|x| \to 0$, with $C_N = 2(N^2-1)/\pi^6$. The $(\ln)^{-2}$ factor is the AF-log correction: in the general formula $(\ln(1/|x|\Lambda))^{-2\gamma_\mathcal{O}/\beta_0}$, the two powers of $\alpha_s$ from the $F^2$ prefactor contribute $2$ to the exponent, independent of operator convention.

**Takeaway.** The preprint's free-scalar bound $|x|^{-2}e^{-\Delta|x|}$ and the correct AF prediction $|x|^{-8}(\ln 1/|x|\Lambda)^{-2}$ differ by *six* engineering powers plus a logarithmic correction. The exponential suppression is a far-infrared ($|x| \gtrsim 1/\Delta_\infty$) phenomenon and does not control the short-distance law.

---

## Section 3 — The lattice perturbative side

The rigorous tool linking lattice and continuum perturbation theory is **Reisz's power-counting theorem** (CMP 116 (1988) 81; CMP 117 (1988) 79, 639):

> **(Reisz, paraphrased.)** *Let $I_L(p; a)$ be a Feynman integral built from a lattice action whose naive continuum limit is a renormalizable QFT, with propagators obeying the standard lattice positivity and UV-degree conditions. If the lattice degree of divergence of every subdiagram is negative, then $I_L(p; a) \to I_{\mathrm{cont}}(p)$ as $a \to 0$, with $I_L - I_{\mathrm{cont}} = O(a^2\log^k a)$.*

Applied to $\mathcal{O}_a^{\mathrm{bare}}(x) := (2N/(a^4 g_0^2)) s_P(x)$ at one loop:
$$\langle \mathcal{O}_a^{\mathrm{bare}}(x)\,\mathcal{O}_a^{\mathrm{bare}}(0)\rangle^{(\text{1-loop})}_{\mathrm{lat}} \;=\; \langle \mathrm{Tr}\,F^2(x)\,\mathrm{Tr}\,F^2(0)\rangle^{(\text{1-loop})}_{\mathrm{cont}} + O(a^2\log a)\cdot|x|^{-10}, \tag{S3.1}$$
a *purely perturbative* agreement theorem. For lattice gauge theory the extensions are due to Lüscher–Weisz (CMP 97 (1985) 59), applied to composite operators by Caracciolo–Curci–Menotti–Pelissetto (1989, 1991, 1992); textbook account Capitani, Phys. Rep. 382 (2003) 113.

**Key point.** (S3.1) is lattice-perturbative $\leftrightarrow$ continuum-perturbative agreement only. It says *nothing* about whether the non-perturbative lattice path integral equals its perturbative expansion at short distances — that is the separate question of Section 5.

---

## Section 4 — Conjectural Matching Theorem

**Hypotheses.**

- **(H1) Tier 3A.** The renormalized operator $[\mathcal{O}]_R^{(a)}(x) = Z_\mathcal{O}(a)\,\mathcal{O}_a^{\mathrm{bare}}(x)$ and the renormalized Schwinger function
$$S_2^{\mathrm{ren}}(x, y) := \lim_{a \to 0}\,Z_\mathcal{O}(a)^2\,\langle \mathcal{O}_a^{\mathrm{bare}}(x)\,\mathcal{O}_a^{\mathrm{bare}}(y)\rangle_{\mathrm{lat}} \tag{S4.1}$$
exist as finite tempered distributions, smooth off the diagonal.

- **(H2) Tier 0+1.** The non-perturbative continuum limit exists (preprint §5; Banach–Alaoglu limit with uniform OS1–OS5).

- **(H3)** Reisz power counting (S3.1) holds.

- **(H4) Non-perturbative $=$ perturbative at short distances.** For $|x-y| \to 0$, $S_2^{\mathrm{ren}}$ admits an asymptotic expansion whose coefficients are the renormalized perturbative diagrams, with error $O(\alpha_s(1/|x-y|))$. This is the standard OPE-in-QCD hypothesis.

**Theorem (Conjectural AF Matching).** *Under (H1)–(H4), as $|x-y| \to 0$,*
$$S_2^{\mathrm{ren}}(x, y) \;=\; \frac{C_N}{|x-y|^{8}}\cdot\left(\ln\frac{1}{|x-y|\Lambda}\right)^{-2}\cdot[1 + o(1)] \tag{S4.2}$$
*with $C_N = 2(N^2-1)/\pi^6$ and $\Lambda$ the non-perturbative $\mathrm{SU}(N)$ Lambda parameter.*

**Sketch.** (H1) gives $S_2^{\mathrm{ren}}$ as a smooth-off-diagonal distribution; (H4) gives an asymptotic expansion in $\alpha_s(1/|x-y|)$ with perturbative coefficients; (H3) identifies these as the continuum perturbative diagrams of Section 2 (lattice $O(a^2)$ artifacts vanish in the $a \to 0$ limit taken before $|x-y| \to 0$); the one-loop coefficient is (S2.4) = (S4.2). The proof logic is downstream of (H1), (H4); technical work is absorbed into those hypotheses.

---

## Section 5 — Rigorous versus conjectural

| Ingredient | Status |
|:-----------|:-------|
| (a) Perturbative continuum one-loop $\langle \mathrm{Tr}\,F^2 \cdot \mathrm{Tr}\,F^2\rangle$ | **Rigorous within perturbation theory.** Textbook result; Zoller–Chetyrkin extend to three loops. |
| (b) Anomalous dimension $\gamma_\mathcal{O}$ | **Rigorous within perturbation theory.** $\mathcal{O} = (\beta/g)\mathrm{Tr}\,F^2$ is a trace-anomaly operator with $\gamma_\mathcal{O} = 2\beta(g)/g$; equivalently, $\mathrm{Tr}\,F^2$ by itself is a *finite* composite operator (Kluberg-Stern–Zuber, Nielsen), so the log corrections come entirely from the coupling renormalization. |
| (c) Reisz lattice power counting | **Rigorous.** Theorem of Reisz (CMP 116, 117, 1988) for lattice scalars; extended to lattice gauge theory via Lüscher–Weisz 1985; compiled in Capitani 2003. A purely perturbative statement at the level of individual Feynman integrals. |
| (d) Lattice bare operator $=$ continuum operator at one loop | **Rigorous** (Caracciolo–Curci–Menotti–Pelissetto 1989, 1991, 1992 for the energy–momentum tensor; same methodology applies to $\mathrm{Tr}\,F^2$). |
| (e) Multiplicative $Z_\mathcal{O}(a)$ exists non-perturbatively | **Open.** This is Gap G4(a) / Tier 3A. Hollands–Wald have a free-field analogue; the 4D non-Abelian gauge case is not rigorously established. |
| (f) Non-perturbative lattice $=$ perturbative continuum at short distances | **Open / Conjectural.** This is the "OPE in QCD" hypothesis. It is the standard working assumption of every lattice QCD computation (all phenomenological applications of the short-distance OPE rely on it implicitly), but has never been rigorously proved for 4D non-Abelian Yang–Mills. For super-renormalizable theories such as $\phi^4_3$, analogous statements have been proved (Glimm–Jaffe; Magnen–Rivasseau); for 4D YM they are open. |

**Summary.** Items (a)–(d) constitute *rigorous, purely perturbative* input that can be quoted directly into the preprint with no additional constructive-QFT work. Items (e) and (f) are the content of Tier 3A and of a separate "perturbative-agreement theorem" which is beyond current rigorous technology. Consequently the AF matching (S4.2) can be stated as a *theorem modulo (e) and (f)*.

**This is a milder open problem than G4(a).** G4(a) is a full composite-operator construction in non-Abelian 4D gauge theory — a research program. G4(b), conditional on G4(a), is essentially a book-keeping exercise: one has the renormalized operator, one quotes the textbook perturbative answer, and one asserts (H4) as a standard hypothesis. The intellectually honest thing to do in the preprint is to state (H4) as a hypothesis rather than as a theorem.

---

## Section 6 — Weaker leading-order check (purely lattice-perturbative)

A genuinely provable fragment, requiring *neither* (e) nor (f):

**Proposition (Leading-order lattice-perturbative match).** *Let $\mathcal{O}_a^{\mathrm{bare}}(x) = (2N/(a^4 g_0^2)) s_P(x)$ be the bare lattice operator. The two-point function $\langle \mathcal{O}_a^{\mathrm{bare}}(x)\,\mathcal{O}_a^{\mathrm{bare}}(0)\rangle$ computed from the lattice action at tree level, for $|x|$ held fixed as $a \to 0$, converges to the tree-level continuum answer*
$$\lim_{a \to 0}\,\langle \mathcal{O}_a^{\mathrm{bare}}(x)\,\mathcal{O}_a^{\mathrm{bare}}(0)\rangle^{(\text{tree})}_{\mathrm{lat}} \;=\; \frac{2(N^2-1)}{\pi^4}\,\frac{1}{|x|^{8}}\cdot\Bigl(\frac{\alpha_s}{\pi}\Bigr)^{2} + O(a^2/|x|^{10}). \tag{S6.1}$$

*Proof idea.* At tree level there are no loops and Reisz power counting reduces to the fact that the free lattice gluon propagator $G_a(p)$ differs from its continuum counterpart $G_0(p) = 1/p^2$ by $O(a^2 p^2)$ for $|p| \ll 1/a$. The bare operator $\mathcal{O}_a^{\mathrm{bare}}$ differs from its continuum representative $\mathrm{Tr}\,F^2(x)$ by $O(a^2)$ from the plaquette-to-$F^2$ expansion (preprint §5.2.1). Substituting into the tree-level contraction yields (S6.1).

This *purely perturbative lattice* check can be performed explicitly (it is the opening computation of Lüscher–Weisz 1985 and the starting point of Capitani 2003). It does *not* require constructing $Z_\mathcal{O}(a)$, does *not* require the non-perturbative continuum limit, and does *not* rely on the OPE hypothesis. It establishes that *at tree level*, the lattice bare operator reproduces the $|x|^{-8}$ engineering-dimension power, correctly identifying the lattice continuum limit as Yang–Mills at short distances.

**Limitations.** The Proposition verifies only the *classical* $|x|^{-8}$ power; the $(\ln)^{-2}$ AF correction requires one-loop diagrams and hence the $Z_\mathcal{O}(a)$ renormalization of Tier 3A. So (S6.1) is genuinely weaker than (S4.2), but it is at least *rigorously provable* from ingredients already in the preprint.

---

## Section 7 — Draft replacement for §5.7(f)

> **Remark (Short-distance asymptotic freedom matching).** *In addition to the exponential-decay bound of the preceding remark, the constructed Schwinger functions of gauge-invariant composite operators are expected, conditional on the standard QCD OPE hypothesis, to match the perturbative AF short-distance predictions.*
>
> *Let $\mathcal{O}(x) = \mathrm{Tr}(F_{\mu\nu}(x)F^{\mu\nu}(x))$. The RG-improved one-loop perturbative result for pure $\mathrm{SU}(N)$ Yang–Mills is*
> $$\langle \mathcal{O}(x)\,\mathcal{O}(0)\rangle^{\mathrm{pert}}_{\mathrm{ren}} \;\sim\; \frac{C_N}{|x|^{8}}\left(\ln\frac{1}{|x|\Lambda}\right)^{-2}[1 + O((\ln)^{-1})],\qquad |x| \to 0, \tag{5.7.f.new.1}$$
> *with $C_N = 2(N^2-1)/\pi^6$, $\beta_0 = 11N/3$, and $\Lambda$ the $\mathrm{SU}(N)$ Lambda parameter. The $(\ln)^{-2}$ factor combines the running of $\alpha_s$ and the trace-anomaly identity $T_\mu^\mu \propto (\beta/g)\mathrm{Tr}\,F^2$ (Chanowitz–Ellis 1972; Kluberg-Stern–Zuber 1974; Nielsen 1977).*
>
> *By the lattice-to-continuum power-counting theorem of Reisz (CMP 116 (1988) 81; CMP 117 (1988) 79), extended to lattice gauge theory by Lüscher–Weisz (CMP 97 (1985) 59) and applied to gauge-invariant composites by Caracciolo et al. (Phys. Lett. B 228 (1989) 375; Nucl. Phys. B 375 (1992) 195), the one-loop lattice Feynman diagrams for $\langle \mathcal{O}_a^{\mathrm{bare}}(x)\,\mathcal{O}_a^{\mathrm{bare}}(y)\rangle$ converge to the one-loop continuum diagrams as $a \to 0$, with $O(a^2\log^k a)$ corrections. This is a rigorous purely-perturbative statement.*
>
> **Proposition 5.7.f.new (Leading-order lattice-perturbative match).** *Let $\mathcal{O}_a^{\mathrm{bare}}(x) = (2N/(a^4 g_0^2))\,s_P(x)$. At tree level in lattice perturbation theory,*
> $$\langle \mathcal{O}_a^{\mathrm{bare}}(x)\,\mathcal{O}_a^{\mathrm{bare}}(0)\rangle^{(\text{tree})}_{\mathrm{lat}} \;=\; \frac{2(N^2-1)}{\pi^4}\,\frac{\alpha_s^2}{|x|^{8}}\bigl[1 + O(a^2/|x|^{2})\bigr] \tag{5.7.f.new.2}$$
> *as $a \to 0$ for fixed $|x| > 0$. In particular, the lattice bare two-point function correctly reproduces the $|x|^{-8}$ engineering-dimension power of (5.7.f.new.1).*
>
> *The full AF-log matching (5.7.f.new.1), including the $(\ln)^{-2}$ correction, requires both the multiplicative operator renormalization $Z_\mathcal{O}(a)$ (Appendix J; see G4(a)) and the hypothesis that the non-perturbative lattice Schwinger function admits at short distances an asymptotic expansion whose coefficients coincide with those of continuum perturbation theory. This is the standard working hypothesis of lattice QCD; a rigorous proof for 4D non-Abelian gauge theory is beyond the scope of this paper.*
>
> *The preprint's earlier bound $|S_2^c(x,y)| \leq C\,|x-y|^{-2}\,e^{-\Delta_\infty|x-y|}$ is an upper bound from the Källén–Lehmann representation with gap $\Delta_\infty$; it controls the far-infrared ($|x-y| \gtrsim 1/\Delta_\infty$) behavior and guarantees OS1 temperedness, but does not state the leading short-distance singularity, which is given by (5.7.f.new.1) / (5.7.f.new.2).*

---

## Section 8 — Recommended next steps for the authors

**(a) Citations.** For the one-loop $\langle \mathrm{Tr}\,F^2\cdot\mathrm{Tr}\,F^2\rangle$ result: Peskin–Schroeder Ch. 17; Collins 1984 Ch. 10–14; Muta 1998 Ch. 5; Zoller–Chetyrkin JHEP 12 (2012) 119 and JHEP 10 (2014) 169 (explicit three-loop Wilson coefficients). For $\gamma_{\mathrm{Tr}\,F^2} = 0$: Chanowitz–Ellis, Phys. Rev. D 7 (1973) 2490; Kluberg-Stern–Zuber, Phys. Rev. D 12 (1975) 467; Nielsen, Nucl. Phys. B 120 (1977) 212. For Reisz lattice power counting: Reisz CMP 116 (1988) 81, CMP 117 (1988) 79, 639. For lattice composites: Lüscher–Weisz CMP 97 (1985) 59; Caracciolo–Curci–Menotti–Pelissetto Phys. Lett. B 228 (1989) 375, Phys. Lett. B 260 (1991) 401, Nucl. Phys. B 375 (1992) 195; Capitani Phys. Rep. 382 (2003) 113.

**(b) Add §5.7(f) subsection.** Incorporate the Section 7 draft verbatim (renumber equations). Do *not* weaken the existing spectral bound (P1); present AF matching as complementary — (P1) gives far-infrared decay, (5.7.f.new.1) gives the short-distance law.

**(c) State (H4) as hypothesis.** Explicitly state the non-perturbative-equals-perturbative short-distance assertion as a hypothesis of the proof, not a theorem. Suggested phrasing:

> *"We take as a hypothesis, standard in lattice QCD but not rigorously proved for 4D non-Abelian gauge theory, that the renormalized lattice Schwinger functions admit a short-distance asymptotic expansion whose coefficients coincide with those of the continuum perturbative OPE. Under this hypothesis, combined with Reisz power counting and the composite operator renormalization of Appendix J, the AF matching (5.7.f.new.1) follows."*

**(d) Optional numerical cross-check.** Explicit one-loop lattice computation of $\langle s_P(x)\,s_P(y)\rangle$ at a few lattice spacings, compared with the continuum one-loop result, verifying $O(a^2)$ agreement. Sanity check, not required for rigor.

---

## Honest assessment (for the caller)

How much of G4(b) can be closed without first solving G4(a)? In purely rigorous terms, the leading-order tree-level lattice-perturbative check of Section 6 (Proposition 5.7.f.new, equation S6.1) can be established completely from lattice perturbation theory plus the naive plaquette $\to F^2$ expansion already used in the preprint — this recovers the $|x|^{-8}$ power and takes the preprint from "free massive scalar short-distance bound" to "correct engineering-dimension power law" without touching G4(a). Everything beyond that — the logarithmic AF correction $(\ln 1/|x|\Lambda)^{-2}$, the non-perturbative-equals-perturbative statement, and the identification of $\Lambda$ with the Yang–Mills scale — requires either the renormalized composite operators of G4(a) or an external hypothesis equivalent to assuming a non-perturbative OPE. Thus G4(b) stratifies cleanly into (i) a rigorous tree-level fragment closable independently (~1 page of new text in §5.7(f)), (ii) a conditional one-loop-and-beyond theorem (conditional on G4(a) plus the standard OPE hypothesis), and (iii) a statement that the full non-perturbative matching is *open* for 4D non-Abelian Yang–Mills and is not resolved by this preprint or its successors short of a separate research program. The honest Clay submission will present (i) as rigorous, (ii) as "Theorem, modulo G4(a) and Hypothesis H4", and (iii) as an explicit acknowledgement of the remaining gap.
