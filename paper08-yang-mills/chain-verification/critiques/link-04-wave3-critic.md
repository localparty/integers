# Link 4 Wave 3 Critic Verdict

**Target:** (B1) analyticity of polymer activities, k-independent radius
**Wave:** 3 (independent adversarial re-check of Wave 2 Author's repair)
**Author repair verdict under attack:** WEAKENED → claimed VERIFIED
**Wave 3 verdict:** WEAKENED (residual gap; repair incomplete on two counts)
**Confidence:** 8/10

---

## Primary source verification protocol

The PDF `journals/balaban-CMP109-1987.pdf` was read directly (journal pages
249–301, PDF pages 1–40). All citations below are verified against the scan.
No secondary paraphrase substituted for primary-source text.

---

## Vector A — Citation content

### A1: Page numbers

**CMP 109 §1 conditions, p. 262.** CONFIRMED. The space $U^c_j(X, \alpha_0,
\alpha_1)$ is defined on p. 262, and conditions (i)–(iv) appear there.
Small-field condition (1.2) is on p. 260.

**CMP 109 §3 Lemma 4, p. 280.** CONFIRMED. Lemma 4 appears exactly at p. 280
and its statement matches the Author's verbatim quote in substance.

### A2: Condition count — ATTACK LANDS (minor)

The Author's insertion cites "CMP 109 §1 conditions (i)–(iii) (p. 262)" in
both the repair body and the proposed sentence. Direct reading of p. 262
shows the $U^c_j$ domain is defined by **four** conditions (i)–(iv), not
three. Condition (iv) specifies the sequence of maximal domains
$\{\Omega_n\}, n = 0,\ldots,j$, and the functions $U_n(V)$ in axial gauges
(eqs. 1.15–1.16). This is not a trivial condition: it encodes the iterative
gauge-fixing structure that ties the minimal configuration $U_k(V)$ to the
background $V$ across scales. Citing only (i)–(iii) is technically
incomplete. A referee who checks p. 262 will find four conditions, not three,
and will notice the omission of condition (iv).

**Severity:** LOW but real. The repair as written contains a verifiable
inaccuracy in the citation. Fixing "conditions (i)–(iii)" to "conditions
(i)–(iv)" is a one-word change.

### A3: What Lemma 4 actually proves — ATTACK LANDS (substantive)

The Author claims Lemma 4 "guarantees that the saddle-point + composition
output again belongs to the domain $U^c_j(X, \alpha_0, \alpha_1)$, placing
it well inside the Mayer domain, not merely at its boundary." This
characterisation is misleading in a material way.

Lemma 4's hypothesis is $\mathbf{U} \in U^c_{k+1}(\square_0,
(1+2\beta)\alpha_0, (1+2\beta)\alpha_1)$ and its conclusion is that
$(U_j(\square_0, \exp i(\tau B + B')), J_j(\square_0, \exp i(\tau B +
B')))|_X \in U^c_j(X, \alpha_0, \alpha_1)$. The objects $B, B'$ are
**fluctuation fields** — not the saddle-point configuration
$u_{\mathrm{cl}}[V_0]$. Lemma 4 controls the Mayer/fluctuation-field step:
given that the background **U** belongs to an inflated domain, it shows
the output of averaging over a small fluctuation $B'$ (satisfying $|B'| <
\alpha_3$) lands in the uninflated domain. This is the **fluctuation
integration step**, not the saddle-point step.

The saddle-point center condition — that $u_{\mathrm{cl}}[V_0] =
-G_k(V_0)\cdot\nabla_u S_{k-1}|_{u=0}$ lies strictly inside the Mayer
domain — is controlled in CMP 109 at an earlier stage: the small-field
hypothesis (1.2) on p. 260 bounds $|V^{(k)} - \bar{U}| < O(1)\varepsilon_0$
(see §0, p. 254–255 text on the regularity of $U_0$), and the saddle-point
analysis in §2 establishes that $V^{(k)} = V^{(k)}(W)$ (eq. 2.3) inherits
this regularity. Lemma 4 is invoked **after** the saddle-point step, to
handle the fluctuation integral, not to establish the center condition for
the saddle-point output itself.

**Therefore:** The Author has cited the right Lemma for the right overall
purpose (domain tracking across one RG step) but has attributed to Lemma 4
a role it does not directly play (establishing the saddle-point center
condition). The actual authority for the center condition is the §2
saddle-point analysis together with the small-field hypothesis (1.2),
neither of which is named in the proposed insertion.

**Consequence:** The proposed one-sentence insertion resolves the Wave 1
gap symptomatically (adds a citation) but not mechanically (the citation
does not do the advertised work). A referee who reads Lemma 4 will see it
is about fluctuation fields $B, B'$, not about $u_{\mathrm{cl}}[V_0]$.
The repair requires a second sentence naming CMP 109 §2 (saddle-point
existence, p. 265: eq. 2.2–2.3) as the direct authority for the
saddle-point center condition, with Lemma 4 cited for the subsequent
fluctuation-integration step.

### A4: The Wave 1 Critic's framing

Wave 1 cited "CMP 109 §3" as a single shorthand for the inductive
hypotheses. The Author calls this "slightly imprecise" and asserts both §1
and §3 must be named. The disambiguation is warranted: §1 states the
conditions, §3 invokes them. However, the Author's own fix is also imprecise
in the ways identified above. The Wave 1 framing was adequate as a gap
description; the Author's repair is not adequate as a resolution.

---

## Vector B — Preprint edit

**Target location:** `preprint/sections/H-balaban-analyticity.md`, §3 "The
Logical Chain", Step (b), final sentence (line 132).

**Verbatim end of Step (b):** "Each step preserves analyticity; the
composition has radius bounded below by the minimum at any step."

CONFIRMED by direct read of H-balaban-analyticity.md, line 132. The target
location exists and the "from" text matches exactly.

**The proposed insertion** is syntactically well-formed and placed at the
correct location.

**However:** the content of the insertion contains the errors identified in
Vector A2 and A3:

- "CMP 109 §1 conditions (i)–(iii)" should be "(i)–(iv)."
- The insertion attributes to Lemma 4 the task of placing $u_{\mathrm{cl}}[V_0]$
  inside the Mayer domain. As argued in A3, Lemma 4 does not address
  $u_{\mathrm{cl}}$ directly; it addresses the fluctuation composition step.
  The insertion as written will not survive a referee reading Lemma 4.

**Net verdict on Vector B:** Location is correct; content requires revision
before the edit is applied.

---

## Vector C — Saddle-point center condition: extrapolation?

The Author's thesis is that "CMP 109's conditions guarantee the saddle-point
output stays in the required domain." The mechanism the Author points to
(Lemma 4 + §1 conditions (i)–(iii)) is a plausible but imprecise route.
The actual Balaban argument works as follows:

1. The background $V$ satisfies the small-field condition (1.2) of §1 by
   the inductive hypothesis (Theorem 3, p. 264: "the sequence of actions
   $A_k$... satisfy all the inductive assumptions (1.1)–(1.22)").

2. The saddle-point $V^{(k)}(W)$ is defined as the unique minimizer of
   $V \mapsto \mathbf{G}(V) + A(U_k(V))$ (eq. 2.2). Its regularity (size)
   is controlled by the bounds in §2, notably that $W$ is regular and the
   characteristic function $\chi_k$ restricts to configurations for which
   $U_{k+1}(W) \in U_k(\varepsilon_0)$ (p. 265).

3. Only at the next stage (§3 Lemma 4) is the full $U^c_j$ membership of
   the composed output established — and that membership is for the
   fluctuation-composed pair $(U_j, J_j)$, not for the raw saddle-point
   output.

This is not an extrapolation: the chain does close, and the center condition
is implicitly handled. But the repair should cite CMP 109 §2 (saddle-point
existence and regularity, pp. 265–268, eq. 2.1–2.3) as the primary
authority, with §3 Lemma 4 as the subsequent fluctuation step.

---

## Vector D — Cross-node consistency

Link 5 (B2, SL(N,ℂ) extension) was adjudicated SURVIVED by the Wave 1
Critic (link-05-critic.md). Link 5's argument rests on the polar
decomposition analyticity, det(V) = 1 polynomial structure, and Cauchy
estimates — none of which depend on the center condition or on the specific
citation in Lemma 4. The citation change in Link 4's repair does not
affect Link 5. No cascade.

Link 10 (non-pert dev ≥ 2) uses (B1) as a black box. The black box is
still functional: analyticity with k-independent radius is established even
if the specific citation support for the center condition is imprecise.
No cascade.

---

## Vector E — Bonus grep: CMP 109 citation consistency

Full grep across `preprint/**/*.md` reveals the following inconsistency:

- `H-balaban-analyticity.md` §3 Step (b) source line: "CMP 95–96 (propagator),
  CMP 98 (kernel), CMP 109 (inductive construction)" — no specific section.
- `H-balaban-analyticity.md` §3 Step (c) source line: "CMP 109, Section 3
  (inductive hypotheses)" — §3 for uniformity in k.
- `05-continuum-limit.md` line 1628: "convergent series of analytic cluster
  activities (CMP 109, **Sec. 4**)" — §4 for the Mayer/cluster-activity step.
- `05-continuum-limit.md` line 1635: "CMP 109, Sec. 3; CMP 119, Sec. 2" for
  uniformity in k.
- `L-clay-conjectures.md` line 612: "CMP 109, inductive hypotheses" for
  $\kappa$ k-independence.

The preprint is internally inconsistent on whether the cluster-activity
analyticity is in CMP 109 §3 or §4. Direct reading confirms:
- §3 (pp. 269–280) is "An Expansion of Terms in Fluctuation Field Integral,
  and Preliminary Analytic Extensions" — this is where Lemma 4 lives and
  where the analytic extension of the expansion terms is constructed.
- §4 (pp. 281+) is "Ward-Takahashi Identities and Their Consequences."

The citation in `05-continuum-limit.md` line 1628 that points to "CMP 109,
Sec. 4" for cluster activities is **incorrect**: the relevant material is in
§3. This is a pre-existing error in the preprint, not introduced by the
Author's repair, but it should be flagged.

**Net finding:** The Author's repair correctly points to §3 for the analytic
extension; the preprint has a pre-existing incorrect citation to §4 that
should be corrected independently.

---

## Summary of findings

| Vector | Attack result | Severity |
|--------|--------------|----------|
| A2: conditions (i)–(iii) vs. (i)–(iv) | LANDS | LOW |
| A3: Lemma 4 misattributed to saddle-point center condition | LANDS | MEDIUM |
| B: preprint edit location | confirmed correct | — |
| B: preprint edit content | requires revision | MEDIUM |
| C: saddle-point center extrapolation | partial extrapolation confirmed | MEDIUM |
| D: cross-node consistency | no cascade | SOUND |
| E: bonus grep | pre-existing §4 vs. §3 inconsistency found | NOTE |

---

## Required repairs (Wave 3 prescription)

**R1 (trivial):** In the proposed insertion, change "conditions (i)–(iii)"
to "conditions (i)–(iv)."

**R2 (substantive):** Split the proposed insertion into two sentences:

- Sentence 1 (saddle-point center condition): "The center condition for the
  saddle-point output $u_{\mathrm{cl}}[V_0]$ — that it lies in the small-field
  region required by the next composition step — follows from the small-field
  inductive hypothesis (1.2) of CMP 109 §1 (p. 260) enforced at each scale
  by Theorem 3 (p. 264): the background $V$ satisfies $|(\partial V)(p) - 1|
  < \varepsilon_0\eta^2$ on $T$, and the saddle-point analysis of CMP 109 §2
  (eqs. 2.2–2.3, pp. 265–266) shows the minimizer $V^{(k)}(W)$ inherits this
  regularity."

- Sentence 2 (fluctuation composition step): "CMP 109 §3 Lemma 4 (p. 280)
  then guarantees that the output of the subsequent fluctuation integration —
  the pair $(U_j(\square_0, \exp i(\tau B + B')), J_j(\square_0,
  \exp i(\tau B + B')))|_X$ — belongs to the domain $U^c_j(X, \alpha_0,
  \alpha_1)$ (conditions (i)–(iv), p. 262) for $\alpha_0, \alpha_1, \alpha_3$
  sufficiently small, confirming domain-membership through the full
  saddle-point + Gaussian + Mayer pipeline."

**R3 (preprint-wide, independent of Link 4):** Correct the citation
"CMP 109, Sec. 4" in `05-continuum-limit.md` line 1628 to "CMP 109, Sec. 3."

---

## Verdict

**WEAKENED.**

The Wave 2 repair is structurally sound in intent and the cited primary
sources are real and at the correct page numbers. However, two residual
gaps survive adversarial check:

1. The condition count (i)–(iii) is verifiably wrong (should be (i)–(iv));
   a referee who opens p. 262 will notice immediately.

2. Lemma 4 is misattributed: it governs the fluctuation-composition step,
   not the saddle-point center condition. The saddle-point center condition
   needs a separate citation to CMP 109 §2 (eqs. 2.2–2.3). As written, the
   insertion will not survive a referee who reads Lemma 4 carefully.

Neither gap is mathematical: the chain closes, the center condition is
handled by Balaban, and no logical hole is introduced. Both gaps are
citation-precision failures that require the two-sentence repair in R1–R2
above. Apply R1–R2; Link 4 becomes VERIFIED.

---

## Summary (≤150 words)

Wave 2's repair has correct page numbers and the right overall intent, but
two citation-precision failures survive adversarial check. First: the
Author cites "conditions (i)–(iii)" at p. 262, but the $U^c_j$ domain is
defined by four conditions (i)–(iv); condition (iv) (iterative gauge-fixing
sequence) is part of the definition and should be cited. Second: Lemma 4
(p. 280) is about the fluctuation-composition step — it handles the pair
$(U_j, J_j)$ after integrating a fluctuation $B'$ — not about the
saddle-point center condition for $u_{\mathrm{cl}}[V_0]$. That center
condition is controlled by CMP 109 §2 eqs. 2.2–2.3 (saddle-point
existence and regularity), not Lemma 4. The repair requires splitting the
proposed sentence into two: one citing §1 + §2 for the saddle-point center
condition, one citing §3 Lemma 4 for the fluctuation composition. No
logical gap; no cascade to Links 5 or 10. Status: WEAKENED pending R1–R2.
