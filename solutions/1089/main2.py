from typing import * 
 
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        l, r = -1, 0 
        while r < n: 
            l += 1 
            if arr[l] == 0: 
                r += 1 
            r += 1 
        if r > n: 
            r -= 2
            arr[r] = 0  
            l -= 1 
            r -= 1
        else: 
            r -= 1 
        while r >= 0:
            arr[r] = arr[l]
            r -= 1 
            if arr[l] == 0: 
                arr[r] = 0 
                r -= 1 
            l -= 1 
        return 
                
if __name__ == "__main__": 
    s = Solution()
    # s.duplicateZeros([1,0,2,3,0,4,5,0]) 
    # s.duplicateZeros([0,0,0,0,0,0,0]) 
    s.duplicateZeros([8,4,5,0,0,0,0,7]) 
