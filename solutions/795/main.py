from typing import * 

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        last_above = -1 
        last_within = -1 
        for i, n in enumerate(nums): 
            if n > right: 
                last_above = i 
            elif n >= left: 
                last_within = i 
                res += last_within - last_above 
            else: 
                res += max(0, last_within - last_above)
        return res 

if __name__ == "__main__": 
    s = Solution()

    nums = [2,9,2,5,6]
    left = 2
    right = 8
    assert s.numSubarrayBoundedMax(nums, left, right) == 7 

    nums = [2,1,4,3]
    left = 2
    right = 3
    assert s.numSubarrayBoundedMax(nums, left, right) == 3 