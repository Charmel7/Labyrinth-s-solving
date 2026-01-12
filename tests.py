from solver import Labyrinth,bfs_solver,bellman_ford_solver
laby=Labyrinth((10,10))
#Test Labyrinth
lab,source,aim=laby.generate()
print(aim)
print(source)
print(laby.neighbours(lab,1,2))
#Test bfs_solver
bfs_solver=bfs_solver(lab,source,aim)
a,b,c=bfs_solver.treat()
print(lab)
print(c)
print(bfs_solver.solve())
#Test bellman_ford_solver
bellman_ford_solver=bellman_ford_solver(lab,source,aim)
a,b=bellman_ford_solver.treat()
print(lab)
print(b)
print(bellman_ford_solver.solve())

