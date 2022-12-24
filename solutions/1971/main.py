from typing import * 

from collections import deque 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True 
        adjacency_list = {}
        for e in edges:  
            if e[0] not in adjacency_list:
                adjacency_list[e[0]] = []
            if e[1] not in adjacency_list:
                adjacency_list[e[1]] = []
            adjacency_list[e[0]].append(e[1])
            adjacency_list[e[1]].append(e[0])
        visited = [0] * n 
        nodes = deque()
        nodes.append(source)
        visited[source] = 1 
        while len(nodes) > 0: 
            num = len(nodes)
            for _ in range(num): 
                node = nodes.popleft()
                for v in adjacency_list[node]:
                    if v == destination: 
                        return True  
                    if visited[v] != 1: 
                        nodes.append(v)
                        visited[v] = 1 
        return False 

if __name__ == "__main__": 
    s = Solution() 

    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    assert s.validPath(n, edges, source, destination)
