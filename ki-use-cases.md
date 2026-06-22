# 💡 KI im Arbeitsalltag – Use-Case-Sammlung

> **Grundlage:** Diese Sammlung entstand auf Basis einer internen Umfrage (Juni 2026).  
> Sie zeigt, wie KI-Tools **konkret und datenschutzkonform** im Abteilungsalltag eingesetzt werden können.  
> ⚠️ Datenschutzregeln immer beachten → [Datenschutz-Guide lesen](./ki-datenschutz-guide.md)

---

## Inhalt

1. [Recherche & Zusammenfassen](#1-recherche--zusammenfassen) (83 %)
2. [Ideen & Brainstorming](#2-ideen--brainstorming) (67 %)
3. [Übersetzungen](#3-übersetzungen) (67 %)
4. [Texte schreiben & überarbeiten](#4-texte-schreiben--überarbeiten) (50 %)
5. [E-Mail & Kommunikation](#5-e-mail--kommunikation) (33 %)
6. [Datenanalyse & Auswertung](#6-datenanalyse--auswertung) (33 %)
7. [EOS-spezifische Use Cases](#7-eos-spezifische-use-cases)
8. [Prompting in 3 Prinzipien](#8-prompting-in-3-prinzipien)
9. [Schnell-Referenz: Prompt-Vorlagen](#9-schnell-referenz-prompt-vorlagen)

> Prozentangaben = Anteil der Befragten, die diesen Bereich nutzen.

---

## 1. Recherche & Zusammenfassen

```
"Erkläre [Fachbegriff] in 5 Sätzen, verständlich ohne Vorkenntnisse."
```
```
"Fasse die wichtigsten Punkte in Stichpunkten zusammen: [Text ohne sensible Daten]"
```
```
"Was sind die 3 wichtigsten Unterschiede zwischen [A] und [B]?"
```

🔒 Nur öffentliche/allgemeine Texte. Für interne Dokumente → **M365 Copilot** (Daten bleiben im Tenant).

---

## 2. Ideen & Brainstorming

```
"Gib mir 10 Ideen für [Thema] – kreativ und pragmatisch gemischt."
```
```
"Schlage eine Gliederung für eine interne Präsentation zu [Thema] vor."
```
```
"Welche 8 Fragen könnte das Publikum nach einem Vortrag zu [Thema] stellen?"
```

🔒 Allgemeine Themen unbedenklich. Keine vertraulichen Projektdetails oder Zahlen nennen.

---

## 3. Übersetzungen

| Tool | Wann |
|------|------|
| **DeepL Business** / **M365 Copilot** | Interne Texte, auch mit Personenbezug (AVV vorhanden) |
| **DeepL Free / ChatGPT** | Nur nicht-sensible, öffentliche Texte |

```
"Übersetze ins Englische, professioneller, formeller Ton: [Text ohne sensible Daten]"
```
```
"Englischer Fachbegriff für [Wort/Konzept]? Gib 2 Alternativen."
```

🔒 Kundenbriefe mit echten Daten nur über DeepL Business / M365 Copilot.

---

## 4. Texte schreiben & überarbeiten

```
"Schreibe einen sachlichen Einleitungsabsatz zum Thema [Thema]."
```
```
"Kürze diesen Text auf max. [X] Wörter, ohne Kerninfos zu verlieren: [Text]"
```
```
"Formuliere professioneller um: '[Satz]'"
```

🔒 Bei echten Namen/Kundendaten: Platzhalter verwenden. KI ist Co-Autor – Inhalt selbst verantworten.

---

## 5. E-Mail & Kommunikation

```
"Schreibe eine höfliche, klare Absage für: [Situation ohne echte Namen]"
```
```
"Ist der Ton dieser E-Mail angemessen? Was würdest du ändern? [Text ohne echte Daten]"
```
```
"Erstelle eine E-Mail-Vorlage für [Anfrageart] mit [X] Platzhaltern."
```

🔒 **Ersatz-Personen nutzen:** Statt „Frau Müller, Firma ABC" → „eine verärgerte Kundin zur Vertragslaufzeit".

---

## 6. Datenanalyse & Auswertung

```
"Welche Muster fallen auf? [aggregierte/anonymisierte Zahlen]"
```
```
"Erstelle eine Vergleichstabelle für [Aspekte] nach Kategorien: [Liste]"
```
```
"Welche Visualisierung passt zu [Datenart] und warum?"
```

🔒 Keine echten Kunden-/Umsatz-/Mitarbeiterdaten. Für echte interne Daten → **M365 Copilot in Excel**.

---

## 7. EOS-spezifische Use Cases

Beispiele mit Bezug zum Finanzdienstleistungs-/Forderungskontext – **immer anonymisiert** (siehe [Datenschutz-Guide](./ki-datenschutz-guide.md)).

**Forderungs-/Inkassokommunikation (entschärft formulieren):**
```
"Formuliere eine verständliche, wertschätzende Zahlungserinnerung für eine
fiktive Privatperson in finanzieller Notlage. Ton: respektvoll, lösungsorientiert."
```

**Regulatorik & Compliance verstehen:**
```
"Erkläre DSGVO Art. 22 (automatisierte Entscheidungen) in einfachen Worten
mit einem Beispiel aus dem Forderungsmanagement."
```
```
"Was ändert sich durch den EU AI Act für Finanzdienstleister? Stichpunkte."
```

**Prozess- & Konzeptarbeit:**
```
"Strukturiere eine Checkliste für [internen Prozess] – ohne echte Daten,
nur Ablaufschritte."
```

🔒 **Hochsensibel:** Bonitäts-/Scoring-Daten und echte Schuldnerdaten gehören **nie** in öffentliche KI-Tools.

---

## 8. Prompting in 3 Prinzipien

**1. Kontext geben** – wer du bist, wofür:
```
"Ich arbeite im Forderungsmanagement und bereite eine Schulung vor. Hilf mir..."
```

**2. Format vorgeben** – wie die Antwort aussehen soll:
```
"Antworte in max. 5 Stichpunkten." / "Erstelle eine Tabelle mit 3 Spalten."
```

**3. Nachschärfen** – der erste Entwurf ist selten perfekt:
```
"Kürzer." / "Freundlicherer Ton." / "Füge ein konkretes Beispiel hinzu."
```

---

## 9. Schnell-Referenz: Prompt-Vorlagen

| Aufgabe | Vorlage |
|---------|---------|
| Zusammenfassung | `"Fasse in [X] Stichpunkten zusammen: [Text]"` |
| E-Mail | `"Schreibe eine [formelle/freundliche] E-Mail zu: [Situation]"` |
| Überarbeitung | `"Kürzer, klarer, professioneller: [Text]"` |
| Übersetzung | `"Übersetze ins [Sprache], professioneller Ton: [Text]"` |
| Brainstorming | `"Gib mir 8 Ideen für [Thema]"` |
| Erklärung | `"Erkläre [Begriff] einfach, ohne Fachjargon"` |
| Toncheck | `"Ist der Ton angemessen? Was ändern? [E-Mail]"` |
| Gliederung | `"Schlage eine Gliederung für [Dokument] vor"` |
| Vergleich | `"Vergleiche [A] und [B] in einer Tabelle nach: [Kriterien]"` |

---

> 📄 Basis: interne KI-Umfrage (Juni 2026). Kapitel = häufigste Einsatzbereiche der Befragten.
> Weitere KI-Lernpfade gruppenweit über **Otto Group LXHub / TechUcation**.
> Datenschutzregeln: → [ki-datenschutz-guide.md](./ki-datenschutz-guide.md) · Stand: Juni 2026.
