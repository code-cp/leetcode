from typing import * 

from collections import deque, Counter 
import math 
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            result = 0 
            r = deque()
            while x > 0: 
                r.append(x % 10)
                x //= 10

            count = 1 
            while len(r) > 0: 
                x = r.pop()
                result += x * count 
                count *= 10 
            return result  

        n = len(nums)
        diff = [0]*n
        for i in range(n): 
            diff[i] = nums[i]-rev(nums[i]) 

        M = 10**9 + 7
        cnt = Counter(diff)
        res = 0 
        for k, v in cnt.items(): 
            if v >= 2:
                res += (math.factorial(v)/(math.factorial(v-2)*math.factorial(2))) % M 
                res %= M 
        return int(res) 
            
if __name__ == "__main__": 
    s = Solution() 

    nums = [42,11,1,97]
    assert s.countNicePairs(nums) == 2 