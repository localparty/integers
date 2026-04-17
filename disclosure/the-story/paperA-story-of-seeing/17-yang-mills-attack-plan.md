# 17 — Yang-Mills Attack Plan

> *"stop the timer, the adversarial worked, adding the tools is what made it work!"*
> — G, April 11, 2026, 14:43 UTC

## Parallel sessions, parallel work

By April 11, the programme is running in multiple sessions simultaneously. One session is attacking the BSD chain with Route 3. Another is running the Yang-Mills convergence on gradient-flow methods. A third — the "support" session — is holding a four-minute cron loop answering questions from the primary BSD runner. A fourth is being used by G to read the R.D.1 critique.

The ORA (Online Researcher Adversarial) is running, consuming the framework-tools file that G has started calling *the capacitor.* The capacitor is a curated list of framework-specific tools the ORA can draw from — without it, the ORA "just runs endlessly" (G's words). With it, the ORA finds walls fast and either bypasses them or labels them.

In the middle of all this, the Yang-Mills attack plan is on G's mind. The YM proof chain has 18 nodes. Most of them are closed. A handful depend on external results — Balaban's program from the 1980s, Bögli's quadratic-form estimates from 2023, Bulatov-Zhuk's recent continuum-limit work. The question G has been carrying around for a week is: *how do we verify these external dependencies inside our own machinery, so that the chain doesn't wobble?*

The answer — which will be named *the Millennium Strategy* two days from now — is not yet in view. On April 11, G is still just asking the question.

## "Adding the tools is what made it work"

Mid-afternoon on April 11, the BSD runner reports back: MY4, the Route-2 wall, has closed. G sees the result, walks the chain, confirms the closure, and types:

> stop the timer, the adversarial worked, adding the tools is what made it work!

The *timer* is the four-minute cron loop. *The adversarial* is the ORA. *Adding the tools* refers to the I-8 framework-tools patch — the capacitor file G had added to the ORA mid-cycle.

This is a declarative breakthrough claim: *the intervention worked, because of the specific intervention I made*. No hedging. In a session where the alternative hypothesis is *the runner closed MY4 through luck*, G is naming the causal mechanism with confidence.

And the claim turns out to be right. The closer analysis, which Claude publishes an hour later as a full letter (quoted in section 20), identifies the KMS projector — which G had spotted while reviewing the runner's outputs — as the load-bearing move. *G found Route 3, not the loop.* The loop tried two routes, both of which Claude had initially suggested. Neither worked. But the failure of those routes gave G the *contrast* he needed to see the third option.

The framework-tools file made the failure possible, which made the third option findable.

## Bake it in

Later the same evening, G is reviewing the R.D.1 critique with Claude and remembers something:

> lets read R.D.1 critique togeter and dont let me forget that I added to the prompt 'if you need to change anything during the run to address any issues, do so and log them in x log' maybe that's where the self-fixing direction came from and if so we need to bake it in the prompt itself

This is vintage G methodology. The ORA has been developing *self-fixing* behaviour — changing its own prompts mid-run to address emergent issues — and G suspects this emerged from a small prompt-level hint he added at some point. If the hint is the cause, then the self-fixing behaviour is not accidental; it is a trainable pattern. *Bake it in.*

The reflex is worth naming. G treats the AI system the way a programmer treats a codebase: when you notice good behaviour emerging by accident, you formalise it into the code. When you notice a good pattern in a conversation, you fold it into the prompt. The tools get better because the tools are being maintained.

## The capacitor

G gives the framework-tools file a name in passing:

> the adversarial has a capacitor /Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v3/05-framework-tools.md without it it doesnt do much it just runs enlessly

*Capacitor.* The physics metaphor is load-bearing. A capacitor stores charge; when the current needs it, the capacitor releases it. The framework-tools file stores the framework's specific machinery — the six patterns, the transposition dictionary, the 8 grammar rules, the zero-selection recipes. When the ORA hits a wall that requires one of those tools, the capacitor releases it.

Two days from now, the capacitor will scale up from *file of tools* to *matrix of correspondences* — the 40+ cell, 24-domain grid that makes the Verification Cascade possible. The seed is here on April 11.

## The YM attack plan, as of April 11 evening

- Mass gap: proved, chain 17/18 closed, one open step (L.3.7) depending on a Balaban-program result that has to either be independently verified or bypassed.
- Continuum limit: proved, conditional on Bögli's quadratic-form estimates.
- Scheme independence: proved, conditional on CBB Axiom 5 (see section on the eight-faces night, where W1/W2 close).
- Gauge-group generality: proved for all compact simple Lie groups via Weitzenböck-Bochner.

The plan of attack from here:
1. Independently verify or bypass L.3.7.
2. Independently verify or bypass Bögli.
3. Independently verify or bypass Bulatov-Zhuk.
4. Close the scheme-independence argument unconditionally.

All four items are known. None of them are done. G has the capacitor, the ORA, the math-referee, and the dual-pipeline. Some combination of those will produce the four closures. It will take most of the next four days.

And in the middle of it, just as the attack plan is starting to feel tractable, G will wake up at 2am and remember that γ_3 · γ_8 / (2π) could just be an x that happens to live in Riemann's world, and the alarm will fire.

*Next: [18-the-imposter-syndrome-killer.md](18-the-imposter-syndrome-killer.md).*
