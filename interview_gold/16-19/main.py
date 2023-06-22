from typing import * 
from collections import deque 
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        ponds = []
        
        def checkValid(i, j): 
            nonlocal m 
            nonlocal n 
            if i < 0 or i >= m: 
                return False 
            if j < 0 or j >= n: 
                return False 
            return True 
        
        dirs = []
        for i in range(-1,2): 
            for j in range(-1,2): 
                dirs.append([i,j])
        
        visited = [[0]*n for _ in range(m)] 
        
        for i in range(m): 
            for j in range(n): 
                if land[i][j] != 0: 
                    continue
                if visited[i][j] == 1:
                    continue  
                q = deque()
                q.append((i,j))
                visited[i][j] = 1
                area = 1  
                while len(q) > 0:
                    x,y = q.popleft()
                    for d in dirs: 
                        r, c = x+d[0], y+d[1]
                        if not checkValid(r,c):
                            continue 
                        if visited[r][c] == 1: 
                            continue 
                        if land[r][c] != 0: 
                            continue 
                        visited[r][c] = 1 
                        area += 1 
                        q.append((r,c))
                ponds.append(area)
        ponds.sort()
        return ponds
    
if __name__ == "__main__": 
    s = Solution()
    
    print(s.pondSizes([
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1]
    ]))