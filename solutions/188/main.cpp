/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov 25 14:51:42 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        // check input
        if (prices.size() == 0) return 0;
        // dp table
        vector<vector<int>> dp(prices.size(), vector<int>(2*k+1, 0));
        // initialize
        for (int i = 1; i < 2*k+1; i+=2) dp[0][i] = -prices[0];
        // traverse table
        for (int i = 1; i < prices.size(); ++i) {
            for (int j = 0; j < 2*k+1; ++j) {
                if (j == 0) dp[i][0] = dp[i-1][0];
                else if (j % 2 == 1) {
                    dp[i][j] = max(dp[i-1][j-1]-prices[i], dp[i-1][j]);
                }
                else {
                    dp[i][j] = max(dp[i-1][j-1]+prices[i], dp[i-1][j]);
                }
            }
        }
        return dp[prices.size()-1][2*k];
    }
};

TEST(Test188, SimpleTest) {
    const int k = 2; 
    vector<int> prices{
        3,2,6,5,0,3
    };
    Solution s; 
    EXPECT_EQ(s.maxProfit(k, prices), 7);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
