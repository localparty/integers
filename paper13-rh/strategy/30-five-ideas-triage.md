# Strategy 30 — Five Ideas Triage

*Date: 2026-04-10*

---

## Triage of the five ideas from strategy/29

### Idea 1: RH from finite N alone — PROMISING (5/10)

**From online search:** arXiv:0704.3448 "Finite Euler products and
the Riemann Hypothesis" — if RH is true, ζ is well approximated
by short Euler products in the critical strip. The CONVERSE
direction is what we need: can finite-N results imply RH?

**The angle:** At each finite N, CCM's operator D(λ,N) has
spectrum at {γ_n} (numerically). Our Cartwright argument gives:
the eigenvalues are SIMPLE at each N. CCM's Theorem 5.10 shows
these eigenvalues APPROACH the Riemann zeros as λ,N → ∞.

**The question:** CCM already show convergence of eigenvalues
TO the zeros. We show simplicity AT each N. Does
{convergence + simplicity at each N} → zeros on critical line?

If CCM's operators are self-adjoint at each N (they are — CF
theorem), their eigenvalues are real. The eigenvalues approach
the Riemann zeros. If the convergence is PROVED (not just
numerical), then the zeros are limits of real numbers, hence
real. That's RH.

**KEY INSIGHT: We don't need Step 10 at all.** We need:
(a) CCM's eigenvalues are real (self-adjointness at each N) ✓
(b) CCM's eigenvalues converge to {γ_n} (CCM Theorem 5.10) — 
    THIS is what CCM haven't fully proved
(c) Our contribution: simplicity at each N (Cartwright) ensures
    the convergence is well-behaved (no eigenvalue collisions
    that could disrupt convergence)

The missing piece is (b): CCM's OWN convergence proof. Their
paper says "numerical experiments show convergence" and identifies
"a rigorous proof of this convergence would establish RH."

So: RH = CCM's convergence theorem. Our Cartwright simplicity
SUPPORTS the convergence (no collisions) but doesn't prove it.

### Idea 2: CCM's growing-space limit — PROMISING (5/10)

CCM send λ → ∞ with N ~ π(λ²). The spaces GROW. In this
topology, the kernel MIGHT converge because the interval grows
to absorb the divergent sum.

||K_N||_HS² on [λ⁻¹,λ] = ∫∫ |K_N(x,y)|² dx dy.
The integral region grows as (λ - λ⁻¹)² ~ λ².
The kernel involves Σ_{p≤λ²} (log p/√p)² cos²(...) terms.
Each term contributes ~(log p)²/p · λ to the HS norm.
Total: Σ_{p≤λ²} (log p)²/p · λ ~ λ · (log λ)² (Mertens).
So ||K_N||_HS ~ λ^{1/2} · log λ — GROWS but polynomially.

The eigenvalues of K_N are bounded by ||K_N||_HS. The number
of eigenvalues ~ λ (Weyl law on [λ⁻¹,λ]). So eigenvalues
are O(log λ / √λ) — they SHRINK. In this regime, eigenvalue
gaps could be bounded below.

### Idea 3: Renormalized kernel — WORTH EXPLORING (4/10)

Zeta function regularization is our OWN tool (Pattern 5). The
divergent Σ log(p)/√p can be regularized by analytic continuation.
The regularized value is related to -ζ'(1/2)/ζ(1/2) (the
logarithmic derivative of ζ at s=1/2). This is a finite number.

### Idea 4: Yakaboylu W ≥ 0 — STILL ALIVE (5/10)

Yakaboylu's W ≥ 0 gives RH from POSITIVITY, not simplicity.
No eigenvalue gaps needed. No Step 10. If W factors via ITPFI
(W = ⊗_p W_p), positivity is a prime-by-prime check.

This was Lead 1 in strategy/07, rated 6/10. The obstacles
(identifying W with BC data, checking factorization) are
unchanged but the motivation is stronger now: it BYPASSES
the Step 10 wall entirely.

### Idea 5: Bombieri finite-N count — SUPPORTING (3/10)

Evidence only. Can't prove RH alone.

## Priority for next cycle

| # | Idea | Why |
|:--|:--|:--|
| 1 | Idea 1 (finite N alone) | CCM convergence is the key; our simplicity supports it |
| 2 | Idea 4 (Yakaboylu W) | Bypasses Step 10 entirely via positivity |
| 3 | Idea 2 (growing space) | CCM's actual limit structure |
