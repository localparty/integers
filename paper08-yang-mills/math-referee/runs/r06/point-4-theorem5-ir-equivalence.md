# Point 4: Theorem 5 -- IR Equivalence

**Location:** Section 4.5

**Verdict:** SOUND

**Finding:**

The interrogation points for this item appear to be based on an earlier version of the preprint in which Theorem 5 was labeled "Proof sketch" and invoked the Appelquist--Carazzone theorem. **The current release candidate contains a complete rigorous proof** via the reduced transfer matrix and the Feshbach projection. The proof is structured as four lemmas (well-definedness, trace-norm bound, spectral perturbation, Feshbach spectral gap) followed by a five-step assembly. The word "Proof sketch" does not appear; the section header reads "Proof" (Section 4.5, after the theorem statement).

I address each interrogation point against the current text.

---

## (a) Does Section 5 actually provide the decoupling?

**Claim under attack:** Section 5 proves the continuum limit for the KK-enhanced theory, not the standard theory. Where is the equivalence established?

**Finding: SOUND.** The interrogation conflates the roles of Section 4.5 and Section 5.

The logical chain is:

1. **Section 4, Theorem 4:** $\Delta_0^{\mathrm{KK}} > 0$ (lattice mass gap for the KK-enhanced theory).
2. **Section 4.5, Theorem 5:** $\Delta_0^{\mathrm{std}} \geq \Delta_0^{\mathrm{KK}} - C e^{-m_1 a/2} > 0$ (lattice mass gap for the standard theory). This is proved purely at the lattice level, for fixed $a$, using operator perturbation theory.
3. **Section 5:** Balaban's RG, applied to the **standard** $\mathrm{SU}(N)$ lattice gauge theory (not the KK theory), preserves the mass gap through the continuum limit: $\Delta_\infty^{\mathrm{std}} > 0$.

Section 5 is NOT applied to the KK-enhanced theory. The KK enhancement has served its purpose after Step 2: it provided the starting input $\Delta_0^{\mathrm{std}} > 0$. Balaban's published results (CMP 109, 119) apply to the standard $\mathrm{SU}(N)$ lattice theory, which is what Step 3 uses.

The equivalence between the two theories is established **entirely within Section 4.5**, at the lattice level, by comparing the spectra of $\hat{T}_{\mathrm{red}}$ and $\hat{T}_{\mathrm{std}}$ on $\mathcal{H}_{\mathrm{std}}$.

---

## (b) The Appelquist--Carazzone limitation

**Claim under attack:** The proof invokes Wilsonian decoupling (Appelquist--Carazzone), which is a perturbative theorem.

**Finding: NOT APPLICABLE TO CURRENT VERSION.**

The current proof of Theorem 5 does NOT invoke the Appelquist--Carazzone theorem. The "Remarks" section (after the proof assembly) explicitly states:

> "The Wilsonian decoupling picture (Appelquist--Carazzone 1975) provided the physical intuition; the transfer matrix argument makes it rigorous. No monotonicity or correlation inequalities are required."

The actual proof uses:
- **Lemma 2 (trace-norm bound):** The cluster expansion of Section 4.3 bounds $\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}} \leq C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. This is a NON-PERTURBATIVE bound: the cluster expansion converges at all couplings in the physical regime.
- **Lemma 3 (Weyl perturbation):** Standard operator perturbation theory (Kato 1966).
- **Lemma 4 (Feshbach decomposition):** Rigorous block-diagonalization of the Hamiltonian, bounding the off-diagonal coupling $W$ by the cluster expansion.

Every step is non-perturbative. The only input is the exponential suppression $e^{-m_1 a}$ of KK modes, which comes from the spectral gap of the internal space (Theorem 1), not from perturbation theory.

---

## (c) Logical consequence for the main claim

**Claim under attack:** If Theorem 5 is a proof sketch, the mass gap for the standard Yang-Mills theory is not proved.

**Finding: SOUND.**

Theorem 5 is NOT a proof sketch in the current version. It is a complete proof. The preprint proves:

- $\Delta_0^{\mathrm{std}} > 0$ (Theorem 5, Section 4.5: rigorous, via Feshbach + Weyl + cluster expansion).
- $\Delta_\infty^{\mathrm{std}} > 0$ (Section 5.7: rigorous, via Balaban's RG + spectral lemma + operator classification).

The mass gap is proved for the **standard** $\mathrm{SU}(N)$ Yang-Mills theory, not only for the KK-enhanced theory.

---

**Detailed verification of Theorem 5's proof:**

| Lemma | Method | Input | Status |
|:------|:-------|:------|:-------|
| Lemma 1 (Well-definedness) | Partial trace of positive operator | Theorem 1 (spectral gap) | **Rigorous** |
| Lemma 2 (Trace-norm bound) | Cluster expansion for internal partition function | Theorem 2 (bond activity bound) | **Rigorous** |
| Lemma 3 (Spectral perturbation) | Weyl's inequality (Kato 1966) | Standard functional analysis | **Rigorous** |
| Lemma 4 (Feshbach spectral gap) | Block decomposition of Hamiltonian | Bach--Frohlich--Sigal 1998 | **Rigorous** |
| Assembly | Combining Lemmas 1--4 | None beyond above | **Rigorous** |

The trace-norm bound (Lemma 2) is the key non-perturbative ingredient. Its proof factors the difference $\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}$ through the internal partition function ratio $\mathcal{Z}_{\mathrm{int}}/\mathcal{Z}_{\mathrm{int}}^{(0)} - 1$, which is bounded by the cluster expansion with uniform control over the 4D link variables. This avoids any perturbative approximation.

---

**Impact on the claimed result:** None. Theorem 5 is a complete proof, not a proof sketch. The IR equivalence between the KK-enhanced and standard theories is established rigorously at the lattice level.
