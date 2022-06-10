class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        # Let dp(i, j) be the answer for the string T = S[i:j+1] including the empty sequence
        dp = [[0] * n for _ in range(n)]
        # init dp 
        for i in range(n): 
            dp[i][i] = 1
        for l in range(1, n): 
            for i in range(0, n-l): 
                j = i + l
                # simple case when two ends are unequal  
                if s[i] != s[j]: 
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] 
                else: 
                    left, right = i+1, j-1 
                    while left <= right and s[left] != s[i]: 
                        left += 1 
                    while left <= right and s[right] != s[i]: 
                        right -= 1 
                    if left > right: 
                        # there are no char in middle equal to end 
                        dp[i][j] = dp[i+1][j-1]*2 + 2 
                    elif left == right: 
                        # there is one char in middle equal to end 
                        dp[i][j] = dp[i+1][j-1]*2 + 1 
                    else: 
                        # there are more than on char in middle equal to end 
                        dp[i][j] = dp[i+1][j-1]*2 - dp[left+1][right-1] 
        return dp[0][n-1] % 1000000007 

if __name__ == "__main__": 
    sol = Solution()
    
    s = "bccb"
    assert sol.countPalindromicSubsequences(s) == 6 