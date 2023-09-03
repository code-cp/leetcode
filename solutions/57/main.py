from typing import * 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:     
        start, end = newInterval
        n = len(intervals)

        # find the last end that < start 
        def bsearch(target): 
            nonlocal n 
            nonlocal intervals 
            l, r = 0, n-1
            while l <= r: 
                mid = (r-l)//2 + l 
                if intervals[mid][1] >= target:
                    r = mid - 1 
                else: 
                    l = mid + 1 
            return r 
        
        
        i = bsearch(start)
        i += 1 
        if i < n: 
            start = min(start, intervals[i][0])
        while i < n: 
            # check if intervals[i] overlap with [start, end]
            if intervals[i][0] <= end: 
                end = max(end, intervals[i][1])
                del intervals[i]
                n -= 1 
            else: 
                break 
        intervals.insert(i, [start, end])
                        
        return intervals 
    
if __name__ == "__main__":
    s = Solution()
    
    # assert s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
            
        
        
         