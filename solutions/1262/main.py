from typing import * 

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.
        n = len(nums)
        dp = [[0]*3 for _ in range(n)]
        dp[0][nums[0]%3] = nums[0]
        for i in range(1,n): 
            # NOTE, need to propagate dp[i-1]
            for j in range(3): 
                dp[i][j] = dp[i-1][j]
            for j in range(3): 
                cur = dp[i-1][j] + nums[i]
                dp[i][cur%3] = max(cur, dp[i][cur%3]) 
        return dp[-1][0]
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.maxSumDivThree([1,2,3,4,4]) == 12 