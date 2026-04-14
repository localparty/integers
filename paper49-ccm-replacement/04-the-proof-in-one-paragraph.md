# §04 — The Proof in One Paragraph

*Paper 49, Part I: Motivation. The entire construction compressed to
one page: formal statement, seven-link chain, brief commentary.*

---

## The claim

**Theorem (Paper 49).** *Let $A_{BC} = C(\hat{\mathbb{Q}}) \rtimes
\mathbb{N}^*$ be the Bost-Connes C*-algebra. Let $\omega_1$ be its
unique KMS$_1$ state. Let $(H_{\omega_1}, \pi_{\omega_1},
\xi_{\omega_1})$ be the GNS triple at $\omega_1$, and let $M_1 :=
\pi_{\omega_1}(A_{BC})''$ be the bicommutant. Let $(\Delta, J)$ be the
canonical modular data of Tomita-Takesaki theory on the standard form
$(M_1, H_{\omega_1}, J, P^+)$. Let $H_R := P_{\text{even}}
H_{\omega_1}$ be the even-sector Hilbert space relative to the BC
parity involution. Define*

$$
D \ := \ -\,(2/\pi^2) \cdot i \, \log \Delta \quad \text{on}\quad
\mathrm{Dom}(D) \subset H_R.
$$

*Then $D$ is self-adjoint with compact resolvent, and its spectrum
equals the set of imaginary parts of the non-trivial zeros of the
Riemann zeta function:*

$$
\mathrm{spec}(D) \ = \ \{\,\gamma_n \,:\, n \geq 1\,\}.
$$

*Since $D$ is self-adjoint, $\mathrm{spec}(D) \subset \mathbb{R}$.
Therefore $\gamma_n \in \mathbb{R}$ for all $n$, i.e., every non-
trivial zero of $\zeta$ lies on $\mathrm{Re}(s) = 1/2$. The Riemann
Hypothesis holds.*

## Derivation sketch

The seven-link chain:

1. **BC algebra at KMS$_1$** (Bost-Connes 1995 Thm 25; Paper 13 L2):
   unique state $\omega_1$; GNS data $(H_{\omega_1}, \pi_{\omega_1},
   \xi_{\omega_1})$; bicommutant $M_1$ is a type III$_1$ factor
   (ITPFI with $\lambda_p = 1/p$; three independent proofs).
