from typing import * 

from collections import deque
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        time_dur = []
        for i, task in enumerate(tasks):
            start, end, dur = task  
            time_dur.append((start, 0, dur, i))
            time_dur.append((end, 1, dur, i))
        
        time_dur.sort()
        active_tasks = {}
        res = 0 
        for task in time_dur: 
            t, state, dur, idx = task 
            if state == 0: 
                # this is start of task 
                active_tasks[idx] = [t, dur]
            elif active_tasks.get(idx, -1) != -1: 
                # this is end of task 
                dur = active_tasks[idx][1] 
                res += dur 
                to_del = []
                for k, v in active_tasks.items(): 
                    delta = min(v[1], t-v[0]+1, dur)
                    active_tasks[k][1] -= delta 
                    active_tasks[k][0] += delta 
                    if active_tasks[k][1] == 0:
                        to_del.append(k)
                for k in to_del:
                    active_tasks.pop(k)
        
        return res 
        
if __name__ == "__main__": 
    s = Solution() 

    
    # tasks = [[2,3,1],[4,5,1],[1,5,2]]
    # assert s.findMinimumTime(tasks) == 2 