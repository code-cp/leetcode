from typing import * 

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        state2cookies = lambda s: sum([c for i, c in enumerate(cookies) if s & (1 << i)])
        # dp table 
        n = len(cookies)
        dp = [[0] * (2 ** n) for _ in range(k)]
        # init 
        for state in range(2 ** n): 
            c = state2cookies(state)
            dp[0][state] = c if c < float("inf") else 0 
        # traverse  
        for i in range(1, k):
            for state in range(2 ** n):  
                # over all possible subsets 
                subset = state
                min_c = float('inf') 
                while subset > 0: 
                    min_c = min(min_c, max(dp[i-1][state^subset], dp[0][subset]))
                    # NOTE how to traverse subset of state  
                    subset = (subset-1) & state 
                dp[i][state] = min_c
        return dp[-1][-1]

if __name__ == "__main__": 
    s = Solution()

    cookies = [8,15,10,20,8]
    k = 2
    assert s.distributeCookies(cookies, k) == 31 