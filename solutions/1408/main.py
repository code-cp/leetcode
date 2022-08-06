from typing import * 

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [s for s in words if any(i!=s and s in i for i in words)]