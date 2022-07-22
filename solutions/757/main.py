from typing import * 

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        def findOverlap(inter, first, second): 
            inRange = lambda x, i: x >= i[0] and x <= i[1]
            count = 0 
            if len(inter) == 0:
                return count
            if inRange(first, inter):
                count += 1 
            if inRange(second, inter):
                count += 1
            return count 

        # sort by end points 
        intervals.sort(key=lambda inter: inter[1])
        n = len(intervals)
        # find non-overlapping interval 
        res = []
        i = 0 

        res.append(intervals[0][1]-1)
        res.append(intervals[0][1])
        first_shot = intervals[0][1]-1
        second_shot = intervals[0][1]
        while i < n-1: 
            i += 1 
            inter = intervals[i]
            o = findOverlap(inter, first_shot, second_shot)
            if o == 0: 
                res.append(inter[1]-1)
                res.append(inter[1])
                first_shot = inter[1]-1
                second_shot = inter[1]
            elif o == 1: 
                # for same end points 
                if second_shot == inter[1]:
                    # can also use res.insert(len(res)-1, inter[1]-1)
                    res.insert(len(res)-1, inter[1]-1)
                    first_shot = inter[1]-1 
                else: 
                    res.append(inter[1])
                    first_shot = second_shot 
                second_shot = inter[1]
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
