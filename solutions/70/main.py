from typing import List 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [1, 2]
        for i in range(3, n+1):
            sum = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = sum
        return sum

if __name__ == "__main__":
    n = 3 
    s = Solution()
    assert s.climbStairs(n) == 3
