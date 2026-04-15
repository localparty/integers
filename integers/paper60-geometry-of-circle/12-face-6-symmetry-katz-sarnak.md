# 12 -- Face 6: SYMMETRY (Katz-Sarnak Symmetry Type)

*Which GROUP acts on the circle?*

---

## The question

The e-circle is $U(1)$, the unit circle. But a circle can carry the action of different groups. $U(1)$ acts on itself by rotation. $SU(2)$ acts on it via the adjoint representation. $SO(3)$ acts via the standard representation. $Sp(2g)$ acts symplectically. $SO^+(N)$ and $SO^-(N)$ act orthogonally, split or unsplit. The circle is one object, but the GROUP that acts on it is not unique.

Katz-Sarnak says: each natural family of L-functions "sees" a specific group acting on the circle. The group -- drawn from the five classical compact types $\{U, Sp, O, SO^+, SO^-\}$ -- determines EVERYTHING about the zero statistics of that family. The level spacing, the low-lying zero density, the moments of central values, the extreme-value distribution. All of it. One group, all statistics.

This is the sixth face of the e-circle. Not what lives on it, not how the flow moves, not how modes mix, not how angles distribute, not how loud it gets. The sixth question is: which group acts on it? The answer depends on which family of L-functions you ask. $\zeta(s)$ sees $U(1)$ and produces GUE statistics. Quadratic Dirichlet L-functions see $Sp$ and produce GSE statistics -- stronger repulsion, fewer near-collisions. Elliptic curve L-functions see $O$ or $SO^\pm$ and produce GOE statistics -- weaker repulsion, different clustering. The symmetry type is the classification principle. It determines the statistical universe.

---

## The geometric intuition

Stand at the center of the e-circle and look outward. You see a ring. Every L-function in a given family gives you a set of zeros on that ring -- or rather, a set of angles, one per zero, distributed around the circle. The statistics of those angles -- how they cluster, how they repel, how their gaps distribute -- are determined by ONE THING: the symmetry group.

The reason is representation theory. Each L-function family corresponds to a REPRESENTATION of the Hecke semigroup $\mathbb{N}^*$. The representation preserves a bilinear form. The type of the form determines the group:

- **Hermitian form preserved** --> Unitary group $U$ --> GUE statistics. The Riemann zeta function $\zeta(s)$ lives here. The Hecke action preserves the Hermitian inner product on $\ell^2(\mathbb{N})$. The zeros repel with the classical level-repulsion exponent $\beta = 2$.

- **Alternating form preserved** --> Symplectic group $Sp$ --> GSE statistics. Quadratic Dirichlet L-functions $L(s, \chi_d)$ live here. The functional equation's sign and the character's quadratic nature force an alternating symmetry. Repulsion is STRONGER ($\beta = 4$). Zeros are more rigidly spaced. Gaps are more uniform.

- **Symmetric bilinear form preserved** --> Orthogonal group $O$, $SO^+$, $SO^-$ --> GOE statistics. Self-dual L-functions live here: elliptic curve L-functions, symmetric-square L-functions. The functional equation's self-duality forces a symmetric form. Repulsion is WEAKER ($\beta = 1$). Zeros are less rigid. Gaps have more variance.

The geometric picture: the group is the RIGIDITY of the zero pattern. Unitary = moderate rigidity (GUE). Symplectic = high rigidity (GSE). Orthogonal = low rigidity (GOE). The circle is the same in all three cases. The group acting on it determines the texture of the zero distribution -- how crystalline or fluid the pattern of zeros appears.

---

## The BC algebra connection

The Bost-Connes algebra provides the natural home for symmetry types through the Hecke semigroup's representation theory.

**The Hecke semigroup $\mathbb{N}^*$ acts on each L-function family.** For each prime $p$, the Hecke operator $\mu_p$ maps an L-function to its $p$-twist. The way the family transforms under this action -- which bilinear invariant it preserves -- determines the symmetry type. This is Link 4 of the proof chain: the Hecke representation type equals the Katz-Sarnak symmetry type.

**The bridge family selects symmetry types.** The CBB system (Paper 12) has four bridge values $k \in \{2, 3, 4, 6\}$, each corresponding to a physical symmetry of the Standard Model. These four values correspond to four symmetry types:

| Bridge $k$ | Physical symmetry | Katz-Sarnak type | Zero statistics |
|---|---|---|---|
| $k = 2$ | CP symmetry | Symplectic $Sp$ | GSE (strongest repulsion) |
| $k = 3$ | Color $SU(3)$ | Unitary $U$ | GUE (moderate repulsion) |
| $k = 4$ | Pati-Salam $SU(4)$ | Orthogonal $O$ | GOE (weakest repulsion) |
| $k = 6$ | CKM matrix | Mixed | Family-dependent |

