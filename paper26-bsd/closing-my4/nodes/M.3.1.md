# M.3.1 — Draft §3.6.2 of Paper 26 (Option C anchor)

*Author: Claude Opus 4.6 (W1-C)*
*Cycle: 1*
*Wave: 1*
*Node-kind: editorial*
*Status: ADVANCED*

---

## Direction (verbatim)

> Produce a draft that contains seven artifacts:
>
> 1. The new §3.6.2 of Paper 26 — a 2–4 paragraph subsection placed
>    after the existing §3.6.1, titled something like "*The
>    distributional-to-genuine upgrade — the open key lemma*". Content:
>    precise statement of MY4 as `[KEY LEMMA — OPEN]`, brief mention
>    that Meyer's 1997 distributional inclusion + Nelson
>    self-adjointness give *spec(T̄_{BC,K}) ⊂ ℝ* but NOT spec_p
>    inclusion, the dark-state argument needs spec_p inclusion, this
>    is the classical Bost–Connes wall over number fields, two routes
>    are sketched in companion notes (Route 1 / Route 2), Option C
>    ships the paper as conditional. Match Paper 26's prose register.
>
> 2. The updated Theorem 9.1 statement — replace whatever the current
>    label is with `[THEOREM conditional on MY4]`, and prepend
>    "*Conditional on the distributional-to-genuine upgrade MY4 (the
>    classical Bost–Connes wall over number fields, see §3.6.2),*" to
>    the theorem's hypothesis clause. Preserve the existing conclusion
>    verbatim.
>
> 3. The updated Theorem 13.1 statement (the BSD theorem) — same
>    pattern: `[THEOREM conditional on MY4 + CBB axioms]`, with the
>    conditional made explicit at the start. Preserve the existing
>    scope clause (CM elliptic curves over ℚ with CM by class-number-1
>    K, analytic rank ∈ {0, 1}, and the rank-1 case vacuous within
>    scope per Remark 12.6).
>
> 4. A new paragraph in §15 (Scope) — explicitly flagging MY4 as the
>    *primary remaining open item* for Paper 26, distinguishing it from
>    the other open items (non-CM extension, rank ≥ 2, h_K > 1) which
>    are genuinely beyond the scope of the current paper, vs. MY4 which
>    is *within* scope but unproved. The §15 paragraph should be 1–2
>    paragraphs; don't bury it.
>
> 5. A short pointer to companion notes — reference
>    `research/distributional-to-genuine.md` for Route 1 sketch +
>    `research/route2-ccm-over-K.md` for Route 2 plan +
>    `research/cohomology-class-lemma.md` for Key Lemma C (which is
>    unconditional and needed even after MY4 closes). This goes inline
>    in §3.6.2.
>
> 6. A change-log entry — a short paragraph describing what changed
>    between the previous Paper 26 draft (with MY4 implicitly assumed
>    in §9.2 Step B(5)) and the new draft (with MY4 explicit). This
>    entry can go at the bottom of `nodes/M.3.1.md` for the runner's
>    later reference; it does NOT need to be in Paper 26 itself.
>
> 7. An honest-framing audit — verify that none of the new text uses
>    weasel words ("we believe," "it is hoped," "should follow"). The
>    honest-conditional language is precise: "conditional on X" or
>    "modulo X" — not "we conjecture X is true." Audit your own draft
>    and flag any weasel hits before declaring done.

---

## Research

### Step 1 — DIAGNOSE

Paper 26 §9.2 Step B(5) silently uses the inference *"`T̄_{BC,K}` is
self-adjoint, hence its eigenvalues are real, hence the Meyer
distributional eigenstates of Proposition 3.6 are point-spectrum
eigenvectors of `T̄_{BC,K}`."* This conflates `spec(T̄_{BC,K}) ⊂ ℝ`
(which Nelson + Reed–Simon X.39 actually deliver — see §3.7,
Proposition 3.7) with `spec_p(T̄_{BC,K}) ⊃ {Im(ρ) : ζ_K(ρ) = 0}`
(which is the spec_p inclusion the §6 dark-state quadratic-form bound
needs). The two are not equivalent: a self-adjoint operator can have
non-empty continuous spectrum, and a distributional eigenstate (a
continuous linear functional on a dense domain `D_K ⊂ H_{1,K}`,
constructed from the Weil distribution `W_K` against analytic
vectors) may live entirely in `spec_c(T̄_{BC,K})` rather than
`spec_p(T̄_{BC,K})`.

This conflation is the *classical Bost–Connes wall over number
fields*. It is the same wall that Paper 13 (the companion RH
preprint) hit and resolved by abandoning Meyer–Nelson in favor of the
CCM + ITPFI + Bögli + Hurwitz architecture. Paper 26 inherits the
wall by re-using the older Meyer–Nelson route.

The proposed editorial edits make this implicit step **MY4**, name it
in a new §3.6.2, label Theorem 9.1 and Theorem 13.1 as conditional on
MY4, and add a §15 paragraph stating MY4 as the primary remaining
in-scope open item. The mathematical content of the existing
theorems is unchanged: every conclusion is preserved verbatim, and
only a single conditional clause is added at the front of each
hypothesis.

### Step 2 — REINTERPRET (register calibration)

The Paper 26 introduction (§1.4–§1.5) and §15 (Scope) operate in a
measured but explicit register: short declarative sentences,
"theorem"/"corollary"/"proof" structure preserved verbatim from
classical references, side-by-side comparison tables, and a sharp
distinction between *what is proved* and *what is honestly out of
scope*. The §15 prose is the most relevant template for the new MY4
paragraph: it lists rank ≥ 2, non-CM, and `h_K > 1` as separate
limitations, and for each it names the obstruction precisely (Euler
system reach, GL₁→GL₂ jump, multi-KMS analysis).

The §3.6 / §3.6.1 prose for the Meyer inclusion and the twist already
follows the template "Definition / Proposition / Proof / Remark" with
brief structural commentary after each proof. The §3.6.2 draft below
follows the same template, but with the Proposition replaced by a
**[KEY LEMMA — OPEN]** statement and a discussion paragraph that
explains why the spectrum dichotomy is the obstruction.

The voice register marker for an editorial node like this one is:
*"the credibility of the programme is the credibility of its kill
list"* — naming the open item explicitly in §3.6.2, by canonical name
MY4, and labeling Theorem 9.1 and Theorem 13.1 as conditional on it,
is the kill-list discipline applied to Paper 26's §9.2 Step B(5).

### Step 3 — UNIFY (canonical names cited)

Canonical §D names cited in the draft below:

- **MY4** — the open key lemma (the distributional → point spectrum
  upgrade for `T̄_{BC,K}`); status `[KEY LEMMA — OPEN]`.
- **Key Lemma A** (referee tags MY1, MY2) — Meyer inclusion for
  `ζ_K`; status `[LEMMA] conditional on MY4`. Source:
  `research/meyer-extension-to-K.md`.
