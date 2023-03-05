from typing import * 

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:

        def getFactors(num): 
            res = []
            if num <= 1: 
                return res 
            for i in range(2, int(num**0.5)+1):
                if num % i == 0: 
                    res.append(i) 
                    res.append(num//i) 
            if len(res) == 0: 
                res.append(num) 
            return res 

        n = len(nums)

        prefix = []
        factors = set()
        for i in range(n-1): 
            f = getFactors(nums[i])
            f = set(f)
            factors |= f
            prefix.append(factors.copy())

        suffix = []
        factors = set()
        for i in range(n-1, 0, -1): 
            f = getFactors(nums[i])
            f = set(f)
            factors |= f 
            suffix.append(factors.copy())

        for i in range(n-1): 
            pre = prefix[i]
            suf = suffix[n-2-i]
            if len(pre.intersection(suf)) == 0:
                return i 

        return -1 


if __name__ == "__main__": 
    s = Solution() 

    nums = [4,7,15,8,3,5]
    assert s.findValidSplit(nums) == -1 

    # nums = [4,7,8,15,3,5]
    # assert s.findValidSplit(nums) == 2 

