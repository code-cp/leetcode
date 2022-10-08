from typing import * 

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        idx1, idx2 = list(range(n)), list(range(n))
        idx1.sort(key=lambda x: nums1[x])
        idx2.sort(key=lambda x: nums2[x])

        ans = [0] * n
        left, right = 0, n - 1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ans[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ans[idx2[right]] = nums1[idx1[i]]
                right -= 1
        
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/advantage-shuffle/solution/you-shi-xi-pai-by-leetcode-solution-sqsf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__": 
    s = Solution()

    nums1 = [2,0,4,1,2]
    nums2 = [1,3,0,0,2]
    assert s.advantageCount(nums1, nums2) == [2,0,2,1,4]
    # official solution [2,0,1,2,4]

    nums1 = [12,24,8,32]
    nums2 = [13,25,32,11]
    assert s.advantageCount(nums1, nums2) == [24,32,8,12]

    nums1 = [2,7,11,15]
    nums2 = [1,10,4,11]
    assert s.advantageCount(nums1, nums2) == [2,11,7,15]
