from typing import * 

# still wrong 
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
            if len(res) > 0 and res[-1] >= inter[0]:
                res.append(inter[1])
                return  
            if len(res) == 0 or res[-1] < inter[1]-1:
                res.append(inter[1]-1)
            if len(res) == 0 or res[-1] < inter[1]:
                res.append(inter[1]) 

        intervals.sort(key=lambda interval: interval[1])
        n = len(intervals)

        i = 0
        inter1 = intervals[0] 
        res = []
        while i < n: 
            if i < n-1: 
                i += 1
            else:
                addEle(res, intervals[i])
                break   
            inter2 = intervals[i]
            pre = inter1 
            inter = findOverlap(inter1, inter2)
            while i < n and inter[1] - inter[0] >= 1: 
                i += 1  
                inter1 = inter
                if i < n:
                    inter2 = intervals[i]
                else: 
                    pre = inter
                    break 
                pre = inter 
                inter = findOverlap(inter1, inter2)
            addEle(res, pre)
            inter1 = inter2 
        return len(res) 

if __name__ == "__main__": 
    s = Solution()

    # intervals = [[1, 3], [3, 5], [1, 4], [2, 5]]
    # assert s.intersectionSizeTwo(intervals) == 3 

    # intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
    # assert s.intersectionSizeTwo(intervals) == 5

    # intervals = [[0,1]]
    # assert s.intersectionSizeTwo(intervals) == 2 

    # intervals = [[1,3],[3,7],[5,7],[7,8]]
    # assert s.intersectionSizeTwo(intervals) == 5 

    # intervals = [[7,8],[0,14],[3,11]]
    # assert s.intersectionSizeTwo(intervals) == 2 

    # intervals = [[1,3],[1,2],[0,1]]
    # assert s.intersectionSizeTwo(intervals) == 3 

    # intervals = [[0,21],[1,2],[3,7],[0,1],[13,24]]
    # assert s.intersectionSizeTwo(intervals) == 7

    # intervals = [[2,3],[2,3],[0,1],[2,5],[2,4]]
    # assert s.intersectionSizeTwo(intervals) == 4 

    # intervals = [[2,3],[2,3],[0,1],[2,5],[2,4]]
    # assert s.intersectionSizeTwo(intervals) == 4 

    # intervals = [[4,14],[6,17],[7,14],[14,21],[4,7]]
    # assert s.intersectionSizeTwo(intervals) == 4 

    # intervals = [[1,3],[4,9],[0,10],[6,7],[1,2],[0,6],[7,9],[0,1],[2,5],[6,8]]
    # assert s.intersectionSizeTwo(intervals) == 7

    intervals = [[4,7],[5,8],[7,9],[2,6],[0,1],[1,4],[1,9],[0,5],[5,10],[7,8]]
    assert s.intersectionSizeTwo(intervals) == 6