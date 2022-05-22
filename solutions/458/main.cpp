/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 24 16:31:50 2021
> Description:   
 ************************************************************************/
#include <math.h> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    int intlog(double base, double x) {
        return ceil(log(x) / log(base));
    }
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int base = minutesToTest / minutesToDie + 1;
        return intlog(base, buckets);
    }
};

TEST(Test458, SimpleTest) {
    const int buckets = 1000; 
    const int minutesToDie = 15; 
    const int minutesToTest = 60; 
    Solution s; 
    EXPECT_EQ(s.poorPigs(buckets, minutesToDie, minutesToTest), 5);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
