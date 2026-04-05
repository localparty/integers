## 11. Scrambling Time


### 11.1 The Fast Scrambling Conjecture

Sekino and Susskind (2008) conjectured that black holes are the
fastest scramblers in nature — they thermalize infalling information
in the minimum time consistent with quantum mechanics:

    t_scr = β/(2π) × ln(S_BH)

where `β = 1/T_H = 8πGM` is the inverse Hawking temperature and
`S_BH = A/(4l_P²)` is the Bekenstein-Hawking entropy. For a
solar-mass black hole: `t_scr ~ 10⁻³` seconds — essentially
instantaneous compared to the evaporation time.

### 11.2 Scrambling in the e-Dimension Framework

The e-dimension framework has two timescales for information
processing:

**The e-propagation time: instantaneous.** The δφ shift from an
infalling bit propagates across the entire horizon surface with
no delay, because e has no causal structure (Section 5.2). In the
e-dimension, information is immediately available everywhere on the
horizon.

**The 4D thermalization time: `t_scr`.** The δφ shift modifies the
e-coordinates of all Planck pixels on the horizon simultaneously,
but the *4D observable* consequences — the modification of the
Hawking radiation spectrum — develop at the rate set by the 4D
thermal dynamics. The Hawking radiation is emitted at rate
`dN/dt ~ T_H = 1/(8πGM)`, and the emitted quanta sample the
scrambled e-configuration.

The scrambling time is the time for the 4D thermal dynamics to mix
the δφ perturbation into the emission process — for the next
`O(ln S_BH)` emitted quanta to carry e-imprints that reflect the
new δφ. This is:

    t_scr = (number of quanta to sample scrambled config) / (emission rate)
           = O(ln S_BH) / T_H
           = β/(2π) × ln(S_BH)

reproducing the Sekino-Susskind result. The logarithmic factor
arises because a random sampling of the scrambled e-configuration
requires `O(ln N)` samples to detect a single-pixel perturbation
in an `N`-pixel surface — the coupon collector's threshold.

### 11.3 The Physical Picture

The two timescales paint a clear physical picture:

1. Information arrives at the horizon and is instantly encoded in
   the e-structure of the entire surface (e-propagation: instant).

2. The 4D thermal dynamics of the horizon scramble the 4D
   manifestation of this e-information over the scrambling time.

3. After `t_scr`, the Hawking radiation begins to carry the
   e-imprint of the infalling bit — but only in the e-coordinates,
   invisible to 4D detectors.

4. After `t_evap ~ M³`, the black hole has fully evaporated and all
   e-imprints are in the radiation.

The e-dimension provides the mechanism (geometric encoding), and
the 4D dynamics provide the timescale (thermal scrambling). Neither
alone suffices — both are needed for the complete picture.

---

