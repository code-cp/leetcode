from typing import * 

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [x[0] for x in intervals]
        starts = [i for i in sorted(enumerate(starts), key=lambda x:x[1])]
        res = [-1] * len(intervals) 
        for idx, i in enumerate(intervals): 
            end = i[1] 
            left, right = 0, len(starts)-1 
            while left <= right: 
                mid = (right - left)//2 + left 
                if starts[mid][1] >= end: 
                    right = mid - 1
                else: 
                    left = mid + 1 
            if left < len(starts): 
                res[idx] = starts[left][0] 
        return res 


if __name__ == "__main__": 
    s = Solution() 

    intervals = [[3,4],[2,3],[1,2]]
    assert s.findRightInterval(intervals) == [-1,0,1] 