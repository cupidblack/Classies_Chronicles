# CLASSIES CHRONICLES — EPISODE CONTINUITY LEDGER & PRODUCTION HANDOVER
## Logical records, sourced state transitions, rights controls, challenge isolation and cross-provider continuity

| Control | Value |
|---|---|
| Document ID | `CC-ECLPM` |
| Version / candidate schema version | `0.04.00` |
| Canonical logical schema ID | `CC-ECLPM` |
| Prepared | 2026-11-05 |
| Status | **PROPOSED — AWAITING AUTHORIZED HUMAN EDITORIAL ADOPTION** |
| Governing integration candidate | `CC-UMP v0.04.00` — `Classies_Chronicles_Unified_Master_Prompt_v0.04.00.md` |
| Daily workflow | `CC-DCGP v0.04.00` — `CC-Daily_Chronicle_Generation_Protocol_v0.04.00.md` |
| Alignment evidence | `CC_v0.04.00_Daily_Protocol_and_Ledger_Alignment_Review.md` |
| Replaces upon authorized adoption | `CC-ECLPM v0.03.01` |
| Logical state owner | Actual current **approved episode archive**, not the persistent AI Desk |
| Physical storage authority | Current approved Studio Blueprint, access policies and human owner decisions |

**Authority boundary.** The CC-UMP controls creative requirements, chronology, the six-stage synthesis, output separation, canon and human decisions. CC-DCGP controls the daily process. This document specifies **what a truthful episode-owned record means** and how it is reconciled and handed to the next provider/editor. This proposal does **not** ratify a new storage layout, approve a schema migration, authorize publication, create private-key custody or assert any GitHub write. If the project's approved physical schema differs, preserve its approved implementation while mapping these semantics explicitly; log incompatibility rather than destroying or silently renaming records.

---

## 1. Purpose and scope of durable continuity

A two-week episode comprises up to ten separately commissioned Monday–Friday chronicles. For each day, preserve the authorized **narrative that actually exists**, the evidence that informed it, the source/rights status, the actual approval and save state, the fictional changes occurring in its world, the active Edubeam and character state, the public challenge obligation, derivative dependencies and a safe starting context for the next production day. Distinguish all of these from unapproved creative suggestions and actual Koware business facts.

The logical record system is not merely a prompt appendix. It supports **event-sourced continuity**: authenticated or clearly marked draft events are retained as history; state projections identify which accepted events determine the current story truth; superseding corrections preserve auditability. The episode archive is authoritative for that episode, and only approved promotions alter franchise-wide canon. Neither event authorship nor a model's file attachment proves editorial acceptance.

**Episode boundary:** day → episode → chapter/phase → season → permitted franchise roll-up. Carry forward only the appropriately approved state, with references back to the source episode. Do not reset deployed characters, unclosed plot threads, public-challenge release obligations or permissions simply because a calendar boundary passed.

## 2. Governance, ownership and access partition

| Custodian | Authorized content | Unsafe inference |
|---|---|---|
| Approved franchise/world/character/visual/technology canon | Durable locked characterization, powers, relationships and world laws | Any daily fiction can revise locked canon |
| Persistent `CC_AI_DESK` | Reusable prompts, schemas, catalogs, metadata indexes, automation and operational controls | The Desk owns all episode stories, missions and raw personal diaries |
| Approved `CC_EPISODE_ARCHIVES` / current episode archive | Manifest, story revisions, source snapshots, research, rights metadata, events, evolving state, handovers, approved assets | A proposed logical family authorizes a new folder, filename or migration |
| Approved Koware record owners | Real organization roles, projects, tasks, genuine completion and evidence | Fictional task success proves work was done |
| Actually access-controlled editorial vault | Challenge solutions and sensitive review details when authorization exists | A Markdown heading, ordinary chat or public repository is secure storage |
| Authorized human editor/owner | Acceptance, locks, titles, canon promotions, permissions, release and publication decisions | A model can declare approval on the editor's behalf |

**Access classifications** are `PUBLIC`, `INTERNAL` and `RESTRICTED`. Apply classification to **the record and any higher-sensitivity field**. A publicly shareable challenge question is not a permission to share its answer or a participant's private diary. Access grants and permission evidence must be checked at use time; never infer consent from a public source URL or a reachable repository. Sensitive metadata should not be included in an otherwise portable packet simply to fill a field.

**Audience destinations:** A is a separable public-eligible draft; B1–B8 is internal to authorized editorial collaborators; C exists only inside an actually controlled restricted environment. If these cannot be separated in the current medium, withhold or redact nonpublic material. Publication eligibility is distinct from authorization to inspect a source.

## 3. Record encoding, identity, versions and evidence classes

### 3.1 Semantics of each record envelope

The following are the **common logical fields**. The approved storage solution may implement them as Markdown front matter, JSON, YAML, table entries or DB columns, provided semantics and access controls remain intact.

