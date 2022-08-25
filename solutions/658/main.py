from typing import * 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [abs(a - x) for a in arr]
        indices = sorted(range(len(diff)), key=lambda i: diff[i])
        res = [arr[i] for i in indices][:k]
        res = sorted(res)
        return res 

if __name__ == "__main__": 
    s = Solution()
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    assert s.findClosestElements(arr, k, x) == [1,2,3,4]

