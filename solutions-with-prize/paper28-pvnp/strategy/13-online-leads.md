# Online Leads (2024-04-11)

## Most promising finds

**1. Nordh-Jonsson-Lagerkvist (SODA 2013): Clone theory meets ETH directly.**
They prove a partial order on NP-complete SAT(S) problems via clone inclusions,
and show ETH holds iff the *easiest* NP-complete SAT problem is not sub-exponential.
This is the closest existing work to our CSP-operator-algebra bridge: clones already
govern exponential vs sub-exponential time, not just P vs NP.
Source: <https://gustavnordh.com/soda2013.pdf>

**2. Chakraborty (arXiv 2312.04702, updated 2024): Smallest Out for type III_1.**
Constructs a full III_1 factor whose Out(M) = R (the canonical modular image).
Uses amalgamated free product. Key insight: fullness forces Out to be *at least* R;
this factor shows equality is achievable. Confirms that non-fullness is the
*only* mechanism producing non-discrete Out beyond the modular flow.
Source: <https://arxiv.org/abs/2312.04702>

**3. Chifan-Ioana et al. (Duke, 2023/2025): Wreath-like products realize any countable Out.**
For every countable Q, there is a property (T) ICC group G with Out(L(G)) = Q.
This is the rigidity side: with enough rigidity, Out is fully controlled.
Our argument needs the *opposite* -- lack of Taylor term means lack of rigidity,
hence uncontrolled Out. Their machinery (spectral gap + property (T)) is exactly
what fails for non-Taylor clones.
Source: <https://arxiv.org/abs/2304.07457>

**4. Marrakchi (Crelle, 2019): Spectral gap characterizes fullness for type III.**
Full factor iff the bimodule L^2(M) ominus C has spectral gap. This is the
precise "if" direction we need: no spectral gap => not full => Inn not closed =>
Out(M) non-discrete. Already in our pipeline but confirms no newer replacement exists.
Source: <https://arxiv.org/abs/1605.09613>

**5. Clone growth: Boolean = countable, |domain| >= 3 = continuum (Janov-Mucnik 1959).**
Post's lattice has countably many clones. For 3+ elements, continuum many.
This is consistent with our construction but the exponential-vs-polynomial
*function growth* within a clone (not number of clones) is the operative quantity.

## Does any of this shorten the 5-step path?

No single result bypasses the pigeonhole. The closest candidate is Nordh et al.,
which already links clone structure to exponential time, but on the *complexity*
side, not the *operator algebra* side. Our bridge (clone -> polymorphism growth ->
spectral gap -> fullness -> Out) remains necessary. However, Chakraborty's
result strengthens step 5: non-fullness is now confirmed as the *only* route
to non-discrete Out for type III_1 factors, eliminating alternative explanations.

## No prior CSP-to-operator-algebra connection found.

Nobody appears to have connected CSPs to von Neumann algebras before.