| Field | Value and validation rule |
|---|---|
| `record_id` | Actually registered unique identifier in governed scope; a proposed ID must be marked provisional and is not evidence of an existing item |
| `record_type` | One of the 19 **master-defined** canonical families in §4, or explicitly documented legacy compatibility alias |
| `schema_id` / `schema_version` | Logical schema identity `CC-ECLPM`, candidate version `0.04.00`, or the truly approved physical schema mapping; **not** the story prompt's version |
| `episode_id` / `chronicle_id` | Approved parent references when verified; episode-level records may have `chronicle_id: null` with a reason |
| `canonical_id` / `legacy_id` / `original_path` | Existing approved identities and physical URI/path; absent ones are not fabricated |
| `record_version` / `base_revision` | Actual revision/sequence; when only preparing a draft, state not yet persisted and preserve source revision read |
| `record_status` | `DRAFT`, `AWAITING_REVIEW`, `APPROVED`, `LOCKED`, `REJECTED`, `SUPERSEDED`, or an approved mapped status, **only if evidenced** |
| `storage_status` | `DRAFTED_NOT_COMMITTED`, `COMMITTED`, or `INACCESSIBLE`; `COMMITTED` requires verified action/revision proof |
| `created_at` / `updated_at` | Real timestamps for actions that occurred, ISO 8601/RFC 3339 offset-aware; never fabricate a repository timestamp |
| `created_by` / `responsible_editor` | Actual author/agent and human responsible party when identified, distinguishing AI draft from human approver |
| `source_refs` | Actual evidence, source snapshots, prior records, signed decisions, textual canon or story revision refs |
| `classification` / `field_access` / `access_policy_ref` | Record and sensitive-field classification, recipient scope and actual policy evidence |
| `evidence_class` | One of the typed classifications in §3.2; fictional drafts cannot be verified-real-world facts |
| `change_reason` / `supersedes_record_ref` | Correction/revision rationale and exact older reference, where applicable |
| `approval_ref` / `decision_effective_at` | Real authorized human action and applicable effective period, absent until approved |
| `exception_refs` | Unresolved contradictions or evidence/permission gaps, with their statuses |

**No data placeholders:** unverified fields use real **typed** `null` (for structured representations) plus a precise status/reason; narrative packets use `UNVERIFIED`, `INACCESSIBLE`, `NOT_APPLICABLE` or `AWAITING_EDITORIAL_DECISION` with cause. These are truthful runtime states, **not** synthetic sample dates or employees. A logical contract is allowed to name fields; it must not pretend their values exist.

### 3.2 Evidence types, revisions and time

Use the approved source-specific evidence vocabulary: `APPROVED_CANON`, `PRIOR_DOCUMENTED_EVENT`, `VERIFIED_REAL_WORLD_FACT`, `HISTORICAL_INTERPRETATION`, `NEW_FICTIONAL_DRAFT`, `PROPOSED_CANON_CHANGE`, `FICTION_PROBE_SCENARIO`, `UNVERIFIED_EXCLUDED`. Where imported records use `FACT`, `DRAFT` or `APPROVED`, preserve the original and record an explicit semantic mapping rather than silently relabeling.

- **Local dates** are `YYYY-MM-DD` with an independently recorded approved production timezone (prefer approved IANA zone when available). **Instants** include their actual timezone offset. Do not compare a local requested date with the UTC date of a Probe reading as if they were the same measure.
- **Source retrieval** records actual UTC and source-local offsets where known. Store event date, publication date and retrieval date **independently**.
- **Snapshot/evidence records and continuity events** are append-only under the approved retention policy. Corrections append a new event with `supersedes_record_ref` and a reason; projections may be recalculated and revisioned.
- **Only approved, non-superseded causal events** can be promoted to accepted continuity. Draft events remain reviewable alternatives. Canon promotion is a separate human-approved action, not a field default.
- **No silent rebase:** compare `base_revision` with the latest approved ledger revision before any authorized write; on conflict, reread and reconcile or escalate. Existing filenames and `S00_T05`, `TP` and `CH` paths remain unchanged absent an approved migration.

## 4. Canonical logical record families: exact master inventory

**CC-UMP §20 defines the following 19 families.** They are **logical capabilities, not necessarily 19 separate files**. The physical implementation may combine them using approved permissions and versioning. The former `calendar_probe_record` used in v0.03.01 is treated as a **compatibility view/alias** for the B1 calendar/three-clock evidence distributed across `episode_manifest`, `episode_context_snapshot`, `source_snapshot_register` and `daily_chronicle_record`. An existing approved `calendar_probe_record` file or DB family must be preserved and mapped; it is **not** a twentieth newly mandatory master family or permission to delete legacy data.

