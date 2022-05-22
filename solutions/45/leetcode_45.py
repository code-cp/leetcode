# -*- coding: utf-8 -*-
"""leetcode 45.ipynb
time complexity O(n), space complexity O(1)
"""

class Solution:

    def jump(self, nums):
        
        cur_reach = 0
        i, n = 0, len(nums) - 1 
        level = 0 
        
        while (cur_reach < n):
            level += 1
            prev_reach = cur_reach 
            while (i <= prev_reach):
                cur_reach = max(cur_reach, i + nums[i])
                i += 1 
        
        return level

s = Solution()
input_arr = [2,3,1,1,4]
print(s.jump(input_arr))