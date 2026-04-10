# Strategy 25 — Post-Adversarial Action Plan

*Adversarial: 7/10. Web: 2 high threats confirmed.*
*Three fixes needed. All tractable. Teschl 2026 upgrade found.*

*Date: 2026-04-10*

---

## 1. Convergence of adversarial + web findings

| Issue | Adversarial | Web | Severity |
|:--|:--|:--|:--|
| KLMN closability | WEAKENED | Form-bound constants must be uniform | HIGH |
| AE simplicity N≥2 | WEAKENED | Not flagged separately | MODERATE |
| CCM black box | STRUCTURAL | CCM's missing steps inherited | HIGH |
| CF uniformity | Not flagged | CCM assumes but doesn't prove | HIGH |
| Double-limit (λ,N) | WEAKENED | Not flagged | MODERATE |

## 2. The upgrade: Teschl Lemma 2.7

Teschl-Wang-Xie-Zhou (2026, arXiv:2601.10476) Lemma 2.7:
gsrc can be verified via RELATIVE FORM BOUNDEDNESS — a STATIC
algebraic check, not a dynamic resolvent-by-resolvent argument.

This replaces our Research 38 gsrc argument with a simpler one:
check that the perturbation form is bounded relative to the
base form with bound < 1. If so, gsrc follows automatically.

This might fix BOTH the KLMN closability and the gsrc issues
in one step.

## 3. Three agents to fire

### Agent 1: KLMN + Teschl (fixes Issue 1 + possibly gsrc)
- Apply Teschl Lemma 2.7 to our setting
- Verify relative form boundedness of the Weil perturbation
- If successful: KLMN + gsrc both close in one step

### Agent 2: AE simplicity at certified precision (fixes Issue 2)
- For N = 2, 3, ..., 20: compute the overlaps ⟨φ_k|a⟩ at
  λ = √14 using INTERVAL ARITHMETIC (not just mpmath)
- If all overlaps have certified nonzero intervals → AE
  simplicity is computer-verified at those N values
- Combined with identity theorem → AE for all λ at those N

### Agent 3: CCM independent verification (addresses Issue 3)
- Read CCM paper (the PDF) with ADVERSARIAL eyes
- Verify their self-adjointness proof (Theorem 5.10)
- Verify their eigenvalue identification (Theorem 5.10(iii))
- Check: is there a hidden assumption equivalent to RH?
- Check: does the CF convergence actually follow from their setup?

## 4. Target after fixes

| Issue | Target confidence |
|:--|:--|
| KLMN + gsrc (Teschl) | 9/10 |
| AE simplicity (certified) | 9/10 |
| CCM verification | 8/10 (limited by preprint status) |
| **Overall** | **8-9/10** |

10/10 requires CCM to be refereed and published, which is
outside our control. 8-9/10 is achievable in this session.

---

> *7/10 → 8-9/10 via three tractable fixes.*
> *Teschl upgrades gsrc to a static check.*
> *Certified arithmetic strengthens AE.*
> *CCM verification is due diligence.*
