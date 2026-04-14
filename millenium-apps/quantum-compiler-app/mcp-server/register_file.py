"""Register file: the first 15 non-trivial Riemann zeros.

Each gamma_n is a hardware register in the quantum compiler's ISA.
Values from LMFDB, certified to 40+ decimal places.
mpmath.zetazero(n) provides arbitrary-precision computation.
"""

from mpmath import mp, mpf, im, zetazero
from typing import Dict, List, Optional

# Precomputed imaginary parts of the first 15 non-trivial zeros of zeta(s).
# These are the "registers" of the quantum compiler.
GAMMA_PRECOMPUTED = {
    1:  "14.134725141734693790457251983562470270784257115699",
    2:  "21.022039638771554992628479593896902777334340524903",
    3:  "25.010857580145688763213790992562821818659549672558",
    4:  "30.424876125859513210311897530584091320181560023715",
    5:  "32.935061587739189690662368964074903488812715603517",
    6:  "37.586178158825671257217763480705332821405597350831",
    7:  "40.918719012147495187398126914633254395726165962777",
    8:  "43.327073280914999519496122165406805782645668371837",
    9:  "48.005150881167159727942472749427516041686844001144",
    10: "49.773832477672302181916784678563724057723178299677",
    11: "52.970321477714460644147296608880990063825017888821",
    12: "56.446247697063394804367759476706198987630750214411",
    13: "59.347044002602353079653648674992219031098772806467",
    14: "60.831778524609809844259901824524003802910090451219",
    15: "65.112544048081606660875054253183705029348149295167",
}

# Physical role of each register (from research/09-pattern-of-zero-indices.md)
REGISTER_ROLES = {
    1:  {"frequency": 11, "role": "FOUNDATIONAL — U(1) singlet, EM gauge boson",
         "sm_interpretation": "dim(adjoint U(1)) = 1 photon"},
    2:  {"frequency": 4, "role": "Higgs sector, CC correction, m_W",
         "sm_interpretation": "Higgs scalar representation"},
    3:  {"frequency": 3, "role": "CC correction, m_t",
         "sm_interpretation": "3rd generation quark"},
    4:  {"frequency": 3, "role": "EM/EW partner of γ₁ — 1/α, m_t/m_W, m_u",
         "sm_interpretation": "1+3 = EW unbroken generators"},
    5:  {"frequency": 3, "role": "Mirror brane ξ, inflation, CKM V_us/V_cb",
         "sm_interpretation": "5D compact dimension"},
    6:  {"frequency": 6, "role": "EW WORKHORSE — N_eff, m_H, m_W/m_Z, m_c, 1/α₂",
         "sm_interpretation": "order of Z₆ center (Z₂ × Z₃)"},
    7:  {"frequency": 2, "role": "Lepton masses: m_τ, m_μ, age of universe",
         "sm_interpretation": "Lepton sector"},
    8:  {"frequency": 4, "role": "SU(3) ADJOINT — m_τ/m_μ, m_t, m_d, m_τ",
         "sm_interpretation": "dim(adjoint SU(3)) = 8 gluons"},
    9:  {"frequency": 6, "role": "QUARK/COSMOLOGY HUB — m_c, n_s, Δm², PMNS",
         "sm_interpretation": "Quark-cosmology bridge"},
    10: {"frequency": 5, "role": "n_s, v (Higgs VEV), m_t/m_b, CKM δ_CP",
         "sm_interpretation": "EW symmetry breaking scale"},
    11: {"frequency": 4, "role": "H₀, m_Z, 1/α₃, CKM sin θ₁₂",
         "sm_interpretation": "Strong/cosmological link"},
    12: {"frequency": 2, "role": "PMNS sin²(2θ₁₂), δ_CP PMNS alt",
         "sm_interpretation": "Neutrino sector"},
    13: {"frequency": 3, "role": "m_W, Y_p, CKM δ_CP, PMNS sin²(2θ₁₃)",
         "sm_interpretation": "Weak/cosmological bridge"},
    14: {"frequency": 1, "role": "η₁₀ (baryon/photon ratio)",
         "sm_interpretation": "Baryogenesis"},
    15: {"frequency": 4, "role": "m_b, m_s, PMNS sin²(2θ₁₃), Σm_ν",
         "sm_interpretation": "Heavy quark/neutrino mass link"},
}

# Gauge-distinguished index set: the four SM gauge invariants
GAUGE_DISTINGUISHED = {1, 4, 6, 8}


class RegisterFile:
    """The quantum compiler's register file: gamma_n values at arbitrary precision."""

    def __init__(self, dps: int = 100):
        self.dps = dps
        mp.dps = dps + 20  # extra guard digits
        self._cache: Dict[int, mpf] = {}
        # Pre-load from certified values
        for n, val_str in GAMMA_PRECOMPUTED.items():
            self._cache[n] = mpf(val_str)

    def gamma(self, n: int) -> mpf:
        """Return γ_n, the imaginary part of the nth non-trivial Riemann zero."""
        if n < 1:
            raise ValueError(f"Zero index must be >= 1, got {n}")
        if n not in self._cache:
            mp.dps = self.dps + 20
            self._cache[n] = im(zetazero(n))
        return +self._cache[n]  # unary + to round to current dps

    def lookup(self, n: int) -> dict:
        """Full register lookup: value + metadata."""
        val = self.gamma(n)
        role = REGISTER_ROLES.get(n, {"frequency": 0, "role": "UNCHARTED",
                                       "sm_interpretation": "Unknown"})
        # Find all formulas using this register
        from master_table import MASTER_TABLE
        formulas_using = [f["name"] for f in MASTER_TABLE
                          if n in f.get("operands", [])]
        return {
            "n": n,
            "value": str(val),
            "frequency": role["frequency"],
            "role": role["role"],
            "sm_interpretation": role["sm_interpretation"],
            "gauge_distinguished": n in GAUGE_DISTINGUISHED,
            "formulas_using": formulas_using,
        }

    def all_registers(self) -> List[dict]:
        """Return all 15 preloaded registers with metadata."""
        return [self.lookup(n) for n in range(1, 16)]
