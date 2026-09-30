# Studio regeneration prompt for spatial displays

Use this after importing the reviewed inputs and accepted primary sources.
Select relevant source lanes for each artifact rather than compressing the
entire notebook into every output.

---

Create a replacement educational artifact for “Spatial Computing, Stereoscopic
Optics & VR Systems Reference”, curated by Daniel Campos Ramos / EchoSystems
AI Studios. Disclose generation with Google NotebookLM and identify this as a
reviewed replacement, not a scientific experiment or solely human-authored work.
Use the imported corrections and primary references; do not cite superseded
generated artifacts as evidence. Include a bibliography/reading list with
edition/page/section references for key claims. If a source is unavailable or
contradictory, omit the precise claim or explicitly identify the open question.

Apply these constraints to text, narration, tables and images equally:

- Spell Panum, horopter, vergence and varifocal correctly.
- A near-eye panel's physical distance is not its optical focal distance.
  Label the latter when explaining accommodation. Separate VAC from motion
  conflict, crosstalk and latency; no universal comfort threshold or guaranteed cure.
- Distinguish row-interleaved FPR panels from passive cinema projection and
  spatially multiplexed multiview systems from time-multiplexed directional designs.
  State how per-eye resolution and brightness are measured.
- Light-field, multifocal, varifocal and holographic systems are different
  architectures. Do not promise correct accommodation from two rays alone.
- Present conventional half-mirror throughput limits only with their idealized
  polarization assumptions. Separate ideal, measured and projected Faraday
  performance. Do not print the exported 71.5/76.3/93.2% values until the primary
  paper's exact conditions have been independently accepted. Not all lost
  throughput becomes local heat. Optical efficiency does not itself solve VAC.
- For Faraday's simplified double-pass illustration, define θ = V(λ)BL:
  B is magnetic flux density and θ is rotation angle. A 45° rotation adds to
  90° on the idealized double pass. Use verified coordinate conventions for
  Jones matrices; never turn malformed source equations into confident graphics.
- HDMI structure codes: frame packing 0; field alternative 1; line alternative
  2; SBS-full 3; L+depth 4; L+depth+graphics+graphics-depth 5; TaB 6; SBS-half 8.
  These are not H.264 SEI enum values or DRM's encoded flags. Show readable labels.
- HDMI layouts do not dictate the sink's internal display architecture.
  Codec representation, container metadata, link timing and optical presentation
  must be separate labelled layers. st3d's uint8 field describes layout, not bpc.
- Keep norms, implementation behaviour and named-hardware results separate.
  IDR-related auto-engagement on our tested BRAVIAs is an observation, not a
  universal decoder-persistence rule. Cite the latest ledger for physical tests.
- Separate RGB/YCbCr, chroma subsampling, colour range, sample depth, HDR transfer
  function and panel depth. HDR does not mean 16-bpc transport. Do not invent
  a 14-bpc HDMI mode or claim our SDR TVs validate HDR/16-bpc output.
- Separate Lighthouse v1/v2, ideal sweep equations from calibrated noisy
  measurements, API contracts from runtime implementation, and reprojection
  from motion smoothing. Do not prescribe exactly half-rate rendering universally.

For a deck, use one mechanism per slide with a source footer; put qualified
numerical comparisons beside their conditions. For a diagram, prioritize a
small readable stack over dense decorative pseudo-text. For an audio overview,
retain the engaging two-host discussion but avoid fictional first-person
experiences presented as evidence; finish with sources and unresolved questions.
For a table, use separate columns for layout, sample precision, transport,
source location, evidence class and review status. Do not silently fill unknowns.

Preserve curatorial attribution and previous correction provenance. Copying
published artifacts is allowed under their specific licence; do not represent
an edited third-party version as Daniel's approved edition.
