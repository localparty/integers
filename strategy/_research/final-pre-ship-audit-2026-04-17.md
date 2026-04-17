# Final Pre-Ship Audit — 2026-04-17

## VERDICT: NEEDS-WORK

Two critical issues must be fixed before ship. Everything else is solid.

## Summary
- Items checked: 68
- PASS: 60
- FAIL: 3
- WARN: 5

---

## Per-section results

### 1. Comply-bare completeness

| Vertex | Exists? | Lines | Theorems (T/L/P/C) | Dated? | Named Walls? | PROVED (cb/pc) |
|--------|---------|-------|---------------------|--------|--------------|----------------|
| ym | PASS | 366 | 55 | 2026-04-14 | PASS (H4) | 9 / 18 |
| rh | PASS | 362 | 40 | 2026-04-14 | PASS (W1, W2) | 7 / 12 |
| bsd | PASS | 477 | 56 | 2026-04-14 | PASS (W_rank, W_nonCM, W_hK, W_Sha) | 14 / 10 |
| pvnp | PASS | 515 | 55 | 2026-04-14 | PASS (W1, W2, W3) | 26 / 1 |
| hodge | PASS | 412 | 37 | 2026-04-14 | PASS (W1, W2, W3) | 18 / 2 |
| ns | PASS | 470 | 33 | 2026-04-14 | PASS (W1-W4) | 16 / 3 |
| goldbach | PASS | 326 | 9 | 2026-04-16 | PASS (W_GB-1, W_GB-2) | 9 / 0 |
| collatz | PASS | 358 | 15 | 2026-04-16 | PASS (W_BC, W_L5, W_cyc) | 13 / 3 |

**Note on PROVED counts**: The comply-bare and PROOF-CHAIN files use "PROVED" differently. Comply-bare grep hits include status labels, inline references, and theorem verdicts. PROOF-CHAIN counts are strictly chain-link statuses. The counts are NOT mismatched — they measure different things. PASS.

**qg5d hub**: `strategy/proof-chain/qg5d/PROOF-CHAIN.md` EXISTS, 1038 lines, 36 numbered row items, 175 occurrences of "PROVED". Exceeds the 22-item threshold. **PASS**.

All 8 comply-bare files: **PASS** (exist, dated, walls disclosed, substantive content).

---

### 2. Atlas infrastructure

| Item | Result |
|------|--------|
| `strategy/x-ray/proof-chain/INDEX.md` | EXISTS, 23 vertex rows | 
| X-RAY.md file count | 25 files |
| INDEX vs X-RAY directory discrepancy | **FAIL** — `baum-connes` and `lehmer` have X-RAY.md files but are NOT listed in INDEX.md. INDEX has 23 rows; should have 25. |
| `visualization/atlas-torus/atlas-torus-data.js` | EXISTS, 2014 lines, 247 nodes across 25 unique vertices, 247 edges |
| `visualization/atlas-torus/ux-strategy-E-composition.html` | EXISTS |

**FAIL**: INDEX.md missing `baum-connes` and `lehmer` rows.

---

### 3. Section illustrations

| Item | Result |
|------|--------|
| File count in `visualization/illustrations/` | 9 HTML files (bsd, collatz, goldbach, hodge, integers, ns, pvnp, rh, ym) |
| All reference `atlas-torus-data.js` | YES — all 9 contain `<script src="../atlas-torus/atlas-torus-data.js">` |

**PASS**.

---

### 4. Root-level deliverables

| File | Exists? | Lines | Content verified? |
|------|---------|-------|-------------------|
| `LICENSE` | YES | 48 | Dual license (CC-BY 4.0 prose + MIT code). PASS. |
| `disclosure.md` | YES | 45 | AI collaboration transparency statement. PASS. |
| `reciprocity-notes.md` | YES | 58 | Fair attribution protocol. PASS. |
| `crosswalk.md` | YES | 94 | Programme-native to community-standard notation bridge. PASS. |

**PASS**.

---

### 5. Digital escrow

| Item | Result |
|------|--------|
| Encrypted file count | 13 (3 parts for file 01 + 4 parts for file 05 + 6 single files: 02, 03, 06-09) |
| ESCROW-MANIFEST.md | EXISTS, 145 lines |
| SHA-256 hashes — reconstructed files | 4 actual hashes (files 01, 02, 03, 05) |
| SHA-256 hashes — single files 06-09 | 4 actual hashes |
| SHA-256 hashes — per-part (01 and 05) | **WARN** — 7 per-part entries say "verify via `shasum -a 256`" instead of actual hash values. The reconstructed-file hashes ARE present and real. Per-part hashes are nice-to-have, not strictly required. |
| All files < 100 MB | YES — largest is 94,371,840 bytes (90.00 MB). Well under GitHub's 104,857,600-byte limit. |
| All files git-tracked | YES |
| File 04 absent | YES — intentionally excluded per manifest note. |

**WARN**: Per-part SHA-256 hashes are placeholder text, not actual values.

---

### 6. Strategy docs

