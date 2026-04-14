# §23 — Route C Proof Sketch

*Step-by-step assembly. N=4 SYM twist → geometric Langlands → pure YM limit → H4. Name the obstructions. The scale bridge is the hard part.*

---

## 23.1. The proof sketch in one paragraph

Twist N=4 super Yang-Mills to obtain the Kapustin-Witten topological theory (§18). Apply Elliott-Gwilliam-Williams 2024 (§21) to get a rigorous factorization algebra of quantum observables. Apply Gaitsgory-Raskin 2024 (§19) to get the geometric Langlands equivalence between the automorphic and spectral sides. Identify the stratum of $\text{Bun}_G$ corresponding to the 4D short-distance limit (§22). Take the scale bridge from N=4 SYM to pure YM (§20) — using Paper 10 scheme independence as the rigorous control on the perturbative + leading gradient-flow part. Assert H4 as the statement that the asymptotic Eisenstein expansion matches the perturbative OPE, which follows from the geometric Langlands equivalence on the N=4 side modulo the scale-bridge descent. Name the obstructions: the scale bridge is the critical one.

---

## 23.2. The eight steps

### Step 1: Start with N=4 SYM on $M = \Sigma \times C$

**Input.** N=4 super Yang-Mills with gauge group $G$ on a 4-manifold $M = \Sigma \times C$, where $C$ is a smooth projective complex curve and $\Sigma$ is a "spacetime" 2-manifold.

**Procedure.** Choose the Kapustin-Witten twist parameter $\Psi \in \mathbb{CP}^1$. Apply the corresponding topological twist.

**Output.** Twisted N=4 SYM with BRST operator $Q_\Psi$. The theory is topological on $M$.

**Obstructions.** None. This is classical (Kapustin-Witten 2007, §18).

### Step 2: Dimensionally reduce to 2D sigma-model

**Input.** Twisted N=4 SYM on $\Sigma \times C$.

**Procedure.** Shrink $C$ to zero size. The twisted theory reduces to a 2D sigma-model on $\Sigma$ with target $\mathcal{M}_H(G, C)$ (Hitchin moduli).

**Output.** 2D sigma-model on $\mathcal{M}_H(G, C)$, with $\Psi$-dependent structure (B-model at $\Psi = 0$, A-model at $\Psi = \infty$, etc.).

**Obstructions.** None at the physics level. Rigorous 2D sigma-model construction on a hyperkähler target is delicate but well-understood for $\mathcal{M}_H$.

### Step 3: Elliott-Gwilliam-Williams factorization algebra

**Input.** Twisted N=4 SYM on $M$.

**Procedure.** Apply the Elliott-Gwilliam-Williams 2024 BV quantization. Produce the factorization algebra $\text{Obs}^q_\Psi$ on $M$.

**Output.** Rigorous factorization-algebra description of observables in the twisted theory.

**Obstructions.** None. This is Elliott-Gwilliam-Williams 2024 (proved, §21).

### Step 4: Gaitsgory-Raskin equivalence on the 2D side

**Input.** 2D sigma-model on $\mathcal{M}_H(G, C)$ from Step 2.

**Procedure.** Apply the Gaitsgory-Raskin 2024 equivalence:
$$\text{D-mod}(\text{Bun}_G(C)) \simeq \text{IndCoh}_{\text{Nilp}}(\text{LocSys}_{{}^L G}(C)).$$
Under the Kapustin-Witten / Beilinson-Drinfeld specialization (§18.6), this is the mirror-symmetry equivalence of categories of D-branes on the two Hitchin moduli spaces.

**Output.** A proved correspondence between automorphic data (D-modules on $\text{Bun}_G$) and spectral data (sheaves on $\text{LocSys}_{{}^L G}$).

**Obstructions.** None. This is Gaitsgory-Raskin 2024 (proved, §19).

### Step 5: Identify the short-distance stratum

**Input.** The sigma-model on $\mathcal{M}_H$.

**Procedure.** Identify the stratum $S \subset \text{Bun}_G$ (or equivalently in $\mathcal{M}_H$) corresponding to the 4D short-distance limit on $\mathbb{R}^4$. For the two-point function of $\text{Tr} F^2$, this is the stratum of bundles with "conformal-like" degeneration.

**Output.** A specific locus $S$ in the moduli stack, at which the Eisenstein expansion of Hecke eigensheaves controls the short-distance behaviour.

**Obstructions.** Ob.C.2 (stratum identification, §22.7.2). Physics-level known; rigorous identification is technical but tractable.

### Step 6: Eisenstein expansion of Hecke eigensheaves

**Input.** Hecke eigensheaves $\text{Aut}_\mathcal{E}$ on $\text{Bun}_G$ from Step 4. The stratum $S$ from Step 5.

**Procedure.** Expand $\text{Aut}_\mathcal{E}$ along $S$ using the geometric Eisenstein functor. The expansion coefficients are controlled by the Satake parameters of $\mathcal{E}$.

