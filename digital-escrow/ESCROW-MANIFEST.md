# Digital Escrow Manifest — Integers Programme

*Cryptographic identity + provenance commitment. Each `.bin` / `.part-*` file is GPG-encrypted with post-quantum-resistant keys (GPG-PQC). The SHA-256 hashes below are the public commitment: they prove these files existed at publication time without revealing their contents. If contention ever arises, the programme author publishes the decryption key(s) selectively — each logical file has its own key.*

*G Six. April 16, 2026.*

---

## Files (13 total, all < 100 MB for GitHub compatibility)

Files 01 and 05 are split into parts for GitHub's 100 MB per-file limit. Reconstruct before decryption.

### File 01 — split into 3 parts

```
cat .gpg-pqc-digital-escrow-01.part-aa \
    .gpg-pqc-digital-escrow-01.part-ab \
    .gpg-pqc-digital-escrow-01.part-ac > digital-escrow-01.bin
```

| Part | Size | SHA-256 (per-part) |
|---|---|---|
| `.gpg-pqc-digital-escrow-01.part-aa` | 90 MB | `3a6a282686fe0d8c185797f2cfa8b32865f0e730646109ec607696dd922d6a6f` |
| `.gpg-pqc-digital-escrow-01.part-ab` | 90 MB | `a3db1166c28080033e581c85a5d74be24204398606094ea007ed2d1f8efb60bf` |
| `.gpg-pqc-digital-escrow-01.part-ac` | 70 MB | `ebaadc336cc0f4299f4aadd660751346769809d730e9f492a2ce4a478443399b` |

**Reconstructed hash (the commitment):**
```
ee998b4a296781b6670be029aa8d118f50e3c0a7b1b38b7d6cb75bb481d475e2  digital-escrow-01.bin (250 MB)
```

### File 02 — single file (15 KB)

```
aa8201231a4d0bc70d297085ba9f76bfb3fe4d4e31e957d4de80e2bfbdd9c1b0  .gpg-pqc-digital-escrow-02.bin
```

### File 03 — single file (14 MB)

```
456caeeba8bf8d70dd3f93dda546edd142ce9f5234b057ab6272c1f7509799fc  .gpg-pqc-digital-escrow-03.bin
```

### File 05 — split into 4 parts

```
cat .gpg-pqc-digital-escrow-05.part-aa \
    .gpg-pqc-digital-escrow-05.part-ab \
    .gpg-pqc-digital-escrow-05.part-ac \
    .gpg-pqc-digital-escrow-05.part-ad > digital-escrow-05.bin
```

| Part | Size | SHA-256 (per-part) |
|---|---|---|
| `.gpg-pqc-digital-escrow-05.part-aa` | 90 MB | `67201e1979305341cf68fa36e2146689040e57015ca4107b4988ff50f706c3cf` |
| `.gpg-pqc-digital-escrow-05.part-ab` | 90 MB | `b9eaa0bc5f83a1725f096eae4e60598b2fa66301d23ad569e50bf114885a14cc` |
| `.gpg-pqc-digital-escrow-05.part-ac` | 90 MB | `a43c621e409104535695279c9ca4dccdc418e9fd0b18a675fecdbcbf14f28811` |
| `.gpg-pqc-digital-escrow-05.part-ad` | 87 MB | `5f0dbdb8b45d0d2ec0a5ecb65c2466d4608f3e6ce8c08242733df8c5a538e367` |

**Reconstructed hash (the commitment):**
```
22992453479f0623d15d3edbe6fe6808a2545deb05fe65ed5b0f8535a92d72ab  digital-escrow-05.bin (357 MB)
```

### Files 06–09 — single files

```
30e7bdbaf3c919515c41ca175ffb201b9b634bc2f670f82e9b351b9fd6f1d59c  .gpg-pqc-digital-escrow-06.bin (1.5 MB)
ee7f9d930726c325fb9e4577f2b37ab38f9a608609e5d5eec7f2569534877d05  .gpg-pqc-digital-escrow-07.bin (2.5 MB)
e89d138e57ce0ce931547d41b17d8306e080a8a090c696de0bd1d9ac5fbdb3fb  .gpg-pqc-digital-escrow-08.bin (2.7 MB)
d31f6dae1a528279df000714062be5aa12d60b0d2a9c49716a482272f2eddb02  .gpg-pqc-digital-escrow-09.bin (1.5 MB)
```

---

## What these files contain (disclosed at category level only)

| File | Category | Contents (sealed until key published) |
|---|---|---|
| 01 (3 parts) | Effort + collaboration record | Sealed |
| 02 | Identity + provenance | Sealed |
| 03 | Identity + provenance | Sealed |
| 05 (4 parts) | Effort + collaboration record | Sealed |
| 06 | Identity + provenance | Sealed |
| 07 | Identity + provenance | Sealed |
| 08 | Identity + provenance | Sealed |
| 09 | Identity + provenance | Sealed |

*Note: file 04 is intentionally absent from this manifest.*

---

## How to verify (for any third party)

### Verify a single-file escrow entry

```bash
shasum -a 256 .gpg-pqc-digital-escrow-02.bin
# Compare output to the hash in this manifest.
```

### Verify a split escrow entry

```bash
# Reconstruct
cat .gpg-pqc-digital-escrow-01.part-aa \
    .gpg-pqc-digital-escrow-01.part-ab \
    .gpg-pqc-digital-escrow-01.part-ac > digital-escrow-01.bin

# Verify
shasum -a 256 digital-escrow-01.bin
# Expected: ee998b4a296781b6670be029aa8d118f50e3c0a7b1b38b7d6cb75bb481d475e2
```

### If the programme author publishes a decryption key

```bash
# Reconstruct (if split)
cat .gpg-pqc-digital-escrow-NN.part-* > digital-escrow-NN.bin

# Decrypt
gpg --decrypt digital-escrow-NN.bin > decrypted-output
```

---

## Encryption standard

GPG with post-quantum-resistant cipher suite (PQC). Keys held exclusively by the programme author. Each logical file encrypted with a separate key — selective disclosure possible without all-or-nothing revelation.

## When to publish keys

Keys remain sealed unless:
1. **Authorship contention** — publish identity files (02, 03, 06–09)
2. **Effort contention** — publish effort files (01, 05)
3. **Legal/institutional requirement** — publish the relevant subset
4. **Never** — if no contention arises, the keys are never published; the hashes stand as proof the commitment existed

## Split rationale

Files 01 (250 MB) and 05 (357 MB) exceed GitHub's 100 MB per-file limit. They are split into ≤90 MB parts using `split -b 90m`. Reconstruction is `cat parts > original.bin` — verified by SHA-256 hash match against the commitment in this manifest.

---

*"The strongest proof of authorship is a commitment you made before anyone asked."*
