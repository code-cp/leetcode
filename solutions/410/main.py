from typing import * 

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i][j] = min of largest sum of splitting [0, j] into i groups 
        dp = [[float("inf")] * n for _ in range(k+1)]
         
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1, n): 
            prefix[i] = prefix[i-1] + nums[i]
        
        # init dp 
        # if only split in 1 group, 
        # then max. sum is just prefix 
        for i in range(n):
            dp[1][i] = prefix[i]
        
        # i is group  
        for i in range(2, k+1):
            # j is index, need to start at least i-1
            # since we need i groups 
            # eg, i = 2, j = 1, then groups are [0], [1] 
            for j in range(i-1, n):
                # split [m+1, j] to the last group 
                # [0, m] into i-1 groups  
                for m in range(j): 
                    dp[i][j] = min(
                        dp[i][j], 
                        max(
                            dp[i-1][m],
                            # sum of [m+1, j]
                            prefix[j]-prefix[m], 
                        )
                    ) 
                    
        return dp[k][n-1]