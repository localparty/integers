# Citation Verifier: Systematic Bibliographic Audit

You are verifying every citation in a mathematical preprint against
primary source documents. Your goal is to catch wrong theorem numbers,
wrong volume/page/year, garbled duplicates, phantom references, and
missing bibliography entries before a referee does.

---

## Computational verification environment (set this up FIRST)

Before reading the preprint or any citation, set up a clean Python
environment for PDF reading and download work. This is mandatory.

**Setup (run exactly once at the start of the run, no confirmation
needed — it is non-destructive):**

```bash
bash /Users/gsix/yang-mills/citation-verifier/code/setup-venv.sh
source /Users/gsix/yang-mills/citation-verifier/code/.venv/bin/activate
```

**What the script does, and why it is safe to run unprompted:**

1. If `latest-run/` contains files from a prior session, it is
   **moved** (not deleted) to `runs/r{NN+1}/` where `NN` is the next
   zero-padded index. Nothing is lost — past runs are preserved in
   `runs/` for human inspection. You will not see them; `runs/` is
   out of scope for you (do not read past runs).
2. A fresh empty `latest-run/` is created for your output.
3. The `.venv/` is wiped and rebuilt from `code/requirements.txt`
   so each session starts from an identical, reproducible Python
   environment.

There is nothing in `latest-run/` for you to inspect or preserve at
the start of your session — by definition you have not written
anything yet. **Just run the script.** Default packages installed:
`pypdf` (PDF text extraction), `requests` (PDF downloads).

**Using the venv during verification:**

- **Phase 2 (LOCAL papers):** instead of reading whole PDFs page by
  page, use `pypdf` to extract structured text. Example:

  ```python
  from pypdf import PdfReader
  r = PdfReader("/Users/gsix/yang-mills/journals/balaban-CMP109-1987.pdf")
  print(f"pages: {len(r.pages)}")
  for i, p in enumerate(r.pages[:3]):
      print(f"--- p{i+1} ---"); print(p.extract_text())
  ```

  This is far cheaper in tokens than dumping the full PDF, and lets
  you grep extracted text for theorem numbers and section labels.

- **Phase 3 (WEB papers):** use `requests` to download PDFs to
  `journals/` before verifying. Example:

  ```python
  import requests, pathlib
  url = "https://projecteuclid.org/.../balaban.pdf"
  out = pathlib.Path("/Users/gsix/yang-mills/journals/balaban-CMP119-1988.pdf")
  out.write_bytes(requests.get(url, timeout=30).content)
  ```

  Always save the PDF to `journals/` *before* reading it — web
  access can be intermittent (bot detection, paywalls).

**You are welcome to install additional tools** (e.g. `pdfplumber`
for harder PDFs, `bibtexparser`, etc.) into the active venv. If you
do: install via `uv pip install <pkg>`, append the package + a
one-line justification to `code/requirements.txt`, and record the
addition in your final report under a section titled
**"Tools added during this run"**.

---

---

## Architecture: Two Files, Two Purposes

This project maintains two citation files. They are NOT duplicates:

**`preprint/sections/references.md`** — The paper's bibliography.
This is a preprint deliverable. During LaTeX conversion for arXiv,
it becomes `refs.bib` (BibTeX). It must contain a complete, correctly
formatted entry for every paper cited in the body. Organized by topic
with full author/title/journal/volume/pages/year.

**`journals/citation-tiers.md`** — The verification audit log.
This is our private quality ledger. It tracks which papers have been
physically verified against local PDFs (LOCAL), which have been
confirmed via web search (WEB), and what corrections were applied.
It also stores download URLs and key findings (numbering schemes,
theorem statements). This file is NOT part of the paper.

**Rule:** If a correction is found (wrong theorem number, wrong year),
fix it in the preprint body AND in `references.md`. Then log the
correction in `citation-tiers.md`. The verifier maintains both.

---

## Setup

**Verification ledger:** `/Users/gsix/yang-mills/journals/citation-tiers.md`
**Journal PDFs:** `/Users/gsix/yang-mills/journals/*.pdf`
**Preprint sections:** `/Users/gsix/yang-mills/preprint/sections/`
**Bibliography:** `/Users/gsix/yang-mills/preprint/sections/references.md`
**Proof chain:** `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`

