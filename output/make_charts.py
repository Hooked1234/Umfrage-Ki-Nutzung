"""Erzeugt PNG-Visualisierungen fuer die KI-Orientierungshilfe."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

OUT = os.path.join(os.path.dirname(__file__), "visualisierungen", "png")
os.makedirs(OUT, exist_ok=True)

# Farbpalette (einheitlich, abgestimmt auf Instructions)
GRUEN = "#82b366"; GRUEN_F = "#d5e8d4"
GELB = "#d6b656"; GELB_F = "#fff2cc"
ROT = "#b85450"; ROT_F = "#f8cecc"
BLAU = "#6c8ebf"; BLAU_F = "#dae8fc"
GRAU = "#666666"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 11

# -------------------------------------------------------------------
# 1. Datenschutz-Ampel
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
ax.set_title("Datenschutz-Ampel: Was darf in KI-Tools?", fontsize=15, fontweight="bold", pad=14)

ampel = [
    (7.0, ROT_F, ROT, "ROT  –  NIE in oeffentliche Tools",
     "Kundendaten · Schuldnerdaten · Namen · Adressen\nBank-/Zahlungsdaten · Vertraege · Scoring-Daten\ninterne Zahlen, Strategien · Passwoerter, API-Keys"),
    (3.9, GELB_F, GELB, "GELB  –  Nur mit geeignetem Tool",
     "interne Prozessbeschreibungen · aggregierte Zahlen\nnicht-sensible interne Inhalte  →  M365 Copilot"),
    (0.8, GRUEN_F, GRUEN, "GRUEN  –  Unkritisch nutzbar",
     "allgemeine Fragen · oeffentliche Infos · fiktive Beispiele\nTexte ohne Personenbezug · Gliederungen, Formulierungen"),
]
for y, fill, edge, title, body in ampel:
    box = FancyBboxPatch((0.4, y), 9.2, 2.7, boxstyle="round,pad=0.1,rounding_size=0.15",
                         linewidth=2.5, edgecolor=edge, facecolor=fill)
    ax.add_patch(box)
    # Farbiger Marker-Kreis links als Ampel-Punkt
    ax.add_patch(plt.Circle((1.0, y + 1.9), 0.32, color=edge, zorder=4))
    ax.text(1.7, y + 2.25, title, fontsize=12.5, fontweight="bold", va="top")
    ax.text(0.75, y + 1.35, body, fontsize=10, va="top", color="#222222")

fig.text(0.5, 0.02, "Faustregel: Wuerdest du es einem Externen unverschluesselt mailen? Nein -> nicht eingeben.",
         ha="center", fontsize=9, style="italic", color=GRAU)
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(os.path.join(OUT, "datenschutz-ampel.png"), dpi=150, bbox_inches="tight")
plt.close()

# -------------------------------------------------------------------
# 2. Anwendungsfaelle Balken
# -------------------------------------------------------------------
faelle = ["Recherche", "Uebersetzung", "Ideen", "Texte", "Kommunikation", "Datenanalyse"]
werte = [83, 67, 67, 50, 33, 33]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(faelle, werte, color=BLAU, edgecolor=BLAU, width=0.62)
for b, v in zip(bars, werte):
    ax.text(b.get_x() + b.get_width()/2, v + 1.5, f"{v}%", ha="center", fontweight="bold", fontsize=11)
ax.set_ylim(0, 100)
ax.set_ylabel("Anteil der Befragten")
ax.set_title("KI-Anwendungsfaelle in der Finanzabteilung (n=6)", fontsize=14, fontweight="bold", pad=12)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "anwendungsfaelle-balken.png"), dpi=150, bbox_inches="tight")
plt.close()

# -------------------------------------------------------------------
# Helper fuer Quadranten-Charts
# -------------------------------------------------------------------
def quadrant(filename, title, xlabel, ylabel, q_labels, points, q_colors):
    fig, ax = plt.subplots(figsize=(8.5, 7))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axhspan(0.5, 1, 0.0, 0.5, color=q_colors[0], alpha=0.30)  # oben links
    ax.axhspan(0.5, 1, 0.5, 1.0, color=q_colors[1], alpha=0.30)  # oben rechts
    ax.axhspan(0, 0.5, 0.0, 0.5, color=q_colors[2], alpha=0.30)  # unten links
    ax.axhspan(0, 0.5, 0.5, 1.0, color=q_colors[3], alpha=0.30)  # unten rechts
    ax.axhline(0.5, color=GRAU, linewidth=1)
    ax.axvline(0.5, color=GRAU, linewidth=1)
    qpos = [(0.25, 0.93), (0.75, 0.93), (0.25, 0.07), (0.75, 0.07)]
    for (qx, qy), lbl in zip(qpos, q_labels):
        ax.text(qx, qy, lbl, ha="center", va="center", fontsize=10.5,
                fontweight="bold", color="#333333")
    for px, py, name in points:
        ax.plot(px, py, "o", color=BLAU, markersize=9, markeredgecolor="white", zorder=5)
        ax.annotate(name, (px, py), textcoords="offset points", xytext=(8, 5),
                    fontsize=9.5, fontweight="bold")
    ax.set_xlabel(xlabel, fontsize=11); ax.set_ylabel(ylabel, fontsize=11)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, filename), dpi=150, bbox_inches="tight")
    plt.close()

# 3. Priorisierungsmatrix: Nutzen (y) x Aufwand (x)
quadrant(
    "priorisierungsmatrix.png",
    "Nutzen vs. Einstiegsaufwand",
    "Einstiegsaufwand  (niedrig  ->  hoch)",
    "Nutzen fuer Alltag  (niedrig  ->  hoch)",
    ["Quick Wins\n(sofort starten)", "Strategisch\n(planen)",
     "Fuellthemen\n(optional)", "Aufwaendig\n(abwaegen)"],
    [(0.20, 0.85, "Texte"), (0.18, 0.90, "Zusammenf."), (0.27, 0.80, "Uebersetzen"),
     (0.24, 0.70, "Ideen"), (0.33, 0.64, "E-Mail"), (0.37, 0.78, "Recherche"),
     (0.72, 0.75, "Datenanalyse"), (0.58, 0.28, "Bildgen.")],
    [GRUEN_F, GELB_F, GRAU, ROT_F],
)

# 4. Skill-Matrix: Wissensstand (x) x Anwendungssicherheit (y)
quadrant(
    "skill-matrix.png",
    "Wissensstand vs. Anwendungssicherheit (n=6)",
    "Wissensstand  (wenig  ->  viel)",
    "Anwendungssicherheit  (gering  ->  hoch)",
    ["Mutig\n(Wissen ausbauen)", "Souveraen",
     "Einsteiger", "Gebremst\n(Sicherheit geben)"],
    [(0.80, 0.40, "P1"), (0.60, 0.80, "P2"), (0.60, 0.60, "P3"),
     (0.20, 0.20, "P4"), (0.80, 1.0, "P5"), (0.40, 0.60, "P6")],
    [GELB_F, GRUEN_F, ROT_F, BLAU_F],
)

print("Alle PNGs erzeugt in:", OUT)
for f in sorted(os.listdir(OUT)):
    print(" -", f)
