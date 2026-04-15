# Lead #2 — L=3 Epstein factorization search (Agent B)

**Date:** 2026-04-14
**Agent:** B (parallel with A, C)
**Precision:** mpmath `mp.dps = 50`, extended to 80 for PSLQ
**Lattice:** A_3 / D_3 / SU(4) root lattice
**Form:** Q_3(n) = n_1^2 + n_2^2 + n_3^2 + n_1 n_2 + n_1 n_3 + n_2 n_3

## Hypothesis under test

`E_3(s; Q_3)` factors into standard L-functions (analogously to
`E_2(s; Q_2) = 6 · zeta(s) · L(s, chi_{-3})` on A_2),
producing zeta(3) at some weight and explaining Pin #6
(J_CKM x 10^5 = log(gamma_1) * zeta(3)) structurally.

## Bottom line

**NEGATIVE.** No multiplicative factorization of E_3(s; Q_3) into
standard L-function pieces exists in the space searched.

- PSLQ with maxcoeff = 10^14, tol = 10^-50 finds no integer relation
  among E_3(3; Q_3), zeta(3), L(3, chi_-3), L(3, chi_-4), L(3, chi_-8),
  or any ζ(3)·L(3, chi) products.
- E_3(3)/12 = 1.20449... is close to zeta(3) = 1.20206... (gap 0.00244,
  0.2%) but fails PSLQ cleanly — coincidence, not identity.
- L=2 factorization "6·zeta(s)·L(s, chi_-3)" verified to 14 digits at
  s=4 (sanity check passes); no analogue at L=3.
- Consistent with lattice-theoretic expectation: A_3 is not a
  biquadratic lattice (Weyl group S_4, not a Galois group of an
  imaginary-quadratic field). A_2 and D_4 are the small exceptions.

## Numerical content (mp.dps = 50)

### Special values of E_3(s; Q_3)

| s    | E_3(s; Q_3) |
|:----:|:-----------|
| 2    | 25.3383043051301683149392016815 |
| 3    | 14.4539210437444718628208366681 |
| 4    | 12.8019372313781325557931846985 |
| 5    | 12.3112456654774057913821580947 |
| 6    | 12.1318801965445797082619464105 |
| 5/2  | 16.9675184583784057360841 |
| 7/2  | 13.3593877007420840426503 |
| 9/2  | 12.4925467021375581431566 |
| 1/2  | -3.24198706341088839428369 |
| -1/2 | -0.22945882512436814641792 |

Direct-summation sanity at s=3: Mellin vs. direct (N=40) agrees to
1e-5 (tail on direct side; Mellin is the high-precision reference).

### L=2 sanity (machine check)

E_2(s; Q_2) = 6·zeta(s)·L(s, chi_-3) verified:

| s   | rel. err |
|:---:|:--------|
| 2   | 1.2e-5 (direct-sum truncation on E_2 side) |
| 5/2 | 4.6e-8 |
| 3   | 1.6e-10 |
| 4   | 1.8e-14 |

Confirms PSLQ machinery sound.

### PSLQ at s = 3 — all return None

- {E_3(3), zeta(3)·L(3,chi_-3)} maxcoeff 10^14 → None
- {E_3(3), zeta(3), L(3,chi_-3), L(3,chi_-4)} maxcoeff 10^10 → None
- {E_3(3), zeta(3), zeta(3)·L(3,chi) for chi in {-3,-4,-7,-8,-11}}
  maxcoeff 10^10 → None
- 13-element basis with L^2, log·zeta terms at maxcoeff 10^12 → None

The only relations PSLQ returned at all were Euler tautologies
(pi^3 = 6·pi·zeta(2); pi^4 = 90·zeta(4)); none involved E_3.

### Pin #6 comparison

- gamma_1 = 14.1347251417346937904...
- log(gamma_1) = 2.6486345457307902...
- zeta(3) = 1.2020569031595942854...
- log(gamma_1)·zeta(3) = **3.183809439642672496...**
- J_CKM x 10^5 measured = 3.18 (matches to 0.12%)

log(gamma_1)·zeta(3) does not equal any E_3(s; Q_3) special value or
simple rational multiple thereof. PSLQ on {pin6, E_3(2), E_3(3),
E_3(5/2), E_3(7/2)} maxcoeff 10^10 returns None.

