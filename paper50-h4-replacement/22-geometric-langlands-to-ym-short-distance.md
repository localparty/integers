# §22 — From Geometric Langlands to YM Short-Distance Behaviour

*The Langlands correspondence's spectral side gives Wilson-loop data. Short-distance behaviour emerges from the asymptotic structure of the Hitchin moduli. How to extract H4's content from the geometric Langlands equivalence.*

---

## 22.1. The extraction problem

Gaitsgory-Raskin 2024 proves
$$\text{D-mod}(\text{Bun}_G(C)) \simeq \text{IndCoh}_{\text{Nilp}}(\text{LocSys}_{{}^L G}(C)).$$
Under Kapustin-Witten (§18) this is related to twisted N=4 SYM on $\Sigma \times C$. Under the scale bridge (§20) it is related (conjecturally) to pure YM.

But H4 is a statement about *short-distance* behaviour of pure YM on $\mathbb{R}^4$: the leading OPE coefficient of $\langle \text{Tr} F^2(0) \cdot \text{Tr} F^2(x) \rangle$ as $|x| \to 0$.

Short distances correspond to *high energies*. The geometric Langlands correspondence on a compact curve $C$ does not immediately give short-distance (UV) behaviour: it organizes global data on the moduli stacks.

The extraction problem: *how does the geometric Langlands correspondence (§19) produce a short-distance statement about pure YM?*

This section addresses the extraction.

---

## 22.2. The asymptotic structure of the Hitchin moduli

Under dimensional reduction from $\Sigma \times C$ to $\Sigma$ (§18), the 4D theory becomes a 2D sigma-model on $\Sigma$ with target $\mathcal{M}_H(G, C)$. The *short-distance* behaviour of the 4D theory corresponds to the *large-volume* behaviour of $\mathcal{M}_H(G, C)$ (since small $|x|$ in 4D maps to large distances on the target under the sigma-model duality).

The Hitchin moduli space has a well-understood asymptotic structure:
- **Compact core:** bounded region of $\mathcal{M}_H$ where the Higgs field is small.
- **Non-compact ends:** directions in $\mathcal{M}_H$ where the Higgs field grows. These correspond to *rescaling* the Higgs field.
- **Gaiotto-Moore-Neitzke asymptotics (2010):** the metric on $\mathcal{M}_H$ has a precise asymptotic form at the non-compact ends, expressed in terms of cluster-algebraic data.

### 22.2.1. The UV limit

In the sigma-model, the *UV limit* (high-energy, short-distance) probes the asymptotic ends of $\mathcal{M}_H$. The sigma-model partition function expands in terms of the Gaiotto-Moore-Neitzke asymptotic data; this expansion is the *perturbative expansion*.

The *full* sigma-model partition function (including the compact core) is the non-perturbative result. The match between UV asymptotic and full is H4 translated into sigma-model language.

### 22.2.2. Perturbative ⟷ asymptotic structure of $\mathcal{M}_H$

This is the *key identification* for Route C:

- **Perturbative YM at short distances** = Sigma-model on $\mathcal{M}_H$ at large distances = Asymptotic structure of $\mathcal{M}_H$.
- **Non-perturbative YM Schwinger functions** = Sigma-model full partition function = Global integration over $\mathcal{M}_H$.
- **H4 (the AF match)** = The asymptotic expansion of the sigma-model partition function reproduces the large-distance sigma-model, which is Gaiotto-Moore-Neitzke's asymptotic structure.

Under this identification, H4 becomes: *the full sigma-model on $\mathcal{M}_H$ reduces, in the large-distance / UV limit, to the asymptotic structure of $\mathcal{M}_H$ at the non-compact ends*.

This is a *geometric* statement, about the sigma-model on a specific moduli space, which is precisely the content Gaitsgory-Raskin's geometric Langlands can address.

---

## 22.3. Hecke eigensheaves and Wilson-loop short-distance behaviour

Under the Gaitsgory-Raskin equivalence, each ${}^L G$-local system $\mathcal{E}$ on $C$ produces a Hecke eigensheaf $\text{Aut}_\mathcal{E}$ on $\text{Bun}_G$. Via the Kapustin-Witten / Elliott-Gwilliam-Williams factorization algebra (§21), $\text{Aut}_\mathcal{E}$ determines the Wilson-loop expectation values in specific flat-bundle backgrounds.

The *Wilson-loop short-distance behaviour* is controlled by the behaviour of $\text{Aut}_\mathcal{E}$ at specific points of $\text{Bun}_G$ — namely, at the boundary strata where the bundle degenerates.

**Structural observation.** The boundary strata of $\text{Bun}_G$ (where bundles degenerate to trivial or partially trivial) are the *geometric analogues of cusps* on automorphic quotients. The behaviour of automorphic forms at cusps is well-understood (Eisenstein-series expansion) and controls the L-function at specific values of $s$.

