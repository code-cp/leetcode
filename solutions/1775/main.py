from typing import * 

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0 
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2: 
            return res 
        if s1 < s2: 
            nums1, nums2 = nums2, nums1 
            s1, s2 = s2, s1 
        nums1.sort(reverse=True)
        nums2.sort()

        n1, n2 = len(nums1), len(nums2)
        i = j = 0 
        while i < n1 and j < n2: 
            diff1, diff2 = nums1[i]-1, 6-nums2[j]
            if s1 - s2 <= max(diff1, diff2): 
                return res + 1 
            if diff1 > diff2: 
                s1 -= diff1 
                i += 1
            else: 
                s2 += diff2 
                j += 1 
            res += 1 

        while i < n1: 
            diff1 = nums1[i]-1 
            if s1 - s2 <= diff1: 
                return res + 1 
            else: 
                s1 -= diff1 
            res += 1
            i += 1 

        while j < n2: 
            diff2 = 6-nums2[j] 
            if s1 - s2 <= diff2: 
                return res + 1 
            else: 
                s2 += diff2 
            res += 1
            j += 1 

        return -1 

if __name__ == "__main__": 
    s = Solution() 

    nums1 = [5,2,1,5,2,2,2,2,4,3,3,5]
    nums2 = [1,4,5,5,6,3,1,3,3]
    assert s.minOperations(nums1, nums2) == 1

    nums1 = [6, 6]
    nums2 = [1]
    assert s.minOperations(nums1, nums2) == 3 

    nums1 = [1,2,3,4,5,6]
    nums2 = [1,1,2,2,2,2]
    assert s.minOperations(nums1, nums2) == 3 