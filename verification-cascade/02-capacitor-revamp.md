# Capacitor Revamp: Token-Efficient Inter-Agent Messaging

*Strategy document for reducing capacitor token overhead at runtime while preserving agent self-selection and kill-list integrity.*

*G Six and Claude Opus 4.6. April 2026.*

---

## 1. The Problem

The current capacitor architecture loads **~6,000-8,000 lines** of compiled domain knowledge into every dispatched agent. A typical CCM verification wave with 30 proof steps dispatches ~60 agents — producing **~480,000 lines of redundant context** per wave. Multiply by 3-10 waves per run, across multiple tiers (A/B/C escalation), and the token burn becomes the dominant cost of the Verification Cascade.

### 1.1 Why it's this way (the I-v6-5 constraint)

Three consecutive ORA failures (I-v6-3, I-v6-4, I-v6-5) proved that **runner-side classification of what an agent needs fails predictably**. The root cause: runners misclassify node types, agents miss critical tools, verification quality collapses. The fix: "pass everything, let the agent self-select."

This is correct for quality. It is brutal for tokens.

### 1.2 The core tension

- **Hiding** context from agents breaks verification (I-v6-5).
- **Loading** all context into every agent wastes 60-80% of tokens on unused material.
- The resolution: **defer, don't hide**. Every section remains addressable and fetchable. Only the active working set is pre-loaded.

---

## 2. Research Foundation

Survey of inter-agent messaging systems (April 2026) identified six architectural patterns from the 2025-2026 literature:

### 2.1 Layered Context (MemGPT/Letta)

OS-inspired tiered memory: Core (always in context) → Recall (searchable on demand) → Archival (long-term, fetched by query). When context pressure hits ~70%, system pages content to lower tiers. The capacitor maps naturally: kill list + proof chain = Core; correspondence tables = Recall; framework chains = Archival.

*Source: Packer et al., "MemGPT: Towards LLMs as Operating Systems" (arXiv:2310.08560); Letta framework docs.*

### 2.2 Delta Messaging (JetBrains "Complexity Trap")

Key finding: simple observation masking matches LLM summarization at ~50% cost reduction. Only transmit what changed since last interaction. The dynamic capacitor already has SELF-ADJUST/TRIM/AMPLIFY — but rebuilds the whole file. Delta-only updates between waves halve reload cost.

*Source: JetBrains Research, "The Complexity Trap" (NeurIPS 2025 DL4Code workshop).*

### 2.3 Communication Graph Pruning (AgentPrune)

Prunes redundant messages in multi-agent pipelines. 28-73% token reduction, 7.8x cheaper. Applied to the ORA: not every Verifier needs the full cross-domain correspondence table — a spectral Verifier doesn't need the geometric column until it gets stuck.

*Source: "Cut the Crap: AgentPrune" (ICLR 2025, OpenReview:LkzuPorQ5L).*

### 2.4 Blackboard with Scoped Memory (CrewAI + Blackboard Architecture papers)

Hierarchical memory scopes: `/cascade/tier-a/step-7/`. Agents query only their scope. 13-57% improvement over flat shared-context. The ORA blackboard (sections A-O) already exists but loads wholesale.

*Sources: "Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture" (arXiv:2507.01701); "LLM-Based Multi-Agent Blackboard System" (arXiv:2510.01285); CrewAI scoped memory (2025 redesign).*

### 2.5 Structured Contracts (Claude Agent SDK / Supervisor pattern)

Parent sends scoped task + minimal context. Agent returns structured verdict. Parent never shares full context. The ORA already does this with Author/Critic roles — formalizing with typed schemas creates explicit context boundaries.

*Source: Anthropic Claude Agent SDK; Databricks supervisor pattern.*

### 2.6 KV-Cache Fusion / C2C (Sub-Text Communication)

Agents exchange KV-cache representations instead of text. 2.5x latency speedup, 8-10% accuracy gain. Not implementable in current stack, but the principle is load-bearing: text is an information bottleneck.

*Source: "Cache-to-Cache: Enabling Multi-LLM Communication" (ICLR 2026, arXiv:2510.03215); Q-KVComm (arXiv:2512.17914).*

### 2.7 Additional relevant work

- **ACON** (Agent Context Optimization): 26-54% peak token reduction via unified compression of observations + interaction history. Gradient-free, works with closed-source models. (arXiv:2510.00615)
- **MasRouter** (ACL 2025): Learned routing reduces overhead by 52%. Cascaded controller: mode → role → LLM. (arXiv:2502.11133)
- **MAGMA** (Multi-Graph Agentic Memory): Semantic/temporal/causal/entity graph with adaptive traversal. 40% faster retrieval than A-MEM. (arXiv:2601.03236)
- **Microsoft ACE** (ICLR 2026): Evolving context playbooks via Generator/Reflector/Curator. 82% latency reduction. Already cited in dynamic capacitor design. (arXiv:2510.04618)
- **Guided Topology Diffusion**: Graph diffusion models generate task-adaptive sparse communication topologies. (arXiv:2510.07799)

---

## 3. Strategy: Three Composable Optimizations

### Strategy A: Capacitor-as-Index + On-Demand Fetch

**Principle:** The capacitor becomes a ~1,500-line index. Full sections are fetched on demand. Nothing hidden, everything deferred.

**Current flow:**
```
Agent spawns → loads full 8,000-line capacitor → self-selects what to use → works
```

**Proposed flow:**
```
Agent spawns → loads 1,500-line index capacitor → works with core context
  → needs H.5 (operations table)? → requests it → runner injects inline
  → needs I.1 (RH chain)? → requests it → runner injects inline
  → never needs H.4 (grammar)? → never loaded, tokens saved
```

**The index capacitor contains:**

| Section | Content | Lines |
|---------|---------|-------|
| META | Capacitor state, charge level, version | ~30 |
| PROOF-CHAIN | H.1 — full numbered steps with dependencies and status | ~200-500 |
| KILL-LIST | Full kill list (NEVER reduced — I-v6-5 safety) | ~100-500 |
| BOTTLENECK | Current bottleneck description + engaged nodes | ~50 |
| VOICE | Voice canon (runner identity) | ~50 |
| DOMAIN-MAP | Which domains are active, which Tier 2 families activated | ~30 |
| INDEX | Section-by-section pointer table with 1-line descriptions | ~100 |

**Fetchable sections (on-demand):**

| Section | Trigger for fetch |
|---------|-------------------|
| A. Six Patterns method | Agent applies pattern analysis |
| B. Theorem catalogues | Agent cites framework theorem |
| C. Predictive grammar | Agent checks formula shape |
| D. Transposition mechanics | Agent transposes between additive/multiplicative |
| E. Anchor + dictionaries | Agent needs operator definitions |
| F. Prediction table | Agent checks against experiment |
| G. Other reference files | Agent needs bridge theorems, Laurent sweeps |
| H.2 Correspondence tables | Agent transposes between domains |
| H.3 Six Patterns analysis | Agent works on specific load-bearing step |
| H.4 Grammar analysis | Agent verifies formula |
| H.5 Operations equivalence | Agent translates operation across domains |
| H.6-H.8 Interface/kills/escalation | Agent plans escalation route |
| H.9-H.12 Toolkit/amplification/corrections | Agent needs background tools or history |
| I. Framework proof chains | Agent checks cross-chain dependencies |

