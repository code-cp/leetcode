/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov 25 17:15:30 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // dp table
        vector<vector<int>> dp(prices.size(), vector<int>(4, 0));
        // initialize
        dp[0][3] = -prices[0];
        // traverse dp table
        for (int i = 1; i < prices.size(); ++i) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]);
            dp[i][1] = dp[i-1][3] + prices[i];
            dp[i][2] = dp[i-1][1];
            dp[i][3] = max(dp[i-1][3], max(dp[i-1][0] - prices[i], dp[i-1][2] - prices[i]));
        }
        return max(dp[prices.size()-1][0], max(dp[prices.size()-1][1], dp[prices.size()-1][2]));
    }
};

TEST(Test309, SimpleTest) {
    vector<int> prices{
        1,2,3,0,2
    };
    Solution s; 
    EXPECT_EQ(s.maxProfit(prices), 3);
}
