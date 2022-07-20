from typing import * 

from copy import deepcopy
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        if k == 0: 
            res = grid 
        for d in range(k):
            if d != 0:
                grid = deepcopy(res)
            for i in range(m):
                for j in range(n-2, -1, -1):
                    res[i][j+1] = grid[i][j]
                if i != m-1:
                    res[i+1][0] = grid[i][n-1]
                else: 
                    res[0][0] = grid[i][n-1]
        return res 

if __name__ == "__main__": 
    s = Solution()

    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    assert s.shiftGrid(grid, k) == [[9,1,2],[3,4,5],[6,7,8]]

    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    k = 4
    assert s.shiftGrid(grid, k) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    grid = [[100]]
    k = 0
    assert s.shiftGrid(grid, k) == [[100]]