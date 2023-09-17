from typing import * 
import heapq 
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        hq = []
        num_used_days = 0 
        for i in range(len(courses)): 
            heapq.heappush(hq, -courses[i][0])
            num_used_days += courses[i][0]
            
            if num_used_days > courses[i][1]: 
                # cannot finish this course
                # remove the longest course
                # so courses[i] can be finished 
                # and total days taken is less  
                num_used_days += heapq.heappop(hq)
        
        return len(hq)
     