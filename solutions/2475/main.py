from typing import * 

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = 0 
        n = len(nums)
        for i in range(n): 
            for j in range(i+1, n): 
                if nums[i] == nums[j]: 
                    continue 
                for k in range(j+1, n):
                    if nums[i] == nums[k] or nums[j] == nums[k]: 
                        continue 
                    cnt += 1 
        return cnt  