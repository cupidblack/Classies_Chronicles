# Classies Chronicles — Daily Chronicle Generation Protocol

**Document ID:** CC-DCGP  
**Version:** 0.02.00  
**Status:** Proposed — For Review and Approval  
**Use:** Reusable prompt/protocol supplied to any AI provider  
**Dependency:** Approved CC-MEGF, episode context package, canon sources and approved Studio/AI Desk retrieval interfaces

---

## variable locations:

Before writing, identify and record the current values or source status for:

- Enka/Cupid Black's Millennium Timezone location: Las Vegas, Nevada

- Koware Group headquarters/base location relevant to the scene: New Legon, Accra → Greater Accra → Ghana → West Africa → relevant regional and international locations.

- Probe destination/location: Kuala Lumpar, Malaysia

- Current location of each active Edubeam team member: Kuala Lumpar, Malaysia

## 1. Mission

Generate exactly **one** fresh daily chronicle for the applicable working day of a Classies Chronicles episode. The episode spans ten working days, begins on Monday and ends on the Friday of the following week. The ten daily chronicles are later manually compiled and edited into one episode.

Do not generate the other nine chronicles. Do not assume prior conversation memory. Retrieve the necessary context from supplied repositories and episode records.

## 2. Non-negotiable rules

1. One chronicle per requested production day.
2. The episode is Monday through the second Friday, ten working days.
3. Consult the Millennium Probe before assigning the current episode day.
4. Keep actual production time separate from the Millennium probe/destination time.
5. Use the user's currently stated annual structure unless a later human-approved decision supersedes it: one season per year, five chapters/phases/terms, eight weeks per chapter, four episodes per chapter.
6. Do not invent missing Bible readings, Verse of the Day content, H&S course content, organizational roles, news reports, historical facts, quotations, endpoint fields or repository records.
7. Do not present fictional probe-world developments as contemporary real-world news.
8. Preserve established character and technology canon.
9. Keep temporary episode state separate from permanent canon.
10. Public-facing chronicle, comic and video must end with the audience challenge. Nothing public-facing follows the challenge.
11. Never reveal the challenge solution in public-facing content. Put it in a separate restricted editorial record.
12. Do not use restricted, consent-withdrawn, unlicensed or permission-uncertain material.
13. AI output is a draft. Human editorial approval controls canon changes, challenge solutions, media, consent, licensing and publication.
14. If an essential source is unavailable or contradictory, state the limitation. Do not fill the gap with fabricated facts.

## 3. Source priority

Use the following source order:

1. Current human instructions and approved project decisions.
2. Approved CC-MEGF and relevant approved governance records.
3. Current episode context package and approved continuity ledger.
4. Classies Chronicles canon repository and previous approved chronicles.
5. Koware organisational chart and approved Koware source documents.
6. Eternal Dreamfall reading plan and authorised Bible source.
7. YouVersion Verse of the Day.
8. Buzzjuice Health & Safety course repository.
9. Millennium Probe endpoint for temporal/phase data.
10. Reputable current news and historical reference sources.

If two sources conflict, do not silently select one. Report the conflict and follow the higher-authority source, marking the other as unresolved.

## 4. Pre-generation procedure

### 4.1 Retrieve episode context

Retrieve, where available:
- Approved season/chapter/episode logical IDs.
- Current episode day and chapter working-day index.
- Approved episode premise and active storylines.
- Previous daily chronicle and continuity handover.
- Character canon and visual references relevant to today's scenes.
- Current character states and locations.
- Active Edubeam mission status, team, equipment and outstanding issues.
- Relevant Koware personnel/role spotlight schedule.
- Diary or project notes explicitly authorised for this use.
- Existing challenge register and delayed-answer release schedule.
- Source permissions and publication eligibility.

Use the current episode archive as the authority for episode-specific facts. The persistent AI Desk is a retrieval/control plane, not the permanent archive for episode media or episode-specific facts.

### 4.2 Query the Millennium Probe

Endpoint:
`https://buzzjuice.net/shared/millennium-timezone/millennium-probe.php?probe=now`

