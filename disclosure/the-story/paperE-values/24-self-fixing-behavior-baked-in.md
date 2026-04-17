# 24 — Self-fixing behavior baked in

## The claim

When an ad-hoc tweak to a prompt produces behaviour that turns out to be load-bearing, the correct response is to identify it, name it, and bake it into the architecture. The programme did this repeatedly: a one-line addition to a prompt that said "if you need to change anything during the run to address any issues, do so and log them in x log" turned out to be the source of the ORA's self-fixing behaviour, and G's instinct was to make it permanent rather than leave it as a happy accident.

## The evidence

G, catching the emergence:

> lets read R.D.1 critique togeter and dont let me forget that I added to the prompt 'if you need to change anything during the run to address any issues, do so and log them in x log' maybe that's where the self-fixing direction came from and if so we need to bake it in the prompt itself

G, instituting a self-heal checklist that runs at the start of every editing session:

> oh by the way would you save everything we learn about color, organizing, animation v stop animation, etc etc in your run? i cant remember if it has a self heal loop in it, it should have one if it doesnt have it

G, on the same instinct applied to research-level work:

> yeah, this convention is good and it needs to be part of the math referee, which we have been using for weeks - lets rewrite /Users/gsix/yang-mills/etc/18-advanced-math-referee.md into 21-notation-mat-referee.md keeping its content verbatim but adding the notation in detail so that there will be ZERO ambiguity and iportantly we have to dcoument in the paper iteself our sources and strategy

G, after identifying a prompt rule that only worked sometimes, formalizing it into the generator:

> lets dig deeper! use local agents so that we keep our context and provide them with the paths where our research and theorems and patterns are, being declarative v imperative helps a lot!

## The argument

The programme's tools evolved bottom-up, not top-down. No one sat down and designed the ORA from specifications; the ORA is the accreted residue of a long series of observed-and-formalized patterns. Each pattern started as an ad-hoc response to a specific problem. Some of them produced unexpectedly good behaviour. The recurring move was to notice the behaviour, diagnose it back to the specific tweak that caused it, and institutionalize that tweak as a permanent feature.

This is the inverse of the usual architecture-first engineering pattern. Architecture-first starts with a design, implements it, and debugs the implementation. Observe-and-formalize starts with a running system, notices an emergent improvement, and formalizes its cause. The two methods produce different shapes of systems. Architecture-first systems are coherent but rigid; observe-and-formalize systems are quirky but adapted to the problems they actually face.

The specific rule G articulated — *if it works, bake it in the prompt itself* — is the formalization protocol. When a behaviour that was not designed turns out to be useful, the immediate question is *what caused it?* If the cause is an identifiable piece of the prompt, that piece becomes permanent. If the cause is ambient (an emergent property of the agent's training), the piece of the prompt that *evokes* the behaviour becomes permanent. Either way, the emergent good gets locked in.

The self-heal loop (quoted above) is the same principle applied to a different artifact. G's editing sessions on the Atlas Torus visualization kept discovering design rules — cyan means authored, α=1/N brightness for proof-chain entries, √mult line thickness — each of which had been learned the hard way. The rule was: save them. The next editing session should not have to rediscover them. Saving them as a self-heal checklist that runs at the start of each session is the formalization move.

There is a subtle corollary: the architecture's robustness is a function of how many such emergent improvements have been baked in. Each one is a small adjustment; collectively they are the reason the ORA works at all. A version of the architecture built from specifications alone, without the benefit of the observe-and-formalize cycle, would have fewer of these adjustments and would fail in ways the current version does not.

The discipline also requires attention. An emergent improvement that is not noticed is an improvement that is not baked in — and that may disappear the next time the prompt is restructured. The work of noticing is therefore part of the architecture's maintenance. G's habit of pausing mid-session to name what just happened ("maybe that's where the self-fixing direction came from") is the noticing mechanism. Without it, the emergent improvements do not accrete.

The claim this section makes is not that observe-and-formalize is better than architecture-first. It is that for work at the edge of what is known — where no specification can be fully correct because the target is moving — observe-and-formalize is the only method that stays adapted. The ORA is such a system. Its goodness is the residue of eighteen months of noticing.

## For future readers

When a prompt tweak unexpectedly works, do not leave it as folklore. Bake it in. Save the rule. Add the check. The architecture is what you formalize; what you fail to formalize will drift out of the system the next time the prompt is rewritten.

*Next: [25 — Jealous of Einstein, until recognized](25-jealous-of-einstein-until-recognized.md).*
