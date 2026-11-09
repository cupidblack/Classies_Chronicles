# Classies Chronicles — Master Document Reconciliation Matrix

**Document ID:** CC-MDRM  
**Version:** 0.02.00  
**Status:** Proposed — For Review and Approval  
**Authority:** Human editorial/project owner  
**Scope:** Framework, daily generation, continuity/production handover, Studio Blueprint and AI Desk interfaces

## 1. Executive outcome

The three follow-up deliverables are designed to work together:

1. **CC-MEGF** — governs the story universe, annual/phase/episode structure and narrative principles.
2. **CC-DCGP** — tells an AI how to research and generate exactly one daily chronicle.
3. **CC-ECLPM** — defines the episode-owned context, continuity and production handover records.

The Studio Structure Skeletal Blueprint governs studio operations, production equipment, media workflow, archive structure, publishing and system-level responsibilities. The AI Desk Architecture governs the persistent AI control plane, retrieval, prompts, catalogs, permissions and operational infrastructure.

Neither CC-MEGF, CC-DCGP nor CC-ECLPM should create a competing studio filesystem, AI Desk filesystem or episode archive structure.

## 2. Sources and evidence status

| Ref | Source | Evidence/status |
|---|---|---|
| SRC-01 | Initial Episode Framework v0.01.05 | Retrieved and reviewed |
| SRC-02 | Compiled AI proposals | Retrieved and reviewed; includes multiple proposals and a later reconciliation section |
| SRC-03 | Studio Structure Skeletal Blueprint v22.2 | Retrieved and reviewed directly |
| SRC-04 | AI Desk Architecture v22.0 | Referenced by Blueprint v22.2 and compilation; full file not independently retrieved in this review |
| SRC-05 | Organizational Chart — Aliased Checks | Retrieved and reviewed |
| SRC-06 | Eternal Dreamfall five-year reading plan | Retrieved and reviewed |
| SRC-07 | Classies Chronicles repository | Supplied as canon/archive source; not every file exhaustively inspected |
| SRC-08 | Health & Safety repository | Supplied as course source; individual course files not exhaustively inspected |
| SRC-09 | Later Studio Blueprint versions (including a referenced v23.0) | Version precedence not established; latest directory inventory not independently confirmed |

**Important limitation:** v22.2 is directly accessible at the time of this review, but it must not be called the latest blueprint until the repository directory and all later versions are inventoried. The AI Desk Architecture v22.0 is identified as a specialist dependency by v22.2, but its full text and current successor status still require direct verification.

## 3. Material findings

### F-001 — Annual calendar model conflict (HIGH)

The initial proposal and the user's current instruction define:
- One season per year.
- Five chapters/phases/terms per year.
- Eight weeks per chapter.
- Four two-week episodes per chapter.
- Ten working-day chronicles per episode.

The compilation also identifies a repository candidate, CC-MEGF v0.01.09, which uses a five-season annual planning baseline.

**Resolution proposed:** For this work, preserve the user's explicit current model: one season per year with five chapters. Treat any conflicting repository framework as a candidate requiring reconciliation, not as authority to silently override the instruction. Record the decision in the project decision register before changing repository canon.

### F-002 — Episode versus chronicle (RESOLVED)

An episode is ten working days, Monday through the following week's Friday. Generate one chronicle only for the applicable working day. The ten chronicles are manually compiled and edited later.

### F-003 — Production time versus probe time (HIGH)

The initial proposal identifies the Millennium Probe as mandatory for determining the current episode day and phase boundaries. The compilation distinguishes actual production time from the Millennium probing date.

**Resolution proposed:** Keep at least three separate values:
- `production_now_iso`: actual timestamp returned by the endpoint (or independently verified fallback).
- `probe_iso`: fictional/temporal destination timestamp.
- `phase_start_iso` and `phase_end_iso`: phase boundaries.

Do not use `probe_iso` to calculate the real-world episode day. Use the endpoint's actual production-time and phase fields, validate them, and derive the Monday episode windows from the phase start. The endpoint response schema must be verified before hard-coding field names beyond those confirmed.

### F-004 — Studio and narrative responsibilities (RESOLVED)

Blueprint v22.2 defines system-level studio architecture and deliberately delegates detailed implementation to specialist documents. It establishes lean-first development, separation of concerns, one persistent AI Desk, episode-owned data, provider neutrality, human editorial authority, rebuildable derived data and fail-safe behaviour.

