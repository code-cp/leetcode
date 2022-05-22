from typing import List 

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        st = []
        st.append(0)
        for i in range(1, len(height)):
            if height[st[-1]] > height[i]:
                st.append(i)
            elif height[st[-1]] == height[i]:
                st[-1] = i
            else:
                while len(st) > 0 and height[st[-1]] < height[i]:
                    mid = height[st[-1]]
                    st.pop()
                    if len(st) > 0:
                        w = i - st[-1] - 1
                        h = min(height[i], height[st[-1]])
                        result += w * (h - mid)
            st.append(i)
        return result

if __name__ == "__main__": 
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution()
    assert s.trap(height) == 6