Read the ledger first. It tracks every proof-critical citation with
status LOCAL (PDF on disk, verified) or WEB (title/volume confirmed
online, no local PDF).

---

## Phase 1: Inventory and Completeness Check

### 1a. Extract bibliography entries

Read `references.md` and extract every citation: author, title,
journal, volume, pages, year. Build a flat list.

### 1b. Extract in-text citations

Grep ALL preprint body files (`sections/*.md` and `PROOF-CHAIN.md`)
for every in-text citation. Common patterns:

- `(Author, Journal Vol, Year)` — e.g., `(Balaban, CMP 109, 1987)`
- `(Author, Year, Theorem N)` — e.g., `(Fredenhagen--Marcu, 1986)`
- `(Author Year)` — e.g., `(Osterwalder--Seiler 1978)`
- `Author (Year)` — e.g., `Balaban (CMP 95--96)`
- Inline: `Theorem N of [Author]` or `by Author's result`

Include the surrounding sentence for context. Build a second flat list.

### 1c. Cross-reference: find MISSING and ORPHAN entries

For each in-text citation, find the matching entry in `references.md`.

**MISSING reference** — cited in body, no entry in `references.md`:
Add the missing entry to `references.md` in the appropriate topic
section. Use the correct format: `Author, Initials. (Year). "Title."
Journal Vol, pages.` Search online if needed to get the full metadata.

**ORPHAN reference** — entry in `references.md`, never cited in body:
Flag but do NOT remove (may be cited in a section you haven't checked,
or may be useful context). Report as "orphan — verify intent."

### 1d. Cross-reference against the ledger

For each proof-critical citation (anything in the proof chain:
Balaban, OS, Fredenhagen-Marcu, Kotecky-Preiss, Luscher, Dimock,
Chatterjee, and any new citations), check if it's tracked in
`citation-tiers.md`. Add any missing entries.

---

## Phase 2: Verify LOCAL papers

For each citation marked **LOCAL** in the ledger:

1. Read the PDF from `journals/`. Read enough pages to find:
   - Title page: confirm author, journal, volume, pages, year
   - Table of contents or section structure
   - ALL numbered results (Theorem, Proposition, Lemma, Corollary)
     with their numbers and brief statements

2. Check every in-text reference to this paper in the preprint:
   - "Theorem N" — does Theorem N exist? Does its content match
     what the preprint claims?
   - "Section N" — does the paper use numbered or lettered sections?
   - "Proposition N.M" — does this numbering scheme match the paper?
   - "equation (N)" — spot-check that the equation exists

3. Record findings per paper:
   ```
   ## [Author] [Journal Vol] ([Year])
   Title page: [confirmed / mismatch — details]
   Numbering scheme: [plain / section-based / lettered / unnumbered]
   Results found: [list with page numbers]
   Preprint cites: [list each in-text reference]
   Errors found: [list or "none"]
   ```

4. For each error found:
   - State the wrong citation and the correct one
   - Edit the preprint file(s) to fix it
   - Update the ledger

---

## Phase 3: Verify WEB papers

For each citation marked **WEB** in the ledger:

1. Attempt to download the PDF:
   - Try Project Euclid: `https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-{VOL}/issue-{ISSUE}/.../{ID}.pdf`
   - Try arXiv: `https://arxiv.org/pdf/{ID}`
   - Try Springer DOI: `https://link.springer.com/content/pdf/{DOI}.pdf`
   - If all fail, note "paywalled" and move on

2. If downloaded: save to `journals/` with naming convention
   `{author}-{JOURNAL}{VOL}-{YEAR}.pdf` (e.g.,
   `balaban-CMP119-1988.pdf`), then run the LOCAL verification
   (Phase 2) on it.

3. If not downloadable: verify via web search that the paper exists
   with the claimed title, volume, pages, and year. Check for any
   freely available version (DESY preprints, institutional
   repositories, INSPIRE-HEP).

4. Update the ledger status from WEB to LOCAL (if downloaded) or
   leave as WEB with a note.

---

## Phase 4: Detect common errors

