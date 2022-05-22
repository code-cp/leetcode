from queue import PriorityQueue 
from typing import List 

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = PriorityQueue()
        visited = set()
        result = []

        pq.put((nums1[0]+nums2[0], (0, 0)))
        visited.add((0, 0))
        while k > 0 and not pq.empty():
            next_item = pq.get()
            i, j = next_item[1]
            result.append([nums1[i], nums2[j]])
            k -= 1 
            if (i, j+1) not in visited and j+1 < len(nums2):
                pq.put((nums1[i]+nums2[j+1], [i, j+1]))
                visited.add((i, j+1))
            if (i+1, j) not in visited and i+1 < len(nums1):
                pq.put((nums1[i+1]+nums2[j], [i+1, j]))
                visited.add((i+1, j))
        return result 

if __name__ == "__main__": 
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3 
    s = Solution()
    assert s.kSmallestPairs(nums1, nums2, k) == [[1,2],[1,4],[1,6]]
