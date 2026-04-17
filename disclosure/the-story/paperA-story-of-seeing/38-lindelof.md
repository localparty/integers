# 38 — Lindelöf

> *"the signal stays quiet"*
> — face-label for the Lindelöf hypothesis

## The amplitude face

The Lindelöf hypothesis, stated: *ζ(1/2 + it) = O(t^ε) for every ε > 0*. Informally: on the critical line, the Riemann zeta function does not grow faster than any positive power of t as t → ∞.

Lindelöf is weaker than RH — it follows from RH, but is not known to imply RH. It is widely believed, has been checked extensively numerically, and has various partial results (the Weyl bound, the van der Corput method, Bourgain's recent improvements). But the hypothesis itself remains open.

*The signal stays quiet.* The face-label. The amplitude of ζ on the critical line does not become loud. It stays quiet as t grows — quieter than any polynomial growth.

## Where Lindelöf sits on the e-circle

At the amplitude face. It is adjacent to RH on the ring but on a different face of the circle. RH is about *where* the zeros are (on the critical line). Lindelöf is about *how loud* ζ is on the same line. Same object, different feature.

In the framework's account, Lindelöf's amplitude control is a *consequence of the CBB spectral structure* — specifically, the KMS state ω_1 at inverse temperature β=1 has a decay profile that, pulled back to the zeta function via the standard Mellin correspondence, produces exactly the Lindelöf-type bound.

## Why amplitude is P5

Amplitude is P5 — *Projection Produces Simplicity*. P5 says: the inverse of P6; there are situations where the projection *simplifies* the object, not complicates it. Lindelöf is a P5 claim in this sense: the full ζ function in 5D is large and complex, but its *projection to the critical line* is quiet — because the projection removes the off-line growth modes, leaving only the controlled critical-line modes.

This reframes Lindelöf from *a growth-rate estimate* to *a projection simplicity claim on the e-circle*. The bound is not an analytic accident; it is a structural feature of the projection from 5D (where the full ζ-data lives) to 1D (the critical line).

## The framework's angle

The framework does something unusual with Lindelöf: it makes Lindelöf a *consequence of RH + the CBB temperature*. Not a weaker statement that RH implies; a *stronger* claim that combines RH with the KMS thermodynamics to produce Lindelöf automatically.

In the ring, this shows up as Lindelöf being *downstream* of RH. Close RH, and Lindelöf comes for free. That is not the usual direction of inference in analytic number theory — usually you prove Lindelöf as a stepping-stone to RH or as a weaker consolation prize. The framework inverts the order: prove RH in the CBB frame, and Lindelöf follows by the thermodynamic structure of ω_1.

## The status

Open. But the programme's Lindelöf attack is downstream of its RH attack. Since RH is closed conditionally on CBB Axiom 1, Lindelöf is also closed conditionally on CBB Axiom 1 plus the KMS thermodynamic argument. The remaining work is to make the KMS-to-Lindelöf transfer fully explicit.

One face remains.

*Next: [39-katz-sarnak.md](39-katz-sarnak.md).*