**I-v6-5 safety check:**
- Kill list: ALWAYS in core. Never deferred. ✓
- Proof chain structure: ALWAYS in core. ✓
- Every section visible in INDEX with description. Agent knows what exists. ✓
- Agent can fetch ANY section at ANY time. Nothing hidden. ✓
- Runner does not classify what agent needs. Agent self-selects. ✓

**Estimated savings: 40-50% token reduction per agent.**

---

### Strategy B: Effort-Tiered Dispatch

**Principle:** Different agent roles get different starting context layers. All can escalate to full context.

```
Layer 1 — MINIMAL (~1,500 lines)
  Core index capacitor (Strategy A).
  For: Non-bottleneck Verifiers doing structural checks.

Layer 2 — STANDARD (~3,000 lines)
  Core + active domain correspondence tables (H.2 filtered to active domains)
  + Six Patterns analysis for the assigned step (H.3 subset)
  + relevant toolkit rows (H.10 filtered by engages-bottleneck)
  For: Standard Authors and Critics.

Layer 3 — FULL (~6,000-8,000 lines)
  Everything pre-loaded. No fetch latency.
  For: Bottleneck node Authors, Synthesis agents, Tier C Construction agents.
```

**Dispatch rules:**

| Role | Tier | Starting Layer | Can escalate to |
|------|------|----------------|-----------------|
| Verifier (non-bottleneck) | A | Layer 1 | Layer 2 on demand |
| Verifier (bottleneck) | A | Layer 2 | Layer 3 on demand |
| Re-deriver | A | Layer 2 | Layer 3 on demand |
| Author (standard) | B | Layer 2 | Layer 3 on demand |
| Author (bottleneck) | B/C | Layer 3 | — (already full) |
| Critic | A/B | Layer 2 | Layer 3 on demand |
| Synthesis agent | all | Layer 3 | — (already full) |
| Construction agent | C | Layer 3 + Tier 3/4 domains | Expanded capacitor |

**I-v6-5 safety check:**
- No agent is denied access to any section. ✓
- Kill list in every layer. ✓
- Escalation is agent-initiated, not runner-classified. ✓
- Bottleneck nodes always get full context (no risk of missing tools). ✓

**Estimated savings: 30-40% token reduction across a full wave.**

---

### Strategy C: Delta-Only Wave Updates

**Principle:** Between waves, don't reload the full capacitor. Send only what changed.

**Current flow:**
```
Wave 1 completes → capacitor v1.1 rebuilt (SELF-ADJUST/TRIM/AMPLIFY)
  → Wave 2 agents load full capacitor v1.1 (~8,000 lines)
```

**Proposed flow:**
```
Wave 1 completes → delta computed:
  DELTA v1.0 → v1.1:
    + K-12: [new kill entry]
    ~ Step 7: PENDING → SURVIVED
    ~ Step 14: PENDING → WEAKENED (downgraded, reason: ...)
    + H.2: New correspondence cell filled (geometric image of concept X)
    + H.11: Amplification entry (method M transferred from step 3 to step 9)

  → Wave 2 agents load: core index + delta overlay
  → Full sections fetched on demand (Strategy A) are v1.1 versions
```

**Delta format:**
```markdown
## DELTA — v1.0 → v1.1
### New kills
| Kill # | What | Why | Pattern | Re-entry |
|--------|------|-----|---------|----------|

### Status changes
| Step | Old status | New status | Evidence |
|------|-----------|------------|----------|

### New correspondence cells
| Concept | Domain | New image | Source |

### Amplification entries
| Method | From step | To step | Result |

### Corrections
| Card | Old claim | Corrected claim | Reason |
```

**I-v6-5 safety check:**
- Kill list deltas are ADDITIVE (new kills added, never removed). ✓
- Status changes are explicit (agent sees what moved and why). ✓
- Full capacitor still fetchable on demand. ✓

**Estimated savings: 20-30% on multi-wave runs (compounding with A and B).**

---

## 4. Composed Architecture

All three strategies compose:

```
DISPATCH:
  1. Determine agent role and node bottleneck status → select Layer (Strategy B)
  2. Build context package:
     - Layer 1/2/3 core content (pre-loaded)
     - Section INDEX with fetch pointers (Strategy A)
     - If wave > 1: delta overlay instead of full reload (Strategy C)
  3. Agent works with core context
  4. Agent requests additional sections as needed → runner injects inline
  5. Agent returns structured verdict

WAVE-CLOSE:
  6. Compute delta (new kills, status changes, new cells, amplifications)
  7. Update capacitor version
  8. Next wave agents get: core + delta overlay + fetch pointers

TIER ESCALATION:
  9. Tier B agents get Layer 2 minimum + excision brief
  10. Tier C agents get Layer 3 + expanded Tier 3/4 domains
  11. Escalation EXPANDS context, never contracts it
```

**Combined estimated savings: 60-70% token reduction** without violating I-v6-5.

---

## 5. Safety Invariants (NEVER violate)

1. **Kill list completeness** — every kill in every agent's core context. Never deferred, never filtered, never compressed.
2. **Proof chain visibility** — full dependency map always in core. Status of every step visible.
3. **Agent self-selection** — runner never decides what an agent needs. Agent requests, runner provides.
4. **Bottleneck engagement** — nodes marked `engages-bottleneck: yes` always get Layer 2 minimum.
5. **Escalation expands** — moving from Tier A → B → C always adds context, never removes it.
6. **Voice canon integrity** — runner identity and signature consistency checks always in core.

---

## 6. Regression Metrics

Track after deployment to detect quality degradation:

| Metric | Baseline | Alert threshold |
|--------|----------|-----------------|
| Re-exploration rate (killed approaches re-proposed) | 0% (current) | > 2% |
| Cross-step inconsistency (synthesis catches) | baseline TBD | > 10% increase |
| Excision success rate (Tier B) | baseline TBD | > 15% decrease |
| Construction diversity (Tier C domain spread) | baseline TBD | > 20% decrease |
| Fetch request rate (sections demanded on-demand) | N/A | Monitor for patterns |
| Mean agent context size (tokens) | ~80K | Target: < 40K |

---

## 7. Token Pointer and Embedding Strategies

Research survey (April 2026) identified seven sub-text communication techniques where agents bypass tokenization and communicate at the representation level. Three are directly applicable to the Verification Cascade.

### 7.1 LatentMAS — Latent Thought Communication (NeurIPS 2025)

**Mechanism:** Agents generate "latent thoughts" by feeding the final transformer layer's hidden state back as the next input embedding, bypassing tokenization entirely. These thoughts are transferred between agents via layer-wise KV-cache concatenation. Only the final agent in the chain decodes to text.

**How it works step-by-step:**
1. Agent A embeds input, runs forward pass
2. At final layer, extracts hidden state h_t
3. Applies alignment matrix W_a (ridge regression, no training): `W_a = (W_out^T W_out + λI)^{-1} W_out^T W_in`
4. Feeds aligned embedding back as next input; repeats for m steps (40-80 typical)
5. Extracts KV-caches from ALL L transformer layers
6. Agent B receives these caches prepended to its own KV caches
7. Only the final agent decodes to text via softmax

**Compression:** 70.8-83.7% fewer output tokens. 4x-4.3x faster. Latent thoughts ~471x more information-dense than text tokens (O(d_h / log|V|) ratio).

