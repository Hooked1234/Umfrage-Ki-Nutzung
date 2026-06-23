# Datenschutz-Ampel: Was darf in KI-Tools?

> **Kernaussage**: Diese Ampel hilft Mitarbeitenden, in Sekunden zu entscheiden, welche Inhalte in öffentliche KI-Tools dürfen – und welche nie. Datenschutz war die größte Hürde in der Umfrage (3 von 6 Nennungen).

## Grafik

![Datenschutz-Ampel](png/datenschutz-ampel.png)

<details>
<summary>Mermaid-Version (interaktiv in VS Code/GitHub)</summary>

```mermaid
flowchart TD
    classDef gruen fill:#d5e8d4,stroke:#82b366,color:#000
    classDef gelb fill:#fff2cc,stroke:#d6b656,color:#000
    classDef rot fill:#f8cecc,stroke:#b85450,color:#000
    classDef frage fill:#dae8fc,stroke:#6c8ebf,color:#000

    START([Ich möchte etwas in ein KI-Tool eingeben]):::frage --> Q1{Enthält es echte<br/>Personen- oder<br/>Kundendaten?}

    Q1 -->|Ja| ROT
    Q1 -->|Nein| Q2{Ist es ein internes,<br/>vertrauliches<br/>Dokument?}

    Q2 -->|Ja| GELB
    Q2 -->|Nein| GRUEN

    subgraph ROTBOX [" "]
        ROT["🔴 ROT – NIE in öffentliche Tools<br/>Kundendaten · Schuldnerdaten · Namen<br/>Bank-/Zahlungsdaten · Verträge · Scoring<br/>interne Zahlen · Passwörter"]:::rot
    end

    subgraph GELBBOX [" "]
        GELB["🟡 GELB – Nur mit geeignetem Tool<br/>interne Prozessbeschreibungen<br/>nicht-sensible interne Inhalte<br/>aggregierte Zahlen → M365 Copilot"]:::gelb
    end

    subgraph GRUENBOX [" "]
        GRUEN["🟢 GRÜN – Unkritisch nutzbar<br/>allgemeine Fragen · öffentliche Infos<br/>fiktive Beispiele · Texte ohne Personenbezug<br/>Gliederungen · Formulierungshilfen"]:::gruen
    end
```

</details>

## Interpretation

Die meisten Alltagsaufgaben (Formulieren, Zusammenfassen, Ideen) fallen in den grünen Bereich – sofern Platzhalter statt echter Daten verwendet werden. Der rote Bereich umfasst alle für EOS als Finanzdienstleister besonders schützenswerten Datenkategorien.

> 🧭 **Faustregel:** Würdest du es einem externen Dienstleister unverschlüsselt mailen? Nein → nicht eingeben.

*Datenquelle: Umfrage KI-Nutzung, Finanzabteilung, Juni 2026 (n=6) · Datenkategorien: ki-datenschutz-guide.md*
