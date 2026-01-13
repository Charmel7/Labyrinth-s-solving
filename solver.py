import numpy as np
print(np.__version__)
import random as rd
import numpy as np
class Labyrinth:
    def __init__(self,shape):
        self.shape=shape
        self.grid=np.zeros(self.shape)
        # We're using binary tree algorithm

    def _carveNorth(self,i,j):
        self.grid[i+1,j]=1
    def _carveEast(self,i,j):
        self.grid[i,j+1]=1

    def generate(self):
        for i in range (self.shape[0]-1):
            for j in range(self.shape[1]-1):
                if i==0 :
                    self._carveEast(i,j)
                if j==self.shape[1]-1:
                    self._carveNorth(i,j)
                else:
                    decision=np.random.randint(0,2)
                    if decision==0:
                        self._carveNorth(i,j)
                    else:
                        self._carveEast(i,j)
        source=(0,0)
        aim=(self.shape[0]-1,self.shape[1]-1)
        self.grid[aim[0],aim[1]]=3
        self.grid[source[0],source[1]]=2
        return self.grid,source,aim

    def _moveLeft(self,a:int ,b:int ) ->bool:
        if a-1<self.shape[0] and b<self.shape[1] and a>=0 and b>=0:
            return True
        return False
    def _moveRight(self,a:int ,b:int ) ->bool:
        if a+1<self.shape[0] and b<self.shape[1] and a>=0 and b>=0:
            return True
        return False
    def _moveUp(self,a:int ,b:int ) ->bool:
        if a<self.shape[0] and b+1<self.shape[1] and a>=0 and b>=0:
            return True
        return False
    def _moveDown(self,a:int ,b:int ) ->bool:
        if a<self.shape[0] and b-1<self.shape[1] and a>=0 and b>=0:
            return True
        return False
    def neighbours(self,lab,a:int,b:int)->list[list]:
        neighbours_list=[]
        if self._moveRight(a,b) and (lab[a+1,b]==1 or lab[a+1,b]==3 or lab[a+1,b]==2):
            neighbours_list.append((a+1,b))
        if self._moveLeft(a,b) and (lab[a-1,b]==1 or lab[a-1,b]==3 or lab[a-1,b]==2):
            neighbours_list.append((a-1,b))
        if self._moveUp(a,b) and (lab[a,b+1]==1 or lab[a,b+1]==3 or lab[a,b+1]==2):
            neighbours_list.append((a,b+1))
        if self._moveDown(a,b) and (lab[a,b-1]==1 or lab[a,b-1]==3 or lab[a,b-1]==2):

            neighbours_list.append((a,b-1))
        return neighbours_list
    
class File:
    def __init__(self):
        self.file=[]
    def first(self):
        return self.file[0]
    def isEmpty(self):
        if len(self.file)==0:
            return True
        return False
    def enfile(self,point:tuple):
        self.file.append(point)
    def defile(self):
        self.file.pop(0)

class bfs_solver:
    def __init__ (self,lab:np.ndarray,source,aim):
        self.lab=lab
        self.source=source
        self.aim=aim
   
    def treat(self):
        file = File() # To visit nodes
        laby=Labyrinth(self.lab.shape)
        file.enfile(tuple(self.source))
        dist={tuple(self.source): 0 }
        parent={tuple(self.source): None}
        color={"white":[],
               "grey":[],
               "black":[]}
        for i in range( self.lab.shape[0]) :
            for j in range (self.lab.shape[1]):
                if (self.lab[i,j]==1 or self.lab[i,j]==2 or self.lab[i,j]==3):
                    color["white"].append((i,j)) 
        while not file.isEmpty():
            vertice=file.first()
            for neighbour in laby.neighbours(self.lab,vertice[0],vertice[1]):
                if  neighbour in color["white"]:
                    color["grey"].append(neighbour)
                    color["white"].remove(neighbour)
                    dist[tuple(neighbour)]=dist[tuple(vertice)]+1
                    parent[tuple(neighbour)]=vertice
                    file.enfile(tuple(neighbour))
            file.defile()
            color["black"].append(tuple(vertice))
            if tuple(vertice) in color["grey"]:
                color["grey"].remove(tuple(vertice))
        return dist,parent,color
    

    def backtracking(self,parent,source,aim):
        path=[]
        current=aim
        if tuple(aim) not in parent:
            return None  # Aim is unreachable
        while current != source:
            path.append(current)
            current=parent[current]
        path.append(source)
        path.reverse()
        return path

    
    def solve(self):
        dist,parent,color=self.treat()
        path=self.backtracking(parent,tuple(self.source),tuple(self.aim))
        return path
    
class bellman_ford_solver:
    def __init__ (self,lab:np.ndarray,source,aim):
        self.lab=lab
        self.source=source
        self.aim=aim
    def treat(self):
        dist={}
        parent={}
        for i in range(self.lab.shape[0]):
            for j in range(self.lab.shape[1]):
                if self.lab[i,j]==2 or self.lab[i,j]==3 or self.lab[i,j]==1:
                    dist[(i,j)]=float('inf')
                    parent[(i,j)]=None
        dist[tuple(self.source)]=0
        laby=Labyrinth(self.lab.shape)
        for _ in range(len(dist)-1):
            for u in dist.keys():
                for v in laby.neighbours(self.lab,u[0],u[1]):
                    if v in dist:
                        if dist[u]+1<dist[v]:
                            dist[v]=dist[u]+1
                            parent[v]=u

        # Check for negative-weight cycles (not applicable here since all weights are positive but...)
        for u in dist.keys():
                for v in laby.neighbours(self.lab,u[0],u[1]):
                    if v in dist:
                        if dist[u]+1<dist[v]:
                            raise ValueError("Graph contains a negative-weight cycle") # That is not possible here but generally good to check
        return dist,parent
    def backtracking(self,parent,source,aim):
        path=[]
        current=aim
        if tuple(aim) not in parent:
            return None  # Aim is unreachable
        while current != source:
            path.append(current)
            current=parent[current]
        path.append(source)
        path.reverse()
        return path
    def solve(self):
        dist,parent=self.treat()
        path=self.backtracking(parent,self.source,self.aim)
        return path
class aco_solver:
    def __init__ (self,lab:np.ndarray,source,aim):
        self.lab=lab
        self.source=source
        self.aim=aim

    def treat(self):
        num_ants = 50
        pheromone = np.ones(self.lab.shape) * 0.1
        best_path = None
        best_length = float('inf')

        for iteration in range(100):
            all_paths = []
            for _ in range(num_ants):
                current_position = self.source
                path = [current_position]
                while current_position != self.aim:
                    neighbours = self.neighbours(self.lab, current_position[0], current_position[1])
                    if not neighbours:
                        break
                    probabilities = []
                    for neighbour in neighbours:
                        pheromone_level = pheromone[neighbour]
                        distance = 1  # Assuming uniform distance
                        probabilities.append(pheromone_level / distance)
                    probabilities = np.array(probabilities)
                    probabilities /= probabilities.sum()
                    next_position = neighbours[np.random.choice(len(neighbours), p=probabilities)]
                    path.append(next_position)
                    current_position = next_position

                all_paths.append(path)
                path_length = len(path)
                if path_length < best_length:
                    best_length = path_length
                    best_path = path

            pheromone *= 0.95  # Evaporation
            for path in all_paths:
                for position in path:
                    pheromone[position] += 1.0 / len(path)  # Deposit pheromone

        return best_path

    def solve(self):
        path = self.treat()
        return path

    


    