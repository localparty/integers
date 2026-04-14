# T9 Vertex 20: OPN — Construction pass on Route 6d

**Verdict: Route 6d CANNOT advance as a literal Hasse-principle argument.**
The framing is a category error; what survives is a rigidity statement.

## Construction attempt

**Target.** For odd n = p^alpha * m^2 (Euler form), show prod_{q|n} h(q^{v_q}) = 2
is impossible via local-global obstruction on the ITPFI factorization
omega_1 = tensor_p omega_1^(p).

**Step 1 — write the condition adelically.** Equality prod h(q^{v_q}) = 2 in Q
gives, after clearing: prod_q (q^{v_q+1} - 1) = 2 * prod_q q^{v_q}(q-1).
At each odd prime ell, this imposes v_ell of both sides match; at 2 likewise.

**Step 2 — local solvability is trivial.** At any single prime ell, the equation
has solutions (pick any v_ell and absorb the deficit into a spectator prime).
So "local points" exist everywhere — the setup looks ripe for Hasse.

**Step 3 — what fails.** A Hasse/Brauer-Manin obstruction requires a SCHEME
X/Q with X(A_Q) nonempty but X(Q) empty, detected by a Brauer class
alpha in Br(X). Here there is no scheme: the Diophantine locus
{(v_q) : prod h(q^{v_q}) = 2} is a discrete subset of a countable lattice
indexed by odd primes, not the Q-points of an algebraic variety. The
"adelic product" is a convergent real product, not a topological space of
adelic points with Brauer pairing.

**Step 4 — test the cocycle candidate anyway.** The BC Hecke semigroup N*
restricted to odd generators is free abelian on {3,5,7,...}. Its group
cohomology H^2(N*_odd, U(1)) = 0 (free abelian groups have trivial H^2
with divisible coefficients). The ITPFI factors omega_1^(p) are type III_{1/p}
on isolated primes; their tensor product is type III_1 with trivial flow
of weights cocycle over the odd-restricted subsystem. **No cocycle exists.**

**Step 5 — the Galois escape hatch closes too.** One might hope Gal(Q^ab/Q) =
Zhat^* acting on KMS_1 produces an obstruction for the odd-restricted state.
But the Bost-Connes Galois action permutes extremal KMS_beta states for
beta > 1; at beta = 1 the state is unique and Galois-invariant. There is no
nontrivial Galois cocycle to harvest at criticality.

## What the ITPFI framing actually buys

Not a Hasse obstruction, but a **rigidity restatement**: prod h(q^v) = 2 is
a resonance of local KMS_1 data on a tensor-factorizable state. The ITPFI
structure recovers classical multiplicativity of sigma; it does not add
arithmetic constraint. The spoof phenomenon (Descartes, Nielsen-21) shows
the constraint IS tight — composite-indexed products hit 2 easily, prime-
indexed ones apparently cannot — but this tightness is empirical, not
cohomological.

## Recommendation for T9

Close Route 6d as **DECOMPOSED**: the Hasse framing was heuristically
suggestive but structurally void. Productive residue: (i) the rigidity
restatement feeds Route 6a's analytic bound by justifying why per-prime
sieving is the right technique; (ii) spoofs as "local solutions" motivate
studying composite-to-prime-index reduction maps on the Hecke semigroup,
which may connect to Paper 37 (ABC rad-bounds) rather than Paper 13 (RH).

Route 6a (odd Robin, halved Mertens e^gamma/2) remains the only live path.

**Confidence: 3/10 (down from 4/10).** The surviving route is narrower than
the PROOF-CHAIN reflects; update recommended.
