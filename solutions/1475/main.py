from typing import * 

from collections import deque 
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = deque()
        # put 0 at bottom so no need to check it's empty
        stack.append(0)

        n = len(prices)
        prices = prices[::-1]
        ans = [] 

        for p in prices: 
            while stack[-1] > p:
                stack.pop()

            ans.append(p-stack[-1])
            stack.append(p)

        ans = ans[::-1]
        return ans 

if __name__ == "__main__": 
    s = Solution()

    prices = [8,4,6,2,3]
    assert s.finalPrices(prices) == [4,2,4,2,3]



