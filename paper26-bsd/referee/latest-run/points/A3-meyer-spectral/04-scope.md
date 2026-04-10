## Point A3(d): Scope of Spectral Inclusion

**The question:**
Does the inclusion capture ALL non-trivial zeros, or only those in a specific region? Are there zeros that could escape the spectral framework?

**Finding:**
The Meyer spectral inclusion, as presented, claims to capture all non-trivial zeros of zeta_K(s). The distributional eigenstate construction uses the explicit formula, which sums over ALL non-trivial zeros. There is no restriction to a specific region of the critical strip.

The concern about "escaping zeros" is addressed by the dark-state impossibility (Section 6): every eigenstate couples to every bridge cocycle. This means there are no "dark" eigenstates that the bridge family fails to detect.

However, there is a logical subtlety: the Meyer construction produces distributional eigenstates for zeros on the critical line. For hypothetical off-line zeros (which are the ones we want to rule out), the construction still works -- the explicit formula includes all zeros regardless of their real part. The off-line zeros would produce eigenvalues in the distributional sense, and the Nelson upgrade to genuine eigenstates forces these eigenvalues to be real (since T_{BC,K} is self-adjoint). The bridge then constrains delta = 0.

The argument is: assume a zero exists at s = 1/2 + delta + it. Meyer produces a distributional eigenstate. Nelson makes T self-adjoint, so the spectrum is real (the eigenvalue t is real). The bridge cocycle at this eigenstate has shift Delta c(delta). The integrality constraint + Baker forces delta = 0.

This logical structure is sound: we are not assuming GRH a priori; we are deriving it by contradiction from the spectral framework.

**Verdict for this sub-question:**
SOUND -- The spectral inclusion captures all non-trivial zeros. The dark-state impossibility ensures no zero escapes detection. The logical structure (proof by contradiction on delta != 0) is correct.