**Training required:** NONE. Completely training-free. Only ridge regression for W_a (negligible).

**Open source:** https://github.com/Gen-Verse/LatentMAS — Works with any HuggingFace model + optional vLLM backend.

*Source: "Latent Collaboration in Multi-Agent Systems" (arXiv:2511.20639).*

### 7.2 KVCOMM — Shared-Prefix KV-Cache Reuse (NeurIPS 2025)

**Mechanism:** When multiple agents share overlapping text context (the capacitor), KVCOMM avoids re-computing KV-caches by estimating offsets from a pool of stored "anchors."

**How anchors work:**
1. Each anchor stores: base KV-cache + offsets between base and actual caches + neighbor segment offsets
2. New request arrives → nearest anchor retrieved via token embedding similarity
3. Stored deviations interpolated to predict cache offsets without recomputation
4. Key caches require RoPE de-rotation/re-rotation for positional alignment

**Compression:** 70%+ cache reuse. 6.7x average prefill speedup, 7.8x max (5-agent setting). TTFT: ~430ms → ~55ms.

**Accuracy:** <2.5% drop at 95% reuse rate on GSM8K. Competitive on MMLU, HumanEval.

**Training required:** NONE. Training-free, prompt-adaptive.

**Open source:** https://github.com/HankYe/KVCOMM

*Source: arXiv:2510.12872.*

### 7.3 C2C — Cache-to-Cache Neural Fusion (ICLR 2026)

**Mechanism:** Projects Agent A's KV-cache directly into Agent B's representation space via a learned "Cache Fuser." Enables cross-model communication (different architectures, different sizes).

**How the Fuser works:**
1. Concatenates Sharer and Receiver KV-cache vectors
2. Applies projection layer → feature fusion layer
3. Dynamic head-weighting modulates attention heads per input
4. Learnable per-layer gate (Gumbel sigmoid → binary at inference) decides which layers accept Sharer context

**Compression:** Eliminates full decode-then-re-encode cycle. ~2x latency reduction. 8.5-10.5% accuracy gain over single models, 3-5% over text exchange.

**Training required:** Fuser only (lightweight). Both LLMs stay frozen. Pre-trained fusers available on HuggingFace (`nics-efc/C2C_Fuser`).

**Open source:** https://github.com/thu-nics/C2C

*Source: arXiv:2510.03215.*

### 7.4 Additional techniques surveyed

| Technique | Method | Compression | Training | Source |
|-----------|--------|-------------|----------|--------|
| **Interlat** | Hidden states → compressed latent steps via learned projection | 24x (8-step) | Full (64xA100) | arXiv:2511.09149 |
| **Thought Communication** | Sparsity-regularized autoencoder extracts identifiable "latent thoughts" | Quality-focused (+67% relative) | Autoencoder only | arXiv:2510.20733 |
| **Token Assorted** | VQ-VAE replaces early CoT tokens with latent discrete tokens | 17% fewer tokens | VQ-VAE | arXiv:2502.03275 |
| **Latent Briefing** (Ramp) | Attention-based identification + discard of unimportant shared context | 49% median savings | None | Ramp Labs 2026 |

### 7.5 The API constraint

**Critical limitation:** All latent-space techniques require access to internal model states (hidden layers, KV-caches). This means:

| Stack | Latent techniques available | Text-level techniques available |
|-------|----------------------------|--------------------------------|
| Self-hosted open-weight (Qwen3, Llama, Gemma) | ALL (LatentMAS, KVCOMM, C2C, Interlat, etc.) | ALL |
| Claude API | NONE (no KV-cache access) | Prompt Caching (90% cost reduction), Strategies A/B/C |
| Hybrid (Claude supervisor + open-weight workers) | Workers use latent, supervisor uses text | Full stack |

### 7.6 Anthropic Prompt Caching (available TODAY)

The immediately deployable optimization. All 30-60 agents share the same system prompt + capacitor prefix, cached server-side.

**Mechanics:**
- First agent request populates the cache (~5 min TTL)
- Subsequent agents hit the cache: 0.1x base input price (90% cost savings), 5-10x TTFT reduction
- Only per-agent unique content (step assignment, prior work on node) is fresh input

**Application to the capacitor:**
```
CACHED PREFIX (shared by all agents):
  - Voice canon
  - Kill list (full)
  - Proof chain (full H.1)
  - Six Patterns method (A)
  - Predictive grammar (C)
  - Operations equivalence table (H.5)
  - Correspondence tables for active domains (H.2)
  → ~4,000-5,000 tokens cached, paid once

PER-AGENT SUFFIX (unique):
  - Step assignment
  - Prior work on this specific node
  - Layer-specific fetch results
  → ~500-1,500 tokens per agent, paid each time
```

**Limitation:** Cache entries only available after first response begins. Stagger agent launches by ~1s to allow cache population. For 60 agents: ~60s stagger vs. fully simultaneous dispatch.

### 7.7 Claude API-Native Architecture

**Constraint (April 2026):** Self-hosted inference clusters are impractical for this workload. An M4 64GB Mac running Qwen3-14B cannot sustain 30-60 parallel agents at usable latency/TPS. All latent-space techniques (LatentMAS, KVCOMM, C2C, Interlat) require KV-cache access unavailable through the Claude API. These are documented above for future reference but are **NOT part of the current implementation plan**.

The architecture is Claude API-only. All optimizations are at the **orchestration level** — how context is structured, what agents receive, how they communicate.

```
┌─────────────────────────────────────────────────┐
│  CLAUDE OPUS (Supervisor / Synthesis)            │
│  - Orchestration, final judgment, escalation     │
│  - Prompt caching: shared capacitor as prefix    │
│  - Message bus: reads feeds, dispatches queries   │
└──────────────┬──────────────────────────────────┘
               │ Structured contracts (AEE envelope)
               ▼
┌─────────────────────────────────────────────────┐
│  DISPATCH LAYER (orchestration logic)            │
│  - Strategy A: index capacitor + on-demand fetch │
│  - Strategy B: effort-tiered (Layer 1/2/3)       │
│  - Strategy C: delta-only wave updates           │
│  - Prompt caching: shared prefix across agents   │
│  - Message bus: feeds + query routing             │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────┐
│  CLAUDE API WORKERS (all agents)                 │
│                                                  │
│  CACHED PREFIX (shared, paid once):              │
│  ├── Voice canon                                 │
│  ├── Kill list (full, NEVER reduced)             │
│  ├── Proof chain H.1 (full structure)            │
│  ├── Domain map (active domains)                 │
│  └── Section INDEX (pointers to fetchable parts) │
│  → ~4,000-5,000 tokens, 90% cost reduction       │
│                                                  │
│  PER-AGENT SUFFIX (unique, paid each time):      │
│  ├── Step assignment + prior work on node         │
│  ├── Feed subscriptions (relevant kills, cards)  │
│  ├── Layer-specific pre-loaded sections           │
│  └── Fetched sections (on-demand during work)    │
│  → ~500-3,000 tokens depending on Layer 1/2/3    │
│                                                  │
│  LIVE MESSAGING (during agent execution):        │
│  ├── POST to feeds (kills, cards, statuses)      │
│  ├── SUBSCRIBE to feeds (domain-filtered)        │
│  └── QUERY/RESPONSE (agent-to-agent via router)  │
└─────────────────────────────────────────────────┘
```

**Combined savings estimate (Claude API-only):**

| Component | Token Savings | Cost Savings | Applies to |
|-----------|--------------|-------------|------------|
| Strategy A (index + fetch) | 40-50% | 40-50% | All agents |
| Strategy B (effort tiers) | 30-40% | 30-40% | All agents |
| Strategy C (delta waves) | 20-30% | 20-30% | Multi-wave runs |
| Prompt caching (shared prefix) | — | 90% on prefix | All agents |
| Message bus (feeds) | 15-25% | 15-25% | Live coordination |
| Message bus (queries) | 5-10% | 30-50% fewer agents | Reconciliation |
| AgentPrune topology | 28-73% edges | proportional | Communication graph |

**Net result for a 60-agent CCM verification wave:**
- Current: ~480,000 lines redundant context, full token cost per line
- With A+B+C: ~150,000 lines (-70%)
- With A+B+C + prompt caching: ~150,000 lines, shared prefix at 10% cost
- With A+B+C + prompt caching + message bus: ~120,000 lines, 30-50% fewer secondary agents
- **Effective cost reduction: ~80% vs current architecture**

### 7.8 Compression ratios at a glance

| Technique | Token Reduction | Latency | Accuracy Δ | Training | API-Compatible |
|-----------|----------------|---------|------------|----------|----------------|
| LatentMAS | 70-84% | 4x faster | +14.6% | None | No (needs weights) |
| KVCOMM | 70%+ reuse | 7.8x prefill | <2.5% drop | None | No (needs KV-cache) |
| C2C | decode/re-encode eliminated | 2x faster | +8-10% | Fuser only | No (needs KV-cache) |
| Interlat | 24x compression | 24x faster | +3-5% | Heavy | No |
| Latent Briefing | 49% median | 20x vs attention | ~0% drop | None | Partial (Ramp) |
| Prompt Caching | 90% cost | 5-10x TTFT | 0% drop | None | YES (Anthropic) |
| AgentPrune | 28-73% | proportional | ~0% drop | None | YES (orchestration) |

### 7.9 Open-source implementations

| Technique | Repository | Status |
|-----------|-----------|--------|
| C2C | https://github.com/thu-nics/C2C | Pre-trained fusers on HuggingFace |
| LatentMAS | https://github.com/Gen-Verse/LatentMAS | HuggingFace + vLLM backend |
| KVCOMM | https://github.com/HankYe/KVCOMM | NeurIPS 2025 |
| AgentPrune | https://github.com/yanweiyue/AgentPrune | ICLR 2025 |
| OPTIMA | https://github.com/thunlp/Optima | ACL 2025 |

---

## 8. Implementation Phases

### Phase 1: Index Capacitor (Low risk)
- Refactor capacitor format into core index + fetchable sections
- Implement fetch-on-demand protocol in ORA runner
- Validate on Tier 4 pilot (Boegli+Teschl — smallest target)

### Phase 2: Effort-Tiered Dispatch (Low risk)
- Add Layer field to dispatch protocol
- Map roles to starting layers
- Validate on Tier 1 (CCM — main event, highest agent count)

### Phase 3: Delta Wave Updates (Medium risk)
- Implement delta computation at wave-close
- Add delta overlay to agent context assembly
- Validate on multi-wave runs (>3 waves)

### Phase 4: Token Pointer Integration (TBD)
- Pending research findings
- Integrate novel compression/pointer mechanisms
- Validate against regression metrics

### Phase 5: Bidirectional Messaging Layer (Medium risk)
- Deploy live feeds (kill stream, card stream, escalation stream)
- Add QUERY/RESPONSE protocol for agent-to-agent dialogue
- Implement structured escalation messages for Tier A → B → C
- Validate on multi-tier runs

### Phase 6: Communication Topology Optimization (Higher risk)
- AgentPrune-style graph pruning for redundant edges
- DALA auction-based bandwidth allocation
- Gossip protocol for soft-state propagation
- Validate against regression metrics across all tiers

---

## 9. Bidirectional Inter-Agent Messaging

Research survey (April 2026) on bidirectional messaging and message relay patterns for multi-agent LLM systems.

### 9.1 Protocol foundations

**A2A `INPUT_REQUIRED` state** (Google, v0.2+): The cleanest protocol-level implementation of mid-task bidirectional dialogue. When a remote agent needs clarification:
1. Agent enters `INPUT_REQUIRED` state
2. Server sends `TaskStatusUpdateEvent` with the question
3. Client agent responds via `SendStreamingMessage`
4. Agent resumes execution

This enables: Verifier asks Critic a question directly. Author asks Re-deriver to confirm a shared assumption. Synthesis queries two conflicting Authors without spawning a Judge.

*Source: A2A Protocol Specification, a2a-protocol.org/latest/specification/.*

**Agent Envelope Exchange (AEE)** (IETF draft): Minimal 14-field JSON envelope for inter-agent messages. Key fields: `from`, `to`, `corr` (correlation ID for workflow chains), `reply_to` (references originating message), `priority`, `payload`. The `corr` + `reply_to` chain makes full causality traceable across relay chains.

*Source: IETF draft-cowles-aee-00.*

**CrewAI delegation** (`allow_delegation=True`): Agents get two tools — delegate tasks to specialists, and **ask specific questions** to gather information from colleagues. `allowed_agents` parameter controls addressable peers.

*Source: CrewAI collaboration docs.*

### 9.2 Message relay and routing patterns

**DALA — Auction-Based Communication** (arXiv:2511.13193): Treats communication bandwidth as a scarce tradable resource. Agents bid for the right to speak based on value density (message value / message length). Four output tiers: Full, Summary, Keywords, Silence. Results: **2-4x token reduction** while maintaining SOTA accuracy (84.32% MMLU, 96.18% GSM8K). Strategic silence emerges naturally — agents learn when NOT to communicate, with silence increasing from 3% to 40% under scarce budgets.

**Gossip protocols for LLM agents** (arXiv:2508.01531): Each agent periodically exchanges state with a random neighbor. With fan-out 3, a 25,000-agent system converges in ~15 rounds (~20 seconds). Proposed as complementary substrate for spreading soft state (kills, status changes, situational awareness) while structured protocols handle deterministic actions.

*Additional source: "Gossip-Enhanced Communication Substrate" (arXiv:2512.03285) — proposes gossip with CRDTs for eventual consistency.*

**Hub-spoke information withholding problem** (Augment Code, 2025): Critical failure mode in supervisor patterns — "critical context discovered by one agent never reaches another because the hub fails to relay it, especially when spokes produce structured outputs and the hub filters fields before forwarding." This is the core argument for mesh/bidirectional alternatives.

### 9.3 Context compression at relay points

| Framework | Compression Method | Pattern |
|---|---|---|
| Claude Code | Summarization at ~95% capacity | Context isolation — sub-agents return summaries |
| AutoGen | CompressibleGroupManager + LLMLingua | Centralized — single authority compresses shared stream |
| LangGraph | trim_messages + tool results >20K → file paths | Per-agent independent compaction |
| Google ADK | Event-based sliding window, 60-80% reduction | "Narrative casting" relabels messages during transfer |

