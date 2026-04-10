# A3.02: Bridge Triples

The four bridge triples (p, N, k):
- (2, 7, 2): ord_7(2) = 3, k = 6/3 = 2. CORRECT.
- (5, 13, 3): ord_13(5) = 4, k = 12/4 = 3. CORRECT.
- (3, 13, 4): ord_13(3) = 3, k = 12/3 = 4. CORRECT.
- (7, 19, 6): ord_19(7) = 3, k = 18/3 = 6. CORRECT.

Verification: 5^1=5, 5^2=25=12, 5^3=60=8, 5^4=40=1 (mod 13). So ord_13(5)=4. Check.
3^1=3, 3^2=9, 3^3=27=1 (mod 13). So ord_13(3)=3. Check.
7^1=7, 7^2=49=11, 7^3=77=1 (mod 19). So ord_19(7)=3. Check.

The values k in {2,3,4,6} are the crystallographic restriction (orders of elements in GL_2(Z)). The paper notes this connection (Remark 3.8).

**Verdict: CORRECT.** All Frobenius orders and bridge indices are arithmetically verified.
