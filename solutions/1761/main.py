from typing import * 
import math 
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        M = 401 
        connect = [[0]*M for _ in range(M)]
        degree = [0]*M 
        nex = DefaultDict(list)
        
        for e in edges: 
            connect[e[0]][e[1]] = 1 
            connect[e[1]][e[0]] = 1 
            degree[e[0]] += 1 
            degree[e[1]] += 1 
            
            # change undirected edge to directed edge 
            # this avoids searching for the same trio 
            x = min(e[0], e[1]) 
            y = max(e[0], e[1])
            nex[x].append(y) 
            
        res = float("inf")
        for a in range(1, n+1): 
            for i in range(len(nex[a])): 
                for j in range(i+1, len(nex[a])):
                    b = nex[a][i] 
                    c = nex[a][j]   
                    if connect[b][c] == 1:
                        res = min(res, degree[a]+degree[b]+degree[c]-6)
                        
        return res if math.isfinite(res) else -1 
        
        