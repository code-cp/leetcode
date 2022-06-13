from typing import * 

from collections import Counter
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len(heights) - Counter([abs(e - heights[i]) for i, e in enumerate(sorted(heights))]).get(0, 0) 

if __name__ == "__main__": 
    s = Solution()
     
    assert s.heightChecker([1,1,4,2,1,3]) == 3 