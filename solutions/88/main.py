from typing import * 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = m+n-1
        i, j = m+n-1, n-1 
        while i >= n and j >= 0: 
            if nums2[j] > nums1[i-n]:
                nums1[cur] = nums2[j]
                j -= 1 
            else: 
                nums1[cur] = nums1[i-n]
                i -= 1 
            cur -= 1 
        
        while j >= 0:
            nums1[cur] = nums2[j]
            cur -= 1 
            j -= 1 
            
        return None
            
if __name__ == "__main__": 
    s = Solution()
    
    s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
             
            