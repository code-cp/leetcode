from typing import * 

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0 
        counter = Counter(words)
        for w, cnt in counter.items(): 
            i = j = 0 
            while i < len(s) and j < len(w): 
                if s[i] == w[j]: 
                    i += 1 
                    j += 1 
                else: 
                    i += 1 
            if j != len(w): 
                continue 
            res += cnt 
        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "abcde"
    words = ["a","bb","acd","ace"]
    assert sol.numMatchingSubseq(s, words) == 3 