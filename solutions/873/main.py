from typing import * 

from collections import defaultdict 
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        result = 0 
        if arr[2] == arr[0] + arr[1]: 
            dp[2][1] = 3
            result = 3 
        arr_set = set(arr)
        for i in range(3, n): 
            for j in range(i):
                diff = arr[i] - arr[j]
                if diff in arr_set:
                    k = arr.index(diff)
                    if k < j:
                        inc =  dp[j][k]+1 if dp[j][k] != 0 else 3
                        dp[i][j] = max(dp[i][j], inc)
                        result = max(result, dp[i][j])
        return result 

if __name__ == "__main__": 
    s = Solution()

    arr = [1,2,3,4,5,6,7,8]
    assert s.lenLongestFibSubseq(arr) == 5 

    arr = [1,3,7,11,12,14,18]
    assert s.lenLongestFibSubseq(arr) == 3 

    arr = [1,3,4,7,10,11,12,18,23,35]
    assert s.lenLongestFibSubseq(arr) == 6  

    arr = [2,4,7,8,9,10,14,15,18,23,32,50]
    assert s.lenLongestFibSubseq(arr) == 5