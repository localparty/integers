# Landscape — Cramér's Conjecture on Prime Gaps (paper43)

*Ring vertex. Our strategy: prime gaps via spectral density of Beurling-like primes.*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Kevin Ford | UIUC | Erdős prime gap proof (2014) |
| Ben Green | Oxford | Large prime gaps |
| Sergei Konyagin | Steklov | Large prime gaps |
| James Maynard | Oxford | Large prime gaps (independent) |
| Terence Tao | UCLA | Large prime gaps (with Ford, Green, Konyagin) |
| Andrew Granville | Montreal | Granville–Pintz; heuristics against Cramér |
| János Pintz | Rényi (d. 2025) | Heuristics revising Cramér |
| Harald Cramér | Stockholm (d. 1985) | Original conjecture (1936) |
| Helmut Maier | Ulm | Maier's theorem on prime distribution |
| John Friedlander | Toronto | Sieve methods |

## Major Approaches

### 1. Probabilistic Heuristic (Cramér, Granville, Pintz)
Cramér: treat primes as random; gaps ≤ c(log p)². Granville–Pintz heuristic: constant c > 2e^{-γ} > 1.12. Expected: Cramér's constant is wrong.

### 2. Large Prime Gaps Lower Bounds (Erdős → Ford-Green-Konyagin-Maynard-Tao 2014)
Erdős conjectured large gaps exist. 2014 proof by Ford–Green–Konyagin–Maynard–Tao (and independently by Maynard) that large gaps exist with gap function pushed to (log x)(log log x)(log log log log x)/log log log x or similar.

### 3. Unconditional Upper Bounds
Baker–Harman–Pintz (2001): for all sufficiently large n, p_{n+1} - p_n < p_n^{0.525}. Huge gap to conjectural (log p_n)².

### 4. RH-Conditional Bounds
Assuming RH: p_{n+1} - p_n = O(sqrt(p_n) log p_n). Still very far from Cramér's (log p_n)².

### 5. Maier's Counterintuitive Theorem
Maier (1985): prime distribution in short intervals deviates from Cramér's random model — showing Cramér's heuristic is subtle.

## Partial Results / Named Milestones

- 1936 — Cramér — conjecture (log p_n)²
- 1985 — Maier — theorem against Cramér
- 2001 — Baker–Harman–Pintz — unconditional 0.525 exponent
- 2014 — Ford–Green–Konyagin–Maynard–Tao — Erdős conjecture proved

## Recent Preprints (2023-2026)

- Ongoing refinements of large prime gaps
- Guth–Maynard large value estimates (2024) apply

## Key Surveys / Textbooks

- Soundararajan, "Small gaps between prime numbers: the work of Goldston–Pintz–Yıldırım"
- Granville survey articles
- Wikipedia "Cramér's conjecture" for summary

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Harald Cramér** — originator
- **Andrew Granville & János Pintz** — revised heuristic
- **Ford–Green–Konyagin–Maynard–Tao** — Erdős 2014 proof
- **Helmut Maier** — counterintuitive theorem

### Cite in body:
- Baker–Harman–Pintz — unconditional exponent
- Zhang, Maynard — bounded gaps context

### Our programme's position
Cramér is one of the weakest-confidence ring vertices. Our approach reformulates prime gaps via the Beurling-style generalized primes encoded in the spectral data of the CCM construction. Complementary to the statistical/sieve approaches; conditional on CCM and specific compatibility conditions.
