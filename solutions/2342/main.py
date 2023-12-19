from typing import * 
import heapq 

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        groups = {}
        # group the numbers that have same digit sums 
        digitSum = lambda n: sum(map(int, str(n)))
        for n in nums: 
            ds = digitSum(n)
            if groups.get(ds) is None: 
                groups[ds] = []
            heapq.heappush(groups[ds], -n)
        
        res = -1 
        for k, v in groups.items(): 
            if len(v) > 1: 
                n1 = heapq.heappop(groups[k])
                n2 = heapq.heappop(groups[k])
                res = max(res, -n1-n2)
                
        return res 