from solver import Labyrinth,bfs_solver,bellman_ford_solver,a_star_solver,Labyrinth3d,bfs_solver_3d
import numpy as np
laby=Labyrinth3d((5,5,5))
grid,source,aim=laby.generate()
#Test bfs_solver_3d
bfs_solver_3d=bfs_solver_3d(grid,source,aim)
a=bfs_solver_3d.solve()
print("BFS 3D Solver Path:",a)

