from typing import * 

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def calApple(n): 
            # https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/solutions/908396/shou-ji-zu-gou-ping-guo-de-zui-xiao-hua-1rjsw/?envType=daily-question&envId=2023-12-24
            # Sn​=2n(n+1)(2n+1)
            return 2*(2*n+1)*n*(n+1)
        
        # 1e5 ^ 3 = 1e15  
        left, right = 1, 1e5
        while left <= right: 
            mid = ((right - left) // 2) + left 
            if calApple(mid) < neededApples:
                left = mid + 1 
            else: 
                right = mid - 1 
        
        # NOTE, n is half the length of square 
        return int(left) * 8  
                