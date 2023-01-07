from typing import * 

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        vals1 = set(nums1)
        vals2 = set(nums2)
        vals3 = set(nums3)
        res = list(vals1.intersection(vals2).union(vals1.intersection(vals3)).union(vals2.intersection(vals3)))
        return res 

if __name__ == "__main__": 
    s = Solution() 

    nums1 = [1,1,3,2]
    nums2 = [2,3]
    nums3 = [3]
    assert s.twoOutOfThree(nums1, nums2, nums3) == [2,3]