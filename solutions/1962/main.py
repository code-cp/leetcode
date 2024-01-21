from typing import * 
import heapq 
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-p for p in piles]
        heapq.heapify(piles)
        
        for _ in range(k): 
            p = heapq.heappop(piles)
            total -= (-p // 2)
            p = -p - (-p // 2) 
            heapq.heappush(piles, -p)
            
        return total     
        
        
        
        