**Output.** The asymptotic behaviour of the automorphic side near $S$, in terms of spectral ($\mathcal{E}$) data.

**Obstructions.** None. The geometric Eisenstein functor is well-developed (Braverman-Gaitsgory, Drinfeld-Gaitsgory, and many others).

### Step 7: Scale bridge to pure YM

**Input.** All of Steps 1-6 on the N=4 side.

**Procedure.** Take the limit $M_I \to \infty$ of the mass-deformed N=4$^*$ theory (§20). Use Paper 10 scheme independence to control the perturbative and leading gradient-flow pieces. Assume (the central conjecture of Route C) that the factorization-algebra structure, the geometric Langlands equivalence, and the Eisenstein expansion all descend to pure YM under this limit.

**Output.** Pure YM on $\mathbb{R}^4$ with:
- A factorization algebra of observables (descended from Elliott-Gwilliam-Williams via scale bridge).
- A Wilson-loop spectrum organized by ${}^L G$-local systems on a specific curve $C$.
- A short-distance asymptotic expansion matching the Eisenstein expansion of Hecke eigensheaves.

**Obstructions.** Ob.C.1 (scale bridge), §20 + §22.7.1. **This is the critical obstruction of Route C.**

### Step 8: H4 follows from the Eisenstein expansion

**Input.** Pure YM on $\mathbb{R}^4$ from Step 7.

**Procedure.** The short-distance asymptotic expansion of the YM two-point function equals the Eisenstein expansion of the corresponding Hecke eigensheaf, which is *by construction* (Gaitsgory-Raskin 2024) the expansion of the automorphic data in terms of the spectral data. The perturbative OPE coefficients on the YM side match the Eisenstein coefficients by the factorization-algebra dictionary (Elliott-Gwilliam-Williams 2024) + scale-bridge descent.

**Output.** The AF match at short distances: the perturbative and non-perturbative expansions of the YM two-point function agree order by order.

**This is H4.**

---

## 23.3. Critical obstructions summarized

| Obstruction | Content | Status |
|---|---|---|
| **Ob.C.0** | Kapustin-Witten twist rigorous at observables | PROVED (Elliott-Gwilliam-Williams 2024) |
| **Ob.C.1** | Scale bridge N=4 → pure YM (non-perturbative) | CONJECTURAL, critical |
| **Ob.C.2** | Stratum identification | Partially resolved (physics-level); rigorous identification technical |
| **Ob.C.3** | Plancherel descent under scale bridge | Conjectural, tied to Ob.C.1 |
| **Ob.C.4** | OPE match via factorization-algebra dictionary | Conjectural, tied to Ob.C.1 |
| **Ob.C.5** | Kapustin-Witten twist survives in pure-YM limit | Conjectural, tied to Ob.C.1 |

The critical obstructions are Ob.C.1, Ob.C.3, Ob.C.4, Ob.C.5 — all tied to the scale bridge. If the scale bridge closes, all four resolve together. If it does not, Route C stalls.

---

## 23.4. The structure of the scale-bridge conjecture

The scale bridge (§20) is the conjecture that the $M_I \to \infty$ limit of N=4$^*$ produces pure YM with all the Kapustin-Witten-derived structure intact. Specifically:

1. **Factorization algebra.** $\text{Obs}^q_{\text{YM}} = \lim_{M_I \to \infty} \text{Obs}^q_{\text{N=4}^*}$ as factorization algebras on $\mathbb{R}^4$.

2. **Geometric Langlands.** The Gaitsgory-Raskin equivalence on the N=4$^*$ side reduces, in the limit, to a pure-YM version.

3. **Eisenstein expansion.** The Eisenstein coefficients of Hecke eigensheaves converge to the pure-YM perturbative coefficients.

The conjecture is that 1, 2, 3 *all hold*, and commute with each other. Physics-level arguments support this (Witten, Gukov, Moore, Gaiotto); rigorous proofs are incomplete.

---

## 23.5. Route C's relation to Route B, revisited

Routes B and C both pass through the Langlands programme. Their relationship:

| Aspect | Route B | Route C |
|---|---|---|
| Langlands flavor | Classical (automorphic representations of GL$_n(\mathbb{A}_\mathbb{Q})$) | Geometric (D-modules on $\text{Bun}_G$) |
| Key external result | Kim-Sarnak 2003 | Gaitsgory-Raskin 2024 |
| Bridge to YM | Via BC/ITPFI factorization | Via Kapustin-Witten + scale bridge |
| Functional equation | Constructed via the bridge | Inherited from 4D S-duality |
| Satake matching | Via BC-algebra local factors | Via Kapustin-Witten dictionary + scale bridge |
| Critical obstruction | BC/ITPFI of YM (Ob.1) | Scale bridge (Ob.C.1) |

