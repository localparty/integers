# 1. Mathematical Setup

## 1.1 The Lattice

Fix an integer $L \geq 2$ and define the periodic hypercubic lattice

$$\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^4.$$

Write $\Lambda_L^0$ for the set of sites, $\Lambda_L^1$ for the set of
oriented nearest-neighbor links (edges), and $\Lambda_L^2$ for the set of
elementary plaquettes.  Every oriented link $\ell = (x, \hat\mu)$ runs from
site $x$ to site $x + \hat\mu$, where $\hat\mu$ is a unit lattice vector,
$\mu = 1,\dots,4$.  The reversed link is $\bar\ell = (x + \hat\mu, -\hat\mu)$.


## 1.2 Dynamical Variables

The theory carries two sets of dynamical variables.

**4D link variables.**
To each oriented link $\ell \in \Lambda_L^1$ assign a group element
$U_\ell \in \mathrm{SU}(N)$, with $U_{\bar\ell} = U_\ell^{-1}$.
A configuration is a map $U : \Lambda_L^1 \to \mathrm{SU}(N)$.

**Internal connections.**
To each site $x \in \Lambda_L^0$ assign a connection
$A_x \in \mathcal{A}_0(\mathbb{CP}^{N-1})$, the space of smooth
$\mathrm{SU}(N)$-connections on the canonical line bundle over
$\mathbb{CP}^{N-1}$ with second Chern number $c_2 = 0$.  The restriction
to the topologically trivial sector $c_2 = 0$ is essential: it excludes
instantonic modes on the internal space and ensures a clean spectral gap
(Section 2).


## 1.3 The Action

The total Euclidean action decomposes as

$$S[U, A] \;=\; S_{\mathrm{4D}}[U] \;+\; S_{\mathrm{int}}[U, A].$$

**Wilson plaquette action.**
For each plaquette $P \in \Lambda_L^2$ with boundary links
$\ell_1, \ell_2, \ell_3, \ell_4$ (ordered), the holonomy is
$U_P = U_{\ell_1} U_{\ell_2} U_{\ell_3} U_{\ell_4}$.  The 4D action is

$$S_{\mathrm{4D}}[U] \;=\; \beta \sum_{P \in \Lambda_L^2}
  \left(1 - \frac{1}{N}\,\operatorname{Re}\operatorname{Tr} U_P\right),
  \qquad \beta = \frac{2N}{g^2}.$$

**Internal action.**
At each site $x$, the Yang-Mills action on $\mathbb{CP}^{N-1}$ is

$$S_{\mathrm{YM}}^{\mathrm{int}}(A_x) \;=\;
  \frac{1}{2\,g_{\mathrm{int}}^2} \int_{\mathbb{CP}^{N-1}}
  \operatorname{Tr}(F_{A_x} \wedge *\, F_{A_x}),$$

where $g_{\mathrm{int}}^2 = g^2 / \operatorname{Vol}(\mathbb{CP}^{N-1})$
and $*$ is the Hodge star of the Fubini-Study metric with radius $r_3$.

**Coupling between sites.**
For each link $\ell = (x, \hat\mu)$, the coupling between the internal
connections at $x$ and $x + \hat\mu$ is

$$V_\ell(U_\ell, A_x, A_{x+\hat\mu}) \;=\;
  \frac{1}{a^2} \int_{\mathbb{CP}^{N-1}}
  \bigl\| A_{x+\hat\mu} - U_\ell^{-1} A_x\, U_\ell \bigr\|^2
  \,\mathrm{dvol},$$

where $a$ is the lattice spacing and $U_\ell$ acts on $A_x$ via the
adjoint representation.  The full interaction action is

$$S_{\mathrm{int}}[U, A] \;=\;
  \sum_{x \in \Lambda_L^0} S_{\mathrm{YM}}^{\mathrm{int}}(A_x)
  \;+\; \sum_{\ell \in \Lambda_L^1} V_\ell(U_\ell, A_x, A_{x+\hat\mu}).$$


