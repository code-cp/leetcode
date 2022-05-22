from typing import * 

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # dp table 
        dp = [0] * len(nums) 
        # init 
        dp[0] = sum([i*ele for i, ele in enumerate(nums)])
        # traverse
        total = sum(nums)
        n = len(nums)
        # F(i) = F(i-1) + sum(nums) - nums[-i]*n 
        for i in range(1, n): 
            dp[i] = dp[i-1] + total - nums[-i]*n
        # return 
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    
    result = s.maxRotateFunction([4, 3, 2, 6])
    assert result == 26 