from typing import * 

# ref https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/solution/by-fuxuemingzhu-dko5/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        num_len = len(nums)
        # need to use abs to ignore the sign 
        for i in range(num_len): 
            if nums[abs(nums[i])-1] < 0: 
                res.append(abs(nums[i])) 
            nums[abs(nums[i])-1] *= -1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    # nums = [1,1,2]
    # result = s.findDuplicates(nums)
    # assert result == [1] 

    nums = [4,3,2,7,8,2,3,1]
    result = s.findDuplicates(nums)
    assert result == [2,3] 

