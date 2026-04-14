# Token Optimization Strategy

## Prompt Caching

The capacitor is the ideal cache candidate: large (~20K tokens), stable
(changes only after compilations), read on every session start.

### Cache structure

```
System message (cached, 1-hour TTL):
  - Compiler identity + grammar rules + Six Patterns + operator dictionary
  - ~15K tokens, cached at 0.1x cost after first call

System message (cached, 5-min TTL):
  - Current capacitor state (formulas, kills, correspondence matrix)
  - ~5-10K tokens, refreshed every 5 minutes

User message (not cached):
  - Current compilation request
  - ~500-2K tokens
```

### Savings

| Scenario | Tokens | Cost |
|----------|--------|------|
| Without caching | ~22K per request | 1x |
| With caching | ~2K new + 20K cached at 0.1x | ~0.18x |
| **Savings** | | **~82% per request** |

## Batch API

For background exploration of blank cells:

```
Queue 100+ candidate compilations as a batch:
- Try all grammar rules on γ₁₆ with each placed zero
- Try all grammar rules on pairs of unplaced zeros
- Check each output against known physics

Batch API cost: 50% of standard
Combined with caching: ~5% of naive cost
```

### Overnight workflow
1. Evening: queue 200 candidate compilations
2. Overnight: batch processes at 50% cost
3. Morning: collect results, update capacitor with any matches
4. New blank cells filled, kill list updated
