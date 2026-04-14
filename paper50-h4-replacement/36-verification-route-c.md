## §36 — Verification of Route C

*N=4 SYM twist computation + geometric Langlands check. Wilson-loop evaluation. Scale-bridge rigidity verification. The verification programme for Route C's geometric-Langlands closure of H4.*

---

## 36.1. The verification target

Route C's analytic construction identifies pure Yang-Mills as a decoupling limit of Kapustin-Witten-twisted N=4 super Yang-Mills, applies Gaitsgory-Raskin's 2024 proof of geometric Langlands to the twisted theory to extract Wilson-loop spectral data at short distances, and verifies that this data matches the perturbative expansion.

Verification has four components:

**V-C1 (N=4 twist computation).** Compute the Kapustin-Witten twist of N=4 SYM at a specific parameter $\Psi \in \mathbb{CP}^1$. Identify the resulting topological quantum field theory and its Wilson-loop observables.

**V-C2 (Geometric-Langlands check).** Apply Gaitsgory-Raskin's equivalence to the twisted theory. Verify that the Wilson-loop observables correspond to Hecke eigensheaves with specific spectral data.

**V-C3 (Scale-bridge rigidity).** Verify that the decoupling limit from N=4 SYM to pure YM is rigorously controlled. The limit must preserve Wilson-loop correlators at short distances while decoupling the scalar and fermion degrees of freedom of N=4 SYM.

**V-C4 (Wilson-loop evaluation).** Evaluate the short-distance behavior of Wilson-loop correlators in pure YM using the spectral data transferred from the twisted N=4 theory via V-C3. Verify the match with the perturbative expansion.

All four components together verify Route C's analytic claim.

---

## 36.2. N=4 twist computation (V-C1)

The Kapustin-Witten twist of N=4 SYM is parameterized by a point $\Psi \in \mathbb{CP}^1$. Three distinguished values are relevant:

- $\Psi = 0$: the A-twist (symplectic). Produces geometric-Langlands-style physics on the automorphic side.
- $\Psi = \infty$: the B-twist (holomorphic). Produces the Galois side.
- $\Psi = 1$: the half-twist. Produces a mixed theory.

For Route C, the primary twist is $\Psi = 0$ (A-twist), because it corresponds most directly to the automorphic side of geometric Langlands, where Hecke eigensheaves live.

**Verification check.** Compute the A-twist of N=4 SYM explicitly. The theory reduces to a 2D sigma model on the Hitchin moduli space $\mathcal{M}_H(G, \Sigma)$ for a Riemann surface $\Sigma$ (Kapustin-Witten 2007). Verify that this sigma model has the correct symmetries, Wilson-loop observables, and topological invariants.

**Wilson-loop observables.** The 4D Wilson loop $W_R(C)$ colored by representation $R$ of $G$, wrapping a closed loop $C$, descends to an observable in the 2D sigma model. Specifically, it becomes a "branes intersection number" on $\mathcal{M}_H(G, \Sigma)$, where the branes are specific submanifolds representing the 2D reduction of the Wilson loop.

