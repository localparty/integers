# T8 Chord Edge Fills — New Cross-Vertex Cells

*Compositional and direct chord edges involving the 3 new vertices + high-value existing-vertex pairs.*

---

## 1. Lindelöf ↔ Cramér — **STRONG**

**Domain pair**: SPEC×ANT ↔ PROB×ANT (use: SPEC×PROB)

**Statement**: Lindelöf's amplitude bound |ζ(1/2+it)| = O(t^ε) IS the missing error-bound control in Cramér's explicit-formula approach. The explicit formula for ψ(x) − ψ(x−h) has error controlled by Σ_{|γ|≤T} x^{−1/2} |ζ'(ρ)|^{−1}. Under RH + Lindelöf: error is O(x^{1/2+ε}) → prime gaps O(x^{1/2+ε}). This is weaker than full Cramér (O(log²x)) but stronger than unconditional (O(x^{0.525})).

**Status**: STRONG. The connection is classical and direct. Lindelöf is the FIRST STEP of the RH→Cramér shortcut.

**Load-bearing for**: Cramér L4 (error-term control); gap-distribution arc propagation.

---

## 2. Katz-Sarnak ↔ Sato-Tate — **ESTABLISHED**

**Domain pair**: ANT×PROB ↔ ANT×PROB (same-domain; use secondary: REP×PROB)

**Statement**: Sato-Tate equidistribution for individual curves IS the unitary/orthogonal case of Katz-Sarnak for the full family. ST says: for a SINGLE curve E, the Frobenius angles equidistribute. KS says: for the FAMILY of all curves of a given type, the zero statistics follow the corresponding random matrix ensemble. ST is the individual-curve projection; KS is the family-level generalization. The symmetry type G determines both the ST measure (pushforward of Haar on G) and the KS spacing statistics.

**Status**: ESTABLISHED. The relationship is containment + generalization.

**Load-bearing for**: Sato-Tate L5 (generalized ST follows from generalized KS); Katz-Sarnak L4 (ST provides individual-curve verification of KS predictions).

---

## 3. Katz-Sarnak ↔ BSD — **PARTIAL**

**Domain pair**: ANT×PROB ↔ ANT×AG (use: PROB×AG)

**Statement**: The Katz-Sarnak symmetry type of the family of elliptic-curve L-functions determines the parity of the analytic rank. For the family of all elliptic curves ordered by height: symmetry type is O (orthogonal). The SO⁺/SO⁻ split (by sign of functional equation) determines even/odd analytic rank. BSD's rank formula L(E,1) = 0 ↔ rank ≥ 1 is the individual-curve shadow of the family-level KS parity constraint.

**Status**: PARTIAL. The family-level parity constraint is well-understood (Katz-Sarnak, Iwaniec-Luo-Sarnak). The individual-curve BSD formula is a different kind of statement (exact rank, not statistical parity). The connection is structural but not a direct implication.

**Load-bearing for**: BSD Step 10-11 (Kolyvagin/Gross-Zagier); KS L3 (elliptic curve one-level density).

---

## 4. Sato-Tate ↔ BSD — **STRONG**

**Domain pair**: ANT×PROB ↔ ANT×AG (use: PROB×AG)

**Statement**: The Frobenius angles θ_p ARE the L-function data. L(E,s) = ∏_p (1 − a_p p^{−s} + p^{1−2s})^{−1} with a_p = 2√p cos(θ_p). Sato-Tate equidistribution of {θ_p} is equivalent to saying the L-function's Euler product converges "democratically" over primes. For CM curves: the ITPFI factorization ω₁^K = ⊗_𝔭 ω₁^(𝔭) decomposes both the BSD local-global structure AND the Sato-Tate equidistribution into the same prime-by-prime factors.

**Status**: STRONG. Frobenius = L-function data is classical. The BC/ITPFI infrastructure is shared between BSD (Paper 26) and Sato-Tate (Paper 44).

**Load-bearing for**: Sato-Tate L4 (BC framing via BSD ITPFI); BSD Steps 8-9 (Deuring CM factorization uses Frobenius data).

---

## 5. Lindelöf ↔ BGS — **PARTIAL**

**Domain pair**: SPEC×ANT ↔ PROB×ERG (use: SPEC×PROB)

**Statement**: The moments of |ζ(1/2+it)| are the interface between Lindelöf (amplitude) and BGS (statistics). The GUE prediction: ∫₀ᵀ |ζ(1/2+it)|^{2k} dt ~ C_k T(log T)^{k²}. Lindelöf says each moment grows at most O(T^{1+ε}). The GUE prediction is COMPATIBLE with Lindelöf (since k² < 1+ε for each fixed k, asymptotically). BGS provides the SPECIFIC growth rate; Lindelöf provides the UPPER BOUND.

**Status**: PARTIAL. The moment connection is classical (Hardy-Littlewood, Keating-Snaith). The BGS-specific GUE prediction goes beyond what Lindelöf constrains.

**Load-bearing for**: Lindelöf L2 (moments equivalence); BGS L4-L6 (zero statistics via moment methods).

---

## 6. Lindelöf ↔ Sato-Tate — **CANDIDATE**

**Domain pair**: SPEC×ANT ↔ ANT×PROB (use: SPEC×PROB)

**Statement**: Two e-circle faces (AMPLITUDE and MEASURE). Lindelöf controls how loud the signal gets; Sato-Tate controls how the angles distribute. For CM curves: |L(1/2+it,ψ)| = O(t^ε) (Lindelöf for Hecke L-functions) is related to equidistribution of Frobenius angles (ST) via the explicit formula. The amplitude bound constrains the fluctuations of the Frobenius angle distribution.

**Status**: CANDIDATE. The conceptual connection exists (amplitude bounds constrain distributional fluctuations) but no explicit theorem links Lindelöf for Hecke L-functions to Sato-Tate equidistribution rates.

**Load-bearing for**: The e-circle face network; KS L5 sub-route 5a (moment extension to higher support).

---

## 7. Lindelöf ↔ Twin Primes — **CANDIDATE**

**Domain pair**: SPEC×ANT ↔ PROB×ANT (use: SPEC×PROB)

**Statement**: Lindelöf controls the explicit formula's error term, which controls prime density in short intervals. Better amplitude bounds → better control on π(x+h)−π(x) → tighter constraints on twin prime density. Under RH + Lindelöf: the error in the prime-counting function is O(x^{1/2+ε}), which gives π(x+h)−π(x) ~ h/log x for h ≫ x^{1/2+ε}. This doesn't prove twin primes but constrains the environment.

**Status**: CANDIDATE. The connection goes through Cramér (Lindelöf→Cramér→Twin Primes) rather than directly.

---

## Summary

| # | Edge | Status | New? |
|---|---|---|---|
| 1 | Lindelöf ↔ Cramér | STRONG | Yes |
| 2 | Katz-Sarnak ↔ Sato-Tate | ESTABLISHED | Yes |
| 3 | Katz-Sarnak ↔ BSD | PARTIAL | Yes |
| 4 | Sato-Tate ↔ BSD | STRONG | Yes |
| 5 | Lindelöf ↔ BGS | PARTIAL | Yes |
| 6 | Lindelöf ↔ Sato-Tate | CANDIDATE | Yes |
| 7 | Lindelöf ↔ Twin Primes | CANDIDATE | Yes |

**7 new chord cells filled.** Total net new cells this traversal: 7.
