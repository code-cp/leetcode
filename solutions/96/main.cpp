/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov 11 10:33:41 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1, 0);
        // initialize
        dp[0] = 1;
        for (int i = 1; i <=n; ++i) {
            for (int j = 1; j <= i; ++j) {
                dp[i] += dp[j-1] * dp[i-j];
            }
        }
        return dp[n];
    }
};

TEST(Test96, SimpleTest) {
    const int n = 3; 
    Solution s; 
    EXPECT_EQ(s.numTrees(n), 5);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
