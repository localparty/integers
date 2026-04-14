# T7 Vertex 23: Sato-Tate — Type B, 6/10

**Action:** Deep construction pass on L4 (CONJECTURED). Checked Sub-route 5a (CM abelian varieties via Paper 26 ITPFI). Literature scan for 2024-2026 results. Date: 2026-04-14.

## L4 analysis: BC framing — CONJECTURED, no upgrade

The identification Frob_p = Hecke mu_p is standard (Ha-Paugam 2005; CCM 2005 endomotives). Paper 26 ITPFI (Node C, PROVED) gives omega_1^K = tensor_p omega_1^(p) as a C*-algebraic fact. IT3 check (CLOSED) confirms Hecke-character twist preserves the tensor product.

**What L4 actually establishes:** For CM curves over K with h_K=1, the BC partition function identity Z_{BC,K,psi}(beta) = L(beta, psi) is tautological (Node G Step C). The ITPFI factorization decomposes this into local Euler factors. This IS the local-global structure that ST equidistribution exploits.

**Where L4 stops:** The claim "spectral measure of Hecke action is Haar" RESTATES ST equidistribution in BC language but does not DERIVE it from BC axioms. The BC algebra gives the Euler product; equidistribution is the statement that partial products converge to the Haar pushforward. The convergence is the content of Hecke 1920 (CM) / Taylor et al. 2011 (non-CM), not a BC consequence. **L4 is a dictionary entry, not a theorem.** No upgrade.

## Sub-route 5a: CM abelian varieties — BLOCKED at rank > 1

Paper 26 infrastructure handles GL_1 objects (rank-1 Grossencharacters). CM abelian varieties of dimension g have CM type of rank g; the Mumford-Tate group is a torus of rank g inside USp(2g), not U(1). The ITPFI factorization would need rank-g local factors, which are not constructed in the literature. The h_K=1 condition ensures unique KMS_1 for rank 1; for rank g the state space is larger and uniqueness fails in general. **5a does not close for g > 1 with current tools.**

## Literature 2024-2026: no closing material found

- **Gaitsgory-Raskin 2024:** Geometric Langlands PROVED for function fields. ST for function fields already follows from Deligne equidistribution. Transfer to number fields is the actual wall; GR does not address it.
- **Effective ST bounds (Fit-Florea-Rouse-Shin 2020):** Effective for abelian surfaces, not full equidistribution for general motives. Already cited in chain.
- **CCM 2025 (arXiv:2511.22755):** Strictly over Q. No imaginary-quadratic extension, no Grossencharacter, no rank-g CM types. Does not help 5a.
- **Sagnier 2017-2019:** Adelic arithmetic site for h_K=1 fields. No BC-type operator, no spectral triple, no Weil quadratic form. Useful as target, not as tool.

## Edges

- **Lehmer -> Sato-Tate: PARTIAL.** Same e-circle; Lehmer (topology/what lives on it) constrains Sato-Tate (measure/how it distributes). CM-curve Mahler measures connect via L'(E,1). Genuine but one-directional.
- **Sato-Tate -> Schanuel: SPECULATIVE.** Equidistribution of Frobenius angles could constrain algebraic relations among L-values at s=1, feeding Schanuel. No mechanism constructed; the spaces (U(1) angles vs transcendence degree) are far apart.

## Verdict

**Confidence: 6/10 — unchanged.** L4 is an honest dictionary entry (Frob = Hecke eigenvalue, ST = Haar spectral measure) but not a theorem. Sub-route 5a is blocked at rank > 1. The two PROVED links (L2: non-CM, L3: CM) are solid literature. The wall (L5: generalized motivic ST) remains open and is not materially closer after this pass. No overclaim found; no upgrade available.
