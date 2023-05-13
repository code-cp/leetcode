from typing import * 

# ref 
# 
# https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/solutions/2266500/bu-hui-hua-jian-qing-kan-zhe-pythonjavac-c2s6/

# https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/solutions/2266591/jian-dan-bao-li-bu-xu-yao-fen-lei-tao-lu-2erb/

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base = d = 0 
        mx, mn = -float("inf"), float("inf")
        for a, b in pairwise(nums): 
            base += abs(a-b)
            mx = max(mx, min(a,b))
            mn = min(mn, max(a,b))
            # 单独考虑从0开始反转，或者到n-1结束反转的情况
            d = max(d, abs(nums[0] - b) - abs(a - b),  # i=0
                       abs(nums[-1] - a) - abs(a - b))  # j=n-1
        return base + max(d, 2 * (mx - mn))

        