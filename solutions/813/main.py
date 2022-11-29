from typing import * 

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # dp[i][k] means use up to i nums, divide to k groups 
        # dp[i][1] = avg(nums[0], nums[i])
        # dp[i][k>1] = max(dp[j][k-1] + avg(nums[j], nums[i])) for every j 
        n = len(nums)
        
        pre_sum = [0]*(n+1)
        for i in range(1, n+1): 
            pre_sum[i] = pre_sum[i-1]+nums[i-1]
        
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        
        avg = lambda i, j: (pre_sum[i] - pre_sum[j]) / (i - j)

        # k == 1 
        for i in range(1, n+1): 
            dp[i][1] = avg(i, 0) 

        # k > 1 
        for i in range(1, n+1): 
            for k_id in range(2, k+1): 
                for j in range(1, i): 
                    dp[i][k_id] = max(dp[i][k_id], dp[j][k_id-1] + avg(i, j)) 

        return dp[-1][-1]

if __name__ == "__main__": 
    s = Solution() 

    nums = [9,1,2,3,9]
    k = 3
    assert s.largestSumOfAverages(nums, k) == 20 
        