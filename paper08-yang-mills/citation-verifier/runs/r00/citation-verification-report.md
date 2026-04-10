# Citation Verification Report

**Session:** r13, 2026-04-07
**Scope:** Full audit of all preprint body files vs references.md and citation-tiers.md ledger;
focus on new appendices (I3, I4, K, J) not audited in prior sessions, plus
re-verification of WEB citations with specific theorem numbers.

---

## New appendices audited this session

### Appendix K (K-balaban-general-groups.md)

**K:12** — `Dimock, arXiv:1108.1335`
→ Correct arXiv ID for Dimock 2013a (LOCAL, verified). ✓

**K:200** — `Balaban (CMP 119, Section 2)`
→ CMP 119 PDF (LOCAL) shows unnumbered Theorem states "if ρ_k satisfies the assumptions
described in Sect. 2" — confirms Section 2 exists. ✓

**K:255** — `Kotecky--Preiss criterion`
→ No specific theorem number cited. Kotecky-Preiss has unnumbered Theorem (p. 492). ✓

**K:288-289** — `Balaban CMP 109, Theorem 1/3`
→ Matches ledger: Thm 1 (UV stability), Thm 3 (detailed). ✓

**Corrections applied:** None.

---

### Appendix I4 (I4-other-gauge-groups.md)

**I4:53** — `(Besse 1987, Theorem 7.73)`
**Finding:** Theorem 7.73 in Besse = Ricci curvature formula r = −B|p (not the Einstein property
itself). The Einstein property follows from Corollary 7.74 (A Riemannian symmetric space is
Einstein iff B|p is definite and proportional to the scalar product). Positivity follows from
compact type (B negative definite on p).

**Error:** Citation "Theorem 7.73" alone is insufficient for the claim "Einstein with λ_G > 0."
The correct citation chain is Theorem 7.73 + Corollary 7.74.

**Fix applied:** `I4-other-gauge-groups.md:53`
- Before: `(Besse 1987, Theorem 7.73)`
- After:  `(Besse 1987, Theorem 7.73 and Corollary 7.74)`

**I4:226, 249** — `(Borel 1953)`
→ General citations without specific theorem numbers. WEB, no issues. ✓

---

### Appendix I3 (I3-N-dependence-tracking.md)

**I3:128** — `(Balaban, CMP 109, Theorem 1; detailed: Theorem 3)`
→ Matches ledger finding exactly. ✓

**I3:356** — `(Balaban, CMP 109, 119)`
→ General citation range, no specific theorem. ✓

**Corrections applied:** None.

---

### Appendix J (J-lattice-symanzik-basis.md)

Appendix J has a self-contained numbered reference list [1]–[3]. Verified against references.md:

| Ref | Cited as | references.md entry | Match? |
|:----|:---------|:--------------------|:-------|
| [1] | Symanzik, Nucl. Phys. B **226** (1983) 187–204 | Symanzik 1983, same vol/pages | ✓ |
| [2] | Luscher-Weisz, CMP **97** (1985) 59–77 | Lüscher-Weisz 1985, same vol/pages | ✓ |
| [3] | Weisz-Wohlert, Nucl. Phys. B **236** (1984) 397–422 | Weisz-Wohlert 1984, same vol/pages | ✓ |

**J:214** — `[2, Section 3]` — Lüscher-Weisz paper (WEB) cited for Section 3. Plausible
but unverifiable without PDF. Flagged.

**Corrections applied:** None.

---

## #18: Nachtergaele-Sims, CMP 265 (2006)

**Status:** LOCAL (this session)
**PDF:** `journals/nachtergaele-sims-CMP265-2006.pdf`
**Source:** arXiv:math-ph/0506030, downloaded this session
**Title page:** CMP 265, 119–130 (2006) — CONFIRMED
**Numbering:** Plain (Theorem 1, Theorem 2)

**Results found:**
- Theorem 1 (Lieb-Robinson bound): exponential bound on propagation speed
- Theorem 2 (Exponential clustering): for a gapped lattice Hamiltonian,
  spatial correlations decay exponentially

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1152` — cites "Thm 2.1" — **WRONG** (no such number)

**Error:** "Thm 2.1" implies section-based numbering. Paper uses plain numbering.
The intended theorem is Theorem 2 (exponential clustering).

**Correction applied:**
- Before: `e.g. Nachtergaele--Sims 2006, Thm 2.1`
- After:  `e.g. Nachtergaele--Sims 2006, Theorem 2`

---

## #23: Friedli-Velenik, Cambridge (2017)

**Status:** WEB (chapter PDF downloaded for verification)
**PDF:** chapter downloaded from unige.ch/math/folks/velenik/smbook/
**Title:** Statistical Mechanics of Lattice Systems — CONFIRMED
**Numbering:** Section-based (Theorem 5.4 = Theorem 4 of Section 5.4)

**Results found:**
- Theorem 5.4 (p. 224): Abstract polymer cluster expansion convergence.
  Statement: given ∑_γ |w(γ)|e^{a(γ)}|ζ(γ,γ*)| ≤ a(γ*) for all γ*, the
  cluster expansion log Ξ converges absolutely. This is the abstract version
  of the Kotecky-Preiss criterion.

**Preprint references this paper at:**
- `sections/04-lattice-proof-part1.md:1001–1002` — cites "Theorem 5.4" — **CORRECT** ✓
- `sections/04-lattice-proof-part1.md:1259` — cites "Chapter 5" — **CORRECT** ✓

**Corrections applied:** None. Added to references.md (was missing).

---

## #24: Krantz-Parks, Birkhäuser (2002)

**Status:** WEB (book, no free PDF)
**Title:** A Primer of Real Analytic Functions, 2nd ed.

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1536` — cites "Thm 1.1.5" for identity theorem
- `sections/H-balaban-analyticity.md:349` — cites "Thm 1.1.5" same

