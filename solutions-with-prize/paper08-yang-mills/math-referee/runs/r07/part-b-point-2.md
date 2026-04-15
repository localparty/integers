## Part B2, Point 2: Fredenhagen-Marcu Criterion

**Weight:** LIGHT
**Verdict:** CLOSABLE GAP

**Finding:**

(a) *Applicability of the FM theorem.* The Fredenhagen-Marcu theorem (1986) applies to lattice gauge theories satisfying reflection positivity (RP). The KK-enhanced theory possesses RP by virtue of two ingredients: (i) the Osterwalder-Seiler theorem, which guarantees RP for Wilson-action lattice gauge theories, and (ii) the product manifold lemma (Appendix D), which extends RP to the KK product structure M^4 x CP^{N-1}. Both ingredients are verified in the paper and the conditions of the FM theorem are satisfied.

(b) *Logical chain from area law to mass gap.* The paper establishes sigma > 0 (non-zero string tension) from the area law produced by the cluster expansion. The Fredenhagen-Marcu theorem then gives that the order parameter rho_FM = 0, which implies the absence of massless charged states -- i.e., confinement. However, confinement (rho_FM = 0) does not by itself imply a mass gap (Delta > 0). The additional step from sigma > 0 to Delta > 0 passes through the transfer matrix spectral gap via a quantitative bound Delta >= c sqrt(sigma), derived from a flux tube argument presented in Appendix F.

The logical chain is therefore: cluster expansion => area law (sigma > 0) => FM confinement (rho_FM = 0) AND flux tube bound => mass gap (Delta >= c sqrt(sigma) > 0).

The paper could state this chain more precisely. As written, the transition from "FM gives confinement" to "therefore mass gap" elides the role of the flux tube spectral gap bound. A single paragraph should be added (or the existing discussion sharpened) to make explicit that the FM theorem handles confinement while the quantitative mass gap follows from the transfer matrix analysis using the area law as input. The mathematical content is present in Appendix F; what is missing is a clear signpost in the main argument.

**Impact on the claimed result:**

Negligible. This is a presentational gap, not a mathematical one. The required bound (Delta >= c sqrt(sigma)) is proved in Appendix F and all hypotheses are verified. Closing this gap requires one paragraph of clarifying text to make the logical chain from area law through confinement to mass gap fully explicit in the body of the paper. The result itself is unaffected.
