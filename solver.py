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

#improved with Gemini
import numpy as np

class Labyrinth3d:
    def __init__(self, shape):
        """
        Shape should ideally be (height, width, depth) with odd numbers
        to allow for a wall-and-passage structure.
        """
        # Ensure shape is odd for wall/path representation
        self.shape = tuple(s if s % 2 != 0 else s + 1 for s in shape)
        # 0 = Wall, 1 = Path
        self.grid = np.zeros(self.shape, dtype=int)

    def generate(self):
        #  Fill cells (odd coordinates)
        for z in range(1, self.shape[2], 2):
            for y in range(1, self.shape[1], 2):
                for x in range(1, self.shape[0], 2):
                    self.grid[x, y, z] = 1
                    
                    # 2. Binary Tree Logic: Carve toward North, East, OR Up
                    directions = []
                    if x + 2 < self.shape[0]: directions.append((1, 0, 0)) # East
                    if y + 2 < self.shape[1]: directions.append((0, 1, 0)) # North
                    if z + 2 < self.shape[2]: directions.append((0, 0, 1)) # Up

                    if directions:
                        dx, dy, dz = directions[np.random.randint(len(directions))]
                        # Carve the wall between current cell and the next
                        self.grid[x + dx, y + dy, z + dz] = 1

        # Define start and end points
        source = (1, 1, 1)
        aim = (self.shape[0] - 2, self.shape[1] - 2, self.shape[2] - 2)
        
        self.grid[source] = 2  # Start
        self.grid[aim] = 3     # End
        
        return self.grid, source, aim

    def get_neighbors(self, pos):
        """ Returns valid walkable neighbors for pathfinding """
        x, y, z = pos
        results = []
        # Check all 6 directions
        offsets = [(2,0,0), (-2,0,0), (0,2,0), (0,-2,0), (0,0,2), (0,0,-2)]
        
        for dx, dy, dz in offsets:
            nx, ny, nz = x + dx, y + dy, z + dz
            # Check boundaries
            if 0 <= nx < self.shape[0] and 0 <= ny < self.shape[1] and 0 <= nz < self.shape[2]:
                # Check if the path between is carved (the wall at mid-point)
                if self.grid[x + dx//2, y + dy//2, z + dz//2] == 1:
                    results.append((nx, ny, nz))
        return results


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

class bfs_solver_3d:

    def __init__ (self,lab:np.ndarray,source,aim):
        self.lab=lab
        self.source=source
        self.aim=aim
   
    def treat(self):
        file = File() # To visit nodes
        laby=Labyrinth3d(self.lab.shape)
        file.enfile(tuple(self.source))
        dist={tuple(self.source): 0 }
        parent={tuple(self.source): None}
        color={"white":[],
               "grey":[],
               "black":[]}
        for i in range(self.lab.shape[0]):
            for j in range(self.lab.shape[1]):
                for k in range(self.lab.shape[2]):
                    if (self.lab[i,j,k]==1 or self.lab[i,j,k]==2 or self.lab[i,j,k]==3):
                        color["white"].append((i,j,k))
        
        while not file.isEmpty():
            vertice=file.first()
            for neighbour in laby.neighbours(self.lab,vertice[0],vertice[1],vertice[2]):
                if neighbour in color["white"]:
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

    #A* algorithm implementation

class a_star_solver:
    def __init__(self, lab: np.ndarray, source, aim):
        self.lab = lab
        self.source = source
        self.aim = aim
    
    def heuristic(self, pos):
        """Manhattan distance heuristic"""
        return abs(pos[0] - self.aim[0]) + abs(pos[1] - self.aim[1])
    
    def treat(self):
        laby = Labyrinth(self.lab.shape)
        open_set = [(self.heuristic(self.source), self.source)]
        came_from = {}
        g_score = {tuple(self.source): 0}
        f_score = {tuple(self.source): self.heuristic(self.source)}
        
        while open_set:
            # Get node with lowest f_score
            open_set.sort(key=lambda x: x[0])
            _, current = open_set.pop(0)
            
            if current == self.aim:
                # Reconstruct path
                path = [current]
                while tuple(current) in came_from:
                    current = came_from[tuple(current)]
                    path.append(current)
                path.reverse()
                return path
            
            for neighbour in laby.neighbours(self.lab, current[0], current[1]):
                tentative_g_score = g_score[tuple(current)] + 1
                
                if tuple(neighbour) not in g_score or tentative_g_score < g_score[tuple(neighbour)]:
                    came_from[tuple(neighbour)] = current
                    g_score[tuple(neighbour)] = tentative_g_score
                    f_score[tuple(neighbour)] = tentative_g_score + self.heuristic(neighbour)
                    
                    if neighbour not in [node for _, node in open_set]:
                        open_set.append((f_score[tuple(neighbour)], neighbour))
        
        return None  # No path found
    
    def solve(self):
        path = self.treat()
        return path
