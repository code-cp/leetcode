from typing import * 

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        M = 10**9+7
        m, n = len(pizza), len(pizza[0])
        apples = [[0]*(n+1) for _ in range(m+1)]
        dp = [[[0 for j in range(n)] for i in range(m)] for _ in range(k+1)]
        
        # init 
        for i in range(m-1, -1, -1): 
            for j in range(n-1, -1, -1): 
                # prefix 
                apples[i][j] = apples[i][j+1] + apples[i+1][j] - apples[i+1][j+1] + (pizza[i][j]=='A') 
                # NOTE, not dp[0][i][j]
                # You have to cut the pizza into k pieces using k-1 cuts
                # so dp[1] means cut pizza into 1 piece 
                dp[1][i][j] = 1 if apples[i][j] > 0 else 0 
                
        for k in range(1, k+1): 
            for i in range(m): 
                for j in range(n): 
                    # horizontal cut 
                    for h in range(i+1, m): 
                        # if if apples[i][j] > apples[h][j], then the cut piece contains at least one apple 
                        if apples[i][j] > apples[h][j]: 
                            # if dp[k-1][h][j] == 0, then the last piece is invalid, so dp[k][i][j] does not change 
                            dp[k][i][j] = (dp[k][i][j] + dp[k-1][h][j]) % M
                    # vertical cut 
                    for v in range(j+1, n): 
                        if apples[i][j] > apples[i][v]:
                            dp[k][i][j] = (dp[k][i][j] + dp[k-1][i][v]) % M
                            
        return dp[k][0][0] 