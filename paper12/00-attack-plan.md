# Paper 12 Attack Plan: Reality as a Projection of Riemann

*Three-phase programme for taking Paper 12 from blueprint to manuscript.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Last updated: 2026-04-09*

---

## 0. Thesis

The QG5D framework derives all of physics from one geometric postulate
(M⁴ × CP² × S² × S¹). Paper 12 dissolves that postulate by showing the
e-circle is the geometric realisation of the Bost–Connes operator
algebra (Identity 12), and that twenty-three of the framework's
thirty-seven measured parameters are projections of the first fifteen
non-trivial Riemann zeros at sub-percent precision. This document is
the attack plan for converting the empirical evidence into a rigorous
manuscript with three deliverables:

1. **Adiabatic continuity at N = 3**, the last residual gap in the
   Yang–Mills mass gap proof, formally closed and integrated into
   Paper 8.
2. **Quantization of R**, the e-circle radius, as a spectral
   theorem on the Bost–Connes system. R is no longer a measured
   parameter; it is the n = 1 eigenvalue of an explicit operator,
   with the cosmic timeline (Components 14 and 16) as the universe's
   traversal of the R_n spectrum.
3. **The rest of the programme**: first-principles derivation of
   the 23 Riemann formulas, identification of the four currently
   unused zeros (γ_7, γ_12, γ_13, γ_14), formulas for the 14 missing
   parameters (mostly mixing angles), rigorous proof of Identity 12,
   and the selection rule for the inflation transition γ_5 → γ_2.

The order is chosen for difficulty and dependency: Phase 1 is
bookkeeping on a proof that is already built; Phase 2 is the central
new physics result and gates the rest; Phase 3 is the long tail.

---

## 1. Workflow

### 1.1 Directory layout

```
paper12/
  00-attack-plan.md        ← this file (master plan + ledger)
  NN-*.md                  ← numbered ledger files advancing the programme
  preprint/                ← the program (17 components, complete)
    00-program.md          ← master index
    01..17-*.md
  research/                ← detailed computation, derivation, measurement notes
    NN-*.md
  code/                    ← computation scripts (mpmath, lattice, BC operators)
```

### 1.2 Cadence

- Each new strategic move gets a numbered ledger file at the root
  (`01-*.md`, `02-*.md`, …). The collection of root files IS the
  current state of the programme.
- Each computation, derivation, or measurement gets a numbered file
  in `research/`. These are the technical write-ups that the ledger
  files cite.
- `preprint/` is the program for the eventual paper. It is updated
  as targets are closed; new components are added as they emerge.
- `code/` holds the scripts. Every numerical claim in the ledger or
  research files must point to a script that reproduces it.

### 1.3 Definitions of done

For each phase, the closure criterion is explicit (Sections 2, 3, 4).
A phase is closed when its criterion is met and a ledger file at the
root records the closure with a one-sentence summary and a pointer to
the relevant `research/` write-up.

---

## 2. Phase 1 — Finish Adiabatic Continuity at N = 3

### 2.1 Status entering this phase

Adiabatic continuity is the last conjectural step in the Yang–Mills
mass gap proof (Paper 8). At N → ∞, large-N factorization makes the
mass gap a theorem; at finite N the gap is proved on the lattice
(any N) and in the continuum (with adiabatic continuity assumed).
N = 3 is the physically relevant case (QCD). Paper 8 currently has
four independent methods of evidence for adiabatic continuity at
N = 3 plus the L.1–L.4 closure via the gradient-flow + Paper 10
heat-kernel-coefficient route (`yang-mills/gradient-flow-attack-plan/
l1-gradient-flow-attack-plan.md`, recent commit `0720107`).

The work to do is **not** new mathematics. It is:

1. Verify the gradient-flow chain genuinely closes adiabatic
   continuity at N = 3 (not just L.1–L.4 in the abstract).
