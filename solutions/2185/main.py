from typing import * 

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0 
        for w in words: 
            i = j = 0 
            while i < len(w) and j < len(pref): 
                if w[i] == pref[j]: 
                    i += 1 
                    j += 1 
                else: 
                    break 
            if j == len(pref): 
                res += 1 
        return res 