# Applied patches to 04-lattice-proof-part1.md

Target file: `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`

Three patch documents were applied in sequence (A1 notation cleanup,
A3 Lüscher applicability lemma, B2 cluster-expansion-implies-mass-gap).
All edits applied successfully via the Edit tool.

## A1 — Weitzenböck notation ($N$-dependence)

Source: `tier-2-fixes/A1-weitzenboeck-notation-patch.md`

1. **Theorem 1 statement (L187–190)** — `$\mu_1 = 6/r_3^2$` → `$\mu_1 \geq 2N/r_3^2$ ($=6/r_3^2$ for $N=3$)`.
2. **Theorem 1 Step 3 (L253–261)** — made $\mu_n \geq 2N/r_3^2$ explicit; rewrote parenthetical to reference $4N/r_3^2$ as the actual Ikeda–Taniguchi eigenvalue.
3. **Theorem 1 Step 4 (L274–278)** — `$\mu_1 = 6/r_3^2$` → `$\mu_1 \geq 2N/r_3^2$`; Hessian bound written as $2N/(g_{\text{int}}^2 r_3^2)$.
4. **Remark 2 (L325–330)** — rewrote "Why $6/r_3^2$ suffices" as "Why the Weitzenboeck bound suffices" with general-$N$ forms.
5. **Theorem 2 statement (L401–406)** — `$m_1 = 2\sqrt{3}/r_3$` → `$m_1 = 2\sqrt{N}/r_3$` (with $N=3$ parenthetical).
6. **Regime B text (L658–661)** — `$m_1 a = 2\sqrt{3}\,a/r_3$` → `$m_1 a = 2\sqrt{N}\,a/r_3$`.
7. **Regime B formula (L666–672)** — `$m_1 a/6 = a/(\sqrt{3}\,r_3)$` → `$\sqrt{N}\,a/(3 r_3) \approx (\sqrt{N}/3)\times 10^{15}$`; numeric $5.8\times 10^{14}$ kept as N=3 side remark.
8. **Crossover (L687)** — `$a_{\mathrm{cross}} \approx 2\sqrt{3}\,r_3\,\beta$` → `$2\sqrt{N}\,r_3\,\beta$`.
9. **§4.3 convergence window (L728–732)** — `$\beta < a_0/(2\sqrt{3}\,r_3) \sim 10^{14}$` → `$\beta < a_0/(2\sqrt{N}\,r_3) \sim (1/(2\sqrt{N}))\cdot 10^{15}$ (for $N=3$, $\sim 2.9\times 10^{14}$)`.
10. **Theorem 4(a) convergence (L774–782)** — `$\lambda_1^{(1)} \geq 6/r_3^2$` → `$\geq 2N/r_3^2$`; `$m_1 = 2\sqrt{3}/r_3$` → `$2\sqrt{N}/r_3$`; $\beta_{\max}$ written in $N$-dependent form.
11. **Scope & Limitations (L934–938)** — `$\beta < a/(2\sqrt{3}\,r_3)$` → `$\beta < a/(2\sqrt{N}\,r_3)$`, with $N=3$ parenthetical.
12. **Theorem 5 statement (L964–966)** — `$m_1 = 2\sqrt{3}/r_3$` → `$m_1 = 2\sqrt{N}/r_3$` with $N=3$ parenthetical.
13. **H.11 comparison table (L1854)** — Weitzenböck-gap row updated: SU(2) column annotated with FS conversion $4/r_3^2, r_3=2r_2$; SU(3) column written as `$2N/r_3^2$ ($=6/r_3^2$ for $N=3$)`.

## A3 — Lüscher admissibility lemma

Source: `tier-2-fixes/A3-luscher-topology-coarse-lattice.md`

14. **§4.4 Corollary "Compatibility with small-field condition" (L841–899)** — replaced the Balaban-based paragraph with full **Lemma A3.1** (statements (i)–(iii), proof sketch via Markov + union bound, and physical-values numerical table) that derives admissibility directly from the Theorem 3 cluster-expansion convergence condition. Self-contained: no appeal to Balaban's RG at the bare scale.

## B2 — Cluster expansion implies mass gap (FM direction fix)

Source: `tier-2-fixes/B2-fredenhagen-marcu-direction.md`

15. **§4.3 Consequences item 4 (L708–726)** — replaced the "$\sigma > 0 \Rightarrow \Delta > 0$ via flux tube" chain with the rigorous cluster-expansion rate argument: $\Delta_0 \geq \alpha/a$ directly from Kotecký–Preiss + RP (Lemma D.2) + spectral theorem. Added **Remark 4.1** marking area law + Fredenhagen–Marcu + flux tube as physical consistency checks rather than steps in the proof.
16. **§4.4 Theorem 4(e) (L800–815)** — replaced "area law ⇒ mass gap via flux tube" with the $\alpha/a$ rigorous chain; added **Remark 4.2** reiterating that FM, area law, and flux-tube are consistency checks, not rigorous steps. Reference to Reed–Simon Vol. IV §XIII.1 added for the spectral theorem.

## Failures

None. All 16 edits applied successfully via `Edit`. The remaining occurrences of `$6/r_3^2$` and `$2\sqrt{3}/r_3$` in the file are all inside "for $N=3$" parentheticals, which is the desired end state.

## Final file line count

- Before: 1798 lines
- After: 1857 lines
- Delta: +59 lines (A3 lemma insertion dominates; B2 remark additions contribute a few lines)
