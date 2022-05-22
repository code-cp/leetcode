from typing import * 

# time O(nlogn)
# space O(n) 
from collections import defaultdict 
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = 0 
        arr_map = defaultdict(int)
        arr.sort()
        for a in arr: 
            arr_map[a] += 1 
        for a in arr: 
            if arr_map[a] == 0: 
                continue 
            if arr_map[a*2] > 0:  
                arr_map[a] -= 1 
                arr_map[a*2] -= 1 
                # deal with a = 0
                if arr_map[a] >= 0: 
                    count += 1 
        if count >= len(arr) // 2: 
            return True 
        return False 

if __name__ == "__main__": 
    s = Solution()

    arr = [3,1,3,6]
    assert not s.canReorderDoubled(arr) 

    arr = [4,-2,2,-4]
    assert s.canReorderDoubled(arr) 

    arr = [1,2,4,16,8,4]
    assert not s.canReorderDoubled(arr) 

    arr = [2,4,0,0,8,1]
    assert s.canReorderDoubled(arr)

    arr = [-33,0]
    assert not s.canReorderDoubled(arr)
