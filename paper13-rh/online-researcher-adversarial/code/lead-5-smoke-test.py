"""Smoke test for lead-5 fixed script — golden-reference check only."""
import sys
sys.path.insert(0, "/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/online-researcher-adversarial/code")
import importlib.util
spec = importlib.util.spec_from_file_location(
    "lead5", "/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/online-researcher-adversarial/code/lead-5-verify-ccm-convergence.py"
)
mod = importlib.util.module_from_spec(spec)
# Don't execute __main__, just load functions
import mpmath
mpmath.mp.dps = 200

# Inline the golden check to avoid running the full __main__
from mpmath import mpf, log, exp, pi, euler, cos, sin, quad

def alpha_L(n, L):
    if n == 0: return mpf(0)
    L = mpf(L); n = mpf(n)
    rho = lambda x: exp(x/2)/(exp(x)-exp(-x))
    f = lambda x: sin(2*pi*n*x/L)*rho(x)
    return quad(f,[0,L])/pi

def beta_L(n, L):
    L = mpf(L); n = mpf(n)
    rho = lambda x: exp(x/2)/(exp(x)-exp(-x))
    f = lambda x: x*cos(2*pi*n*x/L)*rho(x)
    return quad(f,[0,L])/L

def gamma_L_fixed(n, L):
    L = mpf(L); n = mpf(n)
    rho = lambda x: exp(x/2)/(exp(x)-exp(-x))
    integrand = lambda x: (cos(2*pi*n*x/L) - exp(-x/2))*rho(x)
    val = quad(integrand,[0,L])
    wL = (mpf(1)/2)*(euler + log(4*pi)) - (mpf(1)/2)*log((exp(L)+1)/(exp(L)-1))
    return val + wL

def WR_diag_from_eq44(n, L):
    L = mpf(L); n = mpf(n)
    const = euler + log(4*pi*(exp(L)-1)/(exp(L)+1))
    integrand = lambda x: (exp(x/2)*2*(1-x/L)*cos(2*pi*n*x/L)-2)/(exp(x)-exp(-x))
    return const + quad(integrand,[0,L])

print(f"mp.dps={mpmath.mp.dps}")
L = 2*log(mpf(4))
print(f"L=2 log 4 = {mpmath.nstr(L, 20)}")
for n in range(4):
    cf = 2*gamma_L_fixed(n,L) - 2*beta_L(n,L)
    dv = WR_diag_from_eq44(n,L)
    print(f"n={n}: closed={mpmath.nstr(cf,20)}  direct={mpmath.nstr(dv,20)}  diff={mpmath.nstr(abs(cf-dv),5)}")
