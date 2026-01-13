# MAZE SOLVING WITH NUMPY

## Generation of the Labyrinth

This part refers to [Maze Generation Algorithms with Matrices in Python - Medium Article](https://python.plainenglish.io/maze-generation-algorithms-with-matrices-in-python-i-33bc69aacbc4).

**Fun fact:** Do you know the difference between a maze and a labyrinth? A maze refers to a complex branching multistructural puzzle with choices of path and direction, but a labyrinth has only a single path to a center.

In this project, maze and labyrinth are used interchangeably.

The algorithm is based on the binomial distribution: We start by putting a wall in all the domain, and through iteration on the domain and the result of a Bernoulli test, we decide whether to carve in the direction of North or East.

This allows us to generate a beautiful maze that we can solve (finding the optimal path from the source to the goal) with multiple algorithms.

The first algorithm we try is the Breadth-first search.

## Breadth-first search (BFS)

Here we consider the different cases of our NumPy table as nodes of a graph. Then we can apply the BFS algorithm.

## Bellman-Ford

A detailed proof can be found at: [Wikipedia - Bellman-Ford Algorithm](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm)

## ACO (Probabilistic Approach)

The ACO approach is 