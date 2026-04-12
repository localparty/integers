# W1-3 Author Prompt — Node 1.3: OA1 (Polymorphism → Outer Automorphism, via Kernel Analysis)

**Effort:** MAX

## Assignment

Attack **Theorem OA1**: For a Boolean constraint language L, polymorphisms of L lift to outer automorphisms of M_Bool^L. More precisely: construct a group homomorphism Φ: Clone(L) → Out(M_Bool^L) whose kernel is contained in the essentially unary operations.

## The REFRAME (Runner's inversion from cycle 0)

**Do NOT try to prove each polymorphism is individually outer.** Instead, prove the KERNEL of the lift Φ: Clone(L) → Out(M_Bool^L) is small (contained in essentially unary ops). If |Clone_k(L)| grows exponentially (UA1) and the kernel is at most 4k (essentially unary), then |Im(Φ)| grows exponentially → Out has continuous image → non-full by HOUDAYER-MARRAKCHI. This kernel approach is the inversion of the original per-element outerness problem.

## Context

**§C Bottleneck:** THIS IS THE BOTTLENECK. Everything else depends on this.

**§J Voice canon:** "we cannot crack it from the outside; the framework is transposable" / "from the inside out" / "One theorem. Two established fields."

**§D Toolkit rows you MUST know:**
- PATB-DIAGONAL: Taylor = fixes diagonal of M_Bool^Γ. The diagonal is the sub-algebra where all inputs agree. α_f ∘ E_diag = E_diag. This is your STRUCTURAL HANDLE for the lift.
- Q6-OUTDIM: exponential polymorphism dimension for P-time. The space is rich enough that the kernel can't absorb everything.
- HOUDAYER-MARRAKCHI: full ↔ spectral gap ↔ discrete Out.
- O7-HOLONOMY: polymorphism holonomy on constraint-graph cycles is trivial for P-time, non-trivial for NPC. The holonomy IS the Out image measured geometrically.
- A5-AREA-LAW: NPC holonomy follows area law with σ≈0.002. Geometric manifestation of spectral gap.
- SPECTRAL-GAP-DUALITY: solution-graph gap (P large, NPC small) is DUAL to modular gap. Two spectral gaps, opposite directions.
- A3-UNDERIVABILITY: P/NPC distinction invisible at bounded arity. Need k→∞.

**§F Kill list (HARD CONSTRAINTS):**
- K-3: Modular flow DOES NOT PRODUCE the polymorphism. OA controls existence, not identity. DO NOT claim σ_t generates f.
- K-1: Use Out(M), not H²(G).
- K-18: Winding number on Boolean domain is trivially zero — don't use it.
- K-16: SDW expansion meaningless on discrete graphs.
- K-17: Scalar thermodynamic observables don't separate — use algebraic structure.

## Strategy (three sub-approaches to try in order)

**Sub-approach A (kernel analysis):** Construct Φ: Clone_k(L) → Aut(M_Bool^L)/Inn(M_Bool^L). A k-ary polymorphism f acts on M_Bool^L by f-combining k copies of witness operators. Show: (1) this is an automorphism, (2) the map is a homomorphism, (3) the kernel consists only of essentially unary ops (which act trivially on M_Bool because they permute copies without mixing).

**Sub-approach B (diagonal-fixing):** By PATB-DIAGONAL, Taylor = fixes diagonal. A non-trivial Taylor polymorphism fixes E_diag but acts non-trivially on the off-diagonal. In a type III₁ factor, an automorphism that fixes a maximal abelian sub-algebra but acts non-trivially off-diagonal is outer (by Connes' χ(M) invariant or the asymptotic ratio set). This gives outerness for individual Taylor polymorphisms.

**Sub-approach C (holonomy-to-Out):** By O7-HOLONOMY, the polymorphism holonomy on constraint-graph cycles is exactly the geometric measurement of Out. Trivial holonomy = trivial Out contribution = inner. Non-trivial holonomy (NPC) = non-trivial Out. But for P-time: the holonomy is trivial AND the factor is non-full with continuous Out. So the continuous Out comes from the RICHNESS of trivial-holonomy operations (exponentially many), not from individual non-triviality. This connects Q6-OUTDIM to Out dimension.

## Known obstruction

The KST theorem (Kadison-Singer-type rigidity) was found by a prior Author: not every automorphism of a type III₁ factor is outer. Inner automorphisms exist and the inner automorphism group can be large. The kernel approach sidesteps this: we don't need EVERY automorphism to be outer, we need the kernel to be SMALL relative to the clone.

## Framework tools

Read `online-researcher-adversarial/ora-bundle-v7/05-framework-tools.md` for the full framework index. KEY files for this node:
- `paper28-pvnp/strategy/07-toolkit-complete.md` — the complete P vs NP toolkit (10 verified entries, 8+3 kills, trinity, Rule 9 v3)
- `paper28-pvnp/strategy/08-clone-growth-fullness-bridge.md` — the bridge theorem brief
- `paper28-pvnp/strategy/06-transposition-dictionary.md` — the full transposition dictionary
- `paper28-pvnp/preprint/sections-03-boolean-bc-system.md` — M_Bool construction
- `paper12/research/214-the-method-six-patterns.md` — the 6-step method loop
- `paper12/27-anchor-document.md` — operational stance
- `paper12/research/14-transposition-CCM-and-reasoning-patterns.md` — transposition mechanics
- `paper13-rh/preprint/sections-06-10.md` — RH chain (spectral template for how BC algebra works)
- `paper08-yang-mills/preprint/PROOF-CHAIN.md` — YM chain (rigor template)
- `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` — closure pattern template (single algebraic object bypasses wall)
- `paper28-pvnp/strategy/10-amplification-entries.md` — amplification results (A5, SPECTRAL-GAP-DUALITY, A3)

## Output

Write to `nodes/W1-3-OA1.md`. Execute the 6-step method loop at MAX effort. Report status. If BLOCKED, specify WHERE in the loop you got stuck. If BLOCKED-DECOMPOSED, name the sub-requirements.
