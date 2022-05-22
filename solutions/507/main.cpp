/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Dec 31 09:52:59 2021
> Description:   
 ************************************************************************/
#include <cmath> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool checkPerfectNumber(int num) {
        // check input
        if (num == 1) return false;
        int total = 0;
        for (int i = 1; i < int(sqrt(num))+1; ++i) {
            if (num % i == 0) {
                total += i;
                if (i != 1 && i != sqrt(num))
                    total += num / i;
            }
            if (total > num) return false;
        }
        return total == num;
    }
};

TEST(Test507, SimpleTest) {
    int num = 28; 
    Solution s; 
    EXPECT_TRUE(s.checkPerfectNumber(num));
    num = 7; 
    EXPECT_FALSE(s.checkPerfectNumber(num));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
