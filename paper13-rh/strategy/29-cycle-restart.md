# Strategy 29 — Cycle Restart: The Gap Bound

*The wall: eigenvalue gap lower bound for QW^N as N → ∞,*
*in a regime where QW^∞ doesn't exist on a fixed space.*
*The tension: all primes needed for simplicity, all primes*
*destroy compactness. Find a way through.*

*Date: 2026-04-10*
*Status: SEARCHING*

---

## 1. What we know

- Steps 1-7 (Cartwright core): PROVED
- Step 8 (secular induction at finite N): PROVED  
- Step 9 (ITPFI state convergence): PROVED
- Step 10 (limit preserves simplicity): THE WALL
- QW^∞ on fixed L² doesn't exist (kernel diverges)
- CCM uses growing spaces (λ, N increase together)
- The gap at finite N decays as ~10^{-1.5N} (model matrix)
- The continuous eigenfunction gaps are unknown

## 2. The tension stated precisely

> Cartwright gives simplicity for COMPACT operators with
> FINITELY many primes. The limit needs ALL primes but
> destroys compactness. How do you get simplicity for
> an operator that requires infinite primes but can't
> have them?

## 3. Ideas not yet tried

### Idea 1: Don't take the limit — prove RH from finite N
Maybe RH doesn't NEED QW^∞. If the Riemann zeros are eigenvalues
of QW^N for EACH N (CCM shows this numerically), and each QW^N
has simple eigenvalues (Cartwright), then... what? The zeros are
simple eigenvalues of every finite truncation. Does this imply
they're on the critical line?

### Idea 2: CCM's own limit (λ,N → ∞ together)
CCM don't fix λ and send N → ∞. They send BOTH λ → ∞ and
N → ∞ with N ~ π(λ²). In this regime, the space L²([λ⁻¹,λ])
GROWS and can absorb more primes. The kernel might converge in
this growing-space topology. Study the CCM limit structure.

### Idea 3: Renormalization
The kernel diverges because Σ log(p)/√p = ∞. But the Weil
explicit formula has a RENORMALIZED version (subtract the
divergent part, which is a known constant). The renormalized
kernel might converge. This is standard in QFT — divergent
sums become finite after renormalization.

### Idea 4: The Yakaboylu operator W
Yakaboylu's intertwining operator W ≥ 0 gives RH directly from
positivity, without needing eigenvalue simplicity or limits.
Maybe W + ITPFI bypasses Step 10 entirely.

### Idea 5: Bombieri's finite-N eigenvalue count
Bombieri (2000): negative eigenvalues of truncated QW count
off-line zeros. If QW^N ≥ 0 for all N (proved by our Cartwright
+ simplicity argument?), then there are no off-line zeros for
any finite truncation. Does this propagate to the full ζ?

---

> *The tension is the problem. The problem is the invitation.*
> *Five ideas. At least one is new. Keep going.*
