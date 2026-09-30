# Stereoscopy in depth

The [list](../readme.md) points at what exists. These pages go under it: the arithmetic, the signal layouts and the pipelines behind its entries, each drawn twice, once in plain text that reads anywhere and once in Mermaid for GitHub.

Every figure here names its source (FFmpeg's code, the Linux kernel, the cited papers and specifications), and each page was checked against those sources before it was published.

## Guides

| Guide | What it covers | Goes deeper on |
|---|---|---|
| [Anaglyph mathematics](anaglyph-math-and-matrices.md) | Why a plain red/cyan channel split ghosts and rivals; Dubois's least-squares projection; FFmpeg's red/cyan matrices and the colour space it applies them in, with its green/magenta and amber/blue variants; why a matrix fits one display and one pair of glasses | [Anaglyph colour codes](../readme.md#anaglyph-colour-codes) |
| [Frame packing and HDMI timings](frame-packing-and-hdmi-timings.md) | The eight HDMI 1.4 stereo structures grouped by what survives of each eye; the 1080p and 720p frame-packing rasters; the Vendor-Specific InfoFrame byte by byte, as Linux packs it | [Every HDMI 1.4 stereo structure](../readme.md#every-hdmi-14-stereo-structure) |
| [Stereo 3D plus Deep Color on HDMI](stereo-deep-colour-link-budget.md) | How stereo timing, RGB/YCbCr, bits per component, AVI/VSIF/GCP packets and TMDS character rate combine; the 225 MHz HX855 link budget; what the 22-step run-34 record and photographs prove | [Every HDMI 1.4 stereo structure](../readme.md#every-hdmi-14-stereo-structure) and [Evidence ledger](../readme.md#evidence-ledger) |
| [Stereo camera geometry](stereo-camera-geometry.md) | Disparity and parallax; the 1/30 rule; the parallax budget worked from the scene's depth range to the largest baseline; parallel, toe-in and beam-splitter rigs | [Two identical cameras in a rig](../readme.md#two-identical-cameras-in-a-rig) |
| [From a VR engine to a 3D display](vr-to-3d-display-pipeline.md) | How a headset's two eyes reach a 3D television: frustums that meet at the screen, the HUD at zero parallax, packing, and the open projects that do it today | [Open software for headsets](../readme.md#open-software-for-headsets) |

## Reference

- [NotebookLM review and regeneration kit](notebooklm/README.md): pinpoint
  corrections to exported educational artifacts, reviewed source inputs, and
  Deep Research/Studio prompts. Generated learning material is not primary evidence.

- [Federated Signal Ledger pointers](reference/evidence-ledger/pointers.md): machine-checked pointers to measured claims kept in [sony-bravia-linux](https://github.com/danielcamposramos/sony-bravia-linux), bound by semantic hash rather than copied. The list's [Evidence ledger](../readme.md#evidence-ledger) introduces them.
- [NotebookLM companion atlas](notebooklm-companion-atlas.md): the 14 public generated learning artefacts mapped by type, subject and canonical repository, with the boundary between discovery material and primary evidence made explicit.

## How these pages were made

The guides were Daniel's requests, drafted by Gemini inside Google Jules and corrected against their sources before merge; [PROVENANCE.md](../PROVENANCE.md) has the full account. Corrections follow the same rule as the list: a claim without a source it can be checked against does not stay.
