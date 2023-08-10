from typing import * 

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
                
        # create dp 
        dp = [[0]*n for _ in range(m)]
        
        # init dp 
        for j in range(n):
            dp[0][j] = grid[0][j]
            
        # traverse 
        for i in range(1, m):
            # record min vals 
            minvals = [float("inf")]*2 
            minidx = -1 
            for j in range(n): 
                if minvals[0] > dp[i-1][j]:
                    # NOTE, Update the second minimum
                    minvals[1] = minvals[0]  
                    minvals[0] = dp[i-1][j]
                    minidx = j 
                elif minvals[1] > dp[i-1][j]: 
                    minvals[1] = dp[i-1][j] 
                    
            for j in range(n):                
                if j == minidx: 
                    pre = minvals[1]
                else: 
                    pre = minvals[0]
                dp[i][j] = pre + grid[i][j] 
                
        return min(dp[-1]) 
                
            
            

        