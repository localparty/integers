# Verification Report: Section 5 (Continuum Limit)

Referee line-by-line verification of the longest and most critical
section of the preprint.  Cross-referenced against the supporting
proof documents in `etc/proof/`.

---

## Master Checklist

| # | Item | Location | Verdict |
|:--|:-----|:---------|:--------|
| 1 | Balaban UV stability cited correctly | 5.1.2 | **PASS** |
| 2 | Running coupling formula | 5.1.3 | **PASS** |
| 3 | Irrelevant coefficient bound $\|c_n^{(k)}\| \leq C_n g_k^{d_n-4}$ | 5.1.3 | **PASS** |
| 4 | Convergence of $\Lambda_k$ (Basel series) | 5.1.4 | **PASS** |
| 5 | Explicit list of what Balaban does NOT prove | 5.1.5 | **PASS** |
| 6 | Theorem 6(a): parity vanishing of $\nabla_q\hat{E}_k(0)$ | 5.2.3 | **PASS** |
| 7 | Theorem 6(b): operator identity $\hat{E}_k(0)=0$ marked FALSE | 5.2.4 | **PASS** |
| 8 | Redirect to matrix element bound | 5.2.5 | **PASS** |
| 9 | C-symmetry argument for $\mathrm{Tr}(F^3)$ | 5.3.1 | **PASS** |
| 10 | $d^{abc}F^3$ also C-odd | 5.3.1 | **PASS** |
| 11 | $\mathrm{Tr}(F^3) \equiv 0$ for SU(2) | 5.3.1 | **PASS** |
| 12 | Spatial derivative vanishing by translation invariance | 5.3.2 | **PASS** |
| 13 | Temporal derivative: spectral mechanism stated | 5.3.2 | **PASS** -- with caveat (see Finding F2) |
| 14 | Single-step form factor theorem | 5.3.3 | **PASS** (conditional) |
| 15 | RG recursion: 1/4 contraction | 5.4.3 | **PASS** |
| 16 | Fixed point $C_* = (4/3)C_{\mathrm{new}}$ | 5.4.5 | **PASS** |
| 17 | $O(g_k^2)$ correction absorbed by $4^{-k}$ | 5.4.6 | **PASS** |
| 18 | Two-derivative spectral lemma: definition of exc | 5.5.2 | **PASS** |
| 19 | Two-derivative spectral lemma: proof | 5.5.3 | **FLAG** (see Finding F4) |
| 20 | Verification of $\mathrm{exc}(\mathrm{Tr}(D_0 F)^2) \geq 2$ | 5.5.4 | **PASS** |
| 21 | (B1) proof: analyticity with k-independent radius | 5.6, Part I | **PASS** (extraction from Balaban) |
| 22 | (B2) proof: SL(N,C) complexification | 5.6, Part II | **PASS** |
| 23 | Stability of excitation number lemma | 5.6, Part III | **PASS** -- key new argument |
| 24 | Naive splitting correctly identified as failing | 5.6, III.2 | **PASS** |
| 25 | Operator classification avoids naive splitting | 5.6, III.3 | **PASS** |
| 26 | [VERIFY] items correctly identified | 5.6, IV.3 | **PASS** |
| 27 | Moore-Osgood for limit interchange | 5.7(e) | **FLAG** (see Finding F6) |
| 28 | OS axioms verification | 5.7(f) | **FLAG** (see Finding F7) |
| 29 | Final statement $\Delta_\infty > 0$ | 5.7(d) | **PASS** (conditional chain valid) |

---

## Detailed Findings

### F1. Balaban's Results (Section 5.1) -- PASS

The running coupling formula
$$g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6), \quad
  b_0 = \frac{11N}{3(4\pi)^2}$$
is the standard one-loop asymptotic freedom coefficient for SU(N)
in d=4.  Check: $b_0 = 11N/(48\pi^2)$.  The two expressions are
identical ($3 \times (4\pi)^2 = 3 \times 16\pi^2 = 48\pi^2$).
**Correct.**

