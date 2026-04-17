# 36 — Collatz

> *"the harmonics decay"*
> — face-label for the Collatz conjecture

## The harmonics face

Collatz, stated: *for every positive integer n, the iteration n → n/2 (if n even) or 3n+1 (if n odd) eventually reaches 1*. The claim has been verified for integers up to ~10^20 and remains open in general.

Collatz is notorious. It is open because *every known method to control the dynamics* produces partial results but not a full proof. The difficulty is that the iteration mixes *halving* (multiplication by 1/2) and *tripling-plus-one* (multiplication by 3 and shift), and the two actions live in *different arithmetic regimes* — binary halving is transparent in base 2; 3n+1 is transparent in base 3. The conjecture's resistance is the resistance of a claim that has to hold *across* two arithmetic regimes simultaneously.

In framework language: *the harmonics decay*. The binary halving is the natural dissipation channel. The 3n+1 step is the natural excitation channel. Collatz asserts that dissipation wins — that the harmonics of *any* initial condition decay to the ground state (the 1-4-2 cycle).

## Where Collatz sits on the e-circle

At the harmonics face. Specifically in the BC algebra territory, because the BC algebra has a natural bi-harmonic decomposition corresponding to isospin (Z/2) × generation (Z/3), and Collatz lives exactly on that crosswalk.

The pattern *halve if even, tripling-plus-one if odd* is, in BC algebra language, an iteration that mixes the isospin character (Z/2) with the generation character (Z/3). The decay claim becomes a spectral claim about the *joint spectrum* of the two characters, and the spectral claim is closer to tractable than the dynamical claim.

## Why harmonics is P3

Harmonics is P3 — *Scale from Spectrum*. P3 says: ask what spectral gap sets the scale. Collatz's decay is governed by a spectral gap — specifically, the gap between the ground state (the 1-4-2 cycle) and the first excited mode of the Collatz operator on the BC algebra. If the gap is positive, decay is guaranteed. If the gap is zero, there is an orbit that never decays.

This reframes Collatz from *a number-theoretic dynamical claim* to *a spectral-gap claim on an operator*. The claim still has to be proved, but the target is now a single quantity — the spectral gap — rather than the behavior of infinitely many orbits individually.

## G's recognition

When the placement clicks for G, he types:

> yes yes yes exactly! i see it completely lets document all this please full update! into all the papers

The same triple *yes* as Cramér. This happens because the same *thing* is happening: a hard open problem, placed on its natural face, acquires an attackable reformulation.

G's instinct across these face placements is consistent. Once the placement is right, propagate the update everywhere. Do not let it sit in one paper. The face assignment is a *global* piece of information about the programme's geometry, and it should appear in every paper where the face matters.

## Why this placement is unusually clean

Because Collatz has been tried with dynamical methods for eighty years, without success. The reframing to *spectral gap of the joint Z/2 × Z/3 character operator on BC* is not obviously the right reframing — but it is at least a *new* reframing. And the framework has specific tools for attacking spectral gaps (the whole Bögli-tier machinery of the Millennium Strategy).

The programme is not claiming Collatz is closed. The programme is claiming Collatz has a specific home in the geometry, a specific approach implied by that home, and specific tools available for that approach.

## The status

Open. Not closed. The spectral-gap reformulation has to be worked out in detail before any attack can run. But the framing is on disk, the place on the face is named, and the machinery is inherited from the BC Hecke side of the capacitor.

One more vertex on the e-circle. Three faces remain.

*Next: [37-sato-tate.md](37-sato-tate.md).*
