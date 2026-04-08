# Prompt 01 — Number-Theoretic Route: Trivial Zeros of ζ_R

**Issued by:** G (principal investigator)  
**Route:** 01 — Number-theoretic / trivial zeros of the Riemann zeta function  
**Output file:** `01-number-theoretic-zeta-zeros.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/zeta-zeros/`

---

## Context

Paper 1 of the QG5D series proves perturbative UV finiteness of 5D linearized gravity on
M⁴ × S¹/Z₂ using zeta regularization of the KK mode sums. The key step is the Universal
Epstein Vanishing theorem: the Epstein zeta function evaluated at the argument relevant to
the Goroff-Sagnotti counterterm vanishes.

The open honesty: this vanishing is proved in zeta regularization. Scheme-independence
(does the same vanishing occur in dim-reg, Pauli-Villars, heat kernel reg?) is not proved.

## Your question

**Does the Epstein vanishing correspond to a trivial zero of the Riemann zeta function?**

The Riemann zeta function has trivial zeros at negative even integers: ζ_R(−2k) = 0 for
k = 1, 2, 3, ... These zeros follow from the functional equation and are number-theoretic
facts — completely independent of any regularization scheme.

On S¹/Z₂ with KK spectrum {m_n = n/R, n = 0, 1, 2, ...}, the KK mode sum contributing
to the Goroff-Sagnotti counterterm is schematically:

    C_GS ∝ ∑_{n=-∞}^{∞} |n/R|^{−2s}  evaluated at s = s₀

For the orbifold (modes n ≥ 0 with parity), this reduces to a Riemann or Hurwitz zeta
function at argument s₀. If s₀ is a negative even integer, the sum is zero by the
functional equation — and that zero is a number-theoretic identity, not a regularization
artifact.

## Your task

1. **Read the relevant Paper 1 sections** first. Paper 1 source files are at:
   `/Users/gsix/quantum-geometry-in-5d-latex/paper1/`
   Focus on: `32-appendix-u-goroff-sagnotti-verification.md` and
   `22-appendix-k-higher-loop-epstein.md`

2. **Determine the argument s₀** at which the Epstein/Riemann zeta function is
   evaluated in the Goroff-Sagnotti diagram. Use power-counting of the 5D loop
   diagram: graviton propagator ~ 1/p², vertices ~ p², loop measure ~ p⁵ in 5D.
   Track the dimension of the GS operator (dimension 6 in 4D) to identify s₀.

3. **Check if s₀ is a negative even integer.** If yes: state the theorem that the
   vanishing is a consequence of the functional equation, hence scheme-independent.
   If no: characterize what kind of zero it is and whether it can still be argued to
   be scheme-independent.

4. **Write Python code** in `/Users/gsix/quantum-geometry-in-5d-latex/code/zeta-zeros/`
   to:
   - Create a venv named `venv` and install `mpmath`, `sympy`
   - Evaluate ζ_R(s) for s = −2, −4, −6, −8 (the trivial zeros) to verify
   - Evaluate the Epstein function for the S¹/Z₂ KK spectrum at s₀ numerically
   - Verify the functional equation: ζ_R(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ_R(1−s)
   - Show the cancellation between Z₂-even and Z₂-odd mode contributions numerically
   Save scripts as `compute.py` and output as `results.txt`.

5. **Write your research memo** to `01-number-theoretic-zeta-zeros.md` with:
   - Summary (3–5 sentences)
   - Setup (what Paper 1 establishes)
   - Main argument (the functional equation route)
   - Numerical results (embedded from your computation)
   - Gaps / obstacles (what would be needed to complete a full proof)
   - Status: Promising / Partial / Dead End / Requires new mathematics
   - If promising: proposed next step

## Format note

Include key code snippets and numerical output inline in the memo. The memo and code
together form an appendix. Aim for 400–600 lines.
