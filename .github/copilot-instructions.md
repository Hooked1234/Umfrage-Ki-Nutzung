# GitHub Copilot Instructions – KI-Umfrage Projekt

## Projektkontext

Dieses Projekt wertet eine interne KI-Nutzungsumfrage der Finanzabteilung aus (6 Teilnehmende, Juni 2026).
Das Ziel ist ein praxisorientiertes Lernpfad-Dokument, das Mitarbeitenden zeigt, wie sie KI-Tools sicher und effektiv im Arbeitsalltag einsetzen können.

## Ziel des Dokuments

Ein **kompaktes internes Hilfsdokument** zur KI-Nutzung in der Finanzabteilung.

> Dieses Dokument dient als praktische Orientierung zur sicheren und sinnvollen KI-Nutzung im Arbeitsalltag. Es basiert auf einer internen Umfrage und zeigt typische Anwendungsfälle, Grundregeln zum Datenschutz sowie direkt nutzbare Prompt-Beispiele. Es ersetzt keine verbindlichen Vorgaben von IT, Datenschutz oder Compliance.

**Kein mehrstufiger Lernpfad** – stattdessen ein Nachschlagewerk, das sofort brauchbar ist.

## Kernziele

1. **Datenschutz-Klarheit** – Was darf rein, was nicht? Früh und konkret (Ampel-Modell)
2. **Anwendungssicherheit stärken** – Vertrauen in korrektes Handeln, nicht mehr Theorie
3. **Sofort nutzbare Prompts** – Vorlagen zum Kopieren, keine Einleitung nötig
4. **Bestehende Inhalte konsolidieren** – `ki-datenschutz-guide.md` + `ki-use-cases.md` zusammenführen
5. **Visualisierungen** – Ampel-Grafik, Priorisierungsmatrix, Nutzungsübersicht

## Sprache und Ton

- **Primärsprache: Deutsch** – alle Outputs und Analysen auf Deutsch
- Ton: klar, sachlich, praxisnah – keine akademische Sprache
- Zielgruppe: Finanzabteilung, keine Entwickler
- Fachbegriffe immer erklären

## Dateistruktur

```
data/           → Umfragedaten (umfrage.xlsx / umfrage.csv)
output/         → Analyseergebnisse, Lernpfad, Dokumente
output/visualisierungen/  → Charts und Diagramme
```

## Agenten in diesem Projekt

| Agent | Datei | Zweck |
|-------|-------|-------|
| Survey Evaluator | `.github/agents/survey-evaluator.agent.md` | Umfrage auswerten → `output/analyse.md` ✅ bereits erstellt |
| Technical Writer | `.github/agents/technical-writer.agent.md` | Gesamtdokument schreiben → `output/KI-Orientierungshilfe.md` |
| Information Designer | `.github/agents/information-designer.agent.md` | Visualisierungen → `output/visualisierungen/` |

> **Reihenfolge:** Survey Evaluator → Technical Writer → Information Designer

## MCP-Server

- `pandas-mcp-server` – Datenanalyse (Excel/CSV)
- `mcp-plots` – Diagramme und Charts
- `mermaid-mcp-server` – Flowcharts und Lernpfade
- `Office-Word-MCP-Server` – Word-Dokument generieren

## Qualitätsstandards

- Alle Analysen müssen auf den tatsächlichen Umfragedaten basieren
- Keine erfundenen Zahlen oder Annahmen ohne Datenbasis
- Word-Dokument muss ohne technisches Vorwissen lesbar sein
- Visualisierungen müssen beschriftet und verständlich sein
