from typing import * 

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][j][k] 
        # ith num 
        # is j
        # which appears k times 
        # dp[i][6][2] = dp[i-1][6][1]
        # dp[i][6][1] = (dp[i-1][1][?] + ... + dp[i-1][5][?])
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n)]

        for j in range(6):
            dp[0][j][1] = 1  

        M = 10**9 + 7 
        for i in range(1, n): 
            for j in range(6): 
                for k in range(1, rollMax[j]+1): 
                    if k > 1: 
                        dp[i][j][k] = dp[i-1][j][k-1]
                    else: 
                        for m in range(6): 
                            if m == j: 
                                continue 
                            for n in range(1, rollMax[m]+1): 
                                dp[i][j][k] += dp[i-1][m][n]
                                dp[i][j][k] %= M 

        res = 0
        for j in range(6):
            for k in range(1, rollMax[j]+1): 
                res += dp[-1][j][k] 
                res %= M 

        return res 

if __name__ == "__main__": 
    s = Solution() 

    n = 2
    rollMax = [1,1,2,2,2,3]
    assert s.dieSimulator(n, rollMax) == 34 