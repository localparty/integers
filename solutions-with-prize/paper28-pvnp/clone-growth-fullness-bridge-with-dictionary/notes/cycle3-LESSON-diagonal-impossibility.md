# LESSON — The diagonal impossibility and complementary failure

**Cycle:** 3
**Source:** W3-1 Critic + W3-5 Synthesis + W3-4 Author (converging)

## The lesson

On Boolean domain {0,1}, the Mal'cev property (m(x,y,y)=x) and exponential mixing are complementary: each holds where the other fails. This creates a "diagonal impossibility" for any proof that requires BOTH. The 1.3.1 proof required both and covered 0/4 Schaefer classes.

## The structural insight

The complementary failure is not accidental — it reflects a deep algebraic dichotomy:
- **Affine languages (XOR):** algebraically structured, Mal'cev operations exist, but correlations don't decay (global algebraic constraints)
- **Non-affine tractable languages (Horn/2-SAT):** locally structured, mixing works, but no Mal'cev (majority/min/max don't satisfy m(x,y,y)=x)

A unified proof must use a property that BOTH types share. The shared property is: **exponential clone growth** (UA1). The growth rate is the invariant, not any specific algebraic identity.

## The refined sector taxonomy

Mal'cev polymorphisms give automorphisms (Jones index 1). Non-Mal'cev k-ary polymorphisms give proper endomorphisms (Jones index > 1). The proof for non-affine classes needs the proper endomorphism structure, not the Mal'cev automorphism structure.

## Kill list pattern

K-20 (Overspecialization) joins K-1, K-18, K-19 (Wrong-space). Four kills share: using tools specific to one algebraic setting on a broader class. The programme needs tools that match the GENERALITY of the Taylor condition.
