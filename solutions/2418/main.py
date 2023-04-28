from typing import * 

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indices = [i[0] for i in sorted(enumerate(heights), key=lambda x: x[1], reverse=True)]
        return [names[i] for i in indices] 