from typing import * 
import heapq 
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # left wait: (id, efficiency)
        # left arrival: (id, arrive time), arrive time is in future 
        # right wait: (id, efficiency)
        # right arrival: (id, arrive time)
        # next free time: if arrive time is early than next free time, then add it to wait queue 
        
        # max heap 
        left_wait = []
        right_wait = []
        
        # min heap 
        left_arrive = []
        right_arrive = []
        
        next_free = 0 
        for i in range(k): 
            left_arrive.append((0, i))
        heapq.heapify(left_arrive)
        
        res = 0 
        # NOTE, need to record how many people have crossed the bridge 
        crossed = 0 
        returned = 0 
        while returned < n: 
            # all boxes are handled, no need for people on left bank to cross 
            if crossed == n: 
                left_wait = []
                left_arrive = []
            
            while len(left_arrive) > 0 and left_arrive[0][0] <= next_free:
                arrive_time, idx = heapq.heappop(left_arrive)
                # use the eifficiency as priority 
                heapq.heappush(left_wait, (-(time[idx][0]+time[idx][2]), -idx))
            while len(right_arrive) > 0 and right_arrive[0][0] <= next_free:
                arrive_time, idx = heapq.heappop(right_arrive)
                # use the eifficiency as priority 
                heapq.heappush(right_wait, (-(time[idx][0]+time[idx][2]), -idx)) 
            
            # NOTE, need to consider the case when both left/right wait are empty 
            if len(left_wait) == 0 and len(right_wait) == 0: 
                t1, t2 = float("inf"), float("inf")
                # left/right arrive cannot be both empty 
                if len(left_arrive) > 0:
                    t1 = left_arrive[0][0]
                if len(right_arrive) > 0:
                    t2 = right_arrive[0][0] 
                next_free = min(t1, t2) 
                continue 
            
            if len(right_wait) > 0: 
                # from right to left 
                _, idx = heapq.heappop(right_wait)
                idx *= -1 
                # time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi]
                next_free += time[idx][2]
                heapq.heappush(left_arrive, (next_free + time[idx][3], idx))
                returned += 1 
                # Return the instance of time at which the last worker reaches the left bank of the river after all n boxes have been put in the new warehouse.
                res = max(res, next_free)
            elif len(left_wait) > 0: 
                _, idx = heapq.heappop(left_wait)
                idx *= -1 
                next_free += time[idx][0]
                heapq.heappush(right_arrive, (next_free + time[idx][1], idx))
                crossed += 1 
                
        return res 
    
if __name__ == "__main__": 
    s = Solution()
    
    n = 1
    k = 3
    time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
    assert s.findCrossingTime(n,k,time) == 6