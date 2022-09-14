from typing import * 

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        return sum(arr[int(n*0.05):int(-n*(0.05))])/(n*0.9)