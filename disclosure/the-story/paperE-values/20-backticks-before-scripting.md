# 20 — Backticks before scripting

## The claim

When a job has a classification step and a transformation step, use the agent for the classification and a script for the transformation. Agents are probabilistic and consume tokens; scripts are deterministic and run fast. Mixing them — asking the agent to do both — produces a slow pipeline that drifts. The rule originated with the LaTeX backticks strategy and generalized into a programme-wide discipline.

## The evidence

G, explaining the strategy after Claude had missed the point:

> however i don't think you understood my backticks strategy, the first step was to have an agentic run asking please wrap every expression into backticks and you would have all the .md files processed and then you'd kick in - thats 100% deterministic

G, giving a post-hoc endorsement after seeing the results:

> the fencing strategy is the smartes solution ever, i'm having a look at the .md files and their readability was not impacted at all so i can submit the fenced .md to zenodo as they are!
>
> remember that we were on that for hours and hours

G, on the general principle applied to agent dispatch:

> use local agents so that we keep our context and provide them with the paths where our research and theorems and patterns are, being declarative v imperative helps a lot!

## The argument

The LaTeX backticks strategy was invented because the conversion from G's research markdown to compileable LaTeX was failing on expressions that looked like prose but were actually math. An agent asked to convert the markdown directly had to do two jobs simultaneously: decide which substrings were math (classification) and transform those substrings into LaTeX (transformation). The agent did the classification competently but sometimes missed items; it did the transformation competently but was slow and expensive.

G's fix was to split the work. Ask the agent only to wrap every expression that it classifies as math with backticks, producing `math` in prose. Once that is done, a deterministic script takes over: find every backtick-wrapped substring, apply the fixed transformation (backticks → \$…\$), and emit the LaTeX. The agent does the probabilistic work (classifying which substrings are math); the script does the deterministic work (applying a fixed transformation). The division-of-labour rule is: if the work can be specified as a rule, do not pay tokens for it; write the rule.

The rule generalizes. Many research operations have the same shape — a classification that only a reader can perform, followed by a transformation that can be automated. Sorting papers into categories is classification; compiling the sorted results into an index is transformation. Identifying which theorems in a proof chain are "proved" vs. "conjectured" is classification; visualizing the chain with colour-coded vertices is transformation. The rule says: let the agent classify once, then script everything else.

The benefits are several.

- **Cost.** Agent tokens are expensive; deterministic scripts are free to run. Separating the two reduces token cost by orders of magnitude for large artifacts.
- **Reproducibility.** A deterministic script produces the same output on the same input every time. An agent does not. If the transformation is deterministic, capture it in a script so the pipeline is reproducible.
- **Debuggability.** When a deterministic script produces an unexpected output, you can read the script and find the bug. When an agent produces an unexpected output, you have to re-run and hope.
- **Auditability.** The script's code is a record of the transformation rule. Reviewers can inspect it. The agent's behaviour is not as easily auditable.

G's ancillary observation — *their readability was not impacted at all so i can submit the fenced .md to zenodo as they are!* — is the downstream benefit of getting the split right. The classified-and-scripted output is a first-class artifact, submittable, auditable, reproducible. It is not a pipeline intermediate; it is a deliverable.

The instinct also extends into G's attitude toward the ORA itself. The ORA's Authors (the agent roles that attack nodes) do the classification and construction work that requires judgment; the ORA's runner script handles dispatch, logging, and output aggregation, which are deterministic. Every addition to the ORA architecture that G has made — lead files, append-only logs, self-heal loops — is an instance of this same discipline: identify the deterministic part, script it, leave the agent to do what only the agent can do.

## For future readers

Every time you are about to ask an agent to do a repeatable transformation, ask yourself whether a deterministic script could do the transformation given a simpler classification from the agent. The answer is usually yes, and the pipeline that results is cheaper, faster, and more defensible.

*Next: [21 — Fencing strategy](21-fencing-strategy.md).*
