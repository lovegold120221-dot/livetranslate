"""Constants for the translation agent."""

from __future__ import annotations

# --- Gemini Live ---

GEMINI_MODEL = "gemini-3.5-live-translate-preview"

# Gemini Live API audio formats.
GEMINI_INPUT_SAMPLE_RATE = 16000  # Gemini expects 16kHz mono PCM in
GEMINI_OUTPUT_SAMPLE_RATE = 24000  # Gemini emits 24kHz mono PCM out
AUDIO_CHANNELS = 1

# --- LiveKit ---

# Track attribute keys for translator-published tracks.
TRACK_ATTR_KIND = "kind"
TRACK_ATTR_SOURCE_IDENTITY = "source_identity"
TRACK_ATTR_TARGET_LANG = "target_lang"

# Marker value for the `kind` attribute on translator tracks.
TRANSLATION_TRACK_KIND = "translation"

# Participant attribute carrying each participant's chosen language.
PARTICIPANT_LANG_ATTR = "lang"

# Sentinel meaning "no translation, native passthrough."
NATIVE_LANG = "none"

# --- Router behavior ---

# Debounce window for room state changes before reconciling sessions.
RECONCILE_DEBOUNCE_SEC = 0.25

# How long to keep a session warm after its last demand disappears
# (speaker mutes, or the last listener for a target language leaves).
SESSION_GRACE_SEC = 10.0

# --- Language code mapping ---

# Maps the 200+ BCP-47 codes from the frontend's SUPPORTED_LANGUAGES to the
# subset supported by Gemini Live / Cloud Translation (NMT + TLLM).
# Regional variants and minority languages map to their closest supported code.
# The frontend displays the full list; the Python agent normalises before sending
# to Gemini. Keep this in sync with src/lib/languages.ts in the frontend.
LANGUAGE_MAP: dict[str, str] = {
    # Ethiopian / Horn of Africa
    "aa": "am",          # Afar → Amharic
    # Alur: Cloud Translation uses `alz` instead of `alu`
    "alu": "alz",
    # Avar → Russian (spoken in Russian Federation)
    "av": "ru",
    # Baluchi → Persian (Iran / Afghanistan region)
    "bal": "fa",
    # Baoulé → French (Côte d'Ivoire official language)
    "bci": "fr",
    # Tibetan → Chinese (Simplified)
    "bo": "zh-CN",
    # Chechen → Russian
    "ce": "ru",
    # Chamorro → English (Guam / US territory)
    "ch": "en",
    # Chuukese → English (Micronesia)
    "chk": "en",
    # Crimean Tatar Latin → Cyrillic (same language, Cyrillic form is supported)
    "crh-Latn": "crh",
    # Dyula → French (West Africa)
    "dyu": "fr",
    # Faroese → Danish (Faroe Islands / Denmark)
    "fo": "da",
    # Fon → French (Benin)
    "fon": "fr",
    # Friulian → Italian
    "fur": "it",
    # Manx → Irish (both Gaelic)
    "gv": "ga",
    # Iban → Malay (closely related)
    "iba": "ms",
    # Inuktut (both scripts) → English (Canada)
    "iu": "en",
    "iu-Latn": "en",
    # Jingpo → Burmese (Myanmar)
    "kac": "my",
    # Qʼeqchiʼ → Spanish (Guatemala)
    "kek": "es",
    # Kituba → Cloud Translation uses `ktu` for Kituba
    "kgo": "ktu",
    # Khasi → Bengali (Indian region)
    "kha": "bn",
    # Kalaallisut → Danish (Greenland)
    "kl": "da",
    # Kurdish (Kurmanji) → Cloud Translation uses `ku`
    "kmr": "ku",
    # Konkani → Goan Konkani (Cloud Translation uses `gom`)
    "kok": "gom",
    # Kanuri → Hausa (Nigeria / Niger region)
    "kr": "ha",
    # Komi → Russian
    "kv": "ru",
    # Tshiluba → Lingala (DRC)
    "lu": "ln",
    # Madurese → Indonesian
    "mad": "id",
    # Mam → Spanish (Guatemala)
    "mam": "es",
    # Mauritian Creole → French
    "mfe": "fr",
    # Marshallese → English (Marshall Islands)
    "mh": "en",
    # Meadow Mari → Cloud Translation uses `chm`
    "mhr": "chm",
    # Meiteilon (Manipuri) → Cloud Translation uses `mni-Mtei`
    "mni": "mni-Mtei",
    # Marwadi → Hindi (India)
    "mwr": "hi",
    # Ndau → Shona (Zimbabwe, closely related)
    "ndc": "sn",
    # Nahuatl (Eastern Huasteca) → Spanish (Mexico)
    "nhe": "es",
    # NKo → English (no direct match)
    "nqo": "en",
    # Ossetian → Russian
    "os": "ru",
    # Punjabi (Gurmukhi) → Punjabi (same language, base code supported)
    "pa-Guru": "pa",
    # Dari → Persian (Dari is Afghan Persian)
    "prs": "fa",
    # Yakut → Russian
    "sah": "ru",
    # Santali (both scripts) → Bengali (India)
    "sat": "bn",
    "sat-Latn": "bn",
    # Sami (North) → Norwegian
    "se": "no",
    # Susu → French (Guinea)
    "sus": "fr",
    # Tulu → Kannada (Indian region)
    "tcy": "kn",
    # Tiv → Hausa (Nigeria)
    "tiv": "ha",
    # Tongan → Samoan (Polynesian)
    "to": "sm",
    # Tok Pisin → English (Papua New Guinea)
    "tpi": "en",
    # Tumbuka → Chichewa (Malawi)
    "tum": "ny",
    # Twi → Akan (same language, Cloud Translation uses `ak`)
    "tw": "ak",
    # Tahitian → French (French Polynesia)
    "ty": "fr",
    # Tuvan → Russian
    "tyv": "ru",
    # Tamazight (both scripts) → Arabic (Morocco)
    "tzm": "ar",
    "tzm-Tfng": "ar",
    # Udmurt → Russian
    "udm": "ru",
    # Venetian → Italian
    "vec": "it",
    # Waray → Filipino (Philippines)
    "war": "fil",
    # Zapotec → Spanish (Mexico)
    "zap": "es",
}

# --- Gemini connection ---

# Exponential backoff schedule for reconnecting a failed Gemini session.
GEMINI_RECONNECT_BACKOFF_SEC = [0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 30.0]
GEMINI_MAX_FAILURES_BEFORE_LONG_BACKOFF = 5
