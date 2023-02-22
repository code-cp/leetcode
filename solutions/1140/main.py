from typing import * 
from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # me: max dp[state]
        # state -> state' 
        # opponent: max dp[state']
        # I want min(max dp[state'])

        dp = [[0]*101 for _ in range(101)]
        suf = [0] * 101 

        n = len(piles)
        suf[n] = 0 
        for i in range(n-1, -1, -1): 
            suf[i] = suf[i+1] + piles[i]

        # @lru_cache(maxsize=32)
        def solve(i, M):
            # i: start from pile i
            # M: max. num of piles I can choose
            
            # base case 
            if i == n: 
                # no more piles 
                return 0 
            if M >= n-i: 
                # eg i = 0, n = 2, then we have 2 - 0 = 2 more piles 
                # if can take all piles at current round, then take all 
                dp[i][M] = suf[i]
                return dp[i][M]

            if dp[i][M] != 0: 
                return dp[i][M]

            total = 0 
            for x in range(1, 2*M+1): 
                # pick x piles 
                if i+x-1 >= n:
                    break 
                total += piles[i+x-1]
                # opponent need to max. solve(i+k, max(M, x))
                dp[i][M] = max(dp[i][M], total + suf[i+x] - solve(i+x, max(M, x)))

            return dp[i][M] 

        return solve(0, 1)


if __name__ == "__main__": 
    s = Solution() 

    piles = [2,7,9,4,4]
    assert s.stoneGameII(piles) == 10 