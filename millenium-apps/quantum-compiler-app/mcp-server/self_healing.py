"""Self-Healing Runtime — VIGIL-inspired reflective monitoring.

Monitors the compiler and BC engine for failure patterns,
diagnoses root causes, and triggers healing actions.

Inspired by VIGIL (arXiv:2512.07094).

Source: millenium-apps/quantum-compiler-seed/strategy/41-app-generator-prompt.md
"""

from datetime import datetime
from typing import List, Optional
from capacitor import DynamicCapacitor


class SelfHealingRuntime:
    """Monitors the compiler for failures and triggers healing."""

    def __init__(self, capacitor: DynamicCapacitor):
        self.capacitor = capacitor
        self.event_log: List[dict] = []
        self.diagnosis_history: List[dict] = []

    def log_event(self, event: dict):
        """Log a compilation event (success, failure, anomaly)."""
        self.event_log.append({
            **event,
            "timestamp": datetime.now().isoformat(),
        })
        self._check_patterns()

    def _check_patterns(self):
        """Check for failure patterns that need healing."""
        recent = self.event_log[-10:]

        # Pattern 1: Repeated grammar rule failure
        failures = [e for e in recent if e.get("status") == "FAIL"]
        if len(failures) >= 3:
            rule_counts: dict = {}
            for f in failures:
                rule = f.get("grammar_rule")
                if rule is not None:
                    rule_counts[rule] = rule_counts.get(rule, 0) + 1
            for rule, count in rule_counts.items():
                if count >= 2:
                    self._heal_grammar_rule(
                        rule,
                        [f for f in failures if f.get("grammar_rule") == rule]
                    )

        # Pattern 2: Precision floor hit
        precision_fails = [e for e in recent
                           if e.get("failure_mode") == "precision_floor"]
        if precision_fails:
            self._heal_precision(precision_fails)

        # Pattern 3: Correspondence lookup miss
        misses = [e for e in recent
                  if e.get("failure_mode") == "correspondence_miss"]
        if len(misses) >= 2:
            self._suggest_blank_cell_fill(misses)

        # Pattern 4: Repeated same-register failure
        reg_failures: dict = {}
        for f in failures:
            for reg in f.get("operands", []):
                reg_failures[reg] = reg_failures.get(reg, 0) + 1
        for reg, count in reg_failures.items():
            if count >= 3:
                self._heal_register(reg, failures)

    def _heal_grammar_rule(self, rule, failures: list):
        """A grammar rule is failing repeatedly → re-classify input."""
        diagnosis = {
            "pattern": "repeated_grammar_failure",
            "rule": rule,
            "failure_count": len(failures),
            "inputs": [f.get("input", "?") for f in failures],
            "heal_action": "Re-run lexer with P6 (projection diagnosis)",
            "timestamp": datetime.now().isoformat(),
        }
        self.diagnosis_history.append(diagnosis)

        self.capacitor.update({
            "type": "kill",
            "approach": f"Grammar rule {rule} on inputs "
                        f"{[f.get('input', '?') for f in failures]}",
            "reason": "Repeated failure — check input classification",
            "heal_action": diagnosis["heal_action"],
        })

    def _heal_precision(self, failures: list):
        """Precision floor hit → increase dps."""
        for f in failures:
            current_dps = f.get("dps", 50)
            suggested = current_dps * 2
            diagnosis = {
                "pattern": "precision_floor",
                "current_dps": current_dps,
                "suggested_dps": suggested,
                "observable": f.get("name", "?"),
                "timestamp": datetime.now().isoformat(),
            }
            self.diagnosis_history.append(diagnosis)

    def _suggest_blank_cell_fill(self, misses: list):
        """Multiple correspondence misses → prioritize blank cells."""
        domains = list(set(m.get("domain", "") for m in misses))
        concepts = list(set(m.get("concept", "") for m in misses))

        diagnosis = {
            "pattern": "correspondence_miss",
            "domains": domains,
            "concepts": concepts,
            "miss_count": len(misses),
            "timestamp": datetime.now().isoformat(),
        }
        self.diagnosis_history.append(diagnosis)

        self.capacitor.update({
            "type": "blank_cell_priority",
            "domains": domains,
            "concepts": concepts,
            "reason": f"{len(misses)} correspondence misses in recent compilations",
        })

    def _heal_register(self, register: int, failures: list):
        """A register is involved in many failures → check its value."""
        diagnosis = {
            "pattern": "register_failure",
            "register": register,
            "failure_count": sum(1 for f in failures
                                 if register in f.get("operands", [])),
            "heal_action": f"Re-verify γ_{register} at 2x precision",
            "timestamp": datetime.now().isoformat(),
        }
        self.diagnosis_history.append(diagnosis)

    def get_status(self) -> dict:
        """Return current health status."""
        total = len(self.event_log)
        failures = sum(1 for e in self.event_log if e.get("status") == "FAIL")
        recent = self.event_log[-10:]
        recent_failures = sum(1 for e in recent if e.get("status") == "FAIL")

        if recent_failures == 0:
            health = "HEALTHY"
        elif recent_failures <= 2:
            health = "DEGRADED"
        else:
            health = "CRITICAL"

        return {
            "health": health,
            "total_events": total,
            "total_failures": failures,
            "recent_failures": recent_failures,
            "diagnoses": len(self.diagnosis_history),
            "last_diagnosis": (self.diagnosis_history[-1]
                               if self.diagnosis_history else None),
        }
