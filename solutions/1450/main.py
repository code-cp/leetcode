from typing import * 

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        intervals = [[s, e] for s, e in zip(startTime, endTime)]
        intervals.sort(key=lambda x: x[1])

        def bsearch(query, intervals): 
            left, right = 0, len(intervals)-1
            while left <= right: 
                mid = (right-left)//2 + left
                if intervals[mid][1] < query:
                    left = mid+1 
                else: 
                    right = mid-1 
            return left 

        left = bsearch(queryTime, intervals)
        res = 0 
        for i in range(left, len(intervals)):
            if intervals[i][0] <= queryTime and intervals[i][1] >= queryTime:
                res += 1 

        return res 


if __name__ == "__main__": 
    s = Solution()

    startTime = [1,2,3]
    endTime = [3,2,7]
    queryTime = 4
    assert s.busyStudent(startTime, endTime, queryTime) == 1 