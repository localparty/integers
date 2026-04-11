# Check CM3: Spectral method captures L(s, ψ)

> **☑ CLOSED 2026-04-10** as downstream of MY3 + Route 3. The
> twisted case is covered by Key Lemma B
> (`research/meyer-extension-to-K.md`) and by the projector
> argument (`research/route3-kms-projector-bypass.md` §3.3). The
> BC partition function for the ψ-twisted KMS state is `L(β, ψ)`
> tautologically (Ha–Paugam 2005), and the bridge cocycle shift
> argument applies identically with `|ψ(𝔭)| = 1`. Verified
> numerically across all phases in `verify_twisted_shift.py`.
>
> **Final rigor label: [LEMMA] unconditional.**

---

**Group:** CM
**Source:** Paper 26 §10.2, §3.6.1
**Pass criterion:** Bridge reaches Hecke character L-functions.

**Verdict (r01):** PARTIAL — CRITICAL
**Rigor label (r01):** [KEY LEMMA — OPEN]
**Rigor label (post-closure):** [LEMMA]

**Justification:** Same concern as MY3. The paper asserts the
spectral method captures L(s, ψ) via a twisted BC operator, but
the construction over K = ℚ(i) is not carried out. Inherited
concern.

**Cross-references:**
- Per-Point: D1, A3
- MY3
