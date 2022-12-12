from typing import * 

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0 
        for i in range(1, len(nums)): 
            new_val = max(nums[i-1]+1, nums[i])
            res += new_val - nums[i]
            nums[i] = new_val 
        return res 