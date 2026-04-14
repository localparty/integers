"""Dynamic Capacitor — persistent memory that grows through use.

The capacitor stores compiled formulas, kills, blank cells, and
correspondence data. It follows the Self-Adjust-Trim-Amplify cycle
after each ORA verification wave.

Architecture:
  - Five-field cards: WHAT / WHY / DATA / USE / STATUS
  - Three-tier escalation: Verify → Excise → Construct
  - Dynamic cycle: Self-Adjust → Trim → Amplify

Source: verification-cascade/strategy/01-capacitor-architecture.md
         verification-cascade/strategy/02-three-tier-escalation-and-dynamic-capacitor.md
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class DynamicCapacitor:
    """Persistent knowledge store with self-adjust-trim-amplify cycle."""

    def __init__(self, path: Path):
        self.path = path
        self.state = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            return json.loads(self.path.read_text())
        return {
            "version": 1,
            "created": datetime.now().isoformat(),
            "formulas": {},
            "blank_cells": [],
            "kills": [],
            "correspondence": {},
            "cards": [],
            "merge_log": [],
        }

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.state, indent=2, default=str))

    # ── Five-field card management ────────────────────────────────────

    def add_card(self, what: str, why: str, data: str,
                 use: str, status: str = "PENDING") -> dict:
        """Add a five-field deployable knowledge card."""
        card = {
            "id": len(self.state["cards"]) + 1,
            "what": what,
            "why": why,
            "data": data,
            "use": use,
            "status": status,
            "created": datetime.now().isoformat(),
        }
        self.state["cards"].append(card)
        self._save()
        return card

    def update_card_status(self, card_id: int, status: str,
                           note: str = None) -> dict:
        """Update card status: VERIFIED / WEAKENED / BROKEN / PENDING."""
        for card in self.state["cards"]:
            if card["id"] == card_id:
                old_status = card["status"]
                card["status"] = status
                card["last_updated"] = datetime.now().isoformat()
                if note:
                    card["status_note"] = note
                self._save()
                return {"card_id": card_id,
                        "old_status": old_status,
                        "new_status": status}
        raise KeyError(f"Card {card_id} not found")

    # ── Core update cycle ─────────────────────────────────────────────

    def update(self, finding: dict) -> dict:
        """Self-Adjust → Trim → Amplify cycle.

        Args:
            finding: dict with 'type' key and type-specific data.
                     type='formula': new compiled formula
                     type='kill': failed approach
                     type='correspondence': filled blank cell
                     type='blank_cell_priority': prioritize blank cells
        """
        changes = []

        # ── SELF-ADJUST: absorb new finding ───────────────────────────
        finding_type = finding.get("type", "")

        if finding_type == "formula":
            name = finding.get("name", "unknown")
            self.state["formulas"][name] = {
                **finding,
                "added": datetime.now().isoformat(),
            }
            changes.append(f"Added formula: {name}")

        elif finding_type == "kill":
            self.state["kills"].append({
                **finding,
                "killed_at": datetime.now().isoformat(),
            })
            changes.append(f"Added kill: {finding.get('approach', '?')}")

        elif finding_type == "correspondence":
            domain = finding.get("domain", "")
            concept = finding.get("concept", "")
            if domain not in self.state["correspondence"]:
                self.state["correspondence"][domain] = {}
            self.state["correspondence"][domain][concept] = {
                **finding,
                "filled_at": datetime.now().isoformat(),
            }
            changes.append(f"Filled cell: {concept} × {domain}")

        elif finding_type == "blank_cell_priority":
            # Elevate priority of specific blank cells
            domains = finding.get("domains", [])
            concepts = finding.get("concepts", [])
            changes.append(f"Prioritized blank cells: "
                           f"domains={domains}, concepts={concepts}")

        # ── TRIM: remove stale blank cells ────────────────────────────
        before_count = len(self.state["blank_cells"])
        self.state["blank_cells"] = [
            bc for bc in self.state["blank_cells"]
            if not self._is_filled(bc)
        ]
        trimmed = before_count - len(self.state["blank_cells"])
        if trimmed > 0:
            changes.append(f"Trimmed {trimmed} filled blank cells")

        # Downgrade WEAKENED cards
        for card in self.state["cards"]:
            if card["status"] == "WEAKENED":
                # Mark for re-verification
                card["needs_reverification"] = True

        # ── AMPLIFY: cross-domain transfer ────────────────────────────
        if finding_type == "correspondence":
            # If a spectral correspondence was found, check if it
            # implies correspondences in related domains
            domain = finding.get("domain", "")
            concept = finding.get("concept", "")
            amplified = self._attempt_amplification(domain, concept)
            if amplified:
                changes.extend(amplified)

        # ── Version bump ──────────────────────────────────────────────
        self.state["version"] += 1
        self.state["merge_log"].append({
            "version": self.state["version"],
            "date": datetime.now().isoformat(),
            "changes": changes,
            "finding_type": finding_type,
        })

        self._save()
        return {
            "new_version": self.state["version"],
            "changes": changes,
        }

    def _is_filled(self, blank_cell: dict) -> bool:
        """Check if a blank cell has been filled."""
        domain = blank_cell.get("domain", "")
        concept = blank_cell.get("concept", "")
        return (domain in self.state["correspondence"] and
                concept in self.state["correspondence"][domain])

    def _attempt_amplification(self, domain: str, concept: str) -> List[str]:
        """Attempt cross-domain transfer when a new correspondence is found."""
        amplified = []
        # Known bridges between domains
        bridges = {
            "spectral": ["geometric", "algebraic"],
            "geometric": ["topological", "spectral"],
            "number_theoretic": ["algebraic", "automorphic"],
            "algebraic": ["representation_theoretic"],
        }
        if domain in bridges:
            for target_domain in bridges[domain]:
                if (target_domain not in self.state["correspondence"] or
                        concept not in self.state["correspondence"].get(
                            target_domain, {})):
                    amplified.append(
                        f"AMPLIFY: {concept} may have image in "
                        f"{target_domain} (bridge from {domain})")
        return amplified

    # ── Read operations ───────────────────────────────────────────────

    def read(self) -> dict:
        """Read the full capacitor state."""
        return {
            "version": self.state["version"],
            "formulas_compiled": len(self.state["formulas"]),
            "blank_cells": len(self.state["blank_cells"]),
            "kills": len(self.state["kills"]),
            "cards": len(self.state["cards"]),
            "correspondences": sum(
                len(v) for v in self.state["correspondence"].values()
            ),
            "last_update": (self.state["merge_log"][-1]["date"]
                            if self.state["merge_log"] else None),
            "merge_log_length": len(self.state["merge_log"]),
        }

    def get_formulas(self) -> dict:
        return self.state["formulas"]

    def get_kills(self) -> list:
        return self.state["kills"]

    def get_cards(self) -> list:
        return self.state["cards"]

    def get_merge_log(self) -> list:
        return self.state["merge_log"]
