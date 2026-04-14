# Landscape — Odd Perfect Numbers (paper40)

*Ring vertex. Oldest unsolved problem. Our strategy: σ(n)=2n via Hecke-orbit + ITPFI + BSD template.*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Pascal Ochem | LIRMM Montpellier | Lower bound 10^1500; radical, component bounds |
| Michaël Rao | ENS Lyon | OPN lower bound (with Ochem) |
| Pace Nielsen | BYU | OPN structure; divisor bounds |
| Carl Pomerance | Dartmouth | OPN heuristics; combinatorial constraints |
| Keith Conrad | UConn | OPN expository |
| Paul Pollack | UGA | Perfect numbers; Erdős-style |
| William Banks | Missouri | OPN structure |
| Takeshi Goto | Nihon | OPN component bounds |
| Graeme Cohen | (emer.) | Earlier 10^300 bound |
| Richard Brent | ANU | Earlier OPN bounds |
| Herman te Riele | CWI | Earlier OPN bounds |

## Major Approaches

### 1. Structural / Size Bounds (Brent-Cohen-te Riele, Ochem-Rao)
Prove lower bounds on OPN. 1991: > 10^300 (BCR). 2012: > 10^1500 (Ochem–Rao, Math. of Comp.). Increasing the exponent.

### 2. Component / Divisor Count Bounds
OPN has ≥ 101 not-necessarily-distinct prime factors (Ochem–Rao 2012). ≥ 10 distinct prime factors (classic).

### 3. Largest Component Bounds
Largest p^a divisor > 10^62 (Ochem-Rao). Other bounds.

### 4. Radical Bounds
rad(N)^k constraints.

### 5. Sieve / Computational
Parallel computational search; no OPN found.

### 6. Heuristic (Pomerance)
Heuristic arguments against existence.

## Partial Results / Named Milestones

- Antiquity (Euclid) — even perfect ↔ Mersenne prime
- 1747 — Euler — odd perfect number must have specific form
- 1991 — Brent–Cohen–te Riele — > 10^300
- 2006 — Goto–Ohno — at least 9 distinct prime factors (later 10)
- 2012 — Ochem–Rao — > 10^1500; ≥ 101 prime factors counted with multiplicity; largest divisor > 10^62
- 2014 — Ochem–Rao radical remarks
- 2024-25 — Preprint claiming contradiction for OPN not divisible by 3

## Recent Preprints (2023-2026)

- arXiv and preprints.org (2024-25) — various claimed partial/special-case disproofs
- Preprints.org 202410.0547 — "A Note on Odd Perfect Numbers"

## Key Surveys / Textbooks

- Ochem–Rao papers at LIRMM
- Wolfram MathWorld "Odd Perfect Number"
- Pomerance expository

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Pascal Ochem & Michaël Rao** — current best bounds
- **Euler** — historical foundation
- **Richard Brent, Graeme Cohen, Herman te Riele** — previous 10^300 bound
- **Carl Pomerance** — heuristic and structural arguments

### Cite in body:
- Pace Nielsen — divisor bounds
- Paul Pollack, William Banks — analytic perfect number theory
- Euclid, Euler — historical

### Our programme's position
Our strategy treats the equation σ(n) = 2n as a fixed-point equation for a Hecke-orbit-type operator; via ITPFI factor correspondence we lift to a BSD-template with the vanishing of a certain "L-value" obstructing OPN existence. Complementary to all classical number-theoretic structural work; conditional on CBB and specific identifications.
