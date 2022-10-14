class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # dp[i] = no. of distinct subsequences from s[1:i]
        # do not use s[i], dp[i] = dp[i-1]
        # use s[i], dp[i] = dp[i-1]*2 - dp[j-1]
        # dp[j-1] is the duplicated ones 
        dp = [0] * (len(s)+1)
        # initial 0 is null 
        dp[0] = 1 
        last = [0] * 26 
        M = 1e9 + 7
        for i, ch in enumerate(s): 
            idx = ord(ch)-ord('a')
            j = last[idx]
            dp2 = (dp[i]*2)%M
            if j >= 1: 
                dp[i+1] = (dp2 - dp[j-1] + M) % M 
            else: 
                dp[i+1] = dp2
            last[idx] = i+1
        # need to remove null   
        return int(dp[-1] - 1) 

if __name__ == "__main__": 
    sol = Solution() 

    s = "abc"
    assert sol.distinctSubseqII(s) == 7 