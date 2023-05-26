from typing import * 
from collections import deque 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: 
            return -1 
        
        q = deque()
        q.append((0,0))
        dirs = []
        for i in range(-1,2): 
            for j in range(-1,2): 
                dirs.append([i,j])
        n = len(grid)
        
        dist = 1
        target = (n-1,n-1)
        visited = [[0]*n for _ in range(n)]
        visited[0][0] = 1 
        while len(q) > 0: 
            q_len = len(q)
            for _ in range(q_len):
                cur = q.popleft()
                if cur[0] == target[0] and cur[1] == target[1]: 
                    return dist 
                for d in dirs: 
                    nxt = (cur[0]+d[0],cur[1]+d[1])
                    if nxt[0] < 0 or nxt[0] >= n: 
                        continue
                    if nxt[1] < 0 or nxt[1] >= n: 
                        continue 
                    if visited[nxt[0]][nxt[1]]: 
                        continue 
                    visited[nxt[0]][nxt[1]] = 1
                    if grid[nxt[0]][nxt[1]] == 1: 
                        continue  
                    q.append(nxt)
            dist += 1 
            
        return -1 
            
        