# CLASSIES CHRONICLES — EPISODE CONTINUITY LEDGER & PRODUCTION HANDOVER
## Episode-owned record contract, daily state transitions, provenance and cross-provider handover

| Control | Value |
|---|---|
| Document ID | **CC-ECLPM** |
| Version | **0.03.01** |
| Status | **PROPOSED — AWAITING HUMAN EDITORIAL REVIEW AND APPROVAL** |
| Document type | Episode-owned records and continuity/handover specification |
| Governing integration candidate | **CC-SMDP v0.03.01** — Structured Master Prompt |
| Daily execution companion | **CC-DCGP v0.03.01** — Daily Chronicle Generation Protocol |
| Replaces upon approval | CC-ECLPM v0.02.00 |
| Review baseline | CC-SMDP v0.03.01; CC-SMDP-REVIEW v0.03.01; CC-DCGP v0.02.00; CC-ECLPM v0.02.00 |
| Prepared | 2026-11-03 |
| Authoritative storage | Current approved **episode archive** under the approved Studio Blueprint; never the persistent AI Desk by default |

> **Status and authority:** CC-SMDP v0.03.01 and these companion updates are **proposals**, not proof of a ratified governance change. Preserve existing approved record names, paths and permissions until the project owner authorizes the mapping/migration. This document defines a complete *logical contract*, not a command to create new repository directories, publish records or disclose restricted editorial keys.

---

## 1. Objective and scope

Maintain a trustworthy, portable and auditable source of **episode-specific truth** across ten separately commissioned Monday–Friday chronicles in two consecutive weeks. Preserve what each narrative actually said, distinguish approved canon from draft fiction, track the evolving Edubeam/character/organization state, protect source rights, document research and challenge controls, and hand the next writer/editor precisely enough context to continue without access to previous providers' hidden memories.

This document governs **how records are prepared, validated, classified and handed over**, not how stories are authored. The writing workflow is **CC-DCGP v0.03.01**; the master contract for scope, calendars, research/canon and outputs is **CC-SMDP v0.03.01**. A single daily run may prepare candidate updates but does not automatically commit them to a repository, approve them, merge them into permanent canon, generate comics or publish anything.

**Unit boundaries:** daily chronicle → ten-day episode → chapter/phase → annual season → provisional franchise-level continuity index. Only approved records cross a boundary as established fact. An episode archive remains authoritative for that episode; approved franchise canon remains authoritative for global rules.

## 2. Ownership, authority and storage

| Owner | Intended contents | Prohibited assumption |
|---|---|---|
| Approved **franchise canon** sources | Locked reusable character profiles, visual identity, technology limits, relationships, timeline/locations | A draft daily ledger can rewrite canon |
| Persistent **`CC_AI_DESK`** | Reusable prompts, schemas, indexes, source catalogs, retrieval rules, tooling and operational logs | The Desk is the only archive for daily stories, raw media or episode state |
| **Current episode archive** | Manifest, daily stories, immutable source/Probe snapshots, research and permissions, event deltas, temporary states, production manifests, handovers, editorial decisions and approved derivatives | An arbitrary new folder/schema may be created without Studio authorization |
| Restricted **editorial channel** | Challenge answer keys and other protected records, with access logging and authorized release | A normal appendix, unprotected chat, public file or ordinary handover is restricted storage |
| Human **editor/owner** | Acceptance, locks, canon promotions, consent/licensing and challenge/episode release decisions | Model-generated status labels establish human approvals |

Existing approved episode locations, potentially including `01_EPISODE_CONTEXT/` and approved story, graphic, media, publishing and archive areas, must be verified against the **actual** Studio Blueprint. The names in this specification are logical record families—not presumed concrete filenames. Preserve legacy path variants such as `S00_T05` and mapping metadata, rather than renaming assets to meet a proposed ID pattern. Do not store sensitive raw content in a public GitHub repository merely because the repository is convenient.

## 3. Record-format conventions and common envelope

### 3.1 Machine-portability rules

Recommended lightweight implementation: Markdown for readable handovers and a structured JSON/YAML representation where the **approved** architecture allows. Either format must preserve the same field semantics. Do not claim to have an actual schema validator unless one was run. Every factual value must come from evidence, an authorized human decision, or an unmistakably marked fictional draft.

- **Timestamps:** RFC 3339/ISO 8601 date-times with explicit offset when available. Normalize separately to UTC as useful, but **retain** the source's original timezone/offset. Production local dates use `YYYY-MM-DD` and a separately recorded approved IANA timezone or governing fixed offset.
- **Dates vs instants:** A local `production_date` is not interchangeable with a Probe `probe_iso` instant or a historical `historical_iso`. Record independent timezone context for each axis.
- **Unknown:** Use a real typed `null` plus an explanatory `value_status` of `UNVERIFIED`, `INACCESSIBLE`, `AWAITING_EDITORIAL_DECISION` or `NOT_APPLICABLE`, if represented structurally. In Markdown use the same exact states with a reason. Never silently invent sample date/ID/name values.
- **Identifiers:** Stable, unique in their appropriate scope. Store legacy IDs/path aliases and approved logical mapping separately. A provisional pattern describes a type—not an asserted real episode record.
- **Links and provenance:** Relative archive references are permitted only once an actual approved archive path exists. Record full source URI, repository path/revision and/or immutable snapshot reference when known. An unverified URL/title is not a verification result.
- **Revisions:** Every mutable *record revision* has a recorded version/change reason. **Events and immutable evidence snapshots are append-only**; corrections create new events that explicitly supersede earlier erroneous interpretations, never erase the old source history without a lawful retention decision.
- **Evidence classification:** Required values are `APPROVED_CANON`, `PRIOR_DOCUMENTED_EVENT`, `VERIFIED_REAL_WORLD_FACT`, `HISTORICAL_INTERPRETATION`, `NEW_FICTIONAL_DRAFT`, `PROPOSED_CANON_CHANGE`, `FICTION_PROBE_SCENARIO` and `UNVERIFIED_EXCLUDED`; other approved enumerations may be mapped, not freely improvised.
- **Access classification:** `PUBLIC`, `INTERNAL` or `RESTRICTED` with required `recipient_permissions`. The classification attaches to the **record and to sensitive subfields**; a public question does not render its answer public.

