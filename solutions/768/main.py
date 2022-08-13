from typing import * 

from collections import Counter
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def check_permut(list1, list2): 
            return Counter(list1) == Counter(list2)

        arr_s = sorted(arr)
        res = 0
        arr_chunk = []
        arr_sort_chunk = [] 
        for i in range(len(arr)): 
            arr_chunk.append(arr[i])
            arr_sort_chunk.append(arr_s[i])
            if check_permut(arr_chunk, arr_sort_chunk):
                res += 1 
                arr_chunk = []
                arr_sort_chunk = [] 
        return res 

if __name__ == "__main__": 
    s = Solution()

    arr = [2,1,3,4,4]
    assert s.maxChunksToSorted(arr) == 4 

    arr = [1,1,0,0,1]
    assert s.maxChunksToSorted(arr) == 2 
