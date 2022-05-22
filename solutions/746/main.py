from typing import List 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * 2
        for i in range(2, len(cost)+1):
            sum = min(dp[1] + cost[i-1], dp[0] + cost[i-2])
            dp[0] = dp[1]
            dp[1] = sum
        return sum

if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    s = Solution()
    assert s.minCostClimbingStairs(cost) == 6