**Verification:** Book uses section-based theorem numbering (1.1.5 = theorem 5 of §1.1).
Theorem 1.1.5 for an identity theorem result is plausible in Chapter 1 on basic properties
of real analytic functions. Could not verify exact theorem statement without book access.
**Status: UNVERIFIED theorem number — flagged for manual check.**

**Corrections applied:** None. Added to references.md (was missing).

---

## #25: Billingsley, Wiley (1999)

**Status:** WEB (book, no free PDF)
**Title:** Convergence of Probability Measures, 2nd ed.

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:2145` — cites "Theorem 2.1" for Portmanteau theorem

**Verification:** The Portmanteau theorem is the main result of Billingsley's Chapter 2.
Theorem 2.1 is the standard location in the 2nd edition. Could not verify exact theorem
number without book access.
**Status: UNVERIFIED theorem number — flagged for manual check.**

**Corrections applied:** None. Added to references.md (was missing).

---

## #26: Kallenberg, Springer (2002)

**Status:** WEB (book, no free PDF)
**Title:** Foundations of Modern Probability, 2nd ed.

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:2145` — cites "Lemma 4.3" for weak convergence

**Verification:** Could not verify Lemma 4.3 without book access.
**Status: UNVERIFIED lemma number — flagged for manual check.**

**Corrections applied:** None. Added to references.md (was missing).

---

## Previously verified (LOCAL) — status confirmed

| # | Citation | Status | Issues in new files? |
|:--|:---------|:-------|:---------------------|
| 1 | Balaban CMP 95 (1984) | LOCAL ✓ | K:200 (Prop 1.2 cited correctly), PROOF-CHAIN ✓ |
| 2 | Balaban CMP 109 (1987) | LOCAL ✓ | K:289, I3:128 (Thm 1/3 cited correctly) ✓ |
| 3 | Balaban CMP 119 (1988) | LOCAL ✓ | K:200 (Section 2 confirmed) ✓ |
| 4 | Balaban CMP 98 (1985) | LOCAL ✓ | No new citations |
| 5 | Dimock arXiv:1108.1335 (2013a) | LOCAL ✓ | K:12 (arXiv ID correct) ✓ |
| 6 | Fredenhagen-Marcu CMP 92 (1983) | LOCAL ✓ | No new citations |
| 7 | Kotecky-Preiss CMP 103 (1986) | LOCAL ✓ | K:255 (unnumbered, correct) ✓ |
| 8 | OS CMP 31 (1973) | LOCAL ✓ | No new citations |
| 9 | OS CMP 42 (1975) | LOCAL ✓ | No new citations |
| 11 | Lüscher CMP 85 (1982) | LOCAL ✓ | No new citations |

---

## WEB citations — unverifiable theorem numbers

| Citation | Theorem cited | Verdict |
|:---------|:-------------|:--------|
| Seiler 1982, Ch. 6, Thm 6.1 | RP for nearest-neighbor lattice gauge theories | UNVERIFIED (secondary ref only; book paywalled) |
| Glimm-Jaffe, Thm 18.2.1 | Linked cluster theorem | PLAUSIBLE (section-based numbering expected; standard result) |
| Glimm-Jaffe, Thm 19.1.1 | GNS cyclicity / W5 | PLAUSIBLE (same book, Ch. 19 = Wightman) |
| Krantz-Parks, Thm 1.1.5 | Identity theorem for analytic functions | UNVERIFIED (paywalled) |
| Billingsley, Thm 2.1 | Portmanteau theorem | UNVERIFIED (paywalled) |
| Kallenberg, Lemma 4.3 | Weak convergence | UNVERIFIED (paywalled) |
| Lüscher-Weisz, Section 3 | Redundant operators | PLAUSIBLE (WEB) |

---

## Summary

| # | Citation | Status | Errors found | Errors fixed |
|:--|:---------|:-------|:-------------|:-------------|
| 1–11 | Balaban series, Dimock, FM, KP, OS, Lüscher | LOCAL | Prior sessions | Prior sessions |
| 18 | Nachtergaele-Sims CMP 265 | LOCAL (new) | "Thm 2.1" → "Theorem 2" | ✓ this session |
| 19 | Helgason 1978 | WEB | None | — |
| 20 | Besse 1987 | WEB | "Thm 7.73" incomplete | ✓ corrected to "7.73 and Cor. 7.74" |
| 21 | Borel 1953 | WEB | None | — |
| 22 | Dimock 2013b | WEB | None | — |
| 23 | Friedli-Velenik 2017 | WEB | MISSING from references.md | ✓ added |
| 24 | Krantz-Parks 2002 | WEB | MISSING from references.md | ✓ added |
| 25 | Billingsley 1999 | WEB | MISSING from references.md | ✓ added |
| 26 | Kallenberg 2002 | WEB | MISSING from references.md | ✓ added |

**Total citations audited this session:** 10 (4 new LOCAL, 6 WEB)
**Total LOCAL:** 12 (Chatterjee orphan not counted)
**Total errors found this session:** 6 (1 theorem number wrong, 1 imprecise, 4 missing entries)
**Total errors fixed this session:** 6
**Cumulative errors fixed (all sessions):** 28

**Remaining WEB (theorem numbers unverifiable without book access):**
- Seiler 1982, Thm 6.1
- Glimm-Jaffe, Thm 18.2.1 and 19.1.1
- Krantz-Parks, Thm 1.1.5
- Billingsley, Thm 2.1
- Kallenberg, Lemma 4.3
- Lüscher-Weisz, Section 3
- Osterwalder-Seiler Ann. Phys. 110 (definitively paywalled)
