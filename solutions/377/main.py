from typing import List 

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        # dp table
        dp = [[0] * (len(nums)+1) for _ in range(target+1)]
        # initialize
        for i in range(len(nums)+1):
            dp[0][i] = 1

        # order of for loops does not matter
        for j in range(1, len(nums)+1):
            for i in range(target+1):
                # this step needs sorting the num
                if i < nums[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    # need to update all previous combinations using each coin
                    for k in range(j):
                        dp[i][j] += dp[i-nums[k]][j]

        return dp[-1][-1]

if __name__ == "__main__": 
    nums = [1,2,3] 
    target = 4
    s = Solution()
    assert s.combinationSum4(nums, target) == 7
