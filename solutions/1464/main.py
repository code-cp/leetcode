from typing import * 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 0
        n = len(nums) 
        for i in range(n):
            for j in range(i+1, n):
                prod = (nums[i]-1) * (nums[j]-1)
                max_prod = max(max_prod, prod)
        return max_prod