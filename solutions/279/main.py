from typing import List
from math import sqrt 

class Solution:
    def numSquares(self, n: int) -> int:
        # dp table
        MAX = n + 1
        dp = [MAX] * (n + 1)
        # to reduce runtime
        nums = [x**2 for x in range(1, int(sqrt(n))+1)]
        # initialize
        # note, not 1, but 0
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] = min(dp[i], dp[i-nums[j]]+1)
        return dp[-1]

if __name__ == "__main__":
    n = 12 
    s = Solution()
    assert s.numSquares(n) == 3

