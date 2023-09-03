from typing import * 

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        M = 10**9 + 7 
        arr.sort()
        dp = {}
        n = len(arr)
        for i in range(n): 
            dp[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0 and dp.get(arr[i]//arr[j], -1) > 0:
                    dp[arr[i]] += (dp[arr[j]] * dp[arr[i]//arr[j]]) % M 
        ans = 0 
        for k, v in dp.items(): 
            ans += v % M 
            ans %= M 
        return ans  
            