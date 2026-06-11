"use client";

import { PICKER_LANGUAGES, getLanguageByCode } from "@/lib/languages";
import { ChevronDownIcon, SpeakerOnIcon, SpeakerOffIcon } from "./icons";

export default function LanguagePill({
  value,
  onChange,
  translatorAudioOn = true,
  onToggleTranslatorAudio,
}: {
  value: string;
  onChange: (lang: string) => void;
  translatorAudioOn?: boolean;
  onToggleTranslatorAudio?: () => void;
}) {
  const current = getLanguageByCode(value);

  return (
    <div className="lang-pill-wrapper">
      <label className="lang-pill">
        <span className="lang-pill-prefix">Lang</span>
        <span className="lang-pill-flag" aria-hidden>
          {current?.flag ?? "🌐"}
        </span>
        <span className="lang-pill-name">{current?.name ?? "Pick language"}</span>
        <span className="lang-pill-chevron" aria-hidden>
          <ChevronDownIcon />
        </span>
        <select
          className="lang-pill-select"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label="Listening language"
        >
          {PICKER_LANGUAGES.map((l) => (
            <option key={l.code} value={l.code}>
              {l.flag} {l.name}
            </option>
          ))}
        </select>
      </label>
      {onToggleTranslatorAudio && (
        <button
          className={`lang-speaker-btn ${translatorAudioOn ? "lang-speaker-on" : "lang-speaker-off"}`}
          onClick={onToggleTranslatorAudio}
          title={translatorAudioOn ? "Mute translator audio" : "Unmute translator audio"}
          aria-label={translatorAudioOn ? "Mute translator audio" : "Unmute translator audio"}
        >
          {translatorAudioOn ? <SpeakerOnIcon /> : <SpeakerOffIcon />}
        </button>
      )}
    </div>
  );
}
