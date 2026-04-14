# Link 14 Critic: Δ_∞ > 0 (Continuum Mass Gap)

**Verdict: WEAKENED** — one structural flaw survives, one genuine gap in the discharge chain.

---

## Attack-by-attack findings

### Vector 1: Lattice gap vs. continuum gap coincidence
The paper's construction is architecturally sound here. $\Delta_\infty$ is defined
as $C_\infty \cdot \Lambda_\infty$ where $C_\infty = \lim_k C_k = \lim_k \Delta_k/\Lambda_k$
is the RG-invariant ratio and $\Lambda_\infty$ is the physical QCD scale. This is
not merely a limit of dimensionless lattice gaps; the RG-invariant ratio construction
correctly identifies the continuum Hamiltonian gap with the limit of the lattice
transfer-matrix gap divided by the running scale. **No break found.**

### Vector 2: Uniform lower bound vs. only liminf
The recursion $C_{K+1} \leq C_K/4 + C_* + O(g_K^2 C_K)$ is shown to have a
bounded orbit $C_K \leq \max(C_0, 4C_*/3)$, and the sum
$\sum_K C_K g_K^4 \hat\Delta_K^2$ converges because the $2^{-Ks}$ factor dominates.
The argument yields uniform boundedness of $C_K$ from above and positivity
$C_\infty \geq C_0(1 - \varepsilon) > 0$, so this is a genuine uniform lower bound,
not just a liminf. **No break found.**

### Vector 3 (MAIN FLAW): Conjecture 1 discharge is internally contradictory
This is the critical weakness. Theorem 8 is titled **"Conditional continuum mass gap"**
and its statement begins *"Assume Conjecture 1 holds with exponent $s \geq 2$."*
Section 5.6 then claims to discharge Conjecture 1 via the "stability of deviation order"
argument. The internal status table (§5.4.7) marks Conjecture 1 "Proved (Section 5.6),"
yet the theorem statement is never updated from conditional to unconditional, and the
text at line 1035 simultaneously reads: *"The remaining problem is Conjecture 1... it
remains to prove the single-step bound $C_{\mathrm{new}}$."*

The discharge argument itself (Part III, §5.6) classifies dimension-6 operators and
invokes the spectral lemma. The lemma applies to operators with a finite multi-time-slice
representation (eq. (1)) of bounded temporal support $2R$. Balaban's newly generated
operators at each RG step are **polymer activities** summed over polymer clusters $X$;
their temporal support grows with $|X|$. The argument in §III.4 applies the spectral
lemma with $M = \|\delta E_k^{d=6}\| \leq Cg_k^4$ drawn from Balaban's uniform bound,
but the multi-time-slice decomposition (1) requires **bounded** temporal support, not
just bounded $L^\infty$ norm. For operators with support of size $|X|$, the internal
sum over intermediate states introduces factors of $|X|$, and summing over all polymers
$X$ requires the decay $e^{-\kappa|X|}$ to absorb the polynomial $|X|^p$ growth. This
is claimed in the §5.4 Cluster-Balaban Handoff Lemma but the spectral-lemma application
in §III.4 quotes only a single-operator bound, not the summed-over-polymers version.
The junction between the polymer-sum spectral bound and the single-operator classification
argument is asserted, not proved.

**Status: WEAKENED.** Conjecture 1 is not cleanly discharged. The title remains
conditional, an internal inconsistency exists, and the polymer-to-spectral-lemma
handoff carries an unverified step.

### Vector 4: Uniqueness of limit (Schwinger functions vs. gap)
Theorem M.2.1 (doubly exponential convergence) controls the Schwinger functions; the
gap $\Delta_\infty$ is defined via the RG-invariant ratio, not extracted from a
subsequential limit of Schwinger functions. Part (d) proves $\Delta_\infty = C_\infty
\cdot \Lambda_\infty > 0$ independently of limit uniqueness of Schwinger functions.
**No break found.**

### Vector 5: Hidden deconfinement/Polyakov loop assumption
The proof invokes the cluster expansion of Section 4, which requires $\beta < a_0/(2\sqrt{3}r_3)$
(strong-coupling regime at the bare scale). This corresponds to small $g_0$, i.e.,
the weak-coupling / AF trajectory, not a deconfinement phase assumption. The Polyakov
loop does not enter the mass gap argument. **No hidden assumption found.**

### Vector 6: Scope — extension to SO(N), Sp(N), exceptional groups
Appendix I.4 (Theorem I.4.1) proves the extension via the Weitzenböck–Bochner theorem
applied to compact irreducible symmetric spaces $G/H$ of compact type. Requirements
(R1)–(R4) are systematically verified per group including $G_2$, $F_4$, $E_6$, $E_7$,
$E_8$. The spectral data ($\lambda_G > 0$) is cited to Besse (1987) with specific
table references. The Balaban extension to non-SU(N) groups is addressed in Appendix K.
The argument is systematic and the group-by-group verification is present. **No break
found**, though referee checking of specific $\lambda_G$ values against Besse Table 9.85
is noted as outstanding (cited in the text itself).

---

## Summary (≤150 words)

WEAKENED. Theorem 8 as stated remains **conditional** on Conjecture 1 (its own
title says so), yet §5.4.7 marks Conjecture 1 "Proved" and §1035 simultaneously
says "it remains to prove the single-step bound" — a three-way internal
contradiction. The discharge argument (§5.6 Part III) classifies dimension-6
operators and applies the spectral lemma correctly for operators of bounded
temporal support, but Balaban's newly generated operators are polymer-cluster
sums with unbounded support. The required summed-over-polymers version of the
spectral lemma is invoked but not proved at the junction. All other attack
vectors (uniform lower bound, gap identification, limit uniqueness, hidden
assumptions, gauge-group scope) survive. The headline result is sound in
architecture but the conditional/unconditional tension in Conjecture 1's
discharge status must be resolved before Link 14 can be declared fully proved.
