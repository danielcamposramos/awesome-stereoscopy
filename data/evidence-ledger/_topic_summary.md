# Federated Signal Ledger

This consumer registry points to canonical hardware claims in
`sony-bravia-linux` without copying their bodies.

- `federation.toml` indexes and hashes every local pointer.
- `pointers/` contains one immutable pointer per upstream claim.
- `docs/reference/evidence-ledger/pointers.md` is the generated human view.
- `.github/workflows/evidence-ledger.yml` verifies current upstream hashes and
  correction/supersession state through the producer's pinned reusable action.

The initial federation is intentionally limited to the normative HDMI Deep
Color field claim and the measured/observed run-34 3D-plus-12-bpc result.
