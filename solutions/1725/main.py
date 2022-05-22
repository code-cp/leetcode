import re
from typing import List 

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = -float("inf") 
        result = 0 
        for r in rectangles: 
            if max_len < min(r[0], r[1]): 
                result = 1 
                max_len = min(r[0], r[1])
            elif max_len == min(r[0], r[1]): 
                result += 1 
        return result 

if __name__ == "__main__": 
    rectangles = [[5,8],[3,9],[5,12],[16,5]]
    s = Solution()
    assert s.countGoodRectangles(rectangles) == 3 