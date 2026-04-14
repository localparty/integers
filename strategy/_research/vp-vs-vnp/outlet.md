# VP vs VNP (Valiant's Conjecture / Permanent vs Determinant) — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity
- **Original formulation:** Valiant, L. G. (1979). "Completeness classes in algebra." *Proc. 11th ACM STOC*, 249–261.
- **Nonuniform algebraic P vs NP:** Bürgisser, P. (2000). *Completeness and Reduction in Algebraic Complexity Theory*. Algorithms and Computation in Mathematics 7, Springer.
- **GCT program:** https://www.cs.uchicago.edu/~mulmuley/gct/ — Mulmuley's Geometric Complexity Theory program.

## 2. Problem statement

**VP vs VNP (Valiant's conjecture):**
> VP ≠ VNP over any field K of characteristic 0 (most commonly, over ℂ).

Where:
- **VP** = families (f_n)_{n ∈ ℕ} of polynomials over K with deg(f_n), circuit-size(f_n), and number of variables n(f_n) all polynomially bounded in n.
- **VNP** = Valiant's algebraic NP: families (f_n) where f_n is the sum over 0/1-assignments of a VP-computable polynomial.

**Equivalent form (permanent vs determinant):** The permanent polynomial PER_n(X) (over n² variables) is VNP-complete. Its *determinantal complexity* dc(PER_n) is the smallest m such that PER_n can be expressed as DET_m(A(X)) for some affine A in the entries of X. Conjecturally, dc(PER_n) grows super-polynomially in n. Current best lower bound: dc(PER_n) ≥ n²/2 (Mignon-Ressayre 2004).

## 3. Prize

**None.** No monetary prize. Sometimes informally described as "the algebraic P vs NP" — a Clay Millennium problem in spirit but not on the Clay list.

Note: Even a separation of VP and VNP over ℂ would NOT directly resolve Clay's P vs NP, since P vs NP is over a Turing-machine (Boolean) model, not the Valiant algebraic model. However, VP = VNP would imply P/poly ⊇ NC in characteristic 0, which many believe would be a precursor/implication toward P vs NP separation under plausible hypotheses.

## 4. Publication expectation

Expected journals in descending prestige:

- **Journal of the ACM (JACM)** — Mulmuley's 2011 GCT overview published here.
- **SIAM Journal on Computing (SICOMP)** — GCT-I (Mulmuley-Sohoni 2001) published here.
- **Communications of the ACM (CACM)** — high-profile surveys.
- **Annals of Mathematics** — for a full proof using deep representation theory / algebraic geometry.
- **Inventiones Mathematicae**
- **JAMS**
- **Computational Complexity** (Birkhäuser)
- **Theory of Computing** (open-access, reputable).
- **Journal of Computer and System Sciences (JCSS)**
- **Theoretical Computer Science**

Conferences (conference proceedings here are competitive with journals in CS):
- **STOC** (ACM Symposium on Theory of Computing)
- **FOCS** (IEEE Foundations of Computer Science)
- **CCC** (Computational Complexity Conference) — specialty venue.
- **ICALP**
- **SODA**

## 5. Formulation variants

- **VP vs VNP (over ℂ):** standard.
- **VP vs VNP (over finite field):** changes character; some cases easier or harder.
- **VP ≠ VNP under reductions:** strict non-containment.
- **Permanent vs Determinant:** super-polynomial lower bound on dc(PER_n).
- **VNP vs VP^0 (constant-free):** Valiant's original form used constant-free circuits.
- **Algebraic branching program lower bounds:** weakened analogs.
- **Border complexity / approximative closures (VP̄):** with approximation, the conjecture becomes VP̄ ≠ VNP̄; GCT approach targets this.
- **Tensor rank lower bounds:** related; matrix multiplication tensor.

## 6. Known partial results + named walls

**Proven:**
- **dc(PER_n) ≥ n²/2** (Mignon-Ressayre 2004, *Int. Math. Res. Notices*). Over ℂ.
- Characteristic-p versions: Cai-Chen-Li (*JACM* 2010) — quadratic lower bound in any characteristic.
- **No Occurrence Obstructions (2016):** Bürgisser, Ikenmeyer, Panova showed that the original GCT strategy of using multiplicities of irreducible representations in plethysms cannot separate orbit closures. Published: *JAMS* 2019.
- **VP ⊂ VNP** trivially.
- **Strassen's degree bound**, Baur-Strassen method: lower bounds of form Ω(n log n) for general polynomials.

**Named walls:**
- *Natural proofs barrier (algebraic version)* — Aaronson-Drucker and others identified that many lower-bound techniques can't separate VP from VNP without evading natural-proofs-style obstacles.
- *Algebraic relativization / geometric complexity wall* — generic approaches relativize; GCT aimed to transcend this via representation theory.
- *No-go for occurrence obstructions* — the 2016 Bürgisser-Ikenmeyer-Panova result showed the original GCT program cannot work as initially conceived.
- *GCT redirection wall* — since 2016, GCT program has pivoted to multiplicity obstructions + positivity, but no proof yet.
- *Shallow circuits wall* — depth-3 / depth-4 arithmetic circuit lower bounds are themselves open and barely superlinear.

## 7. Key references

**Original:**
- Valiant, L. G. (1979). "Completeness classes in algebra." *Proc. 11th ACM STOC*, 249–261.
- Valiant, L. G. (1979). "The complexity of computing the permanent." *Theoretical Computer Science* 8, 189–201.

**Best modern surveys:**
- Bürgisser, P. (2000). *Completeness and Reduction in Algebraic Complexity Theory*. Springer.
- Bürgisser, P., Clausen, M., Shokrollahi, M. A. (1997). *Algebraic Complexity Theory*. Grundlehren der math. Wissenschaften 315, Springer.
- Mulmuley, K. D. (2011). "On P vs. NP and geometric complexity theory." *JACM* 58(2).
- Landsberg, J. M. (2017). *Geometry and Complexity Theory*. Cambridge.

**Key GCT papers:**
- Mulmuley, K. & Sohoni, M. (2001). "Geometric complexity theory I: An approach to the P vs NP and related problems." *SICOMP* 31, 496–526.
- Bürgisser, P., Ikenmeyer, C., Panova, G. (2019). "No occurrence obstructions in geometric complexity theory." *JAMS* 32, 163–193.

## Status: OPEN. No monetary prize. Target journal: Annals / JAMS / JACM / Inventiones.
