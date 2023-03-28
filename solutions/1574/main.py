from typing import * 

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # find the smallest right 
        right = 0
        for i in range(n-1, 0, -1): 
            if arr[i] < arr[i-1]: 
                right = i 
                break 
        if right == 0: 
            return 0 
        res = n-1
        # iterate the left 
        j = right
        for i in range(right):
            if i > 0 and arr[i] < arr[i-1]:
                left = n-i
                break  
            while j < n and arr[i] > arr[j]: 
                j += 1 
            if j < n: 
                res = min(res, j-i-1)
            left = n-i-1
        return min([res, right, left]) 
       
if __name__ == "__main__": 
    s = Solution() 

    arr = [10,13,17,21,15,15,9,17,22,22,13] 
    assert s.findLengthOfShortestSubarray(arr) == 7

    # arr = [2,2,2,1,1,1]
    # assert s.findLengthOfShortestSubarray(arr) == 3 
   
    # arr = [1,2,3,10,0,7,8,9]
    # assert s.findLengthOfShortestSubarray(arr) == 2 
    
    # arr = [1,2,3,10,4,2,3,5]
    # assert s.findLengthOfShortestSubarray(arr) == 3 
                