### 3.2 Common envelope

Every stored logical item should be attributable through these standard fields (or their approved schema equivalents):

| Field | Required semantic contract |
|---|---|
| `record_id` | Persistent unique ID within governed scope; not generated arbitrarily for an existing item |
| `record_type` | One of the named families in §5 or approved mapped schema |
| `schema_id`, `schema_version` | ECLPM/approved record schema identity and version; **do not confuse** with story prompt version |
| `episode_id` | Parent episode when episode-scoped; preserve actual approved ID/path mapping |
| `chronicle_id` | Parent day when day-scoped; null/`NOT_APPLICABLE` at episode level |
| `record_version` | Version or sequence number under approved policy |
| `status` | Actual enumerated draft/review/approval/access state relevant to this family |
| `created_at`, `updated_at` | Actual action times; no fabricated save timestamps |
| `created_by`, `responsible_editor` | Verified actor or role reference; AI draft creator distinguished from approving human |
| `source_refs` | Evidence, source snapshots, canon and parent records referenced |
| `classification`, `access_policy_ref` | Public/internal/restricted controls and authorization evidence |
| `change_reason`, `supersedes_record_ref` | Provenance for corrections/new revisions where applicable |

These fields are a **contract for actual records**, not permission to populate a completed sample with guessed data. For draft-only chat output, report `NOT STORED` and omit false archive references.

## 4. Identifiers, calendar and three-clock evidence

### 4.1 Identifier governance

The master defines **provisional** patterns: `CC-S{season}`, `CC-S{season}-CH{chapter}`, `CC-S{season}-CH{chapter}-EP{episode}`, `{episode-id}-D{day}`, `CC-STORY-{slug}`, `CC-MISSION-{slug}`, `{chronicle-id}-CHALLENGE-01`, `{chronicle-id}-{asset-type}-{sequence}` and `{episode-id}-SERVICE-{sequence}`. Resolve actual IDs through approved manifests/crosswalks. Store canonical ID, legacy ID, original path, mapping authority, mapping status and any naming conflicts. The presence of a `T05`, `TP` or `CH` suffix is **not** itself proof of a phase, number or date. Never rewrite existing links before a human-ratified migration.

### 4.2 Calendar derivation rules

Store the approved calendar record, or the validated phase snapshot and the deterministic result from **CC-SMDP §9 / CC-DCGP §5**:

- `phase_start_date_local`, `phase_end_date_local` and approved `production_timezone` must be determined from valid effective-dated sources.
- `anchor = first Monday on or after phase start`.
- `elapsed_days = target local date − anchor`, requiring a nonnegative count.
- `episode_number = floor(elapsed_days/14)+1`, within approved episode slots 1–4.
- `day_in_block = elapsed_days mod 14`; `5,6,12,13` are weekends.
- `episode_day = day_in_block+1` for `0…4`; `episode_day = day_in_block−1` for `7…11`.
- `chapter_working_day = 10×(episode_number−1)+episode_day`; valid 1–40.
- `episode_start_date = anchor+14×(episode_number−1)`; `episode_end_date = episode_start_date+11` days, a Friday of the second week. Confirm a complete valid episode within approved bounds.

Five approximate eight-week phases are **not a full 52-week calendar**. Inter-phase gaps, short phases, historical Foundation Phase mappings, incomplete fourth episodes and requested older dates without contemporaneous calendar evidence are recorded as exceptions, not automatically forced into a day. The current live Probe snapshot is **not** retroactive proof of a different day's phase.

### 4.3 Three-clock and location snapshot

Each day must link to an immutable temporal record with (A) requested/current **production date and timezone**, (B) **historical reference** timestamp and verified Enka historical whereabouts, (C) **Probe/destination** timestamp and mission location, plus the separate current HQ/base and member-specific positions. Probe metadata such as `now_iso`, `probe_iso`, `phase_index`, phase labels and bounds, `amplitude_days` or `probe_value_days` is stored **only if actually returned**. Capture source URI, retrieval time, payload format, whether live/supplied/cached, exact raw or approved immutable snapshot ref, validation status and absent-field notes. One pinned snapshot governs the day unless an explicitly recorded later recalibration is approved/used.

## 5. Minimum logical episode record families

These are all **required capabilities** for a ten-day pilot; physical file counts/names may differ under the approved Studio schema.

