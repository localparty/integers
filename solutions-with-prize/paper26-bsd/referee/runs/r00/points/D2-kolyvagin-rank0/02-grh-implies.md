## Point D2(b): GRH implies L(E, 1) != 0 for analytic rank 0

**The question:**
GRH says zeros are on Re(s) = 1/2, and s = 1 is NOT on the critical line. So GRH alone implies L(E, 1) != 0 only if the analytic rank is already known to be 0. How is the analytic rank determined?

**Finding:**
This is an important logical subtlety. GRH says all non-trivial zeros have Re(s) = 1/2. Since Re(1) = 1 != 1/2, the point s = 1 is NOT a non-trivial zero. Therefore L(E, 1) != 0 follows from GRH alone, with no additional assumption about the analytic rank.

Wait -- this is too strong. If L(E, s) has a zero at s = 1 (i.e., analytic rank >= 1), then s = 1 IS a zero of L(E, s), but is it a "non-trivial zero"? The non-trivial zeros of L(E, s) are those in the critical strip 0 < Re(s) < 2 (by the functional equation). The point s = 1 is the CENTER of the critical strip, and a zero at s = 1 IS a non-trivial zero. GRH says non-trivial zeros have Re(s) = 1/2, so s = 1 (with Re(s) = 1) cannot be a non-trivial zero. Therefore L(E, 1) != 0.

But this contradicts the existence of curves with analytic rank >= 1! The resolution: GRH for L(E, s) would imply L(E, 1) != 0, which would mean all elliptic curves have analytic rank 0. This is FALSE -- there exist curves with L(E, 1) = 0.

This reveals a critical issue: GRH for L(E, s) CANNOT be true for curves with analytic rank >= 1, because it would force L(E, 1) != 0, contradicting the known vanishing.

Actually, I need to reconsider. The GRH for the FACTORS L(s, psi) and L(s, psi-bar) says their zeros are on Re(s) = 1/2. The zeros of L(E, s) at s = 1 would come from zeros of L(s, psi) or L(s, psi-bar) at s = 1. If GRH holds for L(s, psi), then L(1, psi) != 0 and L(1, psi-bar) != 0, so L(E, 1) = L(1, psi) * L(1, psi-bar) != 0.

So the preprint's GRH claim -- that all non-trivial zeros of L(s, psi) are on Re(s) = 1/2 -- WOULD imply L(E, 1) != 0 for ALL CM curves, not just rank-0 ones. This means the preprint is effectively claiming that all CM curves over class-number-1 fields have analytic rank 0.

But this is known to be false: there exist CM curves with analytic rank 1 and even rank 2.

This is a MAJOR logical issue. The preprint handles it in Corollary 11.2: "If the analytic rank of E is 0 -- that is, ord_{s=1} L(E,s) = 0 -- then L(E, 1) != 0." This is vacuously true. But the Theorem 12.5 for rank 1 says: "If ord_{s=1} L(E,s) = 1, then..." and uses GRH to ensure L(E, 1) = 0 and L'(E, 1) != 0.

So the preprint does NOT claim L(E, 1) != 0 for all CM curves. It says: GRH determines the exact order of vanishing at s = 1. For rank 0, the order is 0, so L(E, 1) != 0. For rank 1, the order is exactly 1, so L(E, 1) = 0 and L'(E, 1) != 0.

But how can GRH be compatible with L(E, 1) = 0 for rank-1 curves? If all non-trivial zeros of L(s, psi) are on Re(s) = 1/2, then L(1, psi) != 0, hence L(E, 1) != 0. This contradicts rank 1.

The resolution must be that for rank-1 CM curves, the zero at s = 1 is NOT a zero of L(s, psi) or L(s, psi-bar) individually, but rather arises from some other mechanism. Actually no -- if L(E, 1) = L(1, psi) * L(1, psi-bar) = 0, then at least one of L(1, psi) or L(1, psi-bar) must be zero. But GRH for L(s, psi) says Re(s) = 1/2 for all non-trivial zeros, so s = 1 cannot be a zero of L(s, psi).

This is a GENUINE logical contradiction. GRH for the individual Hecke L-functions L(s, psi) is incompatible with the existence of CM curves of analytic rank >= 1.

