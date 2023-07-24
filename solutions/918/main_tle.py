from typing import * 

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums.extend(nums)
        res = -float("inf")
        cur = 0  
        i = 0 
        while i < len(nums)//2: 
            j = i 
            cur = nums[j]
            res = max(res, cur)
            if cur <= 0: 
                i += 1 
                continue 
            j += 1 
            while j < (len(nums)//2+i) and cur > 0: 
                cur += nums[j]
                res = max(res, cur)
                j += 1 
            i += 1 
        return res 
    
if __name__ == "__main__": 
    s = Solution()
   
    # assert s.maxSubarraySumCircular([3,-1,2,-1]) == 4 
    assert s.maxSubarraySumCircular([5,-3,5]) == 10
    # assert s.maxSubarraySumCircular([-3,-2,-3]) == -2 