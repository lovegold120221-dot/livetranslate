## TASK-20260611-0002: Finish mapping of all languages

### START RECORD
- STATUS: STARTED
- Start time: 2026-06-11T12:00:00Z
- User request: Finish the mapping of all 200+ languages from the frontend's SUPPORTED_LANGUAGES to Gemini-supported codes in the Python agent
- Last known state: completed (TASK-20260611-0001)
- Preservation constraints: No CSS/UI changes. No changes to existing test behavior.
- Files/directories to inspect: src/lib/languages.ts, translator/src/config.py, translator/src/session.py, translator/src/router.py
- Success criteria: Every BCP-47 code from SUPPORTED_LANGUAGES either passes through or maps to a Cloud Translation NMT/TLLM supported code.

### TODO
- [x] Research which SUPPORTED_LANGUAGES codes are NOT in Cloud Translation NMT/TLLM
- [x] Add LANGUAGE_MAP dict to translator/src/config.py mapping all 60 unsupported codes
- [x] Apply LANGUAGE_MAP in translator/src/session.py to normalize targetLanguageCode
- [x] Normalize language codes in translator/src/router.py matching logic
- [x] Write test for LANGUAGE_MAP normalization (test_language_map.py — 8 tests)
- [x] Run all tests (19/19 passing)
- [x] Update comment in src/lib/languages.ts
- [x] Write final report

### FINAL REPORT
- STATUS: COMPLETED
- End time: 2026-06-11T12:30:00Z
- Files changed:
  - `translator/src/config.py` — Added `LANGUAGE_MAP` dict with 60 mappings
  - `translator/src/session.py` — Import and apply `LANGUAGE_MAP.get(target_lang, target_lang)` on init
  - `translator/src/router.py` — Import `LANGUAGE_MAP`, add `_normalise_lang()` helper, normalize in `_listener_target_langs()` and `_active_speakers()`
  - `translator/tests/test_language_map.py` — New test file (8 tests covering all codes, edge cases, and router helper)
  - `src/lib/languages.ts` — Updated doc comment to reflect completed mapping
- Validation performed:
  - 19/19 tests pass (8 new language map tests + 11 existing router tests)
  - All 249 frontend codes verified: 189 pass through as Gemini-supported, 60 map to closest supported equivalent
  - Cross-referenced against Cloud Translation NMT + TLLM official supported lists
- CSS/UI preservation: No CSS/UI changes.
- Real data/API credential check: No secrets changed.
- Known issues:
  - Frontend build has a pre-existing TS error in InCall.tsx screen share (unrelated to this change)
- Next step: None.

