# Syntax Repair Run — Papers 1 and 2: Backtick → Dollar Migration

*Delegated run. You are a Claude Code instance dispatched to migrate Papers 1 and 2 from backtick-fenced math (the legacy convention) to standard dollar-sign math (the convention going forward). This is Phase 1 of a two-phase tooling upgrade. Phase 2 (a full adversarial md→LaTeX converter) will be built separately and assumes clean standard markdown as input.*

*You run autonomously. Dispatch parallel workers when helpful. Do not pause to ask "should I continue?" — the cycle runs until the migration is complete and verified, or a hard wall is named honestly.*

---

## 1. Mission

Migrate every math-fenced backtick expression in Papers 1 and 2 to standard dollar-sign math, **preserving the Unicode content inside unchanged**. Actual code expressions (file paths, command names, inline code) stay as backticks. Then verify both papers still compile to PDF with zero errors, zero undefined citations — matching the current baseline.

**Core rule**: delimiter substitution only. No content rewriting, no Unicode-to-LaTeX conversion at the source level. That's the converter's job, not this migration's.

**Examples of correct migrations**:

| Before | After |
|---|---|
| `` `Ω_DM/Ω_b ≈ 5` `` | `$Ω_DM/Ω_b ≈ 5$` |
| `` `α² + β² = 1` `` | `$α² + β² = 1$` |
| `` `N_eff` `` | `$N_{eff}$` (wait — see §4 edge cases) |
| `` `pdflatex main.tex` `` | `` `pdflatex main.tex` `` (unchanged — code) |
| `` `build.sh` `` | `` `build.sh` `` (unchanged — filename) |

---

## 2. Context — what's been decided

The framework has four Millennium-class papers in the pipeline (YM, RH, BSD, P vs NP) plus companion papers (23, 24, 25). All future papers will use **standard markdown math fencing**: `$...$` inline, `$$...$$` display. Unicode is allowed inside the dollars (e.g., `$Ω_DM ≈ 5$` is valid, not `$\Omega_{DM} \approx 5$`). The existing converter at `/Users/gsix/quantum-geometry-in-5d-latex/etc/md2latex.py` has a 100+ entry Unicode→LaTeX mapping table and handles the translation at conversion time.

