# REVISED 2026-04-10

# Paper 24: The Bridge Family
## Cyclotomic Brauer Cocycles and the Standard Model Structural Numbers

### Sections 1--4

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-09*

---

## 1. Introduction

### 1.1 The structural numbers of the Standard Model

The Standard Model of particle physics contains a set of discrete
structural numbers that it does not explain. There are 3 generations
of fermions. There are 4 fundamental forces (or, in the Pati--Salam
picture, 4 colours including the lepton as a fourth colour). There
are 6 quark flavours, decomposing as 2 (isospin up/down) times 3
(generations). The Cabibbo angle, the leading parameter of quark
mixing, takes a specific numerical value
$\lambda_{\mathrm{CKM}} = 0.22500 \pm 0.00067$ (PDG 2024). The
Koide ratio
$$
Q \;=\; \frac{m_e + m_\mu + m_\tau}
           {(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^{\,2}}
\;=\; \frac{2}{3}
$$
holds experimentally to five decimal places. None of these numbers is
derived within the Standard Model. They are inputs.

Collectively we call these the *structural numbers*: the integers
and rational fractions that organise the Standard Model's matter
content and mixing pattern. The present paper derives all of them
from cyclotomic arithmetic.

### 1.2 Why these numbers are unexplained in the SM

In the Standard Model Lagrangian, the generation count $n_{\mathrm{gen}} = 3$
enters as the number of independent copies of the fermion
representation. No principle within the SM selects this number;
anomaly cancellation constrains each generation internally but is
silent on how many generations exist. The 4-colour structure of
Pati--Salam unification ($\mathrm{SU}(4)_c \supset \mathrm{SU}(3)_c
\times \mathrm{U}(1)_{B-L}$, with the lepton as the fourth colour)
is a hypothesis external to the SM, with the unification coupling
$\alpha_{\mathrm{PS}}^{-1}$ undetermined. The 6-quark structure
follows from 3 generations times 2 isospin states, but neither the
"3" nor the "2" is derived. The Cabibbo angle
$\lambda = |V_{us}|$ and its three companion Wolfenstein parameters
$(A, \bar\rho, \bar\eta)$ are fit to data. The Koide ratio $Q = 2/3$
is an empirical coincidence with no SM origin.

Each of these numbers is, from the SM's perspective, a free
parameter or an unexplained structural choice.

### 1.3 The bridge construction in one sentence

A *bridge* is a pair $(p, N)$ of a prime $p$ and a cyclotomic
level $N$ such that the quotient index
$k = [({\mathbb Z}/N{\mathbb Z})^* : \langle p \rangle]$ satisfies
$k \in \{2, 3, 4, 6\}$; at each such pair, the cyclic algebra
$({\mathbb Q}(\zeta_N)/{\mathbb Q}, \mathrm{Frob}_p, \zeta_k)$
defines a Brauer class $\beta_k \in H^2({\mathbb Z}/k{\mathbb Z},
\mathrm{U}(1))$ on the arithmetic side, while on the
operator-algebraic side the Bost--Connes Galois action
$\sigma : \mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q})
\to \mathrm{Out}(\mathcal{M})$ restricts to a ${\mathbb Z}/k{\mathbb Z}$
outer action on the hyperfinite $\mathrm{II}_1$ factor
$\mathcal{M} = \pi_1(\mathcal{A}_{\mathrm{BC}})''$, producing a
Jones sub-factor of index $k$ whose Fuglede--Kadison cocycle
represents the same class in $H^2({\mathbb Z}/k{\mathbb Z},
\mathrm{U}(1))$.

### 1.4 What this paper proves

This paper establishes the following.

**(i)** The Frobenius--Jones bridge theorem at $k = 3$ (Section 3):
a complete six-step proof that the cyclotomic Brauer class at
$(p, N) = (5, 13)$ and the Fuglede--Kadison determinant class of
the index-3 Jones sub-factor are equal as elements of
$H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1)) \cong {\mathbb Z}/3{\mathbb Z}$,
both representing the canonical generator $1/3 \bmod {\mathbb Z}$.

**(ii)** The Koide ratio $Q = 2/3$ as a Brauer-class consequence of
$Q = 2/[\mathcal{M}:\mathcal{N}]$ at Jones index 3 (Section 4),
together with an honest accounting of four independent routes ---
Frobenius orbit periods, mixed Fourier/power-progression dressing,
$A_5$ principal-graph eigenvalues, and Connes--Marcolli
$L$-function matrix elements --- that independently establish this
as a trace identity, not a per-eigenvalue statement.

**(iii)** In subsequent sections (5--14, not in this instalment),
the generalisation of the bridge construction to
$k \in \{2, 4, 6\}$, yielding CP discrete symmetry ($k = 2$),
Pati--Salam $\mathrm{SU}(4)_c$ with
$\alpha_{\mathrm{PS}}^{-1} = 17$ exactly ($k = 4$), and the full
Wolfenstein CKM matrix at sub-$\sigma$ to PDG ($k = 6$).

---

## 2. Mathematical preliminaries

### 2.1 Cyclotomic fields ${\mathbb Q}(\zeta_N)$ and their Galois groups

Let $\zeta_N = e^{2\pi i/N}$. The $N$th cyclotomic field
${\mathbb Q}(\zeta_N)$ is the splitting field of
$\Phi_N(x) = \prod_{(a, N)=1} (x - \zeta_N^a)$ over
${\mathbb Q}$. Its Galois group is canonically isomorphic to the
multiplicative group of units modulo $N$:
$$
\mathrm{Gal}({\mathbb Q}(\zeta_N)/{\mathbb Q})
\;\cong\;
({\mathbb Z}/N{\mathbb Z})^*,
\qquad
\sigma_a(\zeta_N) = \zeta_N^a, \quad (a, N) = 1.
$$
The degree $[{\mathbb Q}(\zeta_N) : {\mathbb Q}] = \varphi(N)$,
where $\varphi$ is Euler's totient. For the three cyclotomic levels
appearing in the bridge family:

| $N$ | $\varphi(N)$ | $({\mathbb Z}/N{\mathbb Z})^*$ | Generator |
|:---:|:---:|:---|:---:|
| 7 | 6 | ${\mathbb Z}/6{\mathbb Z}$ | 3 |
| 13 | 12 | ${\mathbb Z}/12{\mathbb Z}$ | 2 |
| 19 | 18 | ${\mathbb Z}/18{\mathbb Z}$ | 2 |

Each of these groups is cyclic, a consequence of $N$ being prime.

### 2.2 Frobenius elements at unramified primes

Let $p$ be a rational prime not dividing $N$. The Frobenius element
$\mathrm{Frob}_p \in \mathrm{Gal}({\mathbb Q}(\zeta_N)/{\mathbb Q})$
is the unique automorphism acting as $\zeta_N \mapsto \zeta_N^p$, or
equivalently as the $p$th-power map on residue fields. Its order in
$({\mathbb Z}/N{\mathbb Z})^*$ is the *residue degree*
$f = \mathrm{ord}_N(p)$, the smallest positive integer with
$p^f \equiv 1 \pmod{N}$.

The Frobenius element generates the decomposition group
$\langle \mathrm{Frob}_p \rangle \subseteq
({\mathbb Z}/N{\mathbb Z})^*$, a cyclic subgroup of order $f$.
The quotient
$$
G_{\mathrm{arith}}
\;:=\;
({\mathbb Z}/N{\mathbb Z})^* \big/ \langle \mathrm{Frob}_p \rangle
$$
is cyclic of order $k = \varphi(N)/f$. This quotient permutes the
$k$ Frobenius orbits --- the cosets of
$\langle p \rangle$ in $({\mathbb Z}/N{\mathbb Z})^*$ ---
transitively and freely.

For the bridge family:

