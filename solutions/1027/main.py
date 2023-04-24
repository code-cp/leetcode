from typing import * 

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # dp[i][k] means end at i, diff is k
        # dp[i][k] = max(dp[j][k]+1), for k = nums[i]-nums[j] 
        
        # NOTE, Not needed since there is no i-1 or j-1 terms         
        # nums = [0]+nums
        n = len(nums)
        # NOTE, init value is 1, not 0, since each number itself is a valid seq
        # if we init dp, then no need to add dp=[0]+dp step, since every dp value is already initialized 
        # if we don't init dp, then need dp=[0]+dp step, since we need to use [0] to initialize every dp value  
        dp = [[1]*(500*2+1) for _ in range(n)]
        
        ans = 0 
        for i in range(n): 
            for j in range(i):
                # make the diff non-negative 
                # [-500,500] -> [0,1000]
                k = nums[i]-nums[j]+500 
                dp[i][k] = max(dp[i][k], dp[j][k]+1)
                ans = max(ans, dp[i][k])
        
        return ans 

if __name__ == "__main__": 
    s = Solution() 
    
    assert s.longestArithSeqLength([3,6,9,12]) == 4 
                
        
        