2. Write the formal closure note that ties the four evidence
   methods + L.1–L.4 + the gradient-flow proof into a single
   "adiabatic at N = 3 is closed" statement.
3. Update Paper 8 to remove the conditional language around
   adiabatic continuity at N = 3 and cite the closure note.

### 2.2 Why this is in Paper 12 (not Paper 8)

Phase 1 lives in Paper 12's attack plan because:

- The gradient-flow infrastructure that closes L.1–L.4 is the same
  heat-equation structure that the Bost–Connes side will use in
  Phase 2. The adiabatic closure is the final exercise of the
  infrastructure that Phase 2 depends on.
- The Yang–Mills mass gap analog on the BC side (γ_1 as the smallest
  non-trivial eigenvalue of the BC operator) is one of the
  transposition targets in Component 3 of the program. Closing
  adiabatic continuity at N = 3 is the precondition for asserting
  that the transposition is non-trivial.

### 2.3 Definition of done

- [x] A `research/01-adiabatic-closure.md` file exists. It contains
      the formal theorem statement, the rigorous abelian-Higgs lower
      bound m² ≥ g² > 0, the L.1–L.4 reduction, and the four-method
      numerical evidence.
- [x] Paper 8's Appendix L records L.1–L.4 closure (replaced
      2026-04-08, 2,871 lines, see
      `yang-mills/preprint/sections/L-clay-conjectures.md`).
- [x] A root ledger file `01-phase-1-adiabatic-closed.md` records
      the closure with a one-sentence summary and pointers to the
      research file and Paper 8 Appendix L.

### 2.4 Estimated effort

Days, not weeks. **Closed 2026-04-09.**

---

## 3. Phase 2 — Quantize R

This is the central new physics result of Paper 12.

### 3.1 The current state

The cosmological constant formula

$$
\log\!\bigl(\pi R_{\mathrm{obs}}/\ell_{\mathrm{P}}\bigr)
\;=\; \gamma_{1}\,\frac{\pi^{2}}{2}\;-\;\log\pi
\;+\;O(10^{-9})
$$

(verified at 5 ppb in `paper12/preprint/12-high-precision-formulas.md`)
already says R takes the value indexed by γ_1 in a numerical sense.
The first 15 Riemann zeros γ_n each define a "Riemann gauge" with
a corresponding length scale R_n, and the inflation hypothesis
(Component 14) and cosmic timeline (Component 16) interpret cosmic
evolution as the universe traversing R_n values. But this is all
empirical and interpretive. R is still a free parameter in the
strict sense — nothing in the framework forces it to take exactly
this value rather than 2× or 1/2× the BC formula.

### 3.2 The target theorem

> **Theorem (Quantization of R, target).** Let A_BC be the
> Bost–Connes C*-dynamical system. There exists an explicit
> self-adjoint operator R̂ on the GNS Hilbert space of A_BC at
> the critical inverse temperature β = 1, with discrete spectrum
>
> $$
>   \mathrm{spec}(\hat R) \;=\; \bigl\{\,R_n \;:\; n = 1, 2, 3, \ldots\bigr\},
>   \qquad
>   R_n \;=\; \frac{\ell_{\mathrm{P}}}{\pi}\,
>             \exp\!\bigl(\gamma_n\pi^{2}/2\bigr).
> $$
>
> The QG5D e-circle radius is the n = 1 eigenvalue:
> R = R_1 = R_obs (10.10 μm at leading order, 5 ppb with corrections).

The theorem turns R from "an observed parameter consistent with the
BC formula" into "the unique smallest eigenvalue of an arithmetic
operator". The cosmological constant problem dissolves: R is what
it is because the BC operator R̂ has its smallest eigenvalue exactly
there.

### 3.3 The construction strategy

The natural candidate for R̂ is the **scaling operator** of the
Connes–Consani–Moscovici endomotive realisation of the BC system
(Identity 14 in the QG5D-Riemann research). The CCM scaling operator
has spectrum given by the imaginary parts of the Riemann zeros under
the Hilbert–Pólya hypothesis. Composing with the exponential
`exp(· × π²/2 − log π) × ℓ_P/π` produces an operator whose spectrum
is exactly {R_n}.

