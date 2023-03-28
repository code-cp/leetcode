from tying import * 

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = {}
        n = len(nums)
        for i in range(1, n): 
            total = nums[i]+nums[i-1]
            if sums.get(total, -1) != -1:
                return True 
            sums[total] = 1 
        return False  