| Logical family | Scope | Required purpose | Typical access |
|---|---|---|---|
| `episode_manifest` | Episode | IDs, calendar, version sources, owner, title/status, approved storage refs | Internal |
| `episode_context_snapshot` | Episode/revision | Premise, current arcs, locked/draft scope and sourced canon | Internal |
| `calendar_probe_record` | Daily snapshot | Three clocks, payload, calendar algorithm, status and locations | Internal |
| `source_snapshot_register` | Source/run | Actual source revision/fetch and immutable evidence pointer | Internal or restricted |
| `daily_chronicle_record` | Day | Story version, day slot, research/continuity links and editorial state | Internal until approved |
| `research_register` | Source/claim | Claim-by-claim dated evidence, educational sources, research selections | Internal |
| `source_permission_register` | Source/participant | Access, consent, license, revocation and usage conditions | Internal or restricted |
| `role_project_log` | Day | Chapter role-check day, verified roles and actual-vs-fictional activities | Internal |
| `mission_state_record` | Mission/revision | Roster, deployment, communications, equipment, temporal coordinates | Internal |
| `character_state_record` | Character/day revision | Current episode state *delta*, reference to approved global canon | Internal |
| `storyline_register` | Episode/thread | Open/advanced/resolved/deferred plots and causal follow-ups | Internal |
| `continuity_event_log` | Event (append-only) | Chronological, sourced story changes and consequences | Internal |
| `challenge_public_register` | Day | Public wording, release status and restricted record *opaque ref* | Internal (public fields exportable) |
| `challenge_answer_key` | Day/secure | Actual solution, verification, alternatives, approved release | **Restricted only** |
| `production_manifest` | Asset/version | Text, comic/video/audio/card versions, stale/review/publication states | Internal |
| `service_card_register` | Candidate/card | Practical instructions and episode source, rights/approval/status | Internal until approved |
| `editorial_decision_log` | Decision (append-only) | Human approvals, rejections, canon proposals, policy exceptions | Internal/restricted |
| `exception_conflict_register` | Exception | Competing claims, missing evidence, decision/impact/blocker | Internal |
| `validation_report` | Daily/episode | Actual gate results with evidence and responsible reviewer | Internal |
| `handover_record` | Day | Portable next-day context with no hidden chat dependency | Internal, redacted as needed |

If a family is genuinely not applicable on a specific day (e.g., no active Edubeam mission or no Service Card candidate), record a truthful `NOT_APPLICABLE` or `NO_CHANGE` reason in the day's handover; do not fabricate a mission or card to satisfy a schema.

## 6. Episode manifest and context snapshot

### 6.1 `episode_manifest`

Minimum fields and constraints:

| Field | Meaning / validation |
|---|---|
| `episode_id`, `season_id`, `chapter_id` | Approved actual IDs and legacy path crosswalk |
| `episode_number`, `phase_index` | 1–4 if approved; source-specific phase value if actually observed (do not equate unverified numbers) |
| `episode_start_date`, `episode_end_date` | Monday to second Friday, full approved phase fit |
| `production_timezone` | Approved local zone/offset used in derivations |
| `phase_start_iso`, `phase_end_iso` | Original source fields where supplied; unresolved when absent |
| `calendar_authority_ref`, `probe_snapshot_refs` | Effective-dated calendar decision and actual snapshot sources |
| `episode_title`, `title_status` | Proposed/approved/null; title may be finalized after day ten |
| `status` | `PLANNED`, `ACTIVE`, `AWAITING_REVIEW`, `COMPLETE`, `ARCHIVED` with actual approving action |
| `master_prompt_version`, `daily_protocol_version`, `ledger_schema_version` | CC-SMDP v0.03.01; CC-DCGP v0.03.01; CC-ECLPM v0.03.01 *as actually used*, with proposed/approved status noted |
| `studio_blueprint_version`, `ai_desk_architecture_version` | Verified current approved versions, else unknown with explanation |
| `editorial_owner`, `approval_refs`, `last_updated` | Actual roles/decisions/timestamps; no fictitious completion |

### 6.2 `episode_context_snapshot`

Record snapshot/revision ID, manifest ref, effective date, approved premise, chapter/season threads, current story focus, known historical/current/probe locations as applicable, character/mission/canon references, current open plots, previous day/episode handovers, planned boundaries and permissions constraints. Clearly tag each statement `APPROVED`, `LOCKED`, `DRAFT`, `UNVERIFIED` or `EDITORIAL_PROPOSAL`. For day 1 there may be no prior daily chronicle in this episode; bridge from an actual approved previous episode or an explicitly approved opening premise.

## 7. Daily chronicle record and public asset boundary

A `daily_chronicle_record` contains:

- `chronicle_id`, `episode_id`, actual `production_date` and `weekday`, `episode_day` 1–10, `chapter_working_day` 1–40, and computed calendar source/ref.
- `master_prompt_version`, `generation_protocol_version`, `schema_version`, generation actor, actual generation/retrieval timestamps and authorization scope.
- Independent `historical_timestamp`, `probe_timestamp` and all referenced location sets with evidence/status.
- Original daily title and title status, **exact public story text version** or actual approved story-asset ref, and a deterministic version relation (e.g., revision ID/hash **only if calculated**).
- `status`: `DRAFT`, `AWAITING_REVIEW`, `APPROVED`, `LOCKED`, or a documented `REJECTED`/`WITHDRAWN` branch. An AI cannot self-transition to `APPROVED`/`LOCKED`.
- References to source/research IDs, character/missions/storyline IDs, event deltas, public challenge, handover, editorial decisions, source permissions and associated media versions.
- `previous_chronicle_ref` and `previous_handover_ref` when these actually exist; if prior text is draft-only, say so.