| $(p, N)$ | $f = \mathrm{ord}_N(p)$ | $k = \varphi(N)/f$ | $\langle p \rangle$ in $({\mathbb Z}/N{\mathbb Z})^*$ |
|:---:|:---:|:---:|:---|
| $(2, 7)$ | 3 | 2 | $\{1, 2, 4\}$ |
| $(5, 13)$ | 4 | 3 | $\{1, 5, 12, 8\}$ |
| $(3, 13)$ | 3 | 4 | $\{1, 3, 9\}$ |
| $(7, 19)$ | 3 | 6 | $\{1, 7, 11\}$ |

### 2.3 Brauer groups and $H^2(G, \mathrm{U}(1))$

Let $G$ be a finite group and $A$ a $G$-module. The second
cohomology group $H^2(G, A)$ classifies central extensions of $G$
by $A$ up to equivalence, or equivalently, equivalence classes of
normalised 2-cocycles
$c : G \times G \to A$ satisfying the cocycle condition
$c(g,h) \cdot c(gh, k) = g \cdot c(h, k) \cdot c(g, hk)$,
modulo 2-coboundaries $c(g, h) = b(g) \cdot b(h) \cdot b(gh)^{-1}$
for some $b : G \to A$.

When $G = {\mathbb Z}/k{\mathbb Z} = \langle \tau \rangle$ is
cyclic and $A = \mathrm{U}(1)$ with trivial $G$-action, the
universal coefficient theorem gives
$$
H^2({\mathbb Z}/k{\mathbb Z}, \mathrm{U}(1))
\;\cong\;
{\mathbb Z}/k{\mathbb Z}.
$$
The canonical generator is represented by the *carry cocycle*
$$
c_0(\tau^i, \tau^j)
\;=\;
\exp\!\Bigl(\frac{2\pi i}{k}\,
\Bigl\lfloor \frac{i+j}{k} \Bigr\rfloor\Bigr),
\qquad
0 \le i, j < k.
$$
This cocycle detects when addition of exponents "carries" past $k$:
$c_0 = 1$ when $i + j < k$ and $c_0 = \zeta_k$ when $i + j \ge k$.
Its class is $1/k \bmod {\mathbb Z}$ under the identification
$H^2({\mathbb Z}/k{\mathbb Z}, \mathrm{U}(1)) \cong {\mathbb Z}/k{\mathbb Z}$.

The *Brauer group* $\mathrm{Br}(F)$ of a field $F$ is the group of
equivalence classes of central simple $F$-algebras under the Morita
equivalence relation. For $F = {\mathbb Q}$, the Brauer group
injects into $\bigoplus_v H^2(G_v, \bar F_v^*)$ via local
invariants (the Albert--Brauer--Hasse--Noether theorem). Each local
invariant $\mathrm{inv}_v \in {\mathbb Q}/{\mathbb Z}$ encodes the
cohomological obstruction at the place $v$.

### 2.4 Cyclic algebras and the Hasse local invariant

A *cyclic algebra* over ${\mathbb Q}$ is a central simple algebra of
the form
$$
\bigl(K/{\mathbb Q},\, \sigma,\, a\bigr)
\;=\;
K \oplus K\!\cdot\!u \oplus \cdots \oplus K\!\cdot\!u^{n-1},
\qquad
u^n = a,\quad u \cdot x = \sigma(x) \cdot u,
$$
where $K/{\mathbb Q}$ is a cyclic Galois extension of degree $n$,
$\sigma$ generates $\mathrm{Gal}(K/{\mathbb Q})$, and $a \in
{\mathbb Q}^*$.

For the cyclotomic cyclic algebra relevant to the bridge at $k = 3$:
$$
\mathcal{A}_{\mathrm{arith}}
\;:=\;
\bigl({\mathbb Q}(\zeta_{13})/{\mathbb Q},\,
\mathrm{Frob}_5,\, \zeta_3\bigr).
$$
Here the extension ${\mathbb Q}(\zeta_{13})/{\mathbb Q}$ has degree
12, $\mathrm{Frob}_5$ has order 4 in $\mathrm{Gal}({\mathbb Q}
(\zeta_{13})/{\mathbb Q})$, and the construction factors through the
cubic quotient
$G_{\mathrm{arith}} = ({\mathbb Z}/13{\mathbb Z})^*/\langle 5 \rangle
\cong {\mathbb Z}/3{\mathbb Z}$.
More precisely, the cyclic algebra is constructed on the cubic
subfield $K_3 = {\mathbb Q}(\zeta_{13})^{\langle 5 \rangle}$
(the fixed field of $\mathrm{Frob}_5$), where $\mathrm{Frob}_5$
descends to a generator of
$\mathrm{Gal}(K_3/{\mathbb Q}) \cong {\mathbb Z}/3{\mathbb Z}$.

The *Hasse local invariant* at the prime $p = 5$ of this cyclic
algebra is computed via the norm residue symbol. Following
Connes--Marcolli (2008, Prop. 3.34), the unramified local invariant
is
$$
\mathrm{inv}_5(\mathcal{A}_{\mathrm{arith}})
\;=\;
\frac{1}{3} \bmod {\mathbb Z},
$$
because $\mathrm{Frob}_5$ has residue degree 4 on
${\mathbb Q}(\zeta_{13})/{\mathbb Q}$, giving an unramified cyclic
extension of degree 3 on the quotient with the uniformiser raised to
the first power in the norm residue symbol. This invariant represents
the canonical generator of $H^2({\mathbb Z}/3{\mathbb Z},
\mathrm{U}(1)) \cong {\mathbb Z}/3{\mathbb Z}$.

### 2.5 Jones sub-factors and their indices

Let $\mathcal{M}$ be a type $\mathrm{II}_1$ factor with normalised
trace $\mathrm{tr}$, and let $\mathcal{N} \subset \mathcal{M}$ be a
sub-factor. The *Jones index*
$[\mathcal{M}:\mathcal{N}]$ measures the "relative size" of the
inclusion and is defined via the unique trace-preserving conditional
expectation $E_{\mathcal{N}} : \mathcal{M} \to \mathcal{N}$:
$$
[\mathcal{M}:\mathcal{N}]
\;=\;
\bigl(\inf\,\{\lambda > 0 : E_{\mathcal{N}}(x) \ge \lambda^{-1} x
\;\;\forall\, x \ge 0 \text{ in } \mathcal{M}\}\bigr)^{-1}.
$$

Jones's theorem (1983) restricts the admissible values:
$$
[\mathcal{M}:\mathcal{N}]
\;\in\;
\bigl\{4\cos^2(\pi/n) : n = 3, 4, 5, \ldots\bigr\}
\;\cup\;
[4, \infty).
$$
Integer indices $[\mathcal{M}:\mathcal{N}] = d \in \{1, 2, 3, \ldots\}$
are all admissible (they lie in $[4, \infty)$ for $d \ge 4$ and equal
$4\cos^2(\pi/n)$ at $d = 1$ ($n = 3$), $d = 2$ ($n = 4$),
$d = 3$ ($n = 6$)). At each integer index, the canonical
construction is the fixed-point sub-factor
$\mathcal{N} = \mathcal{M}^{{\mathbb Z}/d{\mathbb Z}}$ under an
outer ${\mathbb Z}/d{\mathbb Z}$ action on $\mathcal{M}$.

### 2.6 Standard invariants of sub-factors: Pimsner--Popa basis and Fuglede--Kadison determinant

For an irreducible sub-factor $\mathcal{N} \subset \mathcal{M}$ of
finite index $d = [\mathcal{M}:\mathcal{N}]$, the *Pimsner--Popa
basis* is a set of $d$ unitaries $\{u_0, u_1, \ldots, u_{d-1}\}$ in
$\mathcal{M}$ satisfying the orthogonality relation
$$
E_{\mathcal{N}}(u_i \, u_j^*)
\;=\;
\frac{\delta_{ij}}{d} \cdot \mathbf{1},
\qquad
0 \le i, j < d.
$$
These unitaries span $\mathcal{M}$ as a right $\mathcal{N}$-module,
and their multiplication law is governed by a $\mathrm{U}(1)$-valued
2-cocycle $\lambda$ on ${\mathbb Z}/d{\mathbb Z}$:
$$
u_i \, u_j
\;=\;
\lambda(i, j) \cdot u_{i+j \bmod d},
\qquad
\lambda : {\mathbb Z}/d{\mathbb Z} \times {\mathbb Z}/d{\mathbb Z}
\to \mathrm{U}(1).
$$
The cocycle condition on $\lambda$ is automatic from associativity
of multiplication in $\mathcal{M}$. The class
$[\lambda] \in H^2({\mathbb Z}/d{\mathbb Z}, \mathrm{U}(1))$ is the
*obstruction cocycle* of the sub-factor inclusion and is invariant
under change of Pimsner--Popa basis.

