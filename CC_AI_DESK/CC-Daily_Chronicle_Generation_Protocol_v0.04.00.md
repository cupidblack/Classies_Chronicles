# CLASSIES CHRONICLES — DAILY CHRONICLE GENERATION PROTOCOL
## Controlled execution runbook for one researched chronicle and its safe production handover

| Control | Value |
|---|---|
| Document ID | `CC-DCGP` |
| Version | `0.04.00` |
| Prepared | 2026-11-05 |
| Status | **PROPOSED — AWAITING AUTHORIZED HUMAN EDITORIAL ADOPTION** |
| Governing integration candidate | `CC-UMP v0.04.00` — `Classies_Chronicles_Unified_Master_Prompt_v0.04.00.md` |
| Record contract | `CC-ECLPM v0.04.00` — `CC-Episode_Continuity_Ledger-Production_Handover_v0.04.00.md` |
| Alignment evidence | `CC_v0.04.00_Daily_Protocol_and_Ledger_Alignment_Review.md` |
| Prior companion | `CC-DCGP v0.03.01` (superseded **only if** this version is adopted) |
| Run unit | Exactly one authorized production working day, ordinarily one of ten in a two-week episode |
| Intended operator | Human editor, approved automation or AI provider operating with the permissions actually available |

**Authority and version rule.** This runbook operationalizes, but does not amend, the CC-UMP. The currently **approved** Studio Blueprint, canon, privacy restrictions and editorial decisions remain controlling within their authorized scopes. The presence of v0.04.00 in a repository is not itself evidence of adoption. When the owner asks to test the proposed bundle, identify it as the **requested working baseline**, not as an approved replacement. On conflict, obey the applicable higher authority, register the conflict, and stop only when the conflict is material. Do not mistake a review or refactor request for a commission to generate a chronicle.

**Execution principle:** *One eligible day → one verified evidence set → one integrated Output A → distinct internal B1–B8 → optional genuinely restricted C → truthful review and handover status*. No automatic archive writes, additional days, comic pages, videos, rewards, business actions, answer releases or publication.

---

## 1. Purpose, boundaries and run-state model

The CC-UMP is the policy and creative contract; **this file prescribes the sequence, checks, intermediate artifacts and stopping decisions**. The CC-ECLPM defines the durable record semantics and security of the resulting episode data. Do not restate a modified version of the master's creative or calendar rules here; use the governing sections identified below.

### 1.1 Classify the requested operation

| Mode | Execution rule |
|---|---|
| `REVIEW_ONLY` | Inspect or revise documentation. **Do not** produce a chronicle or alter canon. |
| `DAILY_GENERATION` | Run the complete protocol for one eligible production working day. |
| `SPECIAL_WEEKEND` | Require a separate explicit editorial commission; never consume a standard episode-day slot by default. |
| `COMPILATION` | Separate approved ten-day episode assembly; **not** a daily run. |
| `DERIVATIVE` | Separate comic, audio, video, collage or Service Card order; use approved current derivative rules. |
| `OTHER` | Respond within the expressly requested scope; do not infer story-production authorization. |

A weekday request is not automatically date-eligible. A date must be assigned by an approved effective-dated calendar or a computation **explicitly authorized by that calendar**. A weekend, phase gap, invalid partial episode, missing prerequisite or conflicting locked state is an exception to report, not an invented chapter.

### 1.2 Run states and transitions

| State | Entry / exit condition | Next action |
|---|---|---|
| `REQUEST_CLASSIFIED` | Scope, requested date and operating mode understood | Check governance, authorized inputs and permissions |
| `PREFLIGHT` | Source inventory and previous state read or accurately marked inaccessible | Determine material blockers |
| `BLOCKED` | Essential authority, date, canon, permission or mandatory evidence unresolved | Issue precise blocker report; no definitive Output A |
| `GO_WITH_OMISSIONS` | Essential requirements met; optional inputs unavailable | Log omissions and continue |
| `GO` | Essential requirements verified | Pin temporal evidence and resolve chronology |
| `EVIDENCE_LOCKED_FOR_DRAFT` | Exact run snapshots, date mapping and sources identified | Reconcile continuity, conduct research |
| `DRAFTED` | One candidate A and separately classified B assembled | Validate, correct, mark editorial status |
| `AWAITING_EDITORIAL_REVIEW` | QA results and actual storage status communicated | No self-approval or publication |
| `APPROVED` / `LOCKED` | Only an evidenced authorized human decision | Downstream use only within explicit permissions |
| `COMMITTED` | Only an authorized, verified repository/record operation | Record URI/revision/action evidence; not equivalent to approval |

