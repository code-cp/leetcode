from typing import * 

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = 0 
        m, n = len(nums), len(nums[0])
        
        for r in range(m): 
            nums[r].sort()
        for c in range(n): 
            col = []
            for r in range(m): 
                col.append(nums[r][c])
            ans += max(col)
            
        return ans     
            