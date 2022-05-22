from typing import List 

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            sum = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = sum
        return sum

if __name__ == "__main__":
    n = 4 
    s = Solution()
    assert s.fib(n) == 3
