"""Creation des graphiques du rendu.

Lancer `python visualisation.py` pour creer les images dans assets/.
"""

from math import cos, pi, sin
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from exercice2_transport import COUTS as COUTS_TRANSPORT
from exercice2_transport import recherche_taboue as tabou_transport
from exercice3_recuit_simule import recuit_simule
from exercice3_tabou import COUTS, cout, recherche_taboue


DOSSIER = Path(__file__).parent / "assets"


def graphique_transport():
    solution = tabou_transport()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    matrice = np.array(solution)
    image = axes[0].imshow(matrice, cmap="Blues", vmin=0, vmax=8)
    axes[0].set_title("Exercice 2 - Affectation optimale")
    axes[0].set_xticks(range(3), ["M1\n(demande 4)", "M2\n(demande 5)", "M3\n(demande 8)"])
    axes[0].set_yticks(range(2), ["D1 (stock 8)", "D2 (stock 9)"])
    for i in range(2):
        for j in range(3):
            axes[0].text(j, i, str(matrice[i, j]), ha="center", va="center", fontsize=18)
    fig.colorbar(image, ax=axes[0], label="containers")
    axes[0].set_xlabel("Quantite envoyee")

    cout_total = sum(
        solution[i][j] * COUTS_TRANSPORT[i][j]
        for i in range(2)
        for j in range(3)
    )
    axes[1].bar(["D1-M1", "D1-M2", "D1-M3", "D2-M1", "D2-M2", "D2-M3"],
                [solution[i][j] * COUTS_TRANSPORT[i][j] for i in range(2) for j in range(3)],
                color="#4c9be8")
    axes[1].set_title(f"Contribution au cout (total = {cout_total})")
    axes[1].set_ylabel("cout")
    axes[1].tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(DOSSIER / "exercice2_transport.png", dpi=150)
    plt.close(fig)


def positions_villes():
    return {
        ville: (
            cos(2 * pi * (ville - 1) / 8),
            sin(2 * pi * (ville - 1) / 8),
        )
        for ville in range(1, 9)
    }


def dessiner_tournee(ax, tournee, titre):
    positions = positions_villes()
    for ville in range(1, 9):
        x, y = positions[ville]
        ax.scatter(x, y, s=650, color="#f5d547" if ville == 1 else "white",
                   edgecolor="#555", zorder=3)
        ax.text(x, y, str(ville), ha="center", va="center", fontsize=11, zorder=4)
    tournee_complete = tournee + (tournee[0],)
    for a, b in zip(tournee_complete, tournee_complete[1:]):
        x1, y1 = positions[a]
        x2, y2 = positions[b]
        cout_arete = COUTS[a - 1][b - 1]
        couleur = "#e67e22" if cout_arete >= 100 else "#2c82c9"
        ax.annotate("", (x2, y2), (x1, y1),
                    arrowprops={"arrowstyle": "->", "color": couleur, "lw": 2})
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, str(cout_arete),
                color=couleur, fontsize=8)
    ax.set_title(f"{titre}\ncout = {cout(tournee)}")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.axis("off")


def graphique_tsp_tabou():
    resultat, historique = recherche_taboue(retourner_historique=True)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    dessiner_tournee(axes[0], resultat, "Exercice 3 - Recherche taboue")
    iterations = [ligne[0] for ligne in historique]
    courant = [ligne[1] for ligne in historique]
    meilleur = [ligne[2] for ligne in historique]
    axes[1].plot(iterations, courant, "o-", label="cout courant")
    axes[1].plot(iterations, meilleur, "s--", label="meilleur cout")
    axes[1].set_title("Evolution du cout")
    axes[1].set_xlabel("iteration")
    axes[1].set_ylabel("cout de la tournee")
    axes[1].grid(alpha=0.3)
    axes[1].legend()
    fig.tight_layout()
    fig.savefig(DOSSIER / "exercice3_tabou.png", dpi=150)
    plt.close(fig)


def graphique_tsp_recuit():
    resultat, historique = recuit_simule()
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    dessiner_tournee(axes[0], resultat, "Exercice 3 - Recuit simule")
    iterations = [ligne[0] for ligne in historique]
    couts = [ligne[3] for ligne in historique]
    axes[1].plot(iterations, couts, color="#2c82c9", label="cout courant")
    meilleur = []
    minimum = float("inf")
    for valeur in couts:
        minimum = min(minimum, valeur)
        meilleur.append(minimum)
    axes[1].plot(iterations, meilleur, "s--", color="#2ca02c", label="meilleur cout")
    axes[1].set_title("Evolution du cout")
    axes[1].set_xlabel("essai")
    axes[1].set_ylabel("cout de la tournee")
    axes[1].grid(alpha=0.3)
    axes[1].legend()
    fig.tight_layout()
    fig.savefig(DOSSIER / "exercice3_recuit.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    DOSSIER.mkdir(exist_ok=True)
    graphique_transport()
    graphique_tsp_tabou()
    graphique_tsp_recuit()
    print("Images creees dans le dossier assets/")