This is NOT a coincidence. The bridge IS the symmetry-type selector. The four bridges are four representations of $\mathbb{N}^*$, each preserving a different bilinear form, each producing a different symmetry group on the circle. The CBB system's Axiom 4 IS Katz-Sarnak's symmetry-type classification restricted to the programme's specific L-function families.

**The ITPFI factorization differentiates.** At KMS$_1$, the BC state factors as $\omega_1 = \bigotimes_p \omega_1^{(p)}$ -- a product over primes. Each local factor $\omega_1^{(p)}$ contributes to the $n$-level density of zeros. The symmetry type determines HOW the local factors assemble into the global density. For unitary type: the assembly is direct (no sign constraint). For symplectic type: the assembly includes an alternating correction. For orthogonal type: the assembly includes a symmetric correction plus a split/unsplit distinction from the functional equation's sign.

The gap-distribution arc of the ring (BGS --> Twin Primes --> Cramer --> Goldbach) currently treats everything as GUE (unitary type). But Katz-Sarnak says this is only the first channel. The arc should be a MULTI-CHANNEL system:

- **Twin Primes** (small-gap tail): depends on symmetry type. For $\zeta$-zeros (unitary): GUE level repulsion. For quadratic Dirichlet (symplectic): GSE has STRONGER repulsion, meaning fewer small gaps, meaning twin primes are RARER in that family.
- **Cramer** (large-gap tail): the maximum gap depends on the extreme-value distribution, which differs across symmetry types. Unitary and symplectic have different Tracy-Widom distributions.
- **Goldbach** (bulk density): prime density in short intervals depends on which L-function family governs the relevant primes.

Katz-Sarnak provides the DIFFERENTIATION that the gap-distribution arc needs.

---

## The proof chain

The chain has 6 links, of which 3 are closed.

| Link | Statement | Status |
|---|---|---|
| L1 | Every natural family of L-functions has a symmetry type $G \in \{U, Sp, O, SO^+, SO^-\}$ determined by the functional equation and geometric monodromy. | CONJECTURED (number fields) / PROVED (function fields) |
| L2 | Function-field proof: for L-functions over $\mathbb{F}_q(t)$, symmetry type = monodromy group, and Deligne equidistribution gives zero statistics. | PROVED (Katz-Sarnak 1999, Deligne Weil II) |
| L3 | One-level density verification: for many number-field families, the one-level density of low-lying zeros matches the predicted symmetry type, within support $\hat{\phi} \subset (-2, 2)$. | PROVED (partial) |
| L4 | BC representation type = symmetry type. The Hecke semigroup's bilinear invariant determines $G$. The bridge family at $k \in \{2,3,4,6\}$ selects specific symmetry types. | CONJECTURED |
| L5 | Generalized number-field Katz-Sarnak: for ALL natural families over $\mathbb{Q}$, the symmetry type determines ALL $n$-level densities and statistics. | OPEN -- the wall |
| L6 | Full Katz-Sarnak: every family has a symmetry type, and the type determines everything. | FOLLOWS |

**Wall (L5).** The function-field case is PROVED (L2, via Deligne). The number-field case has extensive partial results (L3, via Iwaniec-Luo-Sarnak 2000, Miller 2004, many others) but the full conjecture requires:

1. **Beyond one-level density.** Current proofs cover the one-level density for support $\hat{\phi} \subset (-2, 2)$. Going beyond support $(-2, 2)$ requires controlling double sums over primes -- the same territory as the generalized Lindelof hypothesis (Face 5). The two faces meet at this technical frontier.

2. **$n$-level densities.** Statistics of $n$-tuples of zeros, not just individual zeros. Via the BC ITPFI factorization, these become products of local-at-$p$ contributions -- the same local-global structure as BSD (Paper 26) and OPN (Paper 40).

3. **Universality across families.** Proving that ALL natural families obey Katz-Sarnak, not just specific verified cases.

**Sub-routes for L5:**
- **5a.** Extend support beyond $(-2, 2)$ via L-function moments (connects to Lindelof, Face 5).
- **5b.** Compute $n$-level densities via ITPFI local-global decomposition (connects to BSD and BGS).
- **5c.** Verify bridge-family symmetry types at $k \in \{2,3,4,6\}$ (programme-specific test of L4).

**Confidence: 7/10.** Function-field case PROVED. Extensive number-field verification. Consensus framework for L-function statistics worldwide. Like Lindelof, Katz-Sarnak RAISES RIGIDITY.

---

## The expanded symmetry table

