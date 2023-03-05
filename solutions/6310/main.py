from typing import * 

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        M = 10**9 + 7 
        n = len(types) 
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        
        # base case
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1): 
            count = types[i-1][0] 
            mark = types[i-1][1] 
            # NOTE, not for j in range(mark, target+1):
            # since we can use zero of this type 
            for j in range(1, target+1):
                for k in range(count+1):
                    if k * mark <= j:
                        dp[i][j] += dp[i-1][j-k*mark] % M 
                        dp[i][j] %= M 
                    else:
                        break 
        
        return dp[n][target]

        

if __name__ == "__main__": 
    s = Solution() 

    target = 6
    types = [[6,1],[3,2],[2,3]]
    assert s.waysToReachTarget(target, types) == 7 