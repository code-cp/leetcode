from typing import * 

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def w2i(w): 
            return ''.join(str(i) for i in map(lambda x: w.index(x), w)) 
        p = w2i(pattern) 
        res = []
        for w in words: 
            w_i = w2i(w) 
            if w_i == p: 
                res.append(w) 
        return res 


if __name__ == "__main__": 
    s = Solution() 

    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    assert s.findAndReplacePattern(words, pattern) == ["mee","aqq"] 