`DRAFTED`, `COMMITTED`, `APPROVED`, `LOCKED` and `PUBLISHED` are different dimensions, not automatic steps in a single ascending ladder. A draft can be stored without approval; approval does not prove storage; neither proves publication.

### 1.3 Output partition

**Output A — public-eligible literary draft.** A self-contained, original daily chronicle. Its **final public element** is the audience challenge; there is no appended technical note or solution. The file may still require human acceptance before publication.

**Output B — internal production and episode handover.** Eight ordered sections, **B1 through B8**, with source-backed metadata, deltas and a portable B6. Never append this packet to the publishable A file. In an editorial chat, show it only where the recipient is authorized; otherwise use genuinely separate files or withhold sensitive details.

**Output C — restricted challenge solution.** Create only with explicit authorization and verified access-controlled storage. An ordinary chat, public repository, Markdown heading or file named “restricted” is **not** proof of restricted custody. If custody is unavailable, do not generate or retain a solution in ordinary outputs; register `RESTRICTED OUTPUT NOT CREATED; HUMAN SECURE CUSTODY REQUIRED` in B8 and a nonrevealing key status in B7. **This is not by itself a block on drafting A**; an actual release/competition policy may separately require secure-key review before publication.

---

## 2. Phase 0 — determine authority and authorize the run

**Inputs to seek:** explicit user commission; local requested date or “today”; approved production timezone; approved season/chapter/episode calendar and manifest; approved Studio Blueprint and AI Desk architecture; applicable locked character/technology canon; prior accepted chronicle and current episode handover; version and approval status of CC-UMP, CC-DCGP and CC-ECLPM.

**Procedure:**
1. Resolve whether the user requests a story or only an analysis, framework revision, comic or compilation. If not `DAILY_GENERATION`, exit this workflow.
2. Identify the actual editor/owner authority behind the commission and the authorized input/output surfaces. An explicit instruction to draft does not grant rights to private diaries, real-person portrayal, unrelated systems or repository writes.
3. Confirm the requested **local** production date. For “today,” use the actually current date in the **approved** production timezone; if that timezone is not established and materially affects assignment, request authoritative calendar/timezone evidence or issue `BLOCKED` rather than silently assuming a zone.
4. Pin the governing versions and effective approval status. Prefer actual approved governance over a proposed newer version. If specifically asked to use the v0.04.00 candidate, flag `WORKING BASELINE — NOT RATIFIED` unless human ratification is evidenced.
5. Check that the required output partition can be enforced. If not, supply only a non-sensitive A and a status note in separate surfaces; avoid transferring unredacted B through an unauthorized channel.

**Phase output:** run scope and authority record; source-access checklist; a draft-only status. **Stop** if scope or essential authority cannot be established.

## 3. Phase 1 — source inventory and preflight gate

The operator **actually retrieves** applicable documents; knowing a URL is not evidence its content was accessed. Record URI/path, source owner, version or immutable revision if available, retrieved-at timestamp and timezone, request-date applicability, actual access state, permission for the intended use and an evidence note. A missing source may be replaced only by a **separately authenticated and permitted** equivalent.

### 3.1 Required source acquisition matrix

