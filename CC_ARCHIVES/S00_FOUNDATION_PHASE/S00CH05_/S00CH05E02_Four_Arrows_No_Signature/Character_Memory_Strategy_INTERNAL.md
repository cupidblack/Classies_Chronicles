# Classies Chronicles — Character memory and relationship continuity strategy

**Scope:** Recommended INTERNAL draft design for the proposed episode; requires editor and Studio schema approval before use.

## Single source of accepted truth

Maintain the **episode-owned accepted event log** as the authority for what happened in an episode. Do not paste entire narrative summaries repeatedly into every character canon. Instead keep a character-scoped *materialized projection* that points back to the accepted episode event IDs and contains the minimum relevant change to that character's knowledge, attitude, relationship, location or obligations.

## Proposed per-character storage

Each approved fictional character may have a file alongside their character canon:

`CC_AI_DESK/04_CANON/CHARACTERS/{APPROVED_CHARACTER_SLUG}/{APPROVED_CHARACTER_SLUG}_behavior_relationship_events.jsonl`

The twenty per-character JSONL records included in this package use `_PROPOSED.jsonl` suffixes precisely because they have **not** been accepted or written to source character folders. The candidate slugs in their filenames are not certified repository identifiers. Do not copy them into an actual repository without resolving approved slugs, IDs, relationship permissions and storage locations.

## Acceptance / update transaction

1. Read the **actual** accepted episode head, effective character canons, revocation/consent status, and latest character memory head. These cannot be inferred from an unapproved manuscript.
2. Human editor accepts or rejects exact events and identifies an approved story revision, event location, character participants and scope of authorized portrayal. Reject events that contradict protected canon or portray private details without permission.
3. Give each **accepted** event a persistent event ID from the approved store; retain the manuscript proposal key as a traceable predecessor, not as the production ID.
4. For each character genuinely affected, append only a concise derived event with `character_id`, `source_episode_id`, `source_event_id`, `scene_time`, `knowledge_delta`, `behavior_delta`, `relationship_edges`, `editor_acceptance_reference`, `record_revision` and `security_classification`. Where a field was not evidenced, represent it as *unverified with reason*, not fabricated content.
5. Use an idempotent key `(approved_episode_revision, accepted_event_id, character_id)` and compare the latest accepted head before writing; this prevents duplicate copies from multiple providers.
6. Perform an authenticated write; check the bytes and revision after write. Update any character-state index only after verified readback. If concurrency or rights conflict occurs, abort and reconcile rather than overwriting.
7. For a later correction, append a new `SUPERSEDES` or `REVERSES` event and recompute the current projection; do not silently alter a prior accepted event. Apply lawful erasure and revoked-consent controls before preserving history.

## Relationship dynamics

Track **directed** relationship edges for each involved character, because Enka's trust in Mubarak can increase without implying that Mubarak's feelings changed identically. Suggested fields include `person_a`, `person_b`, `professional_or_personal_context`, `trigger_event`, `observed_behavior`, `private_belief_if_canonically_available`, `confidence_and_evidence`, `known_to_characters`, `editorial_status`, `effective_time`, and `visibility`. A character may know less than the reader; preserve this asymmetry. Do not infer family, health, religion, intimacy, criminality or other sensitive attributes from a real-world name or a fictional encounter.

## Episode 02 provisional deltas

Potential arcs to review: Johnson is less resistant to Derek's safety corrections; Enka acknowledges Mubarak's authority boundary; Isaac and Bonsu model separate record-custody and visitor-safety duties; Josh and Terry jointly correct a misleading claim; Ceda sees attendance proposals kept separate from confirmed bookings; Edliex advises by invitation instead of exercising operational command. These are draft story effects only.

## Efficient handoff and query

At a future daily production call, query the last accepted episode snapshot plus the *minimum affected characters'* current projections; include their `known_to` constraints and outstanding relational obligations. Use the B6 handover as a portable summary, not as a second mutable authority. When a character has no new accepted event, **do not** rewrite or touch the character's record. Count affected IDs, exact event proposals, accepted IDs, rejected rows and verified writes in the production manifest.
