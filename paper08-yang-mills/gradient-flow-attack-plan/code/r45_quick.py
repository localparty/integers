"""R45 quick: light probe at lam=300, 500, 700 with reduced settings.

Just one or two sigma values, smaller N_basis, to get data points.
"""
import json, os, sys, time
from math import log
import numpy as np

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)
from r45_large_lambda import measure_lambda

results = []
specs = [
    # (lam, Nb, sigma_factors, n_per_sigma, pad)
    (300.0, 700, (0.25, 0.28), 14, 3.5),
    (500.0, 700, (0.25, 0.28), 12, 3.0),
    (700.0, 700, (0.25,),       12, 3.0),
]

for lam, Nb, sf, nps, pad in specs:
    print(f"\n[quick] lam={lam} Nb={Nb}")
    t0 = time.time()
    try:
        res = measure_lambda(lam, Nb, sigma_factors=sf,
                             n_per_sigma=nps, pad_sigma=pad)
        res["wall"] = time.time() - t0
        results.append(res)
        # save incrementally
        with open(os.path.join(CODE, "r45_quick.json"), "w") as f:
            json.dump(results, f, indent=2, default=str)
    except Exception as e:
        print("ERROR:", e)
        results.append({"lam": lam, "Nb": Nb, "error": str(e)})

print("\nDONE")