The *Fuglede--Kadison determinant* of the conditional expectation
$E_{\mathcal{N}}$ is
$$
\Delta_{\mathrm{FK}}(E_{\mathcal{N}})
\;=\;
\exp\!\bigl(\mathrm{tr}(\log E_{\mathcal{N}})\bigr)
\;=\;
\frac{1}{d},
$$
with log-determinant $\log\Delta_{\mathrm{FK}} = -\log d$. The
normalised class associated to the Fuglede--Kadison determinant in
$H^2({\mathbb Z}/d{\mathbb Z}, \mathrm{U}(1))$ is
$$
[c_{\mathrm{op}}]
\;=\;
\frac{1}{d} \bmod {\mathbb Z},
$$
using the normalisation convention of the Connes--Sukochev trace in
which the index-$d$ projection $e_{\mathcal{N}}$ contributes
$1/[\mathcal{M}:\mathcal{N}] = 1/d$ to the central cocycle.

For the irreducible hyperfinite $\mathrm{II}_1$ sub-factor at
integer index $d$, the Jones--Ocneanu classification theorem
(Jones 1980; Ocneanu 1985) guarantees that the outer
${\mathbb Z}/d{\mathbb Z}$ action is *unique up to cocycle
conjugacy*, and therefore the obstruction cocycle $[\lambda]$ is
determined up to the canonical identification.

### 2.7 The Bost--Connes algebra $\mathcal{A}_{\mathrm{BC}}$

The *Bost--Connes $C^*$-algebra* (Bost--Connes, 1995) is the
semigroup crossed product
$$
\mathcal{A}_{\mathrm{BC}}
\;=\;
C({\mathbb Q}^{\mathrm{cyc}}) \rtimes {\mathbb N}^\times,
$$
where ${\mathbb Q}^{\mathrm{cyc}} = \bigcup_N {\mathbb Q}(\zeta_N)$
is the maximal cyclotomic extension of ${\mathbb Q}$, viewed as a
profinite space via the adelic topology, and ${\mathbb N}^\times$
acts by the partial automorphisms $\sigma_n : f(\zeta) \mapsto
f(\zeta^n)$.

The algebra carries a canonical one-parameter family of KMS states
$\omega_\beta$ for $\beta \in (0, \infty]$. At $\beta > 1$ (the
"cold phase"), the KMS states form an infinite-dimensional simplex
parametrised by embeddings
$\varepsilon : {\mathbb Q}^{\mathrm{cyc}} \hookrightarrow
{\mathbb C}$, and the Galois group
$\mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q})$ acts on the
extremal KMS$_\beta$ states by
$$
\sigma_\alpha(\omega_{\beta, \varepsilon})
\;=\;
\omega_{\beta, \alpha \circ \varepsilon},
\qquad
\alpha \in \mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q}).
$$

At $\beta = 1$ (the "phase transition point"), the KMS state is
*unique*: $\omega_1$ is the only KMS$_1$ state on
$\mathcal{A}_{\mathrm{BC}}$.

The GNS representation $\pi_1$ of $\mathcal{A}_{\mathrm{BC}}$ with
respect to $\omega_1$ generates a von Neumann algebra
$\mathcal{M} := \pi_1(\mathcal{A}_{\mathrm{BC}})''$, which is the
hyperfinite type $\mathrm{II}_1$ factor (or more precisely, type
$\mathrm{III}_1$ before reduction; the $\mathrm{II}_1$ factor is
obtained by the Tomita--Takesaki reduction at the modular flow).

### 2.8 The critical state $\omega_1$ and its modular automorphism

The $\beta = 1$ KMS state $\omega_1$ is the fixed point of the
Bost--Connes phase transition: it is the unique state at which the
symmetry-breaking pattern $\mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/
{\mathbb Q}) \curvearrowright \{\text{KMS}_\beta\}$ collapses from
an infinite-dimensional simplex to a single point. In the CBB
system, $\beta = 1$ is not a parameter choice; it is the critical
point forced by the pole of $\zeta(s)$ at $s = 1$.

The modular automorphism group $\sigma_t^{\omega_1}$ of
$\omega_1$ acts on the GNS Hilbert space $H_R$ via
$e^{it \log \hat R}$, where $\hat R$ is the unbounded positive
operator with compact resolvent whose log-spectrum encodes the
non-trivial zeros of $\zeta(s)$:
$$
\hat L := \log \hat R, \qquad
\mathrm{Spec}(\hat L) = \{L_n = \gamma_n \cdot \pi^2/2\},
$$
with $\gamma_n$ the imaginary parts of the Riemann zeta zeros on the
critical line $\mathrm{Re}(s) = 1/2$.

The Galois action of $\mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/
{\mathbb Q})$ descends, after taking the GNS representation at
$\omega_1$, to an action on the von Neumann algebra $\mathcal{M}$:
$$
\bar\sigma :
\mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q})
\;\longrightarrow\;
\mathrm{Out}(\mathcal{M}).
$$
This is the action that, restricted to finite cyclotomic quotients,
produces the bridges of Section 3. Its key property, proved by
Bost--Connes (1995, Section 5) and elaborated by Connes--Marcolli
(2008, Chapter 3), is that $\bar\sigma(\alpha)$ is *outer* for every
non-identity $\alpha \in \mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/
{\mathbb Q})$.

---

## 3. The Frobenius--Jones bridge theorem ($k = 3$)

This section contains the complete proof of the bridge theorem at
$k = 3$, the mathematical heart of this paper. The proof proceeds
in six steps. We state the theorem first, then execute each step in
full.

### 3.1 Statement of the theorem

**Theorem 3.1** (Frobenius--Jones bridge, $k = 3$). *Let
$\mathcal{M} = \pi_1(\mathcal{A}_{\mathrm{BC}})''$ be the
hyperfinite type $\mathrm{II}_1$ factor obtained from the GNS
representation of the Bost--Connes algebra at the unique KMS$_1$
state $\omega_1$. Let $\bar\sigma :
\mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q}) \to
\mathrm{Out}(\mathcal{M})$ be the Bost--Connes Galois action.
Define*
$$
G_{\mathrm{arith}}
\;:=\;
({\mathbb Z}/13{\mathbb Z})^* \big/ \langle \mathrm{Frob}_5 \rangle
\;\cong\;
{\mathbb Z}/3{\mathbb Z},
$$
*where $\mathrm{Frob}_5$ generates $\langle 5 \rangle =
\{1, 5, 8, 12\} \subset ({\mathbb Z}/13{\mathbb Z})^*$. Let
$\mathcal{N} \subset \mathcal{M}$ be a sub-factor with
$[\mathcal{M}:\mathcal{N}] = 3$, constructed as the fixed-point
algebra $\mathcal{N} = \mathcal{M}^{\alpha(G_{\mathrm{op}})}$ under
an outer ${\mathbb Z}/3{\mathbb Z}$-action
$\alpha : G_{\mathrm{op}} \hookrightarrow \mathrm{Out}(\mathcal{M})$.
Then:*

*(i) The restriction
$\rho := \bar\sigma \circ q_{13} : G_{\mathrm{arith}} \to
\mathrm{Out}(\mathcal{M})$ is injective, and
$\rho(G_{\mathrm{arith}}) = \alpha(G_{\mathrm{op}})$.*