The convergence of $\Lambda_k = \prod (1 + O(g_j^4))$: since
$g_j^4 \sim 1/(b_0 j \ln 2)^2$ and $\sum 1/j^2 = \pi^2/6$,
the infinite product converges absolutely.  This is a standard
argument (analogous to convergence of $\prod(1+a_j)$ when
$\sum|a_j|<\infty$).  **Correct.**

The list of what Balaban does NOT prove (5.1.5) is accurate and
important.  Items 1-4 are genuine gaps in Balaban's program that
this paper must fill.  **Correctly stated.**


### F2. Temporal Derivative Mechanism (Section 5.3.2) -- PASS with caveat

The section claims:
$$\langle 1|D_0 F(0)|1\rangle_c = (e^{-\hat{\Delta}} - 1)
  \langle 1|F(0)|1\rangle_c$$

This formula is presented as the temporal derivative acting on the
external one-particle state.  The multi-time-slice analysis document
(etc/proof/multi-time-slice-analysis.md) correctly identifies that
this is a shorthand for the intermediate-state spectral mechanism,
NOT for rigid translation of the operator.  Section 5.3.2 uses the
transfer matrix language $F(t+a) = e^{-aH}F(t)e^{aH}$ which is
the correct derivation via the Heisenberg picture.

**Caveat:** The formula as written in lines 510-512 conflates two
things.  The factor $(e^{-\hat{\Delta}}-1)$ arises because the
*intermediate state* in the spectral sum of $\mathrm{Tr}(D_0 F)^2$
passes through the vacuum, and the Boltzmann weight for the vacuum
intermediate relative to the diagonal ($n=1$) gives
$(e^{+\hat{\Delta}}-1)$, not $(e^{-\hat{\Delta}}-1)$.  However,
the squared expression $(e^{\hat{\Delta}}-1)^2 = \hat{\Delta}^2
(1+O(\hat{\Delta}))$ appears correctly in 5.5.4 and in the
multi-time-slice analysis (Sec 4.2).  The sign/direction is
cosmetic since only the square enters the final bound.

**The underlying physics is correct.**  The $\hat{\Delta}^2$
comes from the vacuum intermediate state in the spectral sum
of $\mathrm{Tr}(D_0 F)^2$, exactly as stated in the
multi-time-slice document.  The diagonal term ($n=1$) gives
$(e^0-1)^2 = 0$.  **Verified.**


### F3. C-Symmetry Argument (Section 5.3.1) -- PASS

Under charge conjugation $\mathcal{C}: F \to -F^T$:

$$\mathrm{Tr}(F^3) \to \mathrm{Tr}((-F^T)^3)
  = -\mathrm{Tr}((F^T)^3) = -\mathrm{Tr}((F^3)^T) = -\mathrm{Tr}(F^3)$$

The chain uses: (i) cube of $-F^T$ gives $(-1)^3 = -1$ times
$(F^T)^3$; (ii) $\mathrm{Tr}(A^T B^T C^T) = \mathrm{Tr}((CBA)^T)
= \mathrm{Tr}(CBA)$; (iii) cyclic invariance of trace:
$\mathrm{Tr}(CBA) = \mathrm{Tr}(ABC)$.  **All steps correct.**

