from typing import List 

class Solution:
    def __init__(self):
        self.months = {}
        for i in [1, 3, 5, 7, 8, 10, 12]:
            self.months[i] = 31
        for i in [4, 6, 9, 11]:
            self.months[i] = 30
        self.months[2] = 28
    @staticmethod
    def checkLeap(year):
        if year % 100 == 0 and year % 400 == 0:
            return True
        if year % 4 == 0:
            return True
        return False
    def dayOfYear(self, date: str) -> int:
        result = 0
        y, m, d = date.split("-")
        y, m, d = int(y), int(m), int(d)
        leap = self.checkLeap(y)
        if leap:
            self.months[2] += 1
        for i in range(1, m):
            result += self.months[i]
        result += d
        return result

if __name__ == "__main__": 
    date = "2019-01-09"
    s = Solution()
    assert s.dayOfYear(date) == 9
