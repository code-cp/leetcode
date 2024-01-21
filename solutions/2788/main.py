from typing import * 
from itertools import chain

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        words = [w.split(separator) for w in words]
        # flatten the list 
        words = list(chain(*words))
        words = [w for w in words if len(w) > 0]
        return words 
    
if __name__ == '__main__': 
    s = Solution()
    
    assert s.splitWordsBySeparator(["one.two.three","four.five","six"], ".") == ["one","two","three","four","five","six"]