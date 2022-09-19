from typing import * 
from collections import defaultdict

class Island: 
    id = -1 
    def __init__(self, i, j, grid): 
        self.id = Island.id 
        Island.id -= 1 
        self.area = self.compute(i, j, grid)
    def compute(self, i, j, grid):
        # base case 
        if i < 0 or j < 0: 
            return 0 
        if i >= len(grid) or j >= len(grid[0]): 
            return 0 
        if grid[i][j] < 1:
            return 0 
        grid[i][j] = self.id 
        # dfs 
        count = 1 
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        for d in dirs: 
            x, y = i+d[0], j+d[1]
            count += self.compute(x, y, grid)
        return count 

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i_dict = defaultdict(int)
        res = 0 
        for i in range(m): 
            for j in range(n): 
                island = Island(i, j, grid)
                i_dict[island.id] = island.area 
                res = max(res, island.area)
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 0: 
                    area = 1 
                    ids = set()
                    if i > 0:
                        area += i_dict[grid[i-1][j]]
                        ids.add(grid[i-1][j])
                    if i < m-1 and grid[i+1][j] not in ids:
                        area += i_dict[grid[i+1][j]]
                        ids.add(grid[i+1][j])
                    if j > 0 and grid[i][j-1] not in ids:
                        area += i_dict[grid[i][j-1]]
                        ids.add(grid[i][j-1])
                    if j < n-1 and grid[i][j+1] not in ids:
                        area += i_dict[grid[i][j+1]]
                        ids.add(grid[i][j+1])
                    res = max(area, res)
        return res 

if __name__ == "__main__": 
    s = Solution()

    grid = [[0,1],[1,1]]
    assert s.largestIsland(grid) == 4

    grid = [[1,1],[1,0]]
    assert s.largestIsland(grid) == 4

    grid = [[1,0],[0,1]]
    assert s.largestIsland(grid) == 3

    grid = [[1,1],[1,1]]
    assert s.largestIsland(grid) == 4