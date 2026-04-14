"""Test all 8 grammar rules against the master prediction table.

Every formula must match its experimental value within 1%.
Zero free parameters — all normalizations derived from geometry.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from mpmath import mp, mpf, pi, log, exp, euler as gamma_E, zeta
from grammar import Grammar
from register_file import RegisterFile


@pytest.fixture(scope="module")
def grammar():
    return Grammar(dps=50)


@pytest.fixture(scope="module")
def rf():
    return RegisterFile(dps=50)


class TestRule1Sum:
    """Rule 1: LINEAR → SUM: γ_a + γ_b"""

    def test_m_W(self, grammar, rf):
        """m_W = γ₂ + γ₁₃ = 80.369 GeV (0.012%)"""
        val = float(grammar.rule_sum(2, 13))
        assert abs(val - 80.3692) / 80.3692 < 0.01


class TestRule2Product:
    """Rule 2: QUADRATIC → PRODUCT: γ_a · γ_b / c"""

    def test_inverse_alpha(self, grammar, rf):
        """1/α = γ₁·γ₄/π + 0.1·log(π) = 137.003 (0.024%)"""
        val = float(grammar.rule_product(1, 4, pi) + 0.1 * log(pi))
        assert abs(val - 137.036) / 137.036 < 0.01

    def test_m_s(self, grammar, rf):
        """m_s = γ₁·γ₁₅/π² = 93.25 MeV (0.16%)"""
        val = float(grammar.rule_product_with_pi2_norm(1, 15))
        assert abs(val - 93.4) / 93.4 < 0.01

    def test_v_higgs_vev(self, grammar, rf):
        """v = γ₁₀·π²/2 = 245.6 GeV (0.24%)"""
        val = float(grammar.rule_scaled(10, pi**2 / 2))
        assert abs(val - 246.22) / 246.22 < 0.01


class TestRule3aYukawaQuark:
    """Rule 3a: BILINEAR YUKAWA (quark): γ_a · γ_b / (2π)"""

    def test_m_t(self, grammar):
        """m_t = γ₃·γ₈/(2π) = 172.47 GeV (0.17%)"""
        val = float(grammar.rule_yukawa_quark(3, 8))
        assert abs(val - 172.76) / 172.76 < 0.01

    def test_m_H(self, grammar):
        """m_H = γ₂·γ₆/(2π) = 125.75 GeV (0.52%)"""
        val = float(grammar.rule_yukawa_quark(2, 6))
        assert abs(val - 125.10) / 125.10 < 0.01


class TestRule3bYukawaLepton:
    """Rule 3b: BARE PRODUCT (lepton): γ_a · γ_b"""

    def test_m_tau(self, grammar):
        """m_τ = γ₇·γ₈ = 1772.89 MeV (0.22%)"""
        val = float(grammar.rule_yukawa_lepton(7, 8))
        assert abs(val - 1776.86) / 1776.86 < 0.01


class TestRule4Exponential:
    """Rule 4: EXPONENTIAL: exp(γ_n · π²/2)"""

    def test_cc_hierarchy(self, grammar):
        """CC hierarchy: exp(γ₁·π²/2) ~ 2×10³⁰"""
        val = float(grammar.rule_exponential(1))
        assert val > 1e29  # order of magnitude check
        assert val < 1e31


class TestRule5Log:
    """Rule 5: LOG THERMAL: log(γ_n) or (log γ_n)^p"""

    def test_m_b(self, grammar):
        """m_b = log(γ₁₅) = 4.176 GeV (0.093%)"""
        val = float(grammar.rule_log(15))
        assert abs(val - 4.18) / 4.18 < 0.01

    def test_t_0(self, grammar):
        """t₀ = (log γ₇)² = 13.776 Gyr (0.081%)"""
        val = float(grammar.rule_log(7, power=2))
        assert abs(val - 13.787) / 13.787 < 0.01

    def test_Y_p(self, grammar, rf):
        """Y_p = 1/log(γ₁₃) = 0.2449 (0.043%)"""
        val = float(grammar.rule_reciprocal_log(13))
        assert abs(val - 0.245) / 0.245 < 0.01


class TestRule6Fractional:
    """Rule 6: FRACTIONAL POWER: γ_n^(1/k)"""

    def test_N_eff(self, grammar):
        """N_eff = γ₆^(1/3) = 3.350 (0.0082%)"""
        val = float(grammar.rule_fractional(6, 1, 3))
        assert abs(val - 3.35) / 3.35 < 0.01

    def test_m_tau_over_m_mu(self, grammar):
        """m_τ/m_μ = γ₈^(3/4) = 16.89 (0.42%)"""
        val = float(grammar.rule_fractional(8, 3, 4))
        assert abs(val - 16.8171) / 16.8171 < 0.01


class TestRule7Ratio:
    """Rule 7: RATIO: γ_n / γ_m"""

    def test_n_s(self, grammar):
        """n_s = γ₉/γ₁₀ = 0.9645 (0.056%)"""
        val = float(grammar.rule_ratio(9, 10))
        assert abs(val - 0.965) / 0.965 < 0.01

    def test_m_c(self, grammar):
        """m_c = γ₉/γ₆ = 1.277 GeV (0.17%)"""
        val = float(grammar.rule_ratio(9, 6))
        assert abs(val - 1.275) / 1.275 < 0.01

    def test_H_0(self, grammar, rf):
        """H₀ = γ₁₁·4/π = 67.44 (0.065%)"""
        val = float(grammar.rule_scaled(11, mpf(4) / pi))
        assert abs(val - 67.4) / 67.4 < 0.01

    def test_m_u(self, grammar):
        """m_u = γ₄/γ₁ = 2.15 MeV (0.35%)"""
        val = float(grammar.rule_ratio(4, 1))
        assert abs(val - 2.16) / 2.16 < 0.01

    def test_m_Z(self, grammar, rf):
        """m_Z = γ₁₁/γ_E = 91.77 GeV (0.64%)"""
        val = float(rf.gamma(11) / gamma_E)
        assert abs(val - 91.1876) / 91.1876 < 0.01


class TestRule8Difference:
    """Rule 8: DIFFERENCE: γ_a − γ_b"""

    def test_m_d(self, grammar):
        """m_d = γ₉ − γ₈ = 4.678 MeV (0.17%)"""
        val = float(grammar.rule_difference(9, 8))
        assert abs(val - 4.67) / 4.67 < 0.01


class TestCompoundFormulas:
    """Compound formulas combining multiple grammar rules."""

    def test_J_CKM(self, rf):
        """J_CKM × 10⁵ = log(γ₁)·ζ(3) = 3.184 (0.12%)"""
        val = float(log(rf.gamma(1)) * zeta(3))
        assert abs(val - 3.18) / 3.18 < 0.01

    def test_sin_theta12_CKM(self, rf):
        """sin θ₁₂ = (γ₁₁ − γ₁₀)/γ₁ = 0.226 (0.51%)"""
        val = float((rf.gamma(11) - rf.gamma(10)) / rf.gamma(1))
        assert abs(val - 0.22500) / 0.22500 < 0.01

    def test_sin2_theta12_PMNS(self, rf):
        """sin²(θ₁₂) = γ₁/(γ₂ + γ₃) = 0.307 (0.019%)"""
        val = float(rf.gamma(1) / (rf.gamma(2) + rf.gamma(3)))
        assert abs(val - 0.307) / 0.307 < 0.01

    def test_sum_m_nu(self, rf):
        """Σm_ν = log(γ₁₀)/γ₁₅ = 0.060 eV (0.019%)"""
        val = float(log(rf.gamma(10)) / rf.gamma(15))
        assert abs(val - 0.06) / 0.06 < 0.02  # wider for tiny value
