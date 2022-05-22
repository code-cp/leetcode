from typing import List 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp table
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        # initialize
        dp[0][0] = 0
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for i in range(1, len(word2)+1):
            dp[0][i] = i
        # traverse dp table
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(*[dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+2])
        return dp[-1][-1]

if __name__ == "__main__": 
    word1 = "leetcode"
    word2 = "etco"
    s = Solution()
    assert s.minDistance(word1, word2) == 4