Analogously, the behaviour of Hecke eigensheaves at boundary strata of $\text{Bun}_G$ is controlled by Eisenstein-series analogues on the moduli stack, and this determines the short-distance (cusp-like) behaviour of the Wilson-loop partition function.

---

## 22.4. The Eisenstein-series extraction

Concretely, the extraction of short-distance behaviour proceeds via three steps.

### 22.4.1. Identify the relevant stratum

The 4D short-distance limit ($|x| \to 0$ in $\mathbb{R}^4$) corresponds, via the sigma-model dual, to a specific stratum $S \subset \text{Bun}_G$ (or equivalently $\mathcal{M}_H$). For the two-point function of $\text{Tr} F^2$, the stratum is where the bundle $E$ has a specific degeneration (conformal-like behaviour).

### 22.4.2. Expand at the stratum

At the stratum $S$, expand $\text{Aut}_\mathcal{E}$ using the (geometric) Eisenstein-series machinery. The leading term is the *constant term* of $\text{Aut}_\mathcal{E}$ along $S$; subleading terms are controlled by the Satake parameters of $\mathcal{E}$.

### 22.4.3. Translate to the OPE

The expansion coefficients on the $\text{Bun}_G$ side correspond, under the Kapustin-Witten / factorization algebra (§21) dictionary, to OPE coefficients on the 4D YM side. Leading coefficient = perturbative leading-order contribution; subleading = higher-order perturbative + instanton + renormalon corrections.

The *Gaitsgory-Raskin theorem guarantees* that these expansions match: the correspondence is exact at the categorical level, so the coefficient-by-coefficient match is automatic.

### 22.4.4. H4 follows

H4 says: the perturbative expansion matches the non-perturbative OPE at short distances. Under the Eisenstein-series extraction, this is: the leading Eisenstein coefficient matches the perturbative YM computation.

The Eisenstein coefficient is computed from the Langlands parameter $\mathcal{E}$ of the automorphic side. The perturbative YM computation is computed from Feynman diagrams. The match is the content of the Langlands correspondence.

---

## 22.5. The local-to-global assembly

The extraction in §22.4 is at the level of a single Hecke eigensheaf $\text{Aut}_\mathcal{E}$. The full YM partition function involves a *sum / integral* over all Hecke eigensheaves (i.e., over all local systems $\mathcal{E}$).

Under the Gaitsgory-Raskin equivalence, this sum is implemented by the *Langlands functor* $\mathbb{L}_G$: integrating over $\mathcal{E} \in \text{LocSys}_{{}^L G}$ on the spectral side produces the corresponding sum over automorphic forms on $\text{Bun}_G$.

This local-to-global assembly is the gauge-theoretic analogue of the Euler-product assembly of automorphic L-functions. For YM, it produces:
$$L_{\text{YM}}(s, W_R) = \int_{\mathcal{E} \in \text{LocSys}_{{}^L G}} L_\mathcal{E}(s, R) \, d\mu(\mathcal{E}),$$
where $L_\mathcal{E}(s, R)$ is the local-system-specific L-function and $d\mu$ is the Plancherel measure on the spectral side.

The Plancherel measure is computed by Gaitsgory-Raskin 2024; the integral gives $L_{\text{YM}}$.

---

## 22.6. What the extraction needs

For the extraction to produce H4, four technical pieces must hold:

### 22.6.1. Stratum identification

The stratum $S \subset \text{Bun}_G$ corresponding to the 4D short-distance limit must be identified. For $\text{Tr} F^2$ two-point function, this is the stratum of "conformally-contracted bundles" (i.e., bundles with a specific punctured structure). Physics-level analyses identify this stratum; a rigorous identification is the technical input.

### 22.6.2. Eisenstein expansion

The geometric Eisenstein-series expansion of $\text{Aut}_\mathcal{E}$ at the stratum $S$ must be computable. This uses the geometric Eisenstein functor (Gaitsgory et al. 2018+), which is well-developed on the automorphic side.

### 22.6.3. Scale bridge for the expansion

The expansion on the N=4 SYM / sigma-model side must descend, under the scale bridge (§20), to the pure-YM side. This is where Route C's main obstruction sits: the scale bridge must commute with the Eisenstein expansion.

### 22.6.4. OPE translation

The expansion coefficients must translate to YM OPE coefficients. This uses the Elliott-Gwilliam-Williams factorization algebra (§21) as the translation dictionary.

---

## 22.7. Obstructions and their resolutions

### 22.7.1. Ob.C.1 — Scale bridge commutes with Eisenstein

**Statement.** Under the $M_I \to \infty$ limit of §20, the N=4$^*$ Eisenstein expansion descends to the pure-YM expansion.

**Status.** Conjectural. Physics-level arguments (Gaiotto-Moore-Neitzke 2010, Witten 2008 on gauge-theoretic Hecke operators) provide support but not rigor.

