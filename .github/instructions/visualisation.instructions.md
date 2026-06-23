---
applyTo: "output/visualisierungen/**"
---

# Visualisierungs-Standards

## Allgemeine Prinzipien

### Klarheit über Schönheit
- Jede Grafik muss ohne Erklärung verständlich sein
- Titel und Beschriftungen sind Pflicht
- Keine Grafik ohne Erkenntnisaussage

### Farbpalette (einheitlich)
| Verwendung | Farbe | Hex |
|---|---|---|
| Grundlagen / Pflicht | Blau | `#dae8fc` |
| Anwendung / Mittel | Grün | `#d5e8d4` |
| Vertiefung / Fortgeschritten | Orange/Gelb | `#fff2cc` |
| Kritisch / Warnung | Rot | `#f8cecc` |
| Neutral / Hintergrund | Grau | `#f5f5f5` |

## Mermaid-Standards

### Flowcharts (Lernpfade)
```mermaid
flowchart TD
    classDef grundlagen fill:#dae8fc,stroke:#6c8ebf
    classDef anwendung fill:#d5e8d4,stroke:#82b366
    classDef vertiefung fill:#fff2cc,stroke:#d6b656
```
- Richtung: TD (top-down) für Lernpfade, LR (links-rechts) für Prozesse
- Knotenbeschriftungen: kurz (max. 5 Wörter)
- Emojis erlaubt für schnelle visuelle Einordnung

### Diagramme
- Immer Titel als erster Kommentar im Code
- Achsenbeschriftungen auf Deutsch
- Legende nur wenn nötig (lieber direkte Beschriftung)

## Ausgabe-Format

Jede Visualisierung in einer eigenen `.md`-Datei unter `output/visualisierungen/`:

```markdown
# [Titel der Grafik]

> **Kernaussage**: [Ein Satz, was diese Grafik zeigt und was die wichtigste Erkenntnis ist]

## Grafik

[Mermaid-Code oder Chart-Definition]

## Interpretation
[2-3 Sätze: Was bedeutet das für den Lernpfad?]

*Datenquelle: Umfrage KI-Nutzung, Finanzabteilung, Juni 2026 (n=6)*
```

## Namenskonvention

| Grafik | Dateiname |
|---|---|
| Datenschutz-Ampel | `datenschutz-ampel.md` |
| Anwendungsfälle Balken | `anwendungsfaelle-balken.md` |
| Skill-Matrix | `skill-matrix.md` |
| Priorisierungsmatrix | `priorisierungsmatrix.md` |
