from typing import * 

# wrong 
# this approach is very messy 
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        def findOverlap(inter1, inter2): 
            if len(inter1) == 0 or len(inter2) == 0:
                return [0, -1]
            start = max(inter1[0], inter2[0])
            end = min(inter1[1], inter2[1])
            if end < start: 
                return [0, -1]
            return [start, end]
        def addEle(res, inter): 
            start, end = findOverlap(res, inter)
            if start > end:
                if len(res) == 0 or res[-1] < inter[1]-1:
                    res.append(inter[1]-1)
                if len(res) == 0 or res[-1] < inter[1]:
                    res.append(inter[1])
                return 
            if res[-1] < end+1:
                res.append(end+1)

        intervals.sort(key=lambda interval: interval[0])
        n = len(intervals)
        unaddressed = []
        res = []
        inter1 = intervals[0]
        pre = inter1
        unaddressed = [] 
        for i in range(1, n): 
            inter2 = intervals[i]
            inter = findOverlap(inter1, inter2)
            if inter[1] - inter[0] <= 0:
                inter1 = inter2 
                addEle(res, pre)
                if len(unaddressed) > 0:
                    addEle(res, unaddressed)
                unaddressed = inter1
            else: 
                inter1 = inter 
                if len(unaddressed) > 0:
                    addEle(res, unaddressed)
                    unaddressed = []
                pre = inter 
        if len(res) == 0:
            res.append(pre[1]-1)
            res.append(pre[1])
        elif len(unaddressed) > 0:
            addEle(res, unaddressed)
        return len(res) 

if __name__ == "__main__": 
    s = Solution()

    # intervals = [[1, 3], [3, 5], [1, 4], [2, 5]]
    # assert s.intersectionSizeTwo(intervals) == 3 

    # intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
    # assert s.intersectionSizeTwo(intervals) == 5

    # intervals = [[0,1]]
    # assert s.intersectionSizeTwo(intervals) == 2 

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
