from typing import * 

from collections import defaultdict 
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mask = defaultdict(int)
        for i, nums in enumerate((nums1, nums2, nums3)):
            for x in nums:
                mask[x] |= 1 << i

        # v & (v - 1)解释 1.三个数组出现：111&110=110(√) 2.两个数组出现：110&101=100(√),101&100=100(√),011&010=010(√) 3.一个数组出现：100&011=000(×),010&001=000(×),001&000=000(×),
        return [x for x, m in mask.items() if m & (m - 1)]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/two-out-of-three/solutions/2034884/zhi-shao-zai-liang-ge-shu-zu-zhong-chu-x-5131/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__": 
    s = Solution() 

    nums1 = [1,1,3,2]
    nums2 = [2,3]
    nums3 = [3]
    assert s.twoOutOfThree(nums1, nums2, nums3) == [2,3]