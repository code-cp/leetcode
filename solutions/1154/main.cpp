/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Dec 20 09:11:24 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 
#include <string> 

using namespace std; 

class Solution {
private:
    vector<int> months;
public:
    Solution() : months(12, 31) {
        months[1] = 28;
        months[3] = 30;
        months[5] = 30;
        months[8] = 30;
        months[10] = 30;
    }
    bool checkLeap(int year) {
        if (year % 100 == 0 && year % 4 == 0) return true;
        if (year % 4 == 0) return true;
        return false;
    }
    int dayOfYear(string date) {
        int y = stoi(date.substr(0, 4));
        int m = stoi(date.substr(5, 2));
        int d = stoi(date.substr(8, 2));
        if (checkLeap(y)) months[1]++;
        int result = 0;
        for (int i = 0; i < m-1; ++i) {
            result += months[i];
        }
        result += d;
        return result;
    }
};

TEST(Test1154, SimpleTest) {
    string date = "2019-01-09";
    Solution s; 
    EXPECT_EQ(s.dayOfYear(date), 9);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
