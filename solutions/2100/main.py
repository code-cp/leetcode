from typing import * 

from collections import deque 
class Solution:
    def getInflection(self, nums, reverse=False):
        n = len(nums) 
        stack = deque()
        
        if reverse:
            result = [-1] * n 
            rn = range(n-1, -1, -1)
            invalid = n 
        else: 
            result = [n] * n 
            rn = range(n)
            invalid = -1 

        for i in rn: 
            while len(stack) != 0 and nums[i] < 0: 
                idx = stack.pop()
                if nums[idx] <= 0:
                    result[idx] = i 
                else: 
                    result[idx] = invalid
            stack.append(i)
        return result 

    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0: 
            return list(range(n))

        sec_rtol = [0] * n 
        for i in range(n-2, -1, -1): 
            sec_rtol[i] = security[i] - security[i+1]
        if all(x == 0 for x in sec_rtol): 
            return list(range(time, n-time))

        sec_ltor = [0] * n
        for i in range(1, n): 
            sec_ltor[i] = security[i] - security[i-1]

        rtol_val = self.getInflection(sec_rtol, reverse=True)
        ltor_val = self.getInflection(sec_ltor)

        result = []
        for i in range(time, n-time): 
            if i - rtol_val[i] - 1 >= time and ltor_val[i] - i - 1 >= time: 
                result.append(i)
                
        return result 

if __name__ == "__main__": 
    s = Solution()
    
    security = [5,3,3,3,5,6,2]
    time = 2
    result = s.goodDaysToRobBank(security, time)
    assert result == [2,3]

    security = [1,2,3,4]
    time = 1 
    result = s.goodDaysToRobBank(security, time)
    assert result == []

    security = [1,1,1,1,1]
    time = 0
    result = s.goodDaysToRobBank(security, time)
    assert result == [0,1,2,3,4]

    security = [4,3,2,1]
    time = 1
    result = s.goodDaysToRobBank(security, time)
    assert result == []

    security = [1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8]
    time = 2
    result = s.goodDaysToRobBank(security, time)
    assert result == [5,10,14]

    security = [2,4,0,5,5]
    time = 1
    result = s.goodDaysToRobBank(security, time)
    assert result == [2]

    security = [2,1,1,0]
    time = 1
    result = s.goodDaysToRobBank(security, time)
    assert result == [1]