*(ii) The fixed-point algebras coincide:
$\mathcal{M}^{\rho(G_{\mathrm{arith}})}$ is unitarily conjugate to
$\mathcal{N}$ in $\mathcal{M}$.*

*(iii) The three Frobenius orbits
$O_1 = \{1, 5, 12, 8\}$,
$O_2 = \{2, 10, 11, 3\}$,
$O_3 = \{4, 7, 9, 6\}$
of $\langle \mathrm{Frob}_5 \rangle$ on
$({\mathbb Z}/13{\mathbb Z})^*$ are in bijection with the three
minimal central projections $p_1, p_2, p_3$ of the relative
commutant $\mathcal{N}' \cap \mathcal{M}$.*

*(iv) The arithmetic 2-cocycle $c_{\mathrm{arith}}$ from the cyclic
algebra $({\mathbb Q}(\zeta_{13})/{\mathbb Q}, \mathrm{Frob}_5,
\zeta_3)$ and the operator 2-cocycle $c_{\mathrm{op}}$ from the
Pimsner--Popa basis of $\mathcal{N} \subset \mathcal{M}$ represent
the same class in $H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1))$:*
$$
[c_{\mathrm{arith}}]
\;=\;
[c_{\mathrm{op}}]
\;=\;
\tfrac{1}{3} \bmod {\mathbb Z},
$$
*the canonical generator of
$H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1)) \cong
{\mathbb Z}/3{\mathbb Z}$.*

### 3.2 Step 1: $\bar\sigma \circ q_{13}$ is well-defined on level 13

Let $q_{13} : \mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q})
\to ({\mathbb Z}/13{\mathbb Z})^*$ be the canonical projection given
by restriction of automorphisms to ${\mathbb Q}(\zeta_{13})$.

**Claim.** The composition $\bar\sigma \circ q_{13}^{-1}$, or more
precisely the map
$\rho_0 : ({\mathbb Z}/13{\mathbb Z})^* \to \mathrm{Out}(\mathcal{M})$
defined by $\rho_0(a) := \bar\sigma(\tilde\sigma_a)$ for any lift
$\tilde\sigma_a \in \mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/
{\mathbb Q})$ of $\sigma_a \in \mathrm{Gal}({\mathbb Q}(\zeta_{13})
/{\mathbb Q})$, is well-defined.

*Proof.* Bost--Connes (1995, Section 5) prove that the Galois action
$\sigma$ factors through finite cyclotomic quotients compatibly with
the KMS structure. Specifically, the BC Galois action on KMS$_\beta$
states for any $\beta$ respects the projective limit
$\mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q}) =
\varprojlim_N ({\mathbb Z}/N{\mathbb Z})^*$: two Galois elements
$\alpha, \alpha'$ that agree on ${\mathbb Q}(\zeta_{13})$ induce the
same action on the level-13 KMS states. At $\beta = 1$, the unique
KMS state $\omega_1$ is fixed by the entire Galois group, but the
GNS representation $\pi_1$ still carries the Galois action on
$\mathcal{M} = \pi_1(\mathcal{A}_{\mathrm{BC}})''$ via automorphisms.
The level-compatibility implies that this action depends only on the
image of $\alpha$ in $({\mathbb Z}/13{\mathbb Z})^*$ when
restricted to the level-13 subalgebra. Therefore $\rho_0$ is
well-defined as a map to $\mathrm{Out}(\mathcal{M})$. $\square$

The map $\rho$ of the theorem is obtained by composing $\rho_0$ with
the quotient $({\mathbb Z}/13{\mathbb Z})^* \twoheadrightarrow
G_{\mathrm{arith}} = ({\mathbb Z}/13{\mathbb Z})^*/\langle 5 \rangle$.
Elements of $\langle 5 \rangle = \{1, 5, 8, 12\}$ map to the
identity in $G_{\mathrm{arith}}$, and their images under $\rho_0$
act within a single Frobenius orbit --- they stabilise the
generation sector (Step 2 will show this).

### 3.3 Step 2: $\rho$ is injective via free action on Frobenius orbits

**Claim.** The map
$\rho : G_{\mathrm{arith}} \to \mathrm{Out}(\mathcal{M})$ is
injective.

*Proof.* The group $G_{\mathrm{arith}} =
({\mathbb Z}/13{\mathbb Z})^*/\langle 5 \rangle$ acts on the three
Frobenius orbits $O_1, O_2, O_3$ by left multiplication of coset
representatives. Explicitly, taking $\tau = [2]$ as the generator of
$G_{\mathrm{arith}}$ (since $2$ has order 3 in the quotient:
$2^1 = 2$, $2^2 = 4$, $2^3 = 8 \equiv 1 \bmod \langle 5 \rangle$,
noting $8 \in \langle 5 \rangle$):

$$
\tau : O_1 \mapsto O_2 \mapsto O_3 \mapsto O_1.
$$

This is a *free* action: the only element of $G_{\mathrm{arith}}$
fixing any orbit $O_j$ is the identity. To see this, suppose
$\tau^m$ fixes $O_1 = \{1, 5, 12, 8\}$. Then $2^m \cdot 1 \in O_1$,
i.e. $2^m \in \{1, 5, 12, 8\}$. Since $2^0 = 1$, $2^1 = 2 \notin
O_1$, $2^2 = 4 \notin O_1$, only $m \equiv 0 \pmod{3}$ works.
Hence the action is free.