| # | Canonical family | Scope / governing contents | Default classification |
|---:|---|---|---|
| 1 | `episode_manifest` | Approved episode identity, season/chapter, calendar/episode range, legacy mapping, owner and title state | INTERNAL |
| 2 | `episode_context_snapshot` | Effective-dated chapter/episode premise, canon and approved/draft thread context | INTERNAL |
| 3 | `source_snapshot_register` | Endpoint responses, source versions, immutable evidence/capture references and missing-field statuses | INTERNAL; RESTRICTED if necessary |
| 4 | `daily_chronicle_record` | One day, exactly one story version/revision, actual research and status links | INTERNAL until public version approved |
| 5 | `research_register` | Individual claims, actual sources, six-stage links, factual/fictional classification | INTERNAL |
| 6 | `source_permission_register` | Distinct source access, portrayal, consent, license and revocation evidence | INTERNAL/RESTRICTED |
| 7 | `role_project_log` | Chapter working-day check, aliased roles, actual work vs fictional events and proposals | INTERNAL |
| 8 | `mission_state_record` | Mission stage, roster, spatial/temporal positions, equipment, communications and retrieval | INTERNAL |
| 9 | `character_state_record` | Episode-local character knowledge, relationships, whereabouts and delta relative to canon | INTERNAL |
| 10 | `storyline_register` | Plot-thread origin, dependencies, current disposition, unresolved actions | INTERNAL |
| 11 | `continuity_event_log` | Append-only, causal, versioned story events, corrections and approvals | INTERNAL |
| 12 | `challenge_public_register` | Public challenge wording, ID, timing and opaque secure-key status **only** | INTERNAL with approved PUBLIC export |
| 13 | `challenge_answer_key` | Answer, explanations, acceptable variants and release authorization | **RESTRICTED ONLY** |
| 14 | `production_manifest` | Story/derivative type, source version, status, source rights, stale dependencies | INTERNAL |
| 15 | `service_card_register` | Optional evidence-backed actionable cards and their release approvals | INTERNAL until approved |
| 16 | `editorial_decision_log` | Human proposals/approvals/rejections, locks and canon promotions | INTERNAL; restricted fields when needed |
| 17 | `exception_conflict_register` | Missing evidence, source conflicts, severity, resolution owner and state | INTERNAL |
| 18 | `validation_report` | Evidence-linked daily/episode quality gate results and reviewer | INTERNAL |
| 19 | `handover_record` | Self-contained, permission-safe, source-linked next-day production context | INTERNAL |

`NO_CHANGE` or `NOT_APPLICABLE` may be used for an inactive family with a reason; do **not** populate phantom missions, fake episode titles, nonexistent Service Cards or false keys to achieve an artificial row count. Existing approved family names may differ: maintain an authorized compatibility table from old names to these semantics.

## 5. Episode, calendar and daily story contracts

### 5.1 `episode_manifest` and `episode_context_snapshot`

Maintain actual IDs for season, chapter/phase, episode and legacy archive; owner and approval evidence; authoritative effective-dated calendar ref; approved production timezone; full episode Monday-to-second-Friday start/end; approved phase bounds; mapping between numeric phase index and `CH`/`T`/`TP` **only if authorized**; role-check chapter index rules; 1–10 day-slot eligibility; prompt/protocol/schema versions and their individual approval states; provisional title and title status; relevant canon constraints; current story premise and approved vs unapproved goals; prior episode/season handovers; actual archive ref, update time and `base_revision`. An actual phase response may expose only some fields: absent values remain absent with status.

A context snapshot captures when its assertions became effective, prior approved events, known character/mission positions, open stories and applicable rights; tag each assertion `APPROVED`, `LOCKED`, `DRAFT`, `UNVERIFIED` or `EDITORIAL_PROPOSAL` as appropriate. Do not convert an AI reconstruction of a missing gist into a verified historical approved manifest.

### 5.2 Clock/date derivation: B1 source evidence

Record three independent axes:

1. **Clock A production** — requested local calendar date, timezone, actual execution/retrieval instant, applicable current news context.
2. **Clock B historical** — actual `historical.iso` or approved dated archival snapshot, Enka's *sourced historical-reference* location, and whether the reference is a memory/flashback rather than current physical location.
3. **Clock C Probe/destination** — actual `probe_iso` and location, in-universe mission status, future vs documented-historical classification.

Also distinguish current HQ/control base, Enka-current and each team member's physical/temporal whereabouts. These are separate attributes even when geographically equal.

Derivation per CC-UMP §8 and DCGP §5 uses an approved effective-dated calendar before any formula. Preserve phase-local start/end, first Monday anchor, target local day, whole-date elapsed count, 14-day block index, episode number 1–4 if authorized, weekend exception, chronicle 1–10, chapter working day 1–40, complete episode dates and boundary fit. The canonical ID crosswalk must be independently verified. The five nominal eight-week chapters account for only forty weeks; gaps have no inferred episode. A live Probe reading today **does not** prove an earlier requested day was in that phase.

