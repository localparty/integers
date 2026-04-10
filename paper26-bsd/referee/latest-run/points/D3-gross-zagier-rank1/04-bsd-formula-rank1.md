## Point D3(d): The BSD Formula at Rank 1

**The question:**
Are all terms of the BSD leading coefficient formula computed for rank 1?

**Finding:**
The rank-1 BSD formula is:
L'(E, 1) = (|Sha| * Omega * R * prod c_p) / |E(Q)_tors|^2

where R = h-hat(P) is the regulator (Neron-Tate height of a generator).

The preprint (Section 12.4) states: "The Gross-Zagier formula itself provides the bridge between L'(E, 1) and h-hat(P_K), and Kolyvagin's finiteness of Sha closes the formula."

This is correct in principle: the Gross-Zagier formula gives L'(E, 1) in terms of h-hat(P_K), and once all other BSD quantities are computed, the formula is verified. However, the preprint does not provide an explicit numerical verification for a rank-1 CM curve (unlike the detailed verification for the rank-0 curve in Section 13.3).

Section 14.3 mentions "A rank-1 CM curve" and sketches the verification, but the treatment is brief and does not give all numerical values.

**Verdict for this sub-question:**
CLOSABLE GAP -- The rank-1 BSD formula is correctly described but not numerically verified for a specific curve. A concrete example with all terms computed would strengthen the paper.
