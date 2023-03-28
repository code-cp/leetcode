class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # dp[i][j] means the super set of str1[:i], str2[:j]
        # if str1[i] == str2[j], dp[i][j] = dp[i-1][j-1]+1
        # else, dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
        m, n = len(str1), len(str2)
        # change to 1-index 
        str1 = "?"+str1
        str2 = "?"+str2 
        dp = [[0]*(n+1) for _ in range(m+1)]
        # init 
        for i in range(1, m+1): 
            dp[i][0] = i 
        for i in range(1, n+1): 
            dp[0][i] = i 
        # traverse 
        for i in range(1, m+1):
            for j in range(1, n+1): 
                if str1[i] == str2[j]: 
                    dp[i][j] = dp[i-1][j-1]+1 
                else: 
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1) 
        # construct 
        res = ""
        i, j = m, n 
        while i > 0 and j > 0: 
            if str1[i] == str2[j]: 
                res += str1[i]
                i -= 1 
                j -= 1 
            else: 
                if dp[i][j] == dp[i-1][j]+1: 
                    res += str1[i]
                    i -= 1
                else: 
                    res += str2[j]
                    j -= 1 
        while i > 0: 
            res += str1[i]
            i -= 1 
        while j > 0: 
            res += str2[j]
            j -= 1
        # NOTE, need to reverse 
        res = res[::-1] 
        return res   