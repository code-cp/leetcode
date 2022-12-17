from typing import * 

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(goal - sum(nums))
        res = diff // limit 
        if diff % limit != 0: 
            res += 1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    nums = [1,-1,1]
    limit = 3
    goal = -4
    assert s.minElements(nums, limit, goal) == 2 