| File | Exists? | Key content |
|------|---------|-------------|
| `strategy/north-star.md` | YES | §11 Risk Management present (§11.1-§11.4). PASS. |
| `strategy/atlas-torus-run.md` | YES | PASS. |
| `strategy/universal-approval-run.md` | YES | Self-Healing Log references found (34 hits). PASS. |
| `strategy/pillar-d/00-architecture.md` | YES | DERIVE-AND-OFFER architecture. PASS. |

**PASS**.

---

### 7. Tools

| File | Exists? |
|------|---------|
| `tools/RUN.md` | YES — explains both ORA v8 and verification-strategy tools. PASS. |
| `tools/ora-v8/01-the-prompt.md` | YES. PASS. |

**PASS**.

---

### 8. Sensitive file check

| Check | Result |
|-------|--------|
| `.zip` files | 0. PASS. |
| Email in filenames | 0. PASS. |
| `.env` / credentials / secrets | 0 git-tracked. 11 `.pem` files exist on disk in venvs but are NOT git-tracked (CA cert bundles in pip, harmless). PASS. |
| `etc/arxiv/` PII | **FAIL** — 4 git-tracked files contain third-party email addresses: `georges.obied@physics.ox.ac.uk` and `luis.anchordoqui@lehman.cuny.edu` appear in `etc/arxiv/arxiv.md`, `etc/arxiv/arxiv-submission-guide.md`, and `etc/arxiv/minimal-disclosure-email.md`. Publishing third-party email addresses without consent in a public Zenodo/GitHub release is a PII exposure risk. |

**FAIL**: `etc/arxiv/` contains third-party email addresses that will ship publicly.

---

### 9. .gitignore

| Entry | Present? |
|-------|----------|
| `.DS_Store` | YES (line 1: `**/.DS_Store`) |
| `__pycache__/` | YES (line 2) |
| `.playwright-mcp/` | YES (line 34) |
| `.venv` | YES (line 17: `**/.venv`) |
| `venv` directories | WARN — `venv/` (without dot prefix) is NOT in `.gitignore`. Currently safe because the existing `venv/` dirs under `integers/paper01-qg5d/code/*/` are excluded by other patterns (`paper1/code` on line 16), but a new `venv/` elsewhere would be unprotected. |

**WARN**: bare `venv/` not in `.gitignore` (currently mitigated by path-specific rules).

---

### 10. Overall repo health

| Metric | Value |
|--------|-------|
| Total files (disk, excl .git) | 43,452 |
| Git-tracked files | 2,385 |
| Total size | 1.6 GB |
| Files > 100 MB | 0. PASS. |
| Empty directories | 84 (all in `programme/ring-traversals/`). WARN — cosmetic only, git ignores empty dirs. |
| Git status | **WARN** — 4,038 staged changes pending (557 additions, 3,330 deletions, 10 modifications). The ship commit has NOT been made yet. |
| `solutions/` removed | YES. PASS. |
| `solutions-with-prize/` removed | YES. PASS. |
| Git LFS | Not in use. The 90 MB escrow parts are tracked as regular git objects. This will make the repo heavy for cloners. |

**WARN**: 84 empty directories in `programme/ring-traversals/`. Non-blocking (git won't track them).

---

## Critical issues (MUST fix before ship)

1. **`etc/arxiv/` contains third-party email addresses** (`georges.obied@physics.ox.ac.uk`, `luis.anchordoqui@lehman.cuny.edu`) in 4 git-tracked files. These are real academics who did not consent to having their email addresses published in a Zenodo archive. **Fix**: either redact the email addresses (replace with `[redacted]` or initials), move these 4 files out of the tracked tree, or add `etc/arxiv/` to `.gitignore`.

2. **INDEX.md missing 2 vertices**: `strategy/x-ray/proof-chain/INDEX.md` lists 23 vertices but 25 X-RAY.md files exist. `baum-connes` and `lehmer` are missing from the index table. **Fix**: add the 2 missing rows.

3. **ESCROW-MANIFEST.md per-part SHA-256 hashes are placeholders**: The 7 per-part entries for files 01 and 05 say `verify via shasum -a 256` instead of actual hex digests. The reconstructed-file hashes ARE real. **Fix**: run `shasum -a 256` on each `.part-*` file and fill in the actual hashes. This is the priority-lock moment — the hashes ARE the commitment.

---

## Warnings (CAN ship but should know about)

1. **Per-part escrow hashes** are placeholder text (item 3 above — elevated to critical).
2. **84 empty directories** in `programme/ring-traversals/` — cosmetic, git won't push them.
3. **`venv/` (without dot)** not in `.gitignore` — currently safe due to path-specific rules, but fragile.
4. **Ship commit not yet made** — 4,038 staged changes pending.
5. **No Git LFS** for 90 MB escrow parts — repo will be heavy for cloners (~1.6 GB).

---

## Recommendations

1. Fix the 3 critical issues above before committing.
2. Consider adding `**/venv/` to `.gitignore` for robustness.
3. Consider Git LFS for the digital-escrow parts if cloning speed matters.
4. The goldbach and collatz comply-bare files are honest about their low confidence (1/10 and 4/10 respectively). This is correct behavior — do not inflate.
5. After fixing criticals, make the ship commit, verify with `git status`, then proceed to Zenodo.
