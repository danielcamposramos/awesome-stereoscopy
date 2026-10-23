# Contribution Guidelines

Please open a pull request that adds one thing, or fixes one thing, and says why in a sentence.

## What belongs here

Stereoscopy as a medium: presenting a different image to each eye, and everything needed to create, store, signal, deliver or display it.
That includes worn displays, because a headset is a stereoscope you wear and the line from Wheatstone's mirrors to Cardboard and current head-mounted displays is one continuous idea.
Historical material is welcome and wanted, because the formats only make sense in order.

## What does not

- Computer-vision depth estimation, unless it is directly useful for producing or repairing stereo pairs. It is a different field that shares a word, and there are better lists for it.
- Engine tooling, game design and platform business news. The headsets belong here as stereo displays, and the software driving their stereo rendering belongs here.
- Haptics, locomotion and body tracking belong **only** in the clearly-labelled *Beyond the eyes* section, which exists because presence needs more than an image but is explicitly not the subject of this list. Keep it short, keep it honest, and do not let it grow into a general VR list: [awesome-vr](https://github.com/danielcamposramos/awesome-vr) is the place for that, and [awesome-ar](https://github.com/danielcamposramos/awesome-ar) for see-through optics and tracking.
- Dead links, abandoned projects with no historical value, and anything whose page no longer loads.

## Quality bar

- **Check the link before submitting.** Every entry here was verified when added.
- One line per entry: `- [Name](url) - What it is, ending with a period.`
- Say what a thing *is*, not how good it is. No marketing language.
- If a project is abandoned or a service is unreliable, say so plainly in the description. An honest note is more useful than an omission, and readers will find out anyway.
- Historical entries should carry a date, because in this subject the date usually explains the format.

## Curators

The list is Daniel's, and every change goes through a pull request that he reviews as code owner.
Regular contributors can take on an area of the list, and the steps are written here so everyone climbs the same ladder.

- **Contributor.** Fork, pull request, one change per request. The checks run on their own after your first merged change.
- **Curator.** Your name and area are listed in [`.github/CURATORS`](.github/CURATORS). On any pull request you can comment `/recheck` to rerun its checks and `/scan-links` to start the link scan of the whole list. You review submissions in your area when asked, and your review is on the record. Earned by merged entries that hold against their primary sources, honest notes on what could not be verified, and a correction handled well.
- **Collaborator.** Write access on GitHub, the only level a repository owned by a personal account offers. You can be requested as reviewer, label and triage, rerun and approve CI, and merge a pull request once it has Daniel's review as code owner. Earned after thirty days of clean record as curator, or earlier when Daniel decides the record already shows it. The protection of `main` does not change: one code owner review, every conversation resolved and the lint check. Releases stay with Daniel.
- **Co-curator.** A `CODEOWNERS` line for the pages of your area, so your approval closes pull requests that touch only them. Decided case by case, when the area has pages of its own.

Curators, by name and area:

- Sisir ([captof-omuamua](https://github.com/captof-omuamua)): historical and regional stereo photography beyond Europe and North America; curator since 21 October 2026, collaborator since 23 October 2026.

## Using an AI assistant

Load [ai-skill/SKILL.md](ai-skill/SKILL.md) first.
It carries these rules plus the verification discipline behind every entry, and it works with any assistant.
Assistance is welcome and never held against you; see [PROVENANCE.md](PROVENANCE.md#on-slop).