**Why the migration**: the original convention for Papers 1 and 2 used backticks to fence math (because the author's converter keyed on backticks). But backticks mean "inline code" in standard markdown — so the sources render wrong on GitHub, Typora, Jupyter, and everywhere else. Migration to standard dollar-sign math fixes this permanently.

**Why now**: Papers 1 and 2 will be republished via Zenodo → GitHub → arXiv per `publishing/release-channels.md`. GitHub-rendered markdown must look correct. Dollar-sign math renders correctly everywhere.

---

## 3. Scope — exact file set

### 3.1 Paper 1 files (migrate)

Location: `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/`

Files to migrate (backtick counts from preliminary survey):
- `preprint/00-abstract.md` (~46 backticks)
- `preprint/01-introduction.md`
- `preprint/02-framework.md` (~54)
- `preprint/03-five-phenomena.md` (~78)
- `preprint/04-aharonov-bohm.md` (~39)
- `preprint/05-spin-statistics.md` (~70)
- `preprint/06-gravity-bridge.md` (~32)
- `preprint/07-quantization-bridge.md` (~27)
- `preprint/08-connections.md` (~73)
- `preprint/09-philosophy.md`
- `preprint/10-conclusion.md` (~27)
- `preprint/11-figures-list.md` (~23 — but these are likely mostly legitimate filename backticks; inspect carefully)
- `appendices/*.md` (26 appendices A through Z — walk the directory)

### 3.2 Paper 2 files (migrate)

Location: `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper02-cosmology/`

- `preprint/00-abstract.md` (~63 backticks)
- `preprint/01-introduction.md` (~45)
- `preprint/02-sections-2-to-7.md` (~341 — the biggest file, highest density)
- `preprint/03-conclusion.md` (~38)
- `preprint/04-figures-list.md` (~23 — likely mostly filenames)
- `appendices/*.md` (9 appendices A through I)

### 3.3 Explicitly EXCLUDED from migration

Do NOT touch these — they are documentation / tooling files, not paper content:
- `integers/paper01-qg5d/etc/*.md` (e.g., `01-journal-referee.md`, `hostile-reviewer.md`, `latex-conversion-for-arxiv.md`)
- `integers/paper02-cosmology/etc/*.md` (same)
- Any file under `integers/paper01-qg5d/journals/`, `integers/paper02-cosmology/camb/`, `reviewer-runs/`, `journal-reviewer/`
- Any `.tex`, `.bib`, `.py`, `.sh`, or non-`.md` file
- Any markdown file that is NOT in `paperN/preprint/` or `paperN/appendices/`

### 3.4 Verify scope before migrating

First action: run a survey script that lists every `.md` file in the Paper 1/2 preprint and appendices directories, counts backticks per file, and samples the patterns. Confirm the scope matches §3.1-3.2 above. If you find files I missed or files I included that shouldn't be (e.g., subdirectories of `preprint/` with sub-files), adjust and note the adjustment in your log.

---

## 4. The migration rule (precise)

For each file in scope:

1. **Parse line by line** (preserve line structure — don't reformat).

2. **Find every single-backtick pair** `` `X` `` on each line (use a regex like `` `([^`]+)` ``, non-greedy).

3. **Classify the content `X` as math or code** using the logic from `/Users/gsix/quantum-geometry-in-5d-latex/etc/md2latex.py` lines 691-699 (the `code_replace` function's classifier):

   ```python
   def is_math(content: str) -> bool:
       # math triggers
       math_chars = r'[αβγδεζηθικλμνξπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ∂∇∫∮∞ℏ†√×·≈≠≤≥≡∈∝±∓⊗⊕⟨⟩≪≫ℝℤℂℕ]'
       operators = r'[=+*/^_-]'
       # code signals (not math):
       code_hints = ['pdflatex', 'bibtex', '.sh', '.py', '.md', '.tex', '.bib',
                     'http://', 'https://', '/Users/', '--', 'www.',
                     'git ', 'ls ', 'cd ', 'bash ']
       if any(hint in content for hint in code_hints):
           return False
       if re.search(math_chars, content):
           return True
       if re.search(operators, content):
           # But exclude comparisons like `1-2-3` in references or file versions
           if re.match(r'^[\w\.\-]+$', content):
               return False
           return True
       return False
   ```

4. **If math**: replace `` `X` `` with `$X$`. **Do not modify `X` itself.** Preserve every Unicode character, every subscript, every space exactly as written. The converter will handle Unicode→LaTeX at conversion time.

5. **If code**: leave the backticks untouched. `` `X` `` stays as `` `X` ``.

6. **If ambiguous** (classifier returns unclear, or edge case not covered): **flag for manual review**. Write the file path + line number + content to a review log at `drafting/syntax-repair-review-log.md`. Do NOT guess. When in doubt, leave the backticks alone and flag.

### Edge cases to handle explicitly

- **`` `N_eff` `` and bare-subscript-word patterns**: these are math (`N` subscript `eff`). Migrate to `$N_{eff}$`. The classifier catches this via the `_` operator test. But note: the converter itself handles the `_{...}` wrapping at conversion time; you're only migrating the delimiter. So `` `N_eff` `` → `$N_eff$` is correct (dollar signs, underscore preserved as-is).

- **Display math (4-space indented equation blocks)**: these are NOT backtick-fenced. They're indented blocks. Migrate them to `$$...$$` blocks:
  ```markdown
      P(↑_â, ↑_b̂) = ½ sin²(θ/2)
  ```
  becomes
  ```markdown
  $$P(↑_â, ↑_b̂) = ½ sin²(θ/2)$$
  ```
  Detect these via 4-space indentation on a blank-line-bounded block AND containing math characters. Ambiguity risk: 4-space indented markdown could also be code. Use the same math/code classifier; if math, migrate; if code, leave alone.

- **Double-backtick spans** `` `` ... `` ``: unusual in the papers per git archaeology, but if present, leave alone and flag for manual review (the converter doesn't handle them anyway).

- **Math with existing backticks inside** (like `` `f(`x`)` ``): shouldn't exist but if found, flag and skip.

- **File/variable names that contain Greek letters or operators** (like `` `α.py` `` or `` `x+y.txt` ``): the classifier will misfire. Use the code_hints list (`.py`, `.txt`, etc.) to catch these. Extend the list if you find new extensions.

- **Figures-list files** (`11-figures-list.md`, `04-figures-list.md`): inspect carefully. Most backticks here will be legitimate filenames (e.g., `` `fig_summary.png` ``) and should NOT be migrated. The classifier's code_hints should catch these, but manual review of these specific files is wise.

---

## 5. Approach

### 5.1 Phase 1a — Survey (first 15 min)

Before writing any migration code, run a survey:

1. Walk the scope directories. List every `.md` file.
2. For each file: count backticks, sample 3-5 backtick-fenced spans, classify them preliminarily (math/code/ambiguous).
3. Write the survey to `drafting/syntax-repair-survey.md` with:
   - Total file count
   - Total backtick span count (estimated)
   - Top 5 files by span count
   - ~20 sample spans with classification
   - Any edge case patterns you didn't anticipate in §4

4. Review the survey. If anything surprises you, update the migration rule (§4) before proceeding.

### 5.2 Phase 1b — Write the migration script (30 min)

Write a Python script at `/Users/gsix/quantum-geometry-in-5d-latex/etc/backtick-to-dollar.py`.

Requirements:
- Takes a list of input files (argument or glob pattern)
- For each file: applies the migration rule from §4
- Writes the migrated content back to the SAME path (in-place)
- Also writes a per-file log: `drafting/syntax-repair-logs/<filename>.log` with:
  - Count of spans examined
  - Count migrated to $...$
  - Count left as `...`
  - List of flagged ambiguous spans (line number + content)
- DOES NOT modify files on dry-run mode (`--dry-run` flag)

Test the script on ONE file first (e.g., `integers/paper01-qg5d/preprint/00-abstract.md`), dry-run. Inspect the diff. If it looks right, apply in-place and inspect the file. If the file looks right, continue.

### 5.3 Phase 1c — Run migration on all scope files

Dispatch the script against the full scope in parallel where possible. Keep per-file logs. Commit the working tree to a separate git branch (`syntax-repair-migration`) BEFORE running in-place, so there's a rollback option if something goes wrong.

### 5.4 Phase 1d — Verify compilation

**This is the critical verification step.** Both papers must still compile with zero errors and zero undefined citations after migration.

1. `cd /Users/gsix/quantum-geometry-in-5d-latex`
2. Run `bash build.sh` (the existing build pipeline). This regenerates `.tex` from migrated `.md` via `md2latex.py`, then runs pdflatex+bibtex.
3. Parse the output for errors.
4. If zero errors, zero undefined citations → **VERIFICATION PASS**. Record in `drafting/syntax-repair-verification.md` with exact build log excerpts.
5. If errors: **self-heal.** The converter might not handle `$Unicode$` as well as it handled `` `Unicode` ``. In that case:
   a. Identify the specific error pattern (likely: converter not translating Unicode inside `$...$` because its code path was keyed on backticks).
   b. Patch `md2latex.py` to also translate Unicode inside `$...$` regions. Specifically: the `convert_unicode_in_math()` function should run on dollar-fenced content the same way it ran on backtick-fenced content.
   c. Re-run build. Re-verify.
   d. Log the patch in `drafting/syntax-repair-converter-patches.md`.

### 5.5 Phase 1e — Byte-level PDF comparison (optional but recommended)

If you have `diff-pdf` or equivalent available, compare the pre-migration PDF to the post-migration PDF. The text content should be effectively identical (same equations, same formatting) even though the source changed. Small differences (spacing, kerning) are acceptable. Content differences are a regression and need investigation.

If `diff-pdf` is not available, sample 5-10 specific pages from each paper and do a visual diff (open both PDFs, check the equations render identically).

---

## 6. Deliverables

When the run completes, these files must exist:

1. `drafting/syntax-repair-survey.md` — the Phase 1a survey
2. `/Users/gsix/quantum-geometry-in-5d-latex/etc/backtick-to-dollar.py` — the migration script
3. `drafting/syntax-repair-logs/*.log` — per-file migration logs
4. `drafting/syntax-repair-review-log.md` — flagged ambiguous spans
5. `drafting/syntax-repair-verification.md` — compilation verification report
6. `drafting/syntax-repair-converter-patches.md` — if any converter patches were needed during verification
7. `drafting/syntax-repair-closure.md` — final summary with: total spans migrated, total flagged, compilation status, any gotchas found, recommendations for Phase 2
8. All Paper 1/2 markdown sources migrated in-place (git-tracked on the `syntax-repair-migration` branch)

---

## 7. Success criteria

The run succeeds if ALL of:

1. Every file in §3.1-3.2 has been processed.
2. Every math-backtick span has been migrated to `$...$` or explicitly flagged.
3. Every code-backtick span has been preserved (no false-positive migrations).
4. `bash build.sh` completes with zero errors and zero undefined citations for both papers.
5. PDFs render identical equation content to the pre-migration baseline (sampled visual diff).
6. The ambiguous-span flag log is small (< 50 total flags across both papers is a reasonable target).
7. All deliverables from §6 exist.

If ANY of these fail:
- Clearly name which one failed.
- Write the root cause to `drafting/syntax-repair-closure.md`.
- Mark the programme as HONEST-STALL with the named blocker.
- Do NOT silently proceed past a failure. The stall is a legitimate outcome if something fundamental is wrong.

---

## 8. Reference files (read as needed)

| File | What it is |
|---|---|
| `/Users/gsix/quantum-geometry-in-5d-latex/etc/md2latex.py` | Main converter. Lines 691-699 have the classifier logic to reuse. |
| `/Users/gsix/quantum-geometry-in-5d-latex/etc/unicode2math.py` | The Phase 0 backtick-insertion script (the opposite of what you're doing). Reference for token classification logic. |
| `/Users/gsix/quantum-geometry-in-5d-latex/etc/md2latex-recipe.md` | The author-facing recipe explaining the backtick convention. Will need updating to document the new dollar-sign convention after migration. |
| `/Users/gsix/quantum-geometry-in-5d-latex/build.sh` | The 44-line build pipeline. Run this for verification. |
| `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/etc/arxiv/main.pdf` | The pre-migration Paper 1 PDF (1406+ pages). Your baseline. |
| `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper02-cosmology/etc/arxiv/paper2.pdf` | The pre-migration Paper 2 PDF (60 pages). Your baseline. |

---

## 9. Operating discipline

- **Autonomous**: run cycles without pausing for confirmation. No "should I continue?" questions. The brief IS the authorization.
- **Parallel when possible**: if you can migrate multiple files simultaneously (each is independent), do it.
- **Self-healing**: if the migration breaks compilation, diagnose and patch the converter. Log the patch. Continue. Do not stop and wait for input.
- **Honest-first**: if the rule in §4 turns out to be wrong for some edge case, flag it and adjust the rule — don't silently force through. Update §4 in your migration log to document the adjustment.
- **Conservative on ambiguity**: when in doubt, leave the backticks alone and flag. It's better to have 50 manual reviews than 50 silently-wrong migrations.
- **Preserve content**: the Unicode inside the dollars is the author's text. Never modify it. Delimiter-only substitution.

---

## 10. What this run does NOT do

- It does NOT build the full md2tex-adversarial tool (that's Phase 2, a separate run)
- It does NOT convert Unicode to LaTeX commands at the source level (the converter does that at build time; keep sources Unicode-legible)
- It does NOT touch Papers 3-28 (they use a different convention or are not yet drafted)
- It does NOT modify `md2latex.py` unless Phase 1d verification fails and a patch is required
- It does NOT introduce new fencing conventions — pure backtick-to-dollar delimiter substitution per §4
- It does NOT reformat, rewrap, or clean up the markdown beyond the delimiter swap

---

## 11. Closing

When the YM proof chain verification run finishes (~3 hours from the time this is launched), the framework's first big delivered artifact lands. This syntax-repair run prepares Papers 1 and 2 so they can be republished alongside it — under the Zenodo → GitHub → arXiv channel strategy in `publishing/release-channels.md`.

Papers 1 and 2 were the framework's first two outputs. Getting their sources into standard-markdown shape is the last step before they're ready to ship through the new pipeline. The backtick mess is what's standing in the way. Clean it up. Verify it compiles. Ship.

Begin.
