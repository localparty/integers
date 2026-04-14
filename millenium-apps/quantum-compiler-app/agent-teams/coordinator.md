# Agent Team Coordinator

## Architecture

Two Claude instances communicate bidirectionally:

```
@quantum-compiler  ←→  @ora-verifier
     (frontend)          (backend)
```

## Communication protocol

### Compiler → Verifier
When the compiler produces a new formula or updates an existing one:
```json
{
  "type": "verification_request",
  "formula": {
    "name": "observable_name",
    "formula_str": "γ_a · γ_b / (2π)",
    "rule": "3a",
    "operands": [3, 8],
    "compiled_value": 172.468,
    "experimental": 172.76,
    "deviation_pct": 0.17
  },
  "priority": "HIGH",
  "verification_depth": "2x_precision"
}
```

### Verifier → Compiler
After verification completes:
```json
{
  "type": "verification_verdict",
  "formula_name": "m_t",
  "tier": "A",
  "verdict": "SURVIVED",
  "checks": [
    {"check": "grammar_compliance", "status": "PASS"},
    {"check": "precision_2x", "status": "PASS", "value_at_100dps": "172.4682..."},
    {"check": "cross_domain", "status": "PASS", "domains_verified": 6}
  ],
  "card": {
    "WHAT": "m_t = γ₃·γ₈/(2π) verified at 100 dps",
    "WHY": "Top quark Yukawa is foundational for EW sector",
    "DATA": "172.4682 GeV vs 172.76 GeV = 0.17%",
    "USE": "Grammar rule 3a (YUKAWA_QUARK) validated",
    "STATUS": "VERIFIED"
  }
}
```

## Shared state
Both agents read/write the same capacitor at:
`capacitor/capacitor-v1.json`

## Escalation triggers
- `deviation_pct > 0.5%` → automatic verification request
- New formula added to capacitor → verification request
- Grammar rule change → re-verify all formulas using that rule
- Register value updated → re-verify all formulas using that register
