from typing import List 

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        empty, full = 0, numBottles
        while empty + full >= numExchange:
            # drink
            result += full
            empty += full
            full = 0
            # change
            full = empty // numExchange
            empty = empty % numExchange
        # drink
        result += full
        return result

if __name__ == "__main__": 
    numBottles = 9
    numExchange = 3
    s = Solution()
    assert s.numWaterBottles(numBottles, numExchange) == 13
