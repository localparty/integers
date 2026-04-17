# Canonical PROOF-CHAIN Directory

*The single source of truth for every vertex's live PROOF-CHAIN.md in the programme. Centralized 2026-04-15 per `strategy/self-healing-log.md` Intervention 2 (Option A).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Role

Every vertex in the ring has ONE live PROOF-CHAIN.md. It lives here:

```
strategy/proof-chain/<vertex>/PROOF-CHAIN.md
```

**This directory is the live, editable source.** The Proof-Chain Adversarial (PAC) operator, Universal Approval bundles, self-healing scans, x-ray builders, decomposition ring, CCM-verification ring, and every PROSE/PREPRINT composition-backward cycle read from (and write to) this single location.

Paper directories (`paper01/`, `solutions-with-prize/paper08-yang-mills/`, `solutions-with-prize/paper13-rh/`, ...) hold their body files (preprints, notes, supplementary LaTeX, `preprint/` bundles) but NO LONGER carry the live PROOF-CHAIN. Each paper dir has a small `PROOF-CHAIN-MOVED.md` stub pointing here.

## Why centralized

PROOF-CHAIN.md files are **core programme artifacts**, not paper-specific:

1. **Every PAC sub-agent** reads them. Having to map paper-dir paths (`solutions-with-prize/paper26-bsd/`) ↔ vertex names (`bsd`) costs every dispatch template a lookup.
2. **PROSE / PREPRINT composition-backward cycles** pull from PROOF-CHAINs. Walking `paper*/` to find them is backward.
3. **Self-healing scans** look for PROOF-CHAIN.md drift. One canonical path = one scan target.
4. **Visualization builders** pull PROOF-CHAIN statuses. Single location = simpler build.
5. **The ring traversal** (`strategy/the-ring.md`) operates on 25 vertices. The canonical location IS the ring's home.

## Canonical vertex → paper mapping

The 25-vertex ring (per `strategy/decomposition/README.md`):

| Vertex | Canonical path | Paper source (historical) |
|---|---|---|
| qg5d | `strategy/proof-chain/qg5d/PROOF-CHAIN.md` | `integers/paper01-qg5d/` |
| rh | `strategy/proof-chain/rh/PROOF-CHAIN.md` | `solutions-with-prize/paper13-rh/` |
| grh | `strategy/proof-chain/grh/PROOF-CHAIN.md` | `solutions/paper13b-grh/` |
| lindelof | `strategy/proof-chain/lindelof/PROOF-CHAIN.md` | `solutions/paper45-lindelof/` |
| bsd | `strategy/proof-chain/bsd/PROOF-CHAIN.md` | `solutions-with-prize/paper26-bsd/` |
| h12 | `strategy/proof-chain/h12/PROOF-CHAIN.md` | `solutions/paper25-hilbert-12/` |
| ym | `strategy/proof-chain/ym/PROOF-CHAIN.md` | `solutions-with-prize/paper08-yang-mills/` |
| ns | `strategy/proof-chain/ns/PROOF-CHAIN.md` | `solutions-with-prize/paper30-navier-stokes/` |
| turbulence | `strategy/proof-chain/turbulence/PROOF-CHAIN.md` | `solutions/paper38-turbulence/` |
| hodge | `strategy/proof-chain/hodge/PROOF-CHAIN.md` | `solutions-with-prize/paper29-hodge/` |
| baum-connes | `strategy/proof-chain/baum-connes/PROOF-CHAIN.md` | `solutions/paper31-baum-connes/` |
| pvnp | `strategy/proof-chain/pvnp/PROOF-CHAIN.md` | `solutions-with-prize/paper28-pvnp/` |
| vp-vs-vnp | `strategy/proof-chain/vp-vs-vnp/PROOF-CHAIN.md` | `solutions/paper39-vp-vs-vnp/` |
| bgs | `strategy/proof-chain/bgs/PROOF-CHAIN.md` | `solutions/paper32-bgs-spectral-statistics/` |
| katz-sarnak | `strategy/proof-chain/katz-sarnak/PROOF-CHAIN.md` | `solutions/paper46-katz-sarnak/` |
| twin-primes | `strategy/proof-chain/twin-primes/PROOF-CHAIN.md` | `solutions/paper34-twin-primes/` |
| cramer | `strategy/proof-chain/cramer/PROOF-CHAIN.md` | `solutions/paper43-cramer/` |
| goldbach | `strategy/proof-chain/goldbach/PROOF-CHAIN.md` | `solutions-with-prize/paper33-goldbach/` |
| abc | `strategy/proof-chain/abc/PROOF-CHAIN.md` | `solutions/paper37-abc/` |
| opn | `strategy/proof-chain/opn/PROOF-CHAIN.md` | `solutions/paper40-odd-perfect/` |
| collatz | `strategy/proof-chain/collatz/PROOF-CHAIN.md` | `solutions-with-prize/paper41-collatz/` |
| lehmer | `strategy/proof-chain/lehmer/PROOF-CHAIN.md` | `solutions/paper42-lehmer/` |
| sato-tate | `strategy/proof-chain/sato-tate/PROOF-CHAIN.md` | `solutions/paper44-sato-tate/` |
| schanuel | `strategy/proof-chain/schanuel/PROOF-CHAIN.md` | `solutions/paper35-schanuel/` |
| hilbert-6 | `strategy/proof-chain/hilbert-6/PROOF-CHAIN.md` | `solutions/paper36-hilbert-6/` |

