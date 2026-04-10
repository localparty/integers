# Strategy 31 — Cycle 3: Genuinely New Angles

*Ledger read. 34 closed leads, all hitting Connes' wall from*
*different angles. Three NEW directions from online search.*

*Date: 2026-04-10, Cycle 3 of 10*

---

## Three new directions (none previously explored)

### N1: De Branges space + Weil distribution
**Source:** arXiv:2301.00421 (2023), preprint on Hilbert-Pólya via de Branges
**NOT in ledger. GENUINELY NEW.**

The Hilbert space from the Weil distribution (under RH) is
isomorphic to a de Branges space. De Branges spaces have
BUILT-IN eigenvalue simplicity (the reproducing kernel forces
simple zeros of the Hermite-Biehler function).

**Connection to us:** Our Cartwright argument proves the overlaps
are nonzero (at finite N). The de Branges framework might give
the UNIFORM gap bound we need, because de Branges spaces have
STRUCTURAL simplicity — not proved case by case, but built into
the axioms.

**The idea:** Instead of proving eigenvalue gaps directly,
show that QW_λ^N lives in (or maps to) a de Branges space.
Then simplicity comes for free from the de Branges axioms.
The limit N → ∞ preserves de Branges structure (if the
spaces are nested).

### N2: Pseudo-random prime perturbation → polynomial gaps
**Source:** Random perturbation literature (Tao-Vu, Nguyen)
**NOT in ledger.** (K-related leads were about SPECIFIC matrices, not randomness)

Adding random perturbation to a deterministic matrix gives
polynomial eigenvalue gaps: gap ≥ N^{-C} with high probability.
Our prime vectors are PSEUDO-random (by PNT/Sato-Tate). If
we can show the prime perturbation has enough "randomness"
to guarantee polynomial gaps, Step 10 closes.

**The idea:** The Weil quadratic form QW^N = QW^0 + Σ (rank-one
from primes). Each prime perturbation is deterministic but
the ENSEMBLE of primes behaves pseudo-randomly (equidistribution
of log p mod 1, Sato-Tate, etc.). A pseudo-random gap bound
might follow from the prime number theorem.

### N3: Guth-Maynard (2024) zero density improvement
**Source:** Quanta Magazine, 2024. First improvement to
Ingham's 1940 bound on zero exceptions.
**NOT directly in our framework, but related to I5 (Bombieri count).**

Guth-Maynard bound the number of zeros OFF the critical line
more tightly than anyone in 80 years. If their method can be
combined with our Cartwright simplicity at finite N, the
number of possible off-line zeros might be shown to be zero.

---

## Priority

| # | Direction | Why | Feasibility |
|:--|:--|:--|:--|
| 1 | N1 (de Branges) | Structural simplicity; new framework | 5/10 |
| 2 | N2 (pseudo-random gaps) | Direct attack on Step 10 wall | 4/10 |
| 3 | N3 (Guth-Maynard) | Established new result; zero density | 3/10 |
