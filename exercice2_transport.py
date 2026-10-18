"""Exercice 2 - probleme de transport resolu par recherche taboue.

Le probleme est equilibre : les stocks totalisent 17 containers et les
demandes totalisent aussi 17 containers.
"""

from random import Random


COUTS = (
    (5, 3, 4),  # D1 vers M1, M2, M3
    (6, 7, 2),  # D2 vers M1, M2, M3
)
STOCKS = (8, 9)
DEMANDES = (4, 5, 8)


def cout(solution):
    """Calcule le cout d'une solution."""
    return sum(
        solution[i][j] * COUTS[i][j]
        for i in range(2)
        for j in range(3)
    )


def solution_complete(premiere_ligne):
    """Construit la deuxieme ligne a partir des demandes."""
    deuxieme_ligne = tuple(
        DEMANDES[j] - premiere_ligne[j] for j in range(3)
    )
    return (tuple(premiere_ligne), deuxieme_ligne)


def solution_valide(solution):
    return (
        all(x >= 0 for ligne in solution for x in ligne)
        and all(sum(solution[i]) == STOCKS[i] for i in range(2))
        and all(
            sum(solution[i][j] for i in range(2)) == DEMANDES[j]
            for j in range(3)
        )
    )


def voisins(solution):
    """Genere les voisins en transferant un container entre deux magasins."""
    ligne = solution[0]
    for depart in range(3):
        for arrivee in range(3):
            if depart == arrivee or ligne[depart] == 0:
                continue
            nouvelle_ligne = list(ligne)
            nouvelle_ligne[depart] -= 1
            nouvelle_ligne[arrivee] += 1
            voisin = solution_complete(nouvelle_ligne)
            if solution_valide(voisin):
                yield voisin, (depart, arrivee)


def recherche_taboue(iterations=40, taille_tabou=5, graine=7):
    """Recherche taboue simple et deterministe."""
    hasard = Random(graine)
    depart = list(DEMANDES)
    while sum(depart) > STOCKS[0]:
        depart[hasard.randrange(3)] -= 1
    courant = solution_complete(depart)
    meilleur = courant
    liste_taboue = []

    for _ in range(iterations):
        candidats = [
            (s, mouvement)
            for s, mouvement in voisins(courant)
            if mouvement not in liste_taboue
        ]
        if not candidats:
            break
        candidat, mouvement = min(candidats, key=lambda item: cout(item[0]))
        courant = candidat
        if cout(courant) < cout(meilleur):
            meilleur = courant
        liste_taboue.append((mouvement[1], mouvement[0]))
        liste_taboue = liste_taboue[-taille_tabou:]

    return meilleur


def afficher(solution):
    print("          M1   M2   M3 | total")
    for i, ligne in enumerate(solution):
        print(f"D{i + 1}       {ligne[0]:>2}   {ligne[1]:>2}   {ligne[2]:>2} | {sum(ligne)}")
    print(f"Cout total : {cout(solution)}")


if __name__ == "__main__":
    resultat = recherche_taboue()
    print("EXERCICE 2 - RECHERCHE TABOUE")
    afficher(resultat)
