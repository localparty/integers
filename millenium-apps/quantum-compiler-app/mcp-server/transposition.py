"""Transposition Dictionary — additive ↔ multiplicative bridge.

Maps every construct in the additive (e-circle, Paper 9) formulation
to its multiplicative (BC algebra, Paper 12) counterpart via
Mellin duality.

Core principle: V T_CCM V* = T_BC (Identity 14 intertwining relation)

Source: paper12/research/14-transposition-CCM-and-reasoning-patterns.md
"""

from typing import Dict


# ── The transposition dictionary ──────────────────────────────────────

TRANSPOSITION: Dict[str, Dict[str, str]] = {
    "compact_manifold": {
        "additive": "S¹_R, compact manifold",
        "multiplicative": "N*, multiplicative semigroup",
    },
    "coordinate": {
        "additive": "θ ∈ [0, 2π)",
        "multiplicative": "log u ∈ R",
    },
    "symmetry": {
        "additive": "Translation θ ↦ θ + a",
        "multiplicative": "Dilation u ↦ λu",
    },
    "generator": {
        "additive": "Momentum p̂_e = −i∂_θ",
        "multiplicative": "Scaling generator T_BC",
    },
    "expansion": {
        "additive": "Fourier series Σ c_n e^{inθ}",
        "multiplicative": "Mellin transform ∫ f(u) u^{s−1} du",
    },
    "mode_sum": {
        "additive": "KK sum over n ∈ Z",
        "multiplicative": "Dirichlet series over N*",
    },
    "vacuum_energy": {
        "additive": "Casimir energy (−π²/90R⁴)",
        "multiplicative": "BC free energy −log ζ(β)",
    },
    "holonomy": {
        "additive": "Holonomy around S¹",
        "multiplicative": "n^{it} phase of μ_n",
    },
    "fundamental_group": {
        "additive": "π₁(S¹) = Z",
        "multiplicative": "Gal(Q^cyc/Q) ≅ Ẑ*",
    },
    "regularization": {
        "additive": "Zeta-regularised: 1 + 2ζ(0) = 0",
        "multiplicative": "Explicit formula: pole at s = 1",
    },
    "partial_trace": {
        "additive": "Partial trace over θ",
        "multiplicative": "Partial trace over log N",
    },
}

# ── Code generation templates ─────────────────────────────────────────
# Maps formula templates to BC operator expressions.

CODE_GEN_TEMPLATES = {
    "gamma_n": {
        "source": "γ_n (register value)",
        "bc_expr": "κ · ⟨n|L̂|n⟩",
        "expansion": "(2/π²) · ⟨n|L̂|n⟩",
        "note": "κ = 2/π² is the BC scale factor",
    },
    "product": {
        "source": "γ_a · γ_b",
        "bc_expr": "κ² · ⟨a|L̂|a⟩ · ⟨b|L̂|b⟩",
        "expansion": "(2/π²)² · ⟨a|L̂|a⟩ · ⟨b|L̂|b⟩",
    },
    "ratio": {
        "source": "γ_a / γ_b",
        "bc_expr": "⟨a|L̂|a⟩ / ⟨b|L̂|b⟩",
        "expansion": "Ratio of eigenvalues (κ cancels)",
    },
    "sum": {
        "source": "γ_a + γ_b",
        "bc_expr": "κ · (⟨a|L̂|a⟩ + ⟨b|L̂|b⟩)",
        "expansion": "(2/π²) · (⟨a|L̂|a⟩ + ⟨b|L̂|b⟩)",
    },
    "difference": {
        "source": "γ_a − γ_b",
        "bc_expr": "κ · (⟨a|L̂|a⟩ − ⟨b|L̂|b⟩)",
        "expansion": "(2/π²) · (⟨a|L̂|a⟩ − ⟨b|L̂|b⟩)",
    },
    "power": {
        "source": "γ_n^p",
        "bc_expr": "(κ · ⟨n|L̂|n⟩)^p",
        "expansion": "(2/π²)^p · ⟨n|L̂|n⟩^p",
    },
    "log": {
        "source": "log(γ_n)",
        "bc_expr": "log(κ · ⟨n|L̂|n⟩)",
        "expansion": "log((2/π²) · ⟨n|L̂|n⟩)",
    },
    "exponential": {
        "source": "exp(γ_n · π²/2)",
        "bc_expr": "⟨n|R̂|n⟩",
        "expansion": "Eigenvalue of R̂ = exp(L̂)",
        "note": "Direct R̂ eigenvalue, no κ needed",
    },
    "reciprocal_log": {
        "source": "1/log(γ_n)",
        "bc_expr": "1/log(κ · ⟨n|L̂|n⟩)",
        "expansion": "Reciprocal of log eigenvalue",
    },
}


class Transposer:
    """Translate between additive and multiplicative formulations."""

    def transpose(self, concept: str) -> dict:
        """Look up the transposition of a concept."""
        if concept not in TRANSPOSITION:
            return {
                "concept": concept,
                "found": False,
                "note": f"'{concept}' not in transposition dictionary",
            }
        entry = TRANSPOSITION[concept]
        return {
            "concept": concept,
            "found": True,
            "additive": entry["additive"],
            "multiplicative": entry["multiplicative"],
        }

    def generate_code(self, template_name: str, **kwargs) -> dict:
        """Generate BC operator expression from a template.

        Args:
            template_name: key from CODE_GEN_TEMPLATES
            **kwargs: template variables (n, a, b, p, etc.)

        Returns:
            dict with bc_expr, expansion, and substituted form.
        """
        if template_name not in CODE_GEN_TEMPLATES:
            return {"error": f"Unknown template: {template_name}"}

        template = CODE_GEN_TEMPLATES[template_name]
        result = {
            "template": template_name,
            "source_form": template["source"],
            "bc_expression": template["bc_expr"],
            "expansion": template["expansion"],
        }
        if "note" in template:
            result["note"] = template["note"]

        # Substitute specific register values if provided
        if "n" in kwargs:
            result["registers"] = {"n": kwargs["n"]}
        if "a" in kwargs and "b" in kwargs:
            result["registers"] = {"a": kwargs["a"], "b": kwargs["b"]}

        return result

    def all_entries(self) -> list:
        """Return the full transposition dictionary."""
        return [{"concept": k, **v} for k, v in TRANSPOSITION.items()]
