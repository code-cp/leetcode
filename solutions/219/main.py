from typing import List 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = []
        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            my_set.append(nums[i])
            if i >= k:
                my_set.pop(0)
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3 
    s = Solution()
    assert s.containsNearbyDuplicate(nums, k)
