from typing import * 
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums] 
        heapq.heapify(nums)
        
        score = 0
        for _ in range(k): 
            n = -heapq.heappop(nums)
            score += n 
            heapq.heappush(nums, -n//3)
            
        return score 