# T7 Extended Quick-Pass -- 22 Existing Vertices

Scan date: 2026-04-14. Read first 30 lines of each PROOF-CHAIN.md. Compared against T7 baseline.

| Pos | Vertex | Links | Confidence | Type | Status change since T7? | Note |
|---|---|---|---|---|---|---|
| 1 | QG5D | 22/22 | 10/10 | A | No | Hub; all proved; W1/W2 closed |
| 2 | RH | 6/6 | 8/10 | B | Yes: L3d caveat resolved (Slepian compat L12.1); S1-S3 added | Wall: CCM external |
| 4 | GRH | 2/8 | 7/10 | B | Yes: L1 PROVED (via BSD 5c), L2 PROVED (Bratteli-Robinson T2) | Wall: L5 chi-modulated estimates |
| 5 | BSD | 11/11 | 9/10 | A | No | All closed; conditional on CBB only |
| 6 | H12 | 1/6 | 2/10 | D | No | Wall: L5 V-Hilbert 12 extraction |
| 7 | YM | 17/18 | 9/10 | A | Yes: L2 unconditional all-loop (Paper 10/11) | Wall: L18 H4 conditional |
| 8 | NS | 3/8 | 4/10 | C | Yes: upgraded 2->4/10; L4 unconditional all-loop; two published BKM routes | Wall: L5 BKM criterion |
| 9 | Turbulence | 2/7 | 2/10 | D | No (inherits NS/YM upgrades passively) | Wall: L5-6 intermittency + K41 |
| 10 | Hodge | 3/8 | 3/10 | C | Yes: L4 partial closure (abelian var powers, arXiv:2510.21562) | Wall: L3-4 motivic Hodge filtration |
| 11 | Baum-Connes | 2/6 | 3/10 | C | Yes: L5 OPEN->LITERATURE (Higson-Kasparov amenable); conf upgraded | Wall: L3-4 explicit K-theory |
| 12 | PvNP | 5/6 | 7/10 | B | Yes: L5 forward direction sharpened (2026-04-14) | Wall: L5 backward (non-full->Taylor) |
| 13 | VP vs VNP | 1/6 | 1/10 | D | No | Wall: L3 continuous BC lift |
| 14 | BGS | 6/7 | 7/10 | B | Yes: L5 CONJ->LITERATURE (Hardy Z PCC, arXiv:2511.18275) | Wall: L6 conditional on CCM |
| 16 | Twin Primes | 1/5 | 1/10 | C | Yes: L2 dependency cascade recorded (BGS L5 now LITERATURE) | Wall: L4 arithmetic C_2 from GUE |
| 17 | Cramer | 3/5 | 5/10 | B | Yes: major rewrite -- two-face e-circle discovery; conf upgraded | Wall: L4-5 (modular flow return times) |
| 18 | Goldbach | 2/6 | 1/10 | D | Yes: L4 cross-paper dependency tagged (RH conditional on CCM) | Wall: L5 circle method transfer |
| 19 | ABC | 1/6 | 1/10 | D | No | Wall: L3 height function |
| 20 | OPN | 4/7 | 4/10 | C | Yes: major rewrite -- Hecke-orbit projector + ITPFI + spoof-Hasse; conf upgraded | Wall: L6 odd local-global impossibility |
| 21 | Collatz | 3.5/7 | 4/10 | C | Yes: three-face e-circle + Cuntz O_2 bridge + Lyapunov=KMS_1; conf upgraded | Wall: L4 partial (phase operator) |
| 22 | Lehmer | 3/6 | 4/10 | C | Yes: Route B partial (CM-curve Mahler gap proved); conf upgraded | Wall: L4 (general Mahler bound) |
| 24 | Schanuel | 1/5 | 1/10 | D | No | Wall: L3 (Schanuel itself open) |
| 25 | Hilbert 6 | 4/7 | 3-7/10 | C | Yes: L2 CBB axioms upgraded (W1/W2 closure) | Wall: L7 completeness |

## Summary

**Vertices changed: 15 / 22** (unchanged: QG5D, BSD, H12, Turbulence, VP vs VNP, ABC, Schanuel)

**Confidence upgrades since T7:**
- NS: 2/10 -> 4/10 (L4 unconditional all-loop + published BKM routes)
- Cramer: rewritten with two-face e-circle discovery, now 5/10
- OPN: rewritten with Hecke-orbit projector, now 4/10
- Collatz: three-face e-circle + Cuntz bridge, now 4/10
- Lehmer: Route B partial (CM gap proved), now 4/10
- Baum-Connes: L5 reclassified to LITERATURE, now 3/10
- Hodge: L4 partial closure (abelian var powers)
- BGS: L5 flipped to LITERATURE (Hardy Z PCC)

**New walls discovered:** None new. Existing walls sharpened (PvNP L5 forward/backward split; OPN v_2 correction).

**Key pattern:** The 2026-04-14 Agent-I audit touched 15 vertices with cross-paper dependency tagging, literature reclassifications, and the e-circle three-face geometric picture (Lehmer/Cramer/Collatz). No confidence downgrades. The ring is tightening.
