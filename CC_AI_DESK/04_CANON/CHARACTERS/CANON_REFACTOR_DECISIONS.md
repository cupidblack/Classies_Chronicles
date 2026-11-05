# Character Canon v0.02.00 — Refactor / Traceability / Editorial Decision Record

**Prepared:** 2026-11-05 | **Decision authority:** human editor, not this generated package | **Result:** 62 detailed fiction-only drafts, 0 images, 0 repository writes

## Input review and conflict decisions

| Observation from prior responses and current sources | Implemented decision |
|---|---|
| Previous ChatGPT generated 62 files with extensive proposals; GitHub response produced lightweight role concepts; Copilot warned volume; Gemini proposed often highly specific names, real colleges/employers, unverified relationships and biographies. | Treat all supplements as creative fiction only; source chart is authoritative exclusively for role, alias, hierarchy and working-day checks. Deliver all 62 with deeply expanded individual profiles in one importable ZIP. |
| Prior manifest and index indicate 62 aliases; Copilot's rough estimate of 52 is incomplete. | Exactly 62 unique folders/files, cross-checked against the 62 source alias entries and earlier 62-row manifest. |
| Several platform sample names risk mistaken formatting (`EUGENE_ACHI AA`, `VERA_AGBEN AHEVI`, `PAULINE_MB USO`). | Use consistent uppercase ASCII slugs `EUGENE_ACHIAA`, `VERA_AGBENAHEVI`, `PAULINE_MBUSO` with user-prescribed lowercase `_character_cannon.md` suffix. |
| The term 'cannon' has a typo relative to editorial 'canon'. | Respect exact requested physical naming `_character_cannon.md`; use canon within field semantics and official linked Cupid Black file. |
| Five NSS roles are generic and may not correspond to known people. | Preserve stable `NSS_PERSONNEL_1` … `_5` source identifiers; offer invented screen identities separately. Do not claim identification of NSS employees. |
| Source alias notes resemble real schools/workplaces and sometimes credentials; Gemini implied actual qualifications and family. | Preserve exact alias text but do not turn mnemonic parentheticals into biography. Invent schools and former workplaces with fictional naming, and label every new claim as an unapproved design proposal. |
| Some chart brackets are malformed (Johnson Ortsin; Pascal Quagrainie). | Preserve alias text as written, with source line trace. Do not silently repair or infer a credential. |
| Enka Yamoah and Cupid Black refer to overlapping character identities. | Keep `ENKA_YAMOAH` organizational role facet while preserving the pre-existing `CUPID_BLACK` authority, illustration references, knowledge boundary and power restrictions. Never overwrite existing Cupid Black canon. |
| The framework distinguishes 40 chapter working days / 20-day role check recurrence and ten working days per episode. | Retain source check labels literally and forbid interpreting them as chronicle-day or real employee attendance. |
| An earlier approach proposed non-existent daily diary files and image paths. | Metadata URL values are `null` until actual authorized assets exist; visual collage is a future production specification only. No empty dummy files. |
| Cross-platform notes include strongly identifying, unverifiable physical/family/relationship claims for named people. | Fictional composites only; explicitly mark consent unknown, public portrayal false, and require review or pseudonymization before publication. |
| Previous archive binary was linked but unavailable to this runtime. | Review published index, manifest, Jacques sample and development compilation; do not pretend to have diffed the inaccessible ZIP contents. |

## Technical controls

- YAML front matter is machine-readable and includes stable IDs, exact aliases, chapter check schedule, diary and collage absent values, and episode state boundaries.
- Every generated profile has 13 substantive sections (Enka has an additional canonical override section).
- Index and CSV manifest are generated from a single role data source, avoiding index/file drift.
- Report links are relative between character folders; checker verifies all internal canon links, with the intentional exception of the pre-existing Cupid Black target (not in ZIP).
- `validate_character_canons.py` is dependency-free Python for checks of coverage and link resolution (no network access needed).
- No implicit repository commits; human review and GitHub import are separate actions.

## Import / governance

1. Extract ZIP at a local clone of the `Classies_Chronicles` repository root, preserving `CC_AI_DESK/04_CANON/CHARACTERS/`.
2. Review proposed characterization/rights, especially if a chart alias maps to an identifiable person. Approved author may rename to a fully fictive screen identity.
3. Run the included validator. Cross-check actual repository content, then commit through normal review.
4. Do not publish or use as locked character/visual canon merely because the files exist. After a separate authorized art operation, add checked image assets and verified diary URLs, then advance version and approval status.

