from typing import * 

# time O(n)
# space O(n) 
from collections import defaultdict 
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr_map = defaultdict(int)
        for a in arr: 
            arr_map[a] += 1 
        if arr_map[0] % 2 != 0: 
            return False 
        del arr_map[0]
        queue = [] 
        in_degrees = defaultdict(int)
        # avoid "RuntimeError: dictionary changed size during iteration" error
        for k in list(arr_map.keys()): 
            if k % 2 == 0 and arr_map[k//2] > 0:
                in_degrees[k] += arr_map[k//2] 
                continue 
            queue.append(k)
        while len(queue) > 0:
            node = queue.pop(0) 
            in_degrees[node*2] -= arr_map[node]
            arr_map[node*2] -= arr_map[node]
            if arr_map[node*2] < 0:
                return False 
            # deal with node*2 
            if in_degrees[node*2] == 0 and arr_map[node*2] > 0: 
                queue.append(node*2) 
            # deal with node*4 
            if in_degrees[node*4] > 0:
                in_degrees[node*4] -= arr_map[node]
                if in_degrees[node*4] == 0 and arr_map[node*4] > 0: 
                    queue.append(node*4) 
        return True 

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

    arr = [2,1,2,6]
    assert not s.canReorderDoubled(arr)

    arr = [-2,-2,1,-2,-1,2]
    assert not s.canReorderDoubled(arr)