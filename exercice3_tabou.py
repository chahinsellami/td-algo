"""Exercice 3 - voyageur de commerce avec une recherche taboue."""

from random import Random

INF = 100
COUTS = (
    (0, 14, 15, INF, INF, INF, INF, 17),
    (14, 0, 13, 14, 20, INF, INF, 21),
    (15, 13, 0, 11, 21, 17, 9, 9),
    (INF, 14, 11, 0, 11, 10, 8, 20),
    (INF, 20, 21, 11, 0, 15, 18, INF),
    (INF, INF, 17, 10, 15, 0, 9, INF),
    (INF, INF, 9, 8, 18, 9, 0, 13),
    (17, 21, 9, 20, INF, INF, 13, 0),
)


def cout(tournee):
    return sum(
        COUTS[tournee[i] - 1][tournee[(i + 1) % len(tournee)] - 1]
        for i in range(len(tournee))
    )


def tournee_valide(tournee):
    return all(
        COUTS[tournee[i] - 1][tournee[(i + 1) % len(tournee)] - 1] < INF
        for i in range(len(tournee))
    )


def voisins(tournee):
    for i in range(1, len(tournee) - 1):
        for j in range(i + 1, len(tournee)):
            nouvelle = list(tournee)
            nouvelle[i], nouvelle[j] = nouvelle[j], nouvelle[i]
            mouvement = tuple(sorted((tournee[i], tournee[j])))
            nouvelle = tuple(nouvelle)
            if tournee_valide(nouvelle):
                yield nouvelle, mouvement


def recherche_taboue(
    iterations=100, taille_tabou=7, graine=3, retourner_historique=False
):
    hasard = Random(graine)
    courant = (1, 2, 3, 4, 5, 6, 7, 8)
    meilleur = courant
    tabou = []
    historique = [(0, cout(courant), cout(meilleur))]

    for _ in range(iterations):
        candidats = [
            (tournee, mouvement)
            for tournee, mouvement in voisins(courant)
            if mouvement not in tabou
        ]
        if not candidats:
            tabou = []
            candidats = list(voisins(courant))
        if not candidats:
            break
        hasard.shuffle(candidats)
        candidat, mouvement = min(candidats, key=lambda item: cout(item[0]))
        courant = candidat
        if cout(courant) < cout(meilleur):
            meilleur = courant
        historique.append((len(historique), cout(courant), cout(meilleur)))
        tabou.append(mouvement)
        tabou = tabou[-taille_tabou:]

    if retourner_historique:
        return meilleur, historique
    return meilleur


if __name__ == "__main__":
    initiale = (1, 2, 3, 4, 5, 6, 7, 8)
    resultat = recherche_taboue()
    print("EXERCICE 3 - RECHERCHE TABOUE")
    print(f"Tournee initiale : {initiale}, cout = {cout(initiale)}")
    print(f"Meilleure tournee : {resultat}, cout = {cout(resultat)}")
