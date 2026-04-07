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

**The e-encoding time: local and immediate.** When an infalling bit
is absorbed at the horizon vertex, the e-conservation law locally
sets the new Planck pixel's e-coordinate to `φ_{in}` (Section 4.3,
Section 5.4). This local encoding is not a signal propagating across
the horizon; it is the creation of a new pixel with the correct
e-charge at the absorption site. The e-coordinate of the new pixel
is immediately fixed by e-conservation — no other pixel is instantly
updated (Section 5.4).

**The 4D thermalization time: `t_scr`.** The *4D observable*
consequences — the modification of the Hawking radiation spectrum
to carry the infalling information — develop at the rate set by the
4D thermal dynamics. The scrambling distributes the localized new
pixel's e-imprint across all horizon pixels, so that subsequent
Hawking emissions sample the mixed e-configuration. The Hawking
radiation is emitted at rate `dN/dt ~ T_H = 1/(8πGM)`, and the
emitted quanta sample the scrambled e-configuration.

The scrambling time is the time for the 4D thermal dynamics to mix
the `δφ` perturbation into the emission process — for the next
emitted quanta to carry e-imprints that reflect the new `δφ`. The
`O(ln S_BH)` factor arises from the Hayden-Preskill decoupling
theorem (Hayden & Preskill 2007, Theorem 2): for a black hole modeled
as a random unitary acting on `S_BH` qubits, an infalling bit becomes
decodable from the Hawking radiation after only `O(ln S_BH)` additional
qubits are emitted. Specifically, the decoupling argument shows that
after k additional emissions following a perturbation, the mutual
information between the perturbation and the accessible radiation
drops to negligible values for `k = O(log₂ S_BH)` — the information
has been scrambled into the full quantum state. In the e-framework,
the perturbation is `δφ` (the new e-imprint), the "qubits" are the
Planck pixels on the horizon, and the thermalization rate is `1/β`.
Therefore:

    t_scr = O(ln S_BH) × β = β/(2π) × ln(S_BH)

reproducing the Sekino-Susskind result.

### 11.3 The Physical Picture

The two timescales paint a clear physical picture:

1. Information arrives at the horizon and is locally encoded in the
   new Planck pixel's e-coordinate by e-conservation at the absorption
   vertex (Section 5.4). The encoding is immediate and local — no
   signal propagates across the entire surface.

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

The Maldacena-Shenker-Stanford (2016) chaos bound `λ_L ≤ 2πT_H/ℏ`
constrains out-of-time-order correlators (OTOCs) of 4D observables.
By the superselection structure of Section 9.3.1 (Property 2:
`[Q̂_e, Ô_{4D}] = 0`), e-propagation does not contribute to any 4D
OTOC — the e-sector is decoupled from the 4D observable algebra.
The Lyapunov exponent measured by 4D OTOCs is `λ_L = 2πT_H/ℏ`,
saturated in the 4D sector alone, consistent with the standard
result for black holes as fastest scramblers. The instantaneous
e-encoding does not enter the chaos bound calculation.

---

