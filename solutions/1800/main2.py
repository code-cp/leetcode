from typing import * 

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 数组后面补一个数，避免对0的判断
        nums.append(-1)
        max_sum = nums[0]  
        cur_sum = nums[0] 
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                cur_sum = nums[i]
            else: 
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum