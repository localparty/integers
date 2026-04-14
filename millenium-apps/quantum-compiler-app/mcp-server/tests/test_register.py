"""Test the register file: γ_n values at high precision.

Verifies the first 15 Riemann zeros against known values.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from mpmath import mp, mpf
from register_file import RegisterFile, GAMMA_PRECOMPUTED


@pytest.fixture(scope="module")
def rf():
    return RegisterFile(dps=100)


# Known values (truncated for test comparison)
KNOWN_VALUES = {
    1:  14.134725141734693,
    2:  21.022039638771555,
    3:  25.010857580145689,
    4:  30.424876125859513,
    5:  32.935061587739190,
    6:  37.586178158825671,
    7:  40.918719012147495,
    8:  43.327073280914999,
    9:  48.005150881167160,
    10: 49.773832477672302,
    11: 52.970321477714461,
    12: 56.446247697063395,
    13: 59.347044002602353,
    14: 60.831778524609810,
    15: 65.112544048081607,
}


class TestRegisterValues:
    """Test that all 15 registers match known zero values."""

    @pytest.mark.parametrize("n", range(1, 16))
    def test_gamma_n(self, rf, n):
        """γ_n matches known value to 15 decimal places."""
        val = float(rf.gamma(n))
        expected = KNOWN_VALUES[n]
        assert abs(val - expected) / expected < 1e-14

    def test_precomputed_count(self):
        """All 15 zeros are precomputed."""
        assert len(GAMMA_PRECOMPUTED) == 15

    def test_monotone_increasing(self, rf):
        """Zeros are strictly increasing: γ_n < γ_{n+1}."""
        for n in range(1, 15):
            assert rf.gamma(n) < rf.gamma(n + 1)


class TestRegisterLookup:
    """Test register metadata lookup."""

    def test_gamma_1_foundational(self, rf):
        info = rf.lookup(1)
        assert info["frequency"] == 11
        assert info["gauge_distinguished"] is True

    def test_gamma_6_ew_workhorse(self, rf):
        info = rf.lookup(6)
        assert info["frequency"] == 6
        assert info["gauge_distinguished"] is True

    def test_gamma_8_su3_adjoint(self, rf):
        info = rf.lookup(8)
        assert info["frequency"] == 4
        assert info["gauge_distinguished"] is True

    def test_gauge_distinguished_set(self, rf):
        """Only {1, 4, 6, 8} are gauge-distinguished."""
        for n in range(1, 16):
            info = rf.lookup(n)
            if n in {1, 4, 6, 8}:
                assert info["gauge_distinguished"] is True
            else:
                assert info["gauge_distinguished"] is False
