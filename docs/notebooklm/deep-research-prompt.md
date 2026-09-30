# Deep Research prompt for spatial display sources

Copy the following prompt into NotebookLM's Deep Research source-discovery
workflow. This asks for a research report and bibliography, not another Studio
summary. If it exceeds the interface limit, run the numbered lanes separately
with the same evidence rules.

---

Expand and critically audit the sources of my notebook, “Spatial Computing,
Stereoscopic Optics & VR Systems Reference”. The goal is a primary-source-backed
reference from binocular vision through stereo media, HDMI colour/signalling,
display optics and VR runtime behaviour. Improve both depth and correctness;
do not recycle my generated decks, videos, podcast or tables as independent proof.

Our project provenance starts here:

- https://github.com/danielcamposramos/awesome-stereoscopy
- https://github.com/danielcamposramos/awesome-stereoscopy/blob/main/standards.md
- https://github.com/danielcamposramos/awesome-stereoscopy/tree/main/docs/notebooklm
- https://github.com/danielcamposramos/sony-bravia-linux
- https://github.com/danielcamposramos/awesome-linux-hdr
- https://github.com/danielcamposramos/awesome-vr
- https://github.com/danielcamposramos/awesome-ar

Daniel Campos Ramos directs and physically tests the project; the repositories
disclose AI partners including Kimi K3 inside Claude CLI, Claude, OpenAI Codex
and Gemini inside Google Jules. Use those records for campaign provenance and
named-hardware observations, not as substitutes for normative specifications
or independent scientific experiments.

## Evidence rules

Prefer official standards/registries, peer-reviewed original experiments,
author/institution-hosted manuscripts, source code and official API/runtime
documentation. Reviews can map a field, but follow numerical claims to their
original experiments. Search snippets are discovery aids, not inspected evidence.
Never bypass access controls; mark inaccessible sources and give lawful access
routes. Do not treat inability to retrieve a document as proof that it says nothing.

For each important claim, give the source title, authors/body, publication date,
exact edition or code commit, DOI/official URL, page/figure/table/section, and a
short paraphrase of the relevant passage. Classify it as normative semantics,
implementation behaviour, controlled measurement, idealized model, projected
performance, or unresolved inference. Record conditions, denominator, error bars
or detection limits where relevant. Distinguish publication dates from experiment
dates. Identify contradictions and corrections rather than averaging them away.

Seek the following six source lanes:

1. **Binocular perception and comfort.** Horopter, retinal disparity, IPD
   distributions, Panum's fusional area, fusion versus stereoacuity, diplopia,
   suppression and vergence/accommodation coupling. Find original measurements
   showing dependence on stimulus, eccentricity, exposure and observer. Audit
   supposed universal limits of 15–30 arc minutes, one degree and 0.4 dioptres.
   Start with Hoffman, Girshick, Akeley and Banks (2008), DOI 10.1167/8.3.33.
   Separate VAC-related fatigue from visual-vestibular conflict and latency;
   no medical diagnosis or promised nausea cure.

2. **Autostereoscopic and focus-cue architectures.** Barrier, lenticular,
   directional-backlight, multiview, super-multiview, integral/light-field,
   multifocal, varifocal and holographic systems. Compare angular sampling,
   spatial resolution, brightness, eyebox, pupil size, depth range and measured
   accommodation response. Test whether “two rays per pupil” is a sufficient
   condition or just a design heuristic under specified assumptions. Separate
   ray-field reproduction from coherent wavefront reconstruction. Do not
   generalize a particular half-resolution or lens-count example to all designs.

3. **Near-eye folded optics and Faraday rotation.** Fresnel/pancake layouts,
   polarization conventions, reciprocal versus nonreciprocal double passes,
   Jones matrices with a stated coordinate basis, absorption versus reflection,
   throughput normalization, ghosts, dispersion and thermal consequences.
   Locate and read Ding et al., “Breaking the optical efficiency limit of virtual
   reality with a nonreciprocal polarization rotator”, DOI 10.29026/oea.2024.230178.
   Verify the exports' 71.5% measured, 76.3% calculated and 93.2% projected
   efficiencies, the claimed 0% second-order ghost, TGG dispersion constants and
   compound angle sequences. State wavelength, polarization, components and
   limitations. Ideal 100% throughput is not a shipping headset's performance
   and efficiency improvement is not an accommodation correction.

4. **Stereo media, metadata and norms.** Pin editions of H.264, H.265, H.274,
   applicable DVB profiles, Matroska StereoMode and Google Spherical Video V2
   st3d. Distinguish message persistence from encoder cadence, IDR-correlated
   behaviour on our tested BRAVIAs from a normative IDR rule, MVC inter-view
   coding from HDMI transport, and codec packing enums from HDMI/DRM values.
   Audit CIPA DC-006/DC-007/Exif scope against their actual text; image containers
   do not guarantee display-link or optical interoperability. Recover original
   bibliography mappings if available; never invent what source marker “11” means.

5. **HDMI stereo plus SDR Deep Color and HDR.** Verify HDMI structure codes
   0/1/2/3/4/5/6/8, frame-packing rasters, EDID/CTA capabilities, AVI/VSIF/GCP,
   RGB and YCbCr 4:4:4/4:2:2/4:2:0, quantization and chroma siting. Separate
   render precision, framebuffer format, signal sample precision, wire packing
   and display-panel native depth. Audit 8/10/12/16-bpc transport support by
   encoding/version; do not invent a standard 14-bpc HDMI Deep Color mode.
   HDR is not synonymous with 16 bpc, and an HDR-capable GPU does not prove
   16-bpc output. Use HDMI, CTA-861.3 and BT.2100 editions and Linux source.
   Analyze real-time HDR-to-SDR tone mapping with high-precision intermediates
   and 10/12/16-bpc output where the actual sink/driver/link support it; include
   dithering, gamut mapping and banding limits. Keep TMDS and FRL models distinct.
   Our 3D-plus-12-bpc BRAVIA observations are measured SDR results, not an HDR
   test or an HDMI packet-analyser capture. Read the current ledger for scope.

6. **Lighthouse and runtime reconstruction.** Separate Lighthouse v1/v2
   timing/modulation, calibration, station capacity versus product limits,
   photodiodes, IMU fusion and pose-estimator placement/rates. Prefer Valve,
   OpenVR/OpenXR, libsurvive and Monado sources with versions/commits. Separate
   prediction, rotational/positional/depth reprojection, motion smoothing and
   synthesized frames from application rendering. Valve's 2018 announcement
   describes more than half-rate rendering; audit later implementation rather
   than assuming one fixed ratio. API definitions do not by themselves prove
   where the compositor implements an operation.

## Deliverables

Return a lane-by-lane report, a deduplicated bibliography and a claim matrix:
claim / evidence class / exact source location / conditions / verified or unresolved /
correction to existing artifacts. Include lawful full-text availability and
redistribution status separately: public access does not imply permission to host.
Identify evidence gaps and disputed claims; rank the next sources by how many
specific errors they can resolve. Prefer a smaller inspected source set to a
large unverified collection. Do not generate replacement Studio artifacts yet.
