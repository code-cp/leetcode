from typing import List 

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        # dp table
        dp = [[0] * len(nums2) for _ in range(len(nums1))]
        # initialize
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
                result = 1
        for i in range(len(nums2)):
            if nums1[0] == nums2[i]:
                dp[0][i] = 1
                result = 1
        # traverse dp table
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if result < dp[i][j]:
                    result = dp[i][j]
        return result

if __name__ == "__main__":
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    s = Solution()
    assert s.findLength(nums1, nums2) == 3
