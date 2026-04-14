"""The 8 Grammar Rules — the quantum compiler's instruction set.

Each rule is a function that takes register indices (γ_n) and returns
a computed value. Together they form the complete ISA for compiling
physical observables from Riemann zeros.

Source of truth: paper12/research/213-theorem-catalogue-grammar.md
"""

from mpmath import mp, mpf, pi, log, exp, euler as gamma_E, zeta
from register_file import RegisterFile
from typing import Optional, Union

# Conversion constant: κ = 2/π²
KAPPA = 2 / pi**2


class Grammar:
    """The 8 grammar rules of the quantum compiler ISA."""

    def __init__(self, register_file: Optional[RegisterFile] = None, dps: int = 50):
        mp.dps = dps + 10
        self.rf = register_file or RegisterFile(dps=dps)

    def _g(self, n: int) -> mpf:
        """Shorthand for register lookup."""
        return self.rf.gamma(n)

    # ── Rule 1: LINEAR → SUM ──────────────────────────────────────────
    # 1st order T_BC: γ_a + γ_b
    # Matrix element: κ(⟨a|L̂|a⟩ + ⟨b|L̂|b⟩)
    # Example: m_W = γ₂ + γ₁₃ = 80.38 GeV (0.012%)
    def rule_sum(self, a: int, b: int) -> mpf:
        return self._g(a) + self._g(b)

    # ── Rule 2: QUADRATIC → PRODUCT ───────────────────────────────────
    # 2nd order T_BC⊗T_BC: γ_a · γ_b / norm
    # Matrix element: κ²⟨a|L̂|a⟩⟨b|L̂|b⟩
    # Example: 1/α = γ₁·γ₄/π + 0.1·log(π) = 137.003 (0.024%)
    def rule_product(self, a: int, b: int, norm: Optional[mpf] = None) -> mpf:
        if norm is None:
            norm = pi
        return self._g(a) * self._g(b) / norm

    # ── Rule 3a: BILINEAR YUKAWA (quark) ──────────────────────────────
    # Bilinear rank-2 with KK normalization: γ_a · γ_b / (2π)
    # KK reduction on S¹: SU(3) colour charge → integrate over 2π
    # Example: m_t = γ₃·γ₈/(2π) = 172.49 GeV (0.17%)
    def rule_yukawa_quark(self, a: int, b: int) -> mpf:
        return self._g(a) * self._g(b) / (2 * pi)

    # ── Rule 3b: BARE PRODUCT (lepton) ────────────────────────────────
    # Bilinear rank-2 without KK: γ_a · γ_b
    # Colour singlets → no S¹ integration
    # Example: m_τ = γ₇·γ₈ = 1772.89 MeV (0.22%)
    def rule_yukawa_lepton(self, a: int, b: int) -> mpf:
        return self._g(a) * self._g(b)

    # ── Rule 4: EXPONENTIAL ───────────────────────────────────────────
    # exp(L̂ eigenvalue): exp(γ_n · π²/2)
    # Matrix element: ⟨n|R̂|n⟩ (R̂ eigenvalue)
    # Example: CC hierarchy: R_obs/R_bare = exp(γ₁·π²/2) ~ 2×10³⁰
    def rule_exponential(self, n: int) -> mpf:
        return exp(self._g(n) * pi**2 / 2)

    # ── Rule 5: LOG THERMAL ───────────────────────────────────────────
    # log(eigenvalue): log(γ_n) or (log γ_n)^p
    # Matrix element: log(κ⟨n|L̂|n⟩)
    # Example: m_b = log(γ₁₅) = 4.176 GeV (0.093%)
    def rule_log(self, n: int, power: int = 1) -> mpf:
        val = log(self._g(n))
        if power != 1:
            val = val ** power
        return val

    # ── Rule 6: FRACTIONAL POWER ──────────────────────────────────────
    # 1/k from internal degrees of freedom: γ_n^(1/k)
    # k=3: 3-fold generation symmetry → N_eff = γ₆^(1/3)
    # k=4: 4-fold EW multiplet → m_μ = γ₇·γ₈^(1/4)
    # 3/4: complement → m_τ/m_μ = γ₈^(3/4)
    def rule_fractional(self, n: int, p: int, q: int = 1) -> mpf:
        """γ_n^(p/q)"""
        return self._g(n) ** (mpf(p) / mpf(q))

    # ── Rule 7: RATIO ─────────────────────────────────────────────────
    # Relative scale: γ_n / γ_m
    # Matrix element: ⟨n|L̂|n⟩ / ⟨m|L̂|m⟩
    # Example: n_s = γ₉/γ₁₀ = 0.9644 (0.056%)
    def rule_ratio(self, a: int, b: int) -> mpf:
        return self._g(a) / self._g(b)

    # ── Rule 8: DIFFERENCE ────────────────────────────────────────────
    # Linear gap: γ_a − γ_b
    # Matrix element: κ(⟨a|L̂|a⟩ − ⟨b|L̂|b⟩)
    # Example: m_d = γ₉ − γ₈ = 4.678 MeV (0.17%)
    def rule_difference(self, a: int, b: int) -> mpf:
        return self._g(a) - self._g(b)

    # ── Composite operations (built from grammar rules) ───────────────

    def rule_product_with_correction(self, a: int, b: int,
                                      norm: mpf = None,
                                      additive_correction: mpf = None) -> mpf:
        """Product rule + additive correction term.
        Example: 1/α = γ₁·γ₄/π + 0.1·log(π)
        """
        base = self.rule_product(a, b, norm)
        if additive_correction is not None:
            base += additive_correction
        return base

    def rule_product_with_pi2_norm(self, a: int, b: int) -> mpf:
        """Product with π² normalization (2nd-gen quarks).
        Example: m_s = γ₁·γ₁₅/π²
        """
        return self._g(a) * self._g(b) / pi**2

    def rule_scaled(self, n: int, scale: mpf = None) -> mpf:
        """Single register times a scale factor.
        Example: H₀ = γ₁₁·4/π, v = γ₁₀·π²/2
        """
        return self._g(n) * scale

    def rule_reciprocal_log(self, n: int) -> mpf:
        """1/log(γ_n). Example: Y_p = 1/log(γ₁₃)"""
        return 1 / log(self._g(n))

    def rule_log_product(self, n: int, constant: mpf = None) -> mpf:
        """log(γ_n) × constant. Example: J_CKM = log(γ₁)·ζ(3)"""
        val = log(self._g(n))
        if constant is not None:
            val *= constant
        return val

    # ── Dispatch by rule name ─────────────────────────────────────────

    RULE_NAMES = {
        1: "SUM",
        2: "PRODUCT",
        "3a": "YUKAWA_QUARK",
        "3b": "YUKAWA_LEPTON",
        4: "EXPONENTIAL",
        5: "LOG",
        6: "FRACTIONAL",
        7: "RATIO",
        8: "DIFFERENCE",
    }

    def apply(self, rule: Union[int, str], **kwargs) -> mpf:
        """Apply a grammar rule by number or name."""
        dispatch = {
            1: lambda: self.rule_sum(kwargs["a"], kwargs["b"]),
            "SUM": lambda: self.rule_sum(kwargs["a"], kwargs["b"]),
            2: lambda: self.rule_product(kwargs["a"], kwargs["b"],
                                          kwargs.get("norm")),
            "PRODUCT": lambda: self.rule_product(kwargs["a"], kwargs["b"],
                                                   kwargs.get("norm")),
            "3a": lambda: self.rule_yukawa_quark(kwargs["a"], kwargs["b"]),
            "YUKAWA_QUARK": lambda: self.rule_yukawa_quark(kwargs["a"], kwargs["b"]),
            "3b": lambda: self.rule_yukawa_lepton(kwargs["a"], kwargs["b"]),
            "YUKAWA_LEPTON": lambda: self.rule_yukawa_lepton(kwargs["a"], kwargs["b"]),
            4: lambda: self.rule_exponential(kwargs["n"]),
            "EXPONENTIAL": lambda: self.rule_exponential(kwargs["n"]),
            5: lambda: self.rule_log(kwargs["n"], kwargs.get("power", 1)),
            "LOG": lambda: self.rule_log(kwargs["n"], kwargs.get("power", 1)),
            6: lambda: self.rule_fractional(kwargs["n"], kwargs["p"],
                                             kwargs.get("q", 1)),
            "FRACTIONAL": lambda: self.rule_fractional(kwargs["n"], kwargs["p"],
                                                        kwargs.get("q", 1)),
            7: lambda: self.rule_ratio(kwargs["a"], kwargs["b"]),
            "RATIO": lambda: self.rule_ratio(kwargs["a"], kwargs["b"]),
            8: lambda: self.rule_difference(kwargs["a"], kwargs["b"]),
            "DIFFERENCE": lambda: self.rule_difference(kwargs["a"], kwargs["b"]),
        }
        key = rule
        if key not in dispatch:
            raise ValueError(f"Unknown grammar rule: {rule}. "
                             f"Valid: {list(dispatch.keys())}")
        return dispatch[key]()
