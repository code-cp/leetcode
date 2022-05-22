from typing import * 

# TLE 
import heapq
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        heap = []
        for j in range(1, m+1): 
            heapq.heappush(heap, (j, 1, j))
        while k > 1:
            _, i, j = heapq.heappop(heap)
            if i+1 <= n:  
                heapq.heappush(heap, ((i+1)*j, i+1, j)) 
            k -= 1
        return heap[0][0] 

if __name__ == "__main__": 
    s = Solution() 

    m = 3
    n = 3
    k = 5
    assert s.findKthNumber(m, n, k) == 3 

    m = 2
    n = 3
    k = 6
    assert s.findKthNumber(m, n, k) == 6 

    m = 9895
    n = 28405
    k = 100787757
    assert s.findKthNumber(m, n, k) == 31666344