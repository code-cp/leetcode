from typing import * 

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        res = []
        for (start, end) in zip(l, r): 
            numbers = sorted(nums[start:end+1])
            m = len(numbers) 
            flag = False 
            for i in range(1, m):
                if numbers[i]-numbers[i-1] != numbers[1]-numbers[0]: 
                    flag = False 
                    break 
                else: 
                    flag = True 
            res.append(flag)
        return res 
    
if __name__ == "__main__": 
    s = Solution() 
    
    nums = [4,6,5,9,3,7]
    l = [0,0,2]
    r = [2,3,5]
    assert s.checkArithmeticSubarrays(nums, l, r) == [True,False,True]
                
            