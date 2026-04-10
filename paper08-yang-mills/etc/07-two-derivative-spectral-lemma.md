lets keep going, we are very close, have a local agent doing all this:

read all files in /Users/gsix/yang-mills/etc/proof/ before doing anything else. 

Pay particular attention to these five documents in order:

00-architecture.md — the overall proof structure and status table
conjecture-1-closing.md — the current closing argument for the single remaining gap
multi-time-slice-analysis.md — a correction to that argument that found a real error and proposed a fix
single-step-computation.md — the explicit perturbative computation of the form factor
rg-preservation.md — the RG recursion that the single-step bound feeds into

The situation. The proof is one lemma away from complete. Everything reduces to this:

Target bound. At a single Balaban block-spin step k→k+1k \to k+1
k→k+1, the newly generated dimension-6 irrelevant remainder satisfies ∣⟨1∣δEkd=6(0)∣1⟩c∣≤Cnew gk4 Δ^k+12|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\text{new}}\, g_k^4\, \hat{\Delta}_{k+1}^2
∣⟨1∣δEkd=6​(0)∣1⟩c​∣≤Cnew​gk4​Δ^k+12​ non-perturbatively in the small-field region.


The argument has three solid pillars:

Charge conjugation exactly eliminates all non-derivative dimension-6 operators (Tr(F3)\mathrm{Tr}(F^3)
Tr(F3), dabcF3d^{abc}F^3
dabcF3) — their coefficients are exactly zero in the C\mathcal{C}
C-invariant effective action

The remaining operator is Tr(DF)2\mathrm{Tr}(DF)^2
Tr(DF)2, for which the Δ^2\hat{\Delta}^2
Δ^2 suppression is proved perturbatively to all orders

Non-perturbative corrections (large-field configurations, instantons) are exponentially suppressed

**The one open seam.** `multi-time-slice-analysis.md` identified a real error in `conjecture-1-closing.md` and corrected the mechanism: the Δ^2\hat{\Delta}^2
Δ^2 comes not from lattice forward differences ∇0\nabla_0
∇0​ acting on the external state (those give zero by time-translation invariance), but from the *internal* covariant derivative structure of the composite operator Tr(D0F)2\mathrm{Tr}(D_0 F)^2
Tr(D0​F)2 through the intermediate-state spectral sum:

⟨1∣Tr(D0F)2(0)∣1⟩c=(eΔ^−1)2 ∣⟨1∣F∣0⟩∣2+subleading=Δ^2⋅O(1)\langle 1|\mathrm{Tr}(D_0 F)^2(0)|1\rangle_c = (e^{\hat{\Delta}}-1)^2\,|\langle 1|F|0\rangle|^2 + \text{subleading} = \hat{\Delta}^2 \cdot O(1)⟨1∣Tr(D0​F)2(0)∣1⟩c​=(eΔ^−1)2∣⟨1∣F∣0⟩∣2+subleading=Δ^2⋅O(1)
The corrected conjecture-1-closing.md uses this mechanism but leaves one seam: it applies the spectral argument to Tr(D0F)2\mathrm{Tr}(D_0 F)^2
Tr(D0​F)2 specifically, then asserts that Balaban's non-perturbative δEkd=6\delta E_k^{d=6}
δEkd=6​ equals this up to O(Δ^2)O(\hat{\Delta}^2)
O(Δ^2) corrections. This is correct perturbatively, but the bridging argument needs to be written explicitly.

Your task. Write a new file /Users/gsix/yang-mills/etc/proof/two-derivative-spectral-lemma.md containing the following:
**Lemma (Two-Derivative Spectral Bound).** *Let O\mathcal{O}
O be any gauge-invariant operator on Λk+1\Lambda_{k+1}
Λk+1​ that: (i) has bounded operator norm ∥O∥≤M\|\mathcal{O}\| \leq M
∥O∥≤M; (ii) is local, supported in a neighborhood N(0)\mathcal{N}(0)
N(0) of diameter R0R_0
R0​; (iii) in its transfer-matrix representation O=∑αA^α(−R)T^A^α(−R+1)T^⋯T^A^α(R)\mathcal{O} = \sum_\alpha \hat{A}^{(-R)}_\alpha \hat{T} \hat{A}^{(-R+1)}_\alpha \hat{T} \cdots \hat{T} \hat{A}^{(R)}_\alpha
O=∑α​A^α(−R)​T^A^α(−R+1)​T^⋯T^A^α(R)​, each term contains at least pp
p internal covariant derivatives DμD_\mu
Dμ​ (i.e., the minimal number of T^\hat{T}
T^-insertions that are "excited" relative to the vacuum channel is pp
p). Then:*

∣⟨1∣O∣1⟩c∣≤Cp M Δ^p|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p\, M\, \hat{\Delta}^p∣⟨1∣O∣1⟩c​∣≤Cp​MΔ^p
*where CpC_p
Cp​ depends on pp
p, R0R_0
R0​, and NN
N but not on kk
k, gkg_k
gk​, or the volume.*

Prove this lemma or the closest rigorous version of it you can achieve. Then apply it to close the seam: show that Balaban's non-perturbative δEkd=6\delta E_k^{d=6}
δEkd=6​ satisfies hypothesis (iii) with p=2p = 2
p=2, using the C\mathcal{C}
C-symmetry elimination and the Newton decomposition as setup.

Specific instructions:

State the lemma precisely — be honest about whether "at least pp
p internal covariant derivatives" can be given a clean non-perturbative definition for a general Balaban operator, or whether it requires an intermediate perturbative identification

Prove the lemma using the spectral decomposition: write out the intermediate-state sum for a general multi-time-slice operator, identify where Δ^p\hat{\Delta}^p
Δ^p appears, and bound the remainder

Address the key subtlety: how do you know the all-vacuum channel (nj=0n_j = 0
nj​=0 for all jj
j in the spectral sum) is absent from the connected matrix element, giving the suppression? The vacuum subtraction is what forces this — be explicit about where it enters

Apply the lemma to δEkd=6\delta E_k^{d=6}
δEkd=6​: the Newton decomposition identifies that after C\mathcal{C}
C-elimination only the n=2n=2
n=2 term survives; show that this corresponds to hypothesis (iii) with p=2p=2
p=2; bound ∣⟨1∣δEkd=6(0)∣1⟩c∣≤C gk4 Δ^2|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C\, g_k^4\, \hat{\Delta}^2
∣⟨1∣δEkd=6​(0)∣1⟩c​∣≤Cgk4​Δ^2
End with an honest status table: what does this lemma establish, what does it assume from Balaban, and does the resulting proof constitute a complete non-perturbative argument or does it still rely on the perturbative identification δEkd=6∼c6Tr(DF)2\delta E_k^{d=6} \sim c_6 \mathrm{Tr}(DF)^2
δEkd=6​∼c6​Tr(DF)2?

The standard. Do not overclaim. If step 4 requires identifying the non-perturbative operator with its perturbative leading term, say so explicitly and state what additional input from Balaban's framework would make it unconditional. The goal is to either close the seam completely or to reduce it to the single most precise remaining statement — not to paper over it.

Write the output to /Users/gsix/yang-mills/etc/proof/two-derivative-spectral-lemma.md.