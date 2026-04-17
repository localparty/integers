# 22 — Rock-solid citations

## The claim

Every citation in the papers has to resolve. Not *mostly* resolve — every one. When Claude found the full text of a journal article that the draft cited, G immediately proposed extending the verification to the rest of the bibliography, prioritized by risk. The discipline is mechanical, tedious, and non-negotiable. It is also one of the cheapest defences against the most common failure mode of ambitious papers: broken, misattributed, or misremembered references that give an adversarial reader easy wins.

## The evidence

G, after seeing one successful citation verification:

> do you think you can help me doing the same for the most relevant/dangerous/weak citations? this would make our paper rock solid

G, on LaTeX errors as a credibility issue:

> we can't ignore those errors because it means that our pdfs are gonna have render errors that will impact the readability and therefore credibility, so i'm happy that the errors are being thrown, we can't swallow or ignore them, we just have to keep progressing like we did this am - run - fix in a cycle until we're down to zero

Claude, catching eight citation errors in an early automated sweep:

> [Citation verifier identified 8 errors across the bibliography — several wrong page numbers, two misattributed results, one broken DOI, others]

G, on why the methodology is load-bearing:

> we have to dcoument in the paper iteself our sources and strategy

## The argument

Citations are a surface feature with a disproportionate effect on credibility. A reader encountering a wrong page number, a misattributed theorem, or a broken DOI concludes that the paper was written carelessly — and from that conclusion often extrapolates that the *content* may also be careless. The inference is not fully warranted, but it is predictable. Defending against it is cheap.

G's rule extends single-citation verification into a systematic most-dangerous-first audit. The prioritization is pragmatic: citations that are central to a load-bearing argument are more dangerous than citations that are ornamental. A wrong citation for a casually named theorem is embarrassing; a wrong citation for the theorem a whole section depends on is substantive. The audit starts at the central citations and works outward.

The "most-relevant/dangerous/weak" framing — G's own phrasing — captures three distinct failure modes:

- **Relevant** means the citation is used in a load-bearing argument; if the citation does not support the claim, the argument fails.
- **Dangerous** means the citation is to a contested or easily-misread result; even if the citation is technically correct, an adversarial reader may interpret it differently.
- **Weak** means the citation is to an unverifiable or low-quality source; even if the claim is supported, the sourcing undermines credibility.

All three require verification; the priority among them depends on the paper. For the QG5D papers, the load-bearing citations are the most relevant; for the RH and BSD papers, the dangerous ones (e.g., claims about the Connes-Consani-Marcolli programme or the Hasse-Brauer-Noether sequence) got extra attention because an adversarial reader would be expected to test those hardest.

The connection to the LaTeX-errors rule (quoted above) is that both are instances of the same discipline: do not leave surface defects in the output. A render warning is a signal that the pipeline produced something it cannot fully guarantee; the warning is to be treated as a bug. A broken citation is a signal that the bibliography was not verified; the broken citation is to be treated as a bug. Both are fixed until the count is zero. *Run-fix in a cycle until we're down to zero* is the same instruction applied to both artifacts.

The requirement "*we have to document in the paper itself our sources and strategy*" generalizes the rule beyond bibliography. The paper should be self-auditable: a reader should be able to check not only *that* a citation is accurate but *why* it was used. For load-bearing citations, the paper states the role of the cited result in the argument, which prevents a later misreading and gives the reviewer a target to check against.

The effort cost is real. A full citation verification pass over a ten-paper bibliography is a significant expenditure. The payoff is that no adversarial reader gets the free shot of pointing at a broken reference and letting the rest of the paper be judged by that error. The surface is clean, so the argument can be judged on its content.

## For future readers

Do a citation audit. Prioritize the most relevant, the most dangerous, and the weakest. Fix every one. The effort is unglamorous and the payoff is that the reader's first impression of your paper is not of careless sourcing. Make the surface rock-solid so the content carries the weight.

*Next: [23 — Bind to as many ends as possible](23-bind-to-as-many-ends-as-possible.md).*
