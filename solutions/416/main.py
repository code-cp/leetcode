from typing import List 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[0] * len(nums) for i in range(target+2)]
        # initialize
        for i in range(target+1):
            if i >= nums[0]:
                dp[i][0] = nums[0]
        for i in range(1, target+1):
            for j in range(1, len(nums)):
                if i >= nums[j]:
                    dp[i][j] = max(dp[i][j-1], dp[i-nums[j]][j-1] + nums[j])
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[target][len(nums)-1] == target

if __name__ == "__main__":
    nums = [1,5,11,5]
    s = Solution()
    assert s.canPartition(nums)
