from typing import List 

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        row, col = target+1, len(stones)
        dp = [[0] * col for _ in range(row)]
        # initialize
        for i in range(row):
            if i >= stones[0]:
                dp[i][0] = stones[0]
        for i in range(1, row):
            for j in range(1, col):
                if i >= stones[j]:
                    dp[i][j] = max(dp[i][j-1], dp[i-stones[j]][j-1] + stones[j])
                else:
                    dp[i][j] = dp[i][j-1]
        return abs(total - 2*dp[-1][-1])

if __name__ == "__main__":
    stones = [2,7,4,1,8,1]
    s = Solution()
    assert s.lastStoneWeightII(stones) == 1
