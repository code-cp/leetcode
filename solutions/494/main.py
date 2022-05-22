from typing import List 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        if (total + target) % 2 == 1:
            return 0
        sum_target = (total + target) // 2
        dp = [[0] * len(nums) for _ in range(sum_target+1)]

        # initialize
        for i in range(len(nums)):
            dp[0][i] = 1
        for i in range(sum_target+1):
            if i == nums[0]:
                dp[i][0] += 1

        for i in range(sum_target+1):
            for j in range(1, len(nums)):
                if i >= nums[j]:
                    dp[i][j] = dp[i][j-1] + dp[i-nums[j]][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        result = dp[sum_target][len(nums)-1]

        return result

if __name__ == "__main__": 
    nums = [1,1,1,1,1]
    target = 3
    s = Solution()
    assert s.findTargetSumWays(nums, target) == 5