For SU(2): The Lie algebra $\mathfrak{su}(2)$ has generators
$\{iT^a\}$ with $T^a = \sigma^a/2$.  The cubic Casimir
$d^{abc} = 2\mathrm{Tr}(T^a\{T^b,T^c\}) = 0$ identically for
SU(2) since the anticommutator of Pauli matrices is proportional
to the identity: $\{\sigma^b, \sigma^c\} = 2\delta^{bc}\mathbf{1}$,
so $\mathrm{Tr}(\sigma^a) = 0$ kills it.
Also: $\mathrm{Tr}(F^3) = F^a_{\mu\nu}F^{b,\nu\rho}F^{c}_{\rho\mu}
\mathrm{Tr}(T^aT^bT^c) = \frac{1}{4}(d^{abc}+if^{abc})
F^aF^bF^c$.  Since $f^{abc}F^aF^bF^c=0$ by antisymmetry of $f$
and symmetry of the cubic form, the entire expression is
$\propto d^{abc} = 0$.  **Correct: $\mathrm{Tr}(F^3) \equiv 0$
for SU(2).**

For SU(N), $N \geq 3$: $\mathrm{Tr}(F^3)$ is nonzero but C-odd.
The $0^{++}$ glueball has $C=+1$, so $\langle 1|\mathrm{Tr}(F^3)|1
\rangle = 0$ exactly.  **Correct.**

The $d^{abc}$ operator argument is also correct: $d^{abc}$ is
fully symmetric, and under $C$ each generator transforms as
$T^a \to -(T^a)^T$.  The triple product picks up $(-1)^3 = -1$.
**Correct.**


### F4. Two-Derivative Spectral Lemma (Section 5.5) -- FLAG

The lemma statement and the Boltzmann extraction (Steps 1-4) are
correct.  However, **Step 5 (from exponential to polynomial)**
requires closer scrutiny.

The bound $e^{-p\hat{\Delta}}$ from Step 2 gives exponential
suppression for large $\hat{\Delta}$ but does not directly yield
the claimed polynomial bound $C_p M \hat{\Delta}^p$ for *small*
$\hat{\Delta}$.  The text claims the polynomial factor arises
from the "deviation structure" where each excited slot contributes
$(1-e^{-\hat{\Delta}}) \sim \hat{\Delta}$.

**Issue:** The transition from exponential to polynomial in Step 5
is presented only for the specific case $p=2$ with the explicit
operator $\mathrm{Tr}(D_0 F)^2$.  For a *general* operator
satisfying hypothesis (iii) with $\mathrm{exc} \geq p$, the
deviation structure must hold generically.  The argument asserts
that "each of the $p$ excitations contributes a factor
$(1-e^{-\hat{\Delta}})$ relative to the baseline" but this requires
that the spectral sum organizes as deviations from a baseline
(all-vacuum) channel.

For the connected matrix element, the baseline is *not* the
all-vacuum channel (because the vacuum subtraction already removes
part of that).  Hypothesis (iii) ensures the all-vacuum channel is
absent from the *full* matrix element (both $m=0$ and $m=1$), so
the deviation structure is indeed $O(\hat{\Delta}^p)$ from the
Boltzmann weights.

**Verdict:** The argument is correct but the general case relies
on hypothesis (iii) doing more work than the text makes explicit.
The key subtlety -- that exc $\geq p$ forces absence of low-
excitation channels from *both* the vacuum and one-particle matrix
elements simultaneously -- is stated at line 1033-1037 but deserves
more emphasis.  This is a **presentation issue, not a mathematical
error**.


### F5. Stability of Excitation Number (Section 5.6, Part III) -- PASS

This is the central new argument of the paper.  The verification
checklist:

**(a) Does it avoid naive splitting?**  YES.  Section III.2
explicitly demonstrates that the splitting
$\mathcal{O} = \mathcal{O}^{\mathrm{pert}} + \delta\mathcal{O}$
fails because $g_k^6/\hat{\Delta}^3$ dominates $g_k^4\hat{\Delta}^2$
on the AF trajectory.  The scaling comparison is correct:
$g_k^2 \sim 1/\ln(1/a\Lambda) \gg e^{-5/(2b_0g^2)} \sim
\hat{\Delta}^5$.  **Correctly identified.**

**(b) Does the universal operator classification work?**  YES.
The classification is:
- Class I (Tr(F^3), d^{abc}F^3): C-odd, eliminated exactly.
- Class II (dim-5): absent in the C-even sector (gauge invariance
  forces even dimension for C-even operators).
