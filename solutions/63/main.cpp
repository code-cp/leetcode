/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov 11 09:13:28 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        // initialize
        for (int i = 0; i < n; ++i) {
            if (obstacleGrid[0][i] == 1) break;
            else dp[0][i] = 1;
        }
        for (int j = 0; j < m; ++j) {
            if (obstacleGrid[j][0] == 1) break;
            else dp[j][0] = 1;
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) dp[i][j] = 0;
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};

TEST(Test63, SimpleTest) {
    vector<vector<int>> obstacleGrid{
        {0,0,0}, {0,1,0}, {0,0,0}
    };
    Solution s; 
    EXPECT_EQ(s.uniquePathsWithObstacles(obstacleGrid), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
