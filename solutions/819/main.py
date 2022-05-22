from typing import * 

import re
from collections import defaultdict 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split('[^\w]', paragraph)
        words = list(filter(None, words))
        counts = defaultdict(int)
        for w in words: 
            w = w.lower()
            if w not in banned:
                counts[w] += 1 
        res = max(counts, key=counts.get)
        return res 

if __name__ == "__main__": 
    s = Solution()

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    result = s.mostCommonWord(paragraph, banned)
    assert result == "ball" 