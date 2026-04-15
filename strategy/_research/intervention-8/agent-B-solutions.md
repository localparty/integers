# Agent B — solutions/ sweep (Intervention 8, 2026-04-15)

## Summary
- Files scanned: 30
- Files with migrations: 3
- Total migrations: 5
- Breakdown: dimension 5 | postulation 0 | labels 0 | e-circle 0 | choice 0

## Per-file report

### 1. `/Users/gsix/quantum-geometry-in-5d-latex/solutions/paper31-baum-connes/00-proof-skeleton.md`
- Drift class: **dimension language** (Canon entry 1)
- Count: 1
- Line 86 — before: `The 5D geometry is encoded in the spectral triple (A, H, D), and A is the BC algebra.`
- After: `The ~~5D geometry~~ 4+1 coordinate structure <!-- legacy 2026-04-15: "5D geometry" → "4+1 coordinate structure" per north-star.md §0.10 Vocabulary Canon, Intervention 8 (Agent B) --> is encoded in the spectral triple (A, H, D), and A is the BC algebra.`

### 2. `/Users/gsix/quantum-geometry-in-5d-latex/solutions/paper13b-grh/strategy/00-grh-attack-plan.md`
- Drift class: **dimension language** (Canon entry 1)
- Count: 2

**Occurrence 2a — line 62**
- Before: `... each corresponding to a crystallographic constraint on the 5D geometry. Each k produces ...`
- After: `... each corresponding to a crystallographic constraint on the ~~5D geometry~~ 4+1 coordinate structure <!-- legacy 2026-04-15: "5D geometry" → "4+1 coordinate structure" per north-star.md §0.10 Vocabulary Canon, Intervention 8 (Agent B) -->. Each k produces ...`

**Occurrence 2b — line 284**
- Before: `The gauge hierarchy problem (Paper 12) requires fine-tuning cancellations in the 5D compactification.`
- After: `The gauge hierarchy problem (Paper 12) requires fine-tuning cancellations in the ~~5D compactification~~ 4+1 coordinate structure (S¹ internal phase fiber) <!-- legacy 2026-04-15: "5D compactification" → "4+1 coordinate structure (S¹ internal phase fiber)" per north-star.md §0.10 Vocabulary Canon, Intervention 8 (Agent B) -->.`

### 3. `/Users/gsix/quantum-geometry-in-5d-latex/solutions/paper32-bgs-spectral-statistics/00-proof-skeleton.md`
- Drift class: **dimension language** (Canon entry 1)
- Count: 2

**Occurrence 3a — line 62**
- Before: `**Energy-level spacing of 5D geometry.** In the QG5D framework, ...`
- After: `**Energy-level spacing of ~~5D geometry~~ the 4+1 coordinate structure.** <!-- legacy 2026-04-15: "5D geometry" → "4+1 coordinate structure" per north-star.md §0.10 Vocabulary Canon, Intervention 8 (Agent B) --> In the QG5D framework, ...`

**Occurrence 3b — line 105**
- Before: `- **BGS --> QG5D:** GUE statistics = quantum chaos of the 5D geometry.`
- After: `- **BGS --> QG5D:** GUE statistics = quantum chaos of the ~~5D geometry~~ 4+1 coordinate structure <!-- legacy 2026-04-15: "5D geometry" → "4+1 coordinate structure" per north-star.md §0.10 Vocabulary Canon, Intervention 8 (Agent B) -->.`

## Notes / edge cases

- **Drift classes 2, 3, 4, 5 all ZERO across solutions/.** Grep for "we propose" / "we postulate" / "we assume" / "we choose" / "we set" / "we fix" / "Postulate P_i" / "Axiom" / "five-dimensional" / "extra dimension" / "5th dimension" / "compactified dimension" returned **no matches** under solutions/. The solutions corpus was drafted in the 2026-04-12+ window and already uses derivation-register language.
- **`T^2` in `paper40-odd-perfect/06b-E2-quasi-modular-obstruction.md`** (lines 91, 178) is the modular-form generator $\langle T^2, S \rangle$ of the theta group `Gamma_theta`, NOT the programme torus $T^2 = S^1_{geo} \times S^1_{spec}$. No e-circle/torus confusion — preserved verbatim.
- **`axiom` in `solutions/README.md` line 27** refers to Hilbert's 6th problem ("axiomatization of physics") which is the problem's classical name, NOT programme P1-P4. Preserved verbatim.
- **`QG5D` as programme identifier** appears in ~8 locations across the corpus (e.g., `paper40-odd-perfect/00-research-programme.md:215`, `paper31-baum-connes/00-proof-skeleton.md:20,85`, `paper13b-grh/strategy/00-grh-attack-plan.md:284`, `paper35-schanuel/00-research-programme.md:13`, `paper32-bgs-spectral-statistics/00-proof-skeleton.md:62,105`). Per Phase 11.1 this is a **separate drift class** ("stale programme-name references: QG5D is Paper 1, the programme is Integers") — **NOT** part of §0.10 Vocabulary Canon scope. Out of Agent B scope; flagged below for the programme-name-drift intervention.
- **`PROOF-CHAIN-MOVED.md` stubs** (13 files) contain only redirect pointers — zero prose content, zero drift.
- **Idempotency check**: zero pre-existing `<!-- legacy ... §0.10 -->` annotations in solutions/. This is the first §0.10 self-healing pass on this corpus.

## Flagged for human review

1. **`QG5D`-as-programme-name drift** (8+ occurrences under solutions/). Deferred to a separate self-healing intervention (programme-name canon per north-star §0.1), not §0.10.
2. **`solutions/README.md:5`**: *"This corpus contains the conjecture-solving papers that do not carry an [active prize]..."* — uses "conjecture-solving" framing rather than derivation register. Borderline — "conjecture" here is the community's classification of the target problem, not a claim about our programme's stance. No migration applied; flagged for editorial preference call.
3. The repo-root directory name `quantum-geometry-in-5d-latex` itself contains "5d". Out of scope (not a prose file), but note for meta-level naming review.
