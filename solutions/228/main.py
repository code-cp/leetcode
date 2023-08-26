from typing import * 

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                ans.append(str(num)) 
                continue 
            if num == nums[i-1] + 1:
                if ans[-1][-1] != ">":
                    ans[-1] = ans[-1]+"->"
                if i == n-1:
                    ans[-1] += str(num)
            else: 
                if ans[-1][-1] == ">": 
                    ans[-1] = ans[-1]+str(nums[i-1])
                ans.append(str(num))
        return ans 

if __name__ == '__main__':
    s = Solution()
    
    # assert s.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert s.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
                
                 