| Source / record | Why inspected | What to record when missing |
|---|---|---|
| Approved calendar, season/chapter/episode manifest and ID crosswalk | Determine target day, full episode span and legacy archive identity | `BLOCKING` if correct episode assignment cannot otherwise be verified |
| Approved Studio governance and applicable locked character/Edubeam canon | Ensure a lawful, continuous narrative | `BLOCKING` if a central canon decision cannot be reconciled |
| Previous approved chronicle, last B6 and current episode event/mission/character state | Avoid contradictory world state or reset deployment | Record precise gap; block only if essential to the requested story |
| Accessible and authorized character canon, organizational aliases/check chart and Koware project material | Character, role and business integrity | Omit unsupported role/project claim; block a compulsory role if its identity is unresolved |
| Rights, consent, current access and publication checks | Protect real persons, private diaries and licenses | Exclude affected material; block if central and irreplaceable |
| Effective-dated reading-plan mapping plus actual reading-list item | Eternal Dreamfall weekly selection | Do not invent week/day; block if expressly mandatory and irreplaceable |
| Dated verse provider / attributed fallback | Distinguish YouVersion from independent alternative | Mark provider, date and limitations; block only if required centrally |
| Actual Buzzjuice H&S course/module/lesson | Document actual practical teaching | Do not invent module; block if lesson required centrally |
| Live or approved pinned Probe, historical endpoint and valid calendar evidence | Separate three clocks and research dates | Record failure and temporal limits; live failure alone is not proof of incorrect calendar |
| Historical/current reporting; weather/conditions when used | Support actual claims and avoid false future news | Omit nonessential claims; record source shortfall |
| Existing challenge public obligations and restricted-key **status only** | Avoid duplicate, premature or revealing answers | Do not inspect keys without explicit authorization |
| Derivative manifests and current locked story version | Avoid stale adaptations | Mark not applicable if no derivative commissioned |

The original master provides relevant source addresses in §§7, 15–17; use the versions actually available rather than claiming the repository remains unchanged.

### 3.2 Go/no-go decision

- **`GO`:** date/episode position and core canon are valid; required central source material and publication eligibility for the proposed public portrayal are established.
- **`GO_WITH_OMISSIONS`:** only nonessential weather, news, optional diary, ancillary verse, side character or game/Service Card input is missing; omit or attribute a valid alternative; disclose in B2/B8.
- **`BLOCKED — SOURCE OR APPROVAL REQUIRED`:** the authoritative calendar/date/episode number is unresolved; central locked canon contradicts itself; an essential real person's use/consent is invalid; or an explicitly required central reading, verse or H&S source cannot be obtained after reasonable, lawful retrieval attempts.

A block report states the requested date, exact unverified dependency, locations actually checked, relevant competing claims, risk of fabrication, and concrete editorial evidence/decision required. It must **not** fill the gap with plausible fiction while presenting the result as a completed chronicle. An authorized **provisional nonpublishable fiction exercise** may be separately produced when safe, visibly labeled outside public A.

---

## 4. Phase 2 — pin independent temporal evidence

Follow CC-UMP §§6–8. Store Clock A (production local date/time and actual retrieval), Clock B (historical reference from an authentic dated source), Clock C (Probe/destination from the actual source) **independently**. Keep separate actual/supported HQ, Enka-current, Enka-historical, mission destination and individual deployed-team locations. An unknown location is `UNVERIFIED`; it is not automatically New Legon, Las Vegas or wherever a previous story happened.

**Interfaces to attempt where within scope:**
- Primary Probe: `https://buzzjuice.net/shared/millennium-timezone/millennium-probe.php?probe=now`
- Historical reference: `https://buzzjuice.net/shared/millennium-timezone/millennium-timezone.php?endpoint=historical`
- Probe supplement: `https://buzzjuice.net/shared/millennium-timezone/millennium-timezone.php?endpoint=probe`

For each actual request, register the endpoint, retrieval instant with timezone, request outcome and parse result, returned fields, omitted fields, raw payload or immutable authorized reference, source offset, normalized timestamps, freshness and evidence classification (`LIVE`, `SUPPLIED`, `CACHED`, `ARCHIVED`, `INACCESSIBLE`). An old user-supplied payload remains **supplied historical evidence** even if its contents resemble a live response. Do not substitute the current `phase_index` for an effective-dated historical chapter assignment. Preserve **one chosen snapshot** governing this draft; later changes require a separately logged recalibration rather than silently blending timestamps.

**Phase output:** B1 temporal evidence and source snapshot entries; any missing-field exception. Historical B and destination C can be unknown without turning A's date into those clocks; do not claim source-verified developments for unknown temporal anchors.

## 5. Phase 3 — resolve calendar day, episode and IDs

