/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 13 14:55:06 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        sum = accumulate(nums.begin(), nums.end(), sum);
        if (sum % 2 == 1) return false;
        int target = sum / 2;
        // dp table
        vector<vector<int>> dp(target+1, vector<int>(nums.size(), 0));
        // initialize
        for (int i = 0; i <= target; ++i) {
            if (i >= nums[0])
                dp[i][0] = nums[0];
        }
        for (int i = 1; i <= target; ++i) {
            for (int j = 1; j < nums.size(); ++j) {
                if (i >= nums[j])
                    dp[i][j] = max(dp[i][j-1], dp[i-nums[j]][j-1] + nums[j]);
                else
                    dp[i][j] = dp[i][j-1];
            }
        }
        return dp[target][nums.size()-1] == target;
    }
};

TEST(Test416, SimpleTest) {
    vector<int> nums{
        1,5,11,5
    };
    Solution s; 
    EXPECT_TRUE(s.canPartition(nums));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
