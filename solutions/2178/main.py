from typing import * 

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans = []
        if finalSum % 2 == 1: 
            return ans
        if finalSum == 2: 
            return [2] 
        
        calSum = lambda x: (2+x)*(x//2)//2 
        
        l, r = 4, finalSum 
        while l <= r: 
            mid = l+(r-l)//2 
            if calSum(mid) < finalSum: 
                l = mid+1
            else: 
                r = mid-1 
        
        if r % 2 == 1: 
            r -= 1 
        total = calSum(r)
        for i in range(2, r+1, 2): 
            ans.append(i)
        diff = finalSum - total
        if diff > ans[-1]:
            ans.append(diff)
        else: 
            ans[-1] += diff 
        
        return ans 
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.maximumEvenSplit(12) == [2,4,6]