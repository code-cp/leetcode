from typing import * 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed = {}
        for i in range(len(nums)): 
            if nums[i] in traversed: 
                return [traversed[nums[i]], i]
            traversed[target-nums[i]] = i