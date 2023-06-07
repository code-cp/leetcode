from typing import * 
from collections import heapq 

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        hq = [0]*n 
        for i in range(n): 
            # min heap 
            hq[i] = reward2[i]-reward1[i]
        heapq.heapify(hq)
        
        ans = sum(reward2)
        for _ in range(k): 
            diff = heapq.heappop(hq)
            ans -= diff 
            
        return ans 
        
                