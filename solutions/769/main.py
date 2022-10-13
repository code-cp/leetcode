from typing import * 

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        res = 1
        max_val = arr[0]
        for i in range(1, n): 
            # check if we must include arr[i] in current chunk 
            if max_val >= i:
                max_val = max(max_val, arr[i])
                continue 
            max_val = arr[i]
            res += 1 
        return res 

if __name__ == "__main__": 
    s = Solution()

    arr = [1,2,0,3]
    assert s.maxChunksToSorted(arr) == 2 

    arr = [4,3,2,1,0]
    assert s.maxChunksToSorted(arr) == 1 

    arr = [1,0,2,3,4]
    assert s.maxChunksToSorted(arr) == 4 