A story in an **internal archive** can include metadata around it; the **publicly exported story asset** must end with **only its public audience challenge**. Neither the internal B1–B8 appendix nor the restricted key may appear after that challenge in the public export. In an unprotected interface, do not combine all three outputs into a file that might be published unchanged.

## 8. Append-only continuity events, current state and Edubeam mission

### 8.1 `continuity_event_log`

Create one event for each **material** new fictional occurrence, sourced factual reference that influences the plot, editorial correction, relationship change, mission change or open/closed storyline. Each event must include:

| Field | Contract |
|---|---|
| `event_id` | Stable episode-scoped unique event ID |
| `chronicle_id`, `episode_id` | Proven parent; story occurrence can refer to earlier day with correction trace |
| `story_timestamp`, `time_axis` | Narrative time/date plus `PRODUCTION`, `HISTORICAL`, `PROBE` or `IN_UNIVERSE_UNRESOLVED`; not an unsupported real-world timestamp |
| `location_ref`, `character_refs`, `mission_ref` | Sourced current episode identities/positions |
| `summary`, `cause`, `consequence` | Clear causal change, not general thematic description |
| `classification`, `approval_status` | Approved canon, earlier recorded, draft fiction, real-world fact, proposed change, scenario or unverified; human approval separate |
| `research_refs`, `source_snapshot_refs` | Evidence for external claims or preceding narrative |
| `thread_ids`, `follow_up` | Open/resolved effects, conditions, next safe story state |
| `supersedes_event_id`, `correction_reason` | New corrective event, not silent historical overwrite |

**Append-only means** do not delete/replace an old event when new information contradicts it. Add a superseding correction or later story event; rebuild the *derived latest state* from approved/draft-qualified history. Do not silently treat a draft event as a universal canonical fact.

### 8.2 `character_state_record` and `storyline_register`

For each featured character, track approved canon ref, currently evidenced physical/time location, health/welfare condition **in-story**, knowledge, skills/capability gates, relationships, obligations and changed possessions, plus source event IDs and review status. Track plots by ID, purpose, open/advanced/resolved/deferred state, constraints, last event and next unresolved question. Keep personal and sensitive real-world facts separate/permission-controlled; the fictional character record is not a health or personnel database. Never duplicate an entire permanent profile or create new powers without a proposed-canon-change decision.

### 8.3 `mission_state_record`

Minimum: real approved/provisional mission ID, stage (e.g., preparing/deployed/out of communication/retrieving/debriefing/on hold), roster/individual current story location and temporal coordinates, destination time, communications with the lab, energy/battery/plasma *only as established canon permits*, equipment/materialized objects, approved operating limitations, objectives, findings, risks, impediments, pending return/retrieval, responsible characters and last event. A missing mission ID is `UNVERIFIED`, not an excuse to create one. A missing team member is not automatically returned home by the next chapter; unresolved deployment survives day boundaries. Distinguish technical story proposals from approved Edubeam laws. Respect the specific **S00E01** early-capability restrictions in the working Enka/Cupid Black canon.

### 8.4 `role_project_log`

Record the verified organizational chart/aliased-checks version, **chapter working day**, scheduled check alias/role, actually featured role(s) (normally 1–2, maximum 4 unless approved otherwise), permission evidence, reference to an actual Koware work/project source, and a three-way action classification: `DOCUMENTED_ACTUAL`, `FICTIONAL_SCENE`, `PROPOSAL_FOR_REAL_REVIEW`. Do not log a fictional inspection as a real completed audit or an AI-suggested deadline as an actual business commitment.

## 9. Research register and source snapshots

The `research_register` associates **individual claims/learning selections** with dated sources. Each entry requires an ID; supported claim/topic; source author/publisher; actual title and URL/path; type (endpoint, approved canon, primary, official, secondary, course, Bible/ancient text, news, etc.); source revision where known; local geographic/temporal scope; **event date, publication date and retrieval timestamp distinctly**; exact relevant passage/section reference; verification method and confidence/limitations; rights status; chronicles that used it; and a classification such as `FACT`, `HISTORICAL_INTERPRETATION`, `FICTION_PROBE_SCENARIO`, `NEW_FICTIONAL_DRAFT` or `UNVERIFIED_EXCLUDED`.

Organize source references by the six-stage synthesis and three temporal streams:

1. **Eternal Dreamfall:** verified reading-plan week and *separately approved calendar anchor*, canonical classification of the listed work, genuine available passage, `OFFICIAL_DAILY_ASSIGNMENT` versus `EDITORIAL_DAILY_SELECTION` status, copyright handling.
2. **Verse:** actual YouVersion date/reference/translation or clearly labeled independent alternative; never copy an earlier verse under today's YouVersion attribution.
3. **Health & Safety:** actual Buzzjuice course/module/lesson title, repository path, section and useful verified guidance.
4. **Historical:** Enka's sourced historical time/place, event evidence and interpretive limitations.
5. **Current:** requested actual production date, relevant verified HQ/character locations, dated event reporting, publication date and source diversity.
6. **Probe:** mission time/place, authentic dated evidence if past/present, or a clearly fictional **future/alternate** scenario without false news attribution.
7. **Weather and environment:** measured/official when available; unsupported weather is only a plainly fictional scene detail, never a sourced observation.
8. **Koware/diary/archives:** approved role, project and continuity records; retrieval/publication eligibility and concrete usage purpose.

