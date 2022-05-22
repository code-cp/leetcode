/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Jan 15 09:25:52 2022
> Description:   
 ************************************************************************/
#include <gtest/gtest.h> 

using namespace std;

class Solution {
public:
    int totalMoney(int n) {
        int result = 0;
        int deposit = 0;
        int last_deposit = 0;
        int last_monday = 0;
        int cur_day = 0;

        while (cur_day != n) {
            cur_day++;
            if (cur_day % 7 == 1) {
                deposit = last_monday + 1;
                last_monday = deposit;
            }
            else {
                deposit = last_deposit + 1;
            }
            result += deposit;
            last_deposit = deposit;
        }
        return result;
    }
};

TEST(Test1716, SimpleTest) {
    const int n = 20;
    Solution s; 
    EXPECT_EQ(s.totalMoney(n), 96);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
