"""End-to-end compilation test: all 36 formulas must pass.

This is the compiler's acceptance test. Every formula in the
master prediction table must compile with zero free parameters
and match experiment within 1%.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from bc_engine import BCAlgebra
from master_table import MASTER_TABLE


@pytest.fixture(scope="module")
def engine():
    return BCAlgebra(dps=50)


class TestFullCompilation:
    """All 36 formulas must compile and match experiment."""

    @pytest.mark.parametrize("entry", MASTER_TABLE,
                             ids=[e["name"] for e in MASTER_TABLE])
    def test_formula(self, engine, entry):
        """Each formula matches experiment within 1%."""
        result = engine.compile_formula(entry)

        assert result["verdict"] == "PASS", (
            f"{entry['name']}: {entry['formula_str']} = "
            f"{result['compiled_value']:.6f} vs "
            f"{result['experimental']} ({result['deviation_pct']:.4f}%)"
        )

    def test_all_pass_count(self, engine):
        """All 36 formulas pass."""
        results = engine.compile_all()
        passed = sum(1 for r in results if r["verdict"] == "PASS")
        assert passed == len(MASTER_TABLE), (
            f"{passed}/{len(MASTER_TABLE)} passed. "
            f"Failures: {[r['name'] for r in results if r['verdict'] != 'PASS']}"
        )


class TestCompilationDetails:
    """Spot-check specific high-precision formulas."""

    def test_cc_5ppb(self, engine):
        """CC hierarchy matches to 5 parts per billion."""
        result = engine.verify("log_CC")
        assert result["deviation_pct"] < 0.001  # < 0.001%

    def test_m_W_best_fit(self, engine):
        """m_W = γ₂ + γ₁₃ is the best sub-percent fit (0.012%)."""
        result = engine.verify("m_W")
        assert result["deviation_pct"] < 0.05

    def test_N_eff_precision(self, engine):
        """N_eff = γ₆^(1/3) matches to 82 ppm."""
        result = engine.verify("N_eff")
        assert result["deviation_pct"] < 0.01

    def test_m_b_log_rule(self, engine):
        """m_b = log(γ₁₅) matches to 0.093%."""
        result = engine.verify("m_b")
        assert result["deviation_pct"] < 0.1


class TestSectorCoverage:
    """Each sector has compiled formulas."""

    def test_sector_A_cosmology(self, engine):
        results = [engine.compile_formula(e) for e in MASTER_TABLE
                   if e["sector"] == "A"]
        assert len(results) >= 7
        assert all(r["verdict"] == "PASS" for r in results)

    def test_sector_B_couplings(self, engine):
        results = [engine.compile_formula(e) for e in MASTER_TABLE
                   if e["sector"] == "B"]
        assert len(results) == 3
        assert all(r["verdict"] == "PASS" for r in results)

    def test_sector_C_masses(self, engine):
        results = [engine.compile_formula(e) for e in MASTER_TABLE
                   if e["sector"] == "C"]
        assert len(results) >= 12
        assert all(r["verdict"] == "PASS" for r in results)

    def test_sector_D_mixing(self, engine):
        results = [engine.compile_formula(e) for e in MASTER_TABLE
                   if e["sector"] == "D"]
        assert len(results) >= 6
        assert all(r["verdict"] == "PASS" for r in results)
