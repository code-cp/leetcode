from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # dp table
        dp = [0] * len(nums)
        # initialize
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

if __name__ == "__main__": 
    nums = [1,2,3,1]
    s = Solution()
    assert s.rob(nums) == 4
