# TD2 - Recherche operationnelle

Travail realise en Python dans le cadre du TD2 de metaheuristiques.

## Presentation du projet

Ce projet contient deux problemes d'optimisation :

| Exercice | Probleme | Methode utilisee |
|---|---|---|
| 2 | Transport de containers entre depots et magasins | Recherche taboue |
| 3 | Voyageur de commerce avec 8 villes | Recherche taboue et recuit simule |

L'algorithme genetique n'est pas inclus, car le message de l'enseignante
demande uniquement la recherche taboue et le recuit simule pour l'exercice 3.

## Organisation des fichiers

```text
td-algo/
|
|-- exercice2_transport.py       Probleme de transport
|-- exercice3_tabou.py           TSP avec recherche taboue
|-- exercice3_recuit_simule.py   TSP avec recuit simule
|-- visualisation.py             Generation des graphiques
|-- requirements.txt             Dependances Python
|-- README.md                    Documentation du projet
|-- assets/                      Images utilisees dans le README
```

## Prerequis

- Python 3.9 ou une version plus recente ;
- pip ;
- Matplotlib, installe avec `requirements.txt`.

Le projet ne necessite pas de solveur externe. Les algorithmes et les calculs
principaux sont implementes directement en Python.

## Installation sous Windows

Ouvrir PowerShell, puis se placer dans le dossier du projet :

```powershell
cd "C:\Users\chahi\OneDrive\Documents\tp\tp algo"
```

Installer la dependance necessaire :

```powershell
python -m pip install -r requirements.txt
```

Si la commande `python` n'est pas reconnue, utiliser le lanceur Windows :

```powershell
py -m pip install -r requirements.txt
```

## Execution des programmes

### Exercice 2 : transport

```powershell
python exercice2_transport.py
```

Le programme affiche la matrice des quantites envoyees et le cout total.
Le resultat attendu est un cout de 52.

### Exercice 3 : recherche taboue

```powershell
python exercice3_tabou.py
```

Le programme affiche la tournee initiale, son cout, puis la meilleure tournee
trouvee par la recherche taboue. Le resultat attendu est un cout de 98.

### Exercice 3 : recuit simule

```powershell
python exercice3_recuit_simule.py
```

Le programme utilise 5 paliers de temperature et 15 essais par palier. Il
affiche le cout de la tournee apres chaque essai. Le meilleur cout attendu est
98.

## Generation des visualisations

Pour generer les trois graphiques PNG :

```powershell
python visualisation.py
```

Les images sont enregistrees dans le dossier `assets/` :

- `assets/exercice2_transport.png` : quantites transportees et contribution
  de chaque liaison au cout total ;
- `assets/exercice3_tabou.png` : tournee obtenue et evolution du cout pendant
  la recherche taboue ;
- `assets/exercice3_recuit.png` : tournee obtenue et evolution du cout pendant
  le recuit simule.

Les images peuvent etre regenerees a tout moment apres une modification du
code. Elles sont integrees directement dans ce README.

## Donnees de l'exercice 2

Les stocks disponibles sont :

```text
D1 = 8 containers
D2 = 9 containers
```

Les demandes des magasins sont :

```text
M1 = 4 containers
M2 = 5 containers
M3 = 8 containers
```

La matrice des couts unitaires est :

| Depot | M1 | M2 | M3 |
|---|---:|---:|---:|
| D1 | 5 | 3 | 4 |
| D2 | 6 | 7 | 2 |

La recherche taboue conserve les stocks et les demandes. Une solution obtenue
est :

| Depot | M1 | M2 | M3 | Total |
|---|---:|---:|---:|---:|
| D1 | 3 | 5 | 0 | 8 |
| D2 | 1 | 0 | 8 | 9 |

Son cout est :

```text
3*5 + 5*3 + 1*6 + 8*2 = 52
```

![Resultat graphique de l'exercice 2](assets/exercice2_transport.png)

## Donnees de l'exercice 3

La tournee initiale imposee par l'enonce est :

```text
1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 1
```

Son cout est :

```text
14 + 13 + 11 + 11 + 15 + 9 + 13 + 17 = 103
```

Le graphe est non complet. Lorsqu'une liaison est absente du tableau, elle
recoit une penalite de 100. Les permutations qui utilisent une liaison
absente sont filtrees dans le voisinage.

### Recherche taboue

Le voisinage est construit en permutant deux villes, en gardant la ville 1
comme point de depart. Une liste taboue memorise les derniers mouvements afin
d'eviter les cycles. La meilleure tournee obtenue est :

```text
1 - 8 - 3 - 7 - 6 - 5 - 4 - 2 - 1
```

Son cout est 98.

![Resultat graphique de la recherche taboue](assets/exercice3_tabou.png)

### Recuit simule

Le recuit simule utilise la regle d'acceptation suivante :

```text
Delta <= 0 : la solution est acceptee
Delta > 0  : acceptation avec la probabilite exp(-Delta / T)
```

La temperature est mise a jour avec :

```text
T(nouveau) = 0.50 * T(ancien)
```

Les parametres utilises sont :

| Parametre | Valeur |
|---|---:|
| Temperature initiale | 30 |
| Nombre de paliers | 5 |
| Essais par palier | 15 |
| Coefficient de refroidissement | 0.50 |
| Graine aleatoire | 42 |

Avec ces parametres, le meilleur cout obtenu est 98.

![Resultat graphique du recuit simule](assets/exercice3_recuit.png)

## Resultats finaux

| Programme | Cout obtenu |
|---|---:|
| Exercice 2 - recherche taboue | 52 |
| Exercice 3 - tournee initiale | 103 |
| Exercice 3 - recherche taboue | 98 |
| Exercice 3 - recuit simule | 98 |

## Reproductibilite

Les graines aleatoires sont fixees dans les programmes afin d'obtenir les
meme resultats lors de plusieurs executions. Pour tester d'autres executions,
il est possible de modifier le parametre `graine` dans les fonctions
correspondantes.

## Resume des commandes

```powershell
cd "C:\Users\chahi\OneDrive\Documents\tp\tp algo"
python -m pip install -r requirements.txt
python exercice2_transport.py
python exercice3_tabou.py
python exercice3_recuit_simule.py
python visualisation.py
```