**Resolution proposed:** CC-MEGF governs narrative; CC-DCGP governs daily content generation; CC-ECLPM governs episode records and handover; Studio Blueprint governs studio/production/archive; AI Desk Architecture governs persistent AI infrastructure and retrieval.

### F-005 — Archive structure duplication (HIGH)

Blueprint v22.2 defines the episode archive:
- `01_EPISODE_CONTEXT/`
- `02_RAW_VIDEO/`
- `03_RAW_AUDIO/`
- `04_PROJECT_FILES/`
- `05_STORY_AND_SCRIPT/`
- `06_GRAPHICS/`
- `07_GENERATED_MEDIA/`
- `08_EDITED_MEDIA/`
- `09_PUBLISHING/`
- `10_ARCHIVE/`

The framework/compilation contains alternative proposed trees.

**Resolution proposed:** Do not introduce a competing physical folder tree. Use the approved Blueprint and AI Desk archive contract. Place continuity and production records inside the existing episode context area according to the approved schema.

### F-006 — Persistent AI Desk versus episode-owned data (HIGH)

Blueprint v22.2 states there is one persistent `CC_AI_DESK` for the franchise. It stores reusable intelligence infrastructure and references, not raw episode media or permanent episode-specific knowledge. Episode data remains episode-owned.

**Resolution proposed:** Keep reusable canon as authoritative source material in its approved repository location. The AI Desk indexes/retrieves it through permission-aware catalogs. Episode-specific research, temporary character state, mission developments, daily chronicles and episode decisions remain in the episode archive.

### F-007 — Character canon versus changing state (MEDIUM)

Character identity, aliases, personality and established abilities belong in reusable character canon. Temporary location, current emotional state, injuries, active assignment and current relationships/events belong in the episode continuity record.

**Resolution proposed:** Never update permanent character canon merely because a daily story introduces a temporary state. Changes to canon require human approval and versioning.

### F-008 — Role spotlight scheduling (MEDIUM)

The organizational chart assigns spotlight/check days across a 40-working-day chapter. Days 1–40 map across four episodes; the schedule must not restart every episode. More than one role may be spotlighted where story-relevant, and a role may recur when justified.

**Resolution proposed:** Calculate chapter working-day index (1–40) independently of episode day (1–10). Use the chart's assigned check days as scheduling guidance, not as a reason to force irrelevant characters into a scene.

### F-009 — Education and research provenance (HIGH)

Bible reading, Verse of the Day, Health & Safety lessons, historical research and current news require source records. The five-year reading plan includes canonical biblical texts and other ancient, historical, apocryphal, fragmentary or lost-text references; these categories must not be conflated.

**Resolution proposed:** Store exact reading-plan week/reference, translation/version where applicable, Verse of the Day source and retrieval date, exact H&S course/lesson, and news/historical source URLs. Distinguish historical fact, contemporary fact and fictional probe-world content.

### F-010 — Audience challenge and delayed solution (HIGH)

Every public-facing daily chronicle, comic and video ends with the day's challenge. The answer is excluded from public material and stored in a restricted editorial record. The solution is released with the subsequent episode, subject to the final-episode/chapter-wrap-up schedule being confirmed.

### F-011 — Service Cards (MEDIUM)

The compilation proposes approximately four to five useful Service Cards per completed episode, derived from real lessons and discoveries rather than forced into every chronicle.

**Resolution proposed:** Track opportunities daily; select and approve approximately 4–5 genuinely useful cards during episode post-production. Service Cards are distinct deliverables and do not replace the daily challenge.

### F-012 — Consent, licensing and privacy (HIGH)

Blueprint v22.2 establishes a controlled community-data pipeline and says current permission state must override stale indexes. Technical completion does not imply retrieval or publication permission.

**Resolution proposed:** Every participant-derived source or asset must carry eligibility, consent, licensing, revocation and publication-permission states. Restricted, withdrawn, unlicensed or unverified material must not be retrieved into generation or published.

### F-013 — Media generation sequence (MEDIUM)

Blueprint v22.2 describes a content pipeline and episode-owned archive. The compiled proposals identify text, cover/title image, comic, short video and interactive question/service card as useful content forms, with audio/podcast and full animation deferred where appropriate.

