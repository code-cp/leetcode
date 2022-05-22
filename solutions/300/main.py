from typing import List 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # check input
        if len(nums) == 1:
            return 1
        # dp table
        # initialize
        dp = [1] * len(nums)
        # traverse dp table
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(*dp)

if __name__ == "__main__": 
    nums = [10,9,2,5,3,7,101,18]
    s = Solution()
    assert s.lengthOfLIS(nums) == 4
