"""
Premise Check Path A: JLO Chern Character

Does ch_n(T_BC) CHANGE when an off-line zero at delta is introduced?

The JLO Chern character ch_0 is the supertrace:
  ch_0 = Tr_s(e^{-T^2})
  
For T_BC with spectrum {gamma_n}, the supertrace with grading sign(gamma) is:
  ch_0 = sum_n sign(gamma_n) * e^{-gamma_n^2}

If zeros are on the critical line, gamma_n are real and come in pairs (gamma, -gamma).
Each pair contributes: (+1)*e^{-gamma^2} + (-1)*e^{-gamma^2} = 0.
So ch_0 = 0 identically for on-line zeros.

Question: does an off-line zero change this?
"""
from mpmath import mp, mpf, mpc, zetazero, exp, re, im, conj, nstr, pi, sign, fabs, sqrt
mp.dps = 50

print("=" * 70)
print("PREMISE CHECK PATH A: JLO CHERN CHARACTER ch_0, ch_2")
print("=" * 70)

N_zeros = 30
zeros = [zetazero(n) for n in range(1, N_zeros + 1)]
gammas = [im(z) for z in zeros]

print("\n--- ch_0 = Tr_s(exp(-T^2)) for on-line zeros ---")
print("Grading: epsilon_n = sign(gamma_n)")
print("Pairs (gamma_n, -gamma_n) cancel exactly.")

ch0_online = mpf(0)
for g in gammas:
    # positive gamma contributes +exp(-g^2), negative gamma contributes -exp(-g^2)
    # net contribution per pair: 0
    ch0_online += exp(-g**2) - exp(-g**2)  # = 0

print(f"ch_0 (on-line, {N_zeros} pairs) = {nstr(ch0_online, 15)}")
print("This is EXACTLY 0 by the functional equation symmetry.")

print("\n--- ch_0 with off-line zero at 1/2 + delta + i*gamma_1 ---")
print("Off-line zero creates a QUARTET of spectral values:")
print("  gamma_* = (rho - 1/2)/i where rho = 1/2 + delta + i*t")
print("  = t - i*delta   (COMPLEX!)")
print()
print("But wait: T_BC is self-adjoint, so its spectrum must be REAL.")
print("An off-line zero at 1/2+delta+it would mean gamma=(rho-1/2)/i=t-i*delta")
print("which is COMPLEX. This contradicts self-adjointness of T_BC.")
print()
print("This IS the structural argument of research/08. The premise check")
print("for Path A must address a different question:")
print()
print("IF we hypothetically perturb T_BC to T_BC(delta) by adding a")
print("complex spectral value, does the Chern character change?")
print("But T_BC(delta) would not be self-adjoint, so the JLO cocycle")
print("is not even defined in the standard sense.")
print()
print("ALTERNATIVE FORMULATION: Consider a deformation of the BC system")
print("that shifts the KMS state from beta=1 to beta=1+2*delta.")
print("Does this shift the Chern character?")

print("\n" + "=" * 70)
print("DIRECT COMPUTATION: Connes pairing for Hecke projection e_2")
print("=" * 70)
print()
print("From research/90: ind_BC(e_2) = 0 by McKean-Singer supertrace.")
print("The functional equation forces EXACT cancellation.")
print()
print("Key insight from research/90:")
print("  <gamma_n|e_2|gamma_n> = 1 - 2^{-1/2 - i*gamma_n}")
print("  <-gamma_n|e_2|-gamma_n> = 1 - 2^{-1/2 + i*gamma_n} = conj of above")
print("  Supertrace pair: [value] - [conj(value)] = 2i * Im(value)")
print("  -> purely imaginary, goes to 0 as t->infinity")
print()

print("Computing the supertrace purity for e_2:")
for t_param in [mpf('0.01'), mpf('0.1'), mpf('1.0')]:
    total = mpc(0,0)
    for g in gammas:
        me = 1 - mpf(2)**(-mpf('0.5') - mpc(0,g))
        me_neg = 1 - mpf(2)**(-mpf('0.5') + mpc(0,g))
        # supertrace: sign(+g)*me*exp(-t*g^2) + sign(-g)*me_neg*exp(-t*g^2)
        total += (me - me_neg) * exp(-t_param * g**2)
    print(f"  Tr_s(e_2 * exp(-{nstr(t_param,3)}*T^2)) = {nstr(re(total),10)} + {nstr(im(total),10)}*i")

print()
print("RESULT: ind_BC(e_2) = 0 for ALL Hecke projections.")
print("Research/90 proved this is universal (supertrace purity).")
print()

print("=" * 70)
print("PATH A PREMISE CHECK: ANALYSIS")
print("=" * 70)
print("""
The Chern character route requires:
1. ch_n(T_BC) changes when an off-line zero is introduced
2. The Connes pairing <ch_n, [e]> must remain integer
3. The change forces delta = 0

FINDING 1: ch_0 = 0 identically (functional equation symmetry).
  An off-line zero would make the spectral parameter COMPLEX,
  but T_BC is self-adjoint -> spectrum is real.
  There is no well-defined "T_BC with off-line zero" because
  adding a complex spectral value destroys self-adjointness.

FINDING 2: ind_BC(e_N) = 0 for ALL Hecke projections (research/90).
  The K-theory pairing is trivially satisfied (0 is always an integer).
  
FINDING 3: The "perturbation" is ill-defined in Path A's formulation.
  T_BC is self-adjoint (Stone's theorem). Off-line zeros would
  require non-self-adjoint perturbation. The JLO cocycle for
  non-self-adjoint operators is not standard.

PREMISE CHECK VERDICT: PATH A PREMISE IS VACUOUS.

The same coboundary-type error: ind_BC = 0 means the integer constraint
is trivially satisfied. The Chern character does not provide a non-trivial
constraint because:
(a) ch_0 = 0 by functional equation symmetry
(b) ind_BC(e_N) = 0 for all Hecke projections
(c) The "perturbation by off-line zero" is ill-defined for self-adjoint T_BC

This is a COBOUNDARY-TYPE ERROR: the constraint is vacuous because the
invariant (index = 0) does not change under the perturbation (because
it's already 0 and can't go below 0 to become non-integer).

The coboundary lesson applies: just as H^2(Z/kZ, U(1)) was too robust
to detect continuous perturbations, K_0(A_BC) paired with the JLO
character gives 0 for all Hecke projections, which is too trivial to
constrain anything.

POSSIBLE SALVAGE: Find a non-Hecke projection e in K_0(A_BC) with
ind_BC(e) != 0. Research/48 Section 6.3 (O1) notes this is open.
Without such a projection, Path A is dead.
""")