### 5.3 `source_snapshot_register`

Every material retrieval stores actual source URL/path, source revision/commit or observed checksum if obtained, retrieval time, response status/content type, raw returned payload or approved immutable pointer, received fields and missing fields, parse validity, timezone interpretation, origin (`LIVE`, `SUPPLIED`, `CACHED`, `ARCHIVED`), license/retention/access classification and downstream claim IDs. Use one clearly pinned run snapshot for chronology; later recalibration gets a separate snapshot and event. A URL without retained revision is not equivalent to immutable evidence, and retaining a raw payload containing personal data requires separate authorization.

### 5.4 `daily_chronicle_record`

Record the actually resolved `chronicle_id`/`episode_id`, production date and weekday, episode day 1–10 and chapter working day 1–40, calendar source and proof, working title plus provisional/approved status, precise story text or approved asset revision, author/creation time, master/protocol/schema versions, six-stage evidence refs, three-clock refs and supported locations, character/mission/role state links, public challenge ID, rights/quality checks, actual draft/approval/lock/publication statuses and write evidence. Never describe a local AI-generated text as a repository-stored day record before verifying the action.

## 6. Event sourcing, character, mission, storyline and role controls

### 6.1 `continuity_event_log` — append-only causal history

Every proposed or accepted event contains: real or explicitly provisional `event_id`; parent day/episode; exact fictional-story time/clock and location where established; event summary and scene/story revision; affected characters, mission, organization or object; preceding cause and consequential change; classification (`NEW_FICTIONAL_DRAFT`, `PRIOR_DOCUMENTED_EVENT`, etc.); source refs; approval status and real editor ref if approved; predecessor/superseded event if corrected; privacy/licensing constraints; state projection impact. **Never delete earlier history solely to make the new draft look continuous.** An accepted story revision that changes an event must trigger dependent state and media review.

Projection rules: construct the **accepted** current state from approved non-superseded events in their story-time/causal order; keep unapproved deltas separately; detect contradictory simultaneous locations, duplicated day records, impossible character knowledge, impossible equipment state and unclosed retrieval. A time-travel narrative can intentionally use nonlinear scene order while the ledger still records the correct in-universe temporal positions and evidence.

### 6.2 `character_state_record`

Link each individual to the actual approved character canon file and its version, approved alias and relation to role chart where applicable, physical location/time, personal knowledge (seen/inferred/told), current motivations, relationship change, health/injury only when established in fiction and appropriate for access, obligations, usable powers at that particular era, recent actions and affected event IDs. State deltas belong to the episode record; reusable character canon only changes via explicit human promotion. Individual canon paths under `CC_AI_DESK/04_CANON/CHARACTERS/` must be actually found, not inferred from a directory listing.

For real-person-inspired figures, differentiate internal access from public portrayal rights; never turn a private family/diary statement into a compulsory public story detail. Record actual exclusions without reproducing the sensitive content in a widely shared B packet.

### 6.3 `mission_state_record`

The mission state is a revision derived from events, not a story convenience reset. Fields include actual or verified proposed mission identifier and stage (`PLANNED`, `PREPARING`, `CALIBRATING`, `DEPLOYING`, `DEPLOYED`, `INVESTIGATING`, `OUT_OF_COMMUNICATION`, `RETRIEVING`, `RETURNING`, `DEBRIEFING`, `ON_HOLD`, `CLOSED` where canon permits), roster and each member's temporal/spatial location, destination/probe reference, HQ/lab communications, equipment/energy and approved Edubeam limits, material transfers only when canon permits, findings, risks, injuries, open rescue/retrieval commitments and prior event links. An inaccessible mission ID is `UNVERIFIED`; a sourced absence can be `NO VERIFIED ACTIVE MISSION`. No automatic Thursday retrieval, Friday departure or episode reset, and no unexplained early-era Enka power upgrade.

### 6.4 `storyline_register`

For each plot thread store origin day/event, thematic or narrative purpose, involved cast, known evidence, last accepted advance, status (`OPEN`, `ADVANCED`, `RESOLVED`, `DEFERRED`, `DISPUTED`), causal dependencies, explicit promised payoff if any, deadline only when a real accepted story constraint, and next-day continuity guidance **without prescribing a future plot**. A resolved thread needs an event demonstrating resolution; an unresolved mission is not resolved by a chapter title change.

### 6.5 `role_project_log`

Record chart URI/revision and approved schedule semantics, `chapter_working_day` 1–40 rather than 1–10, scheduled role checks and actual aliases, featured roles (normally one or two, at most four under the working master unless a verified approved exception changes it), source for real tasks, scene portrayal and source/consent limits. Each action is `DOCUMENTED_ACTUAL`, `FICTIONAL_SCENE` or `PROPOSAL_FOR_REAL_REVIEW`. A character discussing a real project does not certify any corresponding actual milestone, staff activity or new management obligation.

