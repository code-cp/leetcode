from typing import * 
from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        res = 0 
        cnt = Counter(letters)
        n = len(words)
        valid = True 
        # NOTE, not 1<<n + 1
        for i in range(1, 1<<n):
            cur_score = 0 
            cur_cnt = cnt.copy()
            for j in range(n):
                if not valid:
                    break  
                # NOTE, not (1<<j) & i == 1
                if (1&(i>>j)) == 1: 
                    for ch in words[j]: 
                        cur_cnt[ch] -= 1 
                        cur_score += score[ord(ch)-ord("a")]
                        if cur_cnt[ch] < 0: 
                            valid = False 
                            break 
            if valid and cur_score > 0:
                res = max(res, cur_score)
                cur_score = 0 
            valid = True 
        return res 


if __name__ == "__main__": 
    s = Solution() 
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    assert s.maxScoreWords(words[::-1], letters, score) == 23 