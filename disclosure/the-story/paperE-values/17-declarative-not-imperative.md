# 17 — Declarative, not imperative

## The claim

When dispatching sub-agents, G's rule is to describe the *state the work should end in*, not the *sequence of steps the agent should execute*. Declarative prompts preserve context across the agent boundary; imperative prompts do not. The rule sounds minor; in a programme running hundreds of parallel agents, it is the difference between a coherent multi-session run and an expensive drift.

## The evidence

G, stating the rule cleanly at 6am:

> lets dig deeper! use local agents so that we keep our context and provide them with the paths where our research and theorems and patterns are, being declarative v imperative helps a lot!

G, on the backticks strategy — where the same distinction shows up as "separate the agentic from the deterministic":

> however i don't think you understood my backticks strategy, the first step was to have an agentic run asking please wrap every expression into backticks and you would have all the .md files processed and then you'd kick in - thats 100% deterministic

G, pivoting to per-paper referee (a declarative description of what each agent should *be*, not what they should *do*):

> i have a better idea, i think - you are right, the topics are heterogeneous and distinct per paper and having a generalist will not be as thorough as we need lets make a prompt for each paper, listing in each paper the topics that the run should be an expert of

G, later, on traceability — declarative in a different dimension:

> before getting started, when you enage with agents can you write down their prompt in the same directory that they are gonna be delivering their ouput and instruct them to "read this"? that way we have full visibility on what we asked and what was delivered?

## The argument

Imperative prompts ("first do X, then do Y, then check Z") give an agent a procedure. The agent executes the procedure, possibly well, possibly poorly, depending on how well the procedure anticipates the situations the agent will encounter. When something the procedure did not anticipate comes up, the agent has no principled way to recover; it either improvises (which often drifts from what the principal actually wants) or fails.

Declarative prompts ("the output should be in this state, with these properties, sourced from these paths, consistent with these constraints") give an agent a specification. The agent can use any procedure to reach the specification, including procedures the principal did not anticipate. When something novel comes up, the agent can evaluate whether its response would keep the output in the specified state, and act accordingly. The specification is robust; the procedure is fragile. For work where the principal cannot anticipate every situation — which is all ambitious research — declarative prompts are the only form that scales.

G's rule "*being declarative v imperative helps a lot*" applies this general principle to the specific case of sub-agent dispatch. But the same principle shows up throughout the programme in different registers:

- The **separation of agentic and deterministic work** (backticks strategy): the agent classifies, a deterministic script transforms. Classification is a declarative description of the output state; the transformation is procedural and should be fully automated, not re-delegated to an agent that might drift.

- The **per-paper referee pivot**: the prompt specifies the agent's expertise domain ("be an expert in these topics"), not the reading procedure ("first read section 1, then section 2"). The agent chooses how to read; the prompt guarantees they can read competently.

- The **traceability discipline**: write the prompt to the same directory as the output. A future reader reconstructing what happened sees both sides of the interaction. The prompt-plus-output pair is a declarative description of the transaction: this was asked, that was delivered.

All four instances share the same shape: describe what should be true at the end, arrange the environment so the right inputs are available, let the agent find the path. This is how modern engineering teams write infrastructure-as-code (declare the state; let the tool reconcile). The programme imports the same discipline into research dispatch.

There is a subtler benefit that G noticed early: declarative prompts preserve the principal's context. An imperative prompt has to be written with the assumption that the agent will execute it without the principal present; if the agent encounters ambiguity, it will either fabricate a resolution or stall. A declarative prompt plus a reference path ("read the research theorems from here; read the pattern catalog from there") lets the agent stay inside the principal's context without the principal having to maintain that context actively. *Use local agents so that we keep our context*: the context is preserved not by the principal, but by the reference paths that the declarative prompt points to.

## For future readers

When dispatching a sub-agent, write down what the output should look like and what it should be consistent with, not the procedure that should produce it. If you find yourself writing a procedure, ask whether you could instead describe the output state and reference paths. Usually you can. The prompts that result are shorter, more robust, and easier to debug.

*Next: [18 — Credit before someone else uses it](18-credit-before-someone-else-uses-it.md).*
