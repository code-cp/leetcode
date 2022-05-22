from typing import List 
import heapq

class Solution:
    # ref https://youtu.be/sJdJTXhxqjo
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        n = len(arr)

        # since 1/n < 1/(n-1)...
        # 2/n < 2/(n-1)...
        for i in range(n-1):
            heapq.heappush(pq, (arr[i]/arr[n-1], i, n-1))

        while k-1 > 0:
            _, i, j = heapq.heappop(pq)
            if i < j-1:
                heapq.heappush(pq, (arr[i]/arr[j-1], i, j-1))
            k -= 1

        return [arr[pq[0][1]], arr[pq[0][2]]]

if __name__ == "__main__": 
    arr = [1,2,3,5] 
    k = 3
    s = Solution()
    assert s.kthSmallestPrimeFraction(arr, k) == [2, 5]
