/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov 11 10:03:09 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int integerBreak(int n) {
        vector<int> dp(n+1);
        // initialize
        dp[2] = 1;
        for (int i = 3; i <= n; ++i) {
            for (int j = 1; j < i-1; ++j) {
                dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]));
            }
        }
        return dp[n];
    }
};

TEST(Test343, SimpleTest) {
    const int n = 10; 
    Solution s; 
    EXPECT_EQ(s.integerBreak(n), 36);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
