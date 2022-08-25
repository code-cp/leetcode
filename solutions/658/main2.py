from typing import * 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key=lambda a:abs(a-x))[:k])

if __name__ == "__main__": 
    s = Solution()
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    assert s.findClosestElements(arr, k, x) == [1,2,3,4]

