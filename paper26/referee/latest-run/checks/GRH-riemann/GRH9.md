## Check GRH9: GRH for L(s, psi) follows from the bridge construction

**Group:** GRH
**Source:** Preprint Section 9.2, Step C
**Pass criterion (from prompt):** The Grossencharacter psi is a Hecke character over K; its L-function's zeros are controlled by the bridge.

**Verdict:** PARTIAL

**Justification:**
This is the single most critical check in the entire review. The bridge family over Q(i) directly captures zeros of zeta_K(s) (the Dedekind zeta function). To reach L(s, psi) (the Hecke L-function of the Grossencharacter), the preprint invokes the Connes-Marcolli twisted spectral realization (2006, section 4.3). The argument claims the cocycle shift formula is insensitive to the character twist because |psi(p)| = 1 and the Euler factor ratio depends only on N(p), not on the phase psi(p).

This argument is structurally sound and supported by the Connes-Marcolli framework, but the proof is sketched rather than complete. The missing piece: an explicit demonstration that the Hasse invariant of the bridge cyclic algebra is unchanged when the spectral realization is twisted by psi. This should follow from the fact that the Hasse invariant depends on the Frobenius order in the cyclotomic extension, which is independent of the Hecke character, but this needs to be written out.

Estimated closure: 2-3 pages of explicit computation.

**Cross-references:**
- Per-Point file(s): points/A3-meyer-spectral/03-extension-hecke.md, points/D1-cm-factorization/03-zeros.md