Store headline candidate pools and editorial decisions *internally*: location-specific up-to-10, collective up-to-20, global-awareness approximately 5–10, and the optional three-global/five-local interstream selection. These are **research targets, not fabricated report quotas**, and the public story includes only meaningful selected details. The `source_snapshot_register` records exact retrieved content revision/commit, endpoint payload or checksum **only if actually captured**, retrieval time, access classification, verification status and applicable consent constraints. A live URL alone does not prove content at generation time or authorize permanent reproduction.

## 10. Permissions, consent and rights

The `source_permission_register` is separate from research relevance. Minimum fields:

| Field | Allowed interpretation |
|---|---|
| `source_or_participant_ref`, `owner_ref`, `scope_of_use` | Whose material, for what retrieval, adaptation and publication purpose |
| `retrieval_eligible` | `YES`, `NO`, `UNKNOWN` — current permission to access |
| `publication_eligible` | `YES`, `NO`, `UNKNOWN` — distinct permission to publish/depict |
| `consent_state` | `GRANTED`, `LIMITED`, `WITHDRAWN`, `NOT_REQUIRED`, `UNKNOWN` |
| `license_state` | `APPROVED`, `RESTRICTED`, `EXPIRED`, `UNKNOWN` |
| `evidence_ref`, `restriction_details` | Actual consent/license proof and limitations; never invented |
| `checked_at`, `revocation_checked_at`, `next_review_due` | Actual verifications, with stale-check warning as needed |
| `access_policy_ref`, `editorial_owner` | Who can see private notes/answer records and authorize release |

**Default deny on uncertainty:** `UNKNOWN`, `NO`, withdrawn consent or inappropriate license blocks retrieval/publication of the affected item for that purpose; access to a repository is not automatic public-reuse permission. When a participant is identifiable in a sensitive personnel/diary context, do not transcribe or indirectly expose the details in a wide-shared handover. Revocation checks apply before retrieval and before actual publication. A stale AI Desk index does not override a fresh withdrawal.

A real person's name in an organization chart or diary is not permission to portray them in a fictional misconduct scene. Fictionalized substitutes must not be falsely described as real employees. For Bible, H&S and news sources, cite claims and use brief lawful extracts or paraphrase, not large reproductions.

## 11. Challenge records: public index vs restricted answer

### 11.1 `challenge_public_register`

Contains only challenge ID, parent chronicle, **exact public wording/options**, fair-answer criteria description *that does not reveal the key*, intended learning objective, provisional planned **subsequent episode** solution-release reference, current publication/release status, approved public hint if nonrevealing, and an **opaque** restricted-key record reference/status. This register must be safe to share with authorized production collaborators; when sharing publicly, export only approved fields.

### 11.2 `challenge_answer_key` — **restricted exclusively**

Contains the solution, explanation, acceptable alternatives, evidence/source, hint strategy (including any potentially answer-revealing hints), editor, access policy, review/approval state, scheduled release, chapter-final exception and any rewards/game proposals. The record must have actual restricted-channel authorization and storage; a label `RESTRICTED` on an unprotected response/file does not secure it. Never place a key or answer-revealing metadata in B1–B8, the normal handover or public comic/video/audio.

If no authorized storage mechanism is available, maintain only `RESTRICTED ANSWER RECORD — SECURE STORAGE REQUIRED` in B8 and the public index. **Do not generate or persist a solution in the routine output.** A challenge must be designed for fairness, and its solution must be verified through approved restricted review before publication/competition if required.

**Release timing:** default is release with the **next episode**, not next day's chronicle. A final-chapter challenge requires a recorded human decision whether the answer belongs to a chapter wrap-up or the next chapter's first episode. A released answer is a separately approved publication unit; the *current* chronicle and all its derivatives still end with **their own final public challenge**.

## 12. Production manifest and dependency invalidation

Store one `production_manifest` item per actual or planned deliverable: `asset_id`, `episode_id`, `chronicle_id`, `asset_type` (`TEXT`, `COVER`, `COMIC`, `IMAGE`, `VIDEO`, `AUDIO`, `SOCIAL`, `SERVICE_CARD` or approved extension), **source story version/revision**, prompt/version, visual/canon refs, actual permission/license state, `generation_status`, `review_status`, `publication_status`, destination/archive ref when real, approved editor/action ref, timestamps and exceptions.

**Narrative states:** `DRAFT → AWAITING_REVIEW → APPROVED → LOCKED` by authorized human transition. Rejection/withdrawal are documented branch statuses; a model's draft text is never its own proof of approval. **Asset generation:** `NOT_STARTED`, `IN_PROGRESS`, `GENERATED`, `FAILED`. **Review:** `NOT_REVIEWED`, `CHANGES_REQUIRED`, `APPROVED`. **Publication:** `NOT_ELIGIBLE`, `SCHEDULED`, `PUBLISHED`, `WITHDRAWN`.

**Dependencies:** A derivative's story version, challenge wording, character visual refs, scene order, rights and lore must match the **approved/locked** narrative source unless a human expressly authorized a clearly labeled draft test. A later story edit, canon revision, rights withdrawal or challenge amendment invalidates the dependent asset's current approval. Mark `STALE — REVIEW/REGENERATION REQUIRED` and record which dependency changed. Do not publish stale media or claim the underlying text was immutable if it changed.

