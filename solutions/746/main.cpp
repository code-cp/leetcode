/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 10 14:59:52 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        const int n = cost.size();
        vector<int> dp(n+1, 0);
        dp[0] = cost[0];
        dp[1] = cost[1];
        for (int i = 2; i < n; ++i) {
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]);
        }
        dp[n] = min(dp[n-1], dp[n-2]);
        return dp[n];
    }
};

TEST(Test746, SimpleTest) {
    vector<int> cost{
        1,100,1,1,1,100,1,1,100,1
    };
    Solution s; 
    int result = s.minCostClimbingStairs(cost);
    EXPECT_EQ(result, 6);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