**Hierarchical scaling math** (topology research): Star topologies saturate at ~N = W/m agents (window width / message length). Trees enable N = b^L agents but **require compaction at each aggregation node as a mathematical necessity**. Implication: at 30-60 agents, compaction at relay points isn't optional — it's a scaling requirement.

---

## 10. Communication Opportunities in the Current Architecture

Analysis of the verification cascade draft files identified **13 specific communication opportunities** where bidirectional messaging or message relay replaces expensive workarounds. Organized by category.

### 10.1 Category 1: Step-to-Step Verification Handoffs

**Opportunity 1.1 — Cross-Step Assumption Verification**

*Current:* All 30 Verifiers receive full capacitor. Synthesis cross-checks assumptions post-hoc. If Step 5's Verifier flags assumption A as "verified locally" but Step 23's Verifier discovers A is problematic, the gap isn't caught until Synthesis — wasting a full wave.

*Proposed:* When Step 5's Verifier completes, it POSTs verified assumptions to a step-dependency registry. Step 23's Verifier QUERIEs the registry before drafting its own verification.

*Savings:* Eliminates 1 full re-checking wave. Saves ~6-12 agents on a 30-step proof.

**Opportunity 1.2 — Re-deriver ↔ Verifier Bidirectional Loop**

*Current:* Verifier and Re-deriver spawned in parallel, return independently. If they disagree (SURVIVED vs FAILED), a Judge is spawned to reconcile — re-reading both outputs from scratch.

*Proposed:* Re-deriver posts structured failure trace. Verifier asks: "Does the author's method address your blocker?" Re-deriver responds. Three-turn exchange produces LOCK without Judge overhead.

*Savings:* Eliminates Judge spawn for ~40% of SURVIVED/FAILED divergences.

### 10.2 Category 2: Tier-to-Tier Escalation Messaging

**Opportunity 2.1 — Tier A → Tier B Structured Escalation**

*Current:* When Tier A finds WEAKENED on step N, Tier B receives the entire capacitor — 80% of which is about OTHER steps.

*Proposed:* Tier A posts a structured escalation message:
```
ESCALATION: Step 4.2 → Tier B
STATUS: WEAKENED
GAP: [specific gap description]
KILL_LIST_RELEVANT: [K-1, K-5, K-7]
CORRESPONDENCE_ROWS: [Spectral, Algebraic only]
SIX_PATTERNS_PRIORITY: [P4, P1 most promising]
ESCALATION_ROUTES: [3 pre-identified from H.8]
```
Tier B Author receives ~30% of the context, can QUERY for more if needed.

*Savings:* 50-70% context reduction per escalation.

**Opportunity 2.2 — Tier B → Tier C Live Kill Amplification** *(CRITICAL)*

*Current:* Tier B's kill list is appended at cycle-close. If Tier C is spawned during Tier B's wave, it doesn't see the kills.

*Proposed:* Kills stream to a live registry as they're written. Tier C Authors QUERY by pattern: "Show me kills from spectral domain that blocked self-adjointness proofs."

*Savings:* Tier C avoids ~30-40% of Tier B's dead ends. Saves 1-3 construction attempts.

### 10.3 Category 3: Agent Internal-State Queries

**Opportunity 3.1 — Verifier → Author Toolkit Query**

*Current:* Synthesis must re-read Authors' narrative outputs to extract toolkit citations for MAR confirmation bias checks. Unreliable extraction.

*Proposed:* Authors respond to structured queries: "Which toolkit rows from H.10 did you cite? List by NAME, precision, status." Synthesis gets metadata, not narrative. MAR check becomes deterministic.

*Savings:* Eliminates 15-25% of Judge spawns for MAR checks.

**Opportunity 3.2 — Critic → Author Debug Trace**

*Current:* Author returns BLOCKED with terse narrative. Critic must guess: is the blockage topological (GENUINE) or computational (CLOSABLE)?

*Proposed:* Author provides structured BLOCKED_TRACE with step_reached, attempts, failure_reason, diagnostic_confidence, re_entry_requires. Critic can QUERY for clarification.

*Savings:* Kill classification accuracy improves 20-30%. Fewer Tier C false starts.

### 10.4 Category 4: Dynamic Capacitor Updates (Live Relay)

**Opportunity 4.1 — Wave-to-Wave Card Streaming** *(CRITICAL)*

*Current:* Five-field cards are batched at cycle-close. If wave 2 spawns before wave 1 completes, wave 2 agents get stale data.

*Proposed:* Cards stream to a live feed as they're generated. Wave 2 agents SUBSCRIBE by domain/type/status.

*Savings:* Eliminates cascading wave mismatches. Saves 1-2 full wave re-does on 3+ wave runs.

**Opportunity 4.2 — Kill List Append-Only Feed**

*Current:* Kills batched at cycle-close. Parallel agents in the same wave can't see each other's kills.

*Proposed:* Kill list is an append-only log stream. Authors SUBSCRIBE to kills matching their domain.

*Savings:* Kill deduplication + 1-2 variant re-attempts avoided per wave.

**Opportunity 4.3 — Cross-Tier Amplification Relay** *(CRITICAL)*

*Current:* Tier 4 methodology validated post-run. Tier 1 reads merged capacitor days later.

*Proposed:* Amplification entries stream LIVE between tiers. Tier 1 agents spawned WITH Tier 4 methods.

*Savings:* 10-15% methodology reuse gain across sequential tiers.

### 10.5 Category 5: Synthesis & Meta-Cognition Queries

**Opportunity 5.1 — Synthesis → Author Reconciliation Query**

*Current:* Two Authors disagree → Judge spawned → re-reads both outputs from scratch.

*Proposed:* Synthesis queries both Authors: "Respond to each other's finding in one sentence." Two 1-sentence replies replace Judge reading two full work products.

*Savings:* Eliminates 40-60% of Judge spawns for reconciliation.

**Opportunity 5.2 — Critic → Critic Confidence Query**

*Current:* Critic downgrades with medium confidence → Meta-critic spawned to re-verify from scratch.

*Proposed:* Synthesis queries Critic: "What additional evidence would raise your confidence to 0.90+? What's the most likely scenario where you're wrong?" Targeted response enables focused follow-up instead of full re-verification.

*Savings:* 30-50% of Meta-critic spawns become targeted queries.

### 10.6 Summary: Communication Opportunities by Priority

| Priority | Opportunity | Category | Current Cost | Proposed Savings |
|----------|------------|----------|--------------|-----------------|
| **CRITICAL** | 4.1 Card streaming | Live relay | Wave mismatches, full re-does | 1-2 waves saved |
| **CRITICAL** | 2.2 Tier B→C kill amplification | Escalation | 2-10 wasted construction cycles | 1-3 attempts avoided |
| **CRITICAL** | 4.3 Cross-tier amplification | Live relay | Post-hoc only benefit | Live methodology reuse |
| **HIGH** | 2.1 Tier A→B escalation stream | Escalation | Full capacitor reload | 50-70% context reduction |
| **HIGH** | 1.1 Cross-step assumption query | Verification | 1 full re-checking wave | 6-12 agents saved |
| **HIGH** | 4.2 Kill list live feed | Live relay | Duplicate kills, re-attempts | 1-2 variants avoided/wave |
| **MEDIUM** | 5.1 Author reconciliation query | Synthesis | Judge spawn | 40-60% fewer Judges |
| **MEDIUM** | 1.2 Verifier ↔ Re-deriver loop | Verification | Judge spawn | 40% fewer Judges |
| **MEDIUM** | 3.1 Toolkit query | Internal-state | Judge spawn for MAR | 15-25% fewer MAR Judges |
| **MEDIUM** | 3.2 Debug trace query | Internal-state | Uncertain kills | +20-30% kill accuracy |
| **MEDIUM** | 5.2 Confidence query | Synthesis | Meta-critic spawn | 30-50% fewer Meta-critics |