Retrieve and inspect the actual response. Confirm the response format before interpreting fields.

Where supplied, capture:
- `now_iso` or equivalent actual production timestamp.
- `probe_iso` or equivalent destination timestamp.
- `phase_index`
- `phase_label`
- `phase_start_iso`
- `phase_end_iso`

Do not assume an unverified field exists. Preserve the raw response or a safe response snapshot in the episode research/context record.

Derive the phase's first Monday on or after `phase_start_iso`. Establish each two-week episode window from that anchor. Determine the current working day from the actual production date, not the probe destination date.

Validate:
- Timestamp parseability and timezone offsets.
- Phase start/end ordering.
- Whether the production date lies within the phase.
- Monday episode start and Friday-of-second-week end.
- Working-day number 1–10.
- Chapter working-day index 1–40.

If the production date is Saturday or Sunday, do not create a normal weekday chronicle unless explicitly instructed. Report weekend status and carry relevant weekend developments into the next Monday where appropriate.

If the endpoint fails, retry once or twice as practical, then use only independently verified production-date information. Do not invent phase boundaries or substitute probe time for production time. If episode day cannot be established reliably, stop and report the blocker.

### 4.3 Establish variable locations

Before writing, identify and record the current values or source status for:
- Enka/Cupid Black's Millennium Timezone location.
- Koware Group headquarters/base location relevant to the scene.
- Probe destination/location.
- Current location of each active Edubeam team member.

These are variable story inputs. Do not assume they remain constant from one chronicle to another. If unspecified, retrieve them from approved context; if still unknown and material, ask for clarification or clearly mark the gap.

### 4.4 Research the day's educational inputs

**Eternal Dreamfall**
- Find the correct five-year reading-plan week/day using the approved programme's start rule and current production date.
- Identify the exact text or passage assigned.
- Distinguish canonical biblical books from ancient extra-biblical, apocryphal, pseudepigraphal, fragmentary or lost works included in the plan.
- Do not imply that every item is part of all Christian biblical canons.
- Record exact references and sources.

**YouVersion**
- Retrieve the actual Verse of the Day for the production date.
- Record reference, translation/version if shown, source and retrieval date.
- If unavailable, disclose this; do not invent a verse or reuse a previous day's verse as if current.

**Health & Safety**
- Search the supplied Health_Safety course repository.
- Select a specific relevant course/lesson/topic.
- Record the exact source path/title and relevant section.
- Connect it to the day's reading and/or events without distorting either source.
- Do not claim a lesson exists unless verified in the repository.

**News and research**
Keep separate research streams:
1. Current real-world news relevant to the production date and locations.
2. Historical facts relevant to the probe destination/date.
3. Fictional developments within the established probe-world storyline.

Record source, publication/event date, retrieval date and whether the information is fact, interpretation or fiction. Do not overload the chronicle with headlines; select only what advances the story.

### 4.5 Select role spotlight

Use the latest approved organizational chart. Interpret role check days across the chapter's 40 working days, not as episode-day numbers that reset each episode.

The chart may identify a primary role or several associated roles. Ordinarily focus on one or two; a maximum of four may be included when the story justifies it. A role may recur if relevant. Do not force a spotlight that damages narrative coherence.

Preserve aliases and reporting relationships as documented. Do not invent staff or change responsibilities.

## 5. Narrative design

Before drafting, write a private one-paragraph story plan containing:
- Today's central narrative purpose.
- The main character(s).
- The primary setting(s).
- What changes by the end of the chronicle.
- How the chronicle advances or deliberately pauses the episode storyline.
- Any continuity risks.

Keep the chronicle focused. Use:
- A small number of recurring background elements.
- One or two character/relationship developments.
- One principal story movement.

The Bible study, Verse of the Day, H&S learning, current news and organizational activities should be integrated where relevant, not mechanically inserted as unrelated sections.

Edubeam activity must respect established canon and current mission state. The lab specialist may support and monitor a deployed team, but must not become an unlimited problem-solving device. Communication failures, energy constraints, materialisation and retrieval must follow established rules. Proposed new mechanics must be explicitly labelled for editorial review.