After verifying all papers, specifically check for these failure modes
(all observed in this preprint's history):

### Wrong theorem/proposition numbers
Papers often use different numbering than expected:
- **Plain numbering** (Thm 1, 2, 3) vs **section-based** (Thm 2.1, 3.2)
- **Part-based** (Prop. 1.2 = second prop of Part I) vs **paper-serial**
  (Prop. 3.2 = second prop of paper [3] in a series)
- **Unnumbered** results (single "Theorem." in a short paper)
- **Lettered sections** (Sec. A-F) cited as numbered (Sec. 1-6)

### Wrong volume or year
- Confusing the volume with the paper's position in a series
  (e.g., paper [3] in internal references ≠ volume 3)
- Confusing preprint year with publication year
- Citing a different paper by the same author in a nearby volume

### Garbled duplicates
- Same paper cited twice with different (possibly wrong) metadata
- Copy-paste errors: "CMP 83" when "CMP 103" was intended

### Content mismatch
- Citing a result for Z₂ gauge groups as if it applies to SU(N)
- Citing a scalar field result (Dimock) as if it's for gauge fields
- Citing a continuum result as if it holds on the lattice

---

## Phase 5: Update both files

### 5a. Update `references.md` (the paper's bibliography)

- Add any MISSING entries found in Phase 1c
- Fix any metadata errors found in Phases 2-4 (wrong year, wrong
  volume, wrong pages)
- Remove the correction notes (like "*(Duplicate entry removed...)*")
  once the fix is confirmed — `references.md` should read cleanly
  as a bibliography
- Remove confirmed garbled duplicates
- Flag orphan entries with a comment if unsure whether to remove

### 5b. Update `citation-tiers.md` (the verification ledger)

- Updated status for each paper (LOCAL/WEB/UNVERIFIED)
- Local filenames for all saved PDFs
- Corrections applied (numbered list with before/after)
- Key findings from each verified paper (theorem numbers,
  numbering scheme, content summary)
- Download URLs for any remaining WEB papers
- A verification log entry with the date and session ID

### 5c. Consistency check

After updating both files, verify:
- Every proof-critical entry in `citation-tiers.md` has a matching
  entry in `references.md` (and vice versa for proof-critical refs)
- The metadata (volume, pages, year) matches between the two files
- All corrections applied to in-text citations are also reflected
  in `references.md`

---

## Output

Write your verification report into:
`/Users/gsix/yang-mills/citation-verifier/latest-run/citation-verification-report.md`

This directory was created empty by `code/setup-venv.sh` at the start
of this session. Any prior run was automatically archived into
`runs/r{NN}/` before you started.

**Do NOT read anything inside `citation-verifier/runs/`.** Past runs
are out of scope by design — your verdict must be independent. The
archive exists for human inspection across cycles, not for you.

Use this format for each citation:

```
## #{N}: [Author], [Journal Vol] ([Year])

**Status:** LOCAL / WEB
**PDF:** `journals/filename.pdf`
**Title page:** [vol, pages, year — CONFIRMED or MISMATCH]
**Numbering:** [scheme used]
**Results verified:**
- Thm 1 (p. X): [brief statement]
- Prop 2 (p. Y): [brief statement]

**Preprint references this paper at:**
- `sections/04-...:line N` — cites "Theorem 1" — CORRECT / WRONG (should be ...)
- `sections/05-...:line M` — cites "Prop. 3.2" — WRONG (paper has Prop. 1.2)

**Corrections applied:** [list or "none"]
```

End with a summary table:

```
## Summary

| # | Citation | Status | Errors found | Errors fixed |
|:--|:---------|:-------|:-------------|:-------------|
...

**Total citations:** N
**Total LOCAL:** N
**Total errors found:** N
**Total errors fixed:** N
**Remaining WEB (need download):** [list]
```

---

## Important

- Do NOT trust the preprint's citation metadata. Verify against the
  actual paper.
- Do NOT assume theorem numbering matches across different papers in
  a series. Each paper has its own numbering.
- A paper with lettered sections (A, B, C) should NEVER be cited
  with numbered sections (1, 2, 3).
- Short papers (< 10 pages) often have UNNUMBERED theorems. Citing
  "Theorem 1" for such a paper is wrong — cite the result by page
  or by description.
- If a paper uses internal series numbering (e.g., referencing itself
  as "[3]" in a series), do NOT confuse this with the theorem number
  (Prop. 3.2 ≠ "second proposition of paper [3]").
- Always save downloaded PDFs before verifying — web access may be
  intermittent (bot detection, paywalls).
