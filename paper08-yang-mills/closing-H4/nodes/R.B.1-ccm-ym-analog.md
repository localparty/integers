# R.B.1 — CCM 2025 spectral triple port to Yang-Mills (W1-B1 Author output)

*Author: W1-B1 (transposition-mode). Cycle 1, Wave 1. Node R.B.1 on
Route B of the H4 closure programme for Paper 8.*

*Status: **BLOCKED-DECOMPOSED**. The structural transposition is
well-defined and produces a coherent YM analog operator
$(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$, but the load-bearing
"UV asymptotics match perturbation theory by construction" claim in
the brief does **not** correspond to anything CCM 2025 actually
proves. The transposition reframes H4 rather than closes it.*

---

## Direction

Execute the transposition-mode 6-step inner loop on Route B's root
node R.B.1: port the Connes–Consani–Moscovici (2025) zeta spectral
triple $(D_{\log}^{(\lambda,N)}, E_N^+)$ from Paper 13 RH to Paper 8
Yang-Mills, with the Riemann-zero target data replaced by the
gradient-flow Wilson coefficient $c_1(t)$ and the associated
perturbative short-distance structure. Deliver a transposition
dictionary, a concrete description of the YM analog operator, a
statement of the analog self-adjointness mechanism, and a verdict on
whether the port provides H4 as a structural consequence or merely
repackages it. Use **I-7 backward-verification** discipline against
the CCM arXiv paper itself: do not trust the brief's paraphrases.

---

## Framework tools used

**Always (per anchor doc)**
- `paper12/research/214-the-method-six-patterns.md` (end-to-end, 339
  lines).
- `paper12/27-anchor-document.md` (end-to-end, 426 lines).
- `paper12/relaxation/04-geometric-spectral-cross-formula-...-strategy.md`
  §6 (Constraint 5: CCM 2025 timeline-independent confirmation) and
  §9 (Paper 10/Yang-Mills fragility), selective per I-9.

**Transposition-mode (selective per I-9)**
- `paper12/research/14-transposition-CCM-and-reasoning-patterns.md`
  §A.1–A.4 (what Identity 14 actually asserts and what is
  rigorous/conditional in the CCM ↔ BC intertwining) and §B.1 (the
  uniform transposition rule additive ↔ multiplicative). Not read
  end-to-end; the "CCM → YM" sub-section explicitly does not exist in
  this file — the transposition methodology is RH-side, not YM-side.
- `paper13-rh/preprint/00-proof-skeleton.md` (end-to-end, 234 lines
  of actual content) — the six-layer CCM/ITPFI/Boegli/Hurwitz proof
  skeleton, shape the YM port must produce to close H4.
- `paper13-rh/preprint/sections-06-10.md` §6 (eigenvector
  approximation, lines 1–240), §7 (uniform $H^1$ regularity, lines
  242–399), §8 (continued-fraction uniform decay, lines 401–514),
  §9 (Teschl-Boegli synthesis, lines 516–692), §10.3–10.4 (Hurwitz
  eigenvalue identification + the RH deduction, lines 780–896).
  Selective via grep for §6/§7/§8/§9/§10 — NOT end-to-end.
- **`paper13-rh/sources/ccm-zeta-spectral-triples-2025.pdf`** (CCM's
  own preprint, local copy at paper13-rh/sources). Pages 1–5
  (Abstract, Introduction, Theorem 1.1, §§2–3 Weil quadratic form
  setup); pages 14–20 (§4.3 $W_\mathbb R$ matrix, §5 "The infrared
  spectral triples", §5.1–5.4 truncation and perturbed scaling
  operator construction, Prop 5.7 existence and uniqueness); pages
  21–28 (§5.5–5.6 regularized determinant, Theorem 5.10, §6
  Numerical results, §7 Outlook). **This is the I-7 backward
  verification source.** Paraphrases of CCM 2025 in the brief, the
  blackboard §D, and even in paper13-rh's §6 were checked against
  this primary source.

**Load-bearing for H4 / target context**
- `paper08-yang-mills/preprint/PROOF-CHAIN.md` (end-to-end) — 18
  steps, Step 18 the sole `[KEY LEMMA — OPEN]` and `Conditional on
  H4`.
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4b-af-short-distance-match.md`
  (end-to-end, 157 lines) — the precise statement of the AF
  short-distance matching gap and Hypothesis H4.
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4d-operator-product-expansion.md`
  (end-to-end, 176 lines) — the OPE structural gap and its
  collapse under H4.
- `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md`
  §1 (gradient-flow running coupling $\bar g_{\mathrm{GF}}^2(q)$,
  definition 1.2), §2 (small-flow-time expansion, the Wilson
  coefficient $c_1(t) = 1/(8\pi^2 t^2)[1 + \bar c_1 \bar g^2(q) +
  \cdots]$, eq 2.2; the AF-predicted two-point function, eq 2.5),
  §3 (Reisz power counting), §4 (Hypothesis H4 verbatim statement),
  §5 (the reframing of H4 as a Taylor-coefficient identification on
  an analytic $F(t)$), §6 (KK tower protection).
- `paper08-yang-mills/closing-H4/blackboard.md` §A–§D and §E (the
  plan tree, the canonical §D toolkit entries).

**Canonical example**
- `paper26-bsd/strategy/05-route3-kms-projector-bypass.md`
  (end-to-end, 456 lines). This is the BSD MY4 Route 3 closure via
  G's KMS projector $P_k^{\mathfrak p} := I - e_{\mathfrak p^k}$ —
  the canonical ORA-produced structural bypass, and a direct
  structural analog: **there, the bypass observation was that §§7–8
  of Paper 26 were already algebraic and MY4 was never load-bearing**.
  The same "is it really load-bearing?" question applies here to
  the brief's "UV asymptotics match by construction" claim.

---

## Source framework recap (CCM 2025 / Paper 13 §6)

*Primary source: Connes–Consani–Moscovici, "Zeta Spectral Triples",
arXiv:2511.22755v1 (27 Nov 2025), local copy at
`paper13-rh/sources/ccm-zeta-spectral-triples-2025.pdf`. Verified
page-by-page per I-7 discipline.*

**The CCM 2025 construction** (CCM §5, pages 15–20):

1. **Ambient space.** $\mathcal H_\lambda := L^2([\lambda^{-1},
   \lambda], d^*u)$ with $d^*u = du/u$, the invariant measure for
   multiplicative dilations. Here $\lambda > 1$ is a bandwidth
   parameter; set $L := 2\log\lambda$.

2. **Unperturbed scaling operator.** $D_{\log}^{(\lambda)} := -iu
   \partial_u = -i\partial/\partial\log u$ on $\mathcal H_\lambda$
   with periodic boundary conditions (CCM eq. 5.14).

3. **Orthonormal basis.** $V_n(u) := U_n(\log\lambda u)$ for $|n|
   \le N$, where $U_n(x) := L^{-1/2}\exp(2\pi i n x/L)$ (CCM eq.
   2.6, 3.21). The truncated space is $E_N := \mathrm{span}\{V_n :
   |n| \le N\}$, a $(2N+1)$-dimensional subspace.

4. **Weil quadratic form.** $QW_\lambda^N$ is the restriction of
   the Weil quadratic form (built from Weil's distribution $\mathcal
   D = \log_*(\Psi^\sharp)$ encoding the Riemann–Weil explicit
   formula at the primes $p \le \lambda^2$) to $E_N$. Its matrix
   elements in the $V_n$ basis (CCM §5.1 eq. 5.1, Lemma 5.1) have
   the Cauchy form $\tau_{i,j} = (b_i - b_j)/(i-j)$ for $i \ne j$,
   $\tau_{i,i} = a_i$.

5. **The $\mathbb Z/2$-grading $\gamma$.** $\gamma(V_j) := V_{-j}$
   on $E_N$. Since $q_{-i,-j} = q_{i,j}$, $T := QW_\lambda^N$
   commutes with $\gamma$: $T\gamma = \gamma T$ (CCM Lemma 5.2(i)).
   This is load-bearing for the even-sector restriction.

6. **Even-simple hypothesis.** $T$ is **even-simple** if its
   smallest eigenvalue is simple and the corresponding eigenvector
   $\xi$ satisfies $\gamma\xi = \xi$ (CCM Definition 5.3). This
   says the minimal eigenvector lies in the $+1$ eigenspace of
   parity.

7. **The rank-one perturbation (Lemma 5.4).** Assume $T \ge 0$ and
   $\ker T = \mathbb C\xi$. Let $D$ be the diagonal operator
   $D(V_n) := n V_n$. One computes (CCM eq. 5.3) $DT - TD =
   |\beta\rangle\langle\eta| - |\eta\rangle\langle\beta|$ with
   $\beta := \sum b_j V_j$, $\eta := \sum V_j$. Define the **rank-one
   perturbation**
   $$
   D' := D - |D\xi\rangle\langle\eta|.
   $$
   Then $D'$ induces a self-adjoint operator $D''$ on the quotient
   Hilbert space $\mathcal H := E_N/\mathbb C\xi$ with the new inner
   product $\langle f|g\rangle_T := \langle Tf|g\rangle$ (which is
   positive-definite after quotienting by $\ker T$).

8. **The infrared spectral triple (Proposition 5.7, Theorem 5.10).**
   Under the even-simple hypothesis, there exists a unique operator
   $D_{\log}^{(\lambda,N)}$ with the same domain as
   $D_{\log}^{(\lambda)}$ which agrees with $D_{\log}^{(\lambda)}$
   on $\ker(\delta_N)^\perp = E_N^\perp$ and is the $D''$-extension
   on $E_N^+ := \{\xi_N\}^\perp$ inside $E_N$. The operator is
   **self-adjoint** in the direct sum $E_N' \oplus E_N^\perp$ with
   the modified inner product, and its spectrum is real.

9. **The fundamental identity (Theorem 5.10(ii)–(iii)).** The
   regularized determinant satisfies
   $$
   \det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i\,
   \lambda^{-iz}\,\widehat\xi(z),
   $$
   where $\widehat\xi(z) = 2L^{-1/2}\sin(zL/2)\sum_{j=-N}^N \xi_j/
   (z - 2\pi j/L)$ is the Fourier transform (for the duality
   $\langle\mathbb R^*_+|\mathbb R\rangle$) of the minimal
   eigenvector $\xi$. **The zeros of $\widehat\xi$ coincide with
   the spectrum of $D_{\log}^{(\lambda,N)}$, and they are real.**

10. **The §7 Outlook conjecture (the "strategy towards RH").** As
    $N,\lambda \to \infty$, the functions $\widehat\xi_\lambda(z)$,
    suitably normalized, converge uniformly on closed substrips of
    $|\mathrm{Im}(z)| < 1/2$ to the Riemann Xi function $\Xi$. By
    Hurwitz, eigenvalues converge to $\{\gamma_n\}$. **CCM state
    verbatim (p. 28): "Justifying rigorously this step is the main
    remaining obstacle to our approach to RH."** Paper 13
    (`sections-06-10.md` §6 Estimate b + §9 Teschl-Boegli + §10
    Hurwitz) is the synthesis that closes this obstacle.

**Critical clarification after primary-source read**: CCM 2025
itself is an **existence/numerical** construction, not a closed
proof of RH. The spectrum of $D_{\log}^{(\lambda,N)}$ is real by
self-adjointness (Theorem 5.10(i)+(iii)), and numerically it agrees
with $\{\gamma_n\}$ to $10^{-55}$ for the first zero at $N=120$. The
*identification* with $\{\gamma_n\}$ requires the §7 Outlook
convergence step, which is open inside CCM 2025 and is what paper13
closes via ITPFI + Boegli + Hurwitz. There is **no** statement in
CCM 2025 about "UV asymptotics matching perturbation theory by
construction" — that language is entirely a paraphrase from the
blackboard §D / brief.

---

## Research

### Step 1 — DIAGNOSE (source + target)

**Source loop-closure mechanism (RH side).** The "loop" in paper13's
closure of RH via CCM is:

- CCM provides $D_{\log}^{(\lambda,N)}$, a self-adjoint operator
  whose eigenvalues are the zeros of $\widehat\xi_\lambda$ (CCM
  Thm 5.10(iii) — a **constructive identity**, not an
  approximation).
- The eigenvectors of the Weil quadratic form $QW_\lambda^N$ at
  smallest eigenvalue are conjecturally approximated by prolate
  wave functions $k_\lambda$, and $\widehat k_\lambda \to \Xi$
  uniformly (CCM §7 Outlook, Lemma 7.3 in paper13's numbering).
- Paper 13 **fills the gap** between "eigenvalues = zeros of
  $\widehat\xi_\lambda$" and "zeros of $\widehat\xi_\lambda$ =
  Riemann zeros" via ITPFI state convergence + Teschl-Boegli
  spectral exactness + Hurwitz zero convergence.

The "invariant that protects the UV/high-frequency match" on the
RH side is: the **Fourier transform of the minimal eigenvector of
the Weil quadratic form equals (in the limit) the Riemann Ξ
function**. This is a structural identity that ties the infrared
(smallest eigenvalue of $QW_\lambda^N$) to the entire
analytic-continuation structure of $\zeta$. "UV asymptotics" are
not really in the picture here at all. The RH closure is an
**infrared** construction, and the high-frequency limit
($\lambda \to \infty$, equivalent to more primes in the Euler
product truncation) is controlled by CCM's Carathéodory-Fejér decay
$\rho \ge 4.27$ that makes the rank-one perturbation data vanish
super-exponentially in $N$ (paper13 §8, eq. 8.4, $\rho_\Delta \ge
4$ analytically).

**Target loop-closure mechanism (YM side).** What would a YM port
have to close?

- Step 18 of the Paper 8 proof chain is: $S_2^{\mathrm{ren}}(x,y)
  \sim C_N|x|^{-8}(\log 1/|x|\Lambda)^{-2}$ as $|x-y| \to 0$
  (Conjecture L.2 / Lemma 4.2 in W7-14).
- This reduces (per W7-14 §5) to the identification of Taylor
  coefficients of an analytic function $F(t) := S_{2,t}^c(x,y)/
  c_1(t)^2$ at $t = 0^+$, where $c_1(t)$ is the leading Wilson
  coefficient of the small-flow-time expansion (W7-14 eq. 2.2).
- The **target invariant** is: the leading Taylor coefficient
  $F(0)$ equals the tree-level free-field Wick contraction
  coefficient $C_N = 2(N^2-1)/\pi^6$, and the next-to-leading
  coefficients carry the AF logarithms via the trace-anomaly
  identity $\gamma_{\mathrm{Tr}F^2}(g) = -2\beta(g)/g$ (W7-14 eq.
  2.3).

**The analog question**: Is there a self-adjoint operator
$D_N^{\mathrm{YM}}$ on a gradient-flow-eigenfunction Hilbert space
$E_N^{\mathrm{YM},+}$ whose "Fourier transform of minimal
eigenvector" identity (the CCM Thm 5.10(iii) analog) reproduces
$F(t)$ as a function of $t$, with self-adjointness of the spectrum
forcing the Taylor coefficients at $t=0$ to be real and matching
the perturbative values?

*Diagnosis*: **The analogy is not tight**. The CCM construction
produces a self-adjoint operator whose **spectrum** is the target
data (Riemann zeros). The analogous YM structure would want the
target data to be the Taylor coefficients $\{F^{(k)}(0)\}$ of an
analytic function, or equivalently the Wilson coefficients $\{c_k\}
$ of the small-flow-time expansion. These are **not spectra** —
they are coefficients of an analytic function. Forcing them into a
spectral form requires an additional structural choice.

### Step 2 — REINTERPRET (source + target)

**Source reinterpretation.** Paper13's RH closure lives in the
Hilbert space $E_N^+ \subset L^2([\lambda^{-1},\lambda], d^*u)$, the
**even sector** of the truncated scaling-operator space. "Even"
means invariant under $u \mapsto u^{-1}$, equivalently under the
parity involution $\gamma: V_j \mapsto V_{-j}$. This is natural for
the Weil quadratic form because the explicit formula
$\sum_\rho \tilde f(\rho) = \int f + \int f^\sharp - \sum_v
\mathcal W_v(f)$ (CCM eq. 3.2) is symmetric under $f \leftrightarrow
f^\sharp$, with $f^\sharp(u) := u^{-1}f(u^{-1})$.

**Target reinterpretation.** What "space" does the YM analog live
in? The candidates, ordered by structural fidelity:

**Candidate A — Gradient-flow eigenfunction space $E_N^{\mathrm{YM},
+}$ (the brief's tentative proposal).** Let $\mathcal H_{\mathrm{GF}}
:= L^2((0,T], dt/t)$ for some bandwidth $T$ (the analog of
$\lambda$), with $dt/t$ being the natural scale-invariant measure
on flow time. The unperturbed "scaling operator" is $D_{\log
t}^{(T)} := -i\partial/\partial\log t$. An orthonormal basis
consists of $W_n(t) := L^{-1/2}\exp(2\pi i n \log t / L)$ with
$L := 2\log T$, $|n| \le N$. This is a **direct structural port**
of CCM's $V_n$ basis. The "even sector" is invariant under
$t \mapsto T^2/t$ (the natural involution fixing the "midpoint"
$t = T$ in log-scale).

**Candidate B — Small-flow-time Taylor space.** The Taylor
coefficients $F^{(k)}(0)$ of the analytic function $F(t)$ at
$t=0^+$ form a natural sequence. The "operator" is the formal
shift $k \mapsto k+1$; the "spectrum" is the AF-predicted values.
This is **not** a spectral triple — there is no ambient $L^2$ space
and no modular involution. Discard.

**Candidate C — Gluon-field momentum space (Fourier of flowed
correlator).** $\mathcal H_{\mathrm{YM}} := L^2(\mathbb R^4, d^4p)$
with the momentum-space Fourier transform of the flowed two-point
function $\widehat{S_{2,t}^c}(p)$. The analog of
$\widehat\xi_\lambda = \Xi$ identity would be a statement of the
form "$\widehat{(\text{minimal eigenvector of } Q_N^{\mathrm{YM}})}(p) =
F^{\mathrm{pert}}(p)$ at short distances by construction". This is
closer in spirit but fails the transposition discipline: the
self-adjointness of $D_N^{\mathrm{YM}}$ on this space does not force
the perturbative Wilson coefficients.

**Selected**: Candidate A, with explicit acknowledgment that the
natural parameter is not "momentum" (as in CCM's scaling operator
on $[\lambda^{-1},\lambda]$) but "logarithmic flow time"
$\log t$. The analog of the bandwidth $\lambda$ is $T^{1/2} = $ the
UV cutoff flow time (small-$T$ = far UV). The analog of the Weil
quadratic form is the **Luscher-Weisz small-flow-time quadratic
form** arising from the Cauchy estimate on $F(t)$.

### Step 3 — UNIFY (source instance + target instance)

**Source instance.** $(D_{\log}^{(\lambda,N)}, E_N^+, QW_\lambda^N,
\gamma)$ — the CCM 2025 zeta spectral triple with its even-simple
Weil quadratic form, $\mathbb Z/2$-grading by $u \mapsto u^{-1}$,
Cauchy matrix structure of Weil's distribution, and rank-one
perturbation closing the self-adjointness loop. Framework: Connes
noncommutative geometry, specifically the "infrared spectral
triple" genre of Connes-Moscovici-Consani 2019/2024/2025.

**Target instance (proposed).** $(D_N^{\mathrm{YM}},
E_N^{\mathrm{YM},+}, Q_N^{\mathrm{YM}}, \gamma^{\mathrm{YM}})$ — the
proposed gradient-flow spectral triple, defined as follows:

- **Ambient Hilbert space.** $\mathcal H_T^{\mathrm{GF}} :=
  L^2([T^{-1}, T], dt/t)$ for bandwidth $T > 1$ (UV-side:
  $t \to T^{-1}$ = short flow time = far UV; IR-side: $t \to T$ =
  large flow time = IR smearing scale $\sqrt{8t}$). Set
  $L^{\mathrm{YM}} := 2\log T$.

- **Unperturbed scaling operator.** $D_{\log t}^{(T)} :=
  -it\partial_t = -i\partial/\partial\log t$ on
  $\mathcal H_T^{\mathrm{GF}}$, with periodic boundary conditions
  (the flow-time analog of CCM eq. 5.14).

- **Orthonormal basis.** $W_n(t) := (L^{\mathrm{YM}})^{-1/2}
  \exp(2\pi i n \log t / L^{\mathrm{YM}})$, $n \in \mathbb Z$. The
  truncated space is $E_N^{\mathrm{YM}} := \mathrm{span}\{W_n :
  |n| \le N\}$.

- **Involution / $\mathbb Z/2$-grading.**
  $\gamma^{\mathrm{YM}}(W_j) := W_{-j}$, which on the spatial side
  is $t \mapsto 1/t$ (with $T \equiv 1$ normalization) — the
  **flow-time inversion** involution. The even sector
  $E_N^{\mathrm{YM},+} := \{v \in E_N^{\mathrm{YM}} : \gamma^{
  \mathrm{YM}} v = v\}$ consists of linear combinations symmetric
  in $W_n \leftrightarrow W_{-n}$.

- **"Weil quadratic form" analog $Q_N^{\mathrm{YM}}$.** The
  canonical candidate: the Luscher-Weisz small-flow-time bilinear
  form on $E_N^{\mathrm{YM}}$,
  $$
  Q_N^{\mathrm{YM}}(W_m, W_n) := \int_{T^{-1}}^T \overline{W_m(t)}
  F(t) W_n(t)\,\frac{dt}{t},
  $$
  where $F(t) = S_{2,t}^c(x,y)/c_1(t)^2$ is the rescaled two-point
  correlator of W7-14 eq. 2.1 at a fixed reference pair $(x,y)$.
  This is a **positive** quadratic form (by positivity of the
  underlying Schwinger function) and has the same Cauchy-like
  structure in the $W_n$ basis as the CCM Weil matrix:
  $(Q_N^{\mathrm{YM}})_{m,n} = $ integral of $F$ against
  $\exp(2\pi i(n-m)\log t/L^{\mathrm{YM}}) dt/t$, which is the
  $(n-m)$-th Fourier coefficient of $F$ in the $\log t$ variable.

- **The rank-one perturbation.** Following CCM Lemma 5.4 mechanically:
  if $Q_N^{\mathrm{YM}}$ is even-simple with smallest eigenvector
  $\xi^{\mathrm{YM}}$, then $D' := D - |D\xi^{\mathrm{YM}}\rangle
  \langle\eta^{\mathrm{YM}}|$ induces a self-adjoint operator
  $D_N^{\mathrm{YM}}$ on the quotient Hilbert space
  $\mathcal H^{\mathrm{YM}} := E_N^{\mathrm{YM}}/\mathbb C\xi^{
  \mathrm{YM}}$ with the $Q_N^{\mathrm{YM}}$-induced inner product
  $\langle f|g\rangle_Q := \langle Q_N^{\mathrm{YM}} f|g\rangle$.
  Self-adjointness follows from the Carathéodory-Fejér Toeplitz
  extension theorem (Connes-Consani-Moscovici 2025 §5.2, which
  cites the [Pólya-Szegő] extension in Commun. Math. Phys. 2025)
  **if** the Cauchy matrix $(Q_N^{\mathrm{YM}})_{m,n}$ has the
  same Toeplitz-like positive-definiteness structure as the CCM
  Weil matrix.

**Framework placement.** Both source and target are instances of
Connes noncommutative geometry, specifically the class
"infrared/low-lying-spectrum spectral triple with rank-one
perturbation closing self-adjointness". The transposition is
additive ↔ additive (both live on a $(\mathbb R_{>0}, dx/x)$-style
measure space), unlike the multiplicative transposition of
`paper12/research/14` §B which ports Paper 9's additive six patterns
to multiplicative form via the Mellin bridge. **The YM port is
additive-to-additive along the same structural axis** as the CCM
zeta spectral triple, differing only in which quadratic form plays
the role of $QW_\lambda^N$: the Weil distribution on the RH side,
the flowed two-point correlator $F(t)$ on the YM side.

### Step 4 — LOCK (+ decomposition if needed)

**The locking invariant on the source side**: the **fundamental
identity Theorem 5.10(ii)**
$$
\det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i\lambda^{-iz}
\widehat\xi(z)
$$
is the load-bearing structural statement. It says: the regularized
determinant of $D_{\log}^{(\lambda,N)} - z$ IS the Fourier
transform of the minimal eigenvector of $QW_\lambda^N$, up to a
phase factor. This is a **constructive identity**, not a numerical
approximation. It is what makes the spectrum of
$D_{\log}^{(\lambda,N)}$ real (Thm 5.10(iii)): $\widehat\xi$ is an
entire function of the form $\mathrm{sin}\times\mathrm{rational}$
with real coefficients, so its zeros are real.

**Locking invariant on the target side**: the analog would be a
constructive identity of the form
$$
\det_{\mathrm{reg}}(D_N^{\mathrm{YM}} - z) \overset{?}{=}
\text{(phase)} \cdot \widehat{\xi^{\mathrm{YM}}}(z),
$$
where $\widehat{\xi^{\mathrm{YM}}}$ is the Fourier transform of
the minimal eigenvector of $Q_N^{\mathrm{YM}}$ in the $\log t$
variable. The question is whether $\widehat{\xi^{\mathrm{YM}}}(z)$
has any **direct structural interpretation** in Yang-Mills.

On the RH side the answer is yes: $\widehat\xi_\lambda \to \Xi$ by
CCM's §7 Outlook (rigorized by paper13 §6 Estimate b). The limit
function $\Xi$ is **given in advance** — it is the Riemann Xi
function, whose definition involves nothing from the CCM
construction. The CCM construction is *reverse-engineered* to have
this property: the Weil quadratic form is built from Weil's
distribution $\log_*(\Psi^\sharp)$ encoding the explicit formula,
which is a statement about $\zeta$ directly.

**On the YM side, what plays the role of $\Xi$?** The natural
answer is the **perturbative generating function**
$$
F^{\mathrm{pert}}(t) := 1 + \bar c_1 \bar g^2(q(t)) + \bar c_2
\bar g^4(q(t)) + \cdots,\qquad q(t) = (8t)^{-1/2}.
$$
This is the small-flow-time expansion of the Luscher-Weisz Wilson
coefficient $c_1(t)$ divided by its tree-level value $1/(8\pi^2
t^2)$ (W7-14 eq. 2.2). It is an analytic function of $t$ in a
neighborhood of $t = 0^+$ (W7-14 §5.3: the analyticity is proved
by W5-10 Step 2, radius $r_t > 0$ independent of $N$).

**LOCK candidate**: the YM analog locking invariant is
$$
\widehat{\xi^{\mathrm{YM}}}(z) \overset{\mathrm{goal}}{\to}
\text{(some transform of }F^{\mathrm{pert}}(t)\text{)}
$$
as $N, T \to \infty$. If this convergence holds and the zeros of
$\widehat{\xi^{\mathrm{YM}}}$ (which are eigenvalues of
$D_N^{\mathrm{YM}}$ by the determinant identity, hence real by
self-adjointness) converge to the zeros of the transform of
$F^{\mathrm{pert}}$ — **then** Hurwitz's theorem gives a structural
identification, and by construction the Taylor coefficients of
$F^{\mathrm{pert}}$ are reconstructed from real data.

**This is the load-bearing step, and it is where the transposition
stalls.** The analog of "Riemann zeros" in the YM case would be the
zeros of (a suitable transform of) $F^{\mathrm{pert}}(t)$, and it
is **not at all clear** that:

1. $F^{\mathrm{pert}}$ has a natural Fourier/Mellin transform whose
   zeros are physically meaningful;
2. the zeros of that transform correspond to any AF/perturbation
   data (the Wilson coefficients are the *Taylor coefficients*, not
   the zeros, of $F^{\mathrm{pert}}$);
3. the limit "$\widehat{\xi^{\mathrm{YM}}} \to$ Fourier of
   $F^{\mathrm{pert}}$" is forced by the structure of
   $Q_N^{\mathrm{YM}}$ — on the RH side it is forced by the fact
   that the Weil distribution $\mathcal D$ is built from $\zeta$,
   which is the same $\zeta$ whose zeros define $\Xi$; on the YM
   side, $F(t)$ is built from lattice data, and $F^{\mathrm{pert}}
   (t)$ from perturbative diagrams — **these are exactly the two
   independent objects whose equality IS H4**, not a consequence
   of a shared structural origin.

**BLOCKED-DECOMPOSED**: the structural transposition yields a
coherent spectral triple $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$
(see Step 5 dictionary), but the **fundamental-identity / spectral
locking step** (Step 4) does not transpose: the CCM identity
Thm 5.10(ii) uses the Weil distribution's construction directly
from $\zeta$, and the analog YM construction lacks a
self-referential structure. **The rank-one perturbation machinery
transposes cleanly. The self-adjointness transposes cleanly. What
does NOT transpose is the "constructive-identity shortcut" that
relates the spectrum of $D_{\log}^{(\lambda,N)}$ to the target
data ($\{\gamma_n\}$ on the RH side, Wilson coefficients $\{c_k\}$
on the YM side).**

The decomposition:
- **R.B.1.a** (structural): the spectral triple
  $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$ is well-defined and
  self-adjoint by direct transposition. **CLOSES STRUCTURALLY.**
- **R.B.1.b** (locking): the identification of
  $\mathrm{spec}(D_N^{\mathrm{YM}})$ with any AF-predicted data
  requires a separate argument; the brief's "UV asymptotics match
  by construction" paraphrase has no analog in CCM 2025 and does
  not follow from the transposition alone. **STUCK**.
- **R.B.1.c** (reframing): IF R.B.1.b could be closed via the
  Taylor-coefficient route (W7-14 §5.3, Route A's target), then
  Route B collapses into Route A with extra structural decoration.
  **Forward to R.A.1.**

### Step 5 — COMPUTE (transposition dictionary + verification)

The transposition dictionary, entry-by-entry, is given in the next
section "Transposition dictionary". Here I record the computation /
structural verification.

**Structural verification 1 (the even-sector symmetry).** The CCM
parity involution $\gamma(V_j) = V_{-j}$ corresponds in the spatial
variable to $u \mapsto u^{-1}$: indeed $V_j(u) = U_j(\log\lambda u)
= L^{-1/2}e^{2\pi i j \log(\lambda u)/L}$, and $V_{-j}(u) =
L^{-1/2}e^{-2\pi i j\log(\lambda u)/L} = \overline{V_j(u)}$ by
direct computation (CCM p. 3, §2.2). The YM analog involution
$\gamma^{\mathrm{YM}}(W_j) = W_{-j}$ corresponds to complex
conjugation in the $\log t$ Fourier basis, and to $t \mapsto T^2/t$
in the spatial variable (fixing the midpoint $t = T$ in log-scale).
**This is the flow-time analog of the $u \mapsto u^{-1}$ involution
and is structurally natural**.

**Structural verification 2 (the $\mathbb Z/2$-grading commutes
with $Q_N^{\mathrm{YM}}$).** For the CCM Weil matrix, $q_{-i,-j}
= q_{i,j}$ because Weil's distribution $\mathcal D(y) = \log_*(
\Psi^\sharp)(y)$ is symmetric under $y \mapsto -y$ on $[0, L]$
(CCM Lemma 5.2(i)). For the YM analog, the question is whether
$F(t)/c_1(t)^2$ is symmetric under $\log t \mapsto -\log t$, i.e.
$t \mapsto 1/t$. **Answer: NO.** The gradient-flow correlator
$F(t)$ is NOT symmetric under $t \mapsto 1/t$ — it is a monotone
decreasing function of $t$ (on the log scale, away from the UV
fixed point), not a symmetric function. **The even-sector
restriction, which is load-bearing in CCM Lemma 5.2(i), does not
apply to the YM analog without a different choice of quadratic
form.**

*Rescue attempt*: restrict the involution to $t \mapsto T^2/t$
inside a bandwidth $[T^{-1}, T]$ on which $F$ has been symmetrized
by replacing $F(t)$ with $F(t) + F(T^2/t)$. This symmetric
modification is a positive bilinear form (sum of two positive
forms) and satisfies the parity involution by construction. But
**symmetrizing $F$ destroys the Taylor-coefficient identification
at $t = 0^+$**: the sum $F(t) + F(T^2/t)$ evaluated at $t \to 0^+$
picks up the behavior of $F$ at $t = T^2/t \to \infty$, which is
the infrared (confinement) regime, not the UV (perturbation theory)
regime. The even-sector restriction forces the quadratic form to
see both UV and IR data symmetrically, losing the UV
identification.

**Structural verification 3 (the rank-one perturbation).** Given
any positive-definite quadratic form $T = Q_N^{\mathrm{YM}}$ with
even-simple smallest eigenvector $\xi^{\mathrm{YM}}$, CCM Lemma 5.4
applies mechanically: $D' = D - |D\xi^{\mathrm{YM}}\rangle\langle
\eta^{\mathrm{YM}}|$ induces a self-adjoint operator on the
quotient, and the regularized determinant identity Thm 5.10(ii)
holds in the same form (the proof is formal and does not depend on
the specific form of $T$, only on positivity and even-simplicity).
**This is the one step that transposes without modification.**

**Structural verification 4 (the ρ ≥ 4.27 parameter).** In CCM's
construction, $\rho$ is the Carathéodory-Fejér decay base in the
rank-one perturbation data, specifically the decay of the minimal
eigenvector components $|\xi_N(j)| \le C_N \rho_N^{-|j|}$ (paper13
§8.1). The numerical value $\rho \ge 4.27$ for $N \ge 5$ arises
because (paper13 §8.1, last paragraph): "the singularity structure
of the Weil distribution $D(y) = \log_*(\Psi^\sharp)(y)$ on $[0,L]$
is determined by $\zeta$ (the pole at $y=0$ from $\rho(x) =
e^{x/2}/(e^x - e^{-x})$, von Mangoldt contributions at
$y = j\log p$). These singularities are properties of $\zeta$,
independent of the truncation level $N$. The decay base $\rho$
equals the distance from the real axis to the nearest singularity
of the eigenvector's analytic continuation in the complex plane,
which is controlled by the fixed analytic structure of $D$."

For the YM analog, the same structural slot is played by:
$\rho^{\mathrm{YM}}$ = distance from the real axis to the nearest
singularity of (the analytic continuation of) $F(t)/c_1(t)^2$ in
the complex $\log t$ plane. **This is a statement about the
analyticity radius $r_t$ of $F(t)$, which W5-10 Step 2 establishes
to be $r_t > 0$ uniform in $N$ and $K$** (W7-14 §5.3). The YM
analog of $\rho \ge 4.27$ is therefore $\rho^{\mathrm{YM}} \ge
1/r_t^{\mathrm{YM}}$ where $r_t^{\mathrm{YM}}$ is the Cauchy radius
from W5-10 Step 2. **Numerical value: $r_t^{\mathrm{YM}}$ is
bounded below by the polymer-convergence radius of the Balaban
expansion at step $k$, which is $k$-independent by the Balaban
analyticity results (PROOF-CHAIN items 2–4, research/44), giving
$\rho^{\mathrm{YM}} = \Theta(1)$ with an explicit lower bound set
by the gradient-flow polymer convergence** — a weaker quantitative
statement than the CCM $\rho \ge 4.27$, but structurally analogous.

**Structural verification 5 (Carathéodory-Fejér)**. The
Carathéodory-Fejér extension theorem for Toeplitz matrices
(Pólya-Szegő; Commun. Math. Phys. 2025 extension cited by CCM) is
the mechanism by which CCM guarantees self-adjointness of the
rank-one-perturbed scaling operator. **The load-bearing input is
the Toeplitz structure of the Cauchy matrix
$\tau_{i,j} = (b_i - b_j)/(i - j)$** (CCM Lemma 5.1). In the
$V_n$ basis, this is a Toeplitz matrix because the Weil
distribution depends only on the difference $i - j$.

For the YM analog, the matrix $(Q_N^{\mathrm{YM}})_{m,n} = $
$(n-m)$-th Fourier coefficient of $F$ in $\log t$, hence
$(Q_N^{\mathrm{YM}})_{m,n} = \widehat F(n - m)$ where $\widehat F$
is the Fourier transform in $\log t$. **This IS a Toeplitz matrix**,
with symbol $\widehat F$. Carathéodory-Fejér applies to Toeplitz
matrices whose symbols are in $H^\infty$ of the upper half-plane
(or equivalently, whose matrices are positive-definite Toeplitz and
the extension is to the full semi-infinite Toeplitz operator).
**The YM analog Carathéodory-Fejér closure requires $\widehat F$ to
be in $H^\infty$, which is a statement about the analyticity of
$F(t)$ in the complex $\log t$ plane — i.e., about $F(t)$ being
holomorphic on an annulus around $|t| = T$.** By W5-10 Step 2,
$F(t)$ is analytic in a disc of radius $r_t$ around any real
$t > 0$, uniformly in Balaban step and bare-scale. **This is the
Carathéodory-Fejér transposition: the YM analog is the flow-time
analyticity of $F$, playing the same structural role as the
Toeplitz positive-definiteness in CCM.**

**So: the self-adjointness mechanism DOES transpose**, with the CF
Toeplitz positivity replaced by the gradient-flow analyticity of
$F(t)$. This is the **one good news** of the transposition:
Step 3 of W7-14 §5 ("analyticity provides a rigorous bridge")
provides exactly the input that would be needed to run CCM's rank-
one-perturbation self-adjointness on the YM side.

### Step 5.5 — Self-suspicion (3 ways)

**Way 1 — Paraphrase trust (backward-verification, I-7 / I-10)**:
The brief, the blackboard §D row ("CCM 2025 spectral triple:
Operators $D_N$ on prolate even sector $E_N^+$ with **UV
asymptotics matching perturbation theory by construction**"), and
the node spawn prompt §2 all assert that CCM 2025 provides
"operators whose UV asymptotics match perturbation theory by
construction". **I verified this claim by reading the CCM 2025
preprint directly (local copy at `paper13-rh/sources/ccm-zeta-
spectral-triples-2025.pdf`, pages 1, 2, 15–28).** The claim is
**WRONG**: CCM 2025 says nothing about UV asymptotics or
perturbation theory. CCM 2025's Abstract says: "produces
self-adjoint operators whose spectra coincide, with striking
numerical accuracy, with the lowest non-trivial zeros of
$\zeta(1/2+is)$." CCM §7 Outlook (p. 27–28) says: "These numerical
results provide evidence that the spectra of the operators
$D_{\log}^{(\lambda,N)}$ tend to the nontrivial zeros of the
Riemann zeta function $\zeta(1/2+is)$. Establishing this
convergence rigorously would amount to a proof of the Riemann
Hypothesis." **The construction is an existence+numerical
statement, with a conditional structural identification ($\widehat
\xi_\lambda \to \Xi$ as $\lambda\to\infty$) stated verbatim as
open**: "Justifying rigorously this step is the main remaining
obstacle to our approach to RH." **The "UV asymptotics match
perturbation theory by construction" framing does not exist in CCM
2025. It is a paraphrase introduced somewhere in the blackboard
bootstrap / brief authoring chain and has misled the route B
framing.**

This catches the R.B.1 transposition before Step 6: if the source
framework's "UV asymptotics match" claim is spurious, the transposi-
tion of that claim to the YM side is ALSO spurious. The correct
CCM statement is "eigenvalues coincide with $\gamma_n$ by a
Fourier-transform identity and uniform convergence". The correct
YM transposition target is therefore "eigenvalues coincide with
$\Gamma_n^{\mathrm{YM}}$" for some structurally-defined sequence
$\Gamma_n^{\mathrm{YM}}$, **not** "UV asymptotics match
perturbation theory".

**Way 2 — Even-sector failure**: The CCM Lemma 5.2(i) even-sector
preservation $T\gamma = \gamma T$ is load-bearing for the entire
paper13 closure (referee fix #9: "Even-sector compatibility proved
(CCM Lemma 5.2(i): $T\gamma = \gamma T$)"). I verified above (Step
5 Structural Verification 2) that the YM analog quadratic form
$Q_N^{\mathrm{YM}}$ built from the flowed correlator $F(t)$ **does
not satisfy** the parity commutation unless symmetrized, and
symmetrization destroys the $t \to 0^+$ UV identification. This is
a **structural** incompatibility: the even-sector choice in CCM
is a consequence of the $f \leftrightarrow f^\sharp$ symmetry of
the Riemann-Weil explicit formula, which is **intrinsic** to the
arithmetic side and has no counterpart in the gradient-flow side.
**The "even sector" is not transferable.** The YM analog operator
lives on the full $E_N^{\mathrm{YM}}$, not on a parity-selected
sub-sector. This changes the CCM Theorem 3.6 unique-minimal-
eigenvector statement (which relies on even-simplicity) to a
weaker "simple on $E_N^{\mathrm{YM}}$" statement, which in turn
requires a different input for AE simplicity (CCM/paper13 rely on
Slepian compatibility + Krein-Rutman for the even sector, paper13
§12.5).

**Way 3 — Target data mismatch**: Even granting that the
transposition produces a coherent $D_N^{\mathrm{YM}}$, the
**target data** on the RH side (Riemann zeros $\{\gamma_n\}$) and
on the YM side (Wilson coefficients $\{c_k\}$ or equivalently
Taylor coefficients $\{F^{(k)}(0)\}$) are **categorically
different objects**: zeros of an entire function versus Taylor
coefficients of an analytic function. Fourier transforms move
between these: the zeros of $\widehat f$ and the Taylor
coefficients of $f$ are NOT in a natural correspondence. **The
brief's implicit assumption that "UV asymptotics" on the YM side
play the same structural role as "zero spacing" on the RH side is
a category error.** The correct target on the YM side is not a
spectrum to identify (there is no analog of Hurwitz's theorem
closing YM) but a **Taylor-coefficient identification**, which is
exactly Route A's target (R.A.1). **Route B collapses into Route A
with extra structural decoration that adds machinery but not
closure power.**

**Backward-verification summary**: CCM 2025 primary source (local
PDF) verified; the brief's "UV asymptotics match perturbation theory
by construction" paraphrase is wrong; the correct CCM claim is
"eigenvalues coincide with Riemann zeros via Fourier transform
identity and conjectural uniform convergence (open in CCM, closed
by paper13)". **I-7 backward-verification catches the load-bearing
paraphrase error before Step 6.**

### Step 6 — VERIFY (convention preservation)

Verifying that the transposition preserves the consistency
conventions of CCM 2025 against the I-10 Critic check-list:

**Modular eigenvalue convention.** CCM uses $\epsilon_N$ =
smallest eigenvalue of $QW_\lambda^N$, assumed simple and even.
YM analog: smallest eigenvalue of $Q_N^{\mathrm{YM}}$, which
**cannot** be assumed even (Way 2 of Step 5.5). **Convention
failure**: the YM port inherits "smallest-simple" but loses
"even-simple". The Critic (I-10 symmetry) will flag this if using
the same transposition methodology.

**Group representation convention.** CCM's $\mathbb Z/2$-grading
$\gamma$ is a $\mathbb Z/2$-group action generated by the
involution $u \mapsto u^{-1}$, reflecting the structure of the
multiplicative group $\mathbb R_+^*$. YM analog:
$\mathbb Z/2$-grading $\gamma^{\mathrm{YM}}$ generated by
$t \mapsto T^2/t$. **The group-theoretic structure transposes, but
the physical meaning differs**: on the RH side $u$ parametrizes
multiplicative translations (Mellin dual to additive log $u$); on
the YM side $t$ parametrizes gradient-flow time, which has no
natural involution beyond the artificial $t \mapsto T^2/t$
reflection around the bandwidth midpoint. **Convention cautionary
note**: the $\mathbb Z/2$ action on the RH side is canonical; on
the YM side it is an imposed choice without physical origin.

**Sign convention** (signs in the rank-one perturbation
$D' = D - |D\xi\rangle\langle\eta|$). CCM Lemma 5.4: the minus
sign is fixed by the requirement $D'\xi = 0$ (so that $\xi$ is in
the kernel of $D'$ and gets quotiented out). The YM analog
inherits the same sign convention mechanically. **Convention
preserved**.

**"Which side of the spectral triple represents which" convention.**
CCM's spectral triple $(A, \mathcal H, D)$ has $\mathcal H = L^2(
[\lambda^{-1},\lambda], d^*u)$, $D = D_{\log}^{(\lambda,N)}$, and
the algebra $A$ is implicit (it is the Bost-Connes algebra or an
approximation thereof, with the Euler product as the truncation).
**YM analog ambiguity**: the "algebra" side of the YM spectral
triple is unclear. Candidates:
- The C*-algebra generated by the gradient-flow evolution $e^{-tD
  }$ for $t > 0$ — but this is the semigroup acting on $\mathcal H
  _T^{\mathrm{GF}}$, not an algebra of observables.
- The Wilson-line algebra with flow-time smearing — closer to
  physical observables, but then the spectral triple becomes the
  Connes spectral action framework of Route C, not CCM-style
  infrared spectral triple of Route B. **Convention failure**:
  Route B collapses toward Route C at the algebra level.

**Which side represents what**: ON the RH side, the $D$ side of
the spectral triple represents "zeta zeros" and the algebra side
represents "primes". ON the YM side, if we force the analog, the
$D$ side would represent "Taylor coefficients of $F(t)$ at $t=0$"
and the algebra side would represent "gradient-flow observables".
**This is a semantic mismatch**: on RH the zeros are the
**spectrum** (continuous / dense mathematical object); on YM the
Taylor coefficients are a **countable sequence** (a single analytic
function's expansion at a point). The spectral-triple formalism
is natural for the former, artificial for the latter.

**Verification verdict**: The transposition preserves some
conventions (sign, rank-one structure) and fails others (even-
sector parity, algebra interpretation, target-data type). An I-10
symmetric Critic will flag the even-sector failure and the
target-data-type mismatch. **The transposition is structurally
incomplete: we get a well-defined self-adjoint operator, but we
lose the structural link between its spectrum and any AF-predicted
YM data.**

---

## Transposition dictionary

| # | Source (CCM 2025 / Paper 13 RH) | Target (YM analog, proposed) | Notes / rationale / verification |
|:-:|:--|:--|:--|
| 1 | Ambient Hilbert space $\mathcal H_\lambda = L^2([\lambda^{-1},\lambda], d^*u)$ | $\mathcal H_T^{\mathrm{GF}} = L^2([T^{-1},T], dt/t)$ | Direct port along the shared $(\mathbb R_{>0}, dx/x)$ structure. $\log u \leftrightarrow \log t$. **Structurally clean.** |
| 2 | Bandwidth parameter $\lambda > 1$ (CCM eq. 5.14) | $T > 1$ (UV cutoff flow-time bandwidth). Primes $\le \lambda^2$ $\leftrightarrow$ gradient-flow expansion to $t \ge T^{-2}$ | The role of $\lambda$ is to control how far the Euler product truncation reaches; for YM, $T$ controls how close to the UV the flow time goes. **Dimensional analogy only** — no deep correspondence. |
| 3 | Unperturbed operator $D_{\log}^{(\lambda)} = -i\partial/\partial\log u$, periodic BCs | $D_{\log t}^{(T)} = -i\partial/\partial\log t$, periodic BCs | Direct formal port. Flow-time scaling operator. |
| 4 | Truncation space $E_N = \mathrm{span}\{V_n : \|n\| \le N\}$, $V_n(u) = U_n(\log\lambda u)$, $U_n = L^{-1/2}e^{2\pi inx/L}$ | $E_N^{\mathrm{YM}} = \mathrm{span}\{W_n : \|n\| \le N\}$, $W_n(t) = L_{\mathrm{YM}}^{-1/2}e^{2\pi in\log t/L_{\mathrm{YM}}}$ | Direct basis-level port. $2N+1$-dimensional truncation. |
| 5 | Parity involution $\gamma(V_j) = V_{-j}$, equivalently $u \mapsto u^{-1}$ | Proposed $\gamma^{\mathrm{YM}}(W_j) = W_{-j}$, equivalently $t \mapsto T^2/t$ | **Convention failure (Step 5.5 Way 2)**: the physical gradient-flow correlator $F(t)$ is not symmetric under this involution. The even-sector restriction, load-bearing on the RH side, does not restrict to a natural YM subspace. Only "forced" symmetrization works, at the cost of mixing UV and IR data. |
| 6 | Weil quadratic form $QW_\lambda^N$, matrix elements Cauchy $\tau_{i,j} = (b_i - b_j)/(i-j)$, $\tau_{i,i} = a_i$ (CCM Lemma 5.1) | Proposed $Q_N^{\mathrm{YM}}$: matrix elements $= (n-m)$-th Fourier coefficient of $F(t) = S_{2,t}^c(x,y)/c_1(t)^2$ in $\log t$, i.e. a Toeplitz matrix with symbol $\widehat F$ (Fourier transform in $\log t$) | **Partial transposition**: the Toeplitz structure is preserved, the Cauchy form is not. Toeplitz positivity of $Q_N^{\mathrm{YM}}$ follows from positivity of $F(t)$ (Schwinger-function positivity) and the Herglotz theorem. **Structurally coherent**, but the choice of $F(t)/c_1(t)^2$ as the YM "Weil distribution" is an imposed choice without intrinsic YM motivation. |
| 7 | $\mathbb Z/2$-grading $T\gamma = \gamma T$ (CCM Lemma 5.2(i)): parity preserved by the Weil matrix | Proposed $Q_N^{\mathrm{YM}}\gamma^{\mathrm{YM}} = \gamma^{\mathrm{YM}}Q_N^{\mathrm{YM}}$: parity preserved by the flowed-correlator matrix | **FAILS without symmetrization** (Step 5.5 Way 2, Step 5 Structural Verification 2). $F(t)$ is not symmetric under $t \mapsto T^2/t$. The even-sector restriction, which is a referee fix (fix #9) on the RH side, has no analog on the YM side. |
| 8 | Even-simple hypothesis: smallest eigenvalue of $T$ is simple with $\gamma\xi = \xi$ (CCM Def 5.3) | Simple-on-$E_N^{\mathrm{YM}}$ hypothesis: smallest eigenvalue of $Q_N^{\mathrm{YM}}$ is simple (no parity constraint) | Weaker hypothesis on the YM side — but this requires replacing CCM Thm 3.6's uniqueness-via-even-sector argument with a different input. Paper 13's Slepian compatibility lemma (§12.5) extends AE simplicity beyond $N = 20$ for the even sector; the YM analog would need a different lemma. |
| 9 | Rank-one perturbation $D' = D - \|D\xi\rangle\langle\eta\|$ (CCM Lemma 5.4) | $(D^{\mathrm{YM}})' = D^{\mathrm{YM}} - \|D^{\mathrm{YM}}\xi^{\mathrm{YM}}\rangle\langle\eta^{\mathrm{YM}}\|$ | **Transposes cleanly**. The rank-one construction is formal and preserves self-adjointness whenever the underlying $T$ is positive with one-dimensional kernel. |
| 10 | Self-adjoint $D_{\log}^{(\lambda,N)}$ on $E_N^+/\mathbb C\xi_N$ with Carathéodory-Fejér guarantee (CCM Thm 5.10(i)) | Self-adjoint $D_N^{\mathrm{YM}}$ on $E_N^{\mathrm{YM}}/\mathbb C\xi^{\mathrm{YM}}$, self-adjointness input: flow-time analyticity of $F(t)$ (W5-10 Step 2, W7-14 §5.3) replacing CF Toeplitz positivity | **Transposes, with the self-adjointness input replaced**. The CF Toeplitz extension theorem requires positive-definite Toeplitz; the YM analog requires the Toeplitz symbol $\widehat F \in H^\infty$ of the upper half-plane, i.e., $F$ holomorphic on a complex neighborhood of $\log t \in \mathbb R$. W5-10 Step 2 delivers exactly this. **Note**: no "perturbation-theory-matching by construction" anywhere in this step. |
| 11 | Fundamental identity $\det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i\lambda^{-iz}\widehat\xi(z)$ (CCM Thm 5.10(ii)) | Formal analog $\det_{\mathrm{reg}}(D_N^{\mathrm{YM}} - z) = \text{(phase)}\cdot\widehat{\xi^{\mathrm{YM}}}(z)$ | **Transposes formally**. The proof of CCM Thm 5.10(ii) is direct computation (pp. 23–24), does not depend on the specific form of the quadratic form. **But this identity alone does not relate the spectrum to any target data**: it merely says the regularized determinant is a Fourier transform. |
| 12 | Target data: Riemann zeros $\{\gamma_n\}$, defined via $\Xi = \zeta(1/2 + iz) \cdot (\text{completion})$ (classical) | Target data: **???**. No direct analog | **BLOCKING STEP**. On the RH side, the target data are the zeros of $\Xi$, an entire function whose zeros encode the analytic structure of $\zeta$ and are intrinsically interesting (and are the object of RH). On the YM side, there is no natural "YM Xi function" whose zeros correspond to anything physical. The closest analog is $F^{\mathrm{pert}}(t)$ whose **Taylor coefficients** encode the AF-predicted Wilson coefficients, but Taylor coefficients are not zeros. **Category error in the transposition.** |
| 13 | Limit $\widehat\xi_\lambda \to \Xi$ uniformly on substrips of $\|\mathrm{Im}(z)\| < 1/2$ (CCM §7 Outlook, conjectural inside CCM; rigorized by paper13 §6 Estimate b + §10 Theorem 10.1) | Proposed limit $\widehat{\xi^{\mathrm{YM}}} \to \widehat{F^{\mathrm{pert}}}$ (or transform thereof) uniformly on some domain | **DOES NOT TRANSPOSE**. The CCM limit works because Weil's distribution is constructed from $\zeta$, and $\Xi$ is defined from $\zeta$ — they share the same source. The YM analog's $F(t)$ is constructed from the lattice path integral, and $F^{\mathrm{pert}}(t)$ is constructed from Feynman diagrams. **Their equality IS Hypothesis H4**, not a consequence of the transposition — see Step 4. |
| 14 | CF decay base $\rho \ge 4.27$ (paper13 §8.1 Prop 8.1) | $\rho^{\mathrm{YM}} = 1/r_t^{\mathrm{YM}}$ where $r_t^{\mathrm{YM}}$ is the gradient-flow analyticity radius from W5-10 Step 2 | **Transposes with a quantitative downgrade**. On the RH side, $\rho \ge 4.27$ is numerically verified and is anchored by the analytic structure of $\zeta$. On the YM side, $\rho^{\mathrm{YM}}$ is bounded below by a Balaban-polymer-convergence radius, which is $k$-independent but not given explicitly with a clean lower bound. **Structurally analogous, numerically looser.** |
| 15 | Hurwitz eigenvalue convergence: eigenvalues of $D_N \to$ zeros of $\Xi = \{\gamma_n\}$ (paper13 Thm 10.2) | Proposed: eigenvalues of $D_N^{\mathrm{YM}} \to$ **???** | **BLOCKED** by #12. Hurwitz requires a target entire function whose zeros are the target data. No such function exists on the YM side — at best we have $F^{\mathrm{pert}}(t)$ whose Taylor coefficients are the target. |
| 16 | Boegli spectral exactness (paper13 §9) using gnrc + discrete compactness | Would require analogous compactness + resolvent convergence for the YM family | **Transposes formally** assuming R.B.2-R.B.3 (construct gradient-flow Sobolev bounds and resolvent convergence for $D_N^{\mathrm{YM}}$). Downstream node, not within R.B.1's scope. |
| 17 | The Paper 13 closing deduction ($\mathrm{spec}(D_\infty) = \{\gamma_n\} \subset \mathbb R \Rightarrow$ RH) | Proposed analog: $\mathrm{spec}(D_\infty^{\mathrm{YM}}) = \text{(something)} \subset \mathbb R \Rightarrow$ H4 | **BLOCKED** by #12 and #15. The RH closing deduction works because (a) the Riemann zeros are on the real line iff $\zeta$ has them on Re $= 1/2$, and (b) self-adjointness forces real spectra. The YM analog lacks a target like (a): there is no physical statement "the Wilson coefficients are on the real line iff H4 holds". |

---

## Verdict: **BLOCKED-DECOMPOSED**

The transposition dictionary is well-defined up to entry #11 (rank-
one perturbation + self-adjointness via gradient-flow analyticity).
Entries #12, #13, #15, #17 — the **locking step** that ties the
spectrum of the ported operator to target data — **do not
transpose**. The failure is not a computational gap but a
**category mismatch**: the RH construction identifies a spectrum
with a target set of zeros; the YM construction would need to
identify a spectrum with a target set of Taylor coefficients, and
there is no natural correspondence between these data types.

**The brief's load-bearing paraphrase** — "CCM 2025 provides
operators whose UV asymptotics match perturbation theory by
construction" — is **not present in CCM 2025** (I-7 backward
verification against local PDF, pages 1–28). CCM 2025 makes a
different claim: numerical coincidence of eigenvalues with Riemann
zeros, conditional on the §7 Outlook convergence step which CCM
themselves state verbatim as open. The UV-asymptotics-matching
framing is a blackboard-bootstrap paraphrase that misled Route B's
premise. **The paraphrase trust is exactly what I-7 / I-10 warn
against, and it is the structural catch of this node.**

**Decomposition into sub-nodes** (for the runner to register if
Route B continues):

- **R.B.1.a** — The spectral-triple structural port is well-defined
  and delivers $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+},
  Q_N^{\mathrm{YM}})$ with self-adjointness via flow-time
  analyticity. **Status**: advanced (structurally coherent, though
  without physical motivation).
- **R.B.1.b** — The identification of $\mathrm{spec}(D_N^{\mathrm{
  YM}})$ with any AF/perturbative target. **Status**: STUCK. No
  analog of Riemann's $\Xi$ function exists on the YM side; the
  category error in #12 blocks the locking step.
- **R.B.1.c** — Reframing: if R.B.1.b could be closed, it would
  require the same Taylor-coefficient identification that Route A
  targets directly. **Forward to R.A.1**.

---

## Generative step

**The one structural gain from R.B.1**: the observation (Step 5
verification 5 + dictionary entry #10) that the
**Carathéodory-Fejér Toeplitz self-adjointness** of CCM 2025
transposes to the YM side as the **gradient-flow analyticity of
$F(t)$**, which is W5-10 Step 2 material. This is a **transposition
of self-adjointness mechanism, not of target spectrum**. If Route B
is continued, this is the one structurally valid seed: the Toeplitz
positive-definiteness of $(Q_N^{\mathrm{YM}})_{m,n}$ follows from
the Herglotz theorem applied to $\widehat F$ as a positive measure
on the circle, and $F$'s analyticity upgrades the Toeplitz
condition to Carathéodory-Fejér applicability.

**Interpretation**: the "rigorous bridge from analyticity"
(W7-14 §5.3) already has the structural content that a CCM-style
spectral triple would need. Route B does not add closure power
beyond what W7-14 §5.3 already provides; it adds **ritual
decoration** (a spectral-triple wrapper) around the same
Taylor-coefficient content. **Route B is not a route; it is a
reformulation of Route A in spectral-triple language.**

## Stuck-at step

**Step 4 (LOCK) at dictionary entry #12**: identifying a target
spectrum for $D_N^{\mathrm{YM}}$ analogous to $\{\gamma_n\}$. The
RH target (Riemann zeros) is structurally built into the Weil
distribution via the explicit formula; there is no YM analog of
the explicit formula that ties the gradient-flow correlator to a
natural sequence of zeros of an entire function. The natural YM
target is Taylor coefficients, not zeros, and the transposition
hits a category error.

## §I notes to append

- **§I-7 (backward verification) CATCH**: the brief's load-bearing
  paraphrase "CCM 2025 provides operators with UV asymptotics
  matching perturbation theory by construction" is **wrong against
  primary source**. Verified against `paper13-rh/sources/ccm-zeta-
  spectral-triples-2025.pdf` pages 1, 15–28. CCM 2025's actual
  claim is weaker: numerical coincidence of eigenvalues with
  Riemann zeros, with the rigorous identification open (CCM §7
  Outlook, verbatim: "Justifying rigorously this step is the main
  remaining obstacle to our approach to RH"). **Any future Route
  B node inheriting the "UV asymptotics match by construction"
  framing should be killed**, not decomposed: the framing is not
  structurally present in CCM and does not transpose.
  
- **§I-9 (selective-read discipline) HONORED**: read paper13-rh
  §6 (lines 1–240) + §§7–10 (selectively via grep), and CCM 2025
  PDF pages 1, 2, 5, 14–28. Did NOT read paper13-rh
  `sections-06-10.md` end-to-end (1002 lines, skipped §7.2–7.3,
  §8.2–8.3, §9.5–9.8 after grep told me they are downstream of
  the structural core). Did NOT read
  `paper12/research/14-transposition-CCM-and-reasoning-patterns.md`
  end-to-end (755 lines); read §A (CCM intertwining) and §B.1
  (uniform transposition rule). **The "CCM → YM" sub-section
  referenced in the spawn prompt does not exist in file 14** —
  the transposition methodology there is RH-side only, not YM-side,
  which is itself a structural hint that the Route B transposition
  is not a known established route.

- **§I-10 (Critic symmetry) READY**: the Critic will use the same
  transposition methodology and should look at this output for
  exactly three issues: (a) the even-sector failure (Step 5.5
  Way 2, dictionary #7), (b) the target-data category error
  (Step 5.5 Way 3, dictionary #12), (c) the paraphrase-trust catch
  (Step 5.5 Way 1). I flagged all three proactively; the Critic
  should confirm or refute each.

- **§I-5 (HONEST-STALL as first-class)**: this verdict of BLOCKED-
  DECOMPOSED strengthens the case for Route D (R.D.1 running in
  parallel) as the primary shipping path. Route B's p_runner = 0.30
  should be downgraded post-R.B.1 to p_runner ≈ 0.05 (Route B
  would require either a new target-data proposal outside W7-14
  §5.3 or a Route-C-style collapse into the spectral action
  framework).

## Proposed §D toolkit additions

Add to the blackboard §D toolkit (renumber as needed):

| entry | description | source | type | symbol | k | bare | w/% |
|:--|:--|:--|:--|:--|:--|:--|:--|
| $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$ | Proposed gradient-flow spectral triple: rank-one perturbation of $D_{\log t}^{(T)} = -i\partial_{\log t}$ on $L^2([T^{-1},T], dt/t)$, even-sector-incomplete version | R.B.1 this node | R | $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+}, Q_N^{\mathrm{YM}})$ | — | — | 25 |
| $Q_N^{\mathrm{YM}}$ | Toeplitz quadratic form built from Fourier coefficients of $F(t) = S_{2,t}^c/c_1(t)^2$ in $\log t$; positive-definite iff $F$ Herglotz | R.B.1 this node | R | $Q_N^{\mathrm{YM}}$ | — | — | 25 |
| flow-time CF analog | Carathéodory-Fejér Toeplitz self-adjointness for $Q_N^{\mathrm{YM}}$ replaced by flow-time analyticity of $F(t)$ (W5-10 Step 2) | R.B.1, W5-10, W7-14 §5.3 | R/E | — | — | — | 60 |
| CCM Theorem 5.10(ii) (load-bearing identity) | Regularized determinant $\det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i\lambda^{-iz}\widehat\xi(z)$ (CCM source paper pp. 22–24, local PDF) | CCM 2025 arXiv 2511.22755 | R | — | — | — | 100 |
| "UV asymptotics by construction" paraphrase-catch | Brief's claim that CCM 2025 provides UV match by construction; primary-source verification shows this is paraphrase, not CCM text; I-7 backward-verification catch | R.B.1 this node | — | — | — | — | 0 |

Also add a **killed** row in §F:

| approach | reason | source |
|:--|:--|:--|
| "Port CCM 2025 to YM to close H4 via structural identification of the spectral triple" | Category error in the target data (zeros of an entire function vs Taylor coefficients of an analytic function); the load-bearing CCM §7 Outlook structural identity $\widehat\xi_\lambda \to \Xi$ has no YM analog; the brief's "UV asymptotics match by construction" paraphrase is not in CCM 2025. | R.B.1 this node, I-7 backward-verification catch |

## What the next runner needs to know

**Headline**: R.B.1 catches the load-bearing paraphrase "CCM 2025
provides operators with UV asymptotics matching perturbation theory
by construction". The paraphrase is wrong against primary source;
CCM 2025 makes a weaker claim ("numerical coincidence of
eigenvalues with Riemann zeros, with rigorous identification open").
**Route B's premise is a paraphrase error, not a structural route.**

**Structural salvage**: the spectral-triple port transposes up to
the self-adjointness mechanism (entry #10 of the dictionary, with
CF Toeplitz positivity replaced by flow-time analyticity of
$F(t)$). This is a **formal rewrapping** of W7-14 §5.3 in
spectral-triple language, not a new closure vector.

**Recommendation**: mark R.B.1 as **BLOCKED-DECOMPOSED**; downgrade
Route B's $p_{\mathrm{success}}$ from 0.30 to 0.05 (residual
probability that a different target-data proposal — not covered by
this transposition — could close Route B). Redirect W1-B2..B5
effort toward Route A (R.A.1 Taylor-coefficient identification)
and Route D (R.D.1 HONEST-STALL editorial). Route D's
$p_{\mathrm{success}} \approx 0.99$ dominates the joint
probability; Route A's Taylor-coefficient content is what R.B.1
structurally reduces to anyway.

**One-line §M summary** (≤300 words, for the runner's metric row):

R.B.1 catches the brief's load-bearing paraphrase ("CCM 2025
provides operators with UV asymptotics matching perturbation theory
by construction") against the primary source
`paper13-rh/sources/ccm-zeta-spectral-triples-2025.pdf`. The
paraphrase is not in CCM 2025 — the actual claim is numerical
coincidence of eigenvalues with Riemann zeros, with rigorous
identification stated verbatim as open ("Justifying rigorously this
step is the main remaining obstacle to our approach to RH", CCM
p. 28). The structural transposition yields a coherent but
physically-unmotivated $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$:
entries #1–#11 of the dictionary port cleanly (Hilbert space,
basis, rank-one perturbation, self-adjointness via flow-time
analyticity replacing Carathéodory-Fejér Toeplitz), but entries
#12, #13, #15, #17 hit a category error (zeros of an entire
function vs Taylor coefficients of an analytic function, with no
YM analog of the Riemann Xi function to use in Hurwitz). The
even-sector parity preservation (CCM Lemma 5.2(i), referee fix #9
for paper13) fails for the YM analog because $F(t)$ is not
symmetric under $t \mapsto T^2/t$. The Carathéodory-Fejér
self-adjointness DOES transpose, as flow-time analyticity of $F(t)$
from W5-10 Step 2 — but this is exactly the W7-14 §5.3 content
already available to Route A. Route B does not add closure power
beyond Route A; it adds spectral-triple decoration. Verdict
BLOCKED-DECOMPOSED, sub-nodes R.B.1.a (structural port: advanced),
R.B.1.b (locking: stuck at #12 category error), R.B.1.c (collapse
into R.A.1). Recommend downgrading Route B's p to 0.05 and
redirecting Wave 2 effort toward R.A / R.D.

---

*End of W1-B1 Author output for R.B.1. Critic, you have the
transposition methodology (paper12/research/14) and the same
primary-source PDF (paper13-rh/sources/ccm-zeta-spectral-triples-
2025.pdf). I-7 backward-verification catches the load-bearing
paraphrase error; I-10 symmetry protocol applies.*
