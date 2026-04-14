# Vertex Blackboard — PvNP (Position 10)

*Traversal 01 | Type: B (excision-primary) | Confidence: 7/10*

---

## Chain state
5/6 closed. Links 1-4 PROVED/OUTLINED/VERIFIED. Link 5 forward numerically settled. Link 5 backward OPEN (the wall). Link 6 CONDITIONAL on L5.

## Current wall
Link 5 backward: non-full → Taylor polymorphism. Seven routes attempted (A-G), all stalled or in progress.

## T1 ACT phase — Bypass attempt on Link 5 backward
Assessment based on PROOF-CHAIN.md state:

**Route A (direct spectral gap)**: Highest priority. Spectral gap of modular flow separates P/NPC — but transferring gap to finite-domain Taylor requires the backward direction. ALIVE but needs new ideas.

**Route D (Popa cocycle superrigidity)**: If PCirc+ is w-rigid → automatic structure transfer. ALIVE, depends on verifying w-rigidity of specific groups. CRITICAL priority cell in capacitor (ERG↔OA).

**Route E (Kazhdan/Haagerup)**: Property (T) for Out(M) → spectral gap of representation → fullness criterion. ALIVE, CRITICAL priority cell (REP↔OA).

**Route C (channel correspondence)**: Via conditional expectation — translates to Taylor at finite arity? PARTIAL.

**Routes B, F, G**: Stalled / fallback.

**No new bypass route identified on T1.** The wall is genuine. Mark as HONEST-STALL for this traversal.

## T1 EDGE phase
Ring edge PvNP → BGS: INFO↔PROB + OA↔ERG. "Spectral statistics of modular flow." CANDIDATE per §2 table.
- Action: FILL. The modular flow σ_t on M_Bool^Gamma has spectral statistics that feed BGS. The TGap (spectral gap of modular automorphism) separates P from NPC; for NPC instances, the modular flow is ergodic (type III₁), feeding GUE. Fill as CANDIDATE.

## Move
Vertex PvNP: HONEST-STALL at L5 backward (7 routes, none closed) | Edge PvNP→BGS: CANDIDATE (fill)
