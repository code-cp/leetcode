/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 24 11:07:07 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    int helper(vector<int>& nums, int start, int end) {
        // check input
        if (start == end) return nums[start];
        // dp table
        vector<int> dp(end - start + 1, 0);
        dp[0] = nums[start];
        dp[1] = max(nums[start], nums[start+1]);
        // note, start, end are inclusive
        for (int i = start+2; i <= end; ++i) {
            dp[i-start] = max(dp[i-start-1], dp[i-start-2] + nums[i]);
        }
        return dp[end - start];
    }
public:
    int rob(vector<int>& nums) {
        // check input
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);
        int profit1 = helper(nums, 0, nums.size()-2);
        int profit2 = helper(nums, 1, nums.size()-1);
        return max(profit1, profit2);
    }
};

TEST(Test213, SimpleTest) {
    vector<int> nums{
        2,3,2
    };
    Solution s; 
    EXPECT_EQ(s.rob(nums), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
