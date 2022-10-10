from typing import * 

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # dp, a, b are positions for last two digits 
        # case 1: do not swap a, b 
        # case 2: swap both a, b 
        # case 3: swap a 
        # case 4: swap b 
        n = len(nums1)
        keep = [float("inf")] * n 
        swap = [float("inf")] * n 

        keep[0] = 0
        swap[0] = 1 

        for i in range(1, n): 
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]: 
                # no swapping 
                keep[i] = keep[i-1]
                # swap both 
                swap[i] = swap[i-1]+1 
            if nums2[i] > nums1[i-1] and nums1[i] > nums2[i-1]: 
                # swap b
                swap[i] = min(swap[i], keep[i-1]+1)
                # swap a 
                keep[i] = min(keep[i], swap[i-1])
        
        return min(keep[-1], swap[-1])

if __name__ == "__main__": 
    s = Solution() 

    nums1 = [1,3,5,4]
    nums2 = [1,2,3,7]
    assert s.minSwap(nums1, nums2) == 1