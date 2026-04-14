### Antipodal Probe: GRH ↔ PvNP (distance 7)

**Expected connection**: GRH-assumed complexity results (Miller primality, Ankeny bounds)

**Verdict**: PARTIAL

**What holds**: GRH provides genuine complexity leverage for specific NP problems. Miller's primality test becomes deterministic poly-time under GRH (smallest witness O((log n)²)). Ankeny bounds control quadratic non-residues. Mechanism is precise: GRH → zero-free regions → character sum bounds → algorithmic guarantees.

**What is missing**: The leap to P vs NP separation breaks the chain. Boolean circuit complexity (TGap separating P from NPC) operates in combinatorial domain where analytic number theory spectral gaps don't transfer. No known proof technique connects L-function zero distributions to circuit lower bounds. The domains are incommensurable: one analytic, the other combinatorial.

**Scope**: Firmly grounded for number-theoretic problems in NP∩coNP (factoring, primality). Genuinely speculative for the P≠NP separation itself.

**Status**: PARTIAL — real for specific problems, speculative for the general separation.

*Probed by T2 antipodal protocol, 2026-04-13.*
