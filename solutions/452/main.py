from typing import List 

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = 1
        if len(points) == 1:
            return result
        points.sort(key=lambda x: (x[0], x[1]))
        maxRange = points[0][1]
        for i in range(1, len(points)):
            if maxRange < points[i][0]:
                maxRange = points[i][1]
                result += 1
            else:
                maxRange = min(maxRange, points[i][1])
        return result

if __name__ == "__main__":
    mySol = Solution()
    points = [[10,16],[2,8],[1,6],[7,12]]
    assert mySol.findMinArrowShots(points) == 2
