from typing import * 

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        h = set()
        mx = -1 
        for n in nums: 
            if abs(n) > mx and -n in h: 
                mx = abs(n) 
            h.add(n)
        return mx 