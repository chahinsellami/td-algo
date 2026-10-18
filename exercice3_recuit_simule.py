"""Exercice 3 - voyageur de commerce avec un recuit simule.

Le nombre d'iterations demande dans le sujet est fixe a 5.
"""

from math import exp
from random import Random

from exercice3_tabou import cout, tournee_valide


def voisin(tournee, hasard):
    candidats = []
    for i in range(1, len(tournee) - 1):
        for j in range(i + 1, len(tournee)):
            nouvelle = list(tournee)
            nouvelle[i], nouvelle[j] = nouvelle[j], nouvelle[i]
            nouvelle = tuple(nouvelle)
            if tournee_valide(nouvelle):
                candidats.append(nouvelle)
    return hasard.choice(candidats)


def recuit_simule(
    iterations=5,
    essais_par_palier=15,
    temperature=30.0,
    refroidissement=0.50,
    graine=42,
):
    hasard = Random(graine)
    courant = (1, 2, 3, 4, 5, 6, 7, 8)
    meilleur = courant
    historique = []

    iteration = 0
    for _ in range(iterations):
        for _ in range(essais_par_palier):
            iteration += 1
            candidat = voisin(courant, hasard)
            difference = cout(candidat) - cout(courant)
            if difference <= 0 or hasard.random() < exp(
                -difference / temperature
            ):
                courant = candidat
            if cout(courant) < cout(meilleur):
                meilleur = courant
            historique.append((iteration, temperature, courant, cout(courant)))
        temperature *= refroidissement

    return meilleur, historique


if __name__ == "__main__":
    initiale = (1, 2, 3, 4, 5, 6, 7, 8)
    resultat, historique = recuit_simule()
    print("EXERCICE 3 - RECUIT SIMULE")
    print(f"Tournee initiale : {initiale}, cout = {cout(initiale)}")
    for iteration, temperature, tournee, valeur in historique:
        print(
            f"Iteration {iteration} : T = {temperature:.2f}, "
            f"{tournee}, cout = {valeur}"
        )
    print(f"Meilleure tournee : {resultat}, cout = {cout(resultat)}")