**Resolution proposed:** Lock and approve the written chronicle first. Derivative media must follow the approved text and cannot silently alter narrative canon. Keep the daily challenge as the final audience-facing element.

## 4. Responsibility and authority matrix

| Concern | Governing document/system | CC-MEGF | CC-DCGP | CC-ECLPM |
|---|---|---|---|---|
| Story universe and narrative principles | CC-MEGF | Owns | Applies | Records effects |
| Season/chapter/episode logic | CC-MEGF + approved calendar decision | Owns | Calculates current position | Records identifiers |
| Millennium Probe interface | Approved endpoint contract | Defines requirement | Executes/checks | Records response snapshot |
| Daily research and generation | CC-DCGP | Defines content rules | Owns | Records provenance |
| Character canon | Canon repository / governance | References | Retrieves; does not rewrite | Stores temporary state and change proposals |
| Episode continuity | Episode archive | Defines minimum | Updates daily handover | Owns ledger |
| Studio hardware and production | Studio Blueprint | References | Does not redefine | Tracks deliverables/status |
| AI Desk architecture/retrieval | AI Desk Architecture | References | Uses approved retrieval interface | Supplies context references |
| Episode archive structure | Studio Blueprint + AI Desk contract | Does not redefine | Writes into approved structure | Tracks archive manifest |
| Consent/licensing | Studio/AI permission contract | Requires compliance | Checks before use | Records permission evidence |
| Comics/video/audio | Studio Blueprint | Defines narrative fidelity | Produces prompts when requested | Tracks derivative assets |
| Manual episode compilation | Human editorial / studio process | Defines objective | Does not auto-compile | Tracks readiness |
| Challenge answer release | Human editorial | Defines policy | Creates restricted answer record | Tracks release status |
| Service Cards | Studio/content workflow | Defines objective | Flags candidates | Tracks card pipeline |
| Publication | Human editorial + studio publishing | No unilateral approval | No unilateral publication | Records approval/publication state |

## 5. Required corrections before approval

| ID | Required action | Priority | Owner |
|---|---|---|---|
| CR-01 | Confirm one-season/five-chapter model against current repository candidate and record decision | Critical | Project owner |
| CR-02 | Inventory every Studio Blueprint version and establish precedence | Critical | Repository maintainer |
| CR-03 | Retrieve and verify AI Desk Architecture v22.0 or successor | Critical | Repository maintainer |
| CR-04 | Confirm Millennium Probe JSON schema, timezone semantics and failure behaviour | High | Technical owner |
| CR-05 | Confirm official identifier format and map original `Sxx_TPxx_Exx` naming to studio logical IDs | High | Project owner |
| CR-06 | Confirm episode archive/context schemas; do not create parallel folders | High | Studio/AI Desk owners |
| CR-07 | Confirm canon source ownership and retrieval permissions | High | Canon/AI Desk owners |
| CR-08 | Confirm challenge solution release timing for final episode of a chapter | Medium | Editorial owner |
| CR-09 | Confirm Service Card count/status and approval flow | Medium | Content owner |
| CR-10 | Confirm current YouVersion and H&S source-access procedure | Medium | Research owner |

## 6. Approval gates

**Gate A — Source confirmation:** Blueprint version precedence, AI Desk version and repository candidate are verified.

**Gate B — Policy decisions:** Annual hierarchy, identifiers, episode calendar, challenge release and canon ownership are approved.

**Gate C — Document approval:** CC-MEGF, CC-DCGP and CC-ECLPM are versioned and approved together.

**Gate D — Pilot:** One complete ten-working-day episode is generated, handed over, manually compiled and checked.

No repository structure migration, production automation or canon rewrite is authorised by this reconciliation document.

## 7. Source references

- Initial proposal: `Classies_Chronicles-Proposed_Episode_Framework_v0.01.05.txt`
- Compiled proposals: `Classies_Chronicles_Episode_Framework_compilation.txt`
- Studio Blueprint v22.2: `Studio_Structure_Skeletal_Blueprint_v22.2.txt`
- AI Desk Architecture v22.0: referenced by Blueprint v22.2; direct current-version confirmation outstanding.
- Organizational chart: `Organizational_Chart_Structure-Aliased_Checks.txt`
- Bible plan: `list_of_biblical_texts-5_year_reading_plan-1.txt`

**End of document.**
