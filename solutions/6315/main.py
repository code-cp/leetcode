from typing import * 

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        res = 0 
        v = ['a', 'e', 'i', 'o', 'u']
        for i in range(left, right+1): 
            if words[i][0] in v and words[i][-1] in v: 
                res += 1 
        return res 
        
if __name__ == "__main__": 
    s = Solution() 
    
    words = ["are","amy","u"]
    left = 0
    right = 2
    assert s.vowelStrings(words, left, right)