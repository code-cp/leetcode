from typing import * 

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        for i in range(m): 
            for j in range(n):
                if i == 0 and j == 0: 
                    continue 
                if i == 0: 
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    continue 
                if j == 0: 
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    continue 
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]
                
if __name__ == "__main__": 
    s = Solution() 

    grid = [[1,2,5],[3,2,1]]
    assert s.maxValue(grid) == 9
    
    # grid = [[1,3,1],[1,5,1],[4,2,1]]
    # assert s.maxValue(grid) == 12