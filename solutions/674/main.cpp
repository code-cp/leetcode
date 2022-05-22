/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov 26 11:13:52 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        // dp table
        // initialize
        vector<int> dp(nums.size(), 1);
        // travese dp table
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i-1]) dp[i] = dp[i-1] + 1;
        }
        return *max_element(dp.begin(), dp.end());
    }
};

TEST(Test674, SimpleTest) {
    vector<int> nums{
        1,3,5,4,7
    };
    Solution s; 
    EXPECT_EQ(s.findLengthOfLCIS(nums), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
