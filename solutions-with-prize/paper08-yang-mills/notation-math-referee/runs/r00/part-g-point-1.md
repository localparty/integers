## Part G, Point 1: Jaffe–Witten Requirements

**Weight:** HEAVY
**Verdict:** **GENUINE GAP** at the level of full Clay compliance — multiple required Jaffe–Witten ingredients are missing or only partially addressed (see C1–C11 checklist).

**Finding:**

(a) **The KK device.** The proof uses the KK-enhanced theory with $\mathbb{CP}^{N-1}$ internal connections as a *proof device*. Theorem 5 (Section 4.5) establishes that the standard SU(N) Wilson lattice gauge theory (without KK) inherits the same lattice mass gap, modulo $O(e^{-m_1 a/2})$ corrections. So the *lattice* mass gap of the standard theory is established at any $a \gg r_3$.

The continuum limit (Section 5) is then taken for *the standard theory*, using Balaban's RG. This is the right structure: the KK enhancement provides $\Delta_0 > 0$ at the lattice level, and Balaban's RG (modulo Point C1) propagates this to the continuum.

But there is a subtle slippage: Section 4 proves the lattice mass gap *in the cluster-expansion regime* $a \gg r_3$ (coarse lattices). Section 5 takes the continuum limit $a \to 0$. **These are conceptually opposite directions.** The cluster-expansion gives $\Delta_0$ at coarse $a$; the continuum limit needs $\Delta_\infty$ at fine $a$. The "bridge" is Balaban's RG, which (in Balaban's setting) goes from a fine bare $a$ to a coarse effective $a$ — i.e., the *opposite* direction from the cluster-expansion-to-continuum needed here.

This is the K-vs-k issue restated: the proof needs an OUTER refining sequence of bare lattices (with the cluster expansion controlling each one) and an INNER Balaban flow (which coarsens, not refines). The preprint conflates these.

(b) **The gauge group.** Jaffe–Witten requires the result for "any compact simple gauge group $G$." The body of the preprint (Sections 4, 5) treats SU(N), and Appendix I.4 + Appendix K extend the argument to other groups via universal properties of compact symmetric spaces.

Reading I.4 / K carefully:

> "For each group $G$ beyond $\mathrm{SU}(N)$, the following steps would be required:
> 1. Compute the Hodge Laplacian spectrum on $G/H$ for 1-forms...
> 2. Verify the cluster expansion convergence...
> 3. Verify the dimension-6 operator classification...
> 4. Verify or extend Balaban's construction to the gauge group $G$..."

The phrasing "would be required" rather than "is established" is telling. I.4 explicitly says these steps "are carried out in **Appendix K**", and K does indeed sketch each. But "sketch" is the right word: K identifies the relevant homogeneous spaces, gives standard formulas for the Ricci tensor and dual Coxeter number, and asserts that the SU(N) proof generalizes "with $G$-dependent constants." It does NOT execute the full proof for $G_2, F_4, E_6, E_7, E_8$.

The abstract claims:
> "We prove that for any compact simple gauge group $G$... The result covers all compact simple Lie groups."

This is overstated. What is *actually* established (modulo the K-vs-k issue) is the SU(N) case in detail, with sketches for other groups indicating the argument generalizes. For Clay, this is **insufficient** unless the exceptional groups are explicitly worked out — and they are not. **GENUINE GAP at the level of "any compact simple G."**

For SU(N) alone (which is the bulk of the proof), the structural claim is a CLOSABLE GAP modulo Point C1.

(c) **The lattice regulator.** The proof uses Wilson's lattice gauge theory as the regularization. Jaffe–Witten does not prescribe a regularization, so this is acceptable. The continuum limit is independent of lattice details modulo universality, which is *not* claimed (only existence of *some* subsequential limit with a mass gap; see Point F4).

(d) **The precise claim.** Reading the proof's structure:
> "For SU($N$) with $N \geq 2$, starting from Wilson's lattice gauge theory in the trivial $c_2 = 0$ topological sector with $\mathbb{CP}^{N-1}$ KK enhancement, there exists a subsequential continuum limit satisfying OS1–OS5 with mass gap $\Delta_\infty > 0$."

This is the *strongest claim* the proof actually establishes (modulo Point C1). It is *not* the same as the abstract's "any compact simple gauge group". For Clay, the gap between "SU(N) in $c_2 = 0$ with KK technique" and "any compact simple G with the full physical theory" is significant.

Items missing or partial:
- All compact simple G (only SU(N) is fully treated; others sketched).
- Local quantum field operators in the J–W sense (Wilson loop limits exist; correspondence with $\mathrm{Tr}\,F_{ij}F_{kl}$ is loose; see G4).
- Stress tensor (not constructed; G4).
- OPE with prescribed AF singularities (not constructed; G4).
- Short-distance match to perturbative AF (asserted, not derived; G4).

(e) **Quantitative predictions.** §3 of the preprint gives "$\sqrt\sigma = 437$ MeV", "glueball $\sim 1.5$ GeV", "Lüscher coefficient $\pi/6$" etc. These are *not* part of the proof; they are physics consistency checks. The proof's correctness should not be evaluated on numerical agreement with experiment — and it is not, in the formal proof chain. Sound at the level of "the proof does not rely on numerics."

**Impact on the claimed result:** The proof establishes a *partial* result for the Clay problem — specifically, a continuum limit with a mass gap for SU(N) lattice gauge theory under specific conditions, conditional on Point C1. This is a substantive contribution but does NOT meet the full Clay requirement, which mandates:
- All compact simple gauge groups (only SU(N) treated).
- Local field operators with prescribed AF singularities (only Wilson loops + plaquette traces, no operator construction).
- Stress tensor (absent).
- OPE (absent).

A Clay submission as currently written would be returned for major revisions on these grounds.
