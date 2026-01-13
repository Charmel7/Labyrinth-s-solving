# RÉSOLUTION DE LABYRINTHES AVEC NUMPY

## Génération du Labyrinthe

Cette partie fait référence à [Algorithms de Génération de Labyrinthes avec des Matrices en Python - Article Medium](https://python.plainenglish.io/maze-generation-algorithms-with-matrices-in-python-i-33bc69aacbc4).

**Fait amusant :** Connaissez-vous la différence entre un labyrinthe et un dédale ? Un labyrinthe fait référence à un puzzle multistructurel complexe avec des choix de chemins et de directions, tandis qu'un dédale n'a qu'un seul chemin vers le centre.

Dans ce projet, les termes labyrinthe et dédale sont utilisés de manière interchangeable.

L'algorithme est basé sur la distribution binomiale : nous commençons en mettant un mur dans tout le domaine, et grâce à une itération sur le domaine et au résultat d'un test de Bernoulli, nous décidons de creuser dans la direction du Nord ou de l'Est.

Cela nous permet de générer un beau labyrinthe que nous pouvons résoudre (en trouvant le chemin optimal de la source à la destination) avec plusieurs algorithmes.

Le premier algorithme que nous testons est la Recherche en largeur d'abord.

## Recherche en largeur d'abord (BFS)

Ici, nous considérons les différents cas de notre tableau NumPy comme des nœuds d'un graphe. Ensuite, nous pouvons appliquer l'algorithme BFS.

## Bellman-Ford

Une preuve détaillée peut être trouvée à : [Wikipédia - Algorithme de Bellman-Ford](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm)

## ACO (Approche Probabiliste)