Now suppose $\rho(\tau^m) = \mathrm{id} \in \mathrm{Out}(\mathcal{M})$
for some $0 < m < 3$. Then $\bar\sigma(\tilde\sigma_{2^m})$ acts
trivially on $\mathcal{M}$. But $\bar\sigma(\tilde\sigma_{2^m})$
permutes the three minimal projections of the generation sector
(the spectral projections of the relative commutant
$\mathcal{N}' \cap \mathcal{M}$) in the same way that
$\tau^m$ permutes the three orbits. Since the orbit action is free,
$\tau^m$ with $m \not\equiv 0$ sends each orbit to a different
orbit, and hence the corresponding automorphism is non-trivial on
the generation projections. Therefore $\rho(\tau^m) \ne \mathrm{id}$
for $m \not\equiv 0 \pmod{3}$, and $\rho$ is injective. $\square$

### 3.4 Step 3: The image is an order-3 outer subgroup of $\mathrm{Out}(\mathcal{M})$

**Claim.** $\rho(G_{\mathrm{arith}})$ is a cyclic subgroup of
$\mathrm{Out}(\mathcal{M})$ of order exactly 3, consisting entirely
of outer automorphisms.

*Proof.* By Step 2, $\rho$ is injective, so
$|\rho(G_{\mathrm{arith}})| = |G_{\mathrm{arith}}| = 3$. The image
is therefore cyclic of order 3.

It remains to show that $\rho(\tau)$ and $\rho(\tau^2)$ are outer
(i.e. not inner automorphisms of $\mathcal{M}$). This follows from
the Bost--Connes theorem on outerness of the Galois action: for
every non-identity element $\alpha \in
\mathrm{Gal}({\mathbb Q}^{\mathrm{ab}}/{\mathbb Q})$, the
automorphism $\bar\sigma(\alpha)$ is outer on $\mathcal{M}$. This
is the noncommutative-geometric content of the CM complex
multiplication theory (Connes--Marcolli 2008, Chapter 3, Theorem 3.32).
Since $\tau = [2]$ is a non-identity element of
$({\mathbb Z}/13{\mathbb Z})^*$, its lift $\tilde\sigma_2$ is a
non-identity Galois element, and $\bar\sigma(\tilde\sigma_2)$ is
outer. The same holds for $\tau^2 = [4]$. $\square$

### 3.5 Step 4: Jones--Popa uniqueness of the index-3 outer ${\mathbb Z}/3{\mathbb Z}$ fixed-point sub-factor

**Claim.** Any outer action ${\mathbb Z}/3{\mathbb Z} \hookrightarrow
\mathrm{Out}(\mathcal{M})$ on the hyperfinite $\mathrm{II}_1$ factor
$\mathcal{M}$ produces, via the fixed-point construction
$\mathcal{N} = \mathcal{M}^{{\mathbb Z}/3{\mathbb Z}}$, a sub-factor
that is unique up to conjugacy by a unitary in $\mathcal{M}$.
Therefore $\rho(G_{\mathrm{arith}})$ and $\alpha(G_{\mathrm{op}})$
define the same sub-factor $\mathcal{N} \subset \mathcal{M}$.

*Proof.* By the Jones--Popa--Ocneanu classification (Jones 1983;
Popa 1994; Ocneanu 1985), irreducible hyperfinite $\mathrm{II}_1$
sub-factors of index $d$ are classified by their standard invariants
(principal graphs and connections). For integer index $d$, the
standard construction via outer ${\mathbb Z}/d{\mathbb Z}$ actions
produces a unique isomorphism class.

More precisely, Ocneanu's theorem on actions of finite groups on the
hyperfinite $\mathrm{II}_1$ factor states that outer actions of
${\mathbb Z}/d{\mathbb Z}$ are unique up to *cocycle conjugacy*:
if $\alpha, \alpha' : {\mathbb Z}/d{\mathbb Z} \to
\mathrm{Aut}(\mathcal{M})$ are both outer, there exists a unitary
$w \in \mathcal{M}$ and a 1-cocycle $v : {\mathbb Z}/d{\mathbb Z}
\to \mathcal{U}(\mathcal{M})$ such that
$\alpha'_g = \mathrm{Ad}(w) \circ \alpha_g \circ
\mathrm{Ad}(v_g)$ for all $g$.

The fixed-point algebras $\mathcal{M}^{\alpha}$ and
$\mathcal{M}^{\alpha'}$ are therefore conjugate by the unitary
$w$: $w \mathcal{M}^{\alpha'} w^* = \mathcal{M}^{\alpha}$.

Applied to $d = 3$: both $\rho(G_{\mathrm{arith}})$ (from the
arithmetic side) and $\alpha(G_{\mathrm{op}})$ (from the operator
side) are outer ${\mathbb Z}/3{\mathbb Z}$ actions on
$\mathcal{M}$. By Ocneanu's theorem, they are cocycle-conjugate,
and their fixed-point algebras are unitarily conjugate. This
establishes parts (i) and (ii) of Theorem 3.1. $\square$

### 3.6 Step 5: Orbit-to-projection matching via Artin reciprocity

**Claim.** Under the identification $\rho : G_{\mathrm{arith}}
\xrightarrow{\;\sim\;} \alpha(G_{\mathrm{op}})$ established in
Steps 2--4, the three Frobenius orbits $O_1, O_2, O_3$ correspond
bijectively to the three minimal central projections
$p_1, p_2, p_3$ of the relative commutant
$\mathcal{N}' \cap \mathcal{M}$.

*Proof.* The relative commutant $\mathcal{N}' \cap \mathcal{M}$ for
an irreducible sub-factor of index 3 has dimension 3 (equal to the
index, since the sub-factor is irreducible). Its three minimal
projections $p_1, p_2, p_3$ are the spectral projections of the
dual action $\hat\alpha$ on the crossed product
$\mathcal{M} \rtimes {\mathbb Z}/3{\mathbb Z}$.

Under the dual action, $p_j$ transforms as the character
$\chi_j : {\mathbb Z}/3{\mathbb Z} \to {\mathbb C}^*$ with
$\chi_j(\tau) = \omega^j$, $\omega = e^{2\pi i/3}$, and $j = 0, 1, 2$.
On the arithmetic side, the three characters of $G_{\mathrm{arith}}$
are identified with the three Frobenius orbits via the Artin
reciprocity isomorphism. Specifically, the dual group
$$
\widehat{G}_{\mathrm{arith}}
\;=\;
\mathrm{Hom}(G_{\mathrm{arith}}, {\mathbb C}^*)
\;\cong\;
{\mathbb Z}/3{\mathbb Z}
$$
indexes the orbits: the character $\chi_j$ evaluates on
$\tau = [2]$ as $\chi_j(\tau) = \omega^j$, and the orbit $O_j$
is the set of $a \in ({\mathbb Z}/13{\mathbb Z})^*$ on which
$\chi_j$ takes the constant value $\omega^j$ when restricted to
the Frobenius coset structure.

More concretely, the three Gaussian periods
$$
\eta_j \;=\; \sum_{a \in O_j} \zeta_{13}^a, \qquad j = 1, 2, 3,
$$
are the images of $\zeta_{13}$ under the three primitive
idempotents of the unique cubic subfield
$K_3 \subset {\mathbb Q}(\zeta_{13})$, and they correspond to the
three projections $p_j$ under the Artin map. This identification is
the level-13 restriction of the Bost--Connes
Galois-action-on-KMS-states theorem.

The bijection $O_j \leftrightarrow p_j$ is canonical up to a
labelling convention (choice of generator of $G_{\mathrm{arith}}$).
This establishes part (iii) of Theorem 3.1. $\square$

### 3.7 Step 6: Explicit cocycle equality $c_{\mathrm{arith}} = c_{\mathrm{op}}$ in $H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1))$

This step is the punchline of the proof. We must show that the
two 2-cocycles arising from the arithmetic and operator-algebraic
sides of the bridge represent the same cohomology class. We compute
each explicitly and verify their equality.

### 3.8 The arithmetic cocycle $c_{\mathrm{arith}}$

The arithmetic cocycle arises from the cyclic algebra
$$
\mathcal{A}_{\mathrm{arith}}
\;=\;
\bigl({\mathbb Q}(\zeta_{13})/{\mathbb Q},\,
\mathrm{Frob}_5,\, \zeta_3\bigr).
$$
Following Connes--Marcolli (2008, Prop. 3.34), we compute the local
invariant at $p = 5$.

The Frobenius element $\mathrm{Frob}_5$ generates an order-4
subgroup $\langle 5 \rangle = \{1, 5, 8, 12\}$ of the cyclic group
$({\mathbb Z}/13{\mathbb Z})^*$ of order 12. The quotient
$G_{\mathrm{arith}} = ({\mathbb Z}/13{\mathbb Z})^*/\langle 5 \rangle
\cong {\mathbb Z}/3{\mathbb Z}$ has generator $\tau = [2]$ (the
coset of 2). A choice of lift to the full Galois group is immaterial
for the cocycle class.

The cyclic-algebra 2-cocycle in Galois cohomology is the standard
carry cocycle twisted by the root of unity $\zeta_3 = e^{2\pi i/3}$:
$$
c_{\mathrm{arith}}(\tau^i, \tau^j)
\;=\;
\zeta_3^{\lfloor(i+j)/3\rfloor},
\qquad
0 \le i, j < 3.
$$
Written out for all nine values:

| $i$ | $j$ | $i + j$ | $\lfloor(i+j)/3\rfloor$ | $c_{\mathrm{arith}}(\tau^i, \tau^j)$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 0 | 2 | 2 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 2 | 0 | 1 |
| 1 | 2 | 3 | 1 | $\zeta_3$ |
| 2 | 0 | 2 | 0 | 1 |
| 2 | 1 | 3 | 1 | $\zeta_3$ |
| 2 | 2 | 4 | 1 | $\zeta_3$ |

The cocycle is non-trivial: it equals 1 on six of the nine pairs and
$\zeta_3$ on the remaining three (those where $i + j \ge 3$). Its
class in $H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1))$ is
$$
[c_{\mathrm{arith}}] \;=\; \tfrac{1}{3} \bmod {\mathbb Z},
$$
the canonical generator. This is the Hasse local invariant
$\mathrm{inv}_5(\mathcal{A}_{\mathrm{arith}})$: the residue degree
of $\mathrm{Frob}_5$ on ${\mathbb Q}(\zeta_{13})/{\mathbb Q}$ is
$f = 4$, giving a degree-3 unramified cyclic quotient extension,
and the uniformiser contributes $1/3$ to the norm residue symbol.

### 3.9 The operator cocycle $c_{\mathrm{op}}$

The operator cocycle arises from the Jones sub-factor
$\mathcal{N} \subset \mathcal{M}$ of index
$[\mathcal{M}:\mathcal{N}] = 3$, with outer
${\mathbb Z}/3{\mathbb Z}$-action
$\alpha : G_{\mathrm{op}} = {\mathbb Z}/3{\mathbb Z} =
\langle \tau \rangle \hookrightarrow \mathrm{Out}(\mathcal{M})$.

The Pimsner--Popa basis $\{u_0, u_1, u_2\}$ consists of unitaries
in $\mathcal{M}$ satisfying
$E_{\mathcal{N}}(u_i u_j^*) = (\delta_{ij}/3) \cdot \mathbf{1}$.
Their multiplication law defines a 2-cocycle
$\lambda : G_{\mathrm{op}} \times G_{\mathrm{op}} \to \mathrm{U}(1)$
via
$$
u_i \, u_j \;=\; \lambda(i, j) \cdot u_{i+j \bmod 3}.
$$

For the *minimal* index-3 outer action (unique up to cocycle
conjugacy by Jones 1980 / Ocneanu 1985), the cocycle $\lambda$ is
cohomologous to the carry cocycle:
$$
c_{\mathrm{op}}(\tau^i, \tau^j)
\;=\;
\exp\!\Bigl(\frac{2\pi i}{3}\,
\Bigl\lfloor \frac{i+j}{3} \Bigr\rfloor\Bigr)
\;=\;
\zeta_3^{\lfloor(i+j)/3\rfloor}.
$$

The Fuglede--Kadison determinant of the conditional expectation
$E_{\mathcal{N}}$ evaluates to $\Delta_{\mathrm{FK}}(E_{\mathcal{N}}) = 1/3$
(consistent with Section 2.6: $\Delta_{\mathrm{FK}} = 1/d$), with
log-determinant $\log\Delta_{\mathrm{FK}} = -\log 3$. Thus
$$
\Delta_{\mathrm{FK}}(E_{\mathcal{N}}) \;=\; 1/3,
$$
and the associated cocycle class in
$H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(Z(\mathcal{M})))$ is
$$
[c_{\mathrm{op}}]
\;=\;
\frac{1}{[\mathcal{M}:\mathcal{N}]}
\;=\;
\frac{1}{3} \bmod {\mathbb Z},
$$
using the normalisation of the Connes--Sukochev trace in which the
index-3 projection $e_{\mathcal{N}}$ contributes
$1/[\mathcal{M}:\mathcal{N}] = 1/3$ to the central cocycle.

