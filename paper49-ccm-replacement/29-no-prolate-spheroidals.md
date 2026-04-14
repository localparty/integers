# §29 — No Prolate Spheroidals Needed

*Paper 49, Part VI: Comparison with CCM. CCM's construction uses
prolate spheroidal wavefunctions as a specific numerical-analytic
tool. Paper 49 doesn't need them. Why the distinction matters.*

---

## What prolates are

Prolate spheroidal wavefunctions (PSWFs) are the eigenfunctions of
the time-frequency localization operator on the real line. Given a
bandwidth $\Omega > 0$ and a time-window radius $T > 0$, the
integral operator

$$
(K f)(x) \ = \ \int_{-T}^{T} \frac{\sin \Omega(x - y)}{\pi(x - y)}
f(y) \, dy
$$

has a discrete spectrum $\{\lambda_n(c)\}$ (where $c = \Omega T$ is
the time-bandwidth product) with eigenfunctions $\{\psi_n(x; c)\}$ —
the prolate spheroidal wavefunctions. They were introduced by Slepian
and Pollak in 1961 to solve the "concentration problem": which
bandlimited function is most concentrated on a given interval?

PSWFs are spectacular tools for numerical analysis. They give
optimally localized bases for bandlimited signal spaces; they satisfy
a second-order differential equation with polynomial coefficients;
their eigenvalues $\lambda_n(c)$ exhibit a sharp transition ("the
prolate cliff") at $n \approx 2c/\pi$ from $\lambda_n \approx 1$ to
$\lambda_n \approx 0$. Engineers love them. Numerical analysts love
them. Signal processing lives on them.

## How CCM uses them

The CCM construction (arXiv:2511.22755 §3) builds the finite-$N$
Hilbert spaces $E_N$ as the first $N+1$ PSWFs on the band
$[-\lambda, \lambda]$ with time radius $L/2 = \log \lambda$, where
$\lambda$ is the spectral parameter (so $c = \lambda \log \lambda$).
The operators $D_N$ are built as specific matrix elements in this
basis; the prolate structure enables certain quadrature identities
that make the analysis tractable.

CCM's rationale is sound: the PSWF basis optimally captures the
Mellin-transform geometry of the problem, and the eigenvalue cliff
gives natural finite-dimensional truncations.

But PSWFs are not the only basis that works. They are a *convenient*
basis. The structural content of CCM's construction — the operator
$D$ and its spectrum — does not depend on the basis choice.

## Why Paper 49 doesn't need them

Paper 49's Hilbert-Pólya operator $D = -(2/\pi^2) i \log \Delta$ is
defined by functional calculus on the modular operator. The modular
operator $\Delta$ is defined canonically by the Tomita-Takesaki
machinery applied to the standard form $(M_1, H_{\omega_1}, J,
P^+)$. The Hilbert space $H_{\omega_1}$ is the GNS space of the
KMS$_1$ state; its structure is dictated by the BC algebra, not by a
choice of basis.

When we want to compute eigenvalues of $D$ numerically at finite
$N$ (Paper 49 Part VII), we can choose whatever basis is convenient.
PSWFs would work. Hermite functions would work. Wavelets would work.
The natural basis, however, is the one induced by the abelian Fourier
structure of $C(\hat{\mathbb{Q}})$ — the characters of the profinite
completion, truncated to the first $N$ primes. This basis has the
compact-resolvent bound automatically (Paper 13 L3c's Fourier
cancellation argument is formulated in *this* basis, not the PSWF
basis).

In the BC Fourier basis, the finite-$N$ approximation is the
truncation of the BC crossed product to the Hecke action of primes
$p \leq P_N$. The modular operator restricted to this subalgebra is a
finite-dimensional positive self-adjoint matrix. Its logarithm gives
$D_N$. The limit $N \to \infty$ is handled by Paper 13 Layer 4
(Bögli) + Layer 5 (Hurwitz), which we have already proved.

## Why this matters

Three reasons the distinction between "prolate basis" and "BC Fourier
basis" matters beyond aesthetics.

**First: universality.** Tomita-Takesaki produces a canonical
modular operator on *any* standard form, independent of basis
choice. The construction is universal in the sense that it applies
to any type III$_1$ factor, not just the BC factor. Prolate
spheroidals are specific to time-frequency localization; they do not
generalize to, e.g., the BC factor twisted by a Dirichlet character
(needed for Paper 13b GRH), or the BC factor for a number field
(needed for Paper 13's generalization to Dedekind zetas), or the
adele-class-space factors (needed for Paper 31 Baum-Connes). In each
generalization, PSWFs would have to be rebuilt from scratch, if they
apply at all. Tomita-Takesaki extends without modification.

**Second: the "just reproducing CCM in different language" worry.**
PROOF-CHAIN.md notes (in the "What could go wrong" section):

> *The scaling/parity identification might require a finite-
> dimensional approximation scheme that LOOKS like CCM's
> construction. If the approximation scheme requires prolate
> spheroidals or Carathéodory-Fejér, we haven't fully escaped CCM —
> we've just reproduced it in different language.*

§29 answers this worry by pointing out that Paper 49's compact-
resolvent bound (Paper 13 L3c) is established in the BC Fourier
basis, which has nothing to do with PSWFs. If the Fourier basis works
at all (it does, by Paper 13 L3c), then Paper 49 has genuinely
escaped the prolate dependency. The finite-$N$ truncation is
structural (truncate the Hecke action to the first $N$ primes), not
basis-dependent (truncate to the first $N$ prolates of a given
bandwidth).

**Third: robustness to the exact choice of basis.** Different
numerical routes to $\text{spec}(D_N)$ should give the same
eigenvalues. If CCM's prolate-based $D_N$ and Paper 49's BC-Fourier-
based $D_N$ both approximate the same $D_\infty$, they must be
unitarily equivalent modulo an error that goes to zero as $N \to
\infty$. This is a testable claim (Paper 49 §34): compute both and
compare. Agreement at 50+ digits across $N = 60, 90, 120$ is the
expected outcome.

## What CCM uses prolates for that Paper 49 doesn't

CCM's proof machinery uses PSWFs in three specific ways:

1. **As a basis for the finite-$N$ Hilbert space $E_N$**. Paper 49:
   uses the BC Fourier basis instead.
2. **As the eigenbasis of a limit operator $K$ on the band**. Paper
   49: no such limit operator is needed; the modular operator
   $\Delta$ on $H_{\omega_1}$ plays that role directly.
3. **For certain quadrature identities in the proof of Lemma 7.3
   ($\hat{k}_\lambda \to \Xi$)**. Paper 49: the corresponding
   convergence is handled by Paper 13 Layer 5 (Hurwitz) without
   quadrature — the convergence of $\hat \xi_N \to \Xi$ uniformly on
   compact substrips is structural, from the uniform H$^1$ bound.

None of these three uses is irreplaceable.

## A precise statement

**Claim.** The spectrum of Paper 49's $D_\infty$ does not depend on
the choice of finite-$N$ truncation basis (PSWF, BC Fourier, Hermite,
etc.), provided the basis respects the BC algebra's parity
decomposition and the truncation is nested.

**Sketch.** By Bögli spectral exactness (Paper 13 L4; classical
arXiv:1604.07732), $\text{spec}(D_\infty) = \lim \text{spec}(D_N)$
for any approximation satisfying (H1) form convergence and (H2)
discrete compactness. Both hypotheses are structural properties of
the pair (truncation, limit); they are invariant under a change of
truncation basis provided the nested-subspace condition holds.
Different bases give different paths to the same limit; the limit is
basis-independent.

This is why "no prolate spheroidals needed" is not a cosmetic claim.
The structural content of Paper 49 is basis-free. Prolates are one
numerical route; the BC Fourier basis is another; the limiting
operator $D_\infty$ is the same.

---

*Next: §30 — no Carathéodory-Fejér stabilization needed. CCM needs
CF to guarantee self-adjointness at finite $N$. Paper 49 gets self-
adjointness from functional calculus.*
