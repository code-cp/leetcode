from typing import * 
from collections import deque 
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def checkValid(r, c):
            nonlocal m 
            nonlocal n 
            nonlocal grid 
            if r < 0 or r >= m: 
                return False 
            if c < 0 or c >= n: 
                return False 
            if grid[r][c] == 1: 
                return False 
            return True 
        
        # Exclude connected group of 0s on the borders because they are not closed island.
        borders = []
        for r in range(m): 
            borders.append((r,0))
            borders.append((r,n-1))
        for c in range(n): 
            borders.append((0,c))
            borders.append((m-1,c))            
        for (r,c) in borders:
            if grid[r][c] != 0: 
                continue
            visited[r][c] = 1   
            q = deque()
            q.append((r,c))
            while len(q) > 0: 
                r, c = q.popleft()
                # mark as invalid 
                grid[r][c] = 1
                for d in dirs: 
                    nr, nc = r+d[0], c+d[1]
                    if not checkValid(nr, nc): 
                        continue  
                    if grid[nr][nc] != 0: 
                        continue 
                    if visited[nr][nc] != 0: 
                        continue 
                    visited[nr][nc] = 1 
                    q.append((nr,nc))
                    
        # iterate all 0
        ans = 0 
        for i in range(m): 
            for j in range(n):
                # NOTE, r, c is already used, need to use i,j here  
                if not checkValid(i,j): 
                    continue 
                if visited[i][j] != 0: 
                    continue 
                if grid[i][j] != 0: 
                    continue 
                ans += 1 
                # # for debugging 
                # grid[i][j] = ans 
                q = deque()
                q.append((i,j))
                visited[i][j] = 1 
                while len(q) > 0: 
                    r, c = q.popleft()
                    for d in dirs: 
                        nr, nc = r+d[0], c+d[1]
                        if not checkValid(nr, nc): 
                            continue  
                        if grid[nr][nc] != 0: 
                            continue 
                        if visited[nr][nc] != 0: 
                            continue 
                        visited[nr][nc] = 1 
                        q.append((nr,nc))
                        
        return ans 
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]) == 1 
    # assert s.closedIsland([[0,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,1],[1,0,0,0,0,1,0,1],[0,1,0,0,0,1,0,1],[1,0,0,1,0,1,0,1],[1,1,1,1,0,0,1,1],[1,0,0,0,0,0,1,1],[0,1,1,1,1,1,1,1]]) == 1 
    assert s.closedIsland([[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]]) == 4 