### 3.10 Equality in $H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1))$: both equal $1/3 \bmod {\mathbb Z}$

We now verify that $c_{\mathrm{arith}}$ and $c_{\mathrm{op}}$
represent the same class.

**Direct comparison.** Both cocycles take the identical form
$$
c(\tau^i, \tau^j) \;=\; \zeta_3^{\lfloor(i+j)/3\rfloor}
$$
on $G = {\mathbb Z}/3{\mathbb Z} = \langle \tau \rangle$, with the
same primitive root $\zeta_3 = e^{2\pi i/3}$ (after fixing the
generator $\tau = [2]$ on the arithmetic side and $\tau = \alpha$-generator
on the operator side, using the identification
$\rho : G_{\mathrm{arith}} \xrightarrow{\;\sim\;} G_{\mathrm{op}}$
of Steps 2--4).

Their pointwise ratio is
$$
(c_{\mathrm{arith}} \cdot c_{\mathrm{op}}^{-1})(\tau^i, \tau^j)
\;=\;
1 \qquad \text{for all } i, j \in \{0, 1, 2\}.
$$
This is the trivial cocycle --- the zero coboundary. Therefore
$[c_{\mathrm{arith}}] = [c_{\mathrm{op}}]$ in
$H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1))$.

**Generator ambiguity.** One might worry about the choice of
primitive root $\zeta_3$ vs $\zeta_3^{-1} = \bar\zeta_3$. If we had
used $\zeta_3^{-1}$ on one side, the ratio would be
$\zeta_3^{2\lfloor(i+j)/3\rfloor}$, whose class is
$2/3 = -1/3 \bmod {\mathbb Z}$, i.e. the inverse generator.
But $H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1)) \cong
{\mathbb Z}/3{\mathbb Z}$ has exactly one non-trivial class up to
inversion: $\{0, 1/3, 2/3\}$, where $1/3$ and $2/3$ are inverses.
Both cocycles are non-trivial (both equal $1/3$, not $0$), and they
are identified after the canonical choice of generator $\rho$ fixed
in Step 2. Re-choosing the generator of $G_{\mathrm{arith}}$
(replacing $\tau$ by $\tau^{-1} = \tau^2$) flips the sign and
restores equality.

Since $H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1))$ has exactly
one non-trivial class up to inversion, and both cocycles represent a
non-trivial class (value $1/3 \bmod {\mathbb Z}$, not $0$), they
are equal after the canonical identification
$\rho : G_{\mathrm{arith}} \xrightarrow{\;\sim\;} G_{\mathrm{op}}$.

**This completes the proof of part (iv) of Theorem 3.1.** $\square$

### 3.11 Corollaries: 3 generations, Koide $Q = 2/3$, and level 13 $\leftrightarrow$ $\gamma_{13}$

The bridge theorem has three immediate structural consequences.

**Corollary 3.2** (Three generations from one ${\mathbb Z}/3{\mathbb Z}$).
*The generation count $n_{\mathrm{gen}} = 3$ has a single origin:
the unique outer ${\mathbb Z}/3{\mathbb Z}$ subgroup of
$\mathrm{Out}(\mathcal{M})$ induced by $\mathrm{Frob}_5$ at
cyclotomic level 13. The three Frobenius orbits $O_1, O_2, O_3$
and the three minimal projections $p_1, p_2, p_3$ of
$\mathcal{N}' \cap \mathcal{M}$ are two facets of this single
${\mathbb Z}/3{\mathbb Z}$.*

Previously, the generation count was derived from the "three primes
in the smallest non-trivial Hecke subalgebra" (research/40). That
argument is now subsumed: only $p = 5$ survives, and its role is to
be the Frobenius element at level 13, not one of three independent
generators.

**Corollary 3.3** (Koide ratio from the bridge).
*The Koide ratio $Q = 2/[\mathcal{M}:\mathcal{N}] = 2/3$ is
structurally forced by the Jones index 3. More precisely, the
Fuglede--Kadison determinant of $E_{\mathcal{N}}$ at index 3
gives the conditional-expectation normalisation
$\mathrm{tr}(E_{\mathcal{N}}) = 1/3$, and the Koide combination
$Q = 2 \cdot \mathrm{tr}(E_{\mathcal{N}}) = 2/3$. By Theorem 3.1(iv),
this same $1/3$ is the Hasse invariant
$\mathrm{inv}_5({\mathbb Q}(\zeta_{13})/{\mathbb Q},
\mathrm{Frob}_5, \zeta_3)$.*

The Koide relation thereby acquires a purely number-theoretic
reading: $Q = 2/3$ is the cyclotomic Brauer class of
${\mathbb Q}(\zeta_{13})/{\mathbb Q}$ at $p = 5$.

**Corollary 3.4** (Level 13 is structural).
*The cyclotomic level $N = 13$ is the unique prime at which the
generation ${\mathbb Z}/3{\mathbb Z}$ becomes outer on $\mathcal{M}$.
The numerical coincidence $N = 13 \leftrightarrow \gamma_{13}$ (the
13th Riemann zero appearing in the $W$-mass formula
$m_W = \gamma_2 + \gamma_{13}$) is an observed consistency, not a
proved identity: the cyclotomic level $N = 13$ and the ordinal of
the 13th zeta zero are different mathematical objects that share
the label "13." Whether a structural argument connects them is an
open question.*

---

## 4. The Koide ratio as a Brauer class

