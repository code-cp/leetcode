from typing import * 
from collections import defaultdict 
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        # each word is trivially a chain 
        dp = defaultdict(lambda: 1)
        for i in range(n): 
            cur = words[i]
            cur_max = dp[cur] 
            for j in range(len(cur)): 
                prev = cur[:j]+cur[j+1:]
                if prev in dp:
                    cur_max = max(cur_max, dp[prev]+1)
            dp[cur] = cur_max
        return max(dp.values())

if __name__ == "__main__": 
    s = Solution() 
    
    assert s.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4 