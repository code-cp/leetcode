from typing import * 

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        def findOverlap(inter1, inter2): 
            if len(inter1) == 0 or len(inter2) == 0:
                return [-1, -1]
            start = max(inter1[0], inter2[0])+1 
            end = min(inter1[1], inter2[1])
            if end < start: 
                return [-1, -1]
            return [start, end]

        # sort by end points 
        intervals.sort(key=lambda inter: inter[1])
        n = len(intervals)
        # find non-overlapping interval 
        res = []
        res.append(intervals[0][1]-1)
        res.append(intervals[0][1])
        i = 0 
        inter1 = [intervals[i][1]-1, intervals[i][1]]
        while i < n-1: 
            i += 1 
            inter2 = intervals[i]
            o = findOverlap(inter1, inter2)
            if o[0] == -1:
                res.append(inter2[1]-1)
                res.append(inter2[1])
            else: 
                res.append(inter2[0])
                res.append(inter2[1])
            inter1 = inter2 
        return len(res) 

if __name__ == "__main__": 
    s = Solution()

    intervals = [[1, 3], [3, 5], [1, 4], [2, 5]]
    assert s.intersectionSizeTwo(intervals) == 3 

    intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
    assert s.intersectionSizeTwo(intervals) == 5

    intervals = [[0,1]]
    assert s.intersectionSizeTwo(intervals) == 2 

    intervals = [[1,3],[3,7],[5,7],[7,8]]
    assert s.intersectionSizeTwo(intervals) == 5 

    intervals = [[7,8],[0,14],[3,11]]
    assert s.intersectionSizeTwo(intervals) == 2 

    intervals = [[1,3],[1,2],[0,1]]
    assert s.intersectionSizeTwo(intervals) == 3 

    intervals = [[0,21],[1,2],[3,7],[0,1],[13,24]]
    assert s.intersectionSizeTwo(intervals) == 7

    intervals = [[2,3],[2,3],[0,1],[2,5],[2,4]]
    assert s.intersectionSizeTwo(intervals) == 4 
