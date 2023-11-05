from typing import * 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_map = {}
        for n in nums: 
            nums_map[n] = nums_map.get(n, 0) + 1 
            if nums_map[n] == 3: 
                del nums_map[n]
        return next(iter(nums_map))