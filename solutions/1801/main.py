from typing import * 
import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        M = 10**9+7
        buy_heap = []
        sell_heap = []
        res = 0 
        for o in orders: 
            res += o[1]
            res %= M 
            if o[2] == 0: 
                heapq.heappush(buy_heap, (-o[0], [o[0], o[1]]))
            else: 
                heapq.heappush(sell_heap, (o[0], [o[0], o[1]]))
            if len(buy_heap) > 0 and len(sell_heap) > 0 and buy_heap[0][1][0] >= sell_heap[0][1][0]:
                bp, bl = heapq.heappop(buy_heap)
                sp, sl = heapq.heappop(sell_heap)
                diff = min(bl[1], sl[1])
                res -= 2*diff
                res %= M 
                bl[1] -= diff
                sl[1] -= diff
                while bl[1] > 0 and len(sell_heap) > 0: 
                    sp, sl = heapq.heappop(sell_heap)
                    if bl[0] >= sl[0]:
                        diff = min(bl[1], sl[1])
                        res -= 2*diff
                        res %= M 
                        bl[1] -= diff
                        sl[1] -= diff
                    else: 
                        heapq.heappush(buy_heap, (bp, bl))
                        heapq.heappush(sell_heap, (sp, sl))
                        break 
                while sl[1] > 0 and len(buy_heap) > 0: 
                    bp, bl = heapq.heappop(buy_heap)
                    if bl[0] >= sl[0]:
                        diff = min(bl[1], sl[1])
                        res -= 2*diff
                        res %= M 
                        bl[1] -= diff
                        sl[1] -= diff
                    else: 
                        heapq.heappush(buy_heap, (bp, bl))
                        heapq.heappush(sell_heap, (sp, sl))
                        break 
                if bl[1] > 0:
                    heapq.heappush(buy_heap, (bp, bl))
                if sl[1] > 0: 
                    heapq.heappush(sell_heap, (sp, sl))
        return res 

if __name__ == "__main__": 
    s = Solution() 

    orders = [[26,7,0],[16,1,1],[14,20,0],[23,15,1],[24,26,0],[19,4,1],[1,1,0]]
    assert s.getNumberOfBacklogOrders(orders) == 34

    orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
    assert s.getNumberOfBacklogOrders(orders) == 999999984

    orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
    assert s.getNumberOfBacklogOrders(orders) == 6