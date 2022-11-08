from typing import * 

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0 
        for w in words: 
            for a in allowed: 
                w = w.replace(a, "")
            if len(w) == 0: 
                res += 1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    assert s.countConsistentStrings(allowed, words)