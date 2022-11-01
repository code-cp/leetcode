from typing import * 

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        p1 = p2 = i = j = 0 
        while p1 < len(word1) and p2 < len(word2): 
            if word1[p1][i] != word2[p2][j]: 
                return False 
            i += 1 
            j += 1 
            if i == len(word1[p1]): 
                i = 0 
                p1 += 1 
            if j == len(word2[p2]): 
                j = 0 
                p2 += 1 
        if p1 != len(word1) or p2 != len(word2):
            return False 
        return True 

if __name__ == "__main__": 
    s = Solution() 

    word1 = ["abc","d","defg"]
    word2 = ["abcddef"]
    assert not s.arrayStringsAreEqual(word1, word2)