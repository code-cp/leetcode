/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov 23 15:54:23 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <math.h>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int numSquares(int n) {
        // dp table
        vector<int> dp(n+1, INT_MAX);
        int num = sqrt(n);
        vector<int> nums;
        for (int i = 1; i <= num; ++i)
            nums.push_back(i*i);
        // initialize
        dp[0] = 0;
        for (int i = 0; i < n+1; ++i) {
            for (int j = 0; j < nums.size(); ++j) {
                if (i >= nums[j])
                    dp[i] = min(dp[i], dp[i-nums[j]] + 1);
            }
        }
        return dp[n];
    }
};

TEST(Test279, SimpleTest) {
    const int n = 12; 
    Solution s; 
    EXPECT_EQ(s.numSquares(n), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
