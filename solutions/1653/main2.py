# ref https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/solutions/2149746/qian-hou-zhui-fen-jie-yi-zhang-tu-miao-d-dor2/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0]*n 
        count_b = 0 
        for i in range(n): 
            if s[i] == "b": 
                count_b += 1 
                dp[i] = dp[max(0, i-1)]
            else: 
                # delete a, f[i] = f[i-1]+1 
                # keep a, f[i] = count_b 
                dp[i] = min(dp[max(0, i-1)]+1, count_b)
        return dp[-1]