import re
from typing import * 

class Solution:
    def __init__(self): 
        self.result = []
    def sortArr(self, arr):
        # base case 
        if len(arr) == 1: 
            return self.result
        max_ele = max(arr)
        max_idx = arr.index(max_ele)
        arr[:max_idx+1] = arr[:max_idx+1][::-1]
        self.result.append(max_idx+1)
        arr[:] = arr[::-1]
        self.result.append(len(arr))
        self.sortArr(arr[:-1])
    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.sortArr(arr)
        return self.result 

if __name__ == "__main__": 
    s = Solution()
    arr = [3,2,4,1]
    ans = sorted(arr)
    result = s.pancakeSort(arr)
    arr = [3,2,4,1]
    for r in result: 
        arr[:r] = arr[:r][::-1]
    assert arr == ans