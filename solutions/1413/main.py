from typing import * 

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0 
        total = 0
        for n in nums: 
            total += n 
            min_sum = min(total, min_sum)
        if min_sum >= 0: 
            return 1 
        return -min_sum+1