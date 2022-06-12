from typing import * 

# ref https://leetcode.cn/problems/naming-a-company/solution/by-endlesscheng-ruz8/
from collections import defaultdict 
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        group = defaultdict(int)
        for s in ideas: 
            group[s[1:]] |= 1 << (ord(s[0]) - ord('a'))
        ans = 0 
        cnt = [[0] * 26 for _ in range(26)] 
        for mask in group.values(): 
            for i in range(26): 
                if mask >> i & 1 == 0: 
                    for j in range(26): 
                        if mask >> j & 1: 
                            cnt[i][j] += 1 
                else: 
                    for j in range(26): 
                        if mask >> j & 1 == 0: 
                            ans += cnt[i][j] 
        return ans * 2 