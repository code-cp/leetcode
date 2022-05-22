from typing import List 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp table
        dp = [False] * (len(s) + 1)
        # initialize
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i >= len(word):
                    dp[i] = dp[i] or dp[i-len(word)] and s[i-len(word):i] == word
        return dp[-1]

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    sol = Solution()
    assert sol.wordBreak(s, wordDict)
