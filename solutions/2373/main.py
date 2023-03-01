from typing import * 

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]

        def submax(grid, i, j, n): 
            m = -1 
            if i < 1 or i > n-2:
                return m
            if j < 1 or j > n-2:
                return m
            for x in range(i-1, i+2): 
                for y in range(j-1, j+2): 
                    m = max(grid[x][y], m)
            return m 

        for i in range(n-2):
            for j in range(n-2): 
                res[i][j] = submax(grid, i+1, j+1, n)

        return res 
