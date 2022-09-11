from typing import * 
from heapq import heapify, heappush, heappop

# earned_wage[i] / quality[i] = unit_wage[i] is same for every worker i 
# earned_wage[i] >= wage[i]
# so earned_wage[i] / quality[i] >= wage[i] / quality[i]
# unit_wage[i] >= wage[i] / quality[i]
# unit_wage * sum(quality[i]) = sum(earned_wage[i])
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1]/p[0])
        ans = float("inf") 
        totalq = 0 
        h = []
        for q, w in pairs[:k-1]: 
            totalq += q 
            # python heap is min heap 
            heappush(h, -q)
        for q, w in pairs[k-1:]:
            totalq += q 
            heappush(h, -q)
            ans = min(ans, w/q * totalq)
            # subtract off the largest quality
            totalq += heappop(h)
        return ans 


if __name__ == "__main__": 
    s = Solution()

    quality = [10,20,5]
    wage = [70,50,30]
    k = 2
    assert s.mincostToHireWorkers(quality, wage, k) == 105