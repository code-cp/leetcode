from typing import * 

# https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/solutions/2270101/ni-xiang-si-wei-pythonjavacgo-by-endless-915k/

from collections import Counter
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix: 
            if row[0] == 0: 
                for i in range(len(row)): 
                    row[i] ^= 1 
            cnt[tuple(row)] += 1 
        return max(cnt.values())