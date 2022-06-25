from typing import * 

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        for i in range(3): 
            dp[0][i] = costs[0][i]
        for i in range(1, n): 
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        return min(dp[-1])

if __name__ == "__main__":
    s = Solution()

    costs = [[17,2,17],[16,16,5],[14,3,19]]
    assert s.minCost(costs) == 10 