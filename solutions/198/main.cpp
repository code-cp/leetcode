/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 24 10:32:28 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int rob(vector<int>& nums) {
        // check input
        if (nums.size() == 1) return nums[0];
        // dp table
        vector<int> dp(nums.size(), 0);
        // initialize
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size(); ++i) {
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]);
        }
        return dp[nums.size()-1];
    }
};

TEST(Test198, SimpleTest) {
    vector<int> nums{
        1,2,3,1
    };
    Solution s; 
    EXPECT_EQ(s.rob(nums), 4);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
