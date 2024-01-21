from typing import * 

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(s[0] for s in words) == s 