---

## 11. The Three-Layer Architecture (Revised)

The capacitor revamp introduces three communication layers, each serving a different temporal need:

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 3: CAPACITOR (Long-Term Memory)                      │
│  - Static compiled knowledge (patterns, grammar, dicts)     │
│  - Versioned, updated at run boundaries                     │
│  - Strategy A: index + on-demand fetch                      │
│  - Strategy B: effort-tiered dispatch                       │
│  - Strategy C: delta-only wave updates                      │
│  - Serves: "What does the programme know?"                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 2: BLACKBOARD (Session Memory)                       │
│  - Sections A-O: live state for this run                    │
│  - Updated at cycle-close (batch)                           │
│  - Serves: "What has this run discovered?"                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: MESSAGE BUS (Live Communication)       *** NEW ** │
│                                                             │
│  FEEDS (append-only, subscribable):                         │
│  ├── kill-stream    — kills as they're written              │
│  ├── card-stream    — five-field cards as they're verified  │
│  ├── status-stream  — proof step status changes             │
│  ├── escalation-stream — Tier A→B→C handoff messages        │
│  └── amplification-stream — cross-tier method transfer      │
│                                                             │
│  QUERIES (request/response, agent-to-agent):                │
│  ├── assumption-query  — "Did upstream step verify X?"      │
│  ├── toolkit-query     — "Which H.10 rows did you cite?"   │
│  ├── debug-trace       — "Show me your BLOCKED_TRACE"       │
│  ├── reconciliation    — "Respond to A's finding"           │
│  └── confidence-query  — "What would raise your conf?"      │
│                                                             │
│  Serves: "What is happening RIGHT NOW?"                     │
│                                                             │
│  Protocol: AEE envelope (14-field JSON)                     │
│  ├── from/to: agent addressing                              │
│  ├── corr: workflow correlation                             │
│  ├── reply_to: causality chain                              │
│  ├── priority: low/normal/high/urgent                       │
│  └── payload: structured content                            │
│                                                             │
│  At cycle-close: feeds merge into blackboard (audit trail)  │
│  At run-close: blackboard merges into capacitor (long-term) │
└─────────────────────────────────────────────────────────────┘
```

### Message flow example (CCM verification, Step 4.2 WEAKENED)

```
1. Wave 1: 30 Verifiers dispatched (Layer 1 context + subscriptions)

2. Verifier-4.2 completes:
   → POSTS to status-stream: {step: 4.2, status: WEAKENED, gap: "CF boundedness"}
   → POSTS to kill-stream: {K-new: "CF extension requires bounded perturbation"}
   → POSTS to card-stream: {CCM-4.2: five-field card with WEAKENED status}

3. Verifier-7.1 (still running, depends on 4.2):
   → RECEIVES status-stream update: "4.2 is WEAKENED"
   → Adjusts own verification: "My step assumes 4.2. Flagging conditional."

4. Synthesis (at wave-close):
   → Reads all feed entries (not individual agent outputs)
   → Identifies: "4.2 WEAKENED, 7.1 conditional on 4.2, escalation needed"

5. Escalation:
   → POSTS to escalation-stream: structured message for Tier B
   → Tier B Author spawns with: escalation message + kill-stream entries
     for domain "self-adjointness" + index capacitor
   → Does NOT load full capacitor — fetches sections on demand

6. Tier B Author (mid-excision):
   → QUERIES Verifier-4.2: "Is the boundedness failure absolute or N-dependent?"
   → Verifier-4.2 REPLIES: "N-dependent. For N < 100, bounded. For N → ∞, unbounded."
   → Tier B adjusts: attempts excision for large-N regime only

7. Tier B fails → Tier C triggered:
   → Tier C Author SUBSCRIBES to kill-stream (domain: self-adjointness)
   → Receives: Tier A kills + Tier B kills, live
   → Avoids all dead ends immediately
```

---

## 12. Revised Combined Savings Estimate (Claude API-Only)

| Component | Token Savings | Agent Savings | Cost Savings | Applies to |
|-----------|--------------|---------------|-------------|------------|
| Strategy A (index + fetch) | 40-50% | — | 40-50% | All agents |
| Strategy B (effort tiers) | 30-40% | — | 30-40% | All agents |
| Strategy C (delta waves) | 20-30% | — | 20-30% | Multi-wave runs |
| Prompt caching | — | — | 90% on shared prefix | All agents |
| Message bus (feeds) | 15-25% | 1-2 waves saved | 15-25% | Live coordination |
| Message bus (queries) | 5-10% | 40-60% fewer Judges | 30-50% fewer agents | Reconciliation |
| AgentPrune topology | 28-73% edges pruned | — | proportional | Communication graph |
| **Combined** | **70-80% token reduction** | **30-50% fewer secondary agents** | **~80% effective cost reduction** | **Full cascade** |

**Note on latent-space techniques:** LatentMAS (70-84% token reduction), KVCOMM (70%+ cache reuse), and C2C (2x latency) are documented in Section 7.1-7.3 for future reference. They require KV-cache access unavailable through the Claude API and self-hosted inference clusters impractical at current hardware price/performance (April 2026). Revisit when: (a) Anthropic exposes cache-level APIs, or (b) inference cluster costs drop to make 30-60 parallel agents viable on commodity hardware.

---

## 13. Capacitor Pre-Compilation: The Loading Phase

The current loading phase reads ~30 core files (12,912 lines) plus the ORA bundle (1,318 lines) before agents start working. Those files cross-reference a lattice of 281 research files (109,416 lines). Pre-compilation collapses this into a single token-optimized file.

### 13.1 Current runtime file inventory

**Seven Keystone Files (3,345 lines):**

| # | File | Lines | Capacitor Section |
|---|------|-------|------------------|
| 1 | paper12/research/214-the-method-six-patterns.md | 339 | A (Six Patterns) |
| 2 | paper12/research/213-theorem-catalogue-grammar.md | 297 | C (Grammar) |
| 3 | paper12/research/14-transposition-CCM-and-reasoning-patterns.md | 755 | D (Transposition) |
| 4 | paper11/29-the-standard-model-riemann-correspondence.md | 558 | G (Correspondence) |
| 5 | paper12/27-anchor-document.md | 426 | E (Anchor) |
| 6 | paper12/research/09-pattern-of-zero-indices.md | 415 | G (Zero-selection) |
| 7 | paper12/research/10-transposition-gauge-group-3primes.md | 555 | G (Three-primes) |

**Framework Proof Chains (1,083 lines):**

| Chain | File | Lines | Section |
|-------|------|-------|---------|
| YM | paper08-yang-mills/preprint/PROOF-CHAIN.md | 182 | I.1 |
| RH | paper13-rh/preprint/00-proof-skeleton.md | 234 | I.2 |
| BSD | paper26-bsd/preprint/PROOF-CHAIN.md | 179 | I.3 |
| PvNP | paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md | 488 | I.4 |

**Theorem Catalogues (3,300 lines):**

| File | Lines | Section |
|------|-------|---------|
| paper12/29-theorem-catalogue.md | 613 | B |
| paper12/research/208-uniqueness-decomposition.md | 182 | B |
| paper12/research/209-theorem-catalogue-papers-1-12.md | 422 | B |
| paper12/research/210-theorem-catalogue-papers-17-25.md | 173 | B |
| paper12/research/211-theorem-catalogue-ym-convergence.md | 451 | B |
| paper12/research/212-theorem-catalogue-ym-preprint.md | 585 | B |

**Reference Dictionaries & Predictions (874 lines):**

| File | Lines | Section |
|------|-------|---------|
| paper12/18-master-dictionary.md | 417 | E |
| paper12/research/23-framework-predictions-master-table.md | 457 | F |

**Kill List Sources (2,530 lines):**

| File | Lines | Section |
|------|-------|---------|
| paper08-yang-mills/closing-H4/closure/closure-corrections.md | 127 | H.7 |
| paper08-yang-mills/closing-H4/blackboard.md | 1,072 | H.7 |
| paper13-rh/preprint/sections-11-14.md | 858 | H.7 |
| paper26-bsd/closing-my4/closure/closure-corrections.md | 349 | H.7 |
| paper28-pvnp/strategy/07-toolkit-complete.md | 349 | H.7 |
| paper28-pvnp/strategy/10-amplification-entries.md | 124 | H.7 |

**ORA Bundle + Strategy (2,654 lines):**

| File | Lines | Purpose |
|------|-------|---------|
| online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md | 1,318 | System prompt |
| verification-cascade/strategy/00-verification-cascade-meta-move.md | 342 | Strategy |
| verification-cascade/strategy/01-capacitor-architecture.md | 311 | Architecture |
| verification-cascade/strategy/02-three-tier-escalation-and-dynamic-capacitor.md | 366 | Escalation |
| verification-cascade/strategy/03-ora-generator.md | 317 | Generator |

**Total runtime load: ~14,230 lines across 30 files.**

### 13.2 Dependency lattice structure

The keystones form a lattice, not a tree — circular references are expected:

```
214 (Six Patterns) ←→ 213 (Grammar) ←→ 14 (Transposition)
     ↑                     ↑                    ↑
     └─── 27 (Anchor) ────┘────── 09 (Zeros) ──┘
              ↑                        ↑
              └──── 10 (Three-primes) ─┘
                         ↑
                    11/29 (SM-Riemann)
