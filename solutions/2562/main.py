from typing import * 

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0 
        while len(nums) > 1: 
            res += int(str(nums[0])+str(nums[-1]))
            nums.pop(0)
            nums.pop()
        if len(nums) == 1:
            res += nums[0]
        return res 