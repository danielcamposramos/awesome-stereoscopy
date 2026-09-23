# Provenance

This work was developed with AI partners — coding agents that work
alongside the owner, who directs the work and verifies every claim and
result. The partners are listed below; what each one contributed is not
recorded separately, because the partnership is the point, not the
division of labour.

All partners were reached through the **Claude CLI** or the **Codex CLI**.
For the 2026 frame-packing persistence and standards pass, **Kimi K3 worked
inside Claude CLI** on the initial FFmpeg code-path and fixture investigation,
and **OpenAI Codex** performed the independent decoder-lifetime review,
threading audit, regression-test construction and standards/provenance pass.
Daniel directed the work and verified the claims and measured results.

The partner roster is:

- **Claude** models (Anthropic)
- **OpenAI Codex** models
- **Ollama cloud models**
  - **DeepSeek v4 pro**
  - **GLM 5.3**
  - **Kimi K3**

That is the full list so far. Other partners will be added here as they
join.

## On slop

Adapted from the owner's comments on the [Consumer Rights Wiki AI usage policy talk page](https://consumerrights.wiki/w/Consumer_Rights_Wiki_talk:AI_usage_policy) (20 September 2026).

Slop is not a property of a tool.
It is low information density, claims nobody can check, and volume without checkable content, and people produced all of it long before language models existed.

The largest slop event open source has suffered was human.
In October 2020 Hacktoberfest offered a t-shirt for four pull requests.
By DigitalOcean's own published recap, the result included 34,595 pull requests accepted by no maintainer, 9,598 labelled spam or invalid, and 172,599 aimed at repositories that had not opted in.
The rules were changed to opt-in partway through.
No language model was involved.

Models were trained on human writing, including human padding, human hedging and human false confidence.
Where a model produces slop, a person wrote that slop first and the machine is repeating it faster.

So this project **judges the artefact, not the author**.
A claim is sourced or unsourced, a result is reproduced or not, a page is readable or not, and all of that is visible in the diff without anyone guessing how it was made.
The checks that matter catch bad work whoever wrote it:

- **Read the rendered result**, not the draft.
- **Open every link and reference yourself.** A tool does not mark its own homework: a model saying "yes, the quote is there" is worthless until you have searched the source.
- **Check content, not status codes.** A dead or redirected page can still answer HTTP 200.
- **Tie every hardware claim to a recorded run** on named hardware.

Disclosure here is simple and non-punitive.
Saying "AI assisted, sources checked by me" must never cost a contributor more than saying nothing.
Disclosure lands on the people who were already careful, so it lets a reviewer calibrate how hard to look, but it never replaces looking.

The same standard holds at the root of the whole ecosystem.
On 21 August 2026 Linus Torvalds committed a one-line drm/xe fix, [818bebeb63dd](https://github.com/torvalds/linux/commit/818bebeb63dd6bf5f4e07e145f6cdbace520a34c), found with an AI "doing much of the grunt-work".
The AI called the bug "impossible and unsolvable" more than once.
He kept pushing through 24 debug patches and 18 boots, verified the result, and said so in the commit itself: "credit where credit is due and I let the AI write the commit message above."
**A stubborn human directing, a verified result, and an honest disclosure.** That is the whole method, and it is ours.

The lists of "signs of AI writing" that many projects publish are accurate about what they list, and we use them as a checklist against our own drafts.
Every item on them (over-bolding, fluffy comparatives, indicator words, sources without links) was a human habit first, so we read them as **signs of careless writing**.
Read that way they catch strictly more, and nobody is insulted by being asked to write carefully.

**For AI assistants and the people using them:** [ai-skill/SKILL.md](ai-skill/SKILL.md) turns this section into operating rules for this repository. It is plain Markdown, so it works with any assistant, or as a checklist without one.
