# Research Log — QG5D Audit Build

*Append-only. Every web source + finding logged here.*

---

## 2026-04-14 — Initial build (single session)

### Sources consulted

#### Clay Mathematics Institute — rules and problem statements

- **https://www.claymath.org/millennium-problems/rules/** (WebFetch) — rules page (references the PDF).
- **https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf** (curl; 43 KB; saved as `clay-rules-2018-v2.pdf`; text extract `clay-rules-2018-v2.txt`) — **verbatim rules adopted 26 Sept 2018, {N0530588}**. Captures §§1-8 including §4 four gates, §5(b) P-vs-NP/NS either-direction, §5d problem-description compliance, §6 Qualifying Outlet definition (refereed, MathSciNet-indexed, named editorial board).
- **https://www.claymath.org/wp-content/uploads/2024/02/millennium-prize-rules.pdf** (curl; 81 KB; saved as `clay-rules-2018.pdf`) — alternate Clay rules PDF.
- **https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf** (curl; 196 KB; saved as `yang-mills-jaffe-witten.pdf`; text extract `.txt`) — Jaffe-Witten YM statement. Verbatim §4 problem statement extracted.
- **https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf** (curl; 159 KB; saved; text extracted) — Bombieri RH statement. Verbatim problem statement extracted.
- **https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf** (curl; 143 KB; saved; text extracted) — Wiles BSD statement. Verbatim problem statement extracted (weak + refined/strong version).
- **https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf** (curl; 147 KB; saved; text extracted) — Deligne Hodge statement. Verbatim problem statement extracted (§2 remarks including Atiyah-Hirzebruch Q-not-Z obstruction, Kähler ≠ algebraic).
- **https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf** (curl; 204 KB; saved; text extracted) — Fefferman NS statement. Verbatim (A)(B)(C)(D) four sub-problems extracted.
- **https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf** (curl; 176 KB; saved; text extracted) — Cook P-vs-NP statement. Verbatim §1 "Does P = NP?" extracted.
- **https://www.claymath.org/millennium/riemann-hypothesis/** (WebFetch) — RH problem page, confirms Bombieri PDF link.
- **https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/** (WebFetch) — BSD problem page.
- **https://www.claymath.org/millennium/hodge-conjecture/** (WebFetch) — Hodge problem page.
- **https://www.claymath.org/millennium/navier-stokes-equation/** (WebFetch) — NS problem page.
- **https://www.claymath.org/millennium/p-vs-np-problem/** (WebFetch **404** — page has moved; P-vs-NP PDF link obtained via WebSearch).

**Findings:**
- Clay rules §4 (four gates): Qualifying Outlet + 2-year rule + general acceptance + satisfactorily-addresses official description.
- Clay rules §5d: silence on any required element is a violation ("paper that does not address or refer to the specific mathematical questions…will not be considered").
- Clay rules §5(b): P-vs-NP and NS uniquely admit EITHER-direction resolution.
- Clay rules §6e: Qualifying Outlet requires MathSciNet inclusion, named editorial board, published refereeing process.
- Zenodo does NOT qualify (no refereeing).
- arXiv does NOT qualify (no refereeing).
- Direct submission to CMI rejected (§5e).

#### Prizes

- **https://breakthroughprize.org/Rules/3** (WebFetch) — Breakthrough Mathematics rules. $3M, no self-nom, 1 third-party letter + up to 10 citations.
- **https://breakthroughprize.org/Rules/1** (WebFetch) — Breakthrough Fundamental Physics rules. $3M; can be SHARED among any number.
- **https://breakthroughprize.org/Prize/Mathematics** (WebFetch **404**) — top-level page moved.
- **WebSearch** "Breakthrough Prize Mathematics 2026 nomination rules eligibility" — hit set as above.
- **WebSearch** "Breakthrough Prize Fundamental Physics nomination rules" — hit set as above.
- **https://abelprize.no/page/nomination-guidelines-and-nomination-form** (WebFetch **TIMEOUT**) — Abel Prize nomination. Content synthesized from WebSearch abstracts.
- **https://abelprize.no/page/faq-frequently-asked-questions** (WebFetch **TIMEOUT**) — Abel FAQ. Synthesized from search.
- **WebSearch** "Abel Prize 2026 nomination rules eligibility committee" — extracted: anyone can nominate, no self-nom, living nominee, at least one peer-reviewed publication, 5-member committee, recommendations via IMU/EMS.
- **https://www.shawprize.org/nomination/** (WebFetch) — Shaw Prize by-invitation-only, September 1 → November 30 window, self-nominations rejected.
- **WebSearch** "Shaw Prize mathematical sciences" — extracted deadline and eligibility.
- **WebSearch** "Wolf Prize Mathematics nomination rules 2026" — extracted: by invitation, no self-nom, 2-3 person teams, awarded for breakthroughs not career, Nobel laureates ineligible unless for different achievement.
- **WebSearch** "Fields Medal eligibility rules age 40 IMU" — extracted statutes: candidate's 40th birthday must not occur before Jan 1 of Congress year; 2-4 medals per Congress every 4 years.
- **WebSearch** "Nobel Prize Physics nomination rules eligibility 2026" — extracted: by invitation, Sept invites, Jan 31 deadline, 50-year confidentiality.

#### Venues

- **https://info.arxiv.org/help/submit/index.html** (WebFetch) — arXiv submission rules. LaTeX preferred; filename rules; 3-papers/day; self-submission expected.
- **https://info.arxiv.org/help/endorsement.html** (WebFetch) — endorsement required for first submission per category; institutional-email-only auto-endorsement discontinued Dec 2025.
- **https://info.arxiv.org/help/withdraw.html** (WebFetch) — withdrawal creates new version; old versions remain; withdrawing because of journal acceptance is INAPPROPRIATE.
- **https://info.arxiv.org/help/moderation/index.html** (WebFetch) — AI policy: significant use must be reported, AI not listed as author. Review-articles policy tightened Nov 2025 (cs).
- **WebSearch** "arXiv submission moderation rules math.MP hep-th endorsement 2025" — hit confirming.
- **https://about.zenodo.org/policies/** (WebFetch) — Zenodo policies. Anyone can deposit; 50 GB/record; DOI upon deposit; withdrawals replaced by tombstone but DOI/URL preserved.
- **https://help.zenodo.org/** (WebFetch) — Zenodo help hub (limited content).
- **https://annals.math.princeton.edu/submission** (WebFetch) — Annals of Mathematics guidelines. CRITICAL: "does not consider papers generated using AI products." Email submission; aomart LaTeX class; free to publish.
- **https://link.springer.com/journal/222/submission-guidelines** (WebFetch **303 redirect**) — Inventiones. Content synthesized.
- **https://link.springer.com/journal/222** (WebFetch **303**) — Inventiones home.
- **https://www.ams.org/publications/journals/journalsframework/jams** (WebFetch **403 blocked**) — JAMS blocked; content synthesized.
- **https://link.springer.com/journal/220/submission-guidelines** (WebFetch **403**) — CMP. Got partial info via WebSearch.
- **https://www.cambridge.org/core/journals/forum-of-mathematics-pi/information/author-instructions** (WebFetch) — Forum of Math Pi. Open-access; APCs with waivers; submitted via cup.msp.org.
- **https://link.springer.com/journal/13130/submission-guidelines** (WebFetch **303**) — JHEP. Got info via WebSearch.
- **https://journals.aps.org/prd/authors** (WebFetch **403**) — PRD blocked.
- **https://journals.aps.org/prl/authors** (WebFetch **403**) — PRL blocked. Got info via WebSearch (3750-word limit, 100-word justification, 2-page End Matter).
- **WebSearch** various APS pages — extracted PRL 3750-word limit, PRD length guidelines.

### NOT FOUND / blockers

- **Annals AI policy** — found (in text above); Annals "does not consider papers generated using AI products" — CRITICAL, documented.
- **Inventiones submission guidelines** — Springer 303 redirect. Content synthesized from WebSearch. Re-fetch via browser may be required.
- **JAMS submission guidelines** — AMS site 403. Content synthesized.
- **CMP submission guidelines** — Springer 403 on first fetch. Later WebSearch extracted essentials.
- **JHEP / PRD / PRL submission** — similar Springer/APS blocks; WebSearch gave essentials.
- **Preprints.org** — not needed in this run (blocker anticipated but no requests made).

### Summary of this session

Files saved under `/audit/`:
- 1 Clay rules master md + 2 PDFs + 1 text extract
- 6 Clay problem-statement PDFs + 6 text extracts
- 12 compliance checklists / problem-statement / requirements files across YM, RH, BSD, PvNP, Hodge, NS
- 8 prize rule files (breakthrough-math, breakthrough-physics, abel, shaw, wolf-math, wolf-physics, fields, nobel-physics)
- 8 venue files (arxiv × 4, zenodo, annals, inventiones, jams, cmp, forum-pi, jhep, physical-review)
- 53 per-paper files (one per programme paper)
- 1 master compliance-matrix.md
- 1 README.md
- this research-log.md

Total: ~95 markdown files + ~10 PDFs + ~7 text extracts.