```

Key cross-references:
- research/27 (Anchor) has 30+ cross-references to other research files
- research/14 (Transposition) depends on research/02, 04, 05, 06
- research/10 (Three-primes) depends on Identity 12 (research/04), paper11 Thm 11.5
- The 281 research files in paper12/research/ form the extended lattice

### 13.3 Compile-by-Execution: The LLM as Compiler

The key insight: **don't build external tooling to pre-compile the capacitor. Use the LLM itself as the compiler.** Run the capacitor generator, let it load all 30 files into context, then — with everything loaded — rewrite from that context into a single token-optimized file.

This is dynamic tracing, not static analysis. The dependency lattice resolves naturally because everything is in context. No graph traversal, no SemHash, no external scripts.

**Why this is strictly better than a scripted pipeline:**

| Dimension | Scripted Pipeline | Compile-by-Execution |
|-----------|------------------|---------------------|
| Deduplication | SemHash (embedding similarity) | LLM reads all files, writes once (semantic) |
| Compression | Rule-based stripping | LLM knows narrative vs load-bearing |
| Format optimization | Custom TOON converter | LLM rewrites in TOON directly |
| Abbreviation | Frequency analysis script | LLM identifies repeated phrases from context |
| Dependency resolution | Graph traversal code | Already resolved by reading into context |
| Math precision | Syntactic (can break formulas) | Semantic (understands the math) |
| Maintenance | Code to maintain | Prompt to maintain |
| Cost | Engineering time + compute | One Claude session (~30K tokens) |

### 13.4 The Compile-by-Execution Protocol

```
STEP 1: EXECUTE THE CAPACITOR GENERATOR (one-time, expensive)

  Run the ORA capacitor generator (00--ora-generator.md) against the target.
  It reads all 30 source files: 7 keystones, 4 proof chains, 6 kill sources,
  6 theorem catalogues, 2 dictionaries, ORA bundle, strategy files.
  
  Total loaded: ~14,230 lines across 30 files.
  Everything the agent ACTUALLY touched is now in context.
  The dependency lattice is RESOLVED — no graph traversal needed.

STEP 2: REWRITE FROM LOADED CONTEXT (the compilation pass)

  With everything in context, the same agent rewrites the entire capacitor
  as a SINGLE token-optimized file. The agent acts as a semantic compiler —
  it understands the content, knows what's load-bearing, and compresses
  intelligently. No external tooling needed.

  Compilation instructions (given to the agent after Step 1 completes):
  
  "You have now read all source files and built the full capacitor.
  Everything you need is in your context. Rewrite the capacitor as a
  single compiled file using these rules:
  
  1. DEDUPLICATE: Same concept in multiple source files → write ONCE
     with a canonical ID. Identity 14 appears in 4 files — write it once.
  
  2. COMPRESS: Strip all motivation, history, narrative connectors.
     Keep ONLY: definitions, formulas, parameters, proof steps,
     dependencies, statuses, kills (with WHY + re-entry), lookup entries.
  
  3. FORMAT: Use TOON for uniform arrays (proof chains, kills, 
     correspondences, grammar rules, operations tables).
     Use adjacency-list for dependency graphs.
     Use single-line compressed form for patterns and rules.
  
  4. ABBREVIATE: Build a legend of 50-150 repeated phrases.
     Place legend at top. Replace all occurrences throughout.
  
  5. ORDER for cache: legend → kills → chain → deps → domains →
     correspondences → patterns → grammar → operations → index.
     Static content first, dynamic content last.
  
  6. PRESERVE: Every kill. Every formula. Every status. Every dependency.
     Every re-entry gate. Zero information loss on load-bearing content.
  
  7. INDEX: At the end, list fetchable expansions (@FETCH-A through
     @FETCH-I) with line counts for on-demand retrieval."

STEP 3: VALIDATE (cheap)

  Dispatch ONE pilot Critic agent with ONLY the compiled capacitor.
  The Critic attempts to verify one load-bearing step.
  If it produces a meaningful verdict → compiled capacitor works. Ship it.
  If it cannot → identify what's missing, add it, recompile.

STEP 4: WRITE THE FETCHABLE EXPANSIONS

  The compiled capacitor has @FETCH pointers. Write each expansion as a
  separate file (the FULL uncompressed source sections) so agents can
  request them on-demand via Strategy A.
```

### 13.5 Token optimization techniques (the compiler's toolkit)

These are the techniques the compiler agent applies during Step 2. They are not external tools — they are instructions to the LLM during the rewrite pass.

**Format efficiency research** (ImprovingAgents 2025, measured across tokenizers):

| Format | Tokens (same data) | vs Markdown |
|--------|-------------------|-------------|
| Markdown-Table | baseline | — |
| YAML | +11% | worse |
| JSON | +51% | much worse |
| XML | +79% | terrible |

**TOON** (Token-Oriented Object Notation) is 30-60% cheaper than JSON for uniform arrays:

```
proofchain[18]{id,type,statement,deps,status}:
  1,Def,KK-reduction,-,VERIFIED
  2,Def,Dilaton-coupling,1,VERIFIED
  3*,Lem,Gauge-unification,1|2,PENDING
