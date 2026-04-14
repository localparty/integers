# Repair Run Blackboard -- Tier 4 Boegli Post-Verification

*Run: 2026-04-13. Mode: REPAIR. Source: Tier 4 pilot blackboard action items.*

## A. North Star
Apply the three repair actions identified by the Tier 4 pilot run. No new verification needed -- all repairs are CLOSABLE (standard fixes).

## B. Repair actions

| # | Action | Status | Files modified |
|--:|--------|--------|----------------|
| 1 | Section 9.1: swap Teschl Lemma 2.7 gnrc citation -> Chatelin Galerkin route | **DONE** | `paper13-rh/preprint/sections-06-10.md` |
| 2 | Add Chatelin (1983) to references | **DONE** | `paper13-rh/preprint/sections-06-10.md` (external results table, line 962+) |
| 3 | Update capacitor with K-T4-1, TK-6, TK-7 | **DONE** | `verification-cascade/tier-4-trial-boegli/03-capacitor.md` |

## C. Detailed change log

### Repair 1: Section 9.1 gnrc source (sections-06-10.md)

**What changed:**
- Section 9.1 header: "The Teschl form-boundedness criterion" -> "gnrc and KLMN closability"
- Theorem 9.1(i): now explicitly KLMN closability only (Teschl Lemma 2.7). Teschl kept here -- hypothesis (2.1) is not needed for closability.
- Theorem 9.1(ii): NEW -- Chatelin Galerkin gnrc (1983, Ch. 3). Compact resolvent + P_N -> I strongly => norm resolvent convergence. Equation (9.1b) added.
- Remark 9.1a: NEW -- explains why Teschl Lemma 2.7 cannot be cited for gnrc (standing hypothesis (2.1) fails for Galerkin projections: ||P_N - I|| = 1 for all N).
- Corollary 9.5: updated to cite Chatelin Galerkin gnrc (Theorem 9.1(ii)) instead of Teschl. References compact resolvent (Corollary 9.8) and P_N -> I strongly.
- Proof of Theorem 9.9: "(Teschl form bound with a=0<1 giving gnrc)" -> "(Chatelin Galerkin gnrc)".
- Section 9 intro paragraph: updated to describe Chatelin route for gnrc, Teschl for KLMN.
- Proof chain diagram: "Teschl form bound" -> "form bound" for Theorem 9.3; "gnrc via Chatelin Galerkin + compact resolvent" for Corollary 9.5.
- Closing narrative: updated to name Chatelin and Teschl separately by role.
- Closing italicized summary: split "Teschl gives gnrc and KLMN simultaneously" into "Chatelin gives gnrc; Teschl gives KLMN closability."

**What did NOT change:**
- Corollary 9.6 (KLMN closability): still cites Teschl. Correct -- hypothesis (2.1) is not needed.
- Theorem 9.3 (form bound a=0): unchanged. The form bound is correct; only its downstream use for gnrc needed repair.
- Corollary 9.8 (discrete compactness): unchanged.
- Theorem 9.9 (spectral exactness): conclusion unchanged, only proof citation updated.

### Repair 2: Chatelin reference (sections-06-10.md)

- External results table (Section 10.6): added row for "Chatelin Galerkin gnrc | Chatelin, Spectral Approximation of Linear Operators, 1983, Ch. 3 | Corollary 9.5".
- Teschl row updated: "form-bounded gnrc" -> "KLMN closability", role changed from "Theorem 9.3" to "Corollary 9.6".

### Repair 3: Capacitor v2 (03-capacitor.md)

- META: v1 -> v2. Step statuses updated (all SURVIVED+LOCK). Kill count updated (1 target-specific).
- KILLS: K-T4-1 added with full five-field entry.
- CHAIN: all step statuses updated to SURVIVED+LOCK. Step 4 ref fixed (Cor 2.8 -> Thm 2.4(ii)+Thm 2.6 s.a.). Step 5 description updated (Chatelin+Teschl).
- TOOLKIT: TK-6 (Galerkin gnrc) and TK-7 (gsr sufficiency) added.
- AUTHORS' HONEST STATEMENTS: "Cor 2.8" -> "Thm 2.4(ii) + Thm 2.6 s.a. case".
- MERGE LOG: v2 row added.

### Downstream repairs (sections-11-14.md)

Three narrative mentions of "Teschl's Lemma 2.7 gives gnrc" updated:
- Line ~119: H1 description now cites Chatelin for gnrc, Teschl for KLMN.
- Line ~212: "gnrc (via Teschl's Lemma 2.7)" -> "gnrc (via Chatelin Galerkin theory)".
- Line ~656: "gnrc (via Teschl's Lemma 2.7 + ITPFI + CF)" -> "gnrc (via Chatelin Galerkin + compact resolvent)".

## D. Verification

The repair is CLOSABLE (no new mathematics):
- Chatelin 1983, Ch. 3 is a 40-year-old textbook result
- The conclusion (gnrc for CCM operators) is unchanged
- The proof route is redirected from Teschl -> Chatelin, both arriving at the same norm resolvent convergence
- Teschl is retained for KLMN closability, where its standing hypothesis (2.1) is not required

## E. Closure

**CLOSED.** All three repair actions complete. No new verification needed.

Proceed to Tier 1 (CCM).
