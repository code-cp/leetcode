from typing import * 

from collections import defaultdict
import random 
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = sorted(nums)
        self.original = [i[0] for i in sorted(enumerate(nums), key=lambda x:x[1])]
        self.memo = defaultdict(list)

    def search(self, target): 
        left, right = 0, len(self.nums) - 1 
        while left <= right: 
            mid = (right - left) // 2 + left
            if self.nums[mid] == target: 
                break  
            elif self.nums[mid] < target: 
                left = mid + 1 
            else: 
                right = mid - 1 
        left = mid 
        while left > 0 and self.nums[left-1] == target: 
            left -= 1
        right = mid 
        while right < len(self.nums)-1 and self.nums[right+1] == target: 
            right += 1
        return left, right  

    def pick(self, target: int) -> int:
        if target in self.memo:
            left, right = self.memo[target]
        else: 
            left, right = self.search(target)
            self.memo[target] = [left, right]
        rand_idx = random.randint(left, right)
        ori_idx = self.original[rand_idx] 
        return ori_idx

if __name__ == "__main__": 
    s = Solution([1, 2, 3, 3, 3]) 
    assert s.pick(3) in [2, 3, 4]
    assert s.pick(1) == 0 

    
