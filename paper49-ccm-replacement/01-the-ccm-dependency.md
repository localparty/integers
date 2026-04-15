# §01 — The CCM Dependency and Why It Bothers Us

*Paper 49, Part I: Motivation. The programme's single biggest external dependency. Three vertices on the ring — RH (8/10), GRH (7/10), BGS (7/10) — gated by one preprint. This section audits the dependency and states the problem Paper 49 solves.*

---

## The preprint

In late 2025, Alain Connes, Caterina Consani, and Henri Moscovici posted
arXiv:2511.22755 ("Spectral realization of the Riemann zeros via
prolate spheroidal wavefunctions and Carathéodory-Fejér stabilization").
The construction is mathematically clean: for each truncation level $N$
(primes $p \leq P_N$), they define a family of self-adjoint operators
$D_N$ on even-sector Hilbert spaces $E_N^+$ whose eigenvalues
approximate the first $N$ Riemann zeros $\{\gamma_n\}$ to 55-digit
accuracy at $\lambda = \sqrt{13}$, $N = 120$.

The operators are built from three ingredients:

1. **Prolate spheroidal wavefunctions** (Slepian-Pollak 1961) providing a
   time-frequency-localized basis on a band $[-\lambda, \lambda]$.
2. **Carathéodory-Fejér stabilization** guaranteeing self-adjointness of
   the finite-$N$ matrix approximations.
3. **The Bost-Connes Hecke algebra** as the arithmetic skeleton,
   with eigenvalues coming from a Mellin-dual spectral realization.

The construction is rigorous. The three authors are among the world's
leading mathematicians. The numerical agreement at 55 digits is
compelling. We expect the paper to pass peer review.

## Why a preprint is a liability

A paper on arXiv is not a theorem. It is a candidate theorem. Until a
journal's editorial board and referees have vetted the argument, a
preprint may contain undetected errors, undisclosed gaps, or tacit
assumptions that do not survive scrutiny. The history of mathematics
is littered with preprints that looked correct and turned out to need
substantial repair — sometimes the repair succeeds, sometimes it
produces a different (weaker) theorem.

The ~~QG5D~~ Integers<!-- legacy 2026-04-15 Intervention 8b §0.10 §0.1: "QG5D" (programme shorthand) → "Integers" --> programme has a policy, inherited from Paper 1: every
external input to a proof chain is classified by its peer-review
status. We distinguish four tiers:

- **Classical / textbook** (>10 years, in standard references,
  teaching material): essentially risk-free.
- **Published / peer-reviewed** (in a refereed journal, <10 years):
  low risk; may have minor corrections.
- **Preprint / under review** (on arXiv or similar, not yet published):
  moderate risk; conclusions may change.
- **Programme-internal** (proved in one of our own papers): risk
  equals our own proof quality, which we can audit.

CCM is in tier 3. The programme's other external inputs are in tiers
1-2: Bost-Connes 1995 (Selecta Math., 30 years classical), Taylor 2011
(Sato-Tate, 15 years published), Lindenstrauss 2006 (Ann. Math., 20
years published, Fields-Medal work), Bögli 2017 (arXiv refereed), and
the textbook material on Tomita-Takesaki (1970, in every operator-algebra
textbook since 1980). CCM is the single tier-3 dependency.

## The three vertices it gates

Paper 13 (RH) currently lists its confidence as **8/10**, with the
note: *"Conditional on CCM (arXiv:2511.22755). Upon journal
acceptance, chain upgrades to 9/10."* Layers 2-6 of Paper 13 are
independently 9-10/10. Layer 1 — the existence of CCM's operators
$D_N$ with their spectral approximation property — is the one wall.

Paper 13b (GRH) inherits directly via a character-twisted extension of
every layer. Confidence **7/10**.

Paper 32 (BGS — Bohigas-Giannoni-Schmit) inherits via spectral
statistics: GUE pair correlation of zeros reduces to spectral
statistics of the CCM limit operator. Confidence **7/10**.

Three vertices. One preprint. If the preprint has an undisclosed gap,
all three drop in confidence simultaneously. If the preprint changes
substantively during peer review, all three need revision.

This is a structural fragility the programme does not elsewhere have.

## Audit: what CCM provides vs what the programme already has

| CCM contribution | Programme substitute? |
|---|---|
| Prolate-basis finite-$N$ approximation of the Mellin operator | No direct substitute, but not structurally required (see §29) |
| Carathéodory-Fejér stabilization for self-adjointness at finite $N$ | Replaceable by functional calculus on the modular operator (see §30) |
| Theorem 5.10: eigenvalue identification on the even sector | Programme has: Paper 13 Layer 5 Hurwitz argument (independent) |
| Lemma 5.2(i): $T$ commutes with parity involution $\gamma$ | Programme has: BC algebra's $\hat{\mathbb{Z}}^*$-symmetry $-1$ action |
| Lemma 7.3: $\hat{k}_\lambda \to \Xi$ uniformly on compacts | Programme has: Estimate (b) via ITPFI triangle (Paper 13 research/37) |
| Existence of $D_N$ with the right spectrum | **The one irreducible external input.** This paper replaces it. |

The last row is the entire story. Every other piece CCM contributes
either has a programme-internal substitute already, or is not structurally
needed. The only thing the programme actually *uses* from CCM is the
assertion that operators $D_N$ exist with the right spectral
approximation property — a self-adjoint spectrum convergent to the
Riemann-zero set.

Paper 49's claim: we can construct that spectrum without CCM. The
Bost-Connes algebra's own modular data produces the Hilbert-Pólya
operator directly, via Tomita-Takesaki. The route is different. The
conclusion is the same. The external dependency dissolves.

## Why we didn't see this earlier

The programme has known since Paper 13's first draft that the CCM
dependency was a liability. Two reasons we didn't construct Paper 49
earlier:

1. **The substitute looked harder.** Tomita-Takesaki on a type III$_1$
   factor is technical. Building the Hilbert-Pólya operator from the
   modular data requires a parity sector, a spectral-gap analysis, and
   a matching argument against the Weil explicit formula. Each of
   those pieces looked, from far away, like more work than "just wait
   for CCM to be refereed."

2. **The programme's infrastructure was still assembling.** As of late
   2025, Paper 13 Layer 2 (ITPFI factorization) had one proof. Paper
   32 (BGS) L2 (modular flow ergodicity) was projected but not
   written. Paper 44 (Sato-Tate framing) was a stub. Paper 48 (QUE)
   did not exist. The substitute construction would have required
   inventing each of those supports.

Between October 2025 and April 2026, the programme assembled. ITPFI
got three independent proofs (Paper 13 research/265). BGS L2 closed
via Path B (factoriality + trivial center + Tomita-Takesaki). Paper
44 got its Taylor-2011 anchor. Paper 48 got its Lindenstrauss-2010
anchor. The CBB operator dictionary ($\kappa = 2/\pi^2$, $\hat L = \log
\hat R$) stabilized in Paper 12. Each of these was built for its own
reasons, not for Paper 49 specifically.

On April 14, 2026 — the day the e-circle revealed its eight faces and
the S-duality diagnostic sharpened — it became visible that all the
pieces were in place. The Hilbert-Pólya operator was not far away.
It was already there, built out of the programme's own modular data,
waiting to be named. Paper 49 is the naming.

## What this paper is and isn't

**What Paper 49 is.** A proof-chain that constructs a self-adjoint
operator $D$ on the even-sector Hilbert space of the BC-algebra KMS$_1$
representation, using only Tomita-Takesaki theory (classical 1970)
applied to programme-internal objects (the BC algebra, the ITPFI
factorization, the modular flow ergodicity). The construction avoids
prolate spheroidals, avoids Carathéodory-Fejér stabilization, and
avoids every preprint-tier citation.

**What Paper 49 is not.** A refutation of CCM. We expect CCM to pass
peer review; we expect its construction to be unitarily equivalent to
Paper 49's on the relevant sectors; we expect the two approaches to
give the same eigenvalues. The disagreement is not mathematical. It is
*structural*: CCM's route goes through a specific numerical-analytic
machine (prolates + CF); Paper 49's route goes through the algebra's
own canonical modular data. The two routes answer the same question,
but Paper 49's route never needed the machine.

## The target

When Paper 49 closes, the Paper 13 chain's Layer 1 (the CCM-external
input) becomes replaceable by an internal construction. Paper 13's
confidence upgrades from 8/10 to 9/10 *without waiting for CCM's peer
review*. Paper 13b (GRH) and Paper 32 (BGS) inherit automatically. The
programme's three highest-confidence analytic vertices become
unconditional on external preprints.

This was the pending gap G Six identified as "the direction I've been
heading since Yang-Mills." Paper 49 is that direction made explicit.

---

*Next: §02 — the Hilbert-Pólya vision, 113 years old and finally
operationally realized.*
