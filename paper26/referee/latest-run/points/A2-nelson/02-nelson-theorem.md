## Point A2(b): Nelson's Theorem

**The question:**
Nelson's analytic vector theorem requires a specific set of conditions on the domain. Are these satisfied for T_{BC,K} on the GNS Hilbert space?

**Finding:**
Nelson's analytic vector theorem (Reed-Simon, Theorem X.39) states: if T is a symmetric operator on a Hilbert space H, and there exists a dense set of analytic vectors for T, then T is essentially self-adjoint.

The conditions needed:
1. T must be symmetric (formally self-adjoint on its domain).
2. The set of analytic vectors must be dense in H.

For condition 1: T_{BC,K} = log N(a) acting by multiplication is formally symmetric (it acts as multiplication by a real number on each component of the GNS decomposition).

For condition 2: The GNS vectors pi_1(mu_a) Omega_1 for all ideals a generate a dense subspace of H_{1,K}, because the Hecke operators mu_a generate the algebra A_{BC,K}. Each of these vectors is an entire analytic vector (sub-question (a)). Therefore the dense set of analytic vectors exists.

Both conditions are satisfied. The application of Nelson's theorem is correct.

**Verdict for this sub-question:**
SOUND -- Nelson's theorem is correctly applied. Both conditions (symmetry and dense analytic vectors) are verified.
