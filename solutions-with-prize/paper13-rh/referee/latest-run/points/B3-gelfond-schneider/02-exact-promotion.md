# B3.02: Exact Promotion (First-Order to Full Formula)

**The concern:** Does the Gelfond-Schneider argument work for the EXACT formula, not just the first-order approximation?

**Assessment:** The exact formula Delta_c(delta) = (1 - p^{-2*delta})/(p - p^{-2*delta}) = n/k requires p^{-2*delta} = (np - k)/(n - k). This is an explicit algebraic equation. Taking logarithms gives -2*delta*log(p) = log((np-k)/(n-k)), where the RHS is the log of a rational number (for integer n). Cross-bridge comparison then gives:

delta = -log(r_1)/(2 log p_1) = -log(r_2)/(2 log p_2)

This is the exact formula, not an approximation. The Gelfond-Schneider argument applies to the exact expressions.

**Verdict: CORRECT.** The promotion from first-order to exact is not needed because the argument works directly with the exact formula.