**Pin #6 stays at FIT status from this lead.** The zeta(3) factor
in Pin #6 is a canonical 3-loop QFT signature (e.g., massless-QED
beta-function weight-3 transcendental), but the L=3 lattice Epstein
does not produce it. A different derivation route is needed if
Pin #6 is to be upgraded to THEOREM — most plausibly a direct BPHZ
evaluation of the 4D Mercedes-diagram momentum integral, where
zeta(3) arises diagrammatically and log(gamma_1) separately from
the CBB/RH bridge (Paper 13, Paper 26 Step 4).

## Residue at s = 3/2 — correction to PROOF-CHAIN

Numerically extracted: 8.8857658763167324940317...

PROOF-CHAIN.md §E.3 and line 350 read this as `2·sqrt(2·pi)` ~ 5.0133.

But 2·sqrt(2·pi) = 5.013256549262... does **not** match the numerical
residue 8.886.

The correct expression is:

    Res_{s=3/2} E_3(s; Q_3) = pi^(3/2) / [Gamma(3/2) · sqrt(det(A_3))]
                            = pi^(3/2) · sqrt(2) · (2/sqrt(pi))
                            = 2·sqrt(2)·pi
                            = 8.8857658763167324940317...  ✔

The PROOF-CHAIN notation "2·sqrt(2·pi)" is ambiguous; it should be
"2·sqrt(2)·pi" or equivalently "2·pi·sqrt(2)". The numerical value in
Paper 1 Resolution B (8.885765876316732494) is correct; only the
surface symbolic notation needs editing.

## Agent A follow-up: affine Â_3 and the number 17

Agent A's reading `rank + |roots| + 1 = 4 + 12 + 1 = 17` requires
rank = 4, which is the rank of the **affine** Â_3 (4 Dynkin nodes for
Â_3 = affine SU(4)). Finite rank A_3 gives 3 + 12 + 1 = 16, hence
Agent A's formula is specifically the affine reading.

In E_3 numerics, divisor 17 does not produce a clean special value:
E_3(3)/17 = 0.85023... (no recognizable constant).
E_3(3)/12 = 1.20449... ~ zeta(3) (gap 0.2%, fails PSLQ).
E_3(3)/24 = 0.6022... (24 = |W(A_3)|, no match).

**Conclusion on Â_3**: Agent A's `17 = rank(Â_3) + |roots(A_3)| + 1`
reading is combinatorially clean and internally consistent, but the
L=3 Epstein does not add corroboration. Pin #9 (alpha_PS^-1 = 17)
stands or falls on representation theory of the Pati-Salam
embedding in Â_3, not on E_3 special values.

## What's salvageable

1. **Residue notation fix**: PROOF-CHAIN line 350 + §E.3 should read
   `2·sqrt(2)·pi` (or `2·pi·sqrt(2)`) not `2·sqrt(2·pi)`. Editorial,
   but necessary for clarity.

2. **Lead #2 verdict**: NEGATIVE at tested precision. The structural
   derivation of Pin #6 does not go through A_3 Epstein factorization.
   Proposed alternative route: compute the 4D Mercedes momentum
   integral in BPHZ, show transcendental weight = zeta(3), separately
   derive log(gamma_1) prefactor from Paper 13 CBB/RH bridge,
   combine at Paper 26 Step 4 vertex.

3. **Machinery confirmed**: Mellin/Terras implementation from
   Route-C is reliable. Template usable for future E_L(s; Q) factor
   searches on other lattices.

## Files

- `e3_factor_search.py` — main search: L=2 sanity, L=3 specials,
  ratio probes, PSLQ at s=3, Pin #6 check, Â_3 probe.
- `e3_deep_probe.py` — extended 10-element PSLQ basis at s=2,3,4
  plus cubic-lattice comparison.
- `e3_ambitious_pslq.py` — maxcoeff sweep 10^4..10^14 + brute-force
  integer-combo search.
- `e3_special_values.json` — numerics from factor_search.
- `e3_deep_probe.json` — numerics from deep_probe.
- `run_output.txt`, `deep_probe_output.txt`, `ambitious_pslq_output.txt`
  — captured stdout.

## Confidence

9/10 that no multiplicative factorization of E_3(s; Q_3) exists in
the small-conductor Dirichlet-L space with integer coefficients
|c| <= 10^14. Consistent with A_3 not being biquadratic.
1/10 residual covers (i) degree-2 automorphic / Hecke Grossencharacter
L-functions on imaginary cubic CM fields not searched, (ii) identities
involving transcendentals beyond {zeta, L, pi, log k}.
