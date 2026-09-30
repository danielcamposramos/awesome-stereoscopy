# Folded near-eye optics and stereo metadata

Reviewed source input, 30 September 2026. Curated by Daniel Campos Ramos /
EchoSystems AI Studios; editorial replacement by OpenAI Codex for the
NotebookLM-generated report titled “Anaglyph Mathematics & Spectral Multiplexing
Manual”. The original export remains preserved privately. This is a conceptual
primer, not a validated optical prescription. See [licence and attribution](LICENSE.md).

## Keep the layers separate

Stereoscopic images contain different views for the eyes. A codec can describe
their packing, a container can carry layout metadata, a player can interpret
it, a display link can signal its transport structure, and an optical system
can deliver separate views. Agreement at one layer does not certify the next.
Use the [standards index](../../standards.md) for pinned codec/container/link
references and the [anaglyph guide](../../docs/anaglyph-math-and-matrices.md)
for display/glasses-dependent colour matrices.

CIPA still-image standards and Exif are not prescriptions for a headset's
folded optics, nor guarantees of left/right synchronization over HDMI. HDR
transfer characteristics and colour depth are likewise separate from the
polarization mechanisms used to steer light inside a near-eye display.

## Faraday rotation

For the simplified uniform axial-field model, the polarization rotation is

$$\theta(\lambda)=V(\lambda)BL.$$

Here V is the wavelength-dependent Verdet constant, B is magnetic flux density,
and L is path length in the material. VBL is an angle, not magnetic flux density.
Faraday rotation is nonreciprocal: in the simplified double-pass configuration,
its rotations add. A 45° one-way rotation can therefore give a 90° round trip.
Specify propagation direction and polarization-coordinate conventions before
constructing forward/backward Jones matrices. A reciprocal wave plate is not
interchangeable with this simple nonreciprocal rotator model.

## Throughput is a budget, not a slogan

An ideal 50/50 half mirror encountered once in transmission and once in
reflection gives 0.5 × 0.5 = 0.25 useful throughput before additional losses.
If an unpolarized source also loses half its light at an ideal selecting
polarizer, that particular budget becomes 0.125. These calculations are
assumption-bound optical examples, not universal measurements of all headsets.

Replacing the half-mirror routing with nonreciprocal polarization routing can
avoid that particular splitting loss in an idealized design. It does not
make real rotators, polarizers, coatings or lenses lossless. Report measured
throughput with its input polarization, wavelength, geometry and denominator;
keep calculated or projected values explicitly separate. Reflected or leaked
light is not necessarily absorbed as heat in the headset.

The exported report quotes prototype efficiency, projected improvements,
ghost-order tables, material constants and compound rotator angles associated
with [Ding et al., DOI 10.29026/oea.2024.230178](https://doi.org/10.29026/oea.2024.230178).
The complete primary article was not accessible for this pass. Those numerical
prescriptions are deliberately excluded until the original paper and its test
conditions can be read. Do not substitute search snippets for that check.

## Efficiency does not establish focus cues

An efficient folded path can still present a single optical focal plane.
Improving transmission does not make accommodation follow a rendered object's
vergence distance. Varifocal, multifocal, light-field and holographic systems
address focus cues through different mechanisms and have different sampling
and calibration limits. Avoid “VAC eliminated” without measured conditions.
The [Hoffman et al. study](https://www.microsoft.com/en-us/research/publication/vergence-accommodation-conflicts-hinder-visual-performance-and-cause-visual-fatigue/)
provides experimental evidence about focus cues, fusion, performance and fatigue;
it does not justify a universal claim about every source of VR discomfort.

## Engineering use

Use this primer to organize source discovery and explain the distinctions.
Before using a concrete optical design, retrieve its original layout, coordinate
conventions, materials, tolerances and measured results. The accompanying
[artifact corrections](../../docs/notebooklm/artifact-corrections.md) identify
the exported claims that need those checks.