**First:** use the exact date-to-episode entry from an approved effective-dated manifest and its official identifiers. **Only when its terms expressly authorize the four-episode/eight-week derivation**, and phase start/end instants and timezone are verified, perform the following calculation from CC-UMP §8:

```text
local_phase_start = calendar_date(phase_start_instant in approved_production_timezone)
local_phase_end   = calendar_date(phase_end_instant in approved_production_timezone)
anchor            = first Monday on or after local_phase_start
elapsed_days      = target_local_date - anchor, measured in whole calendar dates
episode_number    = floor(elapsed_days / 14) + 1
block_day         = elapsed_days mod 14
block_day 0–4     → chronicle_number = block_day + 1
block_day 7–11    → chronicle_number = block_day - 1
block_day 5,6,12,13 → weekend, no regular chronicle
chapter_working_day = 10 × (episode_number - 1) + chronicle_number
episode_start     = anchor + 14 × (episode_number - 1) calendar days
episode_end       = episode_start + 11 calendar days
```

**Validation:** target must fall in the approved effective phase; `elapsed_days ≥ 0`; calculated episode must occupy an **approved complete slot 1–4**; episode start must be Monday and end second Friday; **the full two-week span including the intervening weekend** must fit the authorized phase's exact local/instant boundary policy; `chronicle_number` is 1–10 and `chapter_working_day` is 1–40. Calendar dates, not elapsed 24-hour intervals, govern chapter-day math; DST or midnight offsets must not silently change the day. An explicit manifest entry outranks the optional derived formula within its approved scope.

**Identifier integrity:** resolve season/chapter/episode/chronicle through an actual approved manifest and physical path crosswalk. The observed Probe `phase_index` does not prove `CH`, `T`, `TP` or `S00_T05`. Preserve existing legacy paths and names; no bulk rename and no invented ID masquerading as an existing file. Store unknown mapping with reason; a blocking missing parent identity is escalated.

**Special cases:** an unallocated inter-phase week, midweek phase start, incomplete fourth episode, historic request with only a **current** Probe reading, weekend, duplicate day or nonexistent manifest all require explicit treatment. Never create an automatic fill episode. Day 10 is not itself permission to compile or close the episode.

**Phase output:** dated calendar calculation and approved crosswalk (B1), any role-check chapter-day result (B3), and validation disposition (B8).

## 6. Phase 4 — reconcile approved continuity before imagining new events

Read the actual latest **approved/locked** preceding day first; qualified drafts and later approved corrections must be visibly labeled. Reconstruct the episode state from the approved event stream and actual character/mission revisions, **not** from hidden AI conversational memory.

Prepare a compact internal state-of-play:
1. Episode premise, prior accepted plot events and open/deferred/resolved threads, with causal consequences.
2. Active characters, real-versus-fictional identity, role, relationship, knowledge and ability gates; what they personally witnessed versus only heard about.
3. Mission state, team roster, HQ and field temporal/location positions, Edubeam calibration, communications, equipment, risk and retrieval obligations. If none verified, record `NO VERIFIED ACTIVE MISSION` only when genuinely supported.
4. Aliased-check chart revision and **chapter working-day 1–40**, not episode day 1–10; the chart's apparent 20-day repeat is not binding until verified. Normally spotlight one or two pertinent roles and never exceed the current approved maximum (the working master defaults to four).
5. Verified Koware projects/tasks versus `FICTIONAL_SCENE` or `PROPOSAL_FOR_REAL_REVIEW`; no fabricated staff audit or actual business accomplishment.
6. Character canon path, specific era/episode limits (including early Enka capabilities when applicable), verified depiction permissions and any proposed canon change kept **unapproved**.

**Phase output:** baseline state references; constraints for drafting; proposed rather than committed corrections if a prior record is wrong.

## 7. Phase 5 — execute six cumulative research/editorial passes

Use **one integrated narrative**, not six public retellings. Each pass adds a compact provenance-to-story linkage in B2 and B5 where relevant. CC-UMP §§15–17 defines substantive research standards and the full stage meaning.

