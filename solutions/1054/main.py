from typing import * 
import heapq 
from collections import Counter 
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # We want to always choose the most common or second most common element to write next. 
        hq = []
        cnt = Counter(barcodes)
        for k, v in cnt.items(): 
            heapq.heappush(hq, (-v, (k, v)))
        ans = []
        while len(hq) > 0: 
            v1, v2 = 0, 0 
            _, (k1, v1) = heapq.heappop(hq)
            ans.append(k1)
            v1 -= 1 
            if len(hq) > 0:
                _, (k2, v2) = heapq.heappop(hq) 
                ans.append(k2)
                v2 -= 1 
            if v1 != 0: 
                heapq.heappush(hq, (-v1, (k1, v1)))
            if v2 != 0: 
                heapq.heappush(hq, (-v2, (k2, v2)))
        return ans 
    
if __name__ == "__main__": 
    s = Solution()

    barcodes = [1,1,2]
    assert s.rearrangeBarcodes(barcodes) == [1,2,1]
    
    # barcodes = [1,1,1,2,2,2]
    # assert s.rearrangeBarcodes(barcodes) == [2,1,2,1,2,1]
            