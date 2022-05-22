from typing import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        left = intervals[0][0]
        right = intervals[0][1]
        for inter in intervals[1:]:
            if right >= inter[0]:
                right = max(right, inter[1])
            else:
                result.append([left, right])
                left = inter[0]
                right = inter[1]
        result.append([left, right])
        return result

if __name__ == "__main__":
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(s.merge(intervals))
