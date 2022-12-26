from typing import * 

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < k*2: 
            return 0 
        M = 10 ** 9 + 7
        n = len(nums)
        dp = [[0]*k for _ in range(n+1)] 
        dp[0][0] = 1  
        for i in range(1, n+1): 
            for j in range(min(nums[i-1], k)):
                dp[i][j] = dp[i-1][j] % M
            for j in range(nums[i-1], k): 
                dp[i][j] = (dp[i-1][j] + dp[i-1][j - nums[i-1]]) % M
        res = (pow(2, n, M) - sum(dp[-1]) * 2) % M
        return res 

if __name__ == "__main__": 
    s = Solution() 

    nums = [6,6]
    k = 2
    assert s.countPartitions(nums, k) == 2  

    # nums = [1,2,3,4]
    # k = 4
    # assert s.countPartitions(nums, k) == 6