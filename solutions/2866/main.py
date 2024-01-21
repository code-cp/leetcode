from typing import * 
from collections import deque 

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        # 在maxHeights的前后补0 
        # 保证永远有栈顶和栈底元素
        # ref leetcode 084 
        maxHeights.insert(n, 0)
        maxHeights.insert(0, 0)
        # NOTE, 这里需要更新一下n
        n = len(maxHeights)
        
        def helper(): 
            nonlocal n 
            nonlocal maxHeights 
            
            total = 0 
            arr = [0]*n 
            stack = deque()
            stack.append(0)
            
            for i in range(1, n): 
                while len(stack) > 0 and maxHeights[i] < maxHeights[stack[-1]]: 
                    # 当前的高度heights[i]比栈顶的p1高度要低
                    # 需要把p1弹出 
                    p1 = stack[-1]
                    stack.pop()
                    # 把p1改成新的栈顶p2的高度
                    p2 = stack[-1]
                    total -= (p1-p2) * maxHeights[p1] 
                # 把栈里所有高于i位置高度的建筑都变成高度i
                # 然后加上这些新增的高度
                # NOTE, 需要在heights前后补0，否则i-stack[-1]会报错
                total += (i-stack[-1]) * maxHeights[i]
                arr[i] = total
                stack.append(i)
                
            return arr 
                 
        left = helper()
        # NOTE, reverse没有返回值
        maxHeights.reverse()
        right = helper()
        right.reverse()

        maxHeights.reverse()
        res = 0 
        for i in range(n): 
            res = max(res, left[i]+right[i]-maxHeights[i])
            
        return res
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.maximumSumOfHeights([5,3,4,1,1]) == 13  