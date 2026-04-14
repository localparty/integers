# P vs NP — Requirements (itemized)

**Source:** `00-problem-statement.md` (Cook 2000)

## Formal requirements (either direction)

| # | Requirement | Cook source |
|---|---|---|
| 1 | Turing machine model (Σ finite, |Σ| ≥ 2) | §1 |
| 2 | P defined via polynomial-time TM | §1 |
| 3 | NP defined via polynomial-time checking relation R with polynomial witness length | §1 |
| 4 | Decide P = NP or P ≠ NP | Problem Statement |
| 5 | Must hold for general Σ with |Σ| ≥ 2 (|Σ| = 1 is a separate still-open variant) | §1 note |

## Obstructions any proof must navigate (Cook §4-§5)

| # | Obstruction | Source |
|---|---|---|
| 6 | Non-relativizing — must distinguish Π from NP in an oracle-independent way | Baker-Gill-Solovay 1975 |
| 7 | Non-natural — must not be a "natural proof" in the Razborov-Rudich sense | Razborov-Rudich 1994 |
| 8 | Non-algebrizing — must not be algebraic in the Aaronson-Wigderson sense | Aaronson-Wigderson 2008 |

Obstructions #6-#8 are not §4 gates — they are informal obligations that any §5d-compliant paper should explicitly address.

## Clay §5(b) note

> In the case of the P versus NP Problem…, a resolution in either direction will be evaluated by the standard evaluation procedure set forth in Section 7.

Either direction wins:
- **P = NP**: constructive algorithm or existence proof for a polynomial-time algorithm for an NP-complete problem.
- **P ≠ NP**: lower bound separating some NP language from P.

## Non-required but customary

- The paper's approach should be robust under standard equivalences of machine models.
- Consistency with the P-hierarchy theorem and the time-hierarchy theorem (otherwise the paper is wrong).

## §5d discipline note

Any Clay-submitted P vs NP paper must explicitly:
- State the machine model used.
- State which direction is being proved.
- Address (or disclaim, with justification) the three obstructions #6-#8.
- Not depend on unproven conjectures.

Silence on these points is a §5d compliance failure.
