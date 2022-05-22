/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 22 13:42:59 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // dp table
        vector<int> dp(target+1, 0);
        // initialize
        dp[0] = 1;
        for (int i = 0; i <= target; ++i) {
            for (int j = 0; j < nums.size(); ++j) {
                if (i >= nums[j]) {
                    if (dp[i] < INT_MAX - dp[i-nums[j]])
                        dp[i] += dp[i-nums[j]];
                }
            }
        }
        return dp[target];
    }
};

TEST(Test377, SimpleTest) {
    const int target = 4; 
    vector<int> nums{
        1,2,3
    };
    Solution s; 
    EXPECT_EQ(s.combinationSum4(nums, target), 7);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
