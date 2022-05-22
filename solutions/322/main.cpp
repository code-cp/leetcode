/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov 23 15:20:35 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp table
        const int MAX = amount + 1;
        vector<int> dp(amount + 1, MAX);
        // initialize
        dp[0] = 0;
        for (int i = 0; i < amount + 1; ++i) {
            for (int j = 0; j < coins.size(); ++j) {
                // dont forget +1
                if (i >= coins[j]) dp[i] = min(dp[i], dp[i-coins[j]]+1);
            }
        }
        return dp[amount] < MAX ? dp[amount] : -1;
    }
};

TEST(Test322, SimpleTest) {
    vector<int> coins{
        1,2,5
    };
    const int amount = 11; 
    Solution s; 
    EXPECT_EQ(s.coinChange(coins, amount), 3); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
