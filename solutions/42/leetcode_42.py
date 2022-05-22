# -*- coding: utf-8 -*-
"""leetcode 42.ipynb
dynamic programming, time O(n), space O(n)
"""

class Solution:
    def trap(self, height):
        
        ret = 0 
        
        # check input 
        if len(height) == 0:
            return ret  
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        
        for i in range(len(height)):
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(left_max[i-1], height[i])

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                right_max[i] = height[i]
            else:
                right_max[i] = max(right_max[i+1], height[i])
        
        for i in range(len(height)):
            ret += (min(left_max[i], right_max[i]) - height[i])

        return ret

if __name__ == "__main__":
    s = Solution()
    input = [0,1,0,2]
    assert s.trap(input) == 1