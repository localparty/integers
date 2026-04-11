## Point C1(d): The Formal Kill

**The question:**
Is the "integrality of the spectral shift" rigorously proved? The argument claims that if delta != 0, the bridge cocycles at two primes impose constraints that Baker shows are simultaneously unsatisfiable.

**Finding:**
The integrality constraint comes from the bridge cocycle structure: the Hasse invariant of the cyclic algebra (K(zeta_N)/K, Frob_p, zeta_k) takes values in (1/k)Z/Z. If a zero of zeta_K at s = 1/2 + delta shifts the effective Euler factor, the shifted Hasse invariant must still be in (1/k)Z (because the Brauer group of Q/Z has no other allowed values for cyclic algebras of degree k).

This integrality constraint is a consequence of the Brauer group structure and is rigorous. The question is whether the shift in the Hasse invariant is correctly computed.

The cocycle shift formula (Proposition 7.1) gives the change in the effective Euler factor ratio. The identification of this ratio with a shift in the Hasse invariant is the key claim. In the preprint, this identification comes from the relationship between the KMS state evaluation and the Euler factor: the shifted state omega_{1+2delta} evaluates the Hecke operator e_p as N(p)^{-(1+2delta)}, and this shifts the local partition function, which in turn shifts the cocycle.

The logic is: off-line zero -> shifted effective temperature -> shifted Euler factor -> shifted cocycle -> integrality constraint -> Baker contradiction -> delta = 0.

Each step in this chain is individually plausible, but the connection between "shifted Euler factor" and "shifted Hasse invariant" needs explicit justification. The Hasse invariant is a cohomological invariant (an element of H^2), not directly an Euler factor. The preprint does not fully spell out why a shift in the Euler factor translates to a shift in the Hasse invariant.

This is the same structural question as in the RH proof (Paper 13). If that proof is accepted, the same connection holds here (the argument is field-independent by Theorem 4.6).

**Verdict for this sub-question:**
CLOSABLE GAP -- The integrality constraint from the Brauer group is rigorous. The connection between Euler factor shift and Hasse invariant shift is the core mechanism of the bridge family and is inherited from the RH proof. If the RH proof mechanism is accepted, this step follows. The gap is in the explicit justification of this connection, estimated at 1-2 pages.
