# 🔒 KI-Nutzung – Datenschutz & Richtlinien

> **Grundlage:** Interne Umfrage Juni 2026 – Datenschutz war die meistgenannte Hürde (3 von 6).
>
> ⚠️ **Wichtiger Hinweis zum Status:** EOS hat (Stand Juni 2026) **keine öffentlich auffindbare KI-Richtlinie oder Acceptable-Use-Policy**. Dieser Guide ist eine **Orientierungshilfe** auf Basis der öffentlichen EOS-DSGVO-Informationen, des Otto-Group-CDR-Rahmens und des EU AI Act – **keine verbindliche Freigabe**. Verbindliche Regeln gibt nur IT / Compliance / Datenschutz.

---

## Inhalt

1. [Die 3 Grundregeln](#die-3-grundregeln)
2. [Was nie in KI-Tools darf](#was-nie-in-ki-tools-darf)
3. [Was unbedenklich ist](#was-unbedenklich-ist)
4. [Tools – Orientierung (keine offizielle Freigabe)](#tools--orientierung-keine-offizielle-freigabe)
5. [Rechtlicher Pflichtrahmen](#rechtlicher-pflichtrahmen)
6. [Umgang mit KI-Ergebnissen](#umgang-mit-ki-ergebnissen)
7. [FAQ](#faq)
8. [Ansprechpartner](#ansprechpartner)

---

## Die 3 Grundregeln

1. **Keine echten Personen- oder Kundendaten** in öffentliche KI-Tools – immer Platzhalter.
2. **Verantwortung bleibt bei dir** – jede KI-Ausgabe vor Verwendung prüfen.
3. **Im Zweifel nicht eingeben** – kurz bei Datenschutz/Compliance nachfragen.

> 🧭 **Faustregel:** Würdest du es einem externen Dienstleister unverschlüsselt mailen? Nein → nicht eingeben.

---

## Was nie in KI-Tools darf

Als Finanzdienstleister verarbeitet EOS besonders schützenswerte Daten. Die folgenden Kategorien (abgeleitet aus der **öffentlichen EOS-DSGVO-Informationspflicht**) gehören **nicht** in öffentliche KI-Tools:

| ❌ Kategorie | Beispiele |
|-------------|-----------|
| **Stamm- & Adressdaten** | Namen, Anschriften von Schuldner:innen, Kund:innen, Kolleg:innen |
| **Vertragsdaten** | Forderungen, Vertragsdetails, Aktenzeichen |
| **Bank- & Zahlungsverkehrsdaten** | Kontonummern, Zahlungshistorie, Mahnstände |
| **Kommunikationsdaten** | Schriftverkehr, Telefonnotizen mit Personenbezug |
| **Bonitäts- & Scoring-Daten** | Bewertungen einzelner Personen → besonders sensibel ([Art. 22 DSGVO](#rechtlicher-pflichtrahmen)) |
| **Interne Unternehmensdaten** | Strategie, Forecasts, Preiskalkulation, nicht-veröffentlichte Zahlen |
| **Zugangsdaten** | Passwörter, API-Keys, interne URLs/Systeminfos |

> ⚠️ Auch **anonymisierte** Daten können re-identifizierbar sein, wenn mehrere Felder kombiniert werden.

---

## Was unbedenklich ist

| ✅ Erlaubt | Beispiel |
|-----------|----------|
| Allgemeine Entwürfe & Gliederungen | Struktur eines Berichts, Präsentationsaufbau |
| Fiktive Beispielsituationen | „E-Mail an eine Kundin, die nach dem Status fragt" – ohne echte Daten |
| Recherche zu öffentlichen Themen | „Unterschied DSGVO Art. 6 und Art. 9?" |
| Sprachliche Überarbeitung | Texte ohne sensiblen Inhalt korrigieren/kürzen |
| Übersetzung nicht-sensibler Texte | Interne Anleitungen ohne Personenbezug |

> 💡 **Platzhalter-Trick:** Statt „Kunde Müller, Konto 12345" → „ein Privatkunde, Vertragsnr. XYZ". Ergebnis bleibt gleich nützlich.

---

## Tools – Orientierung (keine offizielle Freigabe)

> ⚠️ **Es existiert keine veröffentlichte EOS-Tool-Freigabeliste.** Die Tabelle ist eine **Risikoeinschätzung**, keine verbindliche Erlaubnis. Verbindlich erst nach Bestätigung durch IT/Compliance.

| Tool | Datenschutz-Risiko | Hinweis |
|------|--------------------|---------|
| **Microsoft 365 Copilot** | 🟢 Niedrig | Daten bleiben im EU-/M365-Tenant. Für interne Arbeitsdaten die sicherste Option. |
| **DeepL Business** | 🟢 Niedrig | Mit Datenschutzvertrag (AVV). Kostenlose Version: keine Garantie. |
| **ChatGPT Enterprise / Copilot for Work** | 🟡 Mittel | Nur wenn Unternehmensvertrag besteht – intern prüfen. |
| **GitHub Copilot** | 🟡 Mittel | Nur mit Unternehmens-Abo + Code-Review. |
| **ChatGPT (privates Konto)** | 🔴 Hoch | Keine Datenschutzgarantie → nur unkritische, allgemeine Inhalte. |
| **Bildgeneratoren (DALL·E, Midjourney)** | 🔴 Hoch | Einzelfallprüfung: Urheberrecht, keine sensiblen Inhalte. |

---

## Rechtlicher Pflichtrahmen

Diese Punkte sind **keine Empfehlung, sondern geltendes Recht** – besonders relevant für EOS als Finanzdienstleister:

- **AI-Literacy-Pflicht (EU AI Act, seit 02.02.2025 in Kraft):** Wer KI beruflich nutzt, muss ausreichend geschult sein. Das ist eine **Arbeitgeberpflicht** – Schulungen wie diese Umfrage-Maßnahme sind also Pflichterfüllung, nicht „nice to have".
- **DSGVO Art. 22 – automatisierte Entscheidungen:** Rein automatisierte Entscheidungen mit erheblicher Wirkung auf Personen (z. B. Scoring, Forderungsbewertung) sind **ohne menschliche Prüfung unzulässig**. Direkt relevant, sobald KI in Schuldner-/Kundenprozesse einfließt.
- **Transparenzpflicht (EU AI Act, ab 08/2026):** KI-Chatbots und KI-generierte Inhalte müssen **als KI erkennbar** sein.
- **High-Risk-Kontext (ab 12/2027):** Das EOS-Kerngeschäft (Scoring, Bonitätsbewertung) fällt voraussichtlich unter **„Hochrisiko-KI"** → strenge Pflichten zu Dokumentation, Logging und menschlicher Aufsicht.

> 📌 *Datenbasis vs. Interpretation:* Die DSGVO-Datenkategorien stammen aus der öffentlichen EOS-Information. Die EU-AI-Act-Einordnung als „Hochrisiko" ist eine **fachliche Interpretation** des Gesetzestextes – die finale Einstufung trifft EOS Compliance.

---

## Umgang mit KI-Ergebnissen

KI **halluziniert** – sie erfindet überzeugend klingende, falsche Inhalte. Pflicht im Arbeitskontext:

- [ ] **Prüfen:** Zahlen, Zitate, Rechtsaussagen nie ungeprüft übernehmen.
- [ ] **Quellen verifizieren:** KI erfindet teils nicht-existente Quellen.
- [ ] **Verantwortung:** Du haftest für alles unter deinem Namen – auch KI-Output.
- [ ] **Kennzeichnung:** KI-generierte Inhalte ggf. als solche markieren (EU AI Act, ab 08/2026).

---

## FAQ

**Versehentlich echte Kundendaten eingegeben – was tun?**
Sofort an Datenschutz/Vorgesetzte melden, Chat-Verlauf wo möglich löschen (z. B. ChatGPT → Einstellungen → Datenkontrolle), Vorfall dokumentieren.

**Darf ich KI für Kunden-E-Mails oder Forderungsschreiben nutzen?**
Ja, aber nur als Vorlage mit fiktiven Platzhaltern – echte Namen/Konto-/Vertragsdaten erst danach manuell einfügen. Ergebnis vor Versand prüfen.

**Kundenbrief mit DeepL übersetzen?**
Nur mit DeepL Business (AVV) oder M365 Copilot. Kostenloses DeepL: keine echten Personendaten.

**Gibt es genehmigte Tools/Prompts?**
Offizielle EOS-Freigabeliste ist nicht öffentlich → bei IT/Compliance erfragen. Prompt-Vorlagen: → [Use-Case-Sammlung](./ki-use-cases.md).

---

## Ansprechpartner

| Anliegen | Kontakt |
|----------|---------|
| Datenschutz / DSGVO / Datenpanne | EOS-Datenschutz: **datenschutz@eos-group.eu** |
| Aufsichtsbehörde | Hamburgischer Beauftragter für Datenschutz und Informationsfreiheit |
| Tool-Freigaben | IT / Compliance |
| KI-Lernpfade (gruppenweit) | Otto Group **LXHub / TechUcation** |

---

> 📄 Orientierungshilfe auf Basis der internen KI-Umfrage (Juni 2026), der öffentlichen EOS-DSGVO-Informationen, des Otto-Group-CDR-Rahmens und des EU AI Act.
> **Ersetzt keine verbindlichen EOS-Richtlinien.** Datenbasis, Interpretation und Annahmen sind im Text gekennzeichnet. Stand: Juni 2026.
