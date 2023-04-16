class Solution:
    def longestPrefix(self, s: str) -> str:
        # suffix[i] = max len k s.t. s[:k-1] = s[i-k+1:i]
        # ans is suffix[n-1]
        # suffix is the dp array 
        n = len(s)
        dp = [0]*n 
        # 找的是真前缀，前缀不能等于字符串本身
        dp[0] = 0 
        for i in range(1, n): 
            # compute dp[i]
            j = dp[i-1]
            while j >= 1 and s[j] != s[i]:
                j = dp[j-1]
            if s[j] == s[i]:
                dp[i] = j+1 
        l = dp[-1]
        return s[:l] 