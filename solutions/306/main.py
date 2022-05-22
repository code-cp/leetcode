from typing import List 

class Solution:
    def __init__(self):
        self.nums = []
    @staticmethod
    def checkNum(nStr):
        if nStr[0] == "0" and len(nStr) > 1:
            return False
        return True
    def backtracking(self, num, curStart):
        # base case
        if len(self.nums) >= 3:
            if self.nums[-1] != self.nums[-2] + self.nums[-3]:
                return False
            elif curStart == len(num):
                return True
        # backtracking
        for curEnd in range(curStart, len(num)):
            curStr = num[curStart:curEnd+1]
            if not self.checkNum(curStr):
                continue
            self.nums.append(int(curStr))
            if self.backtracking(num, curEnd+1):
                return True
            self.nums.pop()
        return False
    def isAdditiveNumber(self, num: str) -> bool:
        return self.backtracking(num, 0)

if __name__ == "__main__": 
    num = "112358"
    s = Solution()
    assert s.isAdditiveNumber(num)
