from typing import * 

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        m, n = len(nums1), len(nums2) 
        while i < m and j < n: 
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i += 1 
                j += 1 
            elif nums1[i] < nums2[j]:
                res.append([nums1[i][0], nums1[i][1]])
                i += 1 
            else: 
                res.append([nums2[j][0], nums2[j][1]])
                j += 1

        while i < m: 
            res.append([nums1[i][0], nums1[i][1]])
            i += 1 

        while j < n: 
            res.append([nums2[j][0], nums2[j][1]])
            j += 1 

        return res 

if __name__ == "__main__": 
    s = Solution() 

    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    assert s.mergeArrays(nums1, nums2) == [[1,6],[2,3],[3,2],[4,6]]