**Comics/video:** Generate **only after separate authorization**. For a commissioned comic, every requested page must advance the story; respect specified 9:16 portrait/no printed scene numbers, original visual style, approved character appearance, exact story order and the **identical audience challenge on the final public page only**. For video, ensure timings actually sum to the target; a possible 160-second adaptation is 20 eight-second acts arranged 7/7/6, not three scenes totaling 120–128 seconds. For audio, the final public beat is likewise the challenge.

## 13. Service Cards and optional engagement integrations

A `service_card_register` entry requires a real candidate/card ID and source chronicle, episode ID, title/category, practical problem, concise safe actionable guidance (typically three to five steps when appropriate), evidence/education ref, challenge linkage where genuinely relevant, graphic/QR/Buzz Code *only if authorized and real*, consent/license status, editor and release status. **Approximately four or five useful candidates per completed episode** is an editorial target; do not manufacture cards to meet it.

The earlier proposals for **43 Clues**, Buzzjuice/myCred/Palmier scoring, QR/Buzz Codes, treasure hunts, badges and rewards remain optional designs, not deployed capabilities. Track candidate/approval states only. No real award, transaction, notification, collection of participation data, external API integration or publicly advertised prize is implied by the record.

## 14. Editorial decisions, conflicts and validation evidence

The `editorial_decision_log` must distinguish:

- **Proposals:** requested change and rationale, governing section, author, evidence, affected IDs/assets and status `PENDING`.
- **Decisions:** human approver/role, decision timestamp, authority/approval reference, disposition `APPROVED`, `REJECTED`, `DEFERRED` or `REQUIRES_REVISION`, and effective scope/date.
- **Canon promotions:** separate explicit authorization for upgrading a draft story proposition to franchise-level canon, with global canon owner notified/updated only when a real action occurs.

The `exception_conflict_register` must include two or more contradictory claims when applicable, exact document refs/versions, source retrieval evidence, affected run/episode, applicability/precedence rationale, severity (`ADVISORY`, `MATERIAL`, `BLOCKING`), current disposition and required human action. Follow approved governance only within its scope. Missing primary calendar provenance, insecure answer storage, unapproved major character ability, conflicting Edubeam mission state, a revoked consent and missing archive mappings are **distinct** issues and cannot be hidden inside a generic “all good” note.

The `validation_report` stores each daily gate from **CC-DCGP §13** and master **CC-SMDP §25**, actual check performed and its result (`PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`), factual evidence or reason, responsible checker and timestamp when real. A check not performed is **not PASS**. Review may be delegated, but the model does not self-grant approval.

## 15. Output B1–B8 mapping and daily append workflow

### 15.1 Crosswalk

CC-SMDP §20 requires a **separate internal appendix** with eight sections. Map them to ledger ownership as follows:

| Master output | Episode-owned records to create/update (or draft only) |
|---|---|
| **B1 — Generation/temporal** | Episode manifest ref, calendar/Probe snapshot, source snapshot, daily chronicle metadata |
| **B2 — Research** | Research register, selected/rejected news pool refs, permission refs, snapshot refs |
| **B3 — Roles/projects** | Role/project log, organizational source ref, editorial proposed-action status |
| **B4 — Mission** | Mission state revision with event-based changes and no auto-reset |
| **B5 — Continuity** | Append-only event deltas, character-state deltas, storyline changes |
| **B6 — Handover** | Portable next-day handover, public challenge ID, opaque secure-key ref only |
| **B7 — Rights/production/editorial** | Permission checks, production versions/statuses, human decisions/proposals |
| **B8 — Exceptions/QA** | Conflict/exception register, quality gate results, real write status |

### 15.2 Reconciliation transaction

When a daily generation is authorized:

1. Read actual approved episode manifest, context, prior chronicle, latest current ledger, mission/character/storyline states, permissions and decisions. Record source versions.
2. Pin or inspect verified temporal evidence; derive calendar position **without overwriting** a prior day's source snapshot. Record request date versus live retrieval date.
3. Prepare one Output A draft and Output B1–B8; if authorized secure storage exists, write Output C through its restricted process, never in shared B.
4. Identify **deltas**: new event IDs, updated derived states, role/project observations, new sources/permissions, changed challenge/public status, media dependencies and unresolved issues.
5. Validate IDs, timestamps, story chronology, source permissions, factual classifications, challenge separation, prior-state transitions and all required B sections.
6. **If repository write access actually exists and the operation is authorized:** confirm approved paths, check latest versions/concurrency, append new immutable events/snapshots, update materialized state pointers with a real revision and evidence of success. If not, mark **`DRAFTED — NOT COMMITTED`** and provide the ready-to-review artifact/ref, never an invented save path.
7. Have an authorized human review the draft and record actual accept/reject/lock decisions; only then update editorial state and downstream media eligibility.
8. Issue a **portable B6 handover** pointing to what was **actually** accepted and what remains draft, unresolved, unpublished or blocked.

**Concurrency rule:** If another collaborator altered the source ledger or story revision during drafting, do not silently overwrite. Re-read the latest revision, compare changes, record conflict and reconcile through the authorized editor. If a record is corrected, preserve the original and a superseding event with reasons.

## 16. Daily handover record: minimum portable packet

