# Stereoscopy standards and primary references

This index points to the documents that define how stereoscopic intent moves
from a coded video stream or container to a player, compositor, graphics driver
and display. Edition pages are pinned where reproducibility matters; family
landing pages are also included so readers can find later revisions.

The distinction used throughout this list is deliberate:

- **Normative semantics** come from the specification that defines a field.
- **Implementation behaviour** comes from a named encoder, decoder or driver.
- **Measured hardware behaviour** comes from a controlled device test.

An IDR-correlated message cadence observed in an x264 file is therefore not
presented as the lifetime rule of the H.264 message. The message's repetition
field defines decoder persistence; where an encoder chooses to repeat the
message is a separate implementation decision.

## Coded-video signalling

### ITU-T H.264 | ISO/IEC 14496-10 (AVC)

- [Recommendation family](https://www.itu.int/rec/T-REC-H.264)
- [Pinned August 2024 edition](https://www.itu.int/rec/T-REC-H.264-202408-S/en)
- [January 2012 edition used for clause-level verification](https://www.itu.int/rec/T-REC-H.264-201201-S/en)

Annex D defines Supplemental Enhancement Information. In the verified 2012
edition, clauses D.1.25 and D.2.25 define the frame-packing-arrangement syntax
and semantics. The
`frame_packing_arrangement` message carries the packing type, view order,
quincunx flag, cancellation state and
`frame_packing_arrangement_repetition_period`. A repetition period of zero is
current-frame-only; a non-zero value makes the arrangement persistent under the
message's specified later-message/cancellation/coded-video-sequence boundaries.
It does not mean "until the next IDR".

Search terms inside the recommendation:
`frame_packing_arrangement_cancel_flag`,
`frame_packing_arrangement_repetition_period`, and
`frame_packing_arrangement_type`.

### ITU-T H.265 | ISO/IEC 23008-2 (HEVC)

- [Recommendation family](https://www.itu.int/rec/T-REC-H.265)
- [Pinned July 2024 edition](https://www.itu.int/rec/T-REC-H.265-202407-S/en)
- [April 2013 edition used for clause-level verification](https://www.itu.int/rec/T-REC-H.265-201304-S/en)

In the verified 2013 edition, clauses D.2.16 and D.3.16 define the syntax and
semantics. HEVC's frame-packing message uses
`frame_packing_arrangement_persistence_flag` rather than H.264's repetition
period. A clear flag limits the arrangement to the current picture; a set flag
retains it according to the message's persistence semantics until it is
superseded or cancelled.

Search terms inside the recommendation:
`frame_packing_arrangement_persistence_flag`,
`frame_packing_arrangement_cancel_flag`, and
`frame_packing_arrangement_type`.

### ITU-T H.274 | ISO/IEC 23002-7 (versatile SEI messages)

- [Recommendation family](https://www.itu.int/rec/T-REC-H.274)
- [Pinned September 2023 edition](https://www.itu.int/rec/T-REC-H.274-202309-S/en)
- [August 2020 edition used for clause-level verification](https://www.itu.int/rec/T-REC-H.274-202008-S/en)

H.274 defines codec-independent versatile SEI messages used with newer video
coding systems, including VVC. Its frame-packing syntax likewise carries a
persistence flag. In the verified 2020 edition, clauses 8.6.1 and 8.6.2 define
the syntax and semantics: zero is current-picture-only, one persists in output
order until a new coded-layer video sequence, end of bitstream, or a later
applicable frame-packing message. A decoder implementation that shares
H.264/H.265/H.274 SEI code must still preserve the scalar frame-packing state
across that codec's own frame/thread contexts.

## Broadcast and delivery profiles

### ETSI TS 101 547-2 — DVB frame-compatible 3DTV

- [Version 1.2.1 PDF from ETSI](https://www.etsi.org/deliver/etsi_ts/101500_101599/10154702/01.02.01_60/ts_10154702v010201p.pdf)

Clause 6.4.1 specifies use of the H.264 frame-packing-arrangement SEI in a
frame-compatible 3D service. This application profile requires a much denser
message cadence than common files and defines cancellation signalling around
2D/3D transitions. That delivery rule is evidence about DVB services, not a
redefinition of H.264's underlying persistence fields.

### DVB specification catalogue

- [DVB specifications](https://dvb.org/specifications/)

Use the catalogue to locate later frame-compatible and service-compatible 3DTV
documents and their status.

## Container signalling

### Matroska `StereoMode`

- [Matroska element specification](https://www.matroska.org/technical/elements.html)
- [Matroska specification source](https://github.com/ietf-wg-cellar/matroska-specification)

`StereoMode` is track/container metadata. It is not the H.264/H.265 in-stream
frame-packing SEI, and remuxing or delivery paths may preserve one while losing
the other. A player must also define precedence when both exist and disagree.

## Display-link signalling

### HDMI 1.4-era stereoscopic structures

- [HDMI 1.4 feature archive](https://www.hdmi.org/download/savefile?bucket=hdmi-web-public&fileKey=Specifications%2F1dot4_feature_archive.pdf)
- [HDMI 1.4a announcement](https://www.hdmi.org/announce/detail/84)
- [Linux HDMI wire definitions](https://github.com/torvalds/linux/blob/master/include/linux/hdmi.h)
- [Linux DRM stereo-mode definitions](https://github.com/torvalds/linux/blob/master/include/drm/drm_modes.h)

The public HDMI material establishes the 1.4-era stereo feature family. The
Linux headers are the auditable implementation vocabulary for frame packing,
field/line alternatives, full and half side-by-side, top-and-bottom and depth
structures. Capability exposure through EDID/DRM and actual scanout/infoframe
generation are separate driver responsibilities.

## Implementations useful for cross-checking

- [x264](https://code.videolan.org/videolan/x264) - H.264 encoder implementation that writes the frame-packing-arrangement SEI for `--frame-packing`; its physical repetition cadence is implementation behaviour.
- [FFmpeg](https://code.ffmpeg.org/FFmpeg/FFmpeg) - Shared H.264/H.265/VVC SEI parsing and `AV_FRAME_DATA_STEREO3D` export used by players and analysis tools.
- [Linux DRM](https://github.com/torvalds/linux/tree/master/drivers/gpu/drm) - Mode discovery, validation, scanout and HDMI infoframe paths used to audit open-driver stereo support.

## Why the documents are linked, not mirrored

ITU marks the selected recommendations as freely available for download, but
its [copyright notice](https://www.itu.int/en/Pages/copyright.aspx) says ITU
holds copyright and asks users to request permission before reproducing its
materials. ETSI and HDMI documents have their own terms. This CC0 repository
therefore hosts the index, interoperable facts and links—not unlicensed copies
of standards PDFs. A document can be added locally only when its licence or
written permission allows redistribution under compatible terms.
