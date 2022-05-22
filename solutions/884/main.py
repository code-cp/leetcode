from typing import List
from collections import defaultdict  

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_dict = defaultdict(int)
        for w in (s1+" "+s2).split(): 
            word_dict[w] += 1 
        result = []
        for w in word_dict:
            if word_dict[w] == 1: 
                result.append(w)
        return result

if __name__ == "__main__": 
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    s = Solution()
    result = s.uncommonFromSentences(s1, s2)
    ans = ["sweet", "sour"]
    assert result == ans 