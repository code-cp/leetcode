/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 22 10:12:23 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // dp table
        vector<int> dp(amount+1, 0);
        // initialize
        dp[0] = 1;

        for (int i = 0; i < coins.size(); ++i) {
            for (int j = coins[i]; j <= amount; ++j) {
                dp[j] += dp[j-coins[i]];
            }
        }

        return dp[amount];
    }
};

TEST(Test518, SimpleTest) {
    const int amount = 5; 
    vector<int> coins{
        1,2,5
    };
    Solution s; 
    EXPECT_EQ(s.change(amount, coins), 4);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
