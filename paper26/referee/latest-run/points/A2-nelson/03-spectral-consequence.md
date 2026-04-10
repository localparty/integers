## Point A2(c): The Spectral Consequence

**The question:**
Self-adjointness implies real spectrum: spec(T_{BC,K}) subset R. This is the starting point for the bridge argument. Verify the logical chain.

**Finding:**
Essential self-adjointness of T_{BC,K} means its closure T-bar_{BC,K} is a self-adjoint operator. By the spectral theorem for self-adjoint operators, the spectrum of T-bar_{BC,K} is contained in R.

The bridge argument then proceeds: if a zero of zeta_K(s) at s = 1/2 + delta + it corresponds to an eigenvalue t of T-bar_{BC,K}, then t is real (guaranteed by self-adjointness), and the cocycle shift Delta c(delta) must satisfy integrality constraints. The key point is that self-adjointness constrains the spectrum to be real, which means any eigenvalue corresponding to a zero must satisfy the bridge integrality conditions at delta (the off-line displacement).

The logical chain is: Nelson -> essential self-adjointness -> closure is self-adjoint -> spectrum is real -> eigenvalues satisfy integrality constraints -> Baker forces delta = 0.

This chain is logically sound, with one important caveat addressed in Point A3: the Meyer spectral inclusion must actually embed zeros of zeta_K(s) as eigenvalues of T_{BC,K}. The Nelson step itself is correct.

**Verdict for this sub-question:**
SOUND -- The spectral consequence follows from the standard spectral theorem for self-adjoint operators. The logical chain from Nelson to real spectrum is correct.
