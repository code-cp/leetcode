from typing import * 
import math 
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp[i][k] means for days 0-i, min. sum of each max. of k subarray
        # dp[i][k] = dp[j-1][k-1] + max(j:i)
        
        jobDifficulty = [0]+jobDifficulty
        n = len(jobDifficulty)
        dp = [[float("inf")]*(d+1) for _ in range(n)]
        
        # 初始化，没有任务的困难度是0 
        dp[0][0] = 0 
        
        for i in range(1, n): 
            for k in range(1, min(d,i)+1):
                mx = jobDifficulty[i]
                for j in range(i, k-1, -1):
                    # NOTE, 倒叙遍历，可以每次更新max
                    mx = max(mx, jobDifficulty[j]) 
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1]+mx)
        
        if not math.isfinite(dp[-1][-1]):
            return -1  
        return dp[-1][-1]

if __name__ == "__main__": 
    s = Solution() 
    
    jobDifficulty = [6,5,4,3,2,1]
    d = 2
    assert s.minDifficulty(jobDifficulty, d) == 7 