# 🔒 KI-Nutzung in der Abteilung – Datenschutz & Richtlinien

> **Grundlage:** Dieser Guide entstand auf Basis einer internen Umfrage (Juni 2026).  
> Datenschutz wurde von **3 von 6 Befragten** als häufigste Unsicherheit beim KI-Einsatz genannt.  
> Ziel dieses Dokuments: Klare Orientierung geben – was ist erlaubt, was nicht, und warum.

---

## Inhalt

1. [Warum dieser Guide?](#warum-dieser-guide)
2. [Grundprinzip: Was darf rein – was nicht?](#grundprinzip)
3. [Verbotene Eingaben](#verbotene-eingaben)
4. [Zulässige Eingaben](#zulässige-eingaben)
5. [Welche Tools dürfen genutzt werden?](#welche-tools-dürfen-genutzt-werden)
6. [Wie gehe ich mit KI-Ergebnissen um?](#wie-gehe-ich-mit-ki-ergebnissen-um)
7. [Häufige Fragen (FAQ)](#häufige-fragen-faq)
8. [Bei Unsicherheiten: An wen wende ich mich?](#bei-unsicherheiten)

---

## Warum dieser Guide?

KI-Tools wie ChatGPT, Microsoft Copilot oder DeepL bieten echten Mehrwert im Arbeitsalltag –  
aber sie funktionieren oft über externe Server. Das bedeutet: **Was dort eingegeben wird, verlässt potenziell das Unternehmen.**

Unsere Umfrage zeigt: Die größte Hürde bei der KI-Nutzung ist **nicht fehlendes Wissen über die Tools selbst**, sondern **Unsicherheit darüber, was erlaubt ist und welche Daten eingegeben werden dürfen**.

Dieser Guide gibt klare Antworten – direkt umsetzbar, ohne langes Nachfragen.

---

## Grundprinzip

> 🧭 **Faustregel: Würdest du diese Information auch einem externen Dienstleister unverschlüsselt per E-Mail schicken? Wenn nein → nicht in KI-Tools eingeben.**

KI-Chattools wie ChatGPT (ohne Enterprise-Abo) oder öffentliche Bildgeneratoren **trainieren sich potenziell auf eingegebene Daten** oder speichern Anfragen. Selbst wenn kein Training stattfindet: Daten verlassen das Unternehmensnetzwerk.

---

## Verbotene Eingaben

Die folgenden Datenkategorien dürfen **unter keinen Umständen** in öffentliche KI-Tools eingegeben werden:

| ❌ Kategorie | Beispiele |
|-------------|-----------|
| **Kundendaten** | Namen, Adressen, Kundennummern, Kontodaten, Kommunikationshistorie |
| **Personenbezogene Daten (DSGVO)** | Name + Adresse, Geburtsdatum, Krankheitsdaten, HR-Daten von Kolleg:innen |
| **Vertrauliche Unternehmensdaten** | Strategiepapiere, Budgetzahlen, Vertragsdetails, Preiskalkulationen |
| **Interne Systeminformationen** | Passwörter, API-Keys, interne URLs, Systemarchitektur |
| **Rechtlich sensible Informationen** | Laufende Verhandlungen, Compliance-Vorgänge, juristische Schriftsätze |
| **Nicht-öffentliche Finanzdaten** | Quartalszahlen vor Veröffentlichung, interne Forecasts |

> ⚠️ **Auch anonymisierte Daten können problematisch sein**, wenn durch Kombination mehrerer Felder Rückschlüsse auf Personen möglich sind.

---

## Zulässige Eingaben

Diese Inhalte können **grundsätzlich** in KI-Tools eingegeben werden:

| ✅ Kategorie | Beispiele |
|-------------|-----------|
| **Allgemeine Textentwürfe** | Struktur eines Briefes, Gliederung einer Präsentation, Formulierungshilfe |
| **Fiktive Beispielsituationen** | „Schreibe eine E-Mail, in der ein Kunde nach dem Status fragt" – ohne echte Kundendaten |
| **Recherchefragen** | „Was ist der Unterschied zwischen DSGVO-Artikel 6 und Artikel 9?" |
| **Sprachliche Überarbeitung** | Texte korrigieren, kürzen, umformulieren – solange keine sensiblen Inhalte enthalten sind |
| **Öffentlich bekannte Informationen** | Newszusammenfassungen, allgemeine Fachfragen |
| **Brainstorming & Kreativaufgaben** | Ideen entwickeln, Überschriften, Konzeptentwürfe |
| **Übersetzungen von nicht-sensiblen Texten** | Allgemeine Korrespondenz, interne Anleitungen ohne Kundenbezug |

> 💡 **Tipp:** Ersetze echte Daten durch Platzhalter. Statt „Kunde Müller, Konto 12345" → „ein Privatkunde, Vertragsnummer XYZ". Das Ergebnis ist genauso nützlich.

---

## Welche Tools dürfen genutzt werden?

> 🏢 **Dieser Abschnitt muss unternehmensspezifisch bestätigt werden.**  
> Die folgende Tabelle zeigt eine allgemeine Einschätzung – die verbindlichen Freigaben bitte mit **IT / Compliance** abstimmen.

| Tool | Status | Hinweise |
|------|--------|----------|
| **Microsoft 365 Copilot** | ✅ Intern bevorzugt | Daten bleiben im M365-Tenant des Unternehmens. Für Arbeitsdaten empfohlen. |
| **DeepL (kostenpflichtig / Business)** | ✅ In der Regel zulässig | Business-Abos mit Datenschutzzusage. Kostenlose Version: keine Garantie. |
| **ChatGPT (privates Konto)** | ⚠️ Nur für unkritische Inhalte | Kein Unternehmensvertrag → keine Datenschutzgarantie. Nur für allgemeine Anfragen. |
| **ChatGPT Enterprise / Copilot for Work** | ✅ Je nach Unternehmensvertrag | Prüfen, ob Unternehmensvertrag besteht. |
| **GitHub Copilot** | ✅ Für Entwickler | Nur mit aktivem Unternehmens-Abonnement und Code-Review. |
| **Bildgeneratoren (DALL·E, Midjourney)** | ⚠️ Einzelfallprüfung | Keine sensiblen Inhalte, keine Markenlogos ohne Prüfung, kein Copyright-Risiko. |

> 📌 **Frage an IT/Compliance:** Welche Tools sind offiziell für welche Verwendungszwecke freigegeben?

---

## Wie gehe ich mit KI-Ergebnissen um?

KI-Tools können **halluzinieren** – sie erfinden überzeugend klingende, aber falsche Informationen.

**Pflicht beim Einsatz von KI im Arbeitskontext:**

- [ ] **Ergebnisse prüfen:** Niemals KI-Ausgaben ungeprüft verwenden – insbesondere bei Zahlen, Zitaten, Rechtsfragen, Kundenkommunikation.
- [ ] **Quellen verifizieren:** KI nennt Quellen, die manchmal nicht existieren → immer selbst nachschlagen.
- [ ] **Verantwortung bleibt beim Menschen:** Du bist verantwortlich für alles, was du unter deinem Namen versendest – egal ob von KI generiert.
- [ ] **Kennzeichnungspflicht beachten:** Gibt es interne Vorgaben, ob KI-generierte Inhalte als solche markiert werden müssen? → mit Vorgesetzten klären.

---

## Häufige Fragen (FAQ)

**F: Darf ich ChatGPT für E-Mails an Kunden nutzen?**  
A: Ja – wenn du keine echten Kundendaten eingibst. Schreibe die Vorlage mit fiktiven Platzhaltern und fülle sie danach manuell aus. Prüfe das Ergebnis vor dem Versand kritisch.

**F: Ich möchte einen Kundenbrief von DeepL übersetzen lassen. Erlaubt?**  
A: Nur mit der Business-Version (Datenschutzvertrag vorhanden). Mit dem kostenlosen DeepL: ❌ Kundendaten raus, Übersetzung ggf. nur für interne Texte ohne Personenbezug.

**F: Was passiert, wenn ich versehentlich Kundendaten eingegeben habe?**  
A: Sofort melden – an Vorgesetzte und/oder den Datenschutzbeauftragten. Manche Tools bieten an, den Chat-Verlauf zu löschen (z. B. ChatGPT: Einstellungen → Datenkontrolle). Dokumentiere, was eingegeben wurde.

**F: Darf ich KI zur Vorbereitung von Meetings nutzen?**  
A: Ja. Zusammenfassungen, Agendaentwürfe, Gesprächsleitfäden mit allgemeinen Themen sind unproblematisch. Keine vertraulichen Inhalte aus laufenden Projekten eingeben.

**F: Darf ich KI-generierte Bilder in offiziellen Unterlagen verwenden?**  
A: Vorsicht: Urheberrechtsfragen, Markenpolitik und interne Designstandards sind zu beachten. Für offizielle externe Dokumente: vorher mit Marketing/Compliance klären.

**F: Gibt es eine Liste genehmigter Prompts oder Vorlagen?**  
A: Noch nicht – aber genau dafür gibt es unsere [Use-Case-Sammlung](./ki-use-cases.md). Diese wächst kontinuierlich.

---

## Bei Unsicherheiten

Wenn du unsicher bist, ob eine Nutzung in Ordnung ist:

1. **Haltepunkt-Frage:** Würde ich das auch an einen externen Dienstleister mailen?
2. **Faustregel für Daten:** Lieber einmal zu vorsichtig als zu risikofreudig.
3. **Ansprechpartner:**
   - IT-Abteilung: Fragen zu freigegebenen Tools
   - Datenschutzbeauftragter: Fragen zu DSGVO und Datenkategorien
   - Vorgesetzte: Unklarheiten zu Richtlinien

---

> 📄 Dieses Dokument basiert auf der internen KI-Umfrage vom Juni 2026.  
> Es stellt eine Orientierungshilfe dar und ersetzt keine verbindlichen Unternehmensrichtlinien.  
> Stand: Juni 2026 · Erstellt auf Basis der Auswertungsergebnisse der Abteilungsumfrage.
