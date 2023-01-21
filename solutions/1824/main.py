from typing import * 

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[float("inf")]*3 for _ in range(n)]
        # init 
        dp[0][0] = 1
        dp[0][1] = 0  
        dp[0][2] = 1
        # traverse 
        for i in range(1, n): 
            for j in range(3): 
                if obstacles[i]-1 == j: 
                    continue 
                dp[i][j] = dp[i-1][j]
            for j in range(3): 
                if obstacles[i]-1 == j: 
                    continue 
                dp[i][j] = min(dp[i][j], 
                    dp[i][max(0, j-2)]+1, 
                    dp[i][max(0, j-1)]+1, 
                    dp[i][min(2, j+1)]+1,
                    dp[i][min(2, j+2)]+1,
                )
        return min(dp[-1])

if __name__ == "__main__": 
    s = Solution() 

    obstacles = [0,1,2,3,0]
    assert s.minSideJumps(obstacles) == 2 