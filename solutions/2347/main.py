from typing import * 
from collections import Counter 
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cnts = Counter(suits)
        if max(cnts.values()) >= 5: 
            return "Flush"
        cntr = Counter(ranks)
        if max(cntr.values()) >= 3: 
            return "Three of a Kind"
        if max(cntr.values()) >= 2: 
            return "Pair"
        return "High Card"

        