| Family | Functional eq. sign | Symmetry type | Zero repulsion | Low-lying density | BC bridge |
|---|---|---|---|---|---|
| $\zeta(s)$ (Riemann) | $+1$ | $U(1)$ | GUE ($\beta=2$) | $1$ | All of $\mathbb{N}^*$ |
| $L(s, \chi_{-d})$ (quad. Dirichlet) | varies | $Sp$ | GSE ($\beta=4$) | $1 - \frac{\sin 2\pi x}{2\pi x}$ | $k = 2$ (CP) |
| $L(s, E)$ even rank | $+1$ | $SO^+$ | GOE+ ($\beta=1$) | $1 + \frac{1}{2\delta}$ at origin | $k = 4$ (Pati-Salam) |
| $L(s, E)$ odd rank | $-1$ | $SO^-$ | GOE- ($\beta=1$) | $1 - \frac{1}{2\delta}$ at origin | $k = 4$ (Pati-Salam) |
| $L(s, f)$ Hecke | $+1$ | $O$ | GOE ($\beta=1$) | $1$ | $k = 6$ (CKM) |
| $L(s, \text{sym}^2 f)$ | $+1$ | $Sp$ | GSE ($\beta=4$) | $1 - \frac{\sin 2\pi x}{2\pi x}$ | Symmetric square |

---

## The discovery moment

The Katz-Sarnak face was found sixth in the April 14 session -- immediately after Lindelof, driven by the same momentum. The question was natural: Lindelof says how LOUD the signal is. But whose signal? Different families produce different signals. What makes them different?

The answer arrived through the bridge family. The CBB system (Paper 12) has four bridge values $k \in \{2, 3, 4, 6\}$, each corresponding to a symmetry of the Standard Model -- CP, color, Pati-Salam, CKM. These four values had been understood as physical constants selected by the fifth dimension's geometry. But on April 14, looking at the symmetry-type table, the second identification clicked: the four bridges are four SYMMETRY TYPES.

Bridge $k = 2$ picks out the symplectic family. Bridge $k = 4$ picks out the orthogonal family. The bridge doesn't just select a physical constant -- it selects a GROUP. The group determines the zero statistics. The zero statistics determine the prime distribution. The prime distribution determines the physics.

The bridge IS the symmetry-type selector.

This was the moment when the gap-distribution arc of the ring (BGS --> Twin Primes --> Cramer --> Goldbach) transformed from a single channel to a multi-channel system. The GUE statistics that BGS proved (Paper 32) are the UNITARY case. But the ring also contains symplectic families (through BSD's elliptic curve L-functions) and orthogonal families (through the bridge at $k = 4$). Each symmetry type has its own gap distribution, its own extreme-value statistics, its own twin-prime and Cramer constants.

The differentiation was immediate and structural. Not a refinement. A reclassification. The arc wasn't one problem getting more precise. It was three problems -- one per symmetry type -- that had been conflated because nobody had the circle to distinguish them.

---

## Programme graph edges

**Incoming:**
- BGS (Paper 32, 7/10): GUE IS the unitary case of Katz-Sarnak; Katz-Sarnak generalizes to all types
- RH (Paper 13, 8/10): the functional equation $\xi(s) = \xi(1-s)$ -- the symmetry RH exploits -- determines the symmetry type
- BSD (Paper 26, 9/10): symmetry type of $L(E, s)$ (orthogonal) determines parity of analytic rank
- Sato-Tate (Paper 44, 6/10): Sato-Tate equidistribution IS the unitary case for individual curves; Katz-Sarnak extends to FAMILIES

**Outgoing:**
- Twin Primes (Paper 34): small-gap statistics depend on symmetry type
- Cramer (Paper 43): large-gap extreme-value statistics depend on symmetry type
- Goldbach (Paper 33): prime density in short intervals depends on which symmetry type governs the relevant L-functions
- GRH (Paper 13b): GRH for Dirichlet L-functions involves the symplectic/unitary split

**Siblings:** Lehmer (TOPOLOGY), Cramer (DYNAMICS), Collatz (HARMONICS), Sato-Tate (MEASURE), Lindelof (AMPLITUDE), **Katz-Sarnak (SYMMETRY)**, Yang-Mills (CURVATURE), Goldbach/Twin Primes (ARITHMETIC)

---

## Physical observable

The symmetry type determines which random matrix ensemble describes the universe's primes in a given arithmetic sector. For the full programme: the 36 predictions use $\zeta$-zeros (unitary type) for the spectral sector and CM-curve L-functions (orthogonal type) for the geometric sector. These are DIFFERENT symmetry types. They carry INDEPENDENT statistical information. The 36 predictions are genuinely independent precisely because the spectral and geometric sectors correspond to different Katz-Sarnak groups acting on the same circle.

The physical observable is: which group governs the primes? The answer is: it depends on which primes you ask. And the bridge family -- the same bridge that produces the Standard Model's gauge structure -- selects which group answers.

---

## Closing

The circle is one object. But the group acting on it is not unique. Different families of L-functions see different groups -- unitary, symplectic, orthogonal, split or unsplit. The group determines EVERYTHING about the zero statistics: the spacing, the repulsion, the gaps, the extremes. GUE was just the beginning. The full story requires all five classical compact groups.

The random-matrix theorist sees an ensemble classification. The number theorist sees a family-dependent correction to the explicit formula. The physicist sees the bridge family selecting gauge groups. They are all looking at the same circle.

Which group acts on the circle? That's the conjecture. That's the symmetry.