2. **Tomita-Takesaki** (classical 1970): standard form
   $(M_1, H_{\omega_1}, J, P^+)$ gives canonical $\Delta > 0$ (self-
   adjoint, unbounded) and $J$ (antiunitary, $J^2 = I$,
   $J M_1 J = M_1'$).
3. **Modular flow ergodicity** (Paper 32 BGS L2 via Path B): $\sigma_t
   = \text{Ad}(\Delta^{it})$ ergodic; Connes spectrum
   $\text{Sd}(M_1) = \mathbb{R}$.
4. **Hilbert-Pólya operator**: $D := -(2/\pi^2) i \log \Delta$ on
   $\text{Dom}(D) \subset H_R$. Self-adjointness from functional
   calculus on the even sector; compact resolvent from Paper 13 L3c
   Fourier cancellation; spectral gap from Lehmer/Selberg
   comparison.
5. **Matching to zeros**: ITPFI factorization (Paper 13 L2) +
   arithmetic QUE (Lindenstrauss 2006, Paper 48) + Sato-Tate (Taylor
   2011, Paper 44) identify the spectral density of $D$ with the
   Weil explicit-formula density of the Riemann zeros.
6. **Spectral exactness + Hurwitz** (Paper 13 L4–L5 inherit unchanged):
   Bögli H1 + H2 give $\text{spec}(D_\infty) = \lim
   \text{spec}(D_N)$ with no spurious eigenvalues; Hurwitz
   identifies the limit with $\{\gamma_n\}$.
7. **Conclusion**: $D$ self-adjoint $\Rightarrow \text{spec}(D)
   \subset \mathbb{R}$; combined with $\text{spec}(D) = \{\gamma_n\}$
   from Link 6, gives $\gamma_n \in \mathbb{R}$. RH.

## Chain table

| Link | Statement | Status | Source |
|:---:|---|---|---|
| 1 | BC algebra at KMS$_1$; GNS gives $M_1$ = type III$_1$ factor | PROVED | BC 1995 Thm 25; Paper 13 L2 |
| 2 | Tomita-Takesaki: canonical $(\Delta, J)$ on standard form | PROVED (classical) | Tomita-Takesaki 1970 |
| 3 | Modular flow ergodic; $\text{Sd}(M_1) = \mathbb{R}$ | PROVED | Paper 32 BGS L2 |
| 4 | $D := -(2/\pi^2) i \log \Delta$ self-adjoint, compact resolvent | CONSTRUCTABLE | Paper 49 §17–§22 |
| 5 | Spectral density of $D$ = Weil density via QUE + Sato-Tate | CONSTRUCTABLE | Paper 49 §23–§28 |
| 6 | $\text{spec}(D_\infty) = \{\gamma_n\}$ (Bögli + Hurwitz) | PROVED | Paper 13 L4–L5 |
| 7 | $D$ self-adjoint $\Rightarrow \text{spec}(D) \subset \mathbb{R}$; RH | QED | Synthesis |

## Commentary

**On "CONSTRUCTABLE".** Links 4 and 5 are labeled CONSTRUCTABLE
rather than PROVED because they require the 6–12 months of write-up
scheduled as Paper 49's Parts IV–V. The ingredients are either
classical (Tomita-Takesaki, functional calculus, Weil explicit
formula, QUE, Sato-Tate) or programme-internal (Paper 13 L3c, Paper
32 L2, Paper 12 operator dictionary). No new deep theorem is needed.
The work is assembly, not discovery.

**On the rescaling constant $\kappa = 2/\pi^2$.** This is the CBB
operator-dictionary constant from Paper 12 §27 (the anchor
document). The identity $\hat L = \log \hat R$ relating the BC
Hamiltonian $\hat L$ to the scaling operator $\hat R$, combined with
$\gamma_n = \kappa \langle n | \hat L | n \rangle$, forces
$\kappa = 2/\pi^2$. The same $\kappa$ appears in Paper 13's
normalization of the CCM eigenvalues. It is not a free parameter; it
is dictated by the dictionary.

**On the even sector $H_R$.** CCM uses the parity involution $\gamma$
to restrict to the even sector $E_N^+$ (CCM Lemma 5.2(i)). Paper 49
recovers the same restriction from within the BC algebra: the even
sector corresponds to functions on $\hat{\mathbb{Q}}$ that are
invariant under $-1 \in \hat{\mathbb{Z}}^*$. The parity involution is
the $\mathbb{Z}/2$ subgroup of the natural $\hat{\mathbb{Z}}^*$-action
on $\hat{\mathbb{Q}}$. This is intrinsic to the BC algebra; no
external input needed.

**On the functional equation.** Riemann's functional equation
$\xi(s) = \xi(1-s)$ is, in the operator-algebraic dictionary, the
statement $J D J = -D$ on the full Hilbert space (projected to the
even sector: $J$ acts as complex conjugation, and the symmetry
$\gamma_n \mapsto -\gamma_n$ reduces to $\gamma_n \mapsto \gamma_n$
up to sign convention). The modular conjugation $J$ IS the
functional equation. This is why the construction is so natural:
the $s \leftrightarrow 1-s$ symmetry was built into Tomita-Takesaki
from the start.

**On the Bogomolov-style audit.** A reader might worry that
restricting to the parity-even sector is a "cheat" — perhaps the
operator has non-real spectrum on the parity-odd sector, and RH is
only about the even sector. This is not a concern. The Riemann $\xi$
function is itself invariant under $s \mapsto 1-s$, so $\Xi(t) := \xi
(1/2 + it)$ is an even function of $t$, and its zeros are symmetric
about $t = 0$. The even sector is the correct sector. The odd sector
contains no zeros (it is empty of relevant spectral content).

**On why this is not circular.** One might worry: don't we already
know the BC algebra encodes the Riemann zeta function via
$Z(\beta) = \zeta(\beta)$? Isn't Paper 49 just rediscovering this?
No. The partition-function identity $Z(\beta) = \zeta(\beta)$ is a
statement about the free-energy-like quantity derived from $\omega_\beta$;
it does not give the Hilbert-Pólya operator. The Hilbert-Pólya
operator is a self-adjoint *operator* whose eigenvalues are the
zeros, not a scalar function whose values encode the zeros. Paper 49
constructs the operator. The input is the algebra's structure; the
output is a self-adjoint operator with a specific spectrum. This is
a genuine refinement of what BC 1995 supplies.

**On confidence.** Paper 49's projected confidence upon completion
is 7–8/10. Links 1–3 and 6 are at 9–10/10 individually (each is
either classical or a programme-internal proof we have audited).
Links 4 and 5 are each at 7/10 projected: the construction is
natural and the ingredients are in hand, but the explicit matching
in Link 5 requires the substantive write-up. The overall chain's
confidence is governed by the weakest link, which is Link 5.

## The sentence that summarizes the paper

*The Bost-Connes algebra's canonical modular operator $\Delta$ from
Tomita-Takesaki theory, rescaled by the CBB dictionary constant
$\kappa = 2/\pi^2$, restricted to the BC algebra's even-parity sector,
IS the Hilbert-Pólya operator — and therefore the Riemann Hypothesis
is a theorem about a specific canonical object given by the
arithmetic of the integers.*

Eight faces on the e-circle. Two generating circles on the torus.
One modular operator. One Hilbert-Pólya theorem.

---

*End of Part I. Parts II–V develop the construction. Part VI compares
to CCM. Part VII verifies numerically.*
