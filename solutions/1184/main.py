from typing import * 

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        res = 0 
        if start > destination:
            start, destination = destination, start 
        for i in range(start, destination):
            res += distance[i]
        res = min(res, total-res)
        return res 

if __name__ == "__main__": 
    s = Solution()

    distance = [1,2,3,4]
    start = 0
    destination = 1
    assert s.distanceBetweenBusStops(distance, start, destination) == 1 