---

## 7. Claim-level research, permissions and the six-stage link

### 7.1 `research_register`

Each **claim or selected educational insight**, not merely each website, records: stable actual/provisional claim ID; statement/topic; pass 1–6 and historical/current/probe stream; title, author/publisher, source URI and edition/revision; exact relevant section or short allowable quotation reference; geographic/temporal scope; **event date, publication date and retrieval instant separately**; primary/secondary/fictional type; evidence classification; method/corroboration; confidence and uncertainty; use rights; story passage/beat influenced; selection/rejection reason. A newspaper's publication date is not automatically the event's date. Fictional future projections have **real research inspiration refs** but cannot claim a future newspaper exists.

For the required research modes:
- **Eternal Dreamfall weekly reading:** actual 250-entry plan item plus an independently approved date/week anchor; distinguish weekly assignment from authorized daily selection; accurately classify canonical, apocryphal, pseudepigraphal, lost or fragmentary works and available editions.
- **Verse:** verified YouVersion reference/date/translation **or** named independent alternative, never false YouVersion attribution.
- **H&S:** genuine Buzzjuice course/module/lesson path, title, exact section and actual supported practice; no invented course.
- **Historical:** Clock B location/time supported by documentary reporting, distinguish fact from interpretation.
- **Current:** Clock A requested day and verified relevant local/global reporting, distinguish event from publication time.
- **Probe:** Clock C documented history if actually past; otherwise explicitly `FICTION_PROBE_SCENARIO`, not authenticated future reporting.
- **Weather/environment:** observed/archived source for factual weather; otherwise fiction, not a measurement.
- **Koware/archive/diaries:** approved records and specific permission for intended use, including real/fictive differentiation.

Legacy large headline targets and three-global/five-local synthesis belong in **internal candidate pools**, not a quota to fabricate news or force into A. Record actual omissions and rejections; preserve only appropriate evidence excerpts under license.

### 7.2 `source_permission_register`

Each relevant source/participant/asset use stores: `source_or_participant_ref`, owner or author, proposed scope (research, internal paraphrase, fictional inspiration, public portrayal, direct quotation, visual adaptation), `retrieval_eligible` (`YES`/`NO`/`UNKNOWN`), `publication_eligible` independently, `consent_state` (`GRANTED`, `LIMITED`, `WITHDRAWN`, `NOT_REQUIRED`, `UNKNOWN`), `license_state` (`APPROVED`, `RESTRICTED`, `EXPIRED`, `UNKNOWN`), actual evidence and restriction refs, checking/revocation dates, reviewer, recipient policy and next review if required. **Default exclude affected use on `UNKNOWN`, `NO`, withdrawn or unclear rights**; a public URL is not a rights grant and an accessible employee chart is not consent to depict its real staff.

Permissions are rechecked before actual publication and derivative distribution. A consent revocation produces an access/rights event and a revalidation/withdrawal review for affected assets; do not expose the revoked private content merely by describing the issue.

---

## 8. Challenge, Service Card and derivative contract

### 8.1 `challenge_public_register`

Record only actual challenge ID (or explicitly provisional generated identifier), parent day/story revision, **exact public question/options**, intended learning purpose, fairness/nonrevealing evaluation criteria, status, separately approved public hint if harmless, default **subsequent-episode** solution-release reference, chapter-final exception decision status, and an **opaque** restricted-key custody state or opaque authorized pointer. Do not store solution, near-solution, private grading rule or answer-revealing hint in this register, B sections or an ordinary provider handover.

### 8.2 `challenge_answer_key` — RESTRICTED only

Only if a **verified, authorized, access-controlled custody channel** exists: solution, explanation, acceptable alternatives, source basis, revealing hints if any, responsible editor, access permissions/logging, production/review/approval status and actual approved release trigger belong **there and nowhere else**. Do not create C in an unprotected chat or public repository. Otherwise record the nonrevealing state `RESTRICTED OUTPUT NOT CREATED; HUMAN SECURE CUSTODY REQUIRED` in B8. **Lack of secure storage alone does not prevent drafting A**; competitive release may be governed by a separately ratified requirement to have approved custody first.

An answer's default public release belongs with the **next episode's authorized release**, not the next chronicle day. Chapter-final exceptions require an actual human decision; an older answer, if separately released, must not be appended after the current A's own final challenge.

### 8.3 `production_manifest` and `service_card_register`

Track text and any separately commissioned comic, collage, video, audio, graphic or card asset with: actual asset ID, episode/day parent, type, exact **source story revision**, media/prompt version and required visual canon, approved creator/commission, permissions/licensing, creation and editor review states, intended public destination, actual storage/publication ref if verified, version/checksum when available, and **dependency-staleness** status (`CURRENT`, `STALE_REVALIDATION_REQUIRED`, `NOT_APPLICABLE`). A change to a source story, character appearance, challenge wording or accepted canon triggers revalidation of affected derivatives rather than quietly treating an earlier image as canon-compliant.

Service Cards remain **optional** practical 3–5-step evidence-backed guides. Record topic, supporting H&S/educational evidence, rights, approved content version, accessibility/safety review, release channel and actual status. Buzz Codes, QR flows, badges, 43 Clues, rewards, points, myCred/Palmier integrations and treasure hunts are **unapproved integration proposals** until independently sanctioned; writing a card does not issue a reward or track a user.

---

## 9. Editorial decisions, conflicts and validation reports

### 9.1 `editorial_decision_log`

Every decision entry states actual subject, scope, requestor, proposal or decision status, evidence, affected IDs/assets, responsible **human** approver, authorization reference and time if the decision happened, effective date and rollback/exception impact. `PENDING`, `APPROVED`, `REJECTED`, `DEFERRED` and `REQUIRES_REVISION` have different meanings; an AI-generated recommendation is always a **proposal** until ratified. Distinguish a story acceptance, locked canon promotion, privacy permission, episode title, archive migration and publication authorization as **different** decisions.

### 9.2 `exception_conflict_register`

Each exception describes the exact missing source or opposing claims (with URI/version/retrieval), affected requested day and scope, severity (`ADVISORY`, `MATERIAL`, `BLOCKING`), source-governance interpretation, `OPEN`, `DEFERRED`, `RESOLVED` or `BLOCKING` disposition, next authorized decision maker and actionable remediation. Must distinctly track: phase gap/incomplete slot; historic Probe misuse; schema/legacy-ID mismatch; locked canon conflict; diary/consent denial; insecure challenge custody; unknown Bible anchor; absent lesson; rights/derivative stale; possible duplicate day; actual concurrent ledger edit.

### 9.3 `validation_report`

Store each gate (`Q01_SCOPE` through `Q16_BOUNDARIES` from CC-DCGP §10), exact check performed, status `PASS`, `FAIL`, `BLOCKED` or `NOT_APPLICABLE`, factual evidence or reason, checker identity, real checked-at time, severity and required corrective action. `NOT_CHECKED` is distinct from `PASS` even when not explicitly recorded in a final pass/fail enum. An overall pass does not confer human approval, and a writer cannot certify unperformed source retrieval or repository writes.

---

## 10. Output B1–B8 → canonical record crosswalk

These headings reproduce **CC-UMP v0.04.00 §19** exactly; **do not** carry forward the outdated v0.03.01 B3/B7 headings as the primary labels.

| Master B heading | Required state and record correspondence |
|---|---|
| **B1. Run and temporal manifest.** | `episode_manifest`, `episode_context_snapshot`, `source_snapshot_register`, `daily_chronicle_record`; include calendar calculation/Probe compatibility view and accurate write status |
| **B2. Research/source register.** | `research_register`, `source_snapshot_register`, `source_permission_register`; claim/date/rights classification and omissions |
| **B3. Character, Koware role and project register.** | `character_state_record`, `role_project_log`, `source_permission_register`, `editorial_decision_log`; both character **and** project facts vs fiction |
| **B4. Mission and technology state.** | `mission_state_record`, `continuity_event_log`; actual mission stage and era-specific Edubeam limits |
| **B5. Append-only continuity and story ledger.** | `continuity_event_log`, `storyline_register`, `character_state_record`; events are proposed until accepted |
| **B6. Portable production handover.** | `handover_record` with source links, plus nonrevealing `challenge_public_register` status and supporting snapshots |
| **B7. Derivative/media and challenge status.** | `challenge_public_register`, `production_manifest`, `service_card_register`, `source_permission_register` and editorial decisions; **not restricted C** |
| **B8. Validation, exceptions and approval register.** | `validation_report`, `exception_conflict_register`, `editorial_decision_log`, `handover_record`; authentic QA and repo action state |

**Old-to-new mapping:** old B3 role/project details remain within new B3, augmented by canon, character and diary permission status. Old B7's permissions and editorial details are redistributed into B2/B3/B7/B8, **not lost**, while new B7 takes the master's derivative/media/challenge function. The v0.03.01 `calendar_probe_record` is supported as a legacy alias or view for B1 but **not** a new mandatory CC-UMP family. These are the primary compatibility deltas.

## 11. Portable B6 handover — minimum self-contained contract

B6 and the `handover_record` must carry **the following fifteen information elements**, using status+reason for genuine unknowns, not filled dummy examples:

