---
applyTo: "data/**"
---

# Datenanalyse-Anweisungen

## Umfragedaten

Die Datei `data/umfrage.xlsx` (oder `data/umfrage.csv`) enthält die Ergebnisse der internen KI-Nutzungsumfrage der Finanzabteilung (Juni 2026, 6 Teilnehmende).

## Analyse-Standards

### Grundregeln
- Analysiere immer die tatsächlichen Daten – keine Annahmen oder Schätzungen
- Nenne immer absolute Zahlen UND Prozentwerte (z. B. „4 von 6 = 67 %")
- Fehlende Werte (NaN, leer) explizit kennzeichnen und kommentieren
- Datenqualitätsprobleme transparent benennen

### Umfrage-spezifische Analyse
Bei Likert-Skalen (1–5 oder ähnlich):
- Mittelwert, Median und Häufigkeitsverteilung berechnen
- Extremwerte (1 und 5) gesondert auswerten
- Keine Zahlen erfinden wenn n < 3 für Untergruppen

Bei Freitextantworten:
- Thematisch clustern
- Häufigste Nennungen zählen
- Wörtliche Zitate (anonymisiert) einbeziehen

### Ausgabe-Format
Alle Analyse-Outputs nach `output/analyse.md` schreiben.
Zahlen und Tabellen bevorzugen, Fließtext reduzieren.

## Datenschutz
- Keine persönlichen Daten (Namen, E-Mail) in Outputs
- Umfragedaten nur aggregiert ausgeben – keine Einzelauswertungen die Rückschlüsse auf Personen erlauben
- Bei n ≤ 2 in einer Gruppe: Gruppe nicht separat ausweisen
