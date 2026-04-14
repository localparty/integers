"""Zero Selection — the compiler's register allocation algorithm.

Maps observable metadata (sector, generation, color charge) to
specific Riemann zero registers γ_n.

Source: paper12/research/09-pattern-of-zero-indices.md
"""

from typing import List, Dict, Set, Optional

# Gauge-distinguished index set: the four SM gauge invariants
# These correspond to SM gauge group structure:
#   γ₁  = dim(adjoint U(1)) = 1 photon
#   γ₄  = 1+3 = EW unbroken generators
#   γ₆  = |Z₆| = order of SM center (Z₂ × Z₃)
#   γ₈  = dim(adjoint SU(3)) = 8 gluons
GAUGE_DISTINGUISHED = {1, 4, 6, 8}

# Sector → primary register mapping
SECTOR_REGISTERS = {
    "EM":          [1],
    "U(1)":        [1],
    "EW":          [2, 6],
    "Higgs":       [2, 6],
    "SU(2)":       [6],
    "strong":      [8],
    "SU(3)":       [8],
    "color":       [8],
    "cosmology":   [9, 10, 11],
    "BBN":         [13, 14],
    "neutrino":    [12, 15],
    "lepton":      [7],
}

# Generation → operation template
GENERATION_TEMPLATE = {
    3: "PRODUCT",      # Largest values: O(100 GeV)
    2: "RATIO",        # Intermediate: O(1-10 GeV)
    1: "DIFFERENCE",   # Smallest: O(1-10 MeV)
}

# Generation → register hints
GENERATION_REGISTERS = {
    3: [3],    # 3rd gen index
    2: [9],    # 2nd gen → flavor-cosmology hub
    1: [8, 9], # 1st gen → adjacent zero spacing
}

# Color charge → normalization
COLOR_NORMALIZATION = {
    "fundamental":  "1/(2pi)",     # S¹ circumference (KK color)
    "singlet":      "1",           # No S¹ integration
    "adjoint":      "1/pi",        # Half-period
    "2nd_gen":      "1/pi^2",      # S² angular volume
}


class ZeroSelector:
    """Register allocation: observable metadata → γ_n indices."""

    def select(self, metadata: dict) -> dict:
        """Select registers based on observable metadata.

        Args:
            metadata: dict with keys like 'sector', 'generation',
                      'color', 'order', 'type'.

        Returns:
            dict with 'registers', 'rule_hint', 'normalization'.
        """
        registers: List[int] = []
        rule_hint = None
        normalization = "1"

        sector = metadata.get("sector", "").lower()
        generation = metadata.get("generation")
        color = metadata.get("color", "singlet").lower()
        order = metadata.get("order", "").lower()

        # Step 1: Sector assignment
        for key, regs in SECTOR_REGISTERS.items():
            if key.lower() in sector:
                registers.extend(regs)
                break

        # Step 2: Generation assignment
        if generation in GENERATION_TEMPLATE:
            rule_hint = GENERATION_TEMPLATE[generation]
            gen_regs = GENERATION_REGISTERS.get(generation, [])
            registers.extend(gen_regs)

        # Step 3: Color charge → normalization
        if color in COLOR_NORMALIZATION:
            normalization = COLOR_NORMALIZATION[color]
        elif "color" in sector or "su(3)" in sector:
            normalization = "1/(2pi)"

        # Step 4: Order-based rule hint
        if not rule_hint:
            if "linear" in order:
                rule_hint = "SUM"
            elif "bilinear" in order or "quadratic" in order:
                if "fundamental" in color or "su(3)" in sector:
                    rule_hint = "YUKAWA_QUARK"
                else:
                    rule_hint = "YUKAWA_LEPTON"
            elif "exponential" in order:
                rule_hint = "EXPONENTIAL"
            elif "thermal" in order or "log" in order:
                rule_hint = "LOG"
            elif "fractional" in order:
                rule_hint = "FRACTIONAL"

        # Deduplicate while preserving order
        seen: Set[int] = set()
        unique_registers = []
        for r in registers:
            if r not in seen:
                seen.add(r)
                unique_registers.append(r)

        return {
            "registers": unique_registers,
            "rule_hint": rule_hint,
            "normalization": normalization,
            "gauge_distinguished_used": [r for r in unique_registers
                                          if r in GAUGE_DISTINGUISHED],
        }

    def explain(self, metadata: dict) -> str:
        """Human-readable explanation of register selection."""
        result = self.select(metadata)
        lines = [f"Register allocation for: {metadata}"]
        lines.append(f"  Registers: {['γ_' + str(r) for r in result['registers']]}")
        lines.append(f"  Rule hint: {result['rule_hint']}")
        lines.append(f"  Normalization: {result['normalization']}")
        if result['gauge_distinguished_used']:
            lines.append(f"  Gauge-distinguished: "
                         f"{['γ_' + str(r) for r in result['gauge_distinguished_used']]}")
        return "\n".join(lines)