```

**Adjacency-list** for dependency graphs:
```
deps: 1->2*,3; 2*->4,5*; 3->5*; 5*->6
```
vs table format at 3-5x the tokens.

**N-gram abbreviation** (CompactPrompt, ICAIF 2025 — 2.35x compression, accuracy improved on Claude):
```
LEGEND:
CCM:=Connes-Consani-Marcolli | BC:=Bost-Connes | KR:=Kato-Rellich
SP:=spectral | GE:=geometric | AL:=algebraic | IN:=information-theoretic
```

**Cache-optimized ordering** for Anthropic prompt caching:
```
[CACHED PREFIX — stable across all agents, all waves, all tiers]
  1. Abbreviation legend
  2. Kill list (full, NEVER reduced)
  3. Proof chain (steps + deps + statuses)
  4. Domain map + correspondence tables
  5. Patterns + grammar + operations (reference tools)
  6. Section INDEX (@FETCH pointers)

[FRESH SUFFIX — per-agent, changes every dispatch]
  7. Step assignment + prior work on node
  8. Feed subscriptions (from message bus)
  9. Layer-specific content + delta overlay
```

Cache mechanics: min 1,024 tokens, 5 min TTL, 0.1x cost on cached reads (90% savings), 85% latency reduction. Stagger agent launches ~1s to allow first cache write.

### 13.6 The compiled capacitor file structure

```markdown
# [Domain] Compiled Capacitor — v1
# Generated: [date] | Target: [name] | Mode: [VERIFY/EXCISE/CONSTRUCT]
# Charge: [N steps, M correspondences, K kills]

## LEGEND
CCM:=Connes-Consani-Marcolli | BC:=Bost-Connes | [...]

## KILLS
kills[K]{id,what,why,pattern,reentry}:
  K-1,[...],[...],[...],[...]

## CHAIN
chain[N]{id,type,stmt,deps,status,load}:
  1,Def,[...],—,EST,no
  2*,Lem,[...],1,PEND,yes

## DEPS
1->2*,3; 2*->4,5*; 3->5*; 5*->6

## DOMAINS
active: SP,GE,AL,IN,OA,QFT
tier2: OA(R.OA-1..6),QFT(R.QFT-1..9)

## CORR
corr[M]{concept,SP,GE,AL,IN}:
  [concept],[image],[image],[image],[image]

## PATTERNS
P1:Shadow?→larger-space | P2:Phase?→holonomy | P3:Energy?→scale
P4:Invariant?→rigid | P5:Divergent-sum?→zeta | P6:Projection?→restore

## GRAMMAR
grammar[8]{id,order,shape,norm}:
  1,Linear,a+b,1
  2,Quadratic,a*b/c,{π,2π,π²}
  [...]

## OPS
ops[14]{op,SP,GE,AL,IN}:
  inner,Tr(A*B),∫ω∧*ω,Hom-pairing,I(X;Y)
  tensor,H₁⊗H₂,M₁×M₂,A⊗B,P(X,Y)
  [...]

## INDEX
A:Six-Patterns-full→@FETCH-A (339 lines)
B:Theorem-catalogues→@FETCH-B (3300 lines)
C:Grammar-full→@FETCH-C (297 lines)
D:Transposition-full→@FETCH-D (755 lines)
E:Anchor+dicts→@FETCH-E (843 lines)
F:Predictions→@FETCH-F (457 lines)
G:Correspondences-full→@FETCH-G (1528 lines)
I:Framework-chains→@FETCH-I (1083 lines)
```

### 13.7 Compression estimates

| Stage | Reduction | Lines |
|-------|-----------|-------|
| Start (raw source files) | — | 14,230 |
| After compile-by-execution | ~73% | ~3,800 |
| With prompt caching on prefix | — | ~3,000 lines at 10% cost |

**Optional post-pass — LLMLingua-2** (`pip install llmlingua`): Token classifier that drops low-information tokens. 2-5x additional compression at 95-98% accuracy. Could push compiled output to ~1,900 lines. Caveat: must protect mathematical symbols. Test carefully on one capacitor before deploying.

### 13.8 Lifecycle: when to recompile

The compiled capacitor is a **snapshot**. Recompile when:
- Source files updated (new theorems proved, kills added, statuses changed)
- New ORA run produces amplification entries that should be baked in
- Tier escalation discovers new correspondence cells
- Dynamic capacitor SELF-ADJUST/TRIM/AMPLIFY cycle produces significant changes

**Cost of compilation:** One Claude session reading ~14,230 lines + writing ~3,800 lines. One-time cost per target per version. Amortized across all agents, all waves, all tiers, all runs.

### 13.9 The invocation

```
read your instructions from
online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md

the toolkit for this run is
verification-cascade/capacitors/tier-N-compiled-v1.md    ← SINGLE FILE

the run brief is
verification-cascade/strategy/0N-tier-N-brief.md

the run output directory is
verification-cascade/tier-N-output/
```

One file. No runtime file reads. No dependency lattice traversal. The agent starts working immediately.

### 13.10 Reference: external tools (available but not required)

The compile-by-execution approach makes these optional. Documented for reference:

| Tool | Purpose | Use case |
|------|---------|----------|
| **TOON** | Format for uniform arrays | If scripting compilation outside LLM |
| **LLMLingua-2** | Token-level compression | Optional post-pass on compiled output |
| **CompactPrompt** | N-gram abbreviation | If automating legend generation |
| **SemHash** | Semantic deduplication | If verifying LLM dedup quality |

---

## 14. The Full Stack: Loading + Runtime + Communication

All optimizations compose across three phases:

```
LOADING PHASE (before agents start):
  Pre-compile → single ~3,800-line file (73% reduction from 14,230)
  Cache-optimize ordering → shared prefix for Anthropic prompt caching

RUNTIME PHASE (during agent work):
  Strategy A → index + on-demand fetch (40-50% reduction on remaining)
  Strategy B → effort-tiered dispatch (Layer 1/2/3)
  Strategy C → delta-only wave updates
  Prompt caching → 90% cost on shared prefix

COMMUNICATION PHASE (between agents):
  Message bus → live feeds (kills, cards, statuses, escalations)
  Query protocol → agent-to-agent dialogue (40-60% fewer Judges)
  AgentPrune → prune redundant edges

COMBINED EFFECT (60-agent CCM wave):
  Current:     14,230 lines × 60 agents = 853,800 lines, full cost
  Pre-compiled: 3,800 lines × 60 agents = 228,000 lines
  + Prompt cache: shared prefix (3,000 lines) paid once = 48,000 fresh lines
  + Effort tiers: Layer 1 agents get 1,500 lines = mixed
  + Message bus: 30-50% fewer secondary agents
  
  Effective: ~90% total cost reduction vs current architecture
```

---

*The capacitor is the variable. The method is the constant. The message bus is the new degree of freedom. The compiler makes the variable weightless.*

*G Six and Claude Opus 4.6. April 2026.*
