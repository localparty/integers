# rh-comply-bare — Critic Attacks (run-03)

*Critic pass on the author draft of `rh-comply-bare.md`. Each attack maps to an arbiter disposition in `arbiter-decisions.md`.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Attack catalogue

### A-1 — Prose-paragraph discipline

**Attack**: are any sections disguising prose as theorem scholia / remarks / proof sketches?

**Target passages**:
- §13 Remark 13.2 (Littlewood optimality)
- §14 Theorem 14.1 enumerated items (i), (ii), (iii)
- §15.2 parenthetical pending-X-Ray note
- §17.4 "inherited" paragraph

**Critic judgment**: all target passages are single-line citations or enumerations within theorem/remark frames; none form prose paragraphs. §17.4 uses a semicolon-separated classical list, not prose discussion. PASS.

### A-2 — Uncited claim hunt

**Attack**: scan every theorem / corollary / definition for missing programme citation.

**Findings**: every theorem, definition, and remark has a citation in parentheses to paper13 §LX or to an external reference (Bombieri / Edwards / Titchmarsh / arXiv:2511.22755). Classical theorems (5.1, 6.1, 13.1) cite Bombieri §I + Edwards/Titchmarsh. External theorem (7.1) cites arXiv:2511.22755. Chain theorems (8.1, 9.1a-d, 10.1-3, 11.1, 12.1-2) cite paper13 §LX. Supporting theorems cite paper13 §SX.

**Critic judgment**: 0 uncited claims. PASS.

### A-3 — W1 DELTA-10 field completeness

**Attack**: all 12 DELTA-10 fields present for W1?

**Findings**: §10 table contains 12 rows labelled 1-12, covering name, location, statement, status, external citation, bypass route, bypass citation, aggregate confidence, journal-accept effect, retract effect, audit pending, §5d compliance/standing.

**Critic judgment**: all 12 fields present; formatted clearly. PASS.

### A-4 — §3 Requirements Map consistency with run-02 LOCKED

**Attack**: does §3 reproduce the run-02 verdict distribution?

**Spot-check**:
- Req 1 OPEN-BUT-ADDRESSED: run-02 ✓ (L1 O, L5 Pa, L6 O)
- Req 2 PARTIAL via L6: run-02 ✓ (only non-SILENT cell for Req 2 is L6 Pa)
- Req 3 PARTIAL via L5 + L6: run-02 ✓ (L5 Pa, L6 Pa)
- Req 4 PROVED L1 + L6: run-02 ✓ (L1 P, L6 P; Pa at L4c, L5)
- Req 5 PROVED L3d + L6: run-02 ✓ (L3d P, L6 P; Pa at L5, S1)
- Req 6 SILENT column / DEFERRED-STRENGTHENING: run-02 ✓ (optional; paper13b Phase 5 cross-ref)
- Req 7 PASS via L2 P + L6 Pa: run-02 ✓

**Critic judgment**: Requirements Map table matches run-02 LOCKED exactly. PASS.

### A-5 — §5d compliance trace

**Attack**: does the document show §5d-compliance for every Core Bombieri requirement (1-5)?

**Findings**: §3 table's "Verdict" and "Addressing layers" columns collectively show every Core req has $\geq 1$ non-SILENT cell. §15.3 compliance-map summary explicitly states "§5d compliance: PASS on every Core 1-5 requirement."

**Critic judgment**: §5d explicitly traced. PASS.

### A-6 — Page count ≤ 15

**Attack**: is the document ≤ 15 pages?

**Measurement**: ~310 lines of markdown content (excluding blank lines / separators). At typical LaTeX-render density of 35-45 lines per page, $\Rightarrow$ ~7-9 pages rendered. Well under 15.

**Critic judgment**: PASS. Document is on the compact end of the target window (room for minor expansion if needed downstream, but bare-discipline-compliant as-is).

### A-7 — External citation discipline

**Attack**: is arXiv:2511.22755 the ONLY external citation used?

