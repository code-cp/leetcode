from typing import * 

class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for op in operations: 
            change = gem[op[0]] // 2 
            gem[op[0]] -= change 
            gem[op[1]] += change
            
        return max(gem) - min(gem)
            