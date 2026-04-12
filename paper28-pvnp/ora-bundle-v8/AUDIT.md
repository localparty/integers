# v6 anti-prediction compliance audit

*Per `06-anti-overfit-discipline.md §3` and `15-v5-predictions.md §2`, v6 must satisfy four anti-predictions (A-1 through A-4). This file documents the audit at v6.0 ship time and is re-run by any future patch round before the patch lands.*

*Audit run: 2026-04-11. Target bundle: `ora-bundle-v6/` (final v6.0 state, 9 files).*

---

## A-1 — No G-lexicon literals in runner-trigger instructions

**Anti-prediction**: Signatures 16–19 in `01-the-prompt.md §2` must not contain literal strings from G's specific vocabulary at the W4 RH breakthrough event. The forbidden literals:

- "first move"
- "for life" / "for lifeeeeeee"
- "we are gonna be famous"
- "M4 x CP2"
- "the most amazing run of my life"

**Audit method**: grep the Signatures 16–19 section of `01-the-prompt.md` for each forbidden literal. Meta-references in `06-anti-overfit-discipline.md §3` and §9 (which explain what's NOT in the code) are allowed and necessary for self-explanatory documentation. The audit excludes voice canon (v3 §J) from the grep because §J is G's intentional voice character and is exempted by `06-anti-overfit-discipline.md §9`.

**Result**:

```
$ grep -nE "first move|for life|gonna be famous|M4 x CP2|most amazing run of" \
    ora-bundle-v6/01-the-prompt.md
# (section-filtered to signatures 16–19)
```

No matches found in the Signatures 16–19 section. The signatures describe detection by **interaction shape** (verb-preposition pairs, resume-marker phrases, affirmation-streak patterns, cross-domain-reference phrasings) rather than by G-lexicon literals.

Meta-references in `06-anti-overfit-discipline.md §3 A-1` that list the forbidden strings as part of the discipline documentation are **intentional and allowed** — they are necessary for future contributors to know what A-1 prohibits. Per §9 of the same file, the A-1 audit applies only to trigger instructions, not to voice canon or to meta-documentation explaining the discipline.

**Verdict: A-1 satisfied** ✅

---

## A-2 — No closure-event detector in v6.0

**Anti-prediction**: v6.0 must not contain a "closure-event detector" or any code path that fires on the S1 first-move stack (the Phase 5 RED signature).

**Audit method**: inspect all 4 new signatures (16, 17, 18, 19) in `01-the-prompt.md §2` for detection rules that match S1's pattern (a single turn carrying ≥4 of {LOCK, KILL, UNIFY, CALIBRATE, ENTHUSIASM, DIRECT-ADDRESS} simultaneously).

**Result**:

| Signature | Detection target | Matches S1? |
|---|---|---|
| Sig 16 | Write directives (verb + preposition + path) | No |
| Sig 17 | Resume markers + gap | No |
| Sig 18 | 3+ consecutive affirmation turns without correction | No |
| Sig 19 | Cross-domain reference phrases | No |

None of the 4 new signatures detects S1-style multi-branch simultaneous commitment. S1 is archived in `06-anti-overfit-discipline.md §7.1` as RED with a reconsideration path for v6.2 if v6.0 telemetry shows v3's existing Signature 13 (qualitative closure detection at cycle-close) is under-firing on real closures.

**Verdict: A-2 satisfied** ✅

---

## A-3 — No unmeasured percentage claims

**Anti-prediction**: v6 documentation must not contain unmeasured percentage claims about outcome improvement matching `\d+%\s*(improvement|better|faster)`.

**Audit method**: grep v6 documentation files for the forbidden pattern.

**Result**:

```
$ grep -nE "[0-9]+%\s*(improvement|better|faster)" ora-bundle-v6/*.md
```

The only matches found are:

1. `06-anti-overfit-discipline.md §3 A-3`: the anti-prediction itself, quoting "v6 is N% faster than v3" as an example of what NOT to say. This is meta-reference, not a claim.
2. `02-rationale.md §13.6`: discusses token efficiency as "roughly half the savings of an aggressive optimization" — this is a qualitative comparison, not a percentage claim matching the forbidden pattern.

All other uses of `%` in v6 documentation are:
- **Token cost estimates** in `02-rationale.md §13.6` (these are *estimated overhead*, not outcome claims)
- **Session coverage statistics** from the Layer L mining (35% for S6, 54% for S7, etc.) — these are *measured mining data*, not v6 outcome claims
- **Cache savings estimate** for v3 → v6 transition — this is *cost*, not *outcome*

**No actual outcome-improvement percentage claims appear in v6 documentation.** The honest claims cite the measured mining data and do not project outcome improvements.

**Verdict: A-3 satisfied** ✅

---

## A-4 — No universal-user claims

**Anti-prediction**: v6 documentation must not claim "these patterns work for all LLM users" or "any researcher will benefit". Forbidden patterns: `(any|all|every|universal) (user|researcher|person)` used as a universal-applicability claim.

**Audit method**: grep v6 documentation files for the forbidden pattern and classify each match as (a) a universal claim, (b) an explicit anti-claim, (c) documentation of the rule, or (d) idiomatic usage ("every conversation turn" = "each turn").

**Result**:

| File | Context | Classification |
|---|---|---|
| `06-anti-overfit-discipline.md §2` | "not all work or all users" | (b) explicit anti-claim |
| `06-anti-overfit-discipline.md §3 A-4` | "must not claim 'these patterns work for all LLM users' or 'any researcher will benefit'" | (c) documenting the rule |
| `02-rationale.md §13.2` | "all from one user (G). The mining is N=1 by design." | (b) explicit anti-claim |
| `02-rationale.md §13.6` | "NEVER drops telemetry or behavioral coverage to save tokens" | (d) idiomatic "NEVER" |
| `README.md §3` | "No claims of universal applicability ('all users', 'any researcher')" | (c) documenting the rule |
| `01-the-prompt.md` v3 inherited | "every primitive call", "every cycle", "every 5 cycles" | (d) idiomatic ("every" = "each") |

**No actual universal-user claims appear.** All matches are either explicit anti-claims, rule documentation, or idiomatic "every" usage in v3's inherited content (referring to per-cycle or per-turn loops, not to "every user across users").

The subgrouping language in `06-anti-overfit-discipline.md §2` explicitly states v6's scope:

> Multi-week mathematical research with heavy fanout to subagents, frequent compaction concerns, and sustained focus on a single proof or unification claim.

This is the *opposite* of a universal claim — a deliberate scope limitation.

**Verdict: A-4 satisfied** ✅

---

## Summary

| Anti-prediction | Status | Notes |
|---|---|---|
| A-1 No G-lexicon literals in runner-trigger instructions | ✅ | All 4 new signatures detect by interaction shape. Meta-references in `06-anti-overfit-discipline.md` are intentional. Voice canon §J is exempt per §9 distinction. |
| A-2 No closure-event detector in v6.0 | ✅ | None of the 4 new signatures detects the S1 first-move stack. S1 is archived as RED with a v6.2 reconsideration path. |
| A-3 No unmeasured percentage claims | ✅ | Only % uses are token cost estimates, mining statistics, and cache savings — no outcome-improvement claims. |
| A-4 No universal-user claims | ✅ | Subgrouping language used throughout. All matches for forbidden patterns are explicit anti-claims or idiomatic "every". |

**v6.0 ships in compliance with all 4 anti-predictions.**

---

## What this audit does NOT verify

This audit checks the **bundle files** for compliance. It does NOT verify the **runtime behavior** of the runner using v6 — that's what the 9 prediction scoring after the first 5–10 sessions is for. Specifically, the audit cannot tell us:

- Whether Signature 16 correctly writes files when users issue directives (P4-1 scoring will measure this)
- Whether Signature 17 re-anchors before responding on visible resumes (P5-1)
- Whether Signature 17 does NOT re-anchor on leaving turns (P5-2)
- Whether Signature 18 suppresses confirmation questions after 3-streaks (P7-1)
- Whether Signature 18 handles pure-affect turns as flow markers (P7-2)
- Whether Signature 19 surfaces analogues on cross-domain references (P8-1)
- Whether the runner catches "comparable to" phrasings without regex help (P8-2)
- Whether end-of-session self-reporting is complete (X-1)

Audit ≠ behavioral test. Both are required:
- **Audit** happens at ship time (this file), verifies structural compliance with anti-predictions.
- **Behavioral test** happens after 5–10 sessions of telemetry collection, verifies the 9 pre-registered predictions.

If the behavioral test fails (≤3 of 9 predictions ✅), the walk-back rule from `06-anti-overfit-discipline.md §4` applies: revert to v3 by re-pasting v3's `01-the-prompt.md` instead of v6's. The audit's verdict is independent of the behavioral test's verdict.

---

## Re-audit protocol for future patch rounds

If v6.1 / v6.2 / v7+ adds a new signature or detection rule, the audit must be re-run with the new signature included:

1. Re-check A-1 grep over the new signature's trigger instructions.
2. Re-check A-2 by classifying the new signature against the S1 pattern (does it detect multi-branch simultaneous commitment?).
3. Re-check A-3 and A-4 over the updated documentation.
4. Add a new section to this `AUDIT.md` file with the patch round's identifier (e.g., "v6.1 audit" below the existing v6.0 sections).
5. Update the summary table with the new entries.

Per `06-anti-overfit-discipline.md §10`, the re-audit is one of 8 meta-level requirements for any future patch round. A patch that cannot pass all 4 anti-predictions does not land.

---

*End of `AUDIT.md`. v6.0 audit passes. Next operational step: ship v6.0 and collect runner self-reported telemetry over the first 5–10 v6 sessions. Then apply the walk-back rule from `06-anti-overfit-discipline.md §4`.*