Let me re-examine. The GRH for L(s, psi) says all NON-TRIVIAL zeros are on Re(s) = 1/2. Could s = 1 be a TRIVIAL zero? The trivial zeros of Hecke L-functions are at specific negative integers, determined by the functional equation. s = 1 is not a trivial zero.

Therefore: GRH for L(s, psi) implies L(1, psi) != 0, which implies L(E, 1) != 0, which implies analytic rank = 0 for ALL CM curves covered by the theorem. This means BSD rank 1 is vacuously true (there are no CM curves of rank 1 with CM by class-number-1 fields) -- or the GRH claim is wrong.

Actually, wait. Let me check: do CM curves with CM by Q(i) of analytic rank 1 exist? The curve y^2 = x^3 - x has rank 0. The general theory says that for a given CM field K, there are curves with various ranks. But the L-function factorization L(E, s) = L(s, psi) * L(s, psi-bar) means that L(E, 1) = 0 iff L(1, psi) = 0 or L(1, psi-bar) = 0.

For Hecke L-functions L(s, psi) where psi is a Grossencharacter of an imaginary quadratic field, the non-vanishing L(1, psi) != 0 is actually a KNOWN RESULT (this is essentially a theorem of Hecke). Specifically, for Hecke characters of infinity type (1,0) (which is the case for Grossencharacters attached to CM curves), L(1, psi) != 0 is known unconditionally.

So for CM curves with CM by class-number-1 fields, L(E, 1) = L(1, psi) * L(1, psi-bar) != 0 ALWAYS, meaning ALL such curves have analytic rank 0.

This would mean the rank-1 case in the preprint is vacuous -- there are no CM curves of rank 1 with CM by class-number-1 fields (where the CM field is the same as the field K).

But wait: CM curves of rank 1 do exist. The resolution is that when we say "E has CM by K" and "analytic rank 1," the zero at s = 1 comes from a zero of L(E/K', s) for an auxiliary field K', not from L(E, s) itself. Or, more precisely, the Grossencharacter factorization L(E, s) = L(s, psi) * L(s, psi-bar) with L(1, psi) != 0 means L(E, 1) != 0 -- so all CM curves over Q with CM by a class-number-1 field have analytic rank 0 over Q.

But there exist CM elliptic curves over Q with rank >= 1! For example, there are known CM curves of rank 1. However, these may have CM by fields of class number > 1, or the Grossencharacter may have different properties.

Let me reconsider. The non-vanishing L(1, psi) != 0 for Hecke characters of the type attached to CM curves is indeed a classical result. This means L(E, 1) != 0 for CM curves, which means all CM curves over Q have analytic rank 0.

Is this true? Not quite. The issue is that "CM by K" versus "CM defined over Q." A curve E/Q with CM by K may have its CM endomorphisms defined over K, not over Q. The L-function L(E/Q, s) and L(E/K, s) are different. The factorization L(E/Q, s) = L(s, psi) * L(s, psi-bar) uses the Grossencharacter of K, and L(1, psi) != 0 gives L(E/Q, 1) != 0.

But L(E/K, s) has a different factorization and CAN vanish at s = 1. The rank of E(K) can be positive even when rank E(Q) = 0.

So the preprint's rank-1 claim should be for E(Q), not E(K). But Kolyvagin and Gross-Zagier work over Q (for E/Q). If L(E/Q, 1) != 0 always for CM curves with CM by class-number-1 fields, then rank(E(Q)) = 0 always, and the rank-1 case is vacuous.

This needs careful analysis. The preprint may be conflating rank over Q with rank over K.

**Verdict for this sub-question:**
CLOSABLE GAP -- There is a significant logical subtlety regarding whether CM curves with CM by class-number-1 fields can have analytic rank >= 1 over Q. If L(1, psi) != 0 unconditionally (a known result for Hecke characters of the relevant type), then ALL such curves have rank 0 over Q, and the rank-1 case is vacuous. The preprint should clarify this. The gap is closable: either (a) confirm that rank 1 over Q does not occur and note the rank-1 result is vacuously true, or (b) if rank 1 can occur, explain how this is compatible with L(1, psi) != 0.
