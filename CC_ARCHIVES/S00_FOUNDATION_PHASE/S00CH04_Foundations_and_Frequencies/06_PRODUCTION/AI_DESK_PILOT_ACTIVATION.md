# AI Desk Pilot Activation — S00E01

## Objective
Commission the existing persistent CC_AI_DESK without turning E01 into an automation experiment.

## Operating mode
Start **LISTEN**, move to **ASSIST**, then **AUDIO**, then **CONTROLLED CO-HOST** only after each stage passes.

## Required controls
- AI MUTE.
- Source scope display.
- Current episode / archive scope distinction.
- Consent gate.
- Licensing gate.
- Human publication approval.
- Provider failure fallback.

## Minimum acceptance tests
1. Current-episode Bible query returns Nehemiah 1–7.
2. Archive query returns approved source references.
3. A consent-restricted participant query is denied/redacted.
4. AI mute stops return audio immediately.
5. AI does not hear its own TTS return.
6. Provider failure does not bypass the human programme path.
7. Editing an episode context file marks derived indexes stale.

## Important implementation decision
Do not build a new AI Desk for E01. The studio blueprint and AI Desk architecture specify one persistent CC_AI_DESK for the entire franchise.
