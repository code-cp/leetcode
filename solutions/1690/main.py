from typing import * 

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # dp[i][j] means max diff in [i:j]
        # dp[i][j] have two previous states 
        # 1. sum[i+1:j] - dp[i+1:j]
        # 2. sum[i:j-1] - dp[i:j-1]
        # if alice plays first in dp[i][j], then in dp[i+1:j] Bob plays first 
        # so dp[i+1:j] means the max. score diff Bob can get, Alice gain -dp[i+1:j]
        # (1st player always gain dp[i][j], 2nd player gain -dp[i][j]) 
        # sum[i+1:j] is the score diff Alice can gain
        # so need to use sum[i+1:j] - dp[i+1:j] to get the total score diff  

        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        
        prefix = [0] * (n + 1) 
        for i in range(n): 
            prefix[i+1] = prefix[i] + stones[i] 
        
        # if length starts at 1, i+1 will be out of bound 
        for length in range(2, n+1): 
            i = 0
            # i + length - 1 is the end point  
            while i + length - 1 < n:
                j = i + length - 1 
                # NOTE, sum[i+1:j] = prefix[j+1] - prefix[i+1]
                dp[i][j] = max(
                    prefix[j+1] - prefix[i+1] - dp[i+1][j], 
                    prefix[j] - prefix[i] - dp[i][j-1]
                )
                i += 1    
                
        return dp[0][n-1]
        
if __name__ == "__main__":
    s = Solution() 
    
    assert s.stoneGameVII([3,1]) == 3
    # assert s.stoneGameVII([5,3,1]) == 3
    # assert s.stoneGameVII([5,3,1,4,2]) == 6