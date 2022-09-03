from typing import * 
# 贪心
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 0 
        i = 0 
        while i < len(pairs): 
            j = i+1
            while j < len(pairs) and pairs[j][0] <= pairs[i][1]:
                j += 1 
            i = j 
            res += 1 
        return res 

if __name__ == "__main__": 
    s = Solution()

    pairs = [[1,2],[2,3],[3,4]]
    assert s.findLongestChain(pairs) == 2 

    # pairs = [[1,2],[7,8],[4,5]]
    # assert s.findLongestChain(pairs) == 3 