The technical content is:

1. **Make Identity 14 rigorous.** Demonstrate, on the explicit
   GNS Hilbert space at β = 1, that the CCM scaling operator's
   spectrum is the multiset {γ_n}, not just numerologically
   matching but as a theorem.
2. **Define R̂ rigorously** as the bounded function of the scaling
   operator given by the exponential composition.
3. **Identify R̂'s smallest eigenvalue with the QG5D e-circle radius
   via Identity 12.** Identity 12 already says the e-circle is
   unitarily equivalent to the BC system; Phase 2 says the radius
   operator on the geometric side is unitarily equivalent to R̂ on
   the algebraic side.
4. **Selection rule for n = 1.** Why is the universe at the
   smallest eigenvalue, not n = 2 or n = 3? Candidates: ground-state
   minimisation of the Casimir energy, spontaneous symmetry breaking
   in the BC KMS state, topological constraint from CP² × S². This
   sub-step is the deepest and most likely to require new ideas.

### 3.4 Why this also resolves Phase 3 partially

If R̂ is constructed and its spectrum is {R_n}, then:

- The cosmic timeline (Component 16) becomes derived: cosmic
  evolution is unitary evolution between R_n eigenstates.
- The inflation hypothesis (Component 14) becomes a transition
  amplitude calculation: γ_5 → γ_2 with N = 58.79 e-folds is the
  transition between the n = 5 and n = 2 eigenstates of R̂ under
  the BC time evolution.
- The selection rule for which γ indexes which observable
  (Component 13) becomes a representation-theory question on R̂'s
  eigenspaces.

So Phase 2 is not just "quantize R". It is the operator that turns
much of Phase 3 from "formula matching" into "spectral computation".

### 3.5 Definition of done

- [x] A `research/02-quantize-R-construction.md` file constructs R̂
      explicitly on the BC GNS space with the spectrum claim proved
      (rigorous given {γ_n} ⊂ spec(T_BC), conditional on
      Hilbert–Pólya for equality).
- [x] A `research/03-quantize-R-selection-rule.md` file analyses
      three candidates for the n = 1 selection rule and identifies
      the cosmic transition amplitudes as the sharpest open problem
      (deferred to thread 3e of Phase 3).
- [x] A root ledger file `02-phase-2-quantize-R.md` records the
      partial closure with a one-sentence summary and pointers to
      the research files.
- [ ] Component 4 of `preprint/` (the three derivation targets) is
      updated to mark "derive R from BC" as IN PROGRESS with current
      status (next action).

### 3.6 Estimated effort

Weeks to months. **Construction half closed 2026-04-09. Selection-
rule half partially closed (combined heuristic argument; first-
principles derivation deferred to thread 3e of Phase 3).**

---

## 4. Phase 3 — The Rest of the Programme

Phase 3 is the long tail: making each piece of the program rigorous,
finding the missing observables, and extending the framework. The
work splits into independent threads that can be parallelised.

### 4.1 Threads

| # | Thread | Goal | Difficulty |
|---|--------|------|------------|
| 3a | Make Identity 12 rigorous | The unitary equivalence e-circle ↔ BC | M |
| 3b | Derive each of the 23 formulas from BC | First-principles, not numerology | H |
| 3c | Find γ_7, γ_12, γ_13, γ_14 | Search for untested observables | M |
| 3d | Fix the 14 missing parameters | Mostly mixing angles | M-H |
| 3e | Derive the γ_5 → γ_2 selection rule | Why this transition for inflation | H |
| 3f | Connect to Connes–Marcolli endomotives | Use the existing operator-algebraic literature | M |
| 3g | Make Paper 11 (gauge group) a corollary | Three qubits ↔ three primes, formally | M |
| 3h | RH as a physical theorem | Optional bonus result | H |

