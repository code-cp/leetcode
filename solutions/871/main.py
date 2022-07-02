from typing import * 

from queue import PriorityQueue
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = PriorityQueue()
        idx, count = 0, 0 
        cur_max = startFuel
        while cur_max < target: 
            if idx < len(stations) and stations[idx][0] <= cur_max: 
                pq.put(-stations[idx][1])
                idx += 1 
            else: 
                if not pq.empty(): 
                    refill = pq.get()
                    cur_max -= refill
                    count += 1 
                else: 
                    return -1 
        return count  

if __name__ == "__main__": 
    s = Solution()

    # target = 100
    # startFuel = 10
    # stations = [[10,60],[20,30],[30,30],[60,40]]
    # assert s.minRefuelStops(target, startFuel, stations) == 2 

    # target = 1
    # startFuel = 1
    # stations = []
    # assert s.minRefuelStops(target, startFuel, stations) == 0 

    # target = 100
    # startFuel = 50
    # stations = [[50,50]]
    # assert s.minRefuelStops(target, startFuel, stations) == 1 

    target = 1000
    startFuel = 299
    stations = [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]
    assert s.minRefuelStops(target, startFuel, stations) == 4 