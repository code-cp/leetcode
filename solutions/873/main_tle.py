from typing import * 

# TLE 
from collections import defaultdict 
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        if arr[2] == arr[0] + arr[1]: 
            dp[2][1] = 3
        for i in range(3, n): 
            for j in range(i):
                for k in range(j): 
                    if arr[j] + arr[k] == arr[i]:
                        inc =  dp[j][k]+1 if dp[j][k] != 0 else 3
                        dp[i][j] = max(dp[i][j], inc)
        return max(map(max, dp)) 

if __name__ == "__main__": 
    s = Solution()

    # arr = [1,2,3,4,5,6,7,8]
    # assert s.lenLongestFibSubseq(arr) == 5 

    # arr = [1,3,7,11,12,14,18]
    # assert s.lenLongestFibSubseq(arr) == 3 

    arr = [1,3,4,7,10,11,12,18,23,35]
    assert s.lenLongestFibSubseq(arr) == 6  