### Additional (programme-internal bypass vertices, added during migration)

| Vertex | Canonical path | Paper source |
|---|---|---|
| ccm-replacement | `strategy/proof-chain/ccm-replacement/PROOF-CHAIN.md` | `paper49-ccm-replacement/` |
| h4-replacement | `strategy/proof-chain/h4-replacement/PROOF-CHAIN.md` | `paper50-h4-replacement/` |

These are not ring vertices in the original 25-row sense — they are programme-internal bypasses that replace external dependencies (CCM 2025 arXiv:2511.22755; the Yang-Mills H4 hypothesis). They share the PROOF-CHAIN.md form and are managed under the same canonical discipline.

## Publication snapshot discipline

At Zenodo / arXiv / journal release time, the canonical `strategy/proof-chain/<vertex>/PROOF-CHAIN.md` is **copied** into the corresponding paper dir (e.g., `solutions-with-prize/paper26-bsd/`) as a frozen publication snapshot named exactly `PROOF-CHAIN.md`. This snapshot:

- Is the version that ships with the paper
- Is NOT edited after release (immutable per the release's Zenodo DOI)
- May be updated at SUBSEQUENT releases (each release produces its own snapshot copy)

The canonical file under `strategy/proof-chain/` continues to evolve between releases as the programme matures.

### Distinguishing sibling bundles

The following are NOT the canonical live PROOF-CHAINs — they are sibling bundle artifacts with their own purposes:

- `strategy/decomposition/proof-chain/<name>/PROOF-CHAIN.md` — parallel decomposition ring (25 copies under active recursive decomposition per `strategy/decomposition/README.md`)
- `strategy/x-ray/proof-chain/<name>/X-RAY.md` — x-ray annotations (DIFFERENT file name: `X-RAY.md`, not `PROOF-CHAIN.md`)
- `strategy/ccm-verification/...` — CCM-specific hardening artifacts
- `paper*/preprint/PROOF-CHAIN.md` — referee-facing preprint-bundle snapshots (remain in preprint subdirs; NOT the live source)

The canonical live source is EXCLUSIVELY `strategy/proof-chain/<vertex>/PROOF-CHAIN.md`.

## Update discipline

Edits to the live PROOF-CHAIN flow through the PAC (see `online-researcher-adversarial/ora-bundle-v8/07-proof-chain-adversarial.md`). Manual edits should:

1. Leave a dated annotation (comment or strike-through) when migrating labels — non-destructive discipline per `strategy/self-healing-log.md`
2. Commit with a clear message referencing the vertex
3. If the change affects more than one vertex, commit as one change across all affected files

## Migration record

This directory was populated on 2026-04-15 by one-time `git mv` operations from the 27 paper-dir PROOF-CHAIN.md files. See `strategy/self-healing-log.md` entry "2026-04-15 — Intervention 2: PROOF-CHAIN.md centralization (Option A)" for the full migration record.

---

*Single source of truth. 27 canonical files. Every sub-agent reads one location. Paper dirs hold the paper; strategy holds the proof.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