| Pass | Required operational action | Evidence to log | Improper shortcut |
|---|---|---|---|
| **1 — Eternal Dreamfall Bible Study** | Verify the actual 250-entry weekly reading list **and separately approved date-to-week anchor**; find a genuine passage or correctly characterize lost/fragmentary literature | Listed work/week, authorized day choice, tradition/classification, text source and edition, thematic relevance | Invent a 251st week, daily reading or exact passage from a lost work |
| **2 — Eternal Dreamfall Chronicle** | Check the requested date's actual YouVersion verse or identify an independently sourced alternative accurately | Provider, requested vs provider date, verse reference, translation when known, attribution status | Present an unrelated fallback as verified YouVersion for that date |
| **3 — Refreshed Eternal Dreamfall** | Inspect a genuine Buzzjuice H&S course outline and actual module/lesson relevant to the plot | Exact lesson title/path/section and actual supported guidance | Invent accredited safety rules or lesson numbers |
| **4 — Headlined Eternal Dreamfall** | Research historical, current and destination streams separately; verify date, place and event vs publication date | Selected/rejected candidates; `VERIFIED_REAL_WORLD_FACT`, `HISTORICAL_INTERPRETATION` or `FICTION_PROBE_SCENARIO`; source quality and weather status | Fabricate headline counts or pretend the future has confirmed news |
| **5 — Classies Eternal Dreamfall** | Reconcile approved archives, consent-eligible diaries, relationship progress and unresolved story state | Relevant chronicle/event/character refs, usage permission and new causal requirements | Convert a private diary into publishable fact or erase a deployed team |
| **6 — Classies Chronicles** | Build an original story linking verified research, Koware life, roles, ethical stakes and technology within canon | Final story source refs and explicit fictional innovations vs actual activity | Mistake invented scenes for completed real-world work |

The legacy research maxima (up to ten local, up to twenty collective, five–ten global-awareness, optional three-global/five-local synthesis) are **editorial search targets only**; fewer relevant and well-supported selections are preferable to invented quotas. For future/alternate Probe dates, mark extrapolations as fiction, not archived journalism. Do not make confidential CV content a required source, and do not copy large protected works.

**Phase output:** internally selected motifs and claims, evidence/permissions register (B2), constraints for B3/B4/B5; an explicit gap record for every expected-but-missing central source.

## 8. Phase 6 — plan and produce Output A

Prepare a **private outline**, not another public deliverable, containing: resolved calendar day; scene setting and time; viewpoint; one driving need or choice; source-backed/canon constraints; at least one clear causal escalation; the credible consequence; the character's changed knowledge or relationship; a coherent ending; one fair audience challenge anchored in accessible public narrative content. The daily title remains provisional pending the relevant editorial approval.

Write a vivid, culturally grounded, original chronicle aimed ordinarily at approximately **3–5 minutes of reading** (editor may adjust). Let prayer, literature, history, contemporary awareness, a real safety insight, role/project life and Edubeam intrigue contribute naturally **where verified and applicable**. Do not force all seven routines or news items into disconnected paragraphs. Do not show the six production stage names, source table, internal ID calculations, privacy details, telemetry debugging, restricted content or editorial notes in public A. Never imply a fictional operation, forecast or mission report is a verified real business outcome.

**Absolute terminal rule:** the audience challenge is the **last public-facing element** of A. A separate public source-credit asset may be approved but must not be appended after the current story's challenge. A solution-revealing hint is forbidden in A and ordinary B. Write A into a separable public-eligible document, not a file containing B or C.

## 9. Phase 7 — prepare Output B, matching CC-UMP §19 exactly

Use the eight **new master** labels below. This mapping supersedes the old protocol's B3 “Koware role/project spotlight” and B7 “Permissions, production & editorial” headings; **none of their legitimate contents is discarded**. CC-ECLPM §10 (v0.04.00) specifies durable record crosswalks.

