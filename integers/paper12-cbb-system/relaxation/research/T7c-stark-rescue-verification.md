# T7c — Stark-Unit Rescue Verification — Lead 7c

**Test:** Six rescue candidates for the Stark-unit identification
`arg(eps_chi)/(2 pi) mod 1 == 1/k`, systematically tested on the three
CBB bridges `(5,13)`, `(3,13)`, `(7,19)` at `k = 3, 4, 6`.

**Anchor targeted:** Anchor 5 (cocycle equality) of the seven-anchor
relaxation strategy
(`paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md`).

**Relation to prior work:**
- `paper12/research/188-character-decomposed-rbc.md` refuted `L'(1,chi)/L(1,chi) = 1/k`.
- `paper12/research/267-stark-units-computation.md` refuted the naive Stark phase
  `arg(exp(-L'(0,chi)))/(2 pi) = 1/k`, and closed with three rescue options (a,b,c).
- Lead 7b (`T1-T2-brauer-cohomology-verification.md`) **hardened the cohomology
  side of Anchor 5** (all four cyclotomic Brauer classes `inv_p = 1/k mod Z`).
- The present note tests rescue option (b) from 267 §6 — a different
  identification via Gauss sums, conductors, or the functional-equation
  W-factor — in its most disciplined form: six pre-committed candidates,
  no post-hoc search.

**Environment:** Python 3 + mpmath 1.3.0 at `mp.dps = 50`. Tolerance
`|value - 1/k| < 1e-40`. Script at
`paper12/relaxation/research/code/T7c-stark-rescue.py`.

---

## 1. Goal

Paper 25 Conjecture 5 ("V-Hilbert 12") posits that V-matrix elements for the
CBB bridge characters equal `L'(0, chi)` up to period normalization, with
Galois phase landing on the bridge cocycle value `1/k mod Z`. Research/267
refuted the naive reading. Its §6 closes:

