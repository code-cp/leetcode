class Solution:
    def __init__(self):
        # 1971 Dec 31 is Thursday 
        self.startYear = 1971 
        self.monthDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    @staticmethod 
    def isLeapYear(year):
        if year % 100 != 0 and year % 4 == 0:
            return True 
        if year % 400 == 0: 
            return True 
        return False 
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        totalDays = 0
        for y in range(self.startYear, year): 
            totalDays += 365
            if self.isLeapYear(y):
                totalDays += 1
        for m in range(1, month): 
            totalDays += self.monthDay[m-1]
            if m == 2 and self.isLeapYear(year):
                totalDays += 1  
        totalDays += day 
        return self.weekDay[(totalDays+3)%7]
        
if __name__ == "__main__": 
    day = 3 
    month = 1
    year = 2022
    s = Solution()
    assert s.dayOfTheWeek(day, month, year) == "Monday"