**Computability check.** For simple cases ($G = \mathrm{SU}(2)$ or $\mathrm{SU}(3)$, $\Sigma$ a Riemann surface of low genus), the sigma-model observables are computable explicitly. The twist computation should reproduce known results (e.g., Witten's TQFT computations from the 1990s) before extending to the general case.

---

## 36.3. Geometric-Langlands check (V-C2)

Gaitsgory-Raskin 2024 proved the geometric Langlands conjecture in the de Rham setting: there is an equivalence of categories

$$D(\mathrm{Bun}_G) \simeq \mathrm{QCoh}(\mathrm{LocSys}_{G^\vee})$$

(up to technicalities). The left side houses Hecke eigensheaves on the moduli stack of $G$-bundles; the right side houses quasi-coherent sheaves on the moduli stack of $G^\vee$-local systems.

For Route C, the verification check is: Wilson-loop observables in the twisted N=4 theory correspond under the Gaitsgory-Raskin equivalence to specific objects on the Galois side. Specifically, a Wilson loop colored by representation $R$ of $G$ corresponds to a tensor-operation on $\mathrm{LocSys}_{G^\vee}$ indexed by the dual representation $R^\vee$ of $G^\vee$.

**Verification protocol.**

1. **Identify the Wilson-loop brane** in the sigma model on $\mathcal{M}_H(G, \Sigma)$.
2. **Apply the Gaitsgory-Raskin equivalence** (or its extension to the $\mathcal{M}_H$ case; see Ben-Zvi-Nadler 2018 for the geometric dictionary).
3. **Identify the corresponding Galois object** — a specific local system on $\Sigma$ with structure group $G^\vee$.
4. **Extract spectral data** of this local system — eigenvalues of the holonomies, which correspond to Wilson-loop expectation values at short distances.

**Computability check.** The geometric-Langlands equivalence is a *categorical* statement; explicit computation of the equivalence for specific objects is delicate. Gaitsgory-Raskin's proof provides the existence of the equivalence; extracting specific spectral data requires additional work, possibly via the related work of Beilinson-Drinfeld, Frenkel-Gaitsgory, Yun.

---

## 36.4. Scale-bridge rigidity (V-C3)

The decoupling limit from N=4 SYM to pure YM is the single hardest step in Route C. The N=4 theory has:

- One gauge field (same as pure YM).
- Six real scalars in the adjoint representation.
- Four Weyl fermions in the adjoint representation.

The pure YM theory has only the gauge field. The decoupling limit is:

$$\text{N=4 SYM at coupling } g_{\mathrm{N=4}} \xrightarrow{\text{scalar/fermion masses} \to \infty} \text{pure YM at coupling } g_{\mathrm{YM}}$$

where the running coupling $g_{\mathrm{YM}}$ is related to $g_{\mathrm{N=4}}$ via the matching conditions at the decoupling scale.

**Verification checks.**

1. **Scale-bridge existence.** Show that a finite decoupling limit exists — that giving infinite masses to the scalars and fermions produces a finite 4D QFT that is pure YM.

2. **Wilson-loop preservation.** Show that the Wilson-loop correlators of the N=4 theory, evaluated at scales above the decoupling, continue smoothly to the Wilson-loop correlators of pure YM below the decoupling.

3. **Spectral-data transfer.** Show that the spectral data extracted from the twisted N=4 theory via geometric Langlands (V-C2) transfers to spectral data for pure YM Wilson loops at short distances.

4. **Paper 10 + 11 compatibility.** The decoupling limit must be scheme-independent (Paper 10) and respect the all-orders perturbative structure (Paper 11 K.4).

**External support.** Elliott-Gwilliam-Williams 2024 provides the BV-quantization framework that makes the decoupling limit rigorous at the level of factorization algebras. The framework is general but has not been applied to the N=4-to-pure-YM specific case.

**Verification cost.** V-C3 is the most expensive verification step in Route C, estimated at ~500-1000 author-hours. This is because the decoupling limit has no prior rigorous treatment in the literature; Route C's closure requires a substantial original contribution here.

---

## 36.5. Wilson-loop evaluation (V-C4)

With the spectral data transferred via V-C3, evaluate Wilson-loop correlators in pure YM at short distances and verify the match with perturbation theory.

**Method.** The spectral data (eigenvalues of Galois-side local systems) provides a set of numerical inputs to a closed-form expression for the short-distance expansion of Wilson-loop correlators. Compute this expression and compare to the perturbative series.

**Expected output.** A table of Wilson-loop correlators at short distances $|C| \leq 0.05$ fm, with numerical values derived from the geometric-Langlands spectral data.

**Comparison.** Match against:

- The perturbative expansion at 4 loops (same as Route A's V-A1).
- The lattice-QCD values (same as V-A3).
- Route A's Borel-sum estimates (cross-check).
- Route B's L-function values (cross-check).

A successful V-C4 confirms that all three routes produce consistent Wilson-loop data at short distances — the cross-route consistency condition (§37).

---

## 36.6. Scale-bridge rigidity verification: the hardest piece

V-C3 deserves additional attention because it is Route C's main technical challenge.

**Why hard.** The decoupling limit of N=4 SYM to pure YM is well-understood physically but not rigorously. Standard arguments (giving infinite masses to scalars and fermions, performing the path integral over the massive modes) produce the pure YM action up to UV-sensitive corrections. Making this rigorous requires controlling the UV behavior of the decoupled theory.

**Elliott-Gwilliam-Williams framework.** Their 2024 BV-quantization framework gives factorization algebras of observables for Kapustin-Witten twisted theories. The decoupling limit becomes a limit of factorization algebras — a concept that makes sense in the BV framework but requires verification that the limit is well-defined.

**Programme-internal support.** Paper 10's scheme independence and Paper 11's K.4 all-orders result provide the perturbative control that any rigorous decoupling limit must respect. Paper 8 Links 2-5's Balaban polymer expansion provides UV stability independently of the decoupling route.

**Status.** V-C3 is currently at the *target* stage: the programme has identified what needs to be done but has not yet done it. The three-route strategy's robustness (§24) means Route C can proceed in parallel with Routes A and B even while V-C3 is incomplete; if Routes A or B close first, V-C3 becomes a post-facto verification of Route C rather than a prerequisite for Paper 50's publication.

---

## 36.7. Verification infrastructure and cost

Route C's verification is the most expensive of the three routes.

- **N=4 twist computation (V-C1):** ~200 author-days, symbolic + analytic.
- **Geometric-Langlands check (V-C2):** ~300 author-days (requires specialists in Gaitsgory-Raskin machinery).
- **Scale-bridge rigidity (V-C3):** ~500-1000 author-days (the bottleneck).
- **Wilson-loop evaluation (V-C4):** ~50 author-days, numerical.

Total: ~1050-1550 author-days plus modest compute.

Route C's verification is more author-hour-intensive than Routes A or B, concentrated in V-C3. This is why Route C has the lowest a priori confidence (3/10 per the PROOF-CHAIN.md) — the verification's bottleneck step has no prior rigorous treatment.

---

## 36.8. Failure modes and repair

**Failure mode C1: Twist computation inconsistency.** V-C1 fails (the Kapustin-Witten twist produces a theory that does not match Paper 50's target). Repair: use a different twist parameter $\Psi$. Possible but may change Route C's closure argument.

**Failure mode C2: Gaitsgory-Raskin equivalence does not apply.** V-C2 fails (the equivalence, as proved, does not cover the N=4 twist case directly). Repair: extend the equivalence, or use a related result (quantum geometric Langlands, Teschner 2014).

**Failure mode C3: Scale bridge breaks.** V-C3 fails (the decoupling limit produces UV-divergent artifacts or violates scheme independence). Repair: use the Elliott-Gwilliam-Williams framework's regulator structure to isolate and absorb the artifacts. If irreparable, Route C is not closable as formulated.

**Failure mode C4: Wilson-loop evaluation disagrees with perturbation.** V-C4 fails. Repair: identify the discrepancy's source — either V-C3's scale-bridge transferred incorrect data, or V-C2's geometric-Langlands extraction was wrong, or the perturbative comparison was incorrect. Retrace the chain from V-C4 back to the source.

The failure mode with the highest a priori probability is C3. The programme's partnership strategy (collaboration with Elliott, Gwilliam, Williams, or other BV-quantization specialists) is the main mitigation.

---

## 36.9. Summary

Route C's verification has four components: N=4 twist computation (V-C1), geometric-Langlands check via Gaitsgory-Raskin (V-C2), scale-bridge rigidity from N=4 SYM to pure YM (V-C3), and Wilson-loop evaluation at short distances (V-C4). The verification cost is ~1050-1550 author-days, concentrated in V-C3 (the decoupling limit's rigorization). V-C3 is the bottleneck and the primary source of Route C's low a priori confidence. Cross-checks against Routes A and B provide additional validation. Route C is verified when all four components close with adversarial threshold consistency.

---

*Paper 50 §36. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
