# GitHub Copilot Instructions – KI-Umfrage Projekt

## Projektkontext

Dieses Projekt wertet eine interne KI-Nutzungsumfrage der Finanzabteilung aus (6 Teilnehmende, Juni 2026).
Das Ziel ist ein praxisorientiertes Lernpfad-Dokument, das Mitarbeitenden zeigt, wie sie KI-Tools sicher und effektiv im Arbeitsalltag einsetzen können.

## Kernziele

1. **Umfragedaten analysieren** – Wissensstand, Nutzungsverhalten, Lernbedarf und Priorisierung
2. **Umfrageergebnisse bewerten** – Themen, Qualität und didaktische Eignung einschätzen
3. **Lernpfad entwerfen** – Stufenweiser, auf den Bedarf zugeschnittener Lernpfad
4. **Dokument schreiben** – Verständliches Lern- und Hilfedokument auf Deutsch
5. **Visualisieren** – Charts, Diagramme und strukturierte Grafiken

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
| Data Analyst | (MCP: pandas-mcp-server) | Umfragedaten auswerten |
| Survey Evaluator | `.github/agents/survey-evaluator.agent.md` | Ergebnisse bewerten |
| Learning Path Designer | `.github/agents/learning-path-designer.agent.md` | Lernpfad entwerfen |
| Technical Writer | `.github/agents/technical-writer.agent.md` | Dokument schreiben |
| Information Designer | `.github/agents/information-designer.agent.md` | Visualisierungen erstellen |

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
