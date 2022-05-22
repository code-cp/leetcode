from typing import List 

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        if len(intervals) < 2:
            return result
        intervals = sorted(intervals, key=lambda x: x[0])
        maxRange = intervals[0][1]
        for inter in intervals[1:]:
            if maxRange > inter[0]:
                maxRange = min(maxRange, inter[1])
                result += 1
            else:
                maxRange = inter[1]
        return result

if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    s = Solution()
    assert s.eraseOverlapIntervals(intervals) == 1