The `handover_record` must contain, in a compact, **self-contained but source-linked** form:

1. Actual episode/chronicle IDs and any **approved** legacy path mapping; output/version/status and reviewer.
2. Requested production date, weekday, `episode_day` 1–10, `chapter_working_day` 1–40, approved timezone and calendar derivation ref.
3. Immutable pinned Probe snapshot ref and independently sourced historical, production and destination times/locations; clearly separate missing evidence.
4. A concise **today's actual story** recap with causal outcomes, not an invented future episode plot.
5. Character states and changes, location/temporal coordinates, relationships, knowledge and applicable capability restrictions with prior event links.
6. Mission objective/stage, team roster and temporal positions, energy/communications/equipment and unresolved risks or return commitments; `NO_ACTIVE_MISSION` only if sourced.
7. Organizational chart version, **chapter-day** check, role spotlight(s), source-backed real project context versus fictional scene/proposed follow-up.
8. Eternal Dreamfall selected week/passage status, actually verified verse or named alternative, verified H&S lesson and key research refs (not bulk copyrighted material).
9. Real historical/current facts versus fictional Probe scenario and their effect on plot; research and permission warnings.
10. Open/advanced/resolved storylines, event IDs added, new fictional ideas, proposed canon changes and human approvals outstanding.
11. Challenge ID and *exact approved/draft public question reference*, scheduled next-episode release and **opaque secure-key ref/status only**; no solution, answer-revealing hint or protected field.
12. Service Card candidates/actual status; derivatives commissioned, source versions and `STALE` or review flags.
13. Outstanding conflicts, calendar/rights blockers, incomplete research, next required evidence and owner if known.
14. A **safe starting context** for the next working day: what characters know, what remains unresolved, where they actually are, and what must not be contradicted; **not** a mandated plot or a claim the next chronicle has been written.
15. Current record storage status: `DRAFTED — NOT COMMITTED`, `COMMITTED` with actual evidence, or `INACCESSIBLE`, and precise artifact refs only when real.

If the episode day is 10, also mark the episode-compilation readiness and open items without automatically claiming episode completion or field-team retrieval.

### 16.1 Cross-provider minimum transfer set

For a receiving provider/editor, give access-approved versions/references of: **CC-SMDP v0.03.01**, **CC-DCGP v0.03.01**, **CC-ECLPM v0.03.01** (with their proposed/approved status), current approved episode context/manifest, latest approved chronicle (or qualified draft), latest continuity/mission extracts, B6 handover, source/permission register, pinned Probe/calendar snapshot, visual/character canon needed for the work, open conflict/decision register, and active challenge **public record only**. Never rely on a past model's hidden memory; never transmit restricted answer keys to an unauthorized provider.

## 17. Episode completion, manual compilation and roll-up

After **ten separately commissioned and produced** working-day chronicles exist, a human-led separate task may:

1. Verify the ten **distinct** day slots in chronological Monday–second-Friday order and the effective phase/calendar evidence; detect duplicates or missing days.
2. Identify approved/locked story revision of each day; reconcile immutable event history, character/Edubeam state and research provenance across both weeks.
3. Recheck source rights, consent/revocation, approved real-world claims, reading/verse/H&S provenance and all outstanding editorial exceptions.
4. Verify ten public challenges, restricted answer custody, next-episode release obligations and chapter-final exception where needed.
5. Reconcile derivative assets against their source revisions and approved visual canon; block stale or unlicensed media.
6. Select approximately 4–5 genuinely valuable Service Card candidates if present and editorially appropriate.
7. Manually assemble/edit the episode, obtain authorized human sign-off, finalize the **episode title after day ten** if approved, then publish and archive only through actual authorized actions.
8. Create **approved** chapter/season/franchise-level continuity references and retain backward links; do not copy entire raw episode archives into the persistent AI Desk.

The **chapter title**, season-level title, official franchise-level ledger name, phase-gap scheduling and legacy logical ID naming remain editorial/governance questions. The mere existence of ten drafts is **not** proof of an approved, compiled, locked, published episode.

## 18. Change management, migration and retention

- **Non-destructive upgrade:** retain v0.02.00 records and field semantics until approved conversion; add a field alias/crosswalk with `source_field`, `target_field`, compatibility, approval and migration status. `framework_version` in an old manifest is not silently set to the new master version: record original values and the new `master_prompt_version` separately.
- **IDs and directories:** preserve existing archive paths and original filenames. A renaming or path restructure requires approved Studio migration design with redirects/mappings and tested dependent references.
- **Legacy challenge data:** if an old appendix stored answers in ordinary content, mark a **security remediation** task; move or redact through an authorized process, audit exposures and don't redistribute the unsafe record as a handover.
- **Episode state:** produce event-based corrections and retain source/version history; publishable narrative changes require revalidation of derivatives and permissions.
- **Retention:** follow actual Studio privacy, licensing, audit and legal retention requirements when known. This prompt does not authorize indefinite storage of personal material or an unapproved purge.

### 18.1 Specific v0.02.00 → v0.03.01 adjustments