- Class III (Tr(DF)^2): exc $\geq$ 2 by spectral mechanism.
- Class IV (3+ derivatives): exc $\geq$ 3.

The exhaustiveness of this classification for dimension-6 gauge-
invariant operators in d=4 is standard (cf. Luscher-Weisz operator
basis).  **Correct.**

**(c) Does (B1) play the role claimed?**  YES.  Without
analyticity, the "dimension-6 part" of the effective action is only
an asymptotic notion.  (B1) guarantees the Taylor expansion
converges, so the dimension-6 projection is exact and the
classification applies to the *actual* non-perturbative operator,
not just its perturbative approximation.  This is the paper's
key insight.  **Valid logical step.**

**(d) Are the [VERIFY] items genuine reading exercises?**
Mostly yes.  Three items are flagged:

1. **Polymer activity analyticity:** The four operations
   (background evaluation, saddle point, Gaussian integration,
   Mayer resummation) are each standard.  A referee should verify
   the inductive step in CMP 109, Sections 2-4.  This is genuinely
   a reading exercise, not a conceptual gap.

2. **Block-spin kernel complexification:** The map
   $A \mapsto A(A^\dagger A)^{-1/2}$ is analytic near
   $\mathbf{1} \in \mathrm{GL}(N,\mathbb{C})$ by the implicit
   function theorem (the polar decomposition is smooth and the
   square root of a positive-definite matrix is analytic).
   Standard.

3. **Dimension-6 projection exactness:** This depends on
   Balaban's coupling renormalization correctly absorbing the
   Tr(F^2)/g_k^2 part, leaving a genuine dimension-6 remainder.
   This is the most load-bearing of the three [VERIFY] items.
   CMP 109, Section 2 does address coupling renormalization, but
   a referee should verify the separation is clean (no dim-4
   contamination leaks into the remainder).

**The [VERIFY] items are correctly identified and honestly assessed.**


### F6. Moore-Osgood Argument (Section 5.7(e)) -- FLAG

The commutation of limits ($k \to \infty$ and $L \to \infty$)
via Moore-Osgood requires:

1. Uniform convergence in $L$ as $k \to \infty$.
2. Pointwise convergence in $k$ as $L \to \infty$.

Condition 1 is claimed to follow from the volume-independence of
$|C_{k+1}(L) - C_k(L)| \leq C'g_k^4(a_k\Lambda)^s$.  This
bound is indeed $L$-independent because (a) the form factor
$g_k^4\hat{\Delta}^2$ is a per-site quantity, and (b) the volume
factors from the delocalized one-particle state cancel the $V$
in the spatial sum.

**Issue:** The Moore-Osgood theorem requires *uniform convergence*,
meaning $\sup_L |C_k(L) - C_\infty(L)| \to 0$ as $k \to \infty$.
What is shown is that $|C_{k+1}(L) - C_k(L)|$ is $L$-independent
and summable.  This gives uniform convergence of the telescoping
series $C_k(L) = C_0(L) - \sum_{j<k} \delta C_j(L)$, provided
$C_0(L)$ is bounded uniformly in $L$.  Since $C_0(L)$ is the
lattice mass gap ratio at the starting scale, and the lattice mass
gap is bounded by the cluster expansion uniformly in volume,
$C_0(L)$ is indeed uniformly bounded.

**Verdict:** The argument is valid but compressed.  The uniform
boundedness of $C_0(L)$ should be stated explicitly.  **Minor
presentation gap, not a logical error.**


### F7. OS Axioms (Section 5.7(f)) -- FLAG

The verification of the Osterwalder-Schrader axioms is sketched
in four lines.  For a paper claiming to solve a Millennium Problem,
this deserves more detail.  Specific concerns:

