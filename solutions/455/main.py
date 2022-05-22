from typing import List 

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        result = 0
        cookieId = len(s)-1
        # for each kid
        for i in range(len(g)-1, -1, -1):
            if cookieId >= 0 and g[i] <= s[cookieId]:
                result += 1
                cookieId -= 1
        return result

if __name__ == "__main__":
    g = [1,2,3] 
    s = [1,1]
    mySol = Solution()
    assert mySol.findContentChildren(g, s) == 1