## 1.4 Kaluza-Klein Reduction

Let $\Delta_1^{\mathrm{H}}$ denote the Hodge Laplacian on 1-forms on
$(\mathbb{CP}^{N-1}, g_{\mathrm{FS}})$ with the Fubini-Study metric of
radius $r_3$.  Its spectrum is discrete:

$$0 \;<\; \lambda_1^{(1)} \;\leq\; \lambda_2^{(1)} \;\leq\; \cdots$$

The inequality $\lambda_1^{(1)} > 0$ holds because $\mathbb{CP}^{N-1}$ has
no harmonic 1-forms ($b_1 = 0$ for $N \geq 2$).  The precise lower bound
is established in Section 2.

Expand the internal connection in eigenmodes $\{\omega_n\}$ of
$\Delta_1^{\mathrm{H}}$:

$$A_x \;=\; \sum_{n=1}^{\infty} \phi_n(x)\,\omega_n.$$

The mode $\phi_n : \Lambda_L^0 \to \mathfrak{su}(N)$ is a scalar lattice
field with Kaluza-Klein mass

$$m_n \;=\; \frac{\sqrt{\lambda_n^{(1)}}}{r_3}.$$

The lightest KK mass $m_1 = \sqrt{\lambda_1^{(1)}}\,/\,r_3$ sets the scale
that controls all cluster expansion bounds.  In particular, the key
dimensionless ratio is $m_1 a$: when $m_1 a \gg 1$, the KK modes are heavy
relative to the lattice cutoff and their effects are exponentially
suppressed.


## 1.5 Parameters and Scales

The model depends on five parameters:

| Symbol | Meaning |
|:-------|:--------|
| $N$ | rank of the gauge group $\mathrm{SU}(N)$ |
| $L$ | lattice period (number of sites per direction) |
| $a$ | lattice spacing (meters) |
| $r_3$ | radius of $\mathbb{CP}^{N-1}$ (meters) |
| $\beta = 2N/g^2$ | inverse bare coupling |

The physical regime of interest is

$$r_3 \;\sim\; 10^{-31}\;\mathrm{m}, \qquad
  a \;\sim\; 10^{-16}\;\mathrm{m}, \qquad
  \frac{r_3}{a} \;\sim\; 10^{-15}.$$

The internal space is fifteen orders of magnitude smaller than the lattice
spacing.  This extreme hierarchy ensures:

1. **KK masses are enormous:** $m_1 a \sim a/r_3 \sim 10^{15}$, so
   KK modes decouple exponentially from the 4D physics.
2. **The internal space is invisible at lattice resolution:** no lattice
   observable can probe distances of order $r_3$.
3. **The 4D continuum limit is independent of the internal geometry:**
   the limit $a \to 0$ is taken with $r_3$ fixed, and all internal
   corrections vanish faster than any power of $a$.


## 1.6 Measure and Partition Function

The partition function is

$$Z \;=\; \int \prod_{\ell \in \Lambda_L^1} dU_\ell
  \prod_{x \in \Lambda_L^0} \mathcal{D}A_x \;
  e^{-S[U,A]},$$

where $dU_\ell$ is the normalized Haar measure on $\mathrm{SU}(N)$ and
$\mathcal{D}A_x$ is the gauge-fixed functional measure on
$\mathcal{A}_0(\mathbb{CP}^{N-1})$, restricted to the $c_2 = 0$ sector
and divided by the volume of the residual gauge group.

The transfer matrix $\hat{T}$ acts on $L^2$ of a single time-slice
configuration.  The mass gap of the lattice theory is

$$\Delta_0 \;=\; -\frac{1}{a}\,\log\frac{\lambda_1(\hat{T})}
  {\lambda_0(\hat{T})},$$

where $\lambda_0(\hat{T}) > \lambda_1(\hat{T}) \geq 0$ are the two
largest eigenvalues of $\hat{T}$.  The goal of Sections 2-4 is to prove
$\Delta_0 > 0$.
