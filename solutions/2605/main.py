from typing import * 

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        n1 = None 
        for n in nums1: 
            if n in nums2: 
                n1 = n 
                break 
        n2 = None 
        for n in nums2: 
            if n in nums1: 
                n2 = n 
                break 
                
        if n1 is None and n2 is None:     
            minval, maxval = min(nums1[0], nums2[0]), max(nums1[0], nums2[0])
            return minval*10 + maxval 
        elif n1 is None:
            return n2 
        elif n2 is None:
            return n1 
        else: 
            return min(n1, n2)