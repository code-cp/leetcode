from typing import * 

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def bsearch(v, arr): 
            l, r = 0, len(arr)-1
            while l <= r: 
                mid = (r-l)//2+l
                if arr[mid][0] < v: 
                    l += 1 
                elif arr[mid][0] > v: 
                    r -= 1 
                else: 
                    return mid 
            return -1 

        i = 0 
        pieces.sort(key=lambda x: x[0])
        while i < len(arr): 
            v = arr[i]
            idx = bsearch(v, pieces)
            if idx == -1: 
                return False 
            for j in range(len(pieces[idx])):
                if i >= len(arr): 
                    return False 
                if pieces[idx][j] == arr[i]: 
                    i += 1 
                else: 
                    return False 
        return True 


if __name__ == "__main__": 
    s = Solution() 

    arr = [1,2,3]
    pieces = [[2],[1,3]]
    assert not s.canFormArray(arr, pieces)

    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]
    assert s.canFormArray(arr, pieces)