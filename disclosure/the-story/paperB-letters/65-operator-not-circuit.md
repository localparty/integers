# 65 — Operator-algebra engine, not a circuit simulator

**Speaker:** Claude (Opus 4.6, session fd7740d8).
**Date:** 2026-04-13, 19:31 UTC.
**Context:** G had asked about MCP + qubit simulator in Python + dashboard for the quantum compiler. Claude's response reframes the architecture.

> OK here's the calibration. The qubit simulator idea is NOT archaic — MCP is cutting-edge and there's literally a Quantum Simulator MCP server already published + Conductor Quantum's CODA MCP just launched for this exact pattern. But there's a subtlety about WHICH simulator backend is right:
>
> ---
>
> ## The key distinction: gate-based vs operator-algebraic
>
> **Qiskit/Cirq simulate quantum CIRCUITS** — gate sequences on qubits. They're optimized for NISQ hardware.
>
> **Your compiler doesn't produce circuits.** It produces OPERATOR-ALGEBRAIC expressions: matrix elements of L-hat, eigenvalues of R-hat, KMS state expectations, Hecke character actions. These are infinite-dimensional operator algebra computations, not finite gate sequences.
>
> Trying to map `m_t = kappa^2 <3|L-hat|3> <8|L-hat|8> / (2pi)` to qubit gates is like compiling Python to punch cards — technically possible but you're adding a translation layer that doesn't need to be there.
>
> **The right backend is an operator algebra engine, not a circuit simulator.**

Claude catches the technical stakes of G's idea. The memorable analogy: *compiling Python to punch cards.* Gate-based simulators are the wrong abstraction; the framework lives in operator algebra, not gate sequences.

One of the sharpest technical corrections in the archive. Saves the compiler from a wrong turn before the architecture calcifies.

*Next: [66-post-it-note-session.md](66-post-it-note-session.md).*
