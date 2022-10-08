from typing import * 

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        res = [-1] * len(nums1) 

        # find the first one larger than nums2 
        def bsearch(target): 
            left, right = 0, len(nums1)-1 
            while left <= right: 
                mid = (right-left)//2 + left 
                if nums1[mid] <= target: 
                    left = mid + 1 
                else: 
                    right = mid - 1 
            return left 

        for i, n2 in enumerate(nums2): 
            n1 = bsearch(n2)
            if n1 < len(nums1):
                res[i] = nums1[n1]
                del nums1[n1]
                # cannot set nums1[n1] = -1, this will destroy the order 
        
        j = 0 
        for i, r in enumerate(res): 
            if res[i] == -1:
                res[i] = nums1[j]
                j += 1 

        return res 

if __name__ == "__main__": 
    s = Solution()

    # nums1 = [2,0,4,1,2]
    # nums2 = [1,3,0,0,2]
    # assert s.advantageCount(nums1, nums2) == [2,0,2,1,4]
    # official solution [2,0,1,2,4]
    # my solution [2,4,1,2,0]

    nums1 = [12,24,8,32]
    nums2 = [13,25,32,11]
    assert s.advantageCount(nums1, nums2) == [24,32,8,12]

    nums1 = [2,7,11,15]
    nums2 = [1,10,4,11]
    assert s.advantageCount(nums1, nums2) == [2,11,7,15]
