from typing import * 

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dp = 0 
        pre = nums[0]
        for i in range(1, len(nums)): 
            cur = max(pre+1, nums[i])
            dp += cur - nums[i] 
            pre = cur 
        return dp