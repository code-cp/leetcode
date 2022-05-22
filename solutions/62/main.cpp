/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov 11 08:16:54 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0));
        // initialize
        for (int i = 0; i < m; ++i) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; ++j) {
            dp[0][j] = 1;
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};

TEST(Test62, SimpleTest) {
    const int m = 3; 
    const int n = 7; 
    Solution s; 
    EXPECT_EQ(s.uniquePaths(m, n), 28);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
