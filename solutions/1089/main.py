from typing import * 
 
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        memo = [-1] * n 
        res = [0] * n 
        count = 0 
        for i in range(n): 
            if arr[i] == 0: 
                count += 1 
            else: 
                memo[i] = count
        for i, offset in reversed(list(enumerate(memo))): 
            if offset > 0 and i+offset < n: 
                res[i+offset] = arr[i]
        i = 0 
        while i < n: 
            if arr[i] == 0: 
                break 
            i += 1 
        for j in range(i, n): 
            arr[j] = res[j] 
        return 
                
if __name__ == "__main__": 
    s = Solution()
    s.duplicateZeros([1,0,2,3,0,4,5,0]) 
