# NotebookLM Companion Atlas

Daniel Campos Ramos assembled the public NotebookLM notebook
[Spatial Computing, Stereoscopic Optics & VR Systems Reference](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8)
from the project's research corpus. This page preserves a stable map of its
generated learning artefacts and states how they may be used.

These are **navigation and teaching aids**, not independent evidence. Each
page identifies itself as AI-generated from user-provided sources. A “Based on
62 sources” or “Based on 100 sources” badge does not expose the underlying
source list on the public artefact page. Technical claims promoted into this
repository must therefore cite the primary paper, specification, source code,
or Signal Ledger claim directly.

The 14 direct artefact links below were publicly readable without an account
on 30 September 2026. Interactive cards, quizzes, and mind maps render inside
Google's embedded viewer; their inner content may not be available to a plain
HTML reader.

## Artefact Map

| Type | Artefact | Visible scope | Best canonical home |
|---|---|---|---|
| Video overview | [The Tracking Physics & Motion Reconstruction Engine of Virtual Reality](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/ad982761-0e73-4d1d-8eec-f8174ebe8900) | Lighthouse tracking and runtime motion reconstruction; based on 100 sources | `awesome-vr` |
| Video overview | [Global Audiovisual and Imaging Technical Standards Reference Collection](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/31cad53b-de15-4822-b653-444b20de548e) | Standards-oriented overview; based on 62 sources | Cross-project index |
| Audio overview | [Why Your Brain Fights Virtual Reality](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/4ad0c1d2-c493-4763-9211-e096ae021dbc) | Binocular perception, vergence-accommodation conflict, and comfort | `awesome-stereoscopy` / `awesome-vr` |
| Infographic | [Vergence-Accommodation Conflict & Focus Cue Solutions](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/fc3f3dc5-3c03-49b0-aefb-1cea1b247fea) | VAC and four proposed optical solution families | `awesome-stereoscopy` / `awesome-vr` |
| Report | [Anaglyph Mathematics & Spectral Multiplexing Manual](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/080728b7-846f-4828-b364-d2dca899faf2) | Despite its title, spans BT.2100, Faraday rotation, Jones matrices, folded optics, ghost suppression, and spectral materials | Split across `awesome-stereoscopy`, `awesome-vr`, and `awesome-linux-hdr` after source review |
| Slide deck | [Architectural Modalities of Stereoscopic, Autostereoscopic and Near-Eye Displays](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/5847a165-1c8b-49eb-a635-959e9ea4791b) | Public shell describes 24 slides; downloaded PDF has 25 pages covering stereopsis, autostereoscopy, light fields, pancake optics, and camera geometry | `awesome-stereoscopy` / `awesome-vr` |
| Mind map | [3D Video Transmission & Metadata Standards](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/4b1a959c-8fd6-4b61-b66c-785eadaff7bd) | Codec, container, player, and display-link signalling | `awesome-stereoscopy` |
| Quiz | [Optics Quiz](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/2e321291-6c74-4541-8636-a91e2bd213d3) | Interactive review questions | Teaching companion |
| Infographic | [VR Optical Efficiency Comparison](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/4a9ffe83-6a86-4abb-ac07-f343acfe6e13) | Conventional folded pancake optics versus a Faraday-rotator design | `awesome-vr` after primary-paper review |
| Flashcards | [Optics Flashcards](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/133d16be-ea72-4876-a972-38023a1c2433) | Interactive optics terminology | Teaching companion |
| Mind map | [Vision Map](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/d353b6ed-aee4-4457-a7b0-83600f0a1030) | Visual-system concept map | `awesome-stereoscopy` |
| Infographic | [Stereoscopic Systems and Optics Diagram](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/93a9cd95-a479-45d7-93bf-4aab934abbd4) | Vision, camera geometry, encoding, and VR optics | `awesome-stereoscopy` / `awesome-vr` |
| Mind map | [Stereoscopy Mindmap](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/2f46340e-e24b-452a-862d-1e2f301c9c27) | Broad stereoscopy map | `awesome-stereoscopy` |
| Data table | [Stereo 3D Formats, Standards, and Hardware Components](https://notebook.google.com/notebook/6001af04-d8fd-4867-935f-809b85cf6ea8/artifact/65f090bd-dafa-40d3-8ec4-cf44d9ebda47) | 117 rows across formats, standards, hardware, runtimes, drivers, players, broadcast profiles, and project tooling | Discovery index; validate each row before reuse |

## Review Boundaries Already Found

The [local export review and regeneration kit](notebooklm/README.md) contains
specific page/timestamp corrections, reviewed text/table source inputs, and
copy-ready Deep Research and Studio prompts. Original PDF/audio/video/image
exports remain unchanged; the kit must not be mistaken for repaired recordings.

- The report named for anaglyph mathematics is substantially broader than its
  title. Its subjects should be separated before any section is treated as a
  focused reference.
- The data table describes the MP4 `st3d` box's eight-bit `stereo_mode` syntax
  field under “Supported Color Depth and Format”. That is a category error:
  the field width is not the video's colour depth.
- “Lossless Faraday” is stronger than the public page establishes. Until its
  underlying paper and complete loss budget are checked, the safe description
  is a **higher-theoretical-efficiency Faraday-rotator design**.
- Precise efficiency, ghost-order, and material-constant numbers in the
  Faraday/TGG material need direct primary-paper citations before reuse.
- Panum's fusional area is not one fixed disparity limit; it varies with the
  stimulus, retinal eccentricity, and observer.
- Vergence-accommodation conflict and vestibular motion conflict are distinct
  mechanisms. Reprojection and motion-based synthetic-frame generation are
  likewise distinct operations.
- A light-field display usually steers angular views through a physical
  display surface; “projects an image into free space” is not a safe generic
  definition.
- Lighthouse v1 and v2 must not be collapsed into one signalling protocol.

## Documentation Opportunities

The atlas exposes genuine gaps without requiring the root lists to become
monoliths:

1. `awesome-stereoscopy`: binocular fusion and visual comfort, including the
   horopter, Panum's fusional area, fusion/diplopia, stereoacuity, and VAC.
2. `awesome-stereoscopy`: autostereoscopic and light-field display optics,
   separated from the existing product catalogue.
3. `awesome-vr`: a near-eye optical stack guide covering Fresnel and pancake
   optics, polarization passes, efficiency, ghosting, eye box, and eye relief.
4. `awesome-vr`: separate guides for Lighthouse tracking and for late-stage
   reprojection versus motion smoothing.

The HDMI/SEI/Matroska lane is already documented in
[`standards.md`](../standards.md) and the
[frame-packing](frame-packing-and-hdmi-timings.md) and
[Deep Color](stereo-deep-colour-link-budget.md) guides. New material there
should close a specific source-backed gap rather than restate the atlas.
