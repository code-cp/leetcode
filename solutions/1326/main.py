from typing import * 

import math 
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # limit range in [0,n]
        valid_ranges = []
        for i, r in enumerate(ranges): 
            start = max(0, i-r)
            end = min(n, i+r)
            valid_ranges.append([start, end])
        
        # sort by start 
        valid_ranges.sort(key=lambda x: x[0])
        
        # dp[i]: min. intervals to cover [0,i]
        # assume startj <= i <= endj 
        # then dp[i] = min(dp[i], 1+dp[startj])

        dp = [float("inf")] * (n+1)
        dp[0] = 0 
        for start, end in valid_ranges: 
            # cannot cover the entire range 
            if math.isinf(dp[start]): 
                return -1 
            for j in range(start, end+1): 
                dp[j] = min(dp[j], dp[start]+1)
        
        return dp[n]


if __name__ == "__main__": 
    s = Solution() 

    # n = 3
    # ranges = [0,0,0,0]
    # assert s.minTaps(n, ranges) == -1 

    n = 5
    ranges = [3,4,1,1,0,0]
    assert s.minTaps(n, ranges) == 1 