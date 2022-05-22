from typing import List 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # check input
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        # dp table
        dp = [[False] * (len(s)+1) for _ in range(len(t)+1)]
        # initialize
        for i in range(len(t)+1):
            dp[i][0] = True
        # traverse dp table
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

if __name__ == "__main__": 
    s = "abc"
    t = "ahbgdc"
    sol = Solution()
    assert sol.isSubsequence(s, t)
