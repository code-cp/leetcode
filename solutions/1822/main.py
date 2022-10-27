from typing import * 

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums: 
            if n == 0: 
                return 0 
            if n < 0:
                res *= -1 
        return 1 if res > 0 else -1 
