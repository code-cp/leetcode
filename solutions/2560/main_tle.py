from typing import * 
import numpy as np
import math  
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = (n+1)//2+1 
        dp = np.ones((n+1, m, 2)) * float("inf")
        ans = float("inf")
        
        for i in range(1, n+1): 
            if i == 1: 
                dp[i,1,1] = nums[i-1]
            elif i == 2: 
                dp[i,1,0] = dp[i-1,1,1]
                dp[i,1,1] = nums[i-1]
            else: 
                for j in range(1, m):
                    # NOTE, use min here, not max  
                    # NOTE, use inf to init, not -1, otherwise min won't work 
                    dp[i,j,0] = min(dp[i-1,j,0], dp[i-1,j,1])
                    if j == 1: 
                        dp[i,j,1] = nums[i-1]
                    # NOTE, need to check whether dp[i-1,j-1,0] is valid 
                    # if dp[i-1,j-1,0] is not valid, then dp[i,j,1] is also not valid  
                    # eg i = 3, j = 3 
                    elif math.isfinite(dp[i-1,j-1,0]): 
                        # NOTE, the only place we use max is when adding new numbers 
                        dp[i,j,1] = max(dp[i-1,j-1,0], nums[i-1])      

        for i in range(1, n+1): 
            for j in range(k, m):
                ans = min(ans, dp[i,j,0], dp[i,j,1])

        return int(ans)
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.minCapability([2,3,5,9], 2) == 5                     
    # assert s.minCapability([2,7,9,3,1], 2) == 2                    
    # assert s.minCapability([1], 1) == 1
    assert s.minCapability([4,22,11,14,25], 3) == 25   