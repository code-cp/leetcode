/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Jan  3 09:54:25 2022
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool isLeapYear(int year) {
        if (year % 100 != 0 && year % 4 == 0) return true;
        if (year % 400 == 0) return true;
        return false;
    }
    string dayOfTheWeek(int day, int month, int year) {
        vector<int> monthDay{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        vector<string> weekDay{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
        int totalDay = 0;
        for (int y = 1971; y < year; y++) {
            totalDay += 365;
            if (isLeapYear(y)) totalDay++;
        }
        for (int m = 1; m < month; m++) {
            totalDay += monthDay[m-1];
            if (m == 2 && isLeapYear(year)) totalDay++;
        }
        totalDay += day;
        return weekDay[(totalDay+3)%7];
    }
};

TEST(Test1185, SimpleTest) {
    Solution s; 
    int day = 3, month = 1, year = 2022; 
    EXPECT_EQ(s.dayOfTheWeek(day, month, year), "Monday");
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
