from typing import * 

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # dp[i][k] means max. sum end at arr[i], delete k times 
        n = len(arr)
        dp = [[0]*2 for _ in range(n)]
        inf = float("inf") 
        
        dp[0][0] = arr[0]
        # dp[0][1] does not exist, since empty subarray not allowed 
        dp[0][1] = -inf 
        
        # NOTE, ans need to init with arr[0]
        # since in the for loop, arr[0] is never considered for ans 
        ans = arr[0] 
        for i in range(1, n): 
            # no deletion, if dp[i-1][0] > 0, then just add arr[i]
            # else just use arr[i]
            dp[i][0] = max(dp[i-1][0], 0) + arr[i]
            # with deletion, two cases
            # 1. do not delete arr[i], dp[i-1][1] + arr[i]
            # 2. delete arr[i], use dp[i-1][0] 
            dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0])
            ans = max([ans, dp[i][0], dp[i][1]])
            
        return ans 
        