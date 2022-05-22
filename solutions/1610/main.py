from typing import List 

import math 
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        pts_origin, result = 0, 0
        pts_angles = []
        # convert the origin to person location 
        for p in points:
            p[0], p[1] = p[0] - location[0], p[1] - location[1]
        # check how many points are at origin 
        for p in points: 
            if p[0] == 0 and p[1] == 0: 
                pts_origin += 1 
            else: 
                a = math.atan2(p[1], p[0])
                pts_angles.append(a)
        # sort the point angles 
        pts_angles = sorted(pts_angles)
        length = len(pts_angles)
        for i in range(length): 
            pts_angles.append(pts_angles[i] + 2.0 * math.pi)
        # sliding window 
        l = 0
        fov = math.pi * angle / 180 
        # NOTE, time complexity in for+while step is O(n), not O(n^2)
        # since l traverse takes O(n) in total
        for r in range(len(pts_angles)): 
            while pts_angles[r] - pts_angles[l] > fov: 
                l += 1 
            result = max(result, r - l + 1)
        return result + pts_origin
        
if __name__ == "__main__": 
    points = [[2,1],[2,2],[3,3]]
    angle = 90
    location = [1,1]
    s = Solution()
    result = s.visiblePoints(points, angle, location)
    assert result == 3
