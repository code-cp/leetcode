from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # check input
        if len(nums) == 1:
            return nums[0]
        # dp table
        dp = [0] * len(nums)
        # initialize
        dp[0] = nums[0]
        # traverse dp table
        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(*dp)

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    assert s.maxSubArray(nums) == 6