| Section: exact master heading | Minimum contents | Record ownership |
|---|---|---|
| **B1. Run and temporal manifest.** | Actual request/run date/time/timezone; three clocks; supported location sets; source snapshot and missing fields; official calendar/derivation, phase fit, identifiers and legacy path; actual versions/approval and repository state | `episode_manifest`, `episode_context_snapshot`, `source_snapshot_register`, `daily_chronicle_record` |
| **B2. Research/source register.** | Claim-level evidence, distinct event/publication/retrieval dates, study/week/anchor status, verse provider, exact H&S lesson, factual vs fictional history/current/probe streams, optional omissions, rights summary | `research_register`, `source_snapshot_register`, `source_permission_register` |
| **B3. Character, Koware role and project register.** | Character-specific canon, current character/diary consent, chapter-day check, chart revision, aliases and featured roles, actual project evidence, fictional work and proposed business follow-up distinctly labeled | `character_state_record`, `role_project_log`, `source_permission_register`, `editorial_decision_log` |
| **B4. Mission and technology state.** | Mission/roster/locations/times, actual applicable Edubeam limits, lab/energy/communications/equipment, findings, injuries, unresolved retrieval; `NO VERIFIED ACTIVE MISSION` only when supported | `mission_state_record`, `continuity_event_log` |
| **B5. Append-only continuity and story ledger.** | Append-only proposed event deltas, consequences and affected state, relationships/knowledge, open/advanced/resolved/deferred arcs, statuses and human canon proposals | `continuity_event_log`, `character_state_record`, `storyline_register` |
| **B6. Portable production handover.** | Safe standalone story recap, verified chronology and refs, character/mission/role state, unresolved threads, nonrevealing challenge reference/status, remaining decisions, next-day constraints and actual save status | `handover_record`, `challenge_public_register`, `source_snapshot_register` |
| **B7. Derivative/media and challenge status.** | Challenge **public wording**/ID, next-episode release gate, opaque restricted-key status, Service Card options, versioned comic/video/audio/graphic dependencies, stale state, actual commissioning/production; applicable permissions and editor state | `challenge_public_register`, `production_manifest`, `service_card_register`, `source_permission_register`, `editorial_decision_log` |
| **B8. Validation, exceptions and approval register.** | Evidence-backed gate results, failures and omissions, source/rights/canon conflicts, owners, approval/release limits, exact operations performed, `DRAFTED — NOT COMMITTED` when applicable, restricted custody issue | `validation_report`, `exception_conflict_register`, `editorial_decision_log`, `handover_record` |

Use actual values where verified. For unresolved fields, use **explicit statuses with causes** (`UNVERIFIED`, `INACCESSIBLE`, `NOT_APPLICABLE`, `AWAITING_EDITORIAL_DECISION`); use JSON `null` only where type-compatible and paired with an explanatory status. Do not seed fake IDs, timestamps, mission members, approvals, writes or diary rights. The absence of a change is `NO_CHANGE` with a reason, not a fictitious event.

### 9.1 Challenge key / Output C gate

A challenge must be fair, answerable using public story content or a clearly permitted public learning reference, and stored publicly only as its **wording and nonrevealing metadata**. Default answer-release opportunity is the **subsequent episode**, not the next daily chronicle. The final episode of a chapter requires an owner-approved exception if an ordinary next episode is absent. Actual solution, explanation, permissible variants and revealing hints belong **only** in authorized restricted Output C. If that store is absent, the secure-key status remains `SECURE STORAGE REQUIRED`; never print the key in the normal reply or a portable B6. Before competitive publication, enforce any separately approved release requirement for a verified answer key.

---

## 10. Phase 8 — quality gates, disposition and handover

Run and record each check; a check **not performed** must never be marked `PASS`. If fixable, revise A/B and recheck. If a central rule remains violated, withhold definitive A and issue the actual blocker.

