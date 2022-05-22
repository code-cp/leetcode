from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                # if temp is not larger, just push into stack
                stack.append(i)
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    # if temp is larger, update the index
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return ans

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    s = Solution()
    print(s.dailyTemperatures(temperatures))
