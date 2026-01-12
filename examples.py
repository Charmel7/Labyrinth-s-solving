from solver import Labyrinth,bfs_solver
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


labyrinth=Labyrinth((100,100))
lab,source,aim=labyrinth.generate()
bfs_solver=bfs_solver(lab,source,aim)
optimal_path=bfs_solver.solve()
#Vizualisation of bfs_solver result
cmap = ListedColormap(["black","white","green","red"])
plt.imshow(lab, cmap=cmap)
y, x = zip(*optimal_path)
plt.plot(x, y, color='blue', linewidth=2)
plt.grid(True, which='both', color='gray', linewidth=0.5)
plt.xticks(range(lab.shape[1]))
plt.yticks(range(lab.shape[0]))
plt.savefig("labyrinthe.png", dpi=300)
plt.close()
plt.imshow(lab, cmap=cmap)
