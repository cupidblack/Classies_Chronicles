# Classies Chronicles — Episode Continuity Ledger & Production Handover Specification

**Document ID:** CC-ECLPM  
**Version:** 0.02.00  
**Status:** Proposed — For Review and Approval  
**Purpose:** Episode-owned continuity, research provenance, challenge control and production tracking  
**Archive authority:** Approved Studio Structure Skeletal Blueprint and AI Desk Architecture

---

## 1. Purpose

CC-ECLPM defines the minimum records needed to preserve continuity across ten separately generated daily chronicles and transfer work between AI providers, editors and studio production.

It does not create a new archive directory structure. All records must be stored within the episode archive's approved `01_EPISODE_CONTEXT/` and relevant story/script, graphics, generated-media, publishing and archive areas as defined by the approved Studio Blueprint/AI Desk contract.

## 2. Ownership boundaries

### Persistent franchise-level sources
Examples: approved character canon, visual canon, established technology rules, global timeline rules, reusable locations and organizational relationships. These remain in their approved canon repositories.

### Persistent CC_AI_DESK
Owns reusable AI infrastructure: persona, prompts, schemas, catalogs, indexes, retrieval configuration, permissions-aware source references, automation and operational logs. It is not the permanent home for raw episode media or episode-specific story state.

### Episode-owned records
Examples: daily chronicles, episode research, source snapshots, temporary character states, mission status, episode decisions, challenge records, derivative asset prompts, consent evidence and production status.

## 3. Identifier rules

Use the project's approved logical identifiers once confirmed. Until then, identifiers below are provisional patterns and must not be used to rename existing repository assets without approval.

- Season: `CC-S{season}`
- Chapter/phase: `CC-S{season}-CH{chapter}`
- Episode: `CC-S{season}-CH{chapter}-EP{episode}`
- Chronicle: `{episode-id}-D{day}`
- Storyline: `CC-STORY-{slug}`
- Mission: `CC-MISSION-{slug}`
- Challenge: `{chronicle-id}-CHALLENGE-01`
- Asset: `{chronicle-id}-{type}-{sequence}`
- Service Card: `{episode-id}-SERVICE-{sequence}`

Preserve legacy path labels and map them to logical IDs in metadata rather than renaming files prematurely. Resolve the existing `Sxx_TPxx_Exx` versus `SxxExx` versus `CC-Sxx-TPxx-Exx` differences through a documented decision.

## 4. Episode context package

Minimum records in the episode's approved context area:

1. `episode_manifest` — identifiers, title, phase, dates, status and authority.
2. `episode_context_snapshot` — approved premise, scope, current narrative context and source versions.
3. `calendar_probe_record` — raw/normalised endpoint response, retrieval time, production timestamp, probe timestamp, phase boundaries and derived episode-day calculation.
4. `research_register` — factual sources used in the episode.
5. `source_permission_register` — consent, licensing, retrieval eligibility, publication eligibility and revocation state.
6. `continuity_ledger` — chronological events and changing story state.
7. `challenge_register` — public questions and restricted answer keys.
8. `production_manifest` — daily chronicles and derivative assets/status.
9. `editorial_decision_log` — decisions, approvals, rejections and canon-change proposals.
10. `handover_record` — compact context for the next AI/editor.

Use the exact filenames and schemas prescribed by the current approved AI Desk/Studio architecture if they differ from these logical record names.

## 5. Episode manifest — required fields

| Field | Description |
|---|---|
| `document_id` | CC-ECLPM |
| `schema_version` | Record schema version |
| `episode_id` | Stable logical ID |
| `season_id` | Season ID |
| `chapter_id` | Chapter/phase ID |
| `episode_number` | 1–4 within chapter, if approved |
| `episode_title` | Approved title or null |
| `phase_start_iso` | Probe-sourced phase start |
| `phase_end_iso` | Probe-sourced phase end |
| `episode_start_date` | Monday |
| `episode_end_date` | Friday of second week |
| `production_timezone` | Timezone used for calendar derivation |
| `status` | Planned / Active / Awaiting Review / Complete / Archived |
| `calendar_source_ref` | Probe response record |
| `framework_version` | CC-MEGF version |
| `generation_protocol_version` | CC-DCGP version |
| `studio_blueprint_version` | Confirmed version; do not assume latest |
| `ai_desk_architecture_version` | Confirmed version |
| `editorial_owner` | Human role/reference |
| `last_updated` | ISO timestamp |

