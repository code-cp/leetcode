/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Nov 14 21:57:39 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        // sanity check
        int sum = 0;
        sum = accumulate(nums.begin(), nums.end(), sum);
        if (abs(target) > sum) return 0;
        if ((sum + target) % 2 == 1) return 0;

        // dp table
        int sumTarget = (sum + target) / 2;
        vector<vector<int>> dp(sumTarget+1, vector<int>(nums.size(), 0));

        // initialize
        for (int i = 0; i < nums.size(); ++i) {
            dp[0][i] = 1;
        }
        for (int i = 0; i <= sumTarget; ++i) {
            if (i == nums[0])
                dp[i][0] += 1;
        }

        // build dp table
        for (int i = 0; i <= sumTarget; ++i) {
            for (int j = 1; j < nums.size(); ++j) {
                if (i >= nums[j])
                    dp[i][j] = dp[i][j-1] + dp[i-nums[j]][j-1];
                else
                    dp[i][j] = dp[i][j-1];
            }
        }

        return dp[sumTarget][nums.size()-1];
    }
};

TEST(Test494, SimpleTest) {
    vector<int> nums{
        1,1,1,1,1
    };
    const int target = 3; 
    Solution s; 
    EXPECT_EQ(s.findTargetSumWays(nums, target), 5);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
