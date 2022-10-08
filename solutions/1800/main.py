from typing import * 

# dp 
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0 
        cur_sum = 0 
        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i-1]:
                cur_sum = nums[i]
            else: 
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum

if __name__ == "__main__": 
    s = Solution() 

    nums = [10,20,30,5,10,50]
    assert s.maxAscendingSum(nums) == 65 