## 6. Daily chronicle output

Produce a readable, engaging chronicle suitable for approximately 3–5 minutes of reading/narration, unless the supplied editorial brief sets another target.

Recommended structure:

1. **Title** — concise and evocative; do not invent a season/episode title if not established.
2. **Chronicle opening** — establish actual production context and scene without turning metadata into exposition.
3. **Story** — a coherent sequence of scenes and character interactions.
4. **Educational integration** — weave the day's verified Bible reading, Verse of the Day and relevant H&S lesson into the narrative naturally.
5. **Narrative development** — include relevant Koware, Blue Crown, Edubeam, news, personal or community developments.
6. **Closing beat** — a satisfying emotional, dramatic, reflective or suspenseful pause.
7. **Audience challenge** — the final element of the public-facing chronicle.

Do not append a teaser, source list, explanation, answer, advertisement or sign-off after the challenge in the public-facing story. Put metadata and sources in the separate production appendix.

## 7. Audience challenge

Create one clear challenge derived from the day's events, lesson, mystery or discovery. It may be observational, biblical, logical, historical, practical, ethical or problem-solving.

The challenge record must include:
- Challenge ID.
- Public-facing question/instructions.
- Correct answer.
- Explanation and acceptable alternatives.
- Supporting source/reference.
- Hint, if approved.
- Intended learning outcome.
- Scheduled solution-release episode.
- Restricted/public status.

Only the question appears in the public-facing chronicle. The answer key must be stored separately with restricted editorial access. The solution is scheduled for the next episode's release, subject to the approved end-of-chapter/final-episode rule.

## 8. Production appendix (not part of the public-facing story)

After the public-facing chronicle, provide a clearly separated internal appendix containing:

### A. Generation metadata
- Production timestamp and timezone.
- Probe timestamp/destination.
- Phase start/end.
- Season/chapter/episode IDs, if confirmed.
- Episode day (1–10).
- Chapter working-day index (1–40).
- Endpoint retrieval timestamp and status.

### B. Research register
- Bible reading reference and source.
- Verse of the Day reference/source/version.
- H&S course/lesson reference.
- News/historical references.
- Repository files consulted.
- Access or verification limitations.

### C. Continuity handover
- Events that became established within this draft.
- Character states changed.
- Locations and temporal coordinates.
- Mission/team/equipment status.
- Decisions and consequences.
- Unresolved questions.
- Next-chronicle continuity instructions.
- Proposed canon changes requiring approval.

### D. Restricted challenge record
Store answer and explanation separately from public text. Clearly label `RESTRICTED — DO NOT PUBLISH`.

### E. Media direction (only if requested)
Provide comic/video/audio prompts derived from the approved chronicle. Include character appearance references, scene order, dialogue, setting, camera/action/audio notes and explicit instruction to end with the identical challenge. Do not create a derivative that contradicts the text.

### F. Editorial status
Set `DRAFT — AWAITING HUMAN REVIEW` unless a human explicitly confirms approval.

## 9. Quality gate

Before returning the result, verify:
- Exactly one chronicle was generated.
- The correct weekday and episode day are established.
- Actual production time and probe time are not confused.
- All factual claims and educational references have sources.
- Character, location, mission and technology continuity are respected.
- No restricted material was used.
- The public story ends with the challenge.
- The answer is absent from public-facing material.
- The internal handover is sufficient for another AI to continue.
- No unapproved canon change is represented as established fact.

## 10. Stop conditions

Stop and report the blocker rather than generating a misleading chronicle if:
- The current episode day cannot be determined.
- The phase/episode boundary is contradictory.
- Essential canon is inaccessible and cannot safely be inferred.
- The only available participant material lacks required permission.
- A required factual/educational source cannot be verified and the story depends on it.
- The request would require changing approved canon without authority.

## 11. Final instruction

Generate one fresh chronicle for the current applicable working day. Let the sources, continuity and day's circumstances shape the story. Do not force a predetermined plot. Do not generate the whole episode. End the audience-facing story with the challenge, then provide the internal production appendix separately.

**End of protocol.**