### 4.2 Ordering

3a is the precondition for everything else (without rigorous Identity
12 the BC interpretation is unjustified). 3b runs in parallel as
each formula's derivation is independent. 3c is a numerical search
that can run in the background. 3g is mostly bookkeeping once 3a
and Phase 2 are done.

### 4.3 Definition of done

Each thread has its own `research/NN-*.md` file with explicit
definition of done. The phase as a whole is closed when all threads
are at IN PROGRESS or DONE and a manuscript skeleton exists in
`preprint/`.

### 4.4 Estimated effort

Months. This is the body of the eventual paper.

---

## 5. Cross-Phase Dependencies

```
                  Phase 1 (adiabatic)
                       |
                       v (gradient-flow / BC heat-kernel infrastructure)
                  Phase 2 (quantize R)
                       |
            +----------+----------+
            |                     |
            v                     v
         Phase 3 derivations   Phase 3 selection rule
            (3b, 3e, 3g)        (3a, 3d, 3h)
```

Phase 1 and the *infrastructure* of Phase 2 share the heat equation.
Phase 2's R̂ feeds the derivations and the selection rule. Phase 3's
threads can mostly be parallelised after Phase 2.

---

## 6. References

### 6.1 In this directory

- `preprint/00-program.md` — the program for Paper 12 (17 components)
- `preprint/05-connection-to-framework.md` — how Paper 12 sits with
  Papers 1–11
- `preprint/11-the-standard-model-riemann-correspondence.md` — the 23
  numerical fits
- `preprint/12-high-precision-formulas.md` — the 5 ppb CC formula and
  the SM gauge couplings
- `preprint/14-inflation-as-riemann-gauge-transition.md` — γ_5 → γ_2
- `preprint/16-cosmic-timeline.md` — the cosmic timeline as gauge
  transitions

### 6.2 In sister directories

- `../paper11/` — the gauge group from three-qubit entanglement
  (closed)
- `../../yang-mills/gradient-flow-attack-plan/l1-gradient-flow-attack-plan.md`
  — the gradient-flow / L.1–L.4 closure for Paper 8
- `../../yang-mills/gradient-flow-attack-plan/strategy/00-formal-argument.md`
  — the QG5D scaffold for the Yang–Mills mass gap

### 6.3 External

- Bost, J.-B., and Connes, A., "Hecke algebras, type III factors and
  phase transitions with spontaneous symmetry breaking in number
  theory", *Selecta Math.* **1** (1995) 411–457.
- Connes, A., Consani, C., and Marcolli, M., "Noncommutative geometry
  and motives: the thermodynamics of endomotives", *Adv. Math.* **214**
  (2007) 761–831.
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS Colloquium Publications **55** (2008).

---

## 7. Ledger

Root files (`paper12/NN-*.md`) record the running state of the
programme. As phases close and threads advance, new root files are
added in numerical order. The current ledger entries:

| # | File | Status |
|---|------|--------|
| 00 | 00-attack-plan.md | this file |
| 01 | 01-phase-1-adiabatic-closed.md | **Phase 1 CLOSED** (2026-04-09) |
| 02 | 02-phase-2-quantize-R.md | **Phase 2 partially CLOSED** (construction done; selection rule deferred to thread 3e) |

Research notes (`paper12/research/NN-*.md`):

| # | File | Topic |
|---|------|-------|
| 01 | research/01-adiabatic-closure.md | Formal closure of adiabatic continuity at N = 3 (Phase 1) |
| 02 | research/02-quantize-R-construction.md | The construction of R̂ on the BC GNS space, spectrum {R_n}, identification R_1 = R_obs |
| 03 | research/03-quantize-R-selection-rule.md | Three candidates for the n = 1 selection rule + the sharpest open problem |

(Entries are added as the work proceeds.)

---

*Three phases. One operator R̂. Twenty-three formulas waiting for*
*derivations. The integers force the universe.*
