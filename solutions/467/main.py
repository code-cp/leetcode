from typing import * 

from collections import defaultdict
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int) 
        k = 0 
        for i, c in enumerate(p): 
            if i > 0 and (ord(c) - ord(p[i-1])) % 26 == 1:
                k += 1 
            else: 
                k = 1 
            # taking max since we need to count each substring once 
            # ie the same one can only count once 
            dp[ord(c)] = max(dp[ord(c)], k) 
        return sum(dp.values())  


if __name__ == "__main__": 
    s = Solution() 

    assert s.findSubstringInWraproundString("zab") == 6 