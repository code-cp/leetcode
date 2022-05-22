from typing import List 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0

        heights.insert(0, 0)
        heights.append(0)

        stack = []
        stack.append(0)
        for i in range(1, len(heights)):
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            elif heights[stack[-1]] == heights[i]:
                stack[-1] = i
            else:
                while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                    mid = heights[stack[-1]]
                    stack.pop()
                    if len(stack) > 0:
                        left = stack[-1]
                        w = i - left - 1
                        result = max(result, w * mid)
            stack.append(i)
        return result

if __name__ == "__main__": 
    heights = [2,1,5,6,2,3]
    s = Solution()
    assert s.largestRectangleArea(heights) == 10