| Gate | PASS condition | Failure disposition |
|---|---|---|
| `Q01_SCOPE` | One authorized date; no unrequested output/action | Remove excess generation and stop unauthorized actions |
| `Q02_CALENDAR` | Approved/authorized date mapping, weekday, full phase fit, correct chapter day | Block definitive A on unresolved assignment |
| `Q03_THREE_CLOCKS` | Time/locations not conflated; retrieval evidence true; no false historic replay | Correct/qualify; block if central to premise |
| `Q04_IDENTIFIERS` | Actual archive/legacy mapping respected; no invented existing paths | Mark unresolved and escalate material identity conflicts |
| `Q05_CANON` | Character/Edubeam powers, roster, temporal and prior-story events consistent | Revise or block if binding conflict persists |
| `Q06_ROLE_PROJECT` | Chart chapter day and roles sourced; actual vs fictional work distinguished | Omit unsupported claim; revise |
| `Q07_STUDY` | Weekly text/anchor and daily selection genuinely sourced or transparently unresolved | Block only when indispensable; otherwise disclose omission |
| `Q08_VERSE_HS` | Provider/date/version and real lesson section truthfully attributed | Revise/omit; block if expressly mandatory |
| `Q09_RESEARCH` | Facts sourced, future scenario labeled fiction, locations/weather supportable | Remove or reclassify unsupported claims |
| `Q10_RIGHTS` | Public material/participants permitted; private fields excluded and revocations checked | Remove affected content or block central use |
| `Q11_STORY` | One causal narrative; original, coherent, earned final movement | Rewrite |
| `Q12_CHALLENGE` | Fair, final public item, no solution/near-solution in A/B | Rewrite or withhold; log secure-store status |
| `Q13_RECORDS` | B1–B8 in master order; event/state evidence and B6 portable | Repair appendix or accurately mark incomplete |
| `Q14_DERIVATIVES` | No unauthorized media; dependent assets tracked and stale flags accurate | Remove claim, require revalidation |
| `Q15_INTEGRITY` | No invented writes, approvals, consent, publications or repository actions | Correct status, open decision |
| `Q16_BOUNDARIES` | Public/internal/restricted separation enforced at artifact and recipient level | Withhold unsafe packet until separated |

**Regression cases required before adopting the package:** weekday #1/#5/#6/#10; episode boundaries; chapter-working days #10/#11/#20/#21/#30/#31; both weekends; phase starting midweek; incomplete fourth slot; inter-phase gap; conversion across local midnight; retrospective date with only a current Probe; absent/malformed payload; future Probe; role-chart mismatch; revoked consent; missing restricted store; challenge accidentally appended to B or key leaked into B; duplicate day; concurrent archive edit; unresolved field-team retrieval; a story revision invalidating a comic; missing next-episode/chapter-final release decision.

### 10.1 Review, authorized commit and return protocol

1. Record the final draft's version, scope, QA gate outcomes and actual sources. Report A as **draft awaiting editorial review** unless an actual accepted/locked status is evidenced.
2. Prepare event **deltas** and materialized current-state proposals, never retroactively rewrite the event history. Record old ledger/source revision consulted.
3. If and only if a write was expressly authorized and a real supported repository/store action is available: verify the approved path and recipients, compare latest revision, resolve concurrent edits, write with preserved history, verify returned commit/record revision, and capture actual action evidence. No such permission/action means **`DRAFTED — NOT COMMITTED`**.
4. Do not describe draft-state storage as editorial approval or publication. Only a genuine human decision may approve, lock, promote canon, publish, approve rights/consent or release answers.
5. Produce self-contained **B6** carrying only authorized information, clearly distinguishing accepted prior state, current drafted changes and open questions. The next collaborator must be able to continue without another model's hidden memory.
6. On the next commissioned day, reload the **current** approved ledger and any later corrections alongside B6; do not treat B6's older cached state as stronger than accepted updates.
7. When the requested day is #10, flag episode **compilation readiness** and missing approvals without automatically compiling, retrieving a team, choosing a final title or publishing.

### 10.2 Exact blocked-run response fields

For `BLOCKED`, provide a concise **nonpublishable** report containing: request date and zone (if verified); mode; verified vs unresolved calendar slot; exact blocker with source attempts and conflicting refs; privacy/canon impact; permissible omitted/alternative material; evidence or human decision needed; current draft/write/approval status. **Do not** add an invented fully formed Output A merely to satisfy the expected document structure.

---

## 11. Portable invocation directive

When explicitly commissioned for one eligible Classies Chronicle, load the approved governance and the specified `CC-UMP v0.04.00` working baseline, use this runbook, and use `CC-ECLPM v0.04.00` for episode-owned records. Classify the request; resolve the date and authoritative episode position; verify permissions, provenance and current continuity; pin independent clocks; perform all six cumulative passes; write one original Output A ending with its audience challenge; produce separately classified B1–B8 with B6 handover; create restricted C only through actually permitted secure storage; validate and correct; report every actual versus pending approval, write and derivative action. Never claim authority, evidence, security or publication that does not exist.

**END — CC-DCGP v0.04.00 (proposed).**
