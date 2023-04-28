from typing import * 

# ref https://leetcode.cn/problems/longest-string-chain/solutions/2247269/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-wdkm/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        for s in words:
            res = 0  
            for i in range(len(s)): 
                res = max(res, dp.get(s[:i]+s[i+1:], 0))
            dp[s] = res+1 
        return max(dp.values())
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4 
        
        
        