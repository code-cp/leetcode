from typing import * 

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # dp, i, j are positions for last two digits 
        # case 1: do not swap i, j
        # case 2: swap both i, j
        # case 3: swap i
        # case 4: swap j 
        # keep i means nums1[i], nums2[i] do not swap 
        # swap i means swap them 
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
        
        # use the min of keep and swap
        # this means we can either keep or swap at this position
        return min(keep[-1], swap[-1])

if __name__ == "__main__": 
    s = Solution() 

    nums1 = [1,3,5,4]
    nums2 = [1,2,3,7]
    assert s.minSwap(nums1, nums2) == 1