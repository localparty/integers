"""Test correspondence table lookups and linker resolution."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from correspondence import CorrespondenceLinker, BRIDGE_FAMILY, MINIMAL_CONDUCTOR


@pytest.fixture
def linker():
    return CorrespondenceLinker()


class TestCorrespondenceLookup:

    def test_m_t_spectral(self, linker):
        result = linker.check("m_t", "spectral")
        assert result["status"] == "FILLED"
        assert "L̂" in result["image"]

    def test_m_t_geometric(self, linker):
        result = linker.check("m_t", "geometric")
        assert result["status"] == "FILLED"

    def test_blank_cell(self, linker):
        result = linker.check("m_t", "information_theoretic")
        assert result["status"] == "BLANK"

    def test_unknown_observable(self, linker):
        result = linker.check("dark_matter_mass", "spectral")
        assert result["status"] == "BLANK"


class TestLinker:

    def test_m_t_linked(self, linker):
        result = linker.link("m_t")
        assert result["linked"] is True
        assert result["resolution_count"] >= 3

    def test_n_s_linked(self, linker):
        result = linker.link("n_s")
        assert result["linked"] is True

    def test_blank_cells_exist(self, linker):
        blanks = linker.find_blank_cells()
        assert len(blanks) > 0
        assert all(b["status"] in ("BLANK", "PARTIAL") for b in blanks)


class TestBridgeFamily:

    def test_four_brauer_classes(self):
        assert len(BRIDGE_FAMILY) == 4

    def test_minimal_conductor(self):
        assert MINIMAL_CONDUCTOR == 1729
        assert 7 * 13 * 19 == 1729

    def test_cabibbo_class(self):
        cab = BRIDGE_FAMILY[3]  # (7,19) class
        assert cab["p"] == 7
        assert cab["N"] == 19
        assert cab["k"] == 6