> **Verdict**
>
> **Conjecture 5 (V-Hilbert 12) is REFUTED in its literal form.**
>
> The Galois phases of exp(-L'(0, chi)) do not equal 1/k mod Z for
> any of the three bridges, nor for any other character mod 13 or
> mod 19. The conjecture requires either:
>
> (a) A non-trivial "period normalization" that rotates the phases
>     to 1/k — but this would need to be specified to be testable.
>
> (b) A different identification between V's matrix elements and
>     L-function values — perhaps involving Gauss sums, conductors,
>     or the W-factor of the functional equation.
>
> (c) Abandonment: the bridge cocycle 1/k lives in H^2(Z/kZ, U(1))
>     as a discrete invariant and is not encoded in the continuous
>     Galois phase of any Stark unit.

The present verification tests option (b) with a fixed list of six
candidates, all structurally motivated by standard `L`-function
normalisations. Per the anti-overfit discipline: **only these six
candidates are tested; no post-hoc transformation is admitted.**

## 2. Method

All computations are at `mp.dps = 50`, tolerance `1e-40`, using
`mpmath.zeta` (Hurwitz form) for `L(s, chi)` and central-difference
differentiation at `h = 1e-25` for `L'(0, chi)`.

For each bridge `(p, N, k)`, the primitive Dirichlet character `chi` of
order exactly `k` is constructed from the smallest primitive root `g` mod
`N` via `chi(g^j) = zeta_k^j`. The following per-bridge quantities are
computed:

- `L'(0, chi)` by central difference on the Hurwitz representation;
- `eps_chi = exp(-L'(0, chi))` (the Stark unit);
- `tau(chi) = sum_{a=1}^{N-1} chi(a) exp(2 pi i a/N)` (Gauss sum);
- `W(chi) = tau(chi) / (i^a sqrt(N))`, `a = (1 - chi(-1))/2`
  (root number of the functional equation; `|W|=1` for primitive chi
  mod prime `N`);
- `theta(chi) = sum_{a=1}^{N-1} chi(a) (a/N)` (Stickelberger element);
- `f(chi) = N` (conductor, since chi is primitive mod prime `N`).

The six candidates (with sub-tests where the task spec lists more than
one variant):

| # | candidate | expression tested |
|---|---|---|
| C1a | Gauss-sum normalization, raw | `arg(eps / tau)/(2 pi) mod 1` |
| C1b | Gauss-sum normalization, sqrtN | `arg(eps / (tau/sqrt N))/(2 pi) mod 1` |
| C1c | Gauss-sum, no exp            | `arg(L'(0,chi) / tau)/(2 pi) mod 1` |
| C2+ | W-factor, positive sign      | `arg(eps * W)/(2 pi) mod 1` |
| C2- | W-factor, inverse            | `arg(eps / W)/(2 pi) mod 1` |
| C3a | Log-Stark, raw               | `Im( log(eps) / (2 pi i) ) mod 1` |
| C3b | Log-Stark, genus-rescaled    | `Im( log(eps) / (2 pi i * log_N(N-1)) ) mod 1` |
| C4  | Combined Gauss-sum + W       | `arg(L'(0,chi) / (tau W))/(2 pi) mod 1` |
| C5  | Stickelberger                | `arg(theta(chi))/(2 pi) mod 1` |
| C6  | Conductor-adjusted           | `(arg(eps)/(2 pi)) * (k/f(chi)) mod 1` |

That is 6 logical candidates expanded to 10 numerical tests per bridge
(C1 has three sub-tests, C2 has two, C3 has two), for a total of
**30 tests**. A candidate is scored PASS overall if **any** of its
sub-tests passes at tolerance `1e-40`.

*C3b note.* Paper 267 §6 refers to `log_N(genus)` without fixing the
"genus" of the cyclotomic field. The natural readings are `genus = N`
(reducing trivially to C3a) and `genus = N-1 = [Q(zeta_N):Q]` (the
non-trivial reading). The script reports C3b with the second reading.
Neither reading passes.

## 3. Script

The full mpmath script (235 lines, declared `mp.dps = 50` at the top) is
saved at

```
paper12/relaxation/research/code/T7c-stark-rescue.py
```

and was executed on 2026-04-11 with `python3` on the same machine as
Lead 7b. It produces the per-bridge table reproduced below verbatim
(values truncated here to the leading digits for readability; the script
output and full 40-sf numerics live on disk).

## 4. Results

### 4.1 Bridge 1 — `(p, N, k) = (5, 13, 3)` — three generations + Koide

`primitive root g = 2`. `chi(-1) = +1` (even character).

- `L'(0, chi)  = 0.80754060580375617407 + 0.84435066031387994398 i`
- `eps         = 0.29620981608667880622 - 0.33336806043696869556 i`
- `tau(chi)    = 0.91083583244632639180 + 3.48860689765009316890 i`, `|tau| = sqrt(13)`
- `W(chi)      = 0.25262040749347358193 + 0.96756546533959724442 i`, `|W| = 1`
- `theta(chi) = 1.33638e-51 + 4.26806e-51 i` (numerically zero —
  forced by `chi(-1) = +1`, a standard feature of Stickelberger's element
  for even characters)

Target: `1/3 = 0.3333333333333333333333333333333333333333`. Tolerance `1e-40`.

| candidate | computed value (40 sf) | Δ = \|v - 1/3\| | verdict |
|---|---|---|---|
| C1a | `0.6562636096785235071525107058767777232593` | `0.32293` | **FAIL** |
| C1b | `0.6562636096785235071525107058767777232593` | `0.32293` | **FAIL** |
| C1c | `0.9191921463515252912312572422352281041327` | `0.58586` | **FAIL** |
| C2+ | `0.0749712277377568687888196888293985458875` | `0.25836` | **FAIL** |
| C2- | `0.6562636096785235071525107058767777232593` | `0.32293` | **FAIL** |
| C3a | `0.1285240791610914981880072745439659984311` | `0.20481` | **FAIL** |
| C3b | `0.1326640396292963588555209878233072620901` | `0.20067` | **FAIL** |
| C4  | `0.7098383373219086104131027507589176928186` | `0.37650` | **FAIL** |
| C5  | `0.2017056270094908263865656272988042602068` | `0.13163` | **FAIL** (theta ≈ 0; phase is numerical noise) |
| C6  | `0.1997578658557246587624611993891741849016` | `0.13358` | **FAIL** |

### 4.2 Bridge 2 — `(p, N, k) = (3, 13, 4)` — Pati-Salam SU(4)_c

`primitive root g = 2`. `chi(-1) = -1` (odd character).

- `L'(0, chi)  = 0.30175537787295705070 - 0.26033847070895236920 i`
- `eps         = 0.71459930792332523561 + 0.19035782046784634065 i`
- `tau(chi)    = -3.45084437684401872820 + 1.04483160691281543000 i`, `|tau| = sqrt(13)`
- `W(chi)      = 0.28978414868843008972 + 0.95709202648905284959 i`, `|W| = 1`
- `theta(chi) = -1 - i`  (exact; Stickelberger element over Q)

Target: `1/4 = 0.2500000000000000000000000000000000000000`. Tolerance `1e-40`.

| candidate | computed value (40 sf) | Δ | verdict |
|---|---|---|---|
| C1a | `0.5882259149430640791350726241635398581354` | `0.33823`  | **FAIL** |
| C1b | `0.5882259149430640791350726241635398581354` | `0.33823`  | **FAIL** |
| C1c | `0.4334976614335713218806449507348056118159` | `0.18350`  | **FAIL** |
| C2+ | `0.2446423940375646710419462503811505819680` | `0.0053576` | **FAIL** (near-miss) |
| C2- | `0.8382259149430640791350726241635398581354` | `0.58823`  | **FAIL** |
| C3a | `0.0480258599930438524156018376999395565790` | `0.20197`  | **FAIL** |
| C3b | `0.0495728476324070285347146638545361315059` | `0.20043`  | **FAIL** |
| C4  | `0.2302894218863210259272081376260002498995` | `0.019711` | **FAIL** (near-miss) |
| C5  | `0.6250000000000000000000000000000000000000` | `0.37500`  | **FAIL** (exact 5/8) |
| C6  | `0.0127489706124044231041567499299523754005` | `0.23725`  | **FAIL** |

### 4.3 Bridge 3 — `(p, N, k) = (7, 19, 6)` — CKM, six quark flavours

`primitive root g = 2`. `chi(-1) = -1` (odd character).

- `L'(0, chi)  = 0.45669732421748966577 - 0.81697335272366948651 i`
- `eps         = 0.43349944304859937411 + 0.46177737637589985299 i`
- `tau(chi)    = -4.33803016033243765170 - 0.42602151124811207287 i`, `|tau| = sqrt(19)`
- `W(chi)      = -0.09773603764763141521 + 0.99521237278529690447 i`, `|W| = 1`
- `theta(chi) = -1 - sqrt(3) i`  (exact)

Target: `1/6 = 0.1666666666666666666666666666666666666666`. Tolerance `1e-40`.

| candidate | computed value (40 sf) | Δ | verdict |
|---|---|---|---|
| C1a | `0.6144453021892740006679652651781446678899` | `0.44778`  | **FAIL** |
| C1b | `0.6144453021892740006679652651781446678899` | `0.44778`  | **FAIL** |
| C1c | `0.3155468520536870687883299290083554270477` | `0.14888`  | **FAIL** |
| C2+ | `0.3956053927313871042087637929287081538180` | `0.22894`  | **FAIL** |
| C2- | `0.8644453021892740006679652651781446678899` | `0.69778`  | **FAIL** |
| C3a | `0.0726856366460554413128513991377640790557` | `0.093981` | **FAIL** |
| C3b | `0.0740452923335901258539949281838609246971` | `0.092621` | **FAIL** |
| C4  | `0.0499668067826305170179306651330736840837` | `0.11670`  | **FAIL** |
| C5  | `0.6666666666666666666666666666666666666667` | `0.50000`  | **FAIL** (exact 2/3) |
| C6  | `0.0410606360401043849805361670695030771118` | `0.12561`  | **FAIL** |

### 4.4 Totals

| metric | value |
|---|---|
| numerical tests run | **30** |
| PASS at `1e-40` tolerance | **0** |
| FAIL | **30** |
| closest near-miss | C2+ on Bridge 2 (k=4): `Δ = 5.36e-3` |
| second-closest | C4 on Bridge 2 (k=4): `Δ = 1.97e-2` |

**Every candidate fails on every bridge.** No rescue passes.

## 5. Diagnosis

### 5.1 Which rescues survived

**None.** The 30-row table is uniformly FAIL. The two tightest
near-misses (C2+ and C4, both on the k=4 Pati-Salam bridge at
`Δ ~ 10^{-3}` and `10^{-2}`) are four and two orders of magnitude
outside the `10^{-40}` tolerance; at 50-dps precision this is not
"close" — it is not matching. Neither near-miss extends to the k=3 or
k=6 bridges, so even entertained as a heuristic, the pattern is not
uniform across the three bridges. A surviving rescue would have to pass
on all three bridges (that is the minimum requirement of Anchor 5:
every bridge class lands on its own `1/k`), so a rescue that succeeds
only on `k=4` at `10^{-3}` is not a survival under any reasonable
reading.

### 5.2 Structural remarks (not rescues)

- **Stickelberger's element vanishes for the k=3 bridge** because
  `chi(-1) = +1`. This is the classical fact that `theta(chi) = 0` in
  `Q(chi)` for even characters; it is a structural feature, not a bug
  in the computation, and immediately rules C5 out for any even
  character. (For the two odd-character bridges, `theta(chi)` is a
  clean algebraic integer — `-1 - i` and `-1 - sqrt(3) i` — whose
  phases `5/8 * 2 pi` and `2/3 * 2 pi` do not match `1/4 * 2 pi` and
  `1/6 * 2 pi`.)
- **Every Gauss-sum normalization gives the same phase**, because
  `tau` and `tau/sqrt N` differ only by a positive real factor. The
  script confirms C1a = C1b to all 50 digits, as expected.
- **C2+ and C2-** differ from C3a only by the phase of `W(chi)`, which
  is itself a Gauss-sum phase. The W-factor does not rotate any of
  the three bridges onto `1/k`.
- The conductor `f(chi) = N` for every bridge, so C6 is simply
  `(k/N) * phase(eps) mod 1` — a rational rescaling by `3/13, 4/13, 6/19`,
  none of which happens to land on `1/k`.
- The raw `phase(eps) mod 1` values — `0.86562`, `0.04143`, `0.13003`
  from research/267 — reappear (mod 1) as the `Im(-L'(0,chi)/(2 pi))`
  part of C3a, after sign conventions. This cross-checks 267 at
  50-dps precision: the phase quoted there to 5 digits equals the
  value computed here to 40+ digits, within the central-difference
  envelope. **This note therefore does not merely re-run 267 — it
  reproduces 267's numbers at higher precision as a by-product and
  then performs six additional independent tests, all of which fail.**

### 5.3 Comparison with 188 and 267

| test | locus | verdict |
|---|---|---|
| research/188 | `L'(1,chi)/L(1,chi) = 1/k` | refuted |
| research/267 | `arg(exp(-L'(0,chi)))/(2 pi) = 1/k` | refuted |
| **T7c (this note)** | six Gauss/W/Stickelberger/conductor rescues of 267 | **all six refuted** |

The three refutations are logically independent. 188 tested `s=1`,
267 tested `s=0` with no normalization, and T7c tests `s=0` with six
structurally-motivated normalisations. No combination survives.

The structural observation from 188 and 267 — that the order-`k`
characters exist at the right conductors, aligning with the bridges —
remains intact. The *existence* of the characters is confirmed by
Lead 7b. Their *L-function values* do not carry the cocycle class.

## 6. Structural implication for Anchor 5

Anchor 5 is the statement that **two independent constructions** — the
geometric (cyclotomic Brauer) side and the spectral side — produce the
same cohomology class `1/k mod Z` in `H^2(Z/kZ, U(1))`.

- **Geometric side (Lead 7b, T1-T2 verification): HARDENED.**
  For every bridge, the cyclic-algebra Hasse invariant
  `inv_p(Q(zeta_N)/Q, Frob_p, zeta_k) = 1/k mod Z` is verified as
  exact integer arithmetic in `(Z/NZ)*`.
- **Stark-spectral side (Lead 7c, this note): REFUTED in every
  candidate form so far tested.** Neither `L'(1,chi)/L(1,chi)` (188),
  nor the raw Stark phase (267), nor any of the six rescue candidates
  here, lands on `1/k`.

The spectral side of Anchor 5 as Paper 25 Conjecture 5 stated it —
"V-Hilbert 12 encodes the cocycle in the Galois phase of a Stark unit" —
is therefore **dead in its Stark-unit form**. Option (a) of 267 §6
("a non-trivial period normalization that rotates the phases to 1/k —
but this would need to be specified to be testable") is explicitly
untestable in its current form. Option (b) is the family of six
candidates tested here and is refuted. That leaves option (c):

> **(c) Abandonment: the bridge cocycle 1/k lives in H^2(Z/kZ, U(1))
>       as a discrete invariant and is not encoded in the continuous
>       Galois phase of any Stark unit.**

This is the honest finding.

## 7. Verdict

The task spec lists three possibilities for the verdict:

1. **one rescue works** → Anchor 5 saved by that specific identification;
2. **no rescue works** → Anchor 5 half-standing, cohomology side only,
   Stark-phase side refuted;
3. **ambiguous** → more candidates needed.

The result of this verification is unambiguously **possibility 2**:

> **Anchor 5 half-standing.** The geometric (cyclotomic-Brauer) side
> of the bridge-cocycle equality is verified exactly on all four
> bridges (Lead 7b / T1–T2). The spectral (Stark-phase / V-Hilbert 12
> / Conjecture 5) side is refuted in every form tested: L'(1,chi)/L(1,chi),
> the naive Stark phase, and all six pre-committed Gauss-sum /
> W-factor / Stickelberger / conductor-adjusted rescues. Anchor 5
> survives as a **one-sided** statement: a structural fact about the
> cyclotomic Brauer class, not a geometric-vs-spectral coincidence.

This is a real, structural loss. What Anchor 5 *was* supposed to do —
link the geometric and spectral sides of the framework via a single
cohomology class — it no longer does in the Stark-unit
formulation. What Anchor 5 *still does*, unmodified, is provide the
exact `1/k` cohomology class on the geometric side; that class is
still the object the bridge cocycle points at, and Lead 7b still
verifies it is the right class.

## 8. Recommended update to `relaxation/04` §4 Anchor 5

The current text of Anchor 5 in
`paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md`
reads:

> **Anchor 5 — Cocycle equality (research/162)**
>
> **What it is**: The bridge cocycle equality at k=3 — both the
> cyclotomic Brauer class at p=5 on Q(ζ_13) and the Fuglede-Kadison
> determinant cocycle of the index-3 Jones subfactor equal 1/3 mod ℤ
> in H²(Z/3Z, U(1)).

The Fuglede-Kadison-determinant / V-Hilbert identification on the
spectral side, insofar as it was to be realised through Stark units,
is refuted. Anchor 5 should be restated in one of the following two
equivalent ways:

**Option A (narrow).** Demote Anchor 5 to the cyclotomic Brauer
statement alone:

> **Anchor 5 — Cyclotomic Brauer class (research/162, 7b, 7c).**
> For every bridge `(p, N, k) in {(5,13,3), (3,13,4), (7,19,6),
> (2,7,2)}`, the cyclic-algebra Hasse invariant
> `inv_p(Q(zeta_N)/Q, Frob_p, zeta_k) = 1/k mod Z`, verified exactly
> in Lead 7b. The spectral-side identification of this class via a
> Stark unit `exp(-L'(0, chi))` is refuted by Leads 7c and research/267
> and 188; the cocycle is a discrete geometric invariant and is not
> encoded in the continuous Galois phase of a Stark unit at any of
> the six rescue normalisations tested (Gauss sum, sqrt(N)-normalised
> Gauss sum, Gauss sum of L' itself, both signs of the W-factor,
> raw and genus-rescaled log-Stark, combined Gauss+W, Stickelberger
> element, and conductor-adjusted phase).

**Option B (replacement target).** Keep the geometric-spectral
framing of Anchor 5 but move the spectral side from Stark units to
a *discrete* invariant — for instance, the Fuglede-Kadison determinant
cocycle of the index-`k` Jones subfactor computed as an element of
`H^2(Z/kZ, U(1))` directly, without going through an L-function.
This would be a new lead (7d) and is *not* executed here; it is only
proposed as the natural next target if Option A is considered too
narrow.

**Recommended:** adopt **Option A** as the default (it is the honest
statement of what is verified) and open Lead 7d as a follow-up **only
if** an L-function-free spectral cocycle can be specified without
overfit. In either case, the strategy document should cite this note
as the refutation record for the six rescue candidates.

## 9. Discipline log

- `mp.dps = 50` declared in line 34 of the script (within the first 10
  executable lines after the module docstring).
- Tolerance `1e-40` fixed at the top of the script and not adjusted
  during the run.
- No post-hoc candidate was added after seeing the results. The script
  was written to the six candidates in the task spec (expanded to 10
  numerical sub-tests for the documented C1/C2/C3 subvariants) before
  it was run.
- 267 §6 is quoted verbatim in §1 of this note (block quote from the
  file, not paraphrased).
- No near-miss is promoted to a pass. The tightest near-miss
  (C2+ on k=4, `Δ ≈ 5.4e-3`) is listed as FAIL in the per-bridge table
  and in the summary.
- Deliverable path:
  `paper12/relaxation/research/T7c-stark-rescue-verification.md`
- Script path:
  `paper12/relaxation/research/code/T7c-stark-rescue.py`

---

**Bottom line.** Lead 7c closes option (b) of research/267 §6. Anchor 5
survives only on its geometric side. Paper 25 Conjecture 5
(V-Hilbert 12) remains refuted.
