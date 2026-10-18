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

## Structure du projet

```text
td-algo/
|
|-- exercice2_transport.py       Donnees et recherche taboue du transport
|-- exercice3_tabou.py           Donnees et recherche taboue du TSP
|-- exercice3_recuit_simule.py   Recuit simule du TSP
|-- visualisation.py             Generation des trois graphiques
|-- requirements.txt             Dependances Python
|-- README.md                    Documentation et resultats
|-- assets/                      Images generees pour le README
```

### Organisation du code

Les fichiers sont separes par probleme et par methode :

- `exercice2_transport.py` contient la matrice des couts, les stocks, les
  demandes, la verification des solutions et les voisins du probleme de
  transport. La fonction `recherche_taboue` genere une solution initiale,
  explore les voisins et conserve la meilleure solution.
- `exercice3_tabou.py` contient la matrice des distances du TSP, le calcul du
  cout d'une tournee, la verification des liaisons et la recherche taboue.
  Une solution est representee par un tuple de villes, avec la ville 1 comme
  point de depart.
- `exercice3_recuit_simule.py` reutilise le calcul du cout et la validation du
  fichier precedent. Il genere des permutations voisines, applique la regle
  de Metropolis et diminue progressivement la temperature.
- `visualisation.py` importe les fonctions des trois exercices, execute les
  algorithmes avec les parametres fixes, puis enregistre les graphiques dans
  `assets/`.

Le chemin d'execution des visualisations est donc :

```text
visualisation.py
    -> exercice2_transport.py
    -> exercice3_tabou.py
    -> exercice3_recuit_simule.py
    -> assets/*.png
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

## Execution et visualisations

Apres l'installation, une seule commande suffit pour executer les trois
algorithmes et regenerer les trois graphiques PNG :

```powershell
python visualisation.py
```

Les images sont enregistrees dans `assets/` :

- `assets/exercice2_transport.png` : quantites transportees et contribution
  de chaque liaison au cout total ;
- `assets/exercice3_tabou.png` : tournee obtenue et evolution du cout pendant
  la recherche taboue ;
- `assets/exercice3_recuit.png` : tournee obtenue et evolution du cout pendant
  le recuit simule.

Cette commande peut etre relancee apres chaque modification du code. Les
fichiers Python peuvent aussi etre lances individuellement depuis PowerShell
si l'on veut observer la sortie detaillee d'un seul algorithme, mais ce n'est
pas necessaire pour generer le rendu.

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

## Commande complete

```powershell
cd "C:\Users\chahi\OneDrive\Documents\tp\tp algo"
python -m pip install -r requirements.txt
python visualisation.py
```