## 6. Daily chronicle record

Create one record per working day.

| Field | Description |
|---|---|
| `chronicle_id` | Stable daily ID |
| `episode_id` | Parent episode |
| `episode_day` | 1–10 |
| `chapter_working_day` | 1–40 |
| `production_date` | Actual production date |
| `weekday` | Monday–Friday |
| `production_timestamp` | Actual production timestamp |
| `probe_timestamp` | Fictional/destination timestamp |
| `phase_index` | Probe phase index if supplied |
| `status` | Draft / Awaiting Review / Approved / Rejected / Locked |
| `title` | Chronicle title |
| `storyline_ids` | Storylines advanced |
| `character_ids` | Characters appearing |
| `location_ids` | Locations used |
| `mission_ids` | Active mission references |
| `research_refs` | Source register references |
| `challenge_id` | Challenge record |
| `service_card_candidates` | Potential service card references |
| `media_asset_refs` | Derivative media |
| `previous_handover_ref` | Prior context |
| `next_handover_ref` | Handover produced |
| `editorial_decision_refs` | Decisions affecting this chronicle |

## 7. Continuity ledger

The ledger records story state, not permanent character canon.

Each event entry should include:
- Event ID.
- Chronological timestamp or story-time reference.
- Chronicle ID.
- Event summary.
- Characters involved.
- Location/temporal coordinate.
- Mission reference.
- Cause and consequence.
- Evidence/source (if factual).
- Canon classification: established / documented / real-world fact / new fictional draft / proposed / unverified.
- Approval status.
- Follow-on action.

Track at minimum:
- Character current location and condition.
- Character relationships/state changes relevant to the episode.
- Edubeam team membership and deployment status.
- Energy/device status where established canon requires it.
- Lab monitoring and communications status.
- Materialised objects/equipment.
- Discoveries and collected research.
- Decisions, risks and unresolved problems.
- Storylines opened, advanced, resolved or deferred.

Do not copy all permanent character profile data into the ledger. Reference the canon record.

## 8. Research register

For each source:
- Source ID.
- Claim/topic supported.
- Publisher/author.
- Title.
- URL or repository path.
- Publication/event date.
- Retrieval date/time.
- Source type: primary / official / reputable secondary / repository canon / endpoint.
- Geographic/temporal scope.
- Exact passage/reference used.
- Verification status.
- Confidence/limitations.
- Permission/eligibility status.
- Chronicles using the source.

Separate:
1. Contemporary real-world news.
2. Historical research.
3. Millennium probe/destination research.
4. Fictional in-universe material.
5. Bible and educational references.

## 9. Permission and consent record

Minimum states:
- `retrieval_eligible`: yes/no/unknown.
- `publication_eligible`: yes/no/unknown.
- `consent_state`: granted / limited / withdrawn / not-required / unknown.
- `license_state`: approved / restricted / expired / unknown.
- `revocation_checked_at`: timestamp.
- `source_owner`: reference.
- `evidence_ref`: record supporting state.

Unknown or withdrawn permission means do not use the material. Re-check current permission at retrieval and before publication; stale indexes cannot override current revocation.

## 10. Challenge register — restricted answer handling

Each challenge record must contain:

**Public fields**
- Challenge ID.
- Chronicle ID.
- Public question/instructions.
- Any permitted options or materials.
- Learning objective.
- Public release status.

**Restricted editorial fields**
- Correct answer.
- Explanation.
- Acceptable alternative answers.
- Source/answer verification.
- Hint(s), if approved.
- Points/reward proposal, if any.
- Scheduled solution release.
- Editorial approval.
- Access classification.

The public chronicle, comic and video end with the public question only. Never append the answer, source notes or production metadata after the challenge in public output.

Default release is with the subsequent episode. For the final episode of a chapter, the project owner must approve whether the solution accompanies a chapter wrap-up or the next chapter's first episode. Do not assume this exception.

## 11. Production manifest

Track one row per deliverable.