**Scan**: document cites Bombieri, Edwards, Titchmarsh, von Mangoldt, Littlewood, Selberg, Levinson, Conrey, van de Lune-te Riele-Winter, Odlyzko, Teschl, Davis-Kahan, Boegli-Siegl-Tretter, Rellich-Kondrachov — but all classical and inherited via §17.4 programme-bibliographies convention (brief DELTA 8: "programme papers cited at §-level; external references inherited via programme bibliographies"). Only arXiv:2511.22755 receives direct cite-with-location treatment, and is flagged EXTERNAL every time.

**Critic judgment**: PASS. Discipline respected: arXiv:2511.22755 is the only directly-cited external (with EXTERNAL marker); classical are inherited-through-programme-bibliography per DELTA 8.

### A-8 — Main Theorem and QED coherence

**Attack**: does Theorem 2.1 (Main) exactly track Theorem 12.1 (QED)?

**Comparison**:
- T 2.1: $\mathrm{spec}(D_\infty) = \{\gamma_n\} \subset \mathbb{R}$; non-triv zeros on $\Re = \tfrac{1}{2}$; OPEN-BUT-ADDRESSED conditional on W1.
- T 12.1: $\mathrm{spec}(D_\infty) = \{\gamma_n\} \subset \mathbb{R}$ (self-adjointness + Hurwitz + spectral exactness); FE symmetry converts to Re = 1/2; conditional on W1.

**Critic judgment**: T 2.1 = T 12.1 (restated). PASS.

### A-9 — W2 RESOLVED transparency

**Attack**: is W2 (CF uniformity caveat) listed with full disclosure even though RESOLVED?

**Findings**: §16.2 contains an 8-row table for W2 — name, location, original statement, status (RESOLVED), resolution mechanism, resolution citation, retention rationale, chain-effect, audit status.

**Critic judgment**: full transparency per DELTA 10 "retained in disclosure." PASS.

### A-10 — Dependency graph completeness

**Attack**: does §15.1 include all 14 rows (L1-L6 + L3a-d + L4a-c + S1-3)?

**Findings**: graph includes L1, L2, L3a, L3b, L3c, L3d, L4a, L4b, L4c, L5, L6, S1, S2, S3 — 14 nodes.

**Critic judgment**: complete. PASS.

### A-11 — Bare-mode vs §14 numerical enumeration

**Attack**: does §14's enumeration (i)(ii)(iii) count as prose?

**Inspection**: items are theorem-content (facts + attributions), separated by line breaks inside a `Theorem 14.1` block; no connective prose, no "we observe that," no narrative. Format matches DELTA 3 permitted structure (numbered / bulleted facts within theorems).

**Critic judgment**: PASS. Enumeration of facts inside a theorem statement is bare-mode compliant (same convention as §1 Bombieri formal setup bullets and YM §10 AF-match factual-list inside Theorem 10.1).

### A-12 — Ambiguity on Req 2 verdict class

**Attack**: §3 lists Req 2 as PARTIAL (via L6 Pa) and cites "classical Riemann-von Mangoldt." Is this §5d-addressed?

**Reasoning**: run-02 commit-memo.md explicitly states Req 2 §5d PASS (1 non-SILENT cell L6 Pa). The Pa cell is anchored in paper13 §L6 + Bombieri §I classical equivalence. §13 Theorem 13.1 provides the explicit theorem statement + classical-citation. Addressing is explicit, not silent.

**Critic judgment**: PASS. Req 2 is §5d-addressed at PARTIAL class; appropriate per Bombieri §I classical treatment.

---

## Summary

12 attacks executed; 12 PASS. 0 WEAKEN, 0 STRENGTHEN, 0 KILL. Author-draft discipline intact.

**Hand-off to arbiter**: proceed to `arbiter-decisions.md` for PUBLISH-READY vs NEEDS-REVISION verdict.

---

*End critic-attacks.*