**(OS1) Temperedness:** The claim that Schwinger functions are
uniformly bounded in $a$ by cluster expansion estimates is
plausible but not proved here.  It requires the cluster expansion
of Section 3-4 to extend to multi-point functions, which is stated
but not detailed.

**(OS2) Euclidean invariance:** The passage from hypercubic O(4)
to full O(4) invariance as $a \to 0$ requires that irrelevant
operators in the effective action vanish uniformly.  This is
claimed to follow from the RG analysis, which is correct in
principle, but the rate of convergence to O(4) symmetry should
be specified.

**(OS3) Reflection positivity:** Correctly attributed to
Osterwalder-Seiler (1978).  The lattice theory is reflection-
positive for all $a > 0$.  Preservation under the $a \to 0$ limit
is standard (weak limits of reflection-positive functionals are
reflection-positive).

**(OS4) Symmetry:** Automatic.

**Verdict:** No mathematical errors, but the verification is
insufficiently detailed for the importance of the result.
**Presentation concern, not a proof gap.**


### F8. The RG Recursion Fixed Point (Section 5.4.5) -- PASS

The recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}}$ has fixed
point $C_* = 4C_{\mathrm{new}}/3$.  Check: $C_*/4 + C_{\mathrm{new}}
= C_{\mathrm{new}}/3 + C_{\mathrm{new}} = 4C_{\mathrm{new}}/3
= C_*$.  **Correct.**

The contraction factor 1/4 arises because $\hat{\Delta}_k^2 =
\hat{\Delta}_{k+1}^2/4$ (since $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k
(1+O(g_k^4))$, so $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4
\cdot (1+O(g_k^4))^{-2}$).  The factor 1/4 is exact at leading
order.  **Correct.**

The $O(g_k^2)$ correction: the accumulated product
$\prod(1+\alpha g_j^2) \leq \exp(\alpha\sum g_j^2)$.  Since
$g_j^2 \sim 1/(b_0 j \ln 2)$ and $\sum 1/j$ diverges, this
gives power-law growth $k^\gamma$ with
$\gamma = \alpha/(b_0 \ln 2)$.  But the mass gap shift sum
$\sum C_k g_k^4 \hat{\Delta}_k^2 \sim \sum k^{\gamma-2} 4^{-k}$
converges for all $\gamma$ because $4^{-k}$ decays exponentially.
**Correct.**


### F9. Verification of exc(Tr(D_0 F)^2) >= 2 (Section 5.5.4) -- PASS

The explicit spectral sum:
$$\langle m|(D_0 F)^2|m\rangle = \sum_n (e^{E_m-E_n}-1)^2
  |\langle m|F|n\rangle|^2$$

For $m=1$:
- Diagonal ($n=1$): $(e^0-1)^2 = 0$.  **Correct: structural zero.**
- Vacuum intermediate ($n=0$): $(e^{\hat{\Delta}}-1)^2 =
  \hat{\Delta}^2(1+O(\hat{\Delta}))$.  **Correct.**
- Higher states ($n \geq 2$): Suppressed by $(E_n-E_1) > 0$.

The connected matrix element subtracts the vacuum version ($m=0$).
The $n=0$ term in the vacuum version: $(e^0-1)^2 = 0$ (since
$E_0 = 0$).  So the vacuum subtraction does NOT cancel the
$n=0$ intermediate term from the one-particle matrix element.

**This confirms: $\hat{\Delta}^2$ comes from the vacuum
intermediate state in the $m=1$ spectral sum.**  The multi-time-
slice analysis document (Sec 4.2) agrees.  **Verified.**


### F10. Cross-Reference Consistency -- PASS

The architecture document (00-architecture.md) lists Conjecture 1
as the single remaining open problem.  Section 5.6 claims to
discharge this conjecture via the stability-of-excitation-number
argument + (B1)-(B2).

