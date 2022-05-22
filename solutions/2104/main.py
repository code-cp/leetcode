from typing import * 

# TLE when submit 
# https://leetcode-cn.com/submissions/detail/276969351/testcase/
# https://leetcode-cn.com/submissions/detail/276976197/testcase/
# but if run tests individuallly can AC 
# class Solution:
#     def subArrayRanges(self, nums: List[int]) -> int:
#         # dp table 
#         n = len(nums)
#         dp = [[[[0] for _ in range(2)] for _ in range(n)] for _ in range(n)] 
#         # initialize 
#         for i in range(n): 
#             dp[i][i][0] = nums[i]
#             dp[i][i][1] = nums[i]
#         # traverse 
#         for i in range(n): 
#             for j in range(i+1, n): 
#                 dp[i][j][0] = min(dp[i][j-1][0], nums[j])
#                 dp[i][j][1] = max(dp[i][j-1][1], nums[j])
#         # get results 
#         result = 0
#         for i in range(n): 
#             for j in range(i+1, n): 
#                 result += dp[i][j][1] - dp[i][j][0]
#         return result 

# still TLE 
# class Solution:
#     def subArrayRanges(self, nums: List[int]) -> int:
#         # dp table 
#         n = len(nums)
#         dp = [[[[0] for _ in range(2)] for _ in range(n)] for _ in range(n)] 
#         # traverse 
#         result = 0
#         for i in range(n-1): 
#             dp[i][i][0] = nums[i]
#             dp[i][i][1] = nums[i]
#             for j in range(i+1, n): 
#                 dp[i][j][0] = min(dp[i][j-1][0], nums[j])
#                 dp[i][j][1] = max(dp[i][j-1][1], nums[j])
#                 # get results 
#                 result += dp[i][j][1] - dp[i][j][0]
#         return result 

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n-1): 
            mx, mn = nums[i], nums[i]
            for j in range(i+1, n): 
                mx = max(mx, nums[j])
                mn = min(mn, nums[j])
                result += mx - mn 
        return result 

if __name__ == "__main__": 
    s = Solution()

    nums = [1,2,3]
    result = s.subArrayRanges(nums)
    assert result == 4