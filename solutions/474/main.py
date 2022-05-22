from typing import List 

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # initialize dp table
        dp = [[0] * (n+1) for _ in range(m+1)]
        # iterate items
        for s in strs:
            # count number of zero and one
            zeroNum, oneNum = 0, 0
            for c in s:
                if c == '0':
                    zeroNum += 1
                else:
                    oneNum += 1
            # iterate bag size
            for i in range(m, zeroNum-1, -1):
                for j in range(n, oneNum-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
        return dp[m][n]

if __name__ == "__main__":
    strs = ["10","0001","111001","1","0"]
    m, n = 5, 3 
    s = Solution()
    assert s.findMaxForm(strs, m, n) == 4
