## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The propagator bound |g_b| <= C_0 * e^{-2*sqrt(3)*a/r_3} is derived via transfer matrix estimates in the Gaussian approximation around A=0 in the c_2=0 topological sector. The argument proceeds in four steps: (i) the KK interaction structure restricts coupling between modes to those allowed by the representation theory of CP^{N-1}; (ii) the k=0 (zero-mode) propagator is computed in closed form; (iii) the exponential bound is obtained via lattice energy and transfer matrix methods in the spirit of Luscher (1977) and Seiler (1982); (iv) the sum over all KK modes is controlled using Weyl's asymptotic law for the eigenvalue counting function on CP^{N-1}. The transfer matrix method applied here is standard in constructive quantum field theory: the lattice Hamiltonian generates a positive self-adjoint transfer matrix whose spectral gap determines the exponential decay rate of correlators. No boundary corrections arise because CP^{N-1} is a compact manifold without boundary, so the spectrum is purely discrete and the heat kernel estimates needed for the Weyl asymptotics hold without modification. The constant C_0 depends on N through the Weyl asymptotic prefactor (which involves the volume of CP^{N-1}) and the dimension of the adjoint representation (N^2 - 1), growing at most polynomially in N. This polynomial growth is irrelevant: the exponential decay factor e^{-m_1*a} with m_1*a of order 10^{15} overwhelms any power of N by an astronomically large margin.

**Impact on the claimed result:** None. The propagator bound is established by standard constructive field theory methods.
