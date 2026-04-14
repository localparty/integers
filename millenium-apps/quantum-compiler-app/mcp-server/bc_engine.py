"""Bost-Connes Algebra Engine — the compiler's target language.

All physical observables compile to matrix elements of L̂ = log R̂
in the spectral basis of the BC system at KMS_infinity.

Constant κ = 2/π² converts between raw eigenvalues and physical units.

Source: paper12/27-anchor-document.md
"""

from mpmath import mp, mpf, pi, log, exp, euler as gamma_E, zeta
from register_file import RegisterFile
from grammar import Grammar
from typing import Optional


class BCAlgebra:
    """The Bost-Connes algebra engine.

    Provides:
    - Matrix element computation: ⟨n|O|m⟩ for operators L̂, R̂
    - Modular flow simulation: σ_t on BC states
    - Grammar rule evaluation via the Grammar class
    - Full compilation pipeline
    """

    def __init__(self, dps: int = 100):
        self.dps = dps
        mp.dps = dps + 20
        self.rf = RegisterFile(dps=dps)
        self.grammar = Grammar(register_file=self.rf, dps=dps)
        self.kappa = 2 / pi**2  # BC scale factor

    def gamma(self, n: int) -> mpf:
        """Return γ_n — shorthand for register lookup."""
        return self.rf.gamma(n)

    # ── Operator matrix elements ──────────────────────────────────────

    def L_hat(self, n: int, m: int = None) -> mpf:
        """⟨n|L̂|m⟩ = γ_n · π²/2 · δ_{nm}

        L̂ is diagonal in the spectral basis.
        Eigenvalues L_n = γ_n · π²/2 (Basel sum scale).
        """
        if m is not None and m != n:
            return mpf(0)
        return self.gamma(n) * pi**2 / 2

    def R_hat(self, n: int, m: int = None) -> mpf:
        """⟨n|R̂|n⟩ = exp(γ_n · π²/2)

        R̂ = exp(L̂), scaling operator. Diagonal.
        """
        if m is not None and m != n:
            return mpf(0)
        return exp(self.L_hat(n))

    def matrix_element(self, n: int, m: int = None,
                       operator: str = "L_hat") -> mpf:
        """Compute ⟨n|operator|m⟩."""
        ops = {
            "L_hat": self.L_hat,
            "R_hat": self.R_hat,
        }
        if operator not in ops:
            raise ValueError(f"Unknown operator: {operator}. "
                             f"Valid: {list(ops.keys())}")
        return ops[operator](n, m)

    # ── Modular flow ──────────────────────────────────────────────────

    def modular_flow(self, n: int, t: float) -> dict:
        """Simulate Tomita-Takesaki modular flow σ_t on state |n⟩.

        σ_t(a) = Δ^{it} a Δ^{-it} where Δ = R̂.
        On diagonal elements: σ_t(⟨n|L̂|n⟩) = exp(iγ_n·π²t/2) · ⟨n|L̂|n⟩

        Returns phase and modulated eigenvalue.
        """
        L_n = self.L_hat(n)
        phase = self.gamma(n) * pi**2 * mpf(t) / 2
        return {
            "n": n,
            "t": t,
            "L_n": str(L_n),
            "phase": str(phase),
            "phase_mod_2pi": str(phase % (2 * pi)),
            "cos_phase": str(mp.cos(phase)),
            "sin_phase": str(mp.sin(phase)),
        }

    # ── Compilation ───────────────────────────────────────────────────

    def compile_formula(self, entry: dict) -> dict:
        """Compile a master table entry and compare to experiment.

        Args:
            entry: dict from MASTER_TABLE with 'compute' callable and
                   'experimental' value.

        Returns:
            Compilation result with value, error, verdict.
        """
        computed = float(entry["compute"](self.rf))
        experimental = entry["experimental"]

        if experimental != 0:
            deviation_pct = abs(computed - experimental) / abs(experimental) * 100
        else:
            deviation_pct = float("inf")

        if deviation_pct < 0.1:
            verdict = "PASS"
        elif deviation_pct < 1.0:
            verdict = "PASS"
        else:
            verdict = "FAIL"

        return {
            "name": entry["name"],
            "formula": entry["formula_str"],
            "rule": entry["rule"],
            "operands": entry["operands"],
            "compiled_value": computed,
            "experimental": experimental,
            "deviation_pct": deviation_pct,
            "unit": entry["unit"],
            "sector": entry["sector"],
            "verdict": verdict,
        }

    def compile_all(self) -> list:
        """Compile all 36 formulas in the master table."""
        from master_table import MASTER_TABLE
        results = []
        for entry in MASTER_TABLE:
            results.append(self.compile_formula(entry))
        return results

    def verify(self, formula_name: str, experimental_value: float = None) -> dict:
        """Verify a single formula against experiment."""
        from master_table import get_by_name
        entry = get_by_name(formula_name)
        if experimental_value is not None:
            entry = {**entry, "experimental": experimental_value}
        return self.compile_formula(entry)
