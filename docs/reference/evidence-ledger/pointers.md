# Federated Signal Ledger pointers

Generated from local pointer files and live upstream append-only ledgers. Do not edit this view.
Pointer digest: `1b96846e9d5d4c2fa8e3500ce1a235217aa60f3f06e745eed8e73421125e3bc0`.

| Pointer | Upstream claim | State | Purpose |
|---|---|---|---|
| `AS-SBL-3D-0001` | [SBL-3D-0001](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/data/evidence-ledger/claims/sbl-3d-0001.toml) | supported / SUPPORTED | Bind the run-34 22-step DRM/KMS matrix spanning RGB/YCbCr, deep colour and stereoscopic output modes. |
| `AS-SBL-3D-0002` | [SBL-3D-0002](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/data/evidence-ledger/claims/sbl-3d-0002.toml) | supported / SUPPORTED | Bind Daniel's observation that every accepted run-34 mode displayed, including 3D at 12 bpc. |
| `AS-SBL-DC-0001` | [SBL-DC-0001](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/data/evidence-ledger/claims/sbl-dc-0001.toml) | supported / SUPPORTED | Ground the HDMI General Control Packet Deep Color fields used by the combined 3D-plus-12-bpc result. |

Pointers bind the canonical semantic hash of each upstream claim; they do not copy its body.
A changed hash, missing claim, unexpected authority state, or disallowed correction/supersession fails CI.