1. Current **verified** season/episode/chronicle IDs, actual legacy path mapping, story revision, approved/draft/locked state, authorized owner/editor where evidenced.
2. Requested local production date, weekday, episode 1–10 day, chapter 1–40 working day, approved timezone, effective calendar ref and validation result.
3. Chosen immutable source/probe run snapshot ref, independent production/historical/destination clocks, separate HQ/current-Enka/historical-Enka/deployed-team/destination locations and actual unknowns.
4. Accurate short recap of **what the story said happened** and its causal consequences, with a story revision reference; not a prediction for tomorrow.
5. Each relevant character's confirmed whereabouts, knowledge, relationships, injury/obligations where permitted, applicable era capability restrictions and event/source refs.
6. Mission ID/state or supported absence, roster, temporal positions, lab/communications/equipment, risk and open retrieval obligations; no auto-reset.
7. Organizational alias chart version, chapter working-day check, actually featured roles and clear status of real work vs fictional portrayal/proposals.
8. Eternal Dreamfall reading week/anchor/day-selection status, verse source/date, actual H&S lesson, and essential research/permission refs.
9. Historically/currently verifiable claims versus fictional Probe scenarios, relevant source confidence, weather claims and material omitted research.
10. `OPEN`, `ADVANCED`, `RESOLVED` and `DEFERRED` storyline changes plus actual/draft event IDs and proposed canon issues.
11. Public challenge ID, exact public-question **reference** or safe wording, next-episode release gate and nonrevealing custody state **only**; no key, answer or near-answer.
12. Service Card and derivative commission/revision/stale statuses; no claim of actual media unless produced and verified.
13. Missing evidence, rights/canon/calendar conflicts, editor decisions and their genuine owners, with severity/blocker status.
14. Safe **next-working-day starting state** and constraints; identify what must not be contradicted while allowing creative freedom.
15. Actual file/save/lock/publish action state: `DRAFTED — NOT COMMITTED`, `COMMITTED` with verified evidence, or `INACCESSIBLE`; only real links and revisions.

**At day #10** additionally indicate which of the ten distinct days have actually accepted texts and which are missing or pending; do not claim the episode was compiled, the title finalized, a team retrieved or the next episode approved. A self-contained handover does **not** transfer restricted C or another provider's hidden memory.

**Cross-provider handoff set:** access-authorized versions of CC-UMP v0.04.00, CC-DCGP v0.04.00, CC-ECLPM v0.04.00; currently approved Studio/canon/manifest and date mapping; latest accepted text or correctly labeled draft; source snapshot and rights summaries; current event/state extracts; safe B6; open decision register; and public challenge reference. A receiving AI should identify missing privileges and refresh changing sources rather than treating the handover as timeless approval.

---

## 12. Reconciliation, commits and concurrency

**Prepare and validate in this order:**

1. **Read baseline**: approved current episode manifest, current accepted last-day story and corrections, record revisions, consent and open permissions, event history, materialized character/mission/storyline state and active public challenge obligations.
2. **Pin evidence**: calendar/three clocks/source snapshots from the actual run; do not replace a previous day's immutable evidence with today's live response.
3. **Create only a candidate draft**: one text A plus separate B1–B8; determine possible deltas; create restricted C only via an actually authorized custody operation.
4. **Classify all changes**: whether a proposal for real work, a new fictional event, a permitted fact, a canon-change request or an approved prior event. Never merge draft into accepted canon.
5. **Validate**: run CC-DCGP's actual gates; check chronology, source rights, role index, event causality, state transitions, missing/duplicate IDs, B6 completeness and challenge redaction.
6. **Before any authorized write**, confirm actual approved storage path, intended record classification and recipient rights, and compare the baseline revision with the current stored revision. On mismatch, halt write, reread, diff and reconcile with an authorized human.
7. **If authorized and technically available**, append immutable events and snapshots, write revised materialized state, update refs/version, verify success and log real commit/record proof. If not, preserve the reviewable local artifact with `DRAFTED — NOT COMMITTED`; a link printed in prose is not evidence of an operation.
8. **Separate human approval**: accepted text, published media, challenge release and global-canon promotions each require the actual authorized decision. Approval can occur after a draft is stored but is never inferred from the save.
9. **Recalculate dependencies**: any accepted story correction, canon/rights change or replaced public challenge marks affected derivative versions `STALE_REVALIDATION_REQUIRED` until reviewed.
10. **Deliver portable B6** and the safe record refs; preserve all open conflicts and pending next-day work.

**Correction semantics:** an error is repaired by an appended `SUPERSEDES` event, new event/revision and recalculated projection, or by the project's actually approved lawful retention process. Do not destroy evidence history or claim a correction is approved before the editor acts.

## 13. Episode completion and controlled roll-up

Only after **ten distinct, separately commissioned, accurately dated** chronicles exist may a *separately authorized* human-led compilation workflow start. Validate all ten approved/locked story revisions; reconcile dates, three clocks, event history and mission/character state; recheck privacy, permissions and research; account for ten public challenges and restricted custody/release obligations; revalidate media source versions; choose valuable optional Service Cards; obtain actual editorial sign-off; approve the final episode title; compile, publish and archive only through confirmed actions. Chapter and season roll-ups promote only approved summaries, with backlinks to episode evidence. A day-10 draft is not an automatic episode completion or permission to close a mission.

