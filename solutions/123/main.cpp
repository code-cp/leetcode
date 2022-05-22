/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 24 16:20:44 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // dp table
        vector<vector<int>> dp(prices.size(), vector<int>(5, 0));
        // initialize
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        dp[0][2] = 0;
        dp[0][3] = -prices[0];
        dp[0][4] = 0;
        // traverse
        for (int i = 1; i < prices.size(); ++i) {
            dp[i][0] = dp[i-1][0];
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]);
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i]);
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i]);
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i]);
        }
        return max(dp[prices.size()-1][2], dp[prices.size()-1][4]);
    }
};

TEST(Test123, SimpleTest) {
    vector<int> prices{
        3,3,5,0,0,3,1,4
    };
    Solution s; 
    EXPECT_EQ(s.maxProfit(prices), 6); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
