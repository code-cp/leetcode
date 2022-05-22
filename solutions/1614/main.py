class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        leftP, rightP = 0, 0
        for c in s: 
            if c == "(": 
                leftP += 1 
            elif c == ")":  
                diff = leftP - rightP 
                maxDepth = max(diff, maxDepth)
                rightP += 1
        return maxDepth

if __name__ == "__main__": 
    s = "(1+(2*3)+((8)/4))+1"
    sol = Solution()
    assert sol.maxDepth(s) == 3
