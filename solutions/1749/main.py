from typing import * 

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_val, max_val = float("inf"), float("-inf") 
        n = len(nums)
        min_dp = [0]*(n+1) 
        max_dp = [0]*(n+1)
        
        for i, x in enumerate(nums): 
            min_dp[i+1] = min(x, min_dp[i]+x) 
            max_dp[i+1] = max(x, max_dp[i]+x)
            
        res = max(max(max_dp), -min(min_dp)) 
        
        return res 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.maxAbsoluteSum([1,-3,2,3,-4]) == 5