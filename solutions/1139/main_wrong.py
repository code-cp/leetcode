from typing import * 

from collections import deque 
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def largestArea(grid):    
            memo = [[0]*n for _ in range(m)]
            res = 0 
            # consider each as bottom right corner 
            for i in range(m): 
                for j in range(n):
                    if grid[i][j] == 0: 
                        continue  
                    if i == 0 or j == 0: 
                        memo[i][j] = 1 
                    else:
                        memo[i][j] = min(
                            memo[i-1][j-1],
                            memo[i-1][j],
                            memo[i][j-1],
                        ) + 1 
                    res = max(res, memo[i][j])
            return res**2 

        
        # change 0 (surrounded by 1) to 1 
        dirs = []
        for i in range(-1, 2): 
            for j in range(-1, 2):
                if i == 0 and j == 0: 
                    continue 
                dirs.append((i, j))
        visited = [[0]*n for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                if i == 0 or j == 0: 
                    continue 
                if i == m-1 or j == n-1: 
                    continue 
                if visited[i][j] == 1: 
                    continue 
                visited[i][j] = 1 
                if grid[i][j] == 0: 
                    blob = []
                    q = deque()
                    q.append((i, j))
                    while len(q) > 0: 
                        q_size = len(q)
                        for _ in range(q_size): 
                            (i, j) = q.popleft()
                            blob.append((i, j))
                            for d in dirs: 
                                new_i, new_j = i+d[0], j+d[1]
                                if new_i < 0 or new_i >= m: 
                                    blob = []
                                    q = deque()
                                    break 
                                if new_j < 0 or new_j >= n: 
                                    blob = []
                                    q = deque()
                                    break 
                                if visited[new_i][new_j] == 1: 
                                    continue 
                                visited[new_i][new_j] = 1 
                                if grid[new_i][new_j] == 1: 
                                    continue 
                                q.append((new_i, new_j))
                    for (i,j) in blob: 
                        grid[i][j] = 1 

        area = largestArea(grid)
        return area 

if __name__ == "__main__": 
    s = Solution() 

    # [0,1,1,1]
    # [1,1,1,1]
    # [1,0,0,1]
    # [1,1,1,1]
    # [1,0,1,1]
    # [1,1,0,1]
    grid = [[0,1,1,1],[1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,1,1],[1,1,0,1]]
    assert s.largest1BorderedSquare(grid) == 4   

    # # [1,1,1,0]
    # # [1,0,1,1]
    # # [1,1,0,0]
    # # [1,1,1,1]
    # # [0,1,0,1]
    # grid = [[1,1,1,0],[1,0,1,1],[1,1,0,0],[1,1,1,1],[0,1,0,1]]
    # assert s.largest1BorderedSquare(grid) == 4   

    # grid = [[1,1,1],[1,0,1],[1,1,1]]
    # assert s.largest1BorderedSquare(grid) == 9    