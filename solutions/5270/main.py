from typing import * 

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        # init dp table 
        m, n = len(grid), len(grid[0]) 
        dp = [[0] * n for _ in range(m)]
        for i in range(n): 
            dp[0][i] = grid[0][i] 
        # traverse 
        for i in range(1, m): 
            for j in range(n): 
                min_c = float("inf")
                for k in range(n): 
                    min_c = min(min_c, dp[i-1][k] + moveCost[grid[i-1][k]][j]) 
                dp[i][j] = min_c + grid[i][j] 
        return min(dp[m-1])

if __name__ == "__main__": 
    s = Solution() 

    grid = [[5,3],[4,0],[2,1]]
    moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
    assert s.minPathCost(grid, moveCost) == 17 