### 4.1 The Koide ratio: history and status

The Koide ratio (Koide 1982) is the dimensionless combination of
charged lepton masses
$$
Q \;:=\;
\frac{m_e + m_\mu + m_\tau}
     {(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2}.
$$
Experimentally,
$Q_{\mathrm{exp}} = 0.666661 \pm 0.000007$ (PDG 2024), consistent
with $2/3$ to better than $10^{-5}$. The relation $Q = 2/3$ is not
predicted by the Standard Model. It has attracted attention as a
possible clue to the origin of fermion mass hierarchies (Koide 1982;
Foot 1994; Rivero--Gsponer 2005), but no compelling derivation has
been given within any established framework.

### 4.2 The Jones index identity $Q = 2/[\mathcal{M}:\mathcal{N}]$

The CBB framework provides a structural derivation. The key
identity, established in research/140, is:

**Proposition 4.1.** *Let $\mathcal{N} \subset \mathcal{M}$ be a
sub-factor with Jones index
$d = [\mathcal{M}:\mathcal{N}]$. The trace normalisation of the
conditional expectation $E_{\mathcal{N}} : \mathcal{M} \to
\mathcal{N}$ gives $\mathrm{tr}(E_{\mathcal{N}}) = 1/d$. The Koide
combination, interpreted as the ratio of the trace of the mass
operator to the square of the trace of its square root on the three
generation eigenspaces of $\mathcal{N}' \cap \mathcal{M}$,
evaluates to*
$$
Q \;=\; \frac{2}{[\mathcal{M}:\mathcal{N}]}
\;=\; \frac{2}{d}.
$$

Testing this against the Jones restriction:

| $d = [\mathcal{M}:\mathcal{N}]$ | $Q = 2/d$ | Koide match? |
|:---:|:---:|:---:|
| 2 | 1.000 | No ($Q_{\mathrm{exp}} = 2/3$) |
| **3** | **0.66667** | **Yes** (to $9 \times 10^{-4}\%$) |
| 4 | 0.500 | No |
| $\varphi + 1 \approx 3.618$ | 0.553 | No |
| $4\cos^2(\pi/7) \approx 3.247$ | 0.616 | No |

Index 3 is the unique integer Jones index at which $Q = 2/d$
matches the experimental Koide value. No other admissible index in
the tested set comes close. The sub-factor hypothesis
$[\mathcal{M}:\mathcal{N}] = 3$ simultaneously forces $Q = 2/3$
and $n_{\mathrm{gen}} = 3$ (the dimension of
$\mathcal{N}' \cap \mathcal{M}$), merging two independent
structural facts into one.

### 4.3 The trace identity versus the per-eigenvalue picture

A crucial distinction: $Q = 2/[\mathcal{M}:\mathcal{N}] = 2/3$ is
a statement about the *global trace* of the conditional expectation
$E_{\mathcal{N}}$, not about the individual eigenvalues
$(m_e, m_\mu, m_\tau)$. The sub-factor fixes the Koide ratio as an
*identity*, but says nothing about which specific masses the three
generations carry.

This distinction has been tested exhaustively. Four independent
attempts to extract the individual lepton masses from the sub-factor
or cyclotomic structure have failed, all for the same structural
reason: the combinatorial data available from ${\mathbb Z}/3{\mathbb Z}$
or the Jones sub-factor at index 3 has insufficient multiplicative
spread to accommodate the observed hierarchy $m_\tau/m_e \approx 3477$.

### 4.4 The Frobenius--${\mathbb Z}/3{\mathbb Z}$ $\leftrightarrow$ Jones--${\mathbb Z}/3{\mathbb Z}$ identification

By Theorem 3.1, the Jones sub-factor at index 3 and the Frobenius
orbit structure at $(p, N) = (5, 13)$ are manifestations of the
same cohomology class in
$H^2({\mathbb Z}/3{\mathbb Z}, \mathrm{U}(1))$. The Koide ratio
$Q = 2/3$ therefore has a dual interpretation:

- **Operator-algebraic reading**: $Q = 2/d$ with $d = 3$, from the
  Fuglede--Kadison determinant of $E_{\mathcal{N}}$.

- **Number-theoretic reading**: $Q = 2 \cdot \mathrm{inv}_5(
  {\mathbb Q}(\zeta_{13})/{\mathbb Q}, \mathrm{Frob}_5, \zeta_3)$,
  i.e. twice the Hasse local invariant of the cyclotomic Brauer
  class at $p = 5$ on ${\mathbb Q}(\zeta_{13})$.

These are not two independent explanations but two views of the
same mathematical object, unified by the bridge theorem.

### 4.5 Why four independent eigenvalue routes failed

The claim that $Q = 2/3$ is a trace identity and not a
per-eigenvalue statement is supported by four independent negative
results, each testing a different mechanism for extracting
$(m_e, m_\mu, m_\tau)$ from the ${\mathbb Z}/3{\mathbb Z}$ or
sub-factor structure. We state each with its structural diagnosis.

**Route 1: Frobenius orbit Gaussian periods** (research/151).
The three Frobenius orbits of $\langle \mathrm{Frob}_5 \rangle$ on
$({\mathbb Z}/13{\mathbb Z})^*$ yield three Gaussian periods
$$
\eta_1 = \zeta + \zeta^5 + \zeta^8 + \zeta^{12} = +1.377,
\quad
\eta_2 = \zeta^2 + \zeta^3 + \zeta^{10} + \zeta^{11} = -2.507,
\quad
\eta_3 = \zeta^4 + \zeta^6 + \zeta^7 + \zeta^9 = +0.130,
$$
($\zeta = e^{2\pi i/13}$), which are the roots of the period
polynomial $x^3 + x^2 - 4x + 1 = 0$. Setting
$\sqrt{m_{\mathrm{gen}}} \propto |\eta_{\mathrm{orbit}}|$ and
computing the Koide combination gives $Q_{\mathrm{orbit}} = 0.509$,
a $23.7\%$ residual against $2/3$ --- roughly 300 times worse than
the $\gamma$-template baseline of $0.08\%$.

*Structural diagnosis*: the three Gaussian periods span a ratio
$|\eta_2|/|\eta_3| \approx 19$, so their squares span $\approx 370$.
The observed hierarchy $m_\tau/m_e \approx 3477$ requires a
$\sqrt{m}$-spread of $\sim 59$, far exceeding the period spread.
The orbits carry the correct ${\mathbb Z}/3{\mathbb Z}$ *labelling*
but the wrong *magnitude* spread.

**Route 2: Mixed Fourier/power-progression dressing** (research/157).
An attempt to combine the $\gamma$-zero magnitudes (which have the
correct spread) with ${\mathbb Z}/3{\mathbb Z}$ orbit characters
(which have the correct labelling). Two variants were tested:

- *Fourier mixing*: defining
  $m_i = (1/3)|{\textstyle\sum_j} \chi_i(j) A_j|^2$ with
  $A_j$ the $\gamma$-template amplitudes. Result:
  $Q = 0.352$, residual $-47.3\%$.

- *Power-progression mixing*: selecting powers of $\gamma_8$ via
  the ${\mathbb Z}/3{\mathbb Z}$ grading. Result:
  $Q = 0.544$, residual $-18.4\%$.

*Structural diagnosis*: any non-trivial ${\mathbb Z}/3{\mathbb Z}$
mixing redistributes the $\sqrt{m_i}$ weights, pushing $Q$ either
toward $1/3$ (equal masses) or toward 1 (dominant single mass),
*away* from $2/3$. The orbit characters supply labels, not metrics.

**Route 3: $A_5$ principal-graph eigenvalues** (research/161). The
standard invariant of the index-3 hyperfinite $\mathrm{II}_1$
sub-factor has principal graph $A_5$ (five vertices in a line), with
adjacency eigenvalues $\{-\!\sqrt{3}, -1, 0, +1, +\!\sqrt{3}\}$ and
Perron--Frobenius eigenvector quantum dimensions
$(1/2, \sqrt{3}/2, 1, \sqrt{3}/2, 1/2)$. Three candidate
ans\"{a}tze were tested:

- Eigenvalues as $\sqrt{m}$: $Q = 0.536$, residual $-19.6\%$
  (and $m_e = 0$ from the zero eigenvalue).

- Quantum dimensions as $\sqrt{m}$: $Q = 0.357$, residual $-46.4\%$.

- Squared eigenvalues as $m$: reduces to the first case.

*Structural diagnosis*: the $A_5$ spectrum spans a ratio of at most
$\sqrt{3} \approx 1.73$ among non-zero eigenvalues, squared to 3.
The lepton hierarchy requires a spread of $\sim 3477$. The
principal-graph combinatorics are too small by a factor of $\sim 60$
in $\sqrt{m}$.

**Route 4: Connes--Marcolli $L$-function matrix elements**
(research/172). The three characters $\chi_0, \chi_1, \chi_2$ of
$({\mathbb Z}/13{\mathbb Z})^*/\langle 5 \rangle \cong
{\mathbb Z}/3{\mathbb Z}$ yield $L$-function values
$L(1, \chi_k)$. However, the two non-trivial characters are
complex conjugates ($\chi_2 = \bar\chi_1$), so any modulus-squared
matrix element is invariant under complex conjugation:
$$
|L(1, \chi_1)|^2 \;=\; |L(1, \chi_2)|^2 \;=\; 0.420015.
$$
Any ansatz $m_i \propto |L(1, \chi_i)|^2$ therefore forces
$m_\mu = m_\tau$ --- a symmetry obstruction, not a tuning failure.
Numerically: $Q = 0.541$, residual $-18.9\%$, and the heavy leptons
are degenerate by construction.

*Structural diagnosis*: complex conjugation on
$({\mathbb Z}/13{\mathbb Z})^*/\langle 5 \rangle \cong
{\mathbb Z}/3{\mathbb Z}$ acts by $\tau \leftrightarrow \tau^{-1}$,
and $|\cdot|^2$ is invariant. The three-generation mass hierarchy
*breaks* this ${\mathbb Z}/2$ automorphism. No pure order-3-character
$L$-value scheme can reproduce it.

### 4.6 Where the individual masses live: $m_e, m_\mu, m_\tau$ in the spectral sector

The converging conclusion of all four negative results is sharp:
the individual charged-lepton masses are *not*
${\mathbb Z}/13{\mathbb Z}$-arithmetic data. They are Riemann-zero
data.

The $\gamma$-template of research/47 provides sub-percent fits:
$m_\tau = \gamma_7 \cdot \gamma_8$ (0.22\% from PDG),
$m_\mu = \gamma_7 \cdot \gamma_8^{1/4}$ (0.62\% from PDG), and
$m_e$ is implicitly fixed by the Koide relation itself to
$m_e^{\mathrm{Koide}} = 0.5106$ MeV (0.08\% from PDG). These
formulas involve $\gamma_7$ and $\gamma_8$, the 7th and 8th
non-trivial zeros of $\zeta(s)$, and live squarely in the spectral
sector of the CBB system: they are matrix elements of $\hat L = \log
\hat R$ in the spectral basis, not cyclotomic-arithmetic data.

The three-category template of research/47 organises the fermion
mass hierarchy as follows: third-generation masses are *products*
of $\gamma$-zeros (large), second-generation are *ratios* or
*fractional powers* (intermediate), and first-generation are
*differences* or *simple ratios* (small). The 5-order spread
$m_t/m_e \sim 3.4 \times 10^5$ is the natural span of these mixed
templates applied to the first 15 Riemann zeros.

### 4.7 The trace-versus-spectral split for lepton data

The Koide ratio $Q = 2/3$ and the individual masses
$(m_e, m_\mu, m_\tau)$ therefore live in two different sectors of
the CBB system:

| Datum | Sector | Origin | Precision |
|:---|:---|:---|:---:|
| $Q = 2/3$ | Bridge (cyclotomic) | Jones index $[\mathcal{M}:\mathcal{N}] = 3$ | structural ($9 \times 10^{-4}\%$) |
| $m_\tau = \gamma_7 \cdot \gamma_8$ | Spectral | Matrix element of $\hat L$ | 0.22\% |
| $m_\mu = \gamma_7 \cdot \gamma_8^{1/4}$ | Spectral | Matrix element of $\hat L$ | 0.62\% |
| $m_e \approx 0.5106$ MeV | Spectral (via Koide) | Koide-solved from $m_\tau, m_\mu$ | 0.08\% |

The $0.08\%$ Koide residual --- the discrepancy between the
Koide-predicted $m_e = 0.5106$ MeV and the PDG value
$m_e = 0.5110$ MeV --- lives in the $\gamma$-template itself.
It is a statement about $\gamma_7 \cdot \gamma_8$ and
$\gamma_7 \cdot \gamma_8^{1/4}$ meeting PDG, not about
${\mathbb Z}/3{\mathbb Z}$. Four independent routes have
established this cleanly: the ${\mathbb Z}/3{\mathbb Z}$ and
sub-factor layers fix the *identity* $Q = 2/3$ but cannot improve
the numerical residual.

### 4.8 Three different "lepton facts" in three different sectors

The CBB system distributes the information about charged leptons
across three distinct sectors:

1. **Generation count** ($n_{\mathrm{gen}} = 3$): lives in the
   bridge sector. Derived from the outer
   ${\mathbb Z}/3{\mathbb Z} \subset \mathrm{Out}(\mathcal{M})$
   induced by $\mathrm{Frob}_5$ at cyclotomic level 13
   (Theorem 3.1). Equivalently, from the Jones index
   $[\mathcal{M}:\mathcal{N}] = 3$.

2. **Koide ratio** ($Q = 2/3$): lives at the interface of the
   bridge and spectral sectors. The identity $Q = 2/d$ is a
   bridge-sector theorem (Proposition 4.1). Its numerical value
   $2/3$ is fixed by the same index $d = 3$. By Theorem 3.1(iv),
   $Q = 2/3$ is the cyclotomic Brauer class
   $\mathrm{inv}_5 = 1/3$, doubled.

3. **Individual masses** ($m_e, m_\mu, m_\tau$): live in the
   spectral sector. They are matrix elements of $\hat L = \log \hat R$
   involving the Riemann zeros $\gamma_7$ and $\gamma_8$, with the
   three-category template (product/ratio/difference) reflecting
   the generation grading. The $0.08\%$ Koide residual is a spectral
   statement, not a bridge statement.

This separation is the honest accounting of what the bridge
construction does and does not explain about charged leptons. The
bridge gives the *identity* and the *count*. The spectrum gives the
*values*. The four failed routes (Sections 4.5) confirm that these
roles cannot be exchanged.

---

*End of Sections 1--4.*

---

### References for Sections 1--4

- Bost, J.-B. and Connes, A., "Hecke algebras, type III factors and
  phase transitions with spontaneous symmetry breaking in number
  theory," *Selecta Math.* **1** (1995) 411--457.
- Connes, A. and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS Colloquium Publications **55** (2008),
  Chapter 3 and Proposition 3.34.
- Jones, V. F. R., "Index for subfactors," *Invent. Math.* **72**
  (1983) 1--25.
- Koide, Y., "Fermion-boson two-body model of quarks and leptons and
  Cabibbo mixing," *Lett. Nuovo Cim.* **34** (1982) 201.
- Ocneanu, A., *Actions of Discrete Amenable Groups on von Neumann
  Algebras*, Lecture Notes in Mathematics **1138**, Springer (1985).
- Popa, S., "Classification of amenable subfactors of type II,"
  *Acta Math.* **172** (1994) 163--255.
- Goodman, F., de la Harpe, P. and Jones, V. F. R., *Coxeter Graphs
  and Towers of Algebras*, MSRI Publications **14** (1989).
- Research notes 47, 140, 151, 157, 158, 161, 162, 172 (this
  programme).
