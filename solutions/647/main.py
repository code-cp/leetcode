from typing import List 

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        # dp table
        # i, j means s[i:j] is palindrome
        dp = [[False] * (len(s)) for _ in range(len(s))]
        # initialize
        for i in range(len(s)):
            # case "a"
            dp[i][i] = True
            result += 1
        # traverse dp table
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    # this cannot be palindrome
                    pass
                else:
                    if j == i+1:
                        # case "aa"
                        dp[i][j] = True
                        result += 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j]:
                            result += 1
        return result

if __name__ == "__main__": 
    s = "aaa"
    sol = Solution()
    assert sol.countSubstrings(s) == 6
