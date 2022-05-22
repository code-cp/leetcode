from typing import List 

class Solution:
    @staticmethod
    def replaceChar(invalidChars):
        allChars = "abcdefghijklmnopqrstuvwxyz"
        for c in allChars:
            if c in invalidChars:
                continue
            return c
    def modifyString(self, s: str) -> str:
        s = list(s)
        invalidChars = []
        if len(s) == 1:
            if s == "?":
                return self.replaceChar(invalidChars)
        for i in range(len(s)-1):
            if s[i] == "?":
                invalidChars.append(s[i+1])
                s[i] = self.replaceChar(invalidChars)
                invalidChars = [s[i]]
            else:
                invalidChars = [s[i]]
        if s[-1] == "?":
            s[-1] = self.replaceChar(invalidChars)
        return "".join(s)

if __name__ == "__main__": 
    s = "?zs"
    sol = Solution()
    assert sol.modifyString(s) == "azs"
