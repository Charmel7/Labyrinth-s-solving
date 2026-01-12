# MAZE SOLVING WITH NUMPY

## Generation of the Labyrinth 

This part refers to [[Maze Generation Algorithms with Matrices in Python,Medium Article](https://python.plainenglish.io/maze-generation-algorithms-with-matrices-in-python-i-33bc69aacbc4)]

**Fun fact** Do you know the difference between a maze and a labyrinth ? A maze refers to a complex branching multistructural puzzle with choices of path and direction but a labyrinth has only a single path to a center .

But here A Labyrinth is a maze. 

The Algorithm is based on the binomial distribution : We start by putting a wall in all the domain and with an iteration on the domain and the result of a Bernouilli test we take the decision to carve in the direction of North or in the direction of east.

This permit to generate a beatiful maze we can solve(finding the optimal path from the source to the aim ) with multiple algorithms.

The first we try is the Breadth-first search.

# Breadth-first search(BFS)

Here we consider the differens cases of our numpy table as a node of a graph. Then we can use the bfs .

# Bellman_ford

The great of the proof is on [Wiki,Bellman_ford Algorithm](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm)

# ACO(probabilistic approach)


