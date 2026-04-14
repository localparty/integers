# Riemann Hypothesis — Official Problem Statement

**Author of official statement:** E. Bombieri, "Problems of the Millennium: the Riemann Hypothesis"
**Source:** https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf
**Local copy:** `../00-clay-rules/riemann-bombieri.pdf`
**Text extract:** `../00-clay-rules/riemann-bombieri.txt`
**Retrieved:** 2026-04-14

---

## The Problem (verbatim)

Bombieri defines the Riemann zeta function and its analytic continuation to all of C with functional equation
> π^{-s/2} Γ(s/2) ζ(s) = π^{-(1-s)/2} Γ((1-s)/2) ζ(1-s)

The trivial zeros are the negative even integers. The other zeros are the complex numbers 1/2 + iα where α is a zero of Riemann's ξ(t).

> **Riemann hypothesis.** The nontrivial zeros of ζ(s) have real part equal to 1/2.

> In the opinion of many mathematicians the Riemann hypothesis, and its extension to general classes of L-functions, is probably today the most important open problem in pure mathematics.

---

## What a solution must prove

Bombieri is clear that the official Millennium problem is the stated Riemann hypothesis for ζ(s) itself:

> The statement that all zeros of the function ξ(t) are real is the Riemann hypothesis.

Extension to GRH / automorphic L-functions is discussed in Bombieri's text as context but is NOT part of the official prize problem — it is a natural outgrowth.

## Equivalent reformulation

> π(x) = Li(x) + O(√x log x)

(Koch's equivalent; the error term cannot be improved by much — lower bound Ω(Li(√x) log log log x) (Littlewood).)

## Clay §5(c) note

RH is NOT a §5(b) problem. A counterexample (a non-trivial zero off the critical line) would fall under §5(c): full prize if it "effectively resolves the Problem." Since existence of even a single off-line zero refutes RH, this is effectively a full resolution; §5(c)(ii) "reformulation" route less likely to apply.
