from typing import * 

import heapq 

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total / 2 
        nums = [-x for x in nums]
        heapq.heapify(nums)
        ans = 0 
        
        while total > target: 
            x = heapq.heappop(nums)
            x /= 2 
            total += x  
            heapq.heappush(nums, x)
            ans += 1 
        
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.halveArray([5,19,8,1]) == 3        
        
        