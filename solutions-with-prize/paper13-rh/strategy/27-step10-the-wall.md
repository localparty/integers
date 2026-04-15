# Strategy 27 — Step 10: The Wall

*The Cartwright core (Steps 1-7) is PROVED. The induction (Step 8)*
*works at each finite N. The limit (Step 10) is the wall.*

*"Simple at every finite N ≠ simple in the limit."*

*Date: 2026-04-10*

---

## 1. What survives (definitively)

Steps 1-7: PROVED. The adversarial confirmed twice.
- Paley-Wiener: entire of type λ ✓
- Cosine injectivity on L²(0,∞): classical ✓
- Cartwright-Levin: finitely many zeros ✓
- Levin constant uniform in N ✓
- PNT density infinite ✓

Step 8 (secular induction): SOUND at each finite N.

## 2. The wall: Step 10

**"Simple at every finite N does not imply simple in the limit."**

Counter-example: μ_k^N = k/N (simple for each N, continuous limit).

The induction guarantees simplicity at each step but not that
the gaps between eigenvalues stay bounded below.

**What's needed:** A UNIFORM LOWER BOUND on eigenvalue gaps:
|μ_k^N − μ_{k+1}^N| ≥ δ(k) > 0, independent of N.

This requires a new ingredient — not Cartwright, not secular
equations, not Paley-Wiener. Something ARITHMETIC that controls
how close eigenvalues of the Weil quadratic form can get.

## 3. What the programme has achieved

Even without closing Step 10:

1. **RH at each fixed N** (number of primes): the Cartwright
   chain is complete. The Weil quadratic form with finitely
   many Euler factors has simple minimum eigenvalue.

2. **The Cartwright mechanism** is a genuinely new observation:
   eigenfunctions of the Weil form are compactly supported →
   their overlaps with prime vectors are values of entire
   functions → Cartwright limits the zeros.

3. **The CCM+ITPFI connection** identifies the modular
   Hamiltonian with the scaling operator and the state
   convergence with the Euler product.

4. **19 kills + 48 research notes** map the landscape of
   dead ends more thoroughly than any previous programme.

## 4. The open problem (precisely stated)

> **Eigenvalue Gap Problem for the Weil Quadratic Form.**
> Does there exist δ(k) > 0 such that for all N ≥ 1:
> |μ_k(QW_λ^N) − μ_{k+1}(QW_λ^N)| ≥ δ(k)?
>
> Equivalently: as primes are added to the Euler product,
> do the eigenvalues of the Weil form maintain spacing?

This is the NUMBER-THEORETIC content of RH, distilled to one
estimate about eigenvalue repulsion.

## 5. Possible approaches (for future sessions)

1. **GUE repulsion:** random matrix universality predicts
   eigenvalue repulsion ~ gap². If QW_λ^N falls in a
   universality class, repulsion gives the lower bound.

2. **Arithmetic repulsion:** the eigenvalues of QW involve
   sums over primes. Their spacing might be controlled by
   the distribution of primes (PNT, Mertens, etc.).

3. **CCM's own estimates:** CCM (2025) achieve 10⁻⁵⁵
   precision with 6 primes. Their construction may contain
   implicit gap estimates that we haven't extracted.

4. **Connes' prolate operator:** the prolate wave operator
   PW has known eigenvalue spacing (Slepian). If QW → PW
   in some sense, the spacing transfers.

5. **The Cartwright argument applied to gap functions:**
   the function G(ξ) = μ_k(ξ) − μ_{k+1}(ξ) (eigenvalue gap
   as a function of a parameter) might itself be entire. If
   so, Cartwright could bound its zeros.

---

> *19 kills. 48 research notes. The Cartwright core stands.*
> *Steps 1-7: proved. Step 8: works at each N. Step 10: the wall.*
> *The wall is one estimate: eigenvalue gap lower bound.*
> *The estimate is arithmetic. The search continues.*
