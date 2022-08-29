from typing import * 

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0]*(2*n) 
        left, right = 0, n
        for i in range(0, 2*n-1, 2):
            res[i] = nums[left]
            res[i+1] = nums[right]
            left += 1 
            right += 1 
        return res 

if __name__ == "__main__": 
    s = Solution()

    # nums = [2,5,1,3,4,7]
    # n = 3
    # assert s.shuffle(nums, n) == [2,3,5,4,1,7] 

    nums = [1,2,3,4,4,3,2,1]
    n = 4
    assert s.shuffle(nums, n) == [1,4,2,3,3,2,4,1]