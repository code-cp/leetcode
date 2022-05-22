from typing import List 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp table
        # dp[i][j] means max len for text1[0:i-1], text2[0:j-1]
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        # initialize
        # pass
        # traverse dp table
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

if __name__ == "__main__": 
    text1 = "abcde" 
    text2 = "ace"
    s = Solution()
    assert s.longestCommonSubsequence(text1, text2) == 3