| Old behavior or risk | v0.03.01 rule |
|---|---|
| `framework_version` may ambiguously refer to the older CC-MEGF | Record explicit `master_prompt_version` + daily protocol + ledger schema versions; retain old framework metadata for provenance |
| A normal appendix might carry a section titled “Restricted challenge record” with solution | Ordinary B contains only ID/status/opaque ref; solution exists solely as separately authorized C |
| Probe snapshot may be treated as a live universal source for any date | Pin retrieval and effective dates; historical requested days need valid dated calendar authority |
| Generic canon/event classification blurs approved fact and new fiction | Typed evidence classifications, draft state, superseding corrections and explicit human promotion |
| Read-only prompts sometimes assert an archive update | Distinguish `DRAFTED — NOT COMMITTED` versus a verified authorized write |
| Old identifier patterns look like real paths | Crosswalk to legacy paths; no unauthorized rename/migration |
| Derived comic assets can become silently outdated | Explicit source-version dependency and `STALE` invalidation |
| Source permissions are bundled with sources | Independent access vs publication eligibility and revocation checks |
| Historical/probe/current research can be conflated | Three clocks and historical/current/Probe source classifications |
| Studio document version/canon authority is assumed | Verify explicit approved Blueprint/AI Desk versions and specific episode capability gates |

## 19. Acceptance tests and failure cases

A controlled single-episode pilot is acceptable **only if the actual evidence exists** for all of the following:

- Ten daily chronicles were generated **separately** and recorded with distinct verified working days, not fabricated as one run.
- Each has a real requested-date/Probe/calendar evidence record, timezone, three-clock status, phase/day calculation or approved exception, and correctly identified legacy/canonical mapping.
- All external educational/current/historical claims are verified and classified; unsupported or fictional Probe material is never relabeled as real news.
- The latest approved story state can be reconstructed from event logs and actual approvals; draft events never rewrite locked global canon.
- Active Edubeam missions, roster, equipment and known positions survive day and episode transitions without unexplained resets or invented capabilities.
- Real-world staff/diary material is eligible for the stated purpose, with current rights/revocation review and no privacy leakage.
- Each public chronicle ends with its challenge; derivative media use the same challenge at the final public beat and have accurate source/version references.
- **No challenge answer** appears in public story, routine B sections or cross-provider packet; each actual key is in verified restricted storage or marked explicitly not stored.
- A receiving AI/editor can continue coherently from a portable packet without another provider's chat memory.
- All real record writes, approvals, publications and media generations have evidence; unperformed actions are only described as proposed/pending.
- Manual episode compilation is possible using ten approved text versions and related sources, with chapter/season carryover references only as approved.
- Studio/AI Desk/archive ownership is respected and no unauthorized directory migration or real external integration occurred.

**Negative scenarios to explicitly test:** weekend request; phase beginning midweek; a fourth episode that falls outside the phase; non-phase gap; live endpoint absent/rejected; historical date with only current Probe result; a timestamp crossing local midnight; a Probe destination in the future; duplicate day IDs; concurrent ledger edits; withdrawn permission; key accidentally placed in appendix; new S00E01 power inconsistent with character canon; derivative made stale by a story correction; missing final chapter solution-release approval; inability to save to the archive.

## 20. Open approval decisions carried forward

This specification intentionally **does not** claim these issues were resolved by an AI rewrite. Carry them in the `editorial_decision_log` with an authorized owner:

1. Final calendar/season terminology and exact effective phase boundaries, including inter-phase and Foundation Phase mapping.
2. Canonical identifiers/legacy path contract and the currently approved Studio Blueprint and AI Desk architecture versions.
3. Eternal Dreamfall date/week anchor, 250-week/five-year gap, daily-passage selection and treatment of missing/fragmentary works.
4. Edubeam mechanics/Enka capability progression; candidate technology laws and unapproved transfer thresholds.
5. Exact comic/video delivery defaults beyond explicitly commissioned briefs; audiovisual duration approvals and source-lock requirements.
6. Answer key restricted storage mechanism, access roles, next-episode release operation and final-chapter exceptions.
7. Consent/licensing and public depiction of identifiable staff, authorized diaries and institutional references.
8. Chapter/season title finalization, franchise-level continuity index name/ownership and cross-episode canon promotion rules.
9. Service Cards, 43 Clues, Buzz Codes, rewards, calendar/task integrations and any automation or public data collection.

---

## References and compatibility sources

1. **CC-SMDP v0.03.01**, especially §§3–10, 11–16, 19–27: https://raw.githubusercontent.com/cupidblack/Classies_Chronicles/refs/heads/main/CC_AI_DESK/CC_Structured_Master_Prompt_v0.03.01.md
2. **CC-SMDP-REVIEW v0.03.01**, existing conflict/approval decisions: https://raw.githubusercontent.com/cupidblack/Classies_Chronicles/refs/heads/main/CC_AI_DESK/CC_v0.03.01_Refactor_Review_and_Decision_Log.md
3. **CC-DCGP v0.02.00**, superseded daily protocol after approval: https://raw.githubusercontent.com/cupidblack/Classies_Chronicles/refs/heads/main/CC_AI_DESK/CC-Daily_Chronicle_Generation_Protocol_v0.02.00.md
4. **CC-ECLPM v0.02.00**, source records specification: https://raw.githubusercontent.com/cupidblack/Classies_Chronicles/refs/heads/main/CC_AI_DESK/CC-Episode_Continuity_Ledger-Production_Handover_v0.02.00.md
5. **CC-DCGP v0.03.01**, proposed synchronized daily run protocol (companion document delivered with this specification).

**Document end — CC-ECLPM v0.03.01 (proposed).**
