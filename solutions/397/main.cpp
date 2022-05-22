/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov 18 14:53:56 2021
> Description:   
 ************************************************************************/
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int integerReplacement(int n) {
        // base case
        if (n == 1) return 0;
        if (n % 2 == 0) return 1 + integerReplacement(n/2);
        // Note, n+1 may exceed int limit
        else return 2 + min(integerReplacement(n/2 + 1), integerReplacement(n/2));
    }
};

TEST(Test397, SimpleTest) {
    const int n = 8; 
    Solution s; 
    EXPECT_EQ(s.integerReplacement(8), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
