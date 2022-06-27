from typing import * 

# 一个较长的字符串肯定不会是一个较短字符串的子序列，那么只需要从长到短判断，每一个字符串是否为其他长度不小于它的字符串的子序列就行了
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubSeq(w1, w2): 
            if len(w1) > len(w2): 
                return False 
            l, r = 0, 0 
            while l < len(w1) and r < len(w2): 
                if w1[l] == w2[r]: 
                    l += 1 
                r += 1 
            return l == len(w1) 
        strs.sort(key = len, reverse = True)
        for i, w1 in enumerate(strs): 
            if all(not isSubSeq(w1, w2) for j, w2 in enumerate(strs) if i != j): 
                return len(w1)
        return -1 

if __name__ == "__main__": 
    s = Solution()

    assert s.findLUSlength(["aba","cdc","eae"]) == 3 
    assert s.findLUSlength(["aaa","aaa","aa"]) == -1 