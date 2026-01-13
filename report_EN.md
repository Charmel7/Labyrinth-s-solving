# MAZE SOLVING WITH NUMPY

## Maze Generation

This section references [Maze Generation Algorithms with Matrices in Python - Medium Article](https://python.plainenglish.io/maze-generation-algorithms-with-matrices-in-python-i-33bc69aacbc4).

**Fun fact:** Do you know the difference between a maze and a labyrinth? A maze is a complex branching puzzle with multiple pathways and directional choices, whereas a labyrinth contains only a single path leading to the center.

In this project, the terms maze and labyrinth are used interchangeably.

The algorithm is based on the binomial distribution: We start by filling the entire domain with walls, then iterate through the domain. Based on the result of a Bernoulli trial, we decide whether to carve passages in the North or East direction.

This approach allows us to generate intricate mazes that we can then solve (finding the optimal path from source to goal) using various algorithms.

The first algorithm we implement is Breadth-First Search.

## Breadth-First Search (BFS)

In this approach, we treat each cell in our NumPy array as a node in a graph. We then apply the standard BFS algorithm to find the shortest path.

## Bellman-Ford

A detailed mathematical proof can be found at: [Wikipedia - Bellman-Ford Algorithm](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm)

## ACO (Probabilistic Approach)

This section covers the Ant Colony Optimization approach to pathfinding, which uses probabilistic methods to simulate ant behavior.
