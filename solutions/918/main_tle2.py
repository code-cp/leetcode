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
            nex = i+1 
            while j < (len(nums)//2+i) and cur > 0: 
                if nums[j] > 0 and nex == i+1: 
                    nex = j 
                cur += nums[j]
                res = max(res, cur)
                j += 1 
            i = nex 
        return res 
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.maxSubarraySumCircular([0,5,8,-9,9,-7,3,-2]) == 16
    # assert s.maxSubarraySumCircular([3,-1,2,-1]) == 4 
    # assert s.maxSubarraySumCircular([5,-3,5]) == 10
    # assert s.maxSubarraySumCircular([-3,-2,-3]) == -2 