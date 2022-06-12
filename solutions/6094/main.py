from typing import * 

# ref https://leetcode.cn/problems/naming-a-company/solution/by-endlesscheng-ruz8/
from collections import defaultdict 
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        group = defaultdict(int)
        for s in ideas: 
            group[s[1:]] |= 1 << (ord(s[0]) - ord('a'))
        ans = 0 
        # 定义 \textit{cnt}[i][j]cnt[i][j] 表示组中首字母不包含 ii 但包含 jj 的组的个数。枚举每个组，统计 \textit{cnt}cnt，
        # 同时枚举该组的首字母 ii 和不在该组的首字母 jj，答案即为 \textit{cnt}[i][j]cnt[i][j] 的累加值
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