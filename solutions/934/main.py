from typing import * 

from collections import deque 
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [[0,1],[0,-1],[-1,0],[1,0]]

        invalid = lambda r, c: r < 0 or c < 0 or r == n or c == n 

        # fill one island in visited
        # NOTE, no need to identify the island border
        visited = set()
        def dfs(r, c): 
            # base case 
            if invalid(r, c) or grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c)) 
            for d in direction: 
                dfs(r+d[0], c+d[1])
        
        def bfs(): 
            res = 0 
            q = deque(visited)
            while q: 
                q_len = len(q)
                for _ in range(q_len): 
                    r, c = q.popleft()
                    for d in direction:
                        new_r, new_c = r+d[0], c+d[1]
                        if invalid(new_r, new_c) or (new_r, new_c) in visited: 
                            continue 
                        if grid[new_r][new_c] == 1: 
                            return res 
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
                res += 1 

        for r in range(n): 
            for c in range(n): 
                if grid[r][c] == 1: 
                    dfs(r, c)
                    return bfs()

if __name__ == "__main__": 
    s = Solution()

    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    assert s.shortestBridge(grid) == 1 