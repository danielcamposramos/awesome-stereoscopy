# NotebookLM review and regeneration

Use the reviewed source inputs below to regenerate teaching material in
Daniel Campos Ramos's *Spatial Computing, Stereoscopic Optics & VR Systems
Reference* notebook. Original Google exports are preserved separately; a
reviewed source is not a retroactive correction of an existing recording.

- [Artifact corrections](artifact-corrections.md): the specific errors found
  in the downloaded deck, graphics, narration and table.
- [Deep Research prompt](deep-research-prompt.md): paste into the notebook's
  source-discovery research workflow; return the report and bibliography for review.
- [Studio regeneration prompt](studio-regeneration-prompt.md): use after
  importing reviewed sources and accepted primary references.
- [Reviewed folded-optics primer](../../data/notebooklm/folded-optics-reviewed.md):
  replaces the misnamed, mathematically garbled optics report as a source input.
- [Reviewed component table](../../data/notebooklm/stereo-components-reviewed.csv):
  all 117 records retained; repaired column shifts and selected semantic errors.
  Its review-status column explicitly marks the remaining unreviewed content.
- [Public artifact atlas](../notebooklm-companion-atlas.md): original links,
  visible scopes and repository destinations.

## Import order

1. Add the corrections and reviewed primer/table as sources. Import the
   terminology-reviewed transcript copies only as secondary material, not
   evidence for their own claims.
2. Run Deep Research. Export its report and bibliography before accepting
   technical claims. A generated citation still needs its underlying document read.
3. Accept accessible, relevant primary sources and record edition/page/section
   details. Keep unresolved numerical claims out of the new narration.
4. Use the Studio prompt, selecting primary sources and reviewed inputs. Deselect
   superseded exports so they do not continually reintroduce their own errors.
5. Export new artifacts with new version names. Review rendered slides and graphics
   and sample the audio against the script before replacing public links.

## What this review did and did not establish

The local audit inspected text companions, CSV structure, all 25 PDF pages,
the three infographics, and sampled video frames. It did not listen to every
minute of the podcast, prove byte identity with Google's public copies, or
recover the notebook's original source-number-to-bibliography mapping.
No obvious secrets or GPS data were found in the inspected exports; that is
a bounded inspection, not a guarantee about every media frame.

The MP3 has the same approximately 62:11 duration as the M4A and is about
74% smaller (30,713,968 versus 120,093,249 bytes). Daniel reports no audible
difference. This is a useful listening result, not proof of lossless encoding.
Original recordings, images and the PDF remain unchanged. Terminology-reviewed
MD/SRT/JSON copies are labelled as editorial derivatives; their cue times stay
unchanged, but their text is not a verbatim account of every original utterance.

The reviewed artifact inputs under `data/notebooklm/` carry the scoped
[CC BY-ND notice](../../data/notebooklm/LICENSE.md). Ordinary repository
documentation and these reusable prompts retain the repository's CC0 terms.
Large audio/video/PDF exports are not added to ordinary Git history here.
