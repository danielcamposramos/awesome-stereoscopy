# NotebookLM artifact corrections

Review date: 30 September 2026. Original generation: Google NotebookLM,
from sources selected by Daniel Campos Ramos. Review: OpenAI Codex and
partner agents, directed by Daniel. These are editorial findings, not new
bench measurements. Page numbers refer to the downloaded 25-page PDF;
timestamps refer to the downloaded recordings, not the public viewer shell.

## Corrections that apply across artifacts

- Use **Panum's fusional area**, **horopter**, **vergence**, and **varifocal**.
  Terminology-reviewed transcript copies correct these recognizable errors,
  but do not certify the remaining scientific statements.
- A headset's accommodation stimulus comes from its **optical focal plane**,
  not simply the physical panel's millimetre distance from the eye. A fixed-focus
  headset can have a distant virtual focal plane despite a nearby panel.
- VAC, visual-vestibular conflict, latency and crosstalk are separate contributors
  to discomfort. Do not assign all nausea to VAC or promise its complete removal.
  [Hoffman et al. (2008)](https://www.microsoft.com/en-us/research/publication/vergence-accommodation-conflicts-hinder-visual-performance-and-cause-visual-fatigue/)
  supports focus-cue effects on fusion, performance and fatigue, not a universal cure.
- Fusion/comfort thresholds depend on stimulus, observer and viewing geometry.
  Do not use 15–30 arc minutes, 0.4 dioptres or one degree as universal limits.
- Optical throughput, image resolution, accommodation cues and transport packing
  are different axes. Improvements on one do not automatically improve the others.

## Downloaded slide deck

| PDF page | Change for the regenerated deck |
|---|---|
| 3 | Separate VAC from motion-related visual-vestibular conflict; remove a universal fusion threshold. |
| 6 | Qualify shutter-glasses throughput by implementation and measurement conditions; remove the unsupported generic 10–15% value. |
| 7–8 | Row-interleaved FPR panels trade vertical rows per eye; passive cinema projection is a different architecture and does not inherently halve panel rows. |
| 10–11 | Present barrier/lenticular resolution and brightness as geometry-dependent trade-offs; do not generalize a specific lens-count calculation. |
| 12–13, 16 | Two rays entering a pupil is not a universal sufficient condition for correct accommodation. Specify angular sampling, pupil size, viewing range and measured results. Multiview resolution loss is not always vertical. |
| 14–15 | Directional backlight and eye-tracking benefits are design-dependent; remove blanket elimination of view gaps. |
| 17 | Distinguish multifocal, light-field and holographic wavefront methods; none is limited only by compute and SLM étendue. |
| 19 | Light not reaching the eye is not necessarily absorbed as heat inside the headset. Distinguish reflection, leakage and absorption. |
| 20–22 | Label ideal, prototype and projected efficiency separately. `B` is magnetic flux density; `V(λ)BL` is rotation angle. Zero or undetectable ghosting must have a configuration and detection limit. |
| 23 | Replace fixed SBS→barrier, TaB→FPR, frame-packing→shutter/VR mappings. An HDMI layout is not a mandate for the sink's internal display architecture. |
| 25 | Faraday rotation can improve an optical loss budget; it does not itself fix VAC. |

The public shell described a 24-slide path; the downloaded PDF contains 25
pages. Use actual exported page counts when recording a version.

## Infographics

**Stereoscopic Systems and Optics Diagram:** regenerate rather than use as an
engineering diagram. It labels top-and-bottom with code 4 and SBS-half with
code 6. The correct HDMI structure values are:

| HDMI structure | Wire code |
|---|---:|
| Frame packing | 0 |
| Field alternative | 1 |
| Line alternative | 2 |
| Side-by-side full | 3 |
| L + depth | 4 |
| L + depth + graphics + graphics-depth | 5 |
| Top-and-bottom | 6 |
| Side-by-side half | 8 |

These values were checked in the local Linux 7.0 source's `include/linux/hdmi.h`;
see the [upstream definitions](https://github.com/torvalds/linux/blob/master/include/linux/hdmi.h)
and the repository's [byte-level guide](../frame-packing-and-hdmi-timings.md).
They are **not** the H.264 SEI packing-type enum or DRM's encoded flag values.
Regenerate illegible text and equations; do not guess a correction to corrupted
optical annotations. A 45° Faraday rotation gives a 90° ideal double pass in
the simplified model, not the diagram's 80° label.

**VR Optical Efficiency Comparison:** retain the distinction between an
idealized limit and an experiment/projection. The exports quote 71.5% measured
and 93.2% projected, but this pass could not inspect the complete primary
article's conditions. Keep those numbers out of regenerated teaching material
until the [Ding et al. paper, DOI 10.29026/oea.2024.230178](https://doi.org/10.29026/oea.2024.230178)
has been read and its measurement denominator and scope recorded.

**Vergence-Accommodation Conflict Explained:** label the headset's optical
focal plane, not physical panel distance. Qualify the proposed comfort boundary
and angular-sampling claims. Gaze-contingent blur does not move the focal plane.

## Narration and transcripts

| Recording | Segment | Regeneration instruction |
|---|---|---|
| Biological Blueprint | About 00:30 | Use Panum; do not make the quoted range a universal tolerance. |
| Biological Blueprint | About 01:30 | Restrict the half-resolution claim to the depicted two-view spatial-multiplexed design. |
| Biological Blueprint | About 04:29–05:09 | Remove the all-discomfort claim and replace physical-panel focus with optical focal plane. |
| Biological Blueprint | About 06:29 | Do not promise correct accommodation merely from multiple rays. |
| Time as Space | About 01:29, 03:24–04:05 | Treat timing, station count and processing rates as version/device-specific. Calibrated sweep geometry is not flawless or exact. Identify the evidence for where pose estimation runs. |
| Time as Space | About 05:32–06:25 | Attribute reprojection/smoothing to the runtime/compositor, not merely the API. Do not restrict motion smoothing to exactly half-rate rendering. |
| Why Your Brain Fights VR | Throughout | Correct terminology; separate focus cues from physical panel location; remove unconditional VAC cures, all-loss-is-heat claims and universal efficiency promises. |

[Valve's 2018 announcement](https://store.steampowered.com/news/posts/?appids=250820&enddate=1539830168)
explicitly describes both half-rate rendering and two or three synthesized frames
per application frame. It establishes that the narration's “exactly half” is
too narrow, not the behaviour of every later runtime/version.
The podcast's conversational first-person examples are generated narration,
not testimony from two identifiable human experimenters.

## Component table and report

The reviewed CSV keeps all 117 records and original numeric source markers.
Three ITU names contained an unquoted comma, shifting their semantic columns;
those records are repaired. The `st3d` row now separates its `uint8` syntax from
sample colour depth and includes all five layouts defined by the
[Google RFC](https://github.com/google/spatial-media/blob/master/docs/spherical-video-v2-rfc.md).
MVC is separated from HDMI transport, FPR resolution is qualified, and the HDR
and H.264 hardware claims are bounded. Remaining rows are explicitly not fully
reviewed; the numbered source markers still lack a recoverable bibliography.

The original report's title promises anaglyph mathematics but mainly presents
folded optics. Its escaped equations, collapsed tables, ghost-order numbers,
TGG constants and exact angle sequences are not suitable as unverified design
instructions. The [reviewed primer](../../data/notebooklm/folded-optics-reviewed.md)
keeps the supported conceptual distinctions and identifies what still needs
primary-paper verification; the existing [anaglyph guide](../anaglyph-math-and-matrices.md)
is the separate source for actual display/glasses-dependent anaglyph matrices.