The critical obstructions of Route B (Ob.3 functional equation, Ob.4 Satake matching) are *resolved* by Route C's geometric Langlands machinery, *if* the scale bridge closes. Conversely, Route B's construction of $L_{\text{YM}}$ via BC/ITPFI (if it holds) provides a target structure that Route C can match.

The two routes are therefore *not independent*: they share the Langlands programme as common infrastructure. They are *complementary attacks on the same target from different angles*:

- **Route B:** classical Langlands + BC/ITPFI local factors → $L_{\text{YM}}$ with automorphic interpretation → Kim-Sarnak bounds.
- **Route C:** geometric Langlands + Kapustin-Witten scale bridge → $L_{\text{YM}}$ with geometric interpretation → Eisenstein expansion.

Both routes produce the same object ($L_{\text{YM}}$ with Langlands structure), via different constructions.

**If either route closes, both benefit.** A successful Route C scale bridge closes Route B's Ob.3 and Ob.4; a successful Route B BC/ITPFI of YM provides a concrete target for Route C's geometric-Langlands descent.

---

## 23.6. The ship criterion for Route C

**If Ob.C.1 closes, Route C ships.** All other obstructions are tied to Ob.C.1.

Minimum viable product:
- Rigorous proof that the $M_I \to \infty$ limit of N=4$^*$ produces pure YM at the factorization-algebra level.
- Verification that Gaitsgory-Raskin 2024's equivalence descends under this limit.
- Extraction of the Eisenstein-expansion coefficients and their match with perturbative YM coefficients.

If Route C ships, the YM Wilson-loop L-function $L_{\text{YM}}$ inherits:
- A factorization-algebra structure (from Elliott-Gwilliam-Williams).
- A functional equation (from 4D S-duality).
- A Satake matching (from Gaitsgory-Raskin).
- An OPE dictionary (from the factorization algebra).

Route B's obstructions Ob.3 and Ob.4 close simultaneously.

---

## 23.7. Honest confidence assessment

**Before Route C is attempted:** 3/10. The scale bridge is a hard technical problem; the geometric Langlands side is strong (Gaitsgory-Raskin PROVED), but the descent to pure YM is genuinely conjectural.

**After the perturbative + leading-gradient-flow part of Ob.C.1 closes:** 5/10. This is the "easy" part of the scale bridge and is within reach via Paper 10 scheme independence extensions.

**After the full non-perturbative scale bridge closes:** 7-8/10. This is the hard part. If it closes, H4 closes: the Gaitsgory-Raskin equivalence + Kapustin-Witten dictionary + Elliott-Gwilliam-Williams factorization algebra would all descend, and H4 would follow.

**Combined with Route B (shared obstructions closed):** 7-8/10. The scenario where Route C's scale bridge closes is *also* the scenario where Route B's Ob.3 and Ob.4 close. The two routes together would be compelling.

---

## 23.8. What Route C adds even if it does not close H4

Even if Route C does not close H4, the following are permanent additions to the programme:

1. **A geometric interpretation of H4.** H4 becomes "the asymptotic Eisenstein expansion matches the perturbative OPE," a geometrical statement rather than a QFT statement.

2. **A target for the scale bridge.** The exact claim to prove is made precise; future work can attack it directly.

3. **A bridge to Route B.** The construction of $L_{\text{YM}}$ via geometric Langlands (Route C) provides a concrete target structure for Route B's classical-Langlands construction to match.

4. **Integration with the programme's Kapustin-Witten + geometric-Langlands infrastructure.** Papers 29 (Hodge) and other programme papers already reference geometric Langlands; Route C extends the reference to include H4 and YM.

Route C is valuable *as framework development* even if its scale-bridge conjecture is not immediately resolved.

---

## 23.9. Summary of Route C

Eight steps. One critical obstruction (Ob.C.1, the scale bridge from N=4 SYM to pure YM). All other obstructions resolve together when Ob.C.1 resolves. Confidence 3/10 initially, 7-8/10 if the scale bridge closes.

Route C's attack vector: *Kapustin-Witten 2007 showed that N=4 SYM produces geometric Langlands; Gaitsgory-Raskin 2024 PROVED geometric Langlands; Elliott-Gwilliam-Williams 2024 made the observable side rigorous. Pure YM is a limit of N=4 SYM (scale bridge); Paper 10 provides partial rigor on the scale bridge. If the scale bridge is completed, H4 follows from the Eisenstein expansion of Hecke eigensheaves on the Gaitsgory-Raskin side.*

Route C is Langlands attacking YM through the geometric side. Route B is Langlands attacking through the spectral side. Together they represent the full Langlands-programme attack on YM — two complementary facets of the same fundamental symmetry.

The hardest question of Route C is not any of the Langlands results; those are either proved or strongly supported. The hardest question is the *scale bridge*: can pure YM be treated as a limit of N=4 SYM with all the Langlands structure intact? This is where the programme's rigor currently stops.

---

*Paper 50 §23. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
*Part IV complete. Parts III + IV deliver Routes B and C, both facets of the Langlands-programme attack on H4.*