## 14. Backward compatibility, migrations and retention

- **Version lineage:** retain v0.02.00/v0.03.01 records, their original `framework_version`, source schema and original paths. Add **separate** `master_prompt_version`, `daily_protocol_version`, `schema_id` and `schema_version` metadata in a controlled mapping. Never overwrite what the old document claimed at the time.
- **B3/B7 crosswalk:** map old B3 role/project into new B3 with character coverage; map old B7 rights/editorial into B2/B3/B7/B8, and add new B7 media/challenge status without discarding legal/consent evidence.
- **Temporal alias:** preserve any existing `calendar_probe_record` as a compatibility family/view while maintaining the CC-UMP's **19 canonical** families. No silent loss of timestamp, missing-field or phase evidence.
- **Identifiers:** maintain old `S00_T05`, E01, TP/CH and approved filesystem paths. New ID templates are **proposals** until a verified crosswalk and Studio migration sign-off exists.
- **Old challenge leakage:** if an older appendix or public asset contains a solution, flag security incident/remediation for the authorized owner and **do not copy it** into a new ordinary handover. Exposure response follows actual approved security policy.
- **No storage leap:** this logical schema can be implemented through existing files, a DB or version-controlled Markdown only when approved; it does not direct GitHub changes or access-control provisioning.
- **Retention and deletions:** use applicable privacy/licensing/legal/Studio retention policy and actual access controls. Append-only story history is subordinate to legitimate erasure/retention obligations, managed by authorized custodians, not by this prompt.

## 15. Acceptance and negative test scenarios

A candidate is **operationally acceptable** only when the following can be demonstrated using real authorized evidence rather than simulated assertions:

| Test group | Positive result | Required negative case |
|---|---|---|
| Calendar and time | Dates, approved phase fit, 1–10 and 1–40 mapping and all three clocks verified independently | Weekend, midweek phase start, phase gap, partial episode, midnight offset, retrospective date/live Probe mismatch |
| Existing identities | Both approved actual IDs and legacy archive path preserved | Missing crosswalk, duplicate day, attempted unauthorized rename |
| Six-stage claims | Genuine reading/verse/course and dated historical/current evidence; future only labeled fiction | Unapproved weekly anchor, lost-text quote, false YouVersion fallback, fabricated future news |
| Canon and roles | Approved power limit, current chart and intact character knowledge/mission roster | Unauthorized Enka capability, wrong check day, unexplained retrieval/reset |
| Rights | Access and public permission checked separately, revocation reflected | Identifiable private diary published, consent withdrawn after draft |
| Events/state | Approved event projection traceable with correction provenance | Draft event treated as approved; concurrently edited ledger overwritten |
| Challenge | Public question last, only opaque key status in B, restricted key stored only with proof | Solution/near-answer leakage; missing secure store mislabeled as secure; premature answer release |
| Media | Derivatives bound to source revision and canon | Changed story with unchanged comic falsely marked current |
| Daily outputs | Exactly one A; complete separate B1–B8; portable B6; real state labels | Invented ID/snapshot/commit/approval; B appended to public file |
| Episode compilation | Separate human authorization and ten accepted day slots | Day 10 auto-published, non-approved title made canonical |

A successful dry-run is **not** adoption. An approved pilot requires its own authenticated authority, test evidence and applicable storage/rights decision.

## 16. Outstanding editorial and implementation decisions

Carry each as an actual `editorial_decision_log` proposal with an authorized owner, not an assumed resolution:

1. Approved production timezone, effective phase boundaries, forty-week gaps, Foundation Phase and future season calendar.
2. Mapping among Probe `phase_index`, chapter, `CH`/`T`/`TP`, logical episode numbers and existing `S00_T05` archive paths.
3. Current Studio Blueprint version, physical schema approval, repository write authority and immutable snapshot storage/retention policy.
4. The Eternal Dreamfall 250-week date anchor, daily selection procedure and fragmented/lost-text editorial approach.
5. Current organizational chart/check-day semantics, alias rights, publication permissions and character canon paths/approval.
6. Edubeam mechanics, Enka capability gates and mission-state exception approvals.
7. Restricted solution vault, custody and release approvals; special chapter/season-final answer scheduling.
8. Real-world diary/work participant rights, licenses, revocation process and provider-to-provider data permissions.
9. Optional comic/video/Service Card/reward integration, media runtime and any external product-security approval.
10. Human acceptance, locking, source-version audit, conflict-resolution and controlled deployment/pilot authority for this v0.04.00 document bundle.

**END — CC-ECLPM v0.04.00 (proposed). No repository write, approval or secure-key storage is claimed.**
