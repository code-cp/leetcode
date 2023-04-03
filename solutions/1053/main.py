from typing import * 
from collections import deque 

# conditions 
# 1. first number num[i] st num[i] > num[j], i > j 
# 2. for j < i, num[j] is the largest
# 3. if multiple values are equal, use the smallest j 

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]: 
        n = len(arr)
        stack = deque()
        for i in range(n-1,-1,-1):
            num, idx = -1, -1  
            while len(stack) > 0 and arr[i] > stack[-1][0]:
                val = stack.pop()
                if num < val[0]: 
                    num = val[0]
                    idx = val[1]
            if idx != -1: 
                arr[i], arr[idx] = arr[idx], arr[i]
                return arr 
            stack.append((arr[i], i))
        return arr 
    
if __name__ == "__main__": 
    s = Solution() 
    # assert s.prevPermOpt1([3,1,1,3]) == [1,3,1,3]
    # assert s.prevPermOpt1([3,2,1]) == [3,1,2]
    assert s.prevPermOpt1([1,9,4,6,7]) == [1,7,4,6,9]