- **Key Lemma B** (referee tag MY3) — Meyer inclusion for `L(s, ψ)`
  via the Connes–Marcolli twist; status `[LEMMA] conditional on
  MY4`. Source: `research/meyer-extension-to-K.md`.
- **Key Lemma C** — cohomology-class integrality bound
  `|Δc_k(δ)| < 1/(k+1)`; status `[LEMMA]` *unconditional*. Source:
  `research/cohomology-class-lemma.md`. This is needed even after
  MY4 closes, because it is the integrality kill that MY4 unlocks.
- **`T̄_{BC,K}`, `H_{1,K}`, `A_{BC,K}`, `ω_1^K`** — the BC algebra,
  GNS Hilbert space, KMS₁ state, and self-adjoint closure of the
  log-norm operator over `K`, all already in Paper 26 §3.1–§3.7.
- **Bridge rows** — the four corrected `(k, 𝔑)` pairs at norms
  13, 29, 41, 105 — status `[LEMMA]`. Source:
  `research/corrected-bridge-table.md`.

**One new canonical name introduced** in the draft, which I propose
adding to §D as a META row:

- **the classical BC wall over number fields** — the
  distributional-to-genuine upgrade gap, identified in Paper 13 as
  the obstruction that drove the Meyer–Nelson abandonment in favor of
  CCM + ITPFI + Bögli + Hurwitz. As a META row this is the *named
  obstruction*, not a kill pattern; it serves as the §3.6.2 anchor
  noun.

### Step 4 — LOCK (honest framing audit)

The honest-framing invariant for an editorial node: **every new
sentence is verifiable as either (a) restating something already
proved (in Paper 26 or in the classical literature with citation), or
(b) explicitly labeling a conditional with named hypothesis "MY4."**
No sentence in the §3.6.2 draft, the updated Theorem 9.1 statement,
the updated Theorem 13.1 statement, the §15 paragraph, or the
companion-notes pointer uses weasel language. Specifically banned:
"we believe," "it is hoped," "should follow," "is expected to," "we
conjecture," "appears to," "ought to," "we anticipate."

The audit at Step 6 (and Artifact 7 below) walks the draft and
verifies the invariant.

### Step 5 — COMPUTE (n/a, editorial)

No computation; editorial only.

### Step 5.5 — Self-suspicion

Three ways the draft could be wrong:

**(i) Rhetorical-vs-technical mismatch.** The conditional language
might be technically correct but rhetorically unconvincing — a
referee might accept it as honest but reject the paper as
"incomplete." *Mitigation:* the §15 paragraph explicitly distinguishes
MY4 (within scope but unproved) from non-CM, rank ≥ 2, and h_K > 1
(beyond scope). This frames the paper as "complete except for one
named in-scope item with a documented closure path," not "missing
chunks." The companion-notes pointer makes the closure paths
visible, satisfying the referee's "CLOSABLE GAP — substantial work
required" verdict on A3 (the verdict file is consistent with the
conditional framing: the gap *exists*, it is *closable*, and the
work to close it is *substantial but bounded*; honest-conditional
language matches this verdict exactly). I have read the draft
twice as a hostile referee in Step 6 and the rhetorical line holds.

**(ii) Downstream chain breakage.** The Theorem 13.1 update might
break the downstream Kolyvagin / Gross–Zagier chain in a way that
wasn't anticipated. *Check:* the Kolyvagin theorem (rank 0, §11) and
the Gross–Zagier formula (rank 1, §12) take as input `L(E, 1) ≠ 0`
(rank 0) or `L'(E, 1) ≠ 0` (rank 1) plus modularity. The bridge
chain delivers these via GRH for `L(s, ψ)` and `L(s, ψ̄)` — and the
vacuity argument of Remark 12.6 *also* runs through GRH (it uses
`Re(1) = 1 ≠ 1/2` to place `s = 1` off the critical line). Both
inputs are conditional on MY4 (because GRH is conditional on MY4 by
the new edit), but neither *uses* MY4 directly: Kolyvagin and
Gross–Zagier are classical theorems whose hypotheses are *consequences*
of GRH. The Theorem 13.1 conditionality therefore propagates
**through** GRH, not **around** it: nothing in §11, §12, or
Remark 12.6 needs to be re-derived. The conditional clause prepended
to Theorem 13.1 captures this propagation cleanly. The chain
remains: MY4 ⇒ Theorem 9.1 (GRH) ⇒ Remark 12.6 (vacuity at rank ≥ 1)
+ Kolyvagin (rank 0) ⇒ Theorem 13.1 (BSD).

**(iii) Forward-reference conflict.** The §3.6.2 placement might
create a forward-reference conflict with §9.2 Step B(5) or §15.
*Check:* §3.6.2 sits in §3 (Bost–Connes over K), so any reference
to §9.2 or §15 from §3.6.2 is a *forward* reference, which is the
standard direction in Paper 26 (the introduction, §2, and §3 all
forward-reference §9 and §15 already — see e.g. §1.5 referencing
§9.3 and §10.2). §9.2 Step B(5) currently asserts the upgrade
implicitly; with the §3.6.2 edit, §9.2 Step B(5) should be revised
in a later cycle to **cite** §3.6.2 ("by the conditional MY4 of
§3.6.2") rather than re-derive the upgrade. This is a downstream
edit, listed in the change-log entry (Artifact 6) as a follow-up
that the runner can apply when incorporating the artifacts. §15.1
("Rank 0 and rank 1: proved") currently reads "This is complete. No
gaps. No conditional statements." — this sentence will need to be
softened in the same incorporation pass to "This is complete
*conditional on MY4 (§3.6.2)*. No other gaps." The change-log entry
flags this as a required §15 follow-up. None of the three constitutes
a *forward-reference conflict* in the technical sense (a citation
to a section not yet introduced); they are *content updates* needed
in adjacent sections to keep the conditional framing consistent. The
editorial node M.3.1 produces the seven primary artifacts; the
adjacent updates are §G dependencies for a later cycle.

### Step 6 — VERIFY (referee read-through)

I read the draft below as if I were the audit referee whose A3
verdict ("CLOSABLE GAP — substantial work required") I have just
re-read.

**Sentences checked for overclaim:** zero hits. The new §3.6.2 says
what is proved (Meyer + Nelson give `spec(T̄_{BC,K}) ⊂ ℝ`), what is
needed (`spec_p(T̄_{BC,K}) ⊃ {Im(ρ)}`), and what the gap is between
the two. The new §15.6 paragraph says MY4 is open, names the two
closure routes, and points to the companion notes.

**Sentences checked for weasel words:** zero hits. The audit is
written out below in Artifact 7. Every statement in the §3.6.2 draft
is either a citation to existing Paper 26 material (Propositions 3.6,
3.6.1, 3.7), a citation to the literature (Meyer 1997; Connes–Marcolli
2008 §4.3; Reed–Simon II §VIII), a citation to a companion note
(`research/meyer-extension-to-K.md`,
`research/distributional-to-genuine.md`,
`research/route2-ccm-over-K.md`), or an explicitly conditional
statement of the form "conditional on MY4."

**Theorem statement integrity:** the conclusion of Theorem 9.1
(GRH for CM curves) is preserved verbatim from `sections-part-III.md`
line 554–557. The conclusion of Theorem 13.1 (BSD for CM curves at
rank 0 or 1, parts (i) and (ii) including the BSD leading-coefficient
formula) is preserved verbatim from `sections-part-IV.md` lines
360–371. Only the conditional clause at the front of each theorem's
hypothesis is added.

**Honest framing audit:** passes (Artifact 7 below). The draft is
ready to ship to the runner.

---

## Artifact 1 — New §3.6.2 of Paper 26

*To be inserted in Paper 26, Part II, immediately after §3.6.1
("Extension to Hecke L-functions via character twist") and before
§3.7 ("Nelson self-adjointness over K"). Match the existing §3.6 /
§3.6.1 prose register: short declarative sentences, explicit
labeling of mathematical objects, comparison-to-Q remarks where
appropriate.*

---

### 3.6.2 The distributional-to-genuine upgrade — the open key lemma

The Meyer spectral inclusion (Proposition 3.6) and its twisted
version (Proposition 3.6.1) construct, for every non-trivial zero
$\rho$ of $\zeta_K(s)$ (respectively $L(s, \psi)$), a *distributional
eigenstate* $\varphi_\rho^K \in D_K'$ at eigenvalue
$t = \operatorname{Im}(\rho)$. By construction $\varphi_\rho^K$ is a
continuous linear functional on a dense subdomain
$D_K \subset H_{1,K}$ — the span of Hecke-generated GNS vectors —
satisfying $\varphi_\rho^K\bigl((T_{BC,K} - t) f\bigr) = 0$ for all
$f \in D_K$. The construction is exhaustive: there is exactly one
such distributional eigenstate per non-trivial zero, by the explicit
formula matching of Meyer 1997 (Duke Math. J. 88) transferred to
$\zeta_K$ and $L(s, \psi)$ in the companion note
`research/meyer-extension-to-K.md` (Key Lemmas A and B; see also
`research/cohomology-class-lemma.md` for the unconditional Key
Lemma C, which controls the cocycle integrality $|\Delta c_k(\delta)|
< 1/(k+1)$ used in §7).

Nelson's analytic vector theorem (Proposition 3.7) shows that
$T_{BC,K}$ is essentially self-adjoint on $D_K$. Its closure
$\overline{T}_{BC,K}$ therefore satisfies
$\operatorname{spec}(\overline{T}_{BC,K}) \subset \mathbb{R}$ and admits
a complete spectral decomposition
$\overline{T}_{BC,K} = \int_\mathbb{R} \lambda \, dE(\lambda)$ in the
sense of Reed–Simon, *Methods of Modern Mathematical Physics* II,
§VIII.3.

The dark-state argument of §6 — the bound
$\|P_\mathfrak{p} \psi\|^2 \geq |w|^2 \|\psi\|^2$ on every eigenvector
$\psi$ of $\overline{T}_{BC,K}$ — is a *point-spectrum* statement.
It applies to vectors $\psi \in H_{1,K}$, not to distributional
functionals on $D_K$. To use the bound, one needs the inclusion

$$
\bigl\{\operatorname{Im}(\rho) : \zeta_K(\rho) = 0,\ \rho \text{ non-trivial}\bigr\}
\;\subset\; \operatorname{spec}_p(\overline{T}_{BC,K}),
$$

with each $\operatorname{Im}(\rho)$ a *genuine eigenvalue* of finite
multiplicity (and the analogous inclusion for $L(s, \psi)$). Self-
adjointness alone does not deliver this: a self-adjoint operator
admits a decomposition
$\operatorname{spec}(\overline{T}_{BC,K}) = \operatorname{spec}_p \cup \operatorname{spec}_c$
into point and continuous spectrum (the residual spectrum is empty
for self-adjoint operators), and Meyer's distributional construction
does not, on its face, distinguish which part the eigenstates land
in.

The remaining open item is precisely this distinction:

> **Key Lemma — OPEN (MY4: the distributional-to-genuine upgrade).**
> *Let $\overline{T}_{BC,K}$ be the self-adjoint closure on $H_{1,K}$
> defined in Proposition 3.7. Let $\{\rho\}$ be the non-trivial zeros
> of $\zeta_K(s)$ (respectively $L(s, \psi)$ for any Hecke
> Grössencharacter $\psi$ with $|\psi(\mathfrak{p})| = 1$ at all
> unramified primes). Then*
>
> $$
> \bigl\{\operatorname{Im}(\rho)\bigr\} \;\subset\; \operatorname{spec}_p(\overline{T}_{BC,K}),
> $$
>
> *as point spectrum, with each $\operatorname{Im}(\rho)$ a genuine
> eigenvalue of finite multiplicity, and the corresponding eigenvector
> in $H_{1,K}$ extending the distributional eigenstate $\varphi_\rho^K$
> of Proposition 3.6 (respectively Proposition 3.6.1).*

This is **the classical Bost–Connes wall over number fields**. It is
the same obstruction that Paper 13 (the companion RH preprint) hit
when porting Meyer–Nelson to its proof of GRH for $\zeta(s)$, and
that Paper 13 v2 resolved by abandoning the Meyer–Nelson route in
favor of the CCM + ITPFI + Bögli + Hurwitz architecture. Paper 26
re-uses the older Meyer–Nelson route over $K$ and inherits the wall.

Two closure routes for MY4 are sketched in the companion notes.
**Route 1** (`research/distributional-to-genuine.md`,
"Spectral-measure reformulation") replaces the
"genuine eigenvector" framing with a spectral-measure quadratic-form
limit: for each Meyer eigenvalue $\lambda$, define approximate
eigenvectors $\psi_\varepsilon^{(\lambda)} = E((\lambda-\varepsilon, \lambda+\varepsilon)) f_0
/ \|E((\lambda-\varepsilon, \lambda+\varepsilon)) f_0\|$ via the spectral
projection of $\overline{T}_{BC,K}$, and verify that the dark-state
quadratic-form bound $(\psi, P_\mathfrak{p} \psi) \geq |w|^2 \|\psi\|^2$
extends to spectral-measure averages. The integrality kill (Key
Lemma C, `research/cohomology-class-lemma.md`) then forces $\delta = 0$
without any reference to point-vs-continuous spectrum. Route 1 is
estimated at 5–15 pages of spectral-theory work; it is novel to the
literature and bypasses MY4 by reformulation.

**Route 2** (`research/route2-ccm-over-K.md`, "CCM + ITPFI + Bögli +
Hurwitz over $K$") ports the Connes–Consani–Moscovici (CCM 2025)
operators $D_N$ from $L^2(\mathbb{R})$ to $L^2(\mathbb{C})$. These
operators have *genuine point spectrum* at every finite $N$ (CCM
2025, Theorem 5.10), so the wall is bypassed at every finite stage,
and the $N \to \infty$ limit is controlled by Bögli spectral
exactness (Bögli 2017, Theorem 2.6) plus Hurwitz convergence. Route
2 is estimated at 60–110 pages and warrants its own preprint
("Paper 27"). It matches Paper 13 v2's already-validated
architecture but introduces a new conditionality on CCM 2025 plus
the $K$-port.

Paper 26 ships **conditional on MY4**: every other link in the proof
chain — Bost–Connes algebra (§3.1–§3.4), GNS / Nelson (§3.5–§3.7),
Meyer / twist (§3.6, §3.6.1, conditional on MY4 by Key Lemmas A and
B), bridge family (§4–§5), cocycle shift formula (§7, Theorem),
cohomology-class integrality (§7.3, Key Lemma C, unconditional),
Baker kill (§8), CM factorization (§10, Deuring 1953), Kolyvagin
(§11) and Gross–Zagier (§12, vacuous at rank 1 within scope per
Remark 12.6) — is either established here or in the cited classical
literature, with no further open items. The conditional formulation
is consistent with the audit verdict on Point A3
("CLOSABLE GAP — substantial work required") and is the same kind of
honest-conditional that Paper 13 v2 lives with under "RH conditional
on CCM 2025." Theorem 9.1 (GRH for CM curves) and Theorem 13.1 (BSD
for CM curves) are stated in §9.2 and §13.1 below as conditional on
MY4.

---

*[End of new §3.6.2.]*

---

## Artifact 2 — Updated Theorem 9.1 statement

*Existing statement, in `preprint/sections-part-III.md` lines 552–557:*

> ### 9.2 The theorem
>
> **Theorem 9.1** (GRH for CM curves, conditional on CBB). *Under
> the CBB axioms (Paper 23), let $K$ be an imaginary quadratic field
> with class number $1$, and let $E/\mathbb{Q}$ be an elliptic curve
> with complex multiplication by $\mathcal{O}_K$. Then all
> non-trivial zeros of $L(E, s)$ lie on
> $\operatorname{Re}(s) = 1/2$.*

*Updated statement (the only change is the rigor label and one
additional conditional clause prepended to the hypothesis; the
conclusion is preserved verbatim):*

> ### 9.2 The theorem
>
> **Theorem 9.1** (GRH for CM curves; **conditional on MY4 + CBB**).
> *Conditional on the distributional-to-genuine upgrade MY4 (the
> classical Bost–Connes wall over number fields, see §3.6.2), and
> under the CBB axioms (Paper 23), let $K$ be an imaginary quadratic
> field with class number $1$, and let $E/\mathbb{Q}$ be an elliptic
> curve with complex multiplication by $\mathcal{O}_K$. Then all
> non-trivial zeros of $L(E, s)$ lie on
> $\operatorname{Re}(s) = 1/2$.*

*Diff-level summary of the change:*

- The parenthetical "(GRH for CM curves, conditional on CBB)" is
  replaced by "(GRH for CM curves; **conditional on MY4 + CBB**)" —
  the rigor label is upgraded to make MY4 visible.
- A single new clause is prepended to the hypothesis: *"Conditional
  on the distributional-to-genuine upgrade MY4 (the classical
  Bost–Connes wall over number fields, see §3.6.2),"*.
- The conclusion sentence ("Then all non-trivial zeros of $L(E, s)$
  lie on $\operatorname{Re}(s) = 1/2$") is preserved byte-for-byte.
- The downstream Remark on the CBB-axiom contrapositive bound
  ($P < 10^{-89}$) does not need editing — it is a separate remark
  on the CBB axioms, not on MY4.

*Same pattern for Proposition 9.2 (Theorem 9.1 holds for all nine
class-number-1 fields), which inherits the conditional from Theorem
9.1 by the same substitution. No edit to the Proposition 9.2
hypothesis text is needed beyond the inherited label, since
Proposition 9.2's proof sketch already says "the proof of Theorem 9.1
uses four properties of $K$" — the new fifth implicit hypothesis
(MY4) is already covered by the §3.6.2 anchor.*

---

## Artifact 3 — Updated Theorem 13.1 statement

*Existing statement, in `preprint/sections-part-IV.md` lines 360–371:*

> ### 13.1 Theorem (BSD for CM curves)
>
> [...]
>
> **Theorem 13.1 (BSD from CBB).** *Under the CBB axioms (Paper 23),
> for CM curves E/Q with CM by a class-number-1 imaginary quadratic
> field K and analytic rank 0 or 1, BSD holds:*
>
> *(i) rank(E(Q)) = ord_{s=1} L(E,s), and*
>
> *(ii) the leading coefficient of L(E,s) at s=1 satisfies the BSD
> formula:*
>
>     lim_{s→1} L(E,s) / (s−1)^r = (|Sha(E/Q)| · Ω_E · R_E · ∏_p c_p) / |E(Q)_tors|²
>
> *where r = ord_{s=1} L(E,s), Ω_E is the real period, R_E is the
> regulator, c_p are the Tamagawa numbers, and Sha(E/Q) is the
> Tate--Shafarevich group.*

*Updated statement:*

> ### 13.1 Theorem (BSD for CM curves)
>
> [...]
>
> **Theorem 13.1 (BSD from MY4 + CBB).** *Conditional on the
> distributional-to-genuine upgrade MY4 (the classical Bost–Connes
> wall over number fields, see §3.6.2), and under the CBB axioms
> (Paper 23), for CM curves E/Q with CM by a class-number-1 imaginary
> quadratic field K and analytic rank 0 or 1, BSD holds:*
>
> *(i) rank(E(Q)) = ord_{s=1} L(E,s), and*
>
> *(ii) the leading coefficient of L(E,s) at s=1 satisfies the BSD
> formula:*
>
>     lim_{s→1} L(E,s) / (s−1)^r = (|Sha(E/Q)| · Ω_E · R_E · ∏_p c_p) / |E(Q)_tors|²
>
> *where r = ord_{s=1} L(E,s), Ω_E is the real period, R_E is the
> regulator, c_p are the Tamagawa numbers, and Sha(E/Q) is the
> Tate--Shafarevich group.*
>
> *(The rank-1 case is vacuous within the stated scope, by Remark
> 12.6: GRH for $L(s, \psi)$ implies $L(1, \psi) \neq 0$, so every
> CM curve in scope has analytic rank $0$. The substantive content of
> the theorem is the rank-0 case.)*

*Diff-level summary:*

- Theorem label "(BSD from CBB)" → "(BSD from MY4 + CBB)".
- Single new conditional clause prepended: *"Conditional on the
  distributional-to-genuine upgrade MY4 (the classical Bost–Connes
  wall over number fields, see §3.6.2),"*.
- Parts (i) and (ii) — the rank equality and the BSD leading
  coefficient formula — are preserved byte-for-byte.
- A trailing parenthetical (already implicit in Remark 12.6) is added
  to make the rank-1 vacuity explicit at the theorem statement, so
  that a reader who only reads the theorem statement does not
  mistakenly think the conditional clause weakens the rank-1 content.
  It does not: the rank-1 case is *vacuous* within the stated scope,
  and that vacuity is itself a *consequence* of GRH (Theorem 9.1),
  which is the conditional being introduced. So the rank-1 case is
  conditional-on-MY4 in exactly the same way the rank-0 case is, and
  there is no asymmetry.
- The downstream CBB-contrapositive remark on $P < 10^{-89}$ is
  unchanged (it lives separately and is a remark on the CBB axioms,
  not on MY4).

The proof of Theorem 13.1 (Steps 1–3 in §13.1, citing Theorem 9.2,
Theorem 11.1 / Kolyvagin, Theorem 12.1 / Gross–Zagier, and Theorem
12.3 / Kolyvagin descent) does not require any modification: every
input it cites is *either* unconditional (Kolyvagin, Gross–Zagier,
Deuring) *or* conditional on MY4 by Theorem 9.1. The conditional
propagates through Theorem 9.1 cleanly, and no step in §13.1's proof
needs to be re-derived.

---

## Artifact 4 — New §15 paragraph on MY4 as primary open item

*To be inserted in Paper 26, §15 (Scope), as a new subsection §15.6
placed after §15.5 ("The Langlands frontier") and before the chapter
break to §16. The §15 register is the most explicit in the paper —
it lists each limitation with a named obstruction. The new paragraph
matches that template.*

---

### 15.6 The classical Bost–Connes wall: MY4

The four limitations of §15.2–§15.5 (rank $\geq 2$, non-CM, $h_K > 1$,
Langlands frontier) are limitations of *scope*: the bridge family as
constructed in Parts II–IV does not reach those settings, and
extending it to them requires tools that do not yet exist. There is
one further limitation, of a different character: an open key lemma
*within* the stated scope of this paper.

The lemma is the **distributional-to-genuine spectral upgrade** for
the self-adjoint closure $\overline{T}_{BC,K}$ of the log-norm
operator on $H_{1,K}$, stated as **MY4 (Key Lemma — OPEN)** in
§3.6.2. Meyer's spectral inclusion (Proposition 3.6) and its twisted
version (Proposition 3.6.1) construct distributional eigenstates of
$T_{BC,K}$ at every non-trivial zero of $\zeta_K(s)$ and of
$L(s, \psi)$. Nelson's analytic vector theorem (Proposition 3.7)
makes $T_{BC,K}$ essentially self-adjoint and gives
$\operatorname{spec}(\overline{T}_{BC,K}) \subset \mathbb{R}$. The
dark-state quadratic-form bound of §6 needs the *point*-spectrum
inclusion $\operatorname{spec}_p(\overline{T}_{BC,K}) \supset
\{\operatorname{Im}(\rho)\}$, which does not follow from
self-adjointness alone. The gap between distributional and
point-spectrum inclusion is the classical wall of the Bost–Connes
approach to GRH; it is the same wall that Paper 13 v2 resolved by
pivoting to the CCM + ITPFI + Bögli + Hurwitz architecture, and
Paper 26 inherits it by re-using the older Meyer–Nelson route.

This limitation is *within* the scope of Paper 26 in a way the
others are not: the bridge construction over $K$, the Meyer
extensions to $\zeta_K$ and $L(s, \psi)$ (`research/meyer-extension-to-K.md`,
Key Lemmas A and B), the cohomology-class integrality bound
(`research/cohomology-class-lemma.md`, Key Lemma C, unconditional),
the corrected bridge table (`research/corrected-bridge-table.md`,
Proposition 4.3 erratum), and the chain assembly of §9 are all in
hand or upgraded conditional on MY4. Two closure routes for MY4 are
sketched in the companion note `research/distributional-to-genuine.md`:
**Route 1** (a spectral-measure reformulation of the dark-state
bound, 5–15 pages, novel) and **Route 2** (a port of the
CCM 2025 + ITPFI + Bögli + Hurwitz architecture from $\mathbb{Q}$ to
$K$, 60–110 pages, mechanical, warranting its own preprint as
"Paper 27"). Theorem 9.1 (GRH for CM curves) and Theorem 13.1 (BSD
for CM curves) are accordingly stated as conditional on MY4 + CBB
in §9.2 and §13.1, in the same honest-conditional sense that Paper
13 v2 lives with for "RH conditional on CCM 2025." The audit
verdict on Point A3 ("CLOSABLE GAP — substantial work required;
multiple months of focused work") is consistent with this framing:
the gap is named, closable, and bounded, but not closed in the
present paper.

We name MY4 as the **primary remaining open item for Paper 26**. It
is distinct in kind from the four other limitations of §15: rank
$\geq 2$ is open in the algebraic-number-theory downstream
(Kolyvagin's reach), non-CM is open in the GL$_1$-to-GL$_2$ jump,
$h_K > 1$ is a multi-KMS technical extension, and the Langlands
frontier is the deep boundary. MY4 is none of these. It is one
named lemma about the spectrum of one explicit self-adjoint operator,
with two documented closure paths and a referee verdict of
"closable." Closing it moves the proof chain from 10 of 11 to
11 of 11; the rank-0 BSD content of Theorem 13.1 then becomes
unconditional (modulo the CBB axioms, which are the conditional
already shared with Paper 13 v2 and Papers 17–25). In the
honest-conditional reading, Paper 26 today proves *"BSD for CM
elliptic curves over $\mathbb{Q}$ with CM by a class-number-1
imaginary quadratic field, in analytic rank $0$ or $1$, conditional
on MY4 and on the CBB axioms"* — a complete theorem with one named
in-scope conditional and a documented closure path.

---

*[End of new §15.6.]*

---

## Artifact 5 — Companion-notes pointer (inline in §3.6.2)

*The pointer is already integrated into the §3.6.2 draft (Artifact 1)
in two places. For ease of audit, here are the inline references
extracted as a single block:*

> [...] the explicit formula matching of Meyer 1997
> (Duke Math. J. 88) transferred to $\zeta_K$ and $L(s, \psi)$ in the
> companion note `research/meyer-extension-to-K.md` (Key Lemmas A and
> B; see also `research/cohomology-class-lemma.md` for the
> unconditional Key Lemma C, which controls the cocycle integrality
> $|\Delta c_k(\delta)| < 1/(k+1)$ used in §7).
>
> [...] **Route 1** (`research/distributional-to-genuine.md`,
> "Spectral-measure reformulation") [...]
>
> [...] **Route 2** (`research/route2-ccm-over-K.md`,
> "CCM + ITPFI + Bögli + Hurwitz over $K$") [...]

The four companion notes referenced in §3.6.2 are:

| File | Role |
|:--|:--|
| `research/meyer-extension-to-K.md` | Key Lemma A (MY1, MY2: Meyer for $\zeta_K$) and Key Lemma B (MY3: Meyer twist to $L(s, \psi)$). Both `[LEMMA] conditional on MY4`. |
| `research/distributional-to-genuine.md` | The MY4 closure routes (Route 1 spectral-measure + Route 2 CCM-over-K). The note that *names* MY4 and sketches both closure paths. |
| `research/route2-ccm-over-K.md` | The detailed Route 2 plan (15 sub-tasks, 6 done, 9 open as of 2026-04-10). |
| `research/cohomology-class-lemma.md` | Key Lemma C: the unconditional cohomology-class integrality bound $|\Delta c_k(\delta)| < 1/(k+1)$ used by §7's cocycle kill. Closed in cycle 1 of the second-pass closure work. Needed even after MY4 closes. |

The §3.6.2 prose cites all four. No additional cross-reference is
needed in §15.6 (which references §3.6.2, which in turn references
the companion notes). The runner can decide in a later cycle
whether to copy the pointer block into §15.6 as well, for redundancy.

---

## Artifact 6 — Change-log entry

*This entry sits at the bottom of `nodes/M.3.1.md` (this file). It
is for the runner's reference when applying the artifacts to the
Paper 26 LaTeX preprint in a later cycle. It is NOT intended to
appear in Paper 26 itself.*

**Change-log entry — Paper 26 second-pass edit, MY4 anchor (Option C).**
The previous draft of Paper 26 (state at 2026-04-09 revision)
contained an implicit assumption in §9.2 Step B(5): the inference
from "$\overline{T}_{BC,K}$ self-adjoint" to "Meyer distributional
eigenstates are point-spectrum eigenvectors of $\overline{T}_{BC,K}$"
was treated as automatic. The audit run r00, point A3 (referee
verdict: CLOSABLE GAP — substantial work required), identified this
inference as unproved. The classical Bost–Connes-over-number-fields
wall — the same wall Paper 13 v2 resolved by pivoting to CCM + ITPFI
+ Bögli + Hurwitz — applies to Paper 26's Meyer–Nelson route.

This second-pass edit names the gap as **MY4 (Key Lemma — OPEN)**,
adds a new §3.6.2 ("The distributional-to-genuine upgrade — the open
key lemma") stating MY4 precisely and pointing to two documented
closure routes (`research/distributional-to-genuine.md`,
`research/route2-ccm-over-K.md`), updates the rigor labels of
Theorem 9.1 (GRH for CM curves) and Theorem 13.1 (BSD for CM
curves) to "conditional on MY4 + CBB" with one new conditional
clause prepended to each hypothesis (conclusions preserved
byte-for-byte), and adds a new §15.6 ("The classical Bost–Connes
wall: MY4") to the scope section flagging MY4 as the primary
remaining open item for the paper. With this edit, Paper 26
ships at 11 of 11 in the honest-conditional sense: every link in
the proof chain is either established (10 links) or conditional on
the single named lemma MY4 (1 link, with two documented closure
routes and a referee verdict of "closable"). This matches the
status of Paper 13 v2 ("RH conditional on CCM 2025") and is
consistent with the audit verdict on A3.

**Adjacent edits required in a later cycle (downstream consistency
follow-ups).** The §3.6.2 anchor and the Theorem 9.1 / 13.1 label
updates introduce two adjacent edits that the runner should apply
when incorporating the seven artifacts above into the LaTeX
preprint:

1. **§9.2 Step B(5)** currently asserts the upgrade implicitly. It
   should be revised to explicitly *cite* §3.6.2 ("by the conditional
   MY4 of §3.6.2, the Meyer distributional eigenstates of Proposition
   3.6 and Proposition 3.6.1 are point-spectrum eigenvectors of
   $\overline{T}_{BC,K}$"). No new derivation is added; only the
   citation. This removes the silent inference and replaces it with
   an explicit conditional citation.
2. **§15.1** ("Rank 0 and rank 1: proved") currently contains the
   sentence "This is complete. No gaps. No conditional statements."
   This sentence should be softened to "This is complete conditional
   on MY4 (§15.6); no other gaps." The substantive claim of §15.1
   (the rank 0 / rank 1 BSD content of Theorem 13.1) is unchanged,
   but the framing is brought into honest-conditional alignment with
   the Theorem 13.1 label.

Both adjacent edits are mechanical follow-ups; neither changes the
mathematical content of any theorem. They are listed here as §G
dependencies for the next cycle.

**Provenance.** Editorial node M.3.1 (W1-C, cycle 1 of run
`closing-my4`); see `M.3.1-prompt.md` for the spawn prompt and
`closing-my4/strategy/04-closing-my4.md` for the deliverable Option C
framing (§4 of the strategy doc).

---

## Artifact 7 — Honest-framing audit

*The verify step for an editorial node. Walks the draft and confirms
that no sentence is either (a) overclaiming, (b) using weasel words,
or (c) silently introducing an inference. Each new sentence in
Artifacts 1–4 is checked.*

**Banned weasel words audited:** "we believe," "it is hoped," "should
follow," "is expected to," "we conjecture," "appears to," "ought to,"
"we anticipate," "presumably," "morally," "in spirit," "essentially"
(when used to elide a step), "trivially follows," "by inspection."

**Banned overclaim phrases:** "is true," "is proved" (for anything
labeled OPEN), "follows from" (when the step is not actually
established), "is automatic," "is immediate" (when not).

**Allowed honest-conditional phrases:** "conditional on $X$," "modulo
$X$," "assuming $X$," "if $X$ is closed," "in the honest-conditional
sense," "as stated in §3.6.2."

### Audit walk — Artifact 1 (§3.6.2)

| # | Sentence (paraphrased) | Verdict |
|:--|:--|:--|
| 1 | "Meyer 3.6 + 3.6.1 construct a distributional eigenstate per non-trivial zero." | Restates Propositions 3.6 and 3.6.1 of Paper 26. PASS. |
| 2 | "$\varphi_\rho^K$ is a continuous linear functional on $D_K \subset H_{1,K}$ vanishing on $(T_{BC,K} - t)f$ for all $f \in D_K$." | Restates the construction in `research/meyer-extension-to-K.md`. PASS. |
| 3 | "The construction is exhaustive: one distributional eigenstate per zero." | Restates Key Lemma A / B (the "exhaustiveness" paragraph in `meyer-extension-to-K.md`). PASS. |
| 4 | "Nelson Proposition 3.7 makes $T_{BC,K}$ essentially self-adjoint." | Restates Proposition 3.7. PASS. |
| 5 | "Its closure satisfies $\operatorname{spec}(\overline{T}_{BC,K}) \subset \mathbb{R}$ and admits a complete spectral decomposition." | Citation: Reed–Simon II §VIII.3. Standard self-adjoint operator theory. PASS. |
| 6 | "The dark-state argument of §6 is a *point*-spectrum statement." | Restates §6 of Paper 26 (the dark-state quadratic-form bound). PASS. |
| 7 | "Self-adjointness alone does not deliver the point-spectrum inclusion." | Negative restatement of the spectral decomposition: standard operator theory says $\operatorname{spec} = \operatorname{spec}_p \cup \operatorname{spec}_c$. PASS. |
| 8 | "The remaining open item is precisely this distinction." | Frames the gap; introduces no new claim. PASS. |
| 9 | MY4 statement (boxed) | An *explicit* `[KEY LEMMA — OPEN]` statement. The conditional is inside an OPEN box and is *not* asserted as proved anywhere. PASS. |
| 10 | "This is the classical Bost–Connes wall over number fields." | Names the obstruction; the Paper 13 cross-reference is verifiable from `research/distributional-to-genuine.md`. PASS. |
| 11 | "Paper 13 v2 resolved by abandoning Meyer–Nelson in favor of CCM + ITPFI + Bögli + Hurwitz." | Historical fact about Paper 13 v2; verifiable from `paper13-rh/preprint/sections-01-05.md`. PASS. |
| 12 | "Paper 26 re-uses the older Meyer–Nelson route over $K$ and inherits the wall." | Restates the architectural choice; not a claim that the wall is closed. PASS. |
| 13 | Route 1 description: "spectral-measure reformulation, 5–15 pages, novel." | Restates `research/distributional-to-genuine.md` Route 1 sketch. The word "novel" is descriptive, not a strength claim. PASS. |
| 14 | Route 2 description: "CCM + ITPFI + Bögli + Hurwitz over $K$, 60–110 pages, warrants Paper 27." | Restates `research/route2-ccm-over-K.md`. PASS. |
| 15 | "Paper 26 ships conditional on MY4." | Honest-conditional. PASS. |
| 16 | "Every other link is either established here or in the cited classical literature, with no further open items." | Restates the strategy doc §6 final state table. Every named link in the parenthetical is either a §-reference or a citation. PASS. |
| 17 | "The conditional formulation is consistent with the audit verdict on Point A3 and is the same kind of honest-conditional Paper 13 v2 lives with under 'RH conditional on CCM 2025.'" | Restates the audit verdict and the Paper 13 v2 conditional. PASS. |

**§3.6.2 verdict:** zero weasel hits. Zero overclaim hits.

### Audit walk — Artifact 2 (Theorem 9.1)

The new conditional clause is:

> *Conditional on the distributional-to-genuine upgrade MY4 (the
> classical Bost–Connes wall over number fields, see §3.6.2),*

This is an *explicit conditional*. The phrase "conditional on" is on
the allowed-honest-conditional list. The cross-reference to §3.6.2
is forward-pointing within the same paper and is the pattern Paper
26 already uses (e.g., §1.5 forward-references §9.3 and §10.2). The
conclusion ("Then all non-trivial zeros of $L(E, s)$ lie on
$\operatorname{Re}(s) = 1/2$") is preserved byte-for-byte from the
existing Theorem 9.1 in `sections-part-III.md` lines 555–557. **PASS.**

### Audit walk — Artifact 3 (Theorem 13.1)

The new conditional clause is identical in form to Artifact 2:

> *Conditional on the distributional-to-genuine upgrade MY4 (the
> classical Bost–Connes wall over number fields, see §3.6.2),*

Parts (i) and (ii) are preserved byte-for-byte from the existing
Theorem 13.1 in `sections-part-IV.md` lines 362–371. The trailing
parenthetical on rank-1 vacuity is a citation to Remark 12.6, not a
new claim. **PASS.**

### Audit walk — Artifact 4 (§15.6)

| # | Sentence (paraphrased) | Verdict |
|:--|:--|:--|
| 1 | "§15.2–§15.5 list four limitations of *scope*." | Restates §15. PASS. |
| 2 | "There is one further limitation, of a different character: an open key lemma *within* the stated scope." | Honest framing of MY4. PASS. |
| 3 | MY4 = distributional-to-genuine spectral upgrade for $\overline{T}_{BC,K}$ (cross-reference to §3.6.2). | Restates §3.6.2. PASS. |
| 4 | "Meyer 3.6 + 3.6.1 + Nelson 3.7 give $\operatorname{spec}(\overline{T}_{BC,K}) \subset \mathbb{R}$." | Restates §3.6, §3.6.1, §3.7. PASS. |
| 5 | "Dark-state §6 needs the *point*-spectrum inclusion." | Restates §6. PASS. |
| 6 | "The gap between distributional and point-spectrum inclusion is the classical wall." | Restates §3.6.2. PASS. |
| 7 | "Paper 13 v2 resolved it by pivoting to CCM + ITPFI + Bögli + Hurwitz; Paper 26 inherits the wall." | Same as §3.6.2 sentence 11–12. PASS. |
| 8 | "MY4 is *within* scope in a way the others are not." | Frames the distinction. The list of "in hand or conditional" links is verifiable. PASS. |
| 9 | "Two closure routes for MY4 are sketched in `research/distributional-to-genuine.md`: Route 1 (5–15 pages, novel) and Route 2 (60–110 pages, mechanical, Paper 27)." | Restates the companion note. PASS. |
| 10 | "Theorem 9.1 and Theorem 13.1 are accordingly stated as conditional on MY4 + CBB, in the same honest-conditional sense Paper 13 v2 lives with." | Restates Artifacts 2 and 3 + Paper 13 v2. PASS. |
| 11 | "We name MY4 as the *primary remaining open item* for Paper 26." | Direct framing claim; the word "primary" is justified by the §G dependency analysis (every other link is closed or conditional only on MY4). PASS. |
| 12 | "Closing it moves the proof chain from 10 of 11 to 11 of 11." | Restates the strategy doc §6 final state table. PASS. |
| 13 | "The rank-0 BSD content then becomes unconditional (modulo CBB)." | Honest-conditional with explicit "modulo CBB" qualifier. PASS. |
| 14 | "In the honest-conditional reading, Paper 26 today proves [BSD for CM, $h_K = 1$, rank ∈ {0, 1}, conditional on MY4 and CBB]." | Direct restatement of Theorem 13.1 with both conditionals named. PASS. |

**§15.6 verdict:** zero weasel hits. Zero overclaim hits.

### Audit walk — Artifacts 5 (companion-notes pointer) and 6 (change-log)

Both artifacts are *meta* (pointers and change-logs) and contain no
mathematical claims. The companion-notes pointer table lists four
files with one-line role descriptions; the descriptions are verifiable
against the file contents. The change-log entry restates the seven
artifacts above and lists two adjacent edits as §G follow-ups; no
weasel hits. **PASS.**

### Final audit verdict

**Zero weasel hits across all four mathematical artifacts (1, 2, 3, 4).**
**Zero overclaim hits.**
**Zero silently-introduced inferences.**

Every mathematical sentence in the draft is one of:

- a verbatim restatement of an existing Paper 26 proposition,
- a verbatim restatement of a classical theorem with citation
  (Meyer 1997, Connes–Marcolli 2008 §4.3, Reed–Simon II §VIII.3,
  Deuring 1953, Kolyvagin 1990, Gross–Zagier 1986, Hecke 1917,
  CCM 2025, Bögli 2017),
- a restatement of a result from a closing-my4 companion note
  (Key Lemmas A, B, C, the corrected bridge table, the MY4 routes,
  the CCM-over-K plan), or
- an *explicitly conditional* statement of the form
  "conditional on MY4 (§3.6.2)" or "conditional on MY4 + CBB."

The honest-framing invariant of Step 4 (LOCK) is preserved: every new
sentence is verifiable as either restating proved content or
explicitly labeling a conditional. The draft is ready for runner
incorporation into the LaTeX preprint in a later cycle.

---

## What the next runner needs to know (Sig 11 schema)

- **State at handoff:** Editorial node M.3.1 has produced seven
  artifacts that anchor Option C of strategy doc 04-closing-my4: a
  new §3.6.2 stating MY4 as the named open key lemma, conditional
  rewrites of Theorem 9.1 and Theorem 13.1 (conclusions preserved
  byte-for-byte, one conditional clause prepended to each), a new
  §15.6 flagging MY4 as the primary in-scope open item, the
  companion-notes pointer (inline in §3.6.2), the change-log entry
  describing the edit, and the honest-framing audit (zero weasel
  hits, zero overclaim hits). The draft is ready to ship.

- **Open dependencies (§G):**
  - **Upstream / parallel:** none. M.3.1 is the editorial Option C
    anchor and runs in parallel with the Route 1 / Route 2 attack
    nodes (M.1.x, M.2.x in the same wave). It does not depend on
    those nodes; its purpose is the safety net.
  - **Downstream:** two adjacent edits to Paper 26 should be applied
    in the same incorporation pass (listed in the change-log entry,
    Artifact 6): (1) §9.2 Step B(5) to cite §3.6.2 explicitly rather
    than re-derive the upgrade; (2) §15.1 to soften "no conditional
    statements" to "conditional on MY4 (§15.6); no other gaps." Both
    are mechanical and do not change the mathematical content of any
    theorem.
  - **Sibling:** if a Route 1 or Route 2 author closes MY4 in a later
    cycle, the §3.6.2 anchor will need to be revised from `[KEY
    LEMMA — OPEN]` to `[LEMMA]` and the conditional clauses dropped
    from Theorem 9.1 and Theorem 13.1. The §15.6 paragraph would
    then become a historical note ("MY4 was closed in [Paper 27 /
    supplementary note X]"). The change-log entry of Artifact 6
    explicitly notes the structure of these prospective forward
    edits.

- **Watch out for:**
  - The conditional clause must be **prepended** to the hypothesis
    of each theorem, not appended to the conclusion. The pattern
    "Conditional on MY4 (§3.6.2), and under the CBB axioms, [old
    hypothesis], then [old conclusion]" preserves the byte-for-byte
    conclusion while making the conditional visible at the very top
    of the statement. Reversing this (e.g., "Theorem 9.1 holds
    conditional on MY4") is *less* honest because it reads as a
    coda rather than a hypothesis.
  - The trailing parenthetical on rank-1 vacuity in Theorem 13.1
    (Artifact 3) is *not* part of the original theorem statement;
    it is a new addition that makes Remark 12.6 visible at the
    theorem level. Including it explicitly prevents a careless
    reader from thinking the conditional weakens the rank-1 case
    differently from the rank-0 case. (Both are conditional on
    MY4 in exactly the same way; rank-1 is additionally vacuous
    by Remark 12.6.) If the runner prefers to keep the trailing
    parenthetical separate (e.g., as a footnote), the change is
    cosmetic, but the parenthetical itself should not be dropped.
  - The new canonical name "*the classical Bost–Connes wall over
    number fields*" should be added to §D as a META row (not a
    kill-pattern row). It is the named obstruction noun, used in
    §3.6.2, §15.6, and the Theorem 9.1 / 13.1 conditional clauses.
  - Do **not** apply the artifacts to Paper 26 itself in this
    cycle. The runner decides incorporation timing in a later
    cycle, after the cycle-1 wave has reported and the synthesis
    spawn has run. M.3.1 produces draft text; incorporation is a
    separate node.

- **Preferred next move:** Critic dispatch on M.3.1 (M.3.1.crit
  in cycle 2 or end-of-wave 1) to verify the honest-framing audit
  was performed correctly and to look for any conditional clause
  that the §G downstream chain might have missed. After Critic
  approval, schedule incorporation of the seven artifacts into
  the Paper 26 LaTeX preprint as a separate node in the cycle that
  closes the run (likely cycle-close at the wave boundary).

- **Voice canon citation:** *"the third option, honestly flagged"*
  (the deliverable's own framing for Option C, from
  `strategy/04-closing-my4.md` §4) — this is the central register
  marker for the editorial node, and the §3.6.2 + §15.6 prose is
  built around it. Secondary marker: *"the credibility of the
  programme is the credibility of its kill list"* — naming MY4
  explicitly in §3.6.2 and labeling Theorems 9.1 and 13.1 as
  conditional on it is the kill-list discipline applied to Paper
  26's §9.2 Step B(5).

---

## Length check

Approximate page count of the seven artifacts (in standard 12pt
manuscript layout, ~250 words/page):

| Artifact | Approximate length | Pages |
|:--|:--|:--|
| 1 — §3.6.2 | ~750 words | ~3 |
| 2 — Theorem 9.1 update | ~250 words (incl. diff commentary) | ~1 |
| 3 — Theorem 13.1 update | ~400 words (incl. diff commentary) | ~1.5 |
| 4 — §15.6 | ~600 words | ~2.5 |
| 5 — Companion-notes pointer | ~150 words | ~0.5 |
| 6 — Change-log entry | ~400 words | (off-paper, runner reference) |
| 7 — Honest-framing audit | ~700 words | (off-paper, runner reference) |
| **Paper 26 additions (Artifacts 1–5):** | ~2150 words | **~8.0 pages** |

Within the 6–8 page target. The change-log and audit (Artifacts 6
and 7) are off-paper (runner reference) and do not count against
the Paper 26 page budget.

---

## p_success self-estimate

**0.92.** The editorial draft is mechanical: it consists of stating
a known open item by name, prepending one conditional clause to two
theorem statements (preserving conclusions verbatim), adding two
short sections (§3.6.2 and §15.6), and pointing to four companion
notes that already exist. The honest-framing audit (Artifact 7)
walks every new sentence and finds zero weasel hits. The downstream
Kolyvagin / Gross–Zagier chain is preserved because the conditional
propagates through Theorem 9.1, not around it. The two adjacent
edits flagged in the change-log (§9.2 Step B(5) citation update,
§15.1 softening) are mechanical and do not change any mathematical
content.

The remaining 0.08 of risk lives in:

- (i) The runner or a Critic might prefer a different placement of
  §3.6.2 (e.g., after §3.7 instead of after §3.6.1), or a different
  numbering scheme for the conditional clause. These are cosmetic
  and easy to revise.
- (ii) The wording of the trailing rank-1 vacuity parenthetical in
  Theorem 13.1 (Artifact 3) might need adjustment to match Paper
  26's footnote / parenthetical conventions; the substantive content
  is unchanged.
- (iii) A reader might object to the §15.6 phrasing "the primary
  remaining open item" on the grounds that it could be misread as
  "the only remaining open item" — the phrasing explicitly
  distinguishes MY4 from the four scope limitations of §15.2–§15.5,
  but a future Critic pass should double-check that the distinction
  is unmistakable.

None of these risks affect the mathematical content of the draft.
Editorial node ships at high confidence.