| Field | Description |
|---|---|
| `asset_id` | Stable asset ID |
| `episode_id` | Parent episode |
| `chronicle_id` | Source chronicle |
| `asset_type` | Text / cover / comic / image / video / audio / social / service card |
| `source_version` | Approved chronicle version |
| `prompt_ref` | Generation prompt |
| `visual_canon_refs` | Character/location reference |
| `consent_status` | Current permission |
| `license_status` | Current license |
| `generation_status` | Not Started / In Progress / Generated / Failed |
| `review_status` | Not Reviewed / Changes Required / Approved |
| `publication_status` | Not Eligible / Scheduled / Published / Withdrawn |
| `archive_ref` | Approved archive location |
| `notes` | Exceptions |

Written chronicle status should progress through:
`DRAFT → AWAITING REVIEW → APPROVED → LOCKED`.

Derivative media may only use the approved/locked narrative version unless an editor explicitly authorises a draft test. If the text changes after assets are created, mark affected assets stale and review/regenerate them.

## 12. Daily handover record

At the end of each generation, produce a compact handover containing:

1. Episode and chronicle identifiers.
2. Production date, episode day and chapter working-day index.
3. Probe/phase snapshot reference.
4. One-paragraph recap of today's events.
5. Character state changes.
6. Current locations and temporal coordinates.
7. Edubeam mission/team/equipment status.
8. Organizational role spotlight and any role follow-up.
9. Bible/Verse/H&S topics used.
10. Real-world/historical sources that affected the plot.
11. New fictional developments and their approval status.
12. Unresolved matters and continuity risks.
13. Next chronicle's useful starting context (not a predetermined plot).
14. Challenge ID and public question reference.
15. Restricted answer record reference (do not expose answer in normal handover).
16. Service Card candidates.
17. Media derivative status.
18. Editorial status and outstanding approvals.

## 13. Episode completion and manual compilation

After ten working-day chronicles exist:

- Confirm exactly ten chronicle records.
- Confirm correct chronological order and Monday-to-second-Friday coverage.
- Identify the approved version of each chronicle.
- Review character, mission, temporal and organizational continuity.
- Verify educational and research references.
- Check challenge records and solution-release schedule.
- Review derivative assets against the locked text.
- Select approximately 4–5 useful Service Card candidates where the material supports them.
- Manually compile and edit the episode.
- Obtain human editorial approval.
- Obtain consent/licensing and publication clearance.
- Publish through the approved studio process.
- Archive final masters and update episode status.

Manual compilation remains an editorial step; this specification does not authorise automatic publication or automatic canon promotion.

## 14. Service Card record

For each candidate:
- Service Card ID.
- Episode ID.
- Source chronicle.
- Title.
- Category.
- Practical value/problem addressed.
- Actionable instructions.
- Educational/source reference.
- Related challenge, if any.
- Graphic/QR/Buzz Code reference where applicable.
- Consent/license state.
- Editorial status.
- Publication status.

Target approximately four to five cards per completed episode, but quality and genuine usefulness take priority over quota.

## 15. AI handover packet — portable minimum

When moving between AI providers, provide:
- Current approved CC-MEGF.
- Current CC-DCGP.
- Current episode context snapshot.
- Latest approved chronicle.
- Latest continuity ledger extract.
- Current manifest extract.
- Relevant canon references.
- Current research/source register.
- Current permission state for any participant material.
- Probe snapshot and episode-day calculation.
- Outstanding editorial decisions.

Do not rely on the previous AI's hidden memory or assume it can access another provider's conversation. Do not send restricted challenge answers unless the receiving party is authorised to handle them.

## 16. Implementation stages

**Stage 1 — Lightweight files:** Markdown/JSON records in the existing approved episode context archive. No new database required.

**Stage 2 — Controlled indexing:** AI Desk catalog references and indexes approved records; episode archive remains authoritative.

**Stage 3 — Workflow automation:** Only after pilot evidence, automate Probe retrieval, episode-day calculation, record validation, duplicate detection, status tracking and archive checks.

**Stage 4 — Integrations:** Consider Buzzjuice, service-card activation, publishing and media workflow integrations only through approved APIs/connectors and permission boundaries.

## 17. Acceptance criteria

A pilot passes when:
- Ten daily chronicles are generated separately.
- Every chronicle has a valid calendar/probe record.
- Another AI can continue from the handover without hidden conversation context.
- Episode-specific data remains episode-owned.
- Canon is not changed without approval.
- Restricted/withdrawn material is excluded.
- Every public derivative ends with the same challenge.
- Challenge answers remain restricted until the approved release.
- Manual compilation can be completed using the records.
- Studio archive and AI Desk boundaries are respected.

**End of specification.**