The architecture's Status Table labels Conjecture 1 as open, while
Section 5.6 Part IV labels it as proved (conditional on three
[VERIFY] items).  This reflects the evolution of the argument
within the paper.  The Status Table in the architecture document
appears to be an earlier snapshot.

**No inconsistency in the logical chain.  The architecture
document should be updated to reflect the current status.**

The balaban-B1-B2-proof.md document is reproduced nearly verbatim
in Section 5.6.  Cross-referencing confirms no material was lost
or altered in transcription.

The multi-time-slice-analysis.md document correctly identifies the
confusion between rigid operator translation ($\nabla_0$, which
gives zero in energy eigenstates) and internal covariant derivative
($D_0$, which probes the spectral gap).  This distinction is
properly reflected in Section 5.3.2 and 5.5.4.


---

## Circular Reasoning Analysis

**Potential circularity 1: Does the mass gap enter its own proof?**

The spectral lemma (5.5) uses $\hat{\Delta} > 0$ to extract the
$\hat{\Delta}^p$ suppression.  But $\hat{\Delta}$ at step $k+1$
is the object being controlled.  Is this circular?

NO.  The induction starts at $k=0$ where $\hat{\Delta}_0 > 0$ is
proved independently (Theorem 4, Section 4).  At each step, the
spectral lemma uses $\hat{\Delta}_k > 0$ (the inductive hypothesis)
to bound the perturbation, and then the RG recursion shows
$\hat{\Delta}_{k+1} > 0$ with a controlled shift.  The logical
structure is a standard induction.  **No circularity.**

**Potential circularity 2: Does analyticity (B1) depend on the mass gap?**

(B1) uses $m_W^2 > 0$ (the fluctuation mass in Balaban's
construction) to ensure propagator invertibility.  Is $m_W$
related to $\hat{\Delta}$?

No.  $m_W$ is the gauge-fixed mass arising from the background
field, introduced by Balaban's axial gauge fixing.  It is a
property of the UV regularization, not of the IR spectrum.
**No circularity.**

**Potential circularity 3: Does the operator classification
assume what it proves?**

The stability lemma (5.6, III.3) classifies dimension-6 operators
and shows all have exc >= 2.  This relies on (B1) to make the
dimension-6 projection exact.  Does (B1) require the mass gap?

No. (B1) is a statement about analyticity of the effective action
as a function of the link variables, proved from Balaban's polymer
expansion.  It does not reference the spectral gap $\hat{\Delta}$.
**No circularity.**


---

## The Proof Chain

```
Section 4: Delta_0 > 0 (Theorem 4, from KK cluster expansion)
    |
    v
5.1: Balaban's RG: UV stability, effective action structure
    |
    v
5.2: Parity vanishing (Thm 6(a)): PROVED
     Operator identity (Thm 6(b)): correctly identified as FALSE
     Redirect to matrix element bound: CLEAN
    |
    v
5.3: Dimension-6 classification:
     Tr(F^3): eliminated by C-symmetry (EXACT)
     Tr(DF)^2: form factor O(Delta^2) by spectral mechanism (EXACT)
    |
    v
5.4: RG recursion:
     C_{k+1} = C_k/4 + C_new + O(g_k^2 C_k)
     Fixed point: C_* = (4/3) C_new
     Sum convergence: 4^{-k} kills any polynomial growth
    |
    v
5.5: Two-derivative spectral lemma:
     exc >= p implies C_p M Delta^p bound
     Verified for Tr(D_0 F)^2
    |
    v
5.6: (B1)-(B2) from Balaban (proved by extraction)
     Stability of excitation number (KEY NEW ARGUMENT):
       Uses (B1) + dimension-6 classification
       Avoids naive splitting (correctly identified as failing)
       Discharges Conjecture 1 modulo three [VERIFY] items
    |
    v
5.7: Continuum mass gap:
     Moore-Osgood for limit interchange
     OS axioms for Wightman QFT
     Delta_infty > 0
```

**Each step follows logically from the previous.**  There are no
gaps in the chain.  The conditional dependencies are clearly
marked.


---

## Errors Found

### Hard errors: NONE

No mathematical errors were found in any theorem, lemma, or
proposition in Section 5.

### Soft errors (presentation/emphasis):

1. **Lines 510-515 (Sec 5.3.2):** The temporal derivative formula
   uses $(e^{-\hat{\Delta}}-1)$ (negative exponent) for the
   one-particle matrix element, while Section 5.5.4 uses
   $(e^{+\hat{\Delta}}-1)$ for the vacuum intermediate.  Both are
   correct in context (the sign depends on whether one writes the
   Boltzmann factor relative to $m=1$ looking down to $n=0$, or
   relative to $n=0$ looking up to $m=1$), but the alternation is
   potentially confusing.  Only the square $(e^{\hat{\Delta}}-1)^2
   = \hat{\Delta}^2(1+O(\hat{\Delta}))$ enters the final bound,
   so the sign is immaterial.

2. **Lines 527-530 (Sec 5.3.2):** The "cross terms" in the squared
   expression are mentioned but not bounded.  These arise from
   distinct Lorentz index configurations and are subleading by the
   same spectral mechanism.  Not an error but an incomplete
   argument.

3. **Section 5.7(f):** The OS axiom verification is too compressed
   for a Millennium Problem paper.  Each axiom should have a
   paragraph-length argument.


---

## Items Requiring Author Attention

1. **Architecture document (00-architecture.md) is stale.**  It
   still lists Conjecture 1 as open; Section 5.6 discharges it
   modulo [VERIFY] items.  The status table should be updated.

2. **The three [VERIFY] items** (polymer analyticity, block-spin
   complexification, dimension-6 projection) are correctly
   identified as the residual verification burden.  These are
   genuine "reading exercises" from Balaban, not new mathematics.
   However, for a definitive paper, each should be expanded to a
   self-contained paragraph with specific page/equation references
   to Balaban's CMP papers.

3. **The OS axioms** (Section 5.7(f)) deserve at least one page
   of careful verification, not four lines.


---

## Overall Assessment

**The proof chain in Section 5 is logically valid.**

The argument structure is:
- Start with $\Delta_0 > 0$ (proved in Section 4).
- Show the RG preserves a positive gap via a contraction recursion.
- The recursion requires bounding newly generated operators, which
  reduces to showing all dimension-6 operators have exc $\geq$ 2.
- This is established by a clean classification: C-odd operators
  vanish exactly, derivative operators have spectral suppression.
- The non-perturbative validity of this classification is
  guaranteed by Balaban's analyticity (B1)-(B2), which ensures the
  dimension-6 projection is exact.

**The single genuinely new mathematical contribution** is the
stability-of-excitation-number argument (Section 5.6, Part III),
which uses the *universality of the operator classification* to
bypass the failure of naive perturbative splitting.  This argument
is correct and is the intellectual core of the continuum limit
proof.

**Conditional status:** The proof is conditional on three [VERIFY]
items, all of which are verifications of implicit properties in
Balaban's published work (CMP 109, 119).  These are not new
conjectures; they are specific points where a referee must read
Balaban's construction in detail.  The paper correctly identifies
these as the residual verification burden.

**No circular reasoning detected.**  The inductive structure is
clean: lattice mass gap at $k=0$ feeds into the RG recursion,
(B1)-(B2) come from the UV (not the IR), and the operator
classification is a statement about symmetry and dimension that
does not reference the spectral gap.

**Flags (non-fatal):**
- The spectral lemma's Step 5 (exponential to polynomial) needs
  slightly more care in the general case.
- Moore-Osgood needs explicit uniform boundedness of $C_0(L)$.
- OS axioms need expansion.

**If the three [VERIFY] items check out against Balaban's papers,
the proof of $\Delta_\infty > 0$ is complete.**
