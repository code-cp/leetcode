from typing import * 

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_width = 0 
        n = len(points)
        for i in range(1, n): 
            max_width = max(max_width, points[i][0]-points[i-1][0])
        return max_width