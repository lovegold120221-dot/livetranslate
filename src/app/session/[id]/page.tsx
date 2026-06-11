"use client";

import { use, useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { PICKER_LANGUAGES } from "@/lib/languages";

const STORAGE_KEY_NAME = "lt.displayName";
const STORAGE_KEY_LANG = "lt.lang";
const STORAGE_KEY_GENDER = "lt.gender";

type Gender = "male" | "female";

export default function PreFlightPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const router = useRouter();

  const [displayName, setDisplayName] = useState("");
  const [lang, setLang] = useState<string>("en");
  const [gender, setGender] = useState<Gender>("male");
  const [shareCopied, setShareCopied] = useState(false);

  // Restore last-used name + language so returning users skip retyping.
  useEffect(() => {
    if (typeof window === "undefined") return;
    const savedName = window.sessionStorage.getItem(STORAGE_KEY_NAME);
    const savedLang = window.sessionStorage.getItem(STORAGE_KEY_LANG);
    const savedGender = window.sessionStorage.getItem(STORAGE_KEY_GENDER) as Gender | null;
    if (savedName) setDisplayName(savedName);
    if (savedLang) setLang(savedLang);
    if (savedGender) setGender(savedGender);
  }, []);

  function handleJoin() {
    if (!displayName.trim()) return;
    window.sessionStorage.setItem(STORAGE_KEY_NAME, displayName.trim());
    window.sessionStorage.setItem(STORAGE_KEY_LANG, lang);
    window.sessionStorage.setItem(STORAGE_KEY_GENDER, gender);
    router.push(`/session/${id}/room?gender=${gender}`);
  }

  async function copyInviteLink() {
    const url = `${window.location.origin}/session/${id}`;
    try {
      await navigator.clipboard.writeText(url);
      setShareCopied(true);
      setTimeout(() => setShareCopied(false), 2000);
    } catch {
      // ignored
    }
  }

  return (
    <div className="page">
      <div className="container">
        {/* Brand */}
        <div className="enter" style={{ textAlign: "center", marginBottom: 24 }}>
          <span className="brand-orbit">Orbit</span>
          <span className="brand-conference">Conference</span>
          <p className="body-sm" style={{ marginTop: 4, letterSpacing: "0.06em", textTransform: "uppercase" }}>
            Realtime Translator
          </p>
        </div>

        <h1 className="display display-lg enter" style={{ marginBottom: 8 }}>
          Join the call
        </h1>
        <p
          className="body enter-d1"
          style={{ marginBottom: 32 }}
        >
          Pick your language — that&apos;s what you&apos;ll speak and what you&apos;ll
          hear everyone else in.
        </p>

        <div className="enter-d2" style={{ display: "flex", flexDirection: "column", gap: 20, marginBottom: 32 }}>
          <label className="label" style={{ display: "block" }}>
            Your name
            <input
              type="text"
              value={displayName}
              onChange={(e) => setDisplayName(e.target.value)}
              placeholder="e.g. Jesse"
              autoFocus
              className="select-field"
              style={{ marginTop: 8, backgroundImage: "none", paddingRight: 16 }}
              maxLength={40}
            />
          </label>

          <label className="label" style={{ display: "block" }}>
            Language
            <select
              value={lang}
              onChange={(e) => setLang(e.target.value)}
              className="select-field"
              style={{ marginTop: 8 }}
            >
              {PICKER_LANGUAGES.map((l) => (
                <option key={l.code} value={l.code}>
                  {l.flag} {l.name}
                </option>
              ))}
            </select>
          </label>

          <label className="label" style={{ display: "block" }}>
            Voice
            <select
              value={gender}
              onChange={(e) => setGender(e.target.value as Gender)}
              className="select-field"
              style={{ marginTop: 8 }}
            >
              <option value="male">Male</option>
              <option value="female">Female</option>
            </select>
          </label>
        </div>

        <div className="enter-d3" style={{ display: "flex", gap: 12, flexDirection: "column" }}>
          <button
            className="btn btn-dark"
            onClick={handleJoin}
            disabled={!displayName.trim()}
            id="join-btn"
          >
            Join the call
          </button>
          <button
            className="btn btn-outline"
            onClick={copyInviteLink}
          >
            {shareCopied ? "Link copied!" : "Copy invite link"}
          </button>
        </div>

        <p className="mono enter-d4" style={{ marginTop: 32 }}>
          Camera and mic stay off until you turn them on.
        </p>
      </div>
    </div>
  );
}
