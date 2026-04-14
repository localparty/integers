# Self-Healing Protocol

Inspired by VIGIL (arXiv:2512.07094) reflective runtime.

## Failure Patterns Monitored

### Pattern 1: Repeated Grammar Rule Failure
- **Trigger**: Same grammar rule fails 2+ times in last 10 events
- **Diagnosis**: Input misclassification
- **Heal**: Re-run lexer with P6 (projection diagnosis)
- **Action**: Add to kill list, suggest re-classification

### Pattern 2: Precision Floor Hit
- **Trigger**: Computation returns `precision_floor` failure mode
- **Diagnosis**: Insufficient decimal places
- **Heal**: Increase dps to 2x current
- **Action**: Re-compute at higher precision

### Pattern 3: Correspondence Lookup Miss
- **Trigger**: 2+ correspondence misses in last 10 events
- **Diagnosis**: Blank cells blocking compilation
- **Heal**: Prioritize specific blank cells for filling
- **Action**: Update capacitor with blank_cell_priority

### Pattern 4: Register Failure Clustering
- **Trigger**: Same γ_n involved in 3+ failures
- **Diagnosis**: Register value may need re-verification
- **Heal**: Re-verify γ_n at 2x precision
- **Action**: Flag register for independent check

## Health Status Levels

| Level | Condition | Meaning |
|-------|-----------|---------|
| HEALTHY | 0 recent failures | All systems nominal |
| DEGRADED | 1-2 recent failures | Minor issues, self-healing active |
| CRITICAL | 3+ recent failures | Pattern detected, intervention needed |

## Integration with Capacitor

All healing actions update the capacitor:
- Failed approaches → kill list
- Precision upgrades → merge log
- Blank cell priorities → blank_cells array
- Diagnoses → stored in self-healing history
