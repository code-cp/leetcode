from typing import * 
import heapq 
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        indices = sorted(range(n), key=lambda k: queries[k])
        queries.sort()
        intervals.sort()
        
        res = [-1]*n 
        hq = []
        # NOTE, use j instead of i 
        j = 0 
        for i, q in enumerate(queries):
            idx = indices[i]
            
            while j < len(intervals) and intervals[j][0] <= q: 
                duration = intervals[j][1] - intervals[j][0] + 1 
                heapq.heappush(hq, (duration, intervals[j][1]))
                j += 1 
                
            while len(hq) > 0 and hq[0][1] < q: 
                heapq.heappop(hq)
                
            if len(hq) > 0: 
                res[idx] = hq[0][0]     
            
        return res 
    
if __name__ == "__main__": 
    s = Solution()
    
    intervals = [[1,4],[2,4],[3,6],[4,4]]
    queries = [2,3,4,5]
    assert s.minInterval(intervals, queries) == [3,3,1,4]