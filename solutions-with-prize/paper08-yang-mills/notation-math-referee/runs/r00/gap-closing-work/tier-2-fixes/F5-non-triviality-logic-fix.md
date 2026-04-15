# Gap F5 — Non-triviality logic fix for §5.7(f) Proposition

## 1. Statement of the gap

The Proposition (Non-triviality) in §5.7(f) (`05-continuum-limit.md`
L2593–2719) lists three signatures that the constructed continuum
Yang–Mills theory is not Gaussian:

- **(i)** positive string tension, $\sigma > 0$;
- **(ii)** non-vanishing connected 2-point function with
  $|\langle 1|s_P|0\rangle|^2 > 0$;
- **(iii)** asymptotic freedom, $b_0 = 11N/(48\pi^2) > 0$.

The closing line at L2709 says "*Any one of (i) or (ii) alone suffices to
establish non-triviality*". **This is wrong.** A free massive scalar has a
non-vanishing 2-point function (Källén–Lehmann with a delta at the pole),
so (ii) does not exclude the Gaussian case. Only (i) and (iii) genuinely
distinguish the constructed theory from any free theory. The Remark at
L2711–2718 repeats the mistake: "*the 2-point bound (ii) already excludes
the Gaussian case*" is false. (Note also that the body of (ii) is
*mis-headed* — L2605 reads "Non-vanishing connected 4-point function"
but the argument produces only a 2-point bound. That mislabel should be
fixed alongside the logic correction.)

## 2. Corrected Proposition (Non-triviality)

**Proposition (Non-triviality, corrected).** *The continuum Yang–Mills
theory constructed in §5.7 is not isomorphic to a free (Gaussian) quantum
field theory. Any one of the following signatures suffices:*

- *(i) Positive string tension: $\sigma > 0$ (Theorem 4, §4.4).*
- *(iii) Asymptotic freedom: $b_0 = 11N/(48\pi^2) > 0$ (Balaban inner
  RG, §5.1.2 and §5.5).*

*Signature (ii) — the lower bound $|\langle 1|s_P|0\rangle|^2 > 0$ on the
lightest-glueball matrix element, derived in §5.7(f) by strong-coupling
variance + spectral contradiction + Kato analyticity — is auxiliary
information about the overlap of the plaquette operator with the lightest
glueball. It is **not** sufficient on its own to exclude the Gaussian case:
a free massive scalar has non-vanishing 2-point $\langle\phi(x)\phi(y)\rangle$.
(ii) is needed for the §5.7(f) OPE / matrix-element analysis and for G4,
not for non-triviality.*

## 3. Why (i) and (iii) each suffice

**(i) String tension ⇒ non-Gaussian.** In any free (Gaussian) gauge theory,
Wilson loops obey a *perimeter law*: $\log\langle W_C\rangle = -\tfrac{1}{2}
\oint_C\oint_C G(x-y)\,dx\cdot dy$ with $G$ the free propagator, dominated
by the coincidence singularity and scaling with perimeter $P(C)$, not area
(Seiler 1982 Ch. 3; Fradkin–Susskind PRD 17, 1978). Hence $\sigma = 0$ for
every free theory. Theorem 4 establishes $\sigma > 0$ for the constructed
theory, which is therefore not Gaussian. This rules out not only free
Yang–Mills but *every* Gaussian QFT in whose algebra Wilson loops are
definable.

**(iii) Asymptotic freedom ⇒ non-Gaussian.** A free (Gaussian) theory has no
running coupling: its $n$-point functions are fixed by the quadratic action,
and the one-loop $\beta$-function coefficient is $b_0 = 0$. Balaban's inner
RG, propagated through §5.5, gives $b_0 = 11N/(48\pi^2) > 0$ uniformly
along the AF trajectory (Gross–Wilczek PRL 30, 1973; Politzer PRL 30, 1973;
Balaban CMP 109). Logarithmic running $g_k^2 \sim 1/(b_0 k\ln 2)$ is
incompatible with any Gaussian theory, so the constructed theory is
non-Gaussian. Unlike (i), (iii) depends on the continuum-limit RG
trajectory itself, so it rules out even contrived "effective Gaussian"
theories with non-trivial Wick-ordered 2-points that could conceivably
fake (ii).

## 4. Corollary: connected $n$-point functions for $n\geq 4$

Although the proof does not explicitly construct a non-zero connected
4-point function, the combination $(\sigma > 0)$ + exponential clustering
(Theorem 2 of §4.3) + OS reconstruction + reflection positivity forces its
existence:

**Corollary F5.1.** *The constructed continuum theory has at least one
non-zero connected $n$-point function of Wilson loops with $n \geq 4$.*

*Sketch.* If all connected Wilson-loop $n$-point functions for $n \geq 3$
vanished, the Wilson-loop algebra would be Gaussian. Combined with
reflection positivity (Lemma D.2) and OS reconstruction, this would force
the reconstructed theory to be free. A free gauge theory has perimeter law,
$\sigma = 0$, contradicting Theorem 4. Charge conjugation $U \to U^*$
forbids odd $n$ in the pure-glue sector, so some $n \geq 4$ connected
function is non-zero. $\square$

This is consistent with the Jaffe–Witten C2 criterion ("*Some connected
$n$-point with $n \geq 4$ shown nonzero, or interacting S-matrix*"), but
the existence is *indirect* — obtained from area law + clustering, not
from an explicit lattice bound. An explicit construction of a non-zero
connected 4-point function (e.g., by lower-bounding the cluster expansion's
4-point Wilson correlator by a positive quantity) would promote this to
an effective C2 statement and is a candidate Tier-3 strengthening.

## 5. Textual edits

- L2605 header: "Non-vanishing connected 4-point function" → "Non-vanishing
  connected 2-point function with lower-bounded lightest-glueball matrix
  element".
- L2709: "Any one of (i) or (ii) alone suffices" → "Any one of (i) or (iii)
  alone suffices; (ii) is auxiliary and insufficient on its own — a free
  massive scalar has non-zero 2-point".
- L2711–2718 ("Remark (Connected 4-point function)"): replace with
  Corollary F5.1 above. Delete "*the 2-point bound (ii) already excludes
  the Gaussian case*".

The logical content of the §5.7(f) argument for $|\langle 1|s_P|0\rangle|^2
> 0$ (Haar variance + spectral contradiction + Kato analyticity) is
preserved; only its *interpretation* changes: matrix-element information
for the OPE and G4 analyses, not a non-triviality signature.