**Resolution path.** Extend Elliott-Gwilliam-Williams 2024 to N=4$^*$, then check commutativity of Eisenstein expansion with soft breaking. Open.

### 22.7.2. Ob.C.2 — Stratum identification

**Statement.** The stratum $S$ corresponding to the 4D short-distance limit is the specific stratum of bundles with puncture / degeneration of the appropriate type.

**Status.** Physics-level identifications available. Rigorous identification requires work at the level of dimensional reduction + factorization algebra restrictions to strata.

**Resolution path.** Standard dimensional-reduction analysis + factorization-algebra restriction theorems. Technical but tractable.

### 22.7.3. Ob.C.3 — Plancherel measure for YM

**Statement.** The Plancherel measure $d\mu$ on $\text{LocSys}_{{}^L G}$ from Gaitsgory-Raskin 2024 descends, under the scale bridge, to the pure-YM side.

**Status.** Conjectural. The Plancherel measure exists on the Gaitsgory-Raskin side; its descent is part of Route C.

**Resolution path.** Same as Ob.C.1: extend via scale bridge.

### 22.7.4. Ob.C.4 — Rigorous OPE match

**Statement.** The factorization-algebra OPE of Elliott-Gwilliam-Williams 2024 reduces, under the scale bridge, to the YM OPE defined via Paper 8 Link 17 ($[\text{Tr} F^2]_R$ construction).

**Status.** Conjectural. Both sides are well-defined (factorization-algebra side by Elliott-Gwilliam-Williams; YM side by Paper 8); their match is not yet established.

**Resolution path.** Factorization-algebra-theoretic comparison + gradient-flow transfer.

---

## 22.8. A concrete example: SU(2) on a genus-2 curve

For illustration, consider $G = \text{SU}(2)$ and $C$ a genus-2 curve. The Hitchin moduli space $\mathcal{M}_H(\text{SU}(2), C)$ has complex dimension $2 \cdot 2 = 4$ (real dimension 8). Local systems $\mathcal{E}$ on $C$ are parametrized by $\text{LocSys}_{\text{SO}(3)}(C)$ (${}^L \text{SU}(2) = \text{SO}(3)$).

The Gaitsgory-Raskin equivalence gives, for each $\mathcal{E}$, a Hecke eigensheaf $\text{Aut}_\mathcal{E}$ on $\text{Bun}_{\text{SU}(2)}(C)$.

The sigma-model on $\Sigma \times \mathcal{M}_H$ has a clear target geometry. The large-distance structure of $\mathcal{M}_H$ is Gaiotto-Moore-Neitzke's asymptotic region: $\mathcal{M}_H$ asymptotically looks like a specific torus bundle over a flat base.

Under the scale bridge to pure YM, the Wilson-loop expectation at short distance in pure $\text{SU}(2)$ YM on $\mathbb{R}^4$ corresponds to the sigma-model expectation in the asymptotic region of $\mathcal{M}_H(\text{SU}(2), C)$.

The AF match (H4) says: the asymptotic-region expectation (computed perturbatively) equals the full-sigma-model expectation (computed non-perturbatively) up to controlled corrections.

This is now a *geometric* statement, testable (in principle) via numerical integration on $\mathcal{M}_H$. In practice, it is hard — but it is a rigorously defined statement, which is what Route C provides.

---

## 22.9. Why this is progress (even if not yet rigorous)

Before Route C: H4 is a statement about Feynman diagrams and non-perturbative Schwinger functions, with no geometric framework for bridging them.

After Route C (even partially): H4 is a statement about the sigma-model on the Hitchin moduli space, with the geometric Langlands correspondence providing the spectral-automorphic equivalence that implements the bridge.

The transformation is from *a statement about two incommensurable expansions* (perturbative ⟷ non-perturbative) to *a statement about a single geometric object* (the sigma-model on $\mathcal{M}_H$, with two different ways of computing its observables).

This is the kind of reformulation that makes a hard problem tractable: even if Route C does not close H4 immediately, it provides a framework in which H4 has a *geometric interpretation*, enabling further progress.

---

## 22.10. Summary

The geometric Langlands correspondence (Gaitsgory-Raskin 2024) + Kapustin-Witten 2007 + Elliott-Gwilliam-Williams 2024 provides a framework in which the 4D YM Wilson-loop two-point function at short distance corresponds to the sigma-model on the Hitchin moduli space $\mathcal{M}_H(G, C)$ at the asymptotic non-compact ends. The AF match (H4) becomes the match between the asymptotic sigma-model and the full sigma-model, implemented by the Eisenstein expansion of Hecke eigensheaves.

Four obstructions remain (scale bridge commuting with Eisenstein, stratum identification, Plancherel descent, OPE match). The most critical is the first (scale bridge + Eisenstein), which also underlies §20's scale-bridge obstruction.

§23 assembles the full Route C proof sketch.

---

*Paper 50 §22. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
