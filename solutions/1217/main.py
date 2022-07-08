from typing import * 

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0 
        for p in position: 
            if p % 2 == 0: 
                even += 1 
            else: 
                odd += 1 
        return min(odd, even)

if __name__ == "__main__": 
    s = Solution()

    position = [2,2,2,3,3]